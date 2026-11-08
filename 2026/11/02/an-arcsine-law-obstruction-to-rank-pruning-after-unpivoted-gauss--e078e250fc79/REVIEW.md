# Independent mathematical audit

## correctness

PASS

For A=diag(1,c tau,0,0), c in (0,1), 0<tau<1/sqrt(2), the first accepted b=2 Gaussian sketch spans exactly the rank-two range almost surely; first unpivoted QR vector is (X,delta Y), delta=c tau. Direct orthonormal complement gives row squared norms w1^2=(X^2+delta^4 Y^2)/D, w2^2=delta^2(X^2+Y^2)/D. With Z=delta^2Y^2/D, both rows retained exactly for t<Z<1-t; Y/X Cauchy gives explicit two-arctan P0. Excluding initial premature stopping changes probability by at most 1-exp(-tau^2) using chi-square(2); therefore limit is 2 arcsin(c)/pi. SVD of already formed B recovers rank-one error delta<tau. Independently checked QR, Cauchy probability against 36,000 Gaussian samples across three tau/c cases; source MATLAB code independently read to confirm exact pruning and 4x4 cap. Sampling not infinite proof.

## originality

PASS

Smith–Do–Chen explicitly introduce blockwise Gaussian QB and pruning but describe near-optimal rank empirically. The actual unpivoted QR and row-pruning code support this algorithm-specific over-retention example. The sharp Cauchy/arcsine law is distinct from classical SVD best rank, rank-revealing QR and random pivots.

## value

PASS

The algorithm explicitly aims for near-minimal adaptive rank. A 4-by-4 rank-two example with an exactly zero residual but a nonvanishing limiting probability of an extra retained basis column gives a sharp, actionable algorithmic limitation; exact SVD reorientation of an already computed coefficient block demonstrates a cost-contained fix. This is not a generic statement that SVD optimizes rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
