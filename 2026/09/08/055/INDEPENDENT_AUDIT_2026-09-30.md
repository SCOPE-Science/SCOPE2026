# Independent mathematical audit — SCOPE-20260908-055
Audit date: 2026-09-30 UTC.
Disposition: **repaired**.

## Final repaired claim
For the named quartic, the Hilbert vector is (1,6,7,6,1), the classical Hessian vanishes, WLP holds for the exhibited linear form, the displayed Betti table is correct, and the annihilator has 14 quadratic, 2 cubic, and 4 quartic minimal generators; projective dimension is 6 and regularity is 4.

## Correctness
Status: **PASS**.

The original RESULT contains one false consequence of its own displayed Betti table: beta_{1,4}=4, so the annihilator has 14 quadratic, 2 cubic, and 4 quartic minimal generators, not only 14 quadrics and 2 cubics. Fresh exact symbolic recomputation independently confirmed Hilbert vector (1,6,7,6,1), identically zero Hessian, WLP ranks 6 and 6 with minors 2 and 4, and every displayed Betti row. The repaired final claim corrects the generator sentence and slogan while retaining the verified table.

## Originality
Status: **PASS**.

Exact-object searches did not locate this quartic or its full Hilbert/WLP/Betti tuple in prior literature. The checked Perazzo papers cover the two-variable-base family and broader structural regimes but explicitly flag limits of generalization to the three-variable-base setting.

## Scientific value
Status: **PASS**.

An explicit WLP verdict and complete apolar Hilbert/Betti tuple for a concrete three-variable-base Perazzo-type quartic sits in a literature-motivated regime where broader WLP behavior is not classified by the checked sources. The exact object is a natural test point rather than an arbitrary parameter substitution.

## Limitations and residual risk
- The original package omitted the four quartic minimal generators despite displaying beta_{1,4}=4.
- The repaired claim is one named object and does not assert a family classification.
- The literature comparison retains bounded access risk because two arXiv HTML full-text fetches failed in this run.
- Full-text arXiv HTML retrieval failed during this run for two papers, so the literature comparison retains a bounded access risk; indexed scope statements and exact searches did not reveal coverage.
