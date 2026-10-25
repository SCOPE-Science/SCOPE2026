# Independent mathematical audit

## correctness

PASS

For every integer n>=3 and every complex z, normalization D=n-1+|z|²>0. Weyl conjugation diagonalizes the rank-one projector Gram operator: eigenvalue n|B(a,b)|²/D², so rank counts exactly nonzero ambiguities. From v=(z,1,...,1): B(0,0)=D; B(0,b≠0)=|z|²-1; B(a≠0,0)=n-2+2Re(z); B(a≠0,b≠0)=(z-1)+(conj(z)-1)ω^(ab). For δ=z-1≠0, mixed zeros correspond to ω^(ab)= -δ/conj(δ); if not an n-th root none occur. For root ω^r and a with gcd(a,n)=d dividing r, there are d residue solutions b; φ(n/d) such nonzero a, and when r=0 exactly one b=0 for each nonzero a is discarded, yielding C_n(r). The axes and mixed index classes are disjoint; all intersections of parameter loci are therefore additive. At z=1 the n distinct modulated rays form a Fourier ONB and rank n. At z=1+it (t real nonzero), c=1 and C_n(0)=Σ_{a=1}^{n-1}(gcd(a,n)-1), vanishing iff n prime. At z=2+2i, c=(3-4i)/5 has trace 6/5; roots of unity have algebraic-integer traces, and rational algebraic integers are integral, so no n admits mixed zeros; axes are also nonzero. An independent NumPy direct projector-matrix checker matched 35 (n,z) ranks for n=3..9, and an independent exact integer count matched every ab=r fiber for n=3..14. Finite checks are corroborative, not proof of the all-n claim.

## originality

PASS

Originality is qualified and restricted to the exact ALL-integer all-complex-parameter rank function, particularly composite modulus gcd/totient zero-divisor multiplicities and simultaneous exceptional loci. Goldberger–Kang–Okoudjou already prove the Weyl ambiguity/rank equivalence. Bojarovska–Flinth supply the linear-lifting nonvanishing frame criterion. A published same-family prime-length work computes the full singular-value multiset for every complex impulse at p>=5, thereby ALREADY implying this claim on all such prime dimensions; no new credit for those cases, the root-of-unity rank criterion, or generic IC. No inspected source determines the same exact composite-order multiplicities and full complex phase stratification; older equivalent/unindexed composite results remain a risk. This is a best-of-knowledge judgment, not proof of priority.

## value

PASS

The one-coordinate perturbation of the constant cyclic window is a geometrically and experimentally natural minimal symmetry breaking. The exact rank of its n² Gabor POVM projectors, including every composite-modulus zero-divisor defect and the complex exceptional parameter geometry, is an independently useful natural tomography invariant beyond generic injectivity. The same-family prime case and general spectral tool are credited to prior work, not counted anew. Composite group arithmetic yields distinct irrecoverable matrix-direction counts (e.g. n=4 rank 15, n=6 rank 32, n=8 rank 59 at z=1+i). This is a complete motivated all-integer classification rather than an arbitrary finite slice. No claim of conditioning, SIC optimality or noise robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
