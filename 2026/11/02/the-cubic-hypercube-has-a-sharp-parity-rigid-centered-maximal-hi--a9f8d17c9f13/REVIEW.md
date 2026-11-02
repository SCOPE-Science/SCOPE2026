# Scientific assessment

## Correctness — PASS

For the centered operator, every choice of one ball per vertex gives a nonnegative averaging matrix. The finite-family spectral identity in RESULT.md is exact. The exceptional zero/one-radius pattern has a \(2\)-by-\(2\) controlling Gram block \(\frac1{16}\bigl(\begin{smallmatrix}25&3\\3&1\end{smallmatrix}\bigr)\), with top eigenvalue \((13+3\sqrt{17})/16\). Its norming vector \((1,\sqrt{17}-4)\) satisfies strict active-ball inequalities. Exact integer Sylvester certificates from `verify.py` exclude all \(65,534\) other radius selections below \(317/200\), a strict gap below the winning value. Perron–Frobenius simplicity and the exhaustive strict gap prove all equality cases. The checker uses no floating point. Limit: the certificate treats only the eight-vertex cube.

## Originality — PASS, qualified

The closest full-text inspected research includes Soria–Tradacete's general finite-graph maximal work (arXiv:1410.6204, principally \(p\le1\)), González-Riquelme–Madrid's strong \(\ell^2\) constants for complete graphs and stars (arXiv:2005.03146), and the spherical hypercube maximal results of Harrow–Kolla–Schulman (arXiv:1209.4148) and Krause (arXiv:1309.4466). Spherical estimates address a pointwise larger operator but do not fix the ball norm. The matching parity lower-bound construction on \(K_{3,3}\) does not cover the diameter-three graph's additional averaging matrices. Targeted research-record and literature queries found no exact \(Q_3\) ball-norm classification. Residual risk: unpublished or unindexed equivalent tables.

## Value — PASS

The cubic cube is the first genuine three-dimensional Boolean graph and the first cube with both radius-two and radius-three candidates. The result determines the sharp Hilbert norm, proves those larger balls never improve it, and classifies a rigid parity-symmetric extremizer. Its equality with the explicit parity construction on a distinct diameter-two cubic bipartite graph is mathematically informative, not just numerical parameter matching. This is an exact natural finite invariant with a reproducible full classification; it does not claim an all-dimensions cube theorem.

Self-review: passed. Independent audit: not yet performed.
