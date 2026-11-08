# Independent mathematical audit

## correctness

PASS

For A_L=diag(L,1,1), L>1 and a 3x2 real Gaussian sketch, the orthogonal plane normal has t=n_1^2 with CDF sqrt(t). The rank-one Nyström residual N=A−nn^T/(n^T A^-1 n) gives active nonzero eigenvalues tau=[L^2(1-t)+t]/[L(1-t)+t] and 1; on the active plane preconditioned eigenvalue trace T=L+1−L(L−1)(1-t)[L^3(1-t)+t]/[L^2(1-t)+t]^2 and product D=L[L(1-t)+t]/[L^2(1-t)+t]. One eigenvalue exceeds one and the other lies below one except null endpoints, allowing comparison K_L>L by T²/D>(L+1)²/L. The exact sign factorization is negative a positive prefactor times the bracket L^5(1-t)^2−L^3t(1-t)−(L+1)t². Its unique positive ratio root yields t_c=2L²/(2L²+1+sqrt(5+4/L)); integrating the exact Haar coordinate law proves Pr(K_L>L)=1−sqrt(t_c) and asymptotic (1+sqrt5)/(4L²)+O(L^-3). A sketch rank one in dimension two gives P=I; full rank makes P proportional A, so n=3 rank2 is minimal. Independent Gaussian-sketch direct numerical samples (360) matched the threshold event and eigenvalue condition number. Finite checks corroborate only.

## originality

PASS

Best-of-knowledge comparison of exact statements and mathematical implications across relevant primary literature and Resultary; key source-access/alias risks are explicitly retained. The assessed new claim is not the background object, source algorithm, or textbook intermediate identities.

## value

PASS

Randomized Nyström preconditioning is a natural large-scale SPD solver operation. At its smallest nontrivial intermediate rank the finding gives the exact probability of an adverse condition-number event, a sharp rare-event rate and a minimal-dimensional boundary, thereby identifying a reproducible quantitative risk omitted by expectation or high-probability favorable bounds. It does not pretend to imply more Krylov iterations or numerical failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
