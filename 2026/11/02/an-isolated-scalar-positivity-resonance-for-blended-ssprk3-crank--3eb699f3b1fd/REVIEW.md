# Independent mathematical audit

## correctness

PASS

For the scalar application of Eq. (6), put z=-x, b=(1-theta)z and a=1+theta*z/2. The intermediate stages are a, a(1+b), a(1+b/2+b^2/4). Inserting them into the stiffly accurate last row gives a(1+b+b^2/2+b^3/6)/(1-theta*z/2); its denominator is strictly positive on x≥0. On s≥0 the cubic derivative is -[(s-1)^2+1]/2, so its positive zero is unique and simple. The rational factor also decreases strictly when theta>0. Until the first zero both factors are in [0,1]. At distinct zeros the first sign change immediately violates the requirement; at theta=0 or 1 the absent zero is at infinity and the same argument applies. At the unique coincidence, x=alpha+2, both factors change sign with nonzero derivative. Afterward their absolute values strictly increase, the cubic without bound and the rational factor to 1, so the product crosses 1 once. This also verifies that the other blends have a supremal limiting radius alpha+2, strictly below the attained maximum. Substituting y=alpha*x/(alpha+2) into R=1 and removing y=0 yields exactly the reported cubic. Exact rational interval checks independently confirm the stated decimal roundings.

## originality

PASS

The supported distinct claim is the exact positive-contractive scalar radius over all constant blends and its isolated, discontinuous maximizer. The tableau and scalar factorization are not credited as new. The strongest checked equivalent-method source uses the factorization for a different, Fourier-modulus question; the checked works do not establish the sign-coincidence extension or optimum.

## value

PASS

The radius is a natural scalar diagnostic for the published scheme. The computation exposes a non-robust optimizer where two sign switches cancel, giving a contiguous positive-contractive range of about 7.45 versus at most about 3.60 for every other blend. The sharp, discontinuous boundary matters more than an incremental estimate or a re-evaluation of the amplification factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
