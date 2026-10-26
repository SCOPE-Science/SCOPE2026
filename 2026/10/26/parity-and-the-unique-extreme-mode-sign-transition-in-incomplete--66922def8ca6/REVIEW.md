# Scientific review: extreme-mode sign parity in Lanczos exponential approximation

## Correctness — PASS
The claim is the exact-arithmetic, incomplete, polynomial symmetric Lanczos approximation applied to an entrywise positive starting vector and a positive diagonal generator. The orthogonal-polynomial/Krylov representation yields a degree-\(m-1\) Ritz interpolation polynomial. Exact Newton remainder plus the Hermite–Genocchi integral yields \(p_{m-1,t}(x)e^{tx}=1-(-1)^mH_m(t,x)\), with \(H_m(0,x)=0\), strictly increasing to infinity for \(x>\theta_m\). This proves both the all-time odd-depth sign and the sole even-depth crossing, including boundaries. Relative-error growth follows from the leading Lagrange basis coefficient. The provided Python verification reproduces finite checks of representative depths; it is not substituted for the analytic argument.

## Originality — PASS (best-knowledge, residual risk)
The closest prior statement is *The exact positivity horizon of the two-step Lanczos exponential* (2026), which covers exactly \(m=2\). Its complete mathematical presentation was inspected and its higher-depth disclaimer checked. The general Lanczos-FA background in Chen–Greenbaum–Musco–Musco (arXiv:2202.11251, 2022) was inspected in full-text sections covering Lanczos and matrix functions, without finding the extreme-mode sign parity. Related polynomial/rational Krylov background in Bergermann–Stoll (arXiv:2303.09482, 2023), Druskin (2008) bibliographic context, published-result searches, and accessible mathematical claims showed no result entailing the all-order odd/even sign law. The possibility of an earlier equivalent interpolation lemma specialized to Krylov extrapolation is the main unresolved risk. A failed search alone does not certify novelty.

## Value — PASS
The result distinguishes sign preservation from approximation accuracy across every incomplete Krylov dimension, showing an alternating parity obstruction to preserving the highest-frequency positive mode. The uniqueness and monotonic spectral ordering of crossings yield an exact, non-asymptotic failure criterion at *each even depth*, and the odd-depth error asymptotic prevents mistaking a positive coordinate for a reliable approximation. This is a natural structural extension of the known two-step phenomenon, not another isolated finite witness.

## Scope and limitations
The theorem does not claim all-coordinate positivity for odd depths, an optimal approximation, a general non-diagonal positive-semigroup theorem, or any finite-precision guarantee. Its first-public date is the February 23, 2022 arXiv record for the primary Lanczos-FA literature, not a date for the new theorem. The source paper's primary 2020 MSC classification is 65F60. Independent review and validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
