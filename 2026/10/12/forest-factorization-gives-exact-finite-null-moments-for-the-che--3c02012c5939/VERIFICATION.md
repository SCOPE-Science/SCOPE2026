---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The mathematical result concerns independent row-fixed, site-equiprobable binary presence--absence randomization, not a fixed-column null.

For every pair of row sizes \(a,b\), the verifier calculates the exact law of their overlap from
\[
\Pr(X=x)=\binom ax\binom{H-a}{b-x}/\binom Hb.
\]
It derives the empirical mean and variance of the pairwise checkerboard score directly from this probability law and compares them against the falling-factorial formulas. This is checked for all integer pairs \(1\le a,b\le H\) and all \(2\le H\le12\), totaling 649 parameter cases.

In six completely enumerated heterogeneous/homogeneous row-degree systems it generates the entire Cartesian product of possible species-presence subsets, 30,665 matrices total, and compares exactly evaluated whole-matrix C-score mean and variance with the theorem. It separately checks every two-edge overlap joint distribution, including edges sharing one species; it checks full path-forest joint factorizations and the cyclic three-edge counterexample. Exact fractions are used throughout.

The case with \(H=5\) and species occupancies \((2,3,4)\) has
\[
\mathbb E[C]=\frac75,
\qquad \operatorname{Var}(C)=\frac{49}{75},
\]
verified by complete enumeration of 500 matrices.

To rerun the standalone verifier with standard Python 3:

`python3 verify_checkerboard_fe_moments.py`

The last line should be `VERIFY_OK`.

These finite checks are not presented as an infinite proof. The all-parameter correctness rests on the leaf-conditioning forest independence lemma and the exact falling-factorial moment expansion in the paper.
