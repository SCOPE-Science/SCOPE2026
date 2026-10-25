# Independent mathematical audit

## correctness

PASS

The base-b=n-1 signed residue-sum vector satisfies S(bx)=B S(x), with B_(r,s)=a_(r+s mod n), a_d=(-1)^d for d<=n-2 and a_(n-1)=0. For n odd Fourier characters v_z (z^n=1) satisfy B v_z=A(z) v_(z^-1) with A(z)=sum_{d=0}^{n-2}(-z)^d; hence B² has eigenvalue 0 for z=1 and -((z-1)/(z+1))² otherwise. The odd-binomial polynomial P_n(Y)=sum_{j=0}^{(n-1)/2}(-1)^j binom(n,2j+1)Y^j vanishes on all nonconstant eigenvalues by ((1+w)^n-(1-w)^n)/(2w) and equals n at 0. Consequently P_n(B²)=J_n, and multiplying S(x) proves the conjectured all-residue relation for every odd n>=3 and integer x>=0. Sum of digit signs cancels in consecutive pairs since b even, yielding the parity endpoint. Independently verified exact integer P_n(B²)=J_n for n=3,5,7,9.

## originality

PASS

Best-of-knowledge original combined claim, not merely its known premises: Prior spectral roots and digit-step equations are key premises and must not be rebranded as new. Merely possessing those two statements does not entail the full conjecture without demonstrating that the polynomial evaluated on the exact digit-transfer matrix equals J_n; this is the supplied algebraic link. Broader works and residual risks below qualify priority.

## value

PASS

Resolves the explicit all-residue conjecture posed in 2012 uniformly across infinitely many odd moduli and all integer cutoffs, with a rank-one matrix projector explaining the cancellation. The spectral polynomial itself is credited as prior; the new structural bridge is mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
