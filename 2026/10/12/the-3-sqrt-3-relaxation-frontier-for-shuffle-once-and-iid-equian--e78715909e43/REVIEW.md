# Independent mathematical audit

## correctness

PASS

The three unit rows form a tight frame sum u_i u_i^T=(3/2)I. Conditional IID means square norm multiplies by a(eta)=1-eta+eta^2/2 per update, hence I_K=a^(3K). Reflection symmetries conjugate all six fixed three-row epoch products; isotropic initial covariance gives S_K=(1/2)||T^K||_F^2, limiting base rho(T)^2 even at a Jordan double root. Independently multiplied exact 2x2 matrices: trT=(eta-2)(eta^2+8eta-8)/8; detT=-(eta-1)^3; discr=eta^4(eta^2+12eta-12)/64. For real eigenvalues, sign comparison reduces to eta^4(eta-2)^2(eta^2-6eta+6)Q(eta)/512, where Q(1+z)=z^2(7z^2-4z+1)+(29z^2-4z+7)>0; unique sign change eta=3-sqrt(3) on 0<eta<2. Exact eta=3/2 checks S1=473/2048<I1=125/512, S2=586697/8388608>I2=15625/262144. Endpoint eta=0,2 excluded; rate equality does not assert finite-epoch equality.

## originality

PASS

Yun-Sra-Jadbabaie 2021 explicitly use the same equiangular rank-one rows, a serious same-object precursor; their Appendix A Eq.(16) compares an operator norm of mean fixed-permutation powers to a power of a mean permutation operator, not the isotropic expected squared error under a fixed order vs IID with replacement. The precise threshold eta=3-sqrt3 and opposite eventual mean-square regimes are not implications of that comparison. General IID and 2026 high-dimensional Gaussian shuffling work likewise lack this fixed finite-dimensional objective. Best-of-knowledge, not a novelty guarantee.

## value

PASS

This is a sharp necessary-and-sufficient phase transition on a minimally sized condition-number-one tight frame, with exact finite-epoch transient reversal. It isolates a mathematically meaningful boundary showing when one-shuffle-with-fixed-order outperforms or underperforms independent row selection, rather than a minor arbitrary parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
