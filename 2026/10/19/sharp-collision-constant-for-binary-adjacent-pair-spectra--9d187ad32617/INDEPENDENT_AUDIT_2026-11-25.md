# Independent mathematical audit

## correctness

PASS

For N=n−1, A=c00 and B=c11 determine the total mixed count and δ=last−first determines the mixed-count imbalance. Thus Parseval must be applied within δ buckets, with the two same-endpoint contributions added before squaring. The transfer matrix has entries weighted by 1/2 and an additional 1/2 for the initial bit, as used in RESULT.md lines 23–35. Equality in the row triangle inequalities at a unit-modulus eigenvalue enforces λ²=1 and both diagonal phases equal to λ. Compactness and a uniform resolvent bound give exponential decay off the two torus neighborhoods, including potentially defective matrices. At the simple eigenvalue 1, lag-zero and lag-one indicator covariances give Σ=[[5,−3],[−3,5]]/16, det Σ=1/16. The endpoint-sector squared amplitudes sum to 3/8. Conjugation by diag(1,−1) and a global minus sign give the same squared weights at the other peak (one peak on the torus, not four corner peaks). The analytic expansion yields a uniform Gaussian bound and each peak integral is 4π/N before the Fourier normalization. The resulting factor is 3/(4πN), giving the claimed limit and entropy. Inspected RESULT.md, VERIFICATION.md and verify.py without executing the uploaded program. Review-side direct counting, dynamic counts and the run sum independently agree through n=16; the count there is 70,873,180. The two sum methods also agree at n=60,100,160 with nP_n≈0.2446063, 0.2421977, 0.2408783. These are finite checks only.

## originality

PASS

The same ordered linear read model, exact fiber sizes, and formulas for the count, maximum and singleton fibers are prior coverage. The distinct result supported by the checks is the evaluated aggregate second-moment asymptotic, including its endpoint and lattice normalization, and the corresponding entropy constant.

## value

PASS

The exact leading constant quantifies average two-sample confusability under the simplest nontrivial ordered-read model and fixes the additive term of its Rényi-2 entropy. It is not a class size or a uniqueness probability; the endpoint and lattice factors explain why estimates from closely related models need not predict this normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
