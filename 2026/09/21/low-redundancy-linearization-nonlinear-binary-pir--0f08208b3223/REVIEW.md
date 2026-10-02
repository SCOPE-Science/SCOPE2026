# Independent scientific review — 2026-10-01

## Final claim

If a binary \(t\)-PIR encoder maps \(\mathbb F_2^k\) bijectively onto a linear \([n,k]\) associated code with redundancy \(r=n-k\), then each inverse-label coordinate factors through a quotient of dimension at most \(\lfloor r/(t-1)\rfloor\). Hence for \(r\le3t-4\) the labeling is affine and the same recovery sets yield a linear \(t\)-PIR encoder; in particular any binary 3-PIR code of length 11 and size \(2^7\), if it exists, must have a genuinely nonlinear associated code.

## Correctness — PASS

For a fixed requested bit, each recovery set with column span \(W_s\) makes the inverse-label coordinate constant on cosets of \(W_s^\perp\), hence on the sum of these orthogonal complements. The quotient dimension is \(\dim(\cap_s W_s)\). Modding out the common intersection and using disjointness of the recovery sets gives \((t-1)d_j\le n-k=r\). When \(r\le3t-4\), every coordinate therefore factors through at most two binary variables. Because the inverse labeling is a permutation, every coordinate is balanced; every balanced Boolean function on a space of dimension at most two is affine. Thus the whole permutation is affine with invertible linear part and can be converted to a linear encoder without changing recovery sets except fixed output complements. The \((11,7)\) consequence then follows from the standard linear 3-PIR redundancy bound \(\binom r2\ge k\).

**Risk:** The threshold is only sufficient. For quotient dimension three, balanced nonlinear Boolean functions exist, so this argument stops exactly where claimed.

## Originality — PASS

The full arXiv text of Hollmann–Luhaäär explicitly distinguishes two nonlinear mechanisms—nonlinear associated code versus nonlinear encoder onto a linear code—and states the length-11, size-\(2^7\) existence problem, but it does not prove that low redundancy forces the second mechanism to be affine. It only proves special no-encoder results for Hamming codes and parameter bounds. A Resultary search found no earlier SCOPE theorem equivalent to the quotient-dimension/affine-linearization result.

**Risk:** Equivalent results may exist under Boolean-function factorization or batch-code terminology not surfaced by the searches.

## Value — PASS

The theorem answers a natural structural ambiguity emphasized by the primary PIR source: in a broad low-redundancy regime, nonlinear labeling of a linear code cannot create extra PIR power. It also strengthens the documented open \((n,k)=(11,7)\) case from “necessarily nonlinear” to “the associated code itself must be nonlinear.”

**Risk:** It does not settle whether the open \((11,7)\) code exists and makes no optimality claim for the threshold.

## Overall disposition

**PASSED**
