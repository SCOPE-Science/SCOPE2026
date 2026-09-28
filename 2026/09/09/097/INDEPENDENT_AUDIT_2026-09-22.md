# Independent audit — SCOPE-20260909-097

## Scope
Independent review of `2026/09/09/097` at tree `c9f98049fe89a9472f3a6be48c745a5518db5542`.

## Correctness
**PASS.** The finite Brill–Noether arithmetic and the bundle argument check out. For a general genus-11 curve, the Brill–Noether thresholds used by the record are
`d1=7, d2=10, d4=13, d6=16, d12=23`. A hypothetical semistable rank-3 bundle of degree 20 with seven sections has expected Brill–Noether number `-28` and Clifford value `4`. Re-running the numerical inequalities in the proof gives the same rank-1 and rank-2 subbundle exclusions and the same quotient-section caps.

The key logical point is that the Paranjape–Ramanan determinant lemma reduces seven sections in rank three to a proper subbundle with more sections than rank unless the determinant has at least 13 sections, which would require degree at least `d12=23`. Semistability then excludes the line-subbundle case, and the rank-2 case is bounded exactly as stated.

## Originality
**PASS, with a narrow claim.** Lange–Mercat–Newstead (2012) construct rank-3 degree-20 bundles with six sections on a general genus-11 curve and explicitly leave finer rank-3 Clifford questions open; the searched rank-3 lower-bound papers do not state the specific nonexistence of a semistable `(3,20,7)` bundle. This audit does not claim a universal priority result beyond that exact cell.

## Scientific value
**PASS.** The statement closes a concrete Brill–Noether cell immediately adjacent to the known six-section Mukai example and is reusable as an exact exclusion in rank-3 Clifford-index calculations.

## Reproducibility
The audit independently recomputed the genus-11 Brill–Noether thresholds from `rho(g,r,d) >= 0`, the expected dimension, the Clifford value, and every degree/section cap used in the case split. `artifacts/verify_target.py` is consistent with these checks.

## Literature checked
- H. Lange, V. Mercat, P. E. Newstead, *On an example of Mukai*, Glasgow Math. J. 54 (2012), DOI 10.1017/S0017089511000577; arXiv:1003.4007.
- H. Lange, P. E. Newstead, *Lower bounds for Clifford indices in rank three*, Math. Proc. Camb. Phil. Soc. 150 (2011), DOI 10.1017/S0305004110000502; arXiv:0912.2618.
- H. Lange, P. E. Newstead, *On bundles of rank 3 computing Clifford indices*, Kyoto J. Math. 53 (2013), arXiv:1201.2333.

## Limitations
The originality conclusion is confined to the exact `(rank, degree, h0)=(3,20,7)` cell on a general genus-11 curve. It is not a claim that the surrounding rank-3 Clifford problem is new.
