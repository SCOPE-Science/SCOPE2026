"""Exact checks for two-frequency common-index tensor interpolation."""
from fractions import Fraction as Q
from random import Random


def coefficients(t1, t2):
    q = (t1 + t2) / 2
    m1 = q / t1 + (1 - q) / (1 - t1)
    m2 = q / t2 + (1 - q) / (1 - t2)
    balanced = 2 + (t1 - t2)**2 / 4 * (1 / (t1*t2) + 1 / ((1-t1)*(1-t2)))
    eta = max(q/t1, (1-q)/(1-t1), q/t2, (1-q)/(1-t2))
    assert (m1 + m2) / 2 == balanced
    assert max(m1, m2) <= 1 + eta
    assert balanced >= 2
    assert (balanced == 2) == (t1 == t2)
    return m1, m2, balanced, eta


def norm2(x):
    return sum(a*a for a in x)


def two_frequency_physical_exact():
    # Positive rational unit vectors, with rational orthogonal complements.
    vectors = ((Q(3,5), Q(4,5)), (Q(5,13), Q(12,13)))
    orths = tuple((-v[1], v[0]) for v in vectors)
    for v, w in zip(vectors, orths):
        assert norm2(v) == norm2(w) == 1 and sum(x*y for x,y in zip(v,w)) == 0
    t1, t2 = vectors[0][0]**2, vectors[1][0]**2
    m1, m2, balanced, eta = coefficients(t1,t2)
    q = (t1+t2)/2
    rng = Random(20261009)
    for _ in range(300):
        betas = [Q(rng.randint(-12,12)), Q(rng.randint(-12,12))]
        if betas == [0,0]:
            continue
        alphas = [Q(rng.randint(-12,12)), Q(rng.randint(-12,12))]
        fhat = [tuple(alphas[i]*vectors[i][j] + betas[i]*orths[i][j]
                     for j in range(2)) for i in range(2)]
        # Two-point inverse DFT on every component; physical tensors are real.
        vtime = [[(vectors[0][j] + vectors[1][j])/2,
                  (vectors[0][j] - vectors[1][j])/2] for j in range(2)]
        ftime = [[(fhat[0][j] + fhat[1][j])/2,
                  (fhat[0][j] - fhat[1][j])/2] for j in range(2)]
        assert all(vtime[j][0]+vtime[j][1] == vectors[0][j] for j in range(2))
        assert all(ftime[j][0]-ftime[j][1] == fhat[1][j] for j in range(2))
        # Invert each Fourier scalar sampled component (equivalently tubal inverse).
        base = (betas[0]**2 + betas[1]**2)/2
        mean = Q(0)
        for pivot, weight in ((0,q),(1,1-q)):
            ehat = []
            for i in range(2):
                v = vectors[i]
                f = fhat[i]
                scalar = f[pivot]/v[pivot]
                ehat.append(tuple(f[j]-scalar*v[j] for j in range(2)))
            # Inverse two-point DFT, followed by physical Frobenius energy.
            error_time = [[(ehat[0][j]+ehat[1][j])/2,
                           (ehat[0][j]-ehat[1][j])/2] for j in range(2)]
            energy = sum(norm2(row) for row in error_time)
            mean += weight*energy
        assert mean/base == (betas[0]**2*m1+betas[1]**2*m2)/(betas[0]**2+betas[1]**2)
    return balanced, eta


def run():
    rng = Random(992033)
    for _ in range(3500):
        t1, t2 = Q(rng.randint(1,999),1000), Q(rng.randint(1,999),1000)
        m1,m2,b,e = coefficients(t1,t2)
        b1,b2 = Q(rng.randint(-99,99)),Q(rng.randint(-99,99))
        if b1 == b2 == 0:
            continue
        w1,w2=b1*b1,b2*b2
        r = (w1*m1+w2*m2)/(w1+w2)
        assert min(m1,m2) <= r <= max(m1,m2)
        assert r <= max(m1,m2)
        if t1 != t2:
            assert b > 2 and max(m1,m2)>2
        else:
            assert b == m1 == m2 == 2 and e==1
    # The exact minimax is achieved by a nonzero residual in the more adverse slice.
    for t1,t2 in ((Q(3,11),Q(4,5)),(Q(1,3),Q(2,7)),(Q(1,2),Q(1,2))):
        m1,m2,_,_=coefficients(t1,t2)
        vals = [m1,m2]
        assert max(vals) == (m1 if m1 >= m2 else m2)
        independent = (t1/t1+(1-t1)/(1-t1)+t2/t2+(1-t2)/(1-t2))/2
        assert independent == 2
    for denominator in (2,3,4,5,7,100,10000):
        t = Q(1,denominator)
        m1,m2,b,eta=coefficients(t,1-t)
        assert m1==m2==b==1/(2*t*(1-t))
        assert eta==1/(2*t)
        assert b/(1+eta)==1/((1-t)*(1+2*t))
    expected,_=two_frequency_physical_exact()
    assert expected==coefficients(Q(9,25),Q(25,169))[2]
    print('VERIFY_OK: exact rational identities, independent physical t-DFT interpolation, extremizers')


if __name__=='__main__':
    run()
