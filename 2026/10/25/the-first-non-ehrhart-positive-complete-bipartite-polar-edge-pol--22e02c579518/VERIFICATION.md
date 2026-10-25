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
# Mathematical verification record

The accompanying `verify.py` uses only Python's standard library: exact integers, `fractions.Fraction`, `math.factorial`, and `itertools.product`. Execute `python3 verify.py` in a directory also containing `coefficients.csv` (the code recomputes its entries rather than trusting them). The exact line printed on success is:

`EXACT_OK classes=49 strict_positive_d_le_12=42 first_failures=1 exception=K_7_7 c1=-7184/715 direct_counts= 48`

The 49 unordered complete-bipartite part-size classes cover every dimension from one through thirteen: 42 through dimension twelve and seven at dimension thirteen. For every class, values at all consecutive integers \(0\leq n\leq d\) determine the degree-at-most-\(d\) Ehrhart polynomial because vertex integrality has been proved independently. Newton finite differences and polynomial multiplication are performed with exact rational coefficients. The program asserts strict positivity for all 42 lower-dimensional cases, then exact uniqueness of the sole nonpositive coefficient among the seven thirteen-dimensional cases.

Independently of the coefficient-sign checks, all 49 leading coefficients are tested against the proven beta-integral volume formula, and reciprocity is verified at two integer arguments. A second enumeration directly loops through the first-part integer potential assignments for 48 small \((p,q,n)\) parameter combinations; it independently matches the proven range formula. These spot checks support implementation confidence and are **not** the reason finite-dimensional coverage is exhaustive: coverage follows from the explicit 49-class loop plus exact interpolation and the separate counting proof.

Limits: The conclusion does not cover other graph families or dimensions at least fourteen. No general monotonicity or positivity beyond the cutoff is inferred. Historical priority has not been independently audited; the newest relevant full text was unavailable for comparison.
