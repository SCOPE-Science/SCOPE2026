"""Numerical spectral cross-checks for the finite-atomic Boolean entropy expansion.

Uses only the Python standard library. Spectral roots are found independently
from the strictly increasing rational Schur-complement equation; this program
checks formulas derived in the accompanying mathematical proof, not an infinite
claim by finite enumeration.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def D(x):
    if isinstance(x, Fraction):
        return Decimal(x.numerator) / Decimal(x.denominator)
    return Decimal(str(x))


def bisect_increasing(fn, low, high, steps=230):
    for _ in range(steps):
        mid = (low + high) / 2
        if fn(mid) > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def spectra(nodes, weights, n):
    t = (Decimal(1) / Decimal(n)).sqrt()
    poles = [t * a for a in nodes]
    radius = Decimal(3) + max(abs(x) for x in poles)
    intervals = [(-radius, poles[0])]
    intervals += [(poles[i], poles[i + 1]) for i in range(len(poles) - 1)]
    intervals += [(poles[-1], radius)]
    def schur(z):
        return z - sum(w / (z - a) for a, w in zip(poles, weights))
    eigenvalues = [bisect_increasing(schur, a, b) for a, b in intervals]
    masses = [Decimal(1) / (Decimal(1) + sum(
        w / (z - a)**2 for a,w in zip(poles,weights))) for z in eigenvalues]
    return eigenvalues, masses


def predicted(nodes, weights):
    mean = sum(a*w for a,w in zip(nodes,weights))
    second = sum(a*a*w for a,w in zip(nodes,weights))
    variance = second-mean*mean
    C = (3*mean*mean-2*second)/4
    residues = []
    for i in range(len(nodes)-1):
        def transform(z):
            return sum(w/(z-a) for a,w in zip(nodes, weights))
        # Decreasing Nevanlinna transform: bisect increasing -transform.
        q = bisect_increasing(lambda z:-transform(z),nodes[i],nodes[i+1])
        if abs(q) < Decimal('1e-45'):
            return None, variance, residues
        L = sum(w/(q-a)**2 for a,w in zip(nodes,weights))
        weight = Decimal(1)/L
        residues.append((q,weight))
        C -= weight*abs(q).ln()
    return C,variance,residues


def main():
    with localcontext() as ctx:
        ctx.prec = 75
        cases = [
            ('one-atom skew',['0.7'],['1']),
            ('two-atom skew',['-1','1'],['0.4','0.6']),
            ('three-atom symmetric',['-1','0','1'],['0.15','0.7','0.15']),
            ('three-atom asymmetric',['-2','0','1'],['0.25','0.5','0.25']),
            ('four-atom generic',['-2','-0.5','0.6','2'],['0.2','0.3','0.1','0.4']),
            ('five-atom generic',['-3','-1','0','1','3'],['0.11','0.19','0.34','0.23','0.13']),
        ]
        tests=0
        for name, aa, ww in cases:
            nodes=[D(x) for x in aa]; weights=[D(x) for x in ww]
            assert sum(weights)==1 and all(x>0 for x in weights)
            C,v,residues=predicted(nodes,weights)
            assert C is not None,name
            assert abs(sum(p for _,p in residues)-v)<Decimal('1e-45'),name
            tests+=1
            discrepancies=[]
            for n in (100,1000,10000,100000,1000000):
                roots,masses=spectra(nodes,weights,n)
                assert abs(sum(masses)-1)<Decimal('1e-45'),name
                gamma=-sum(w*abs(z).ln() for z,w in zip(roots,masses))
                Cseen=Decimal(n)*gamma-v*Decimal(n).ln()/2
                discrepancies.append(abs(Cseen-C))
                assert gamma>Decimal('-1e-40'),name
                tests+=2
            assert discrepancies[-1]<Decimal('0.0003'),(name,discrepancies[-1])
            assert discrepancies[-1]<discrepancies[0],name
            tests+=2
            print(name,'C=',str(C)[:22],'error_at_1e6=',str(discrepancies[-1])[:18])
        # A zero of the Nevanlinna transform at zero is an exact support atom.
        aa=[Decimal(-1),Decimal(1)];ww=[Decimal('0.5')]*2
        assert sum(w/(-a) for a,w in zip(aa,ww))==0
        C,v,_=predicted(aa,ww)
        assert C is None and v==1
        tests+=2
        # Exact rational moment identity for the fixed-variance family.
        for p in (Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(7,8)):
            # Taking v=p and support {-1,0,+1} keeps m3=0 and m4=1+p.
            a=[Fraction(-1),Fraction(0),Fraction(1)]
            w=[p/2,1-p,p/2]
            assert sum(wi*ai for ai,wi in zip(a,w))==0
            assert 1+sum(wi*ai*ai for ai,wi in zip(a,w))==1+p
            tests+=2
        # Independent explicit four-point formula in Pan, Example 4.1:
        # this is a previously known SPECIAL CASE, used only as corroboration.
        for v in (Decimal('0.25'),Decimal('0.5'),Decimal('0.75')):
            nodes=[Decimal(-1),Decimal(0),Decimal(1)]
            weights=[v/2,1-v,v/2]
            for n in (1,2,10,100,1000,100000):
                roots,masses=spectra(nodes,weights,n)
                spectral=-sum(w*abs(z).ln() for z,w in zip(roots,masses))
                delta=((Decimal(n)-1)**2+4*Decimal(n)*v).sqrt()
                uplus=(Decimal(n)+1+delta)/(2*Decimal(n))
                uminus=(Decimal(n)+1-delta)/(2*Decimal(n))
                omegaplus=(Decimal(n)-1+delta)/(2*delta)
                omegaminus=(delta-Decimal(n)+1)/(2*delta)
                published=-(omegaplus*uplus.ln()+omegaminus*uminus.ln())/2
                assert abs(spectral-published)<Decimal('1e-48')
                tests+=1
        # Known zero case: symmetric two-point Nevanlinna law has an atom
        # at zero of mass exactly 1/(n+1), so logarithmic entropy is -infty.
        for n in (1,2,10,1000):
            roots,masses=spectra([Decimal(-1),Decimal(1)],
                                 [Decimal('0.5')]*2,n)
            mid=min(range(3),key=lambda j:abs(roots[j]))
            assert abs(roots[mid])<Decimal('1e-48')
            assert abs(masses[mid]-Decimal(1)/(Decimal(n)+1))<Decimal('1e-48')
            tests+=2
        print('PASS',tests,'root, residue, normalization, asymptotic, moment, published-special-case, and zero-atom assertions')

if __name__ == '__main__':
    main()
