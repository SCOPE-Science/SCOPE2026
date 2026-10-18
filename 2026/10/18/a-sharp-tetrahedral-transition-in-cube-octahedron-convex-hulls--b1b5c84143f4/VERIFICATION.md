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
# Verification and reproducibility

The exact self-contained script `verify.py` is included alongside the proof. Run `python3 verify.py` with Python 3.9 or later, without third-party packages. It must exit successfully with a line beginning `VERIFY_OK`. The script constructs all fourteen formal vertices as polynomials in the real parameter \(t\), enumerates all \(\binom{14}{4}=1001\) four-vertex subsets, and evaluates determinants by two different exact integer-polynomial expansions. It compares all eighteen complete sign-normalized determinant classes against the expected multiplicities, and tests the ten potential maximizing vertex sets for any shared triple. This validates the finite case split, not a sampling of real parameters.

The geometric proof in `RESULT.md` separately establishes the complete vertex set; the affine-in-each-corner reduction from arbitrary tetrahedra; strict dominance of the other sixteen polynomial classes over the entire open interval \(1<t<3\); and the exclusion of all nonvertex maximizers. The volume dissections establish \(\operatorname{vol}_3(P_t)=8t\) for \(t\le2\), and \(4t^2\) for \(t\ge2\). Direct differentiation of the three resulting volume-fraction branches proves the unique minimizer. These continuous and geometric assertions are not consequences of a program's mere successful exit and require the supplied analytic arguments.

No independent audit has been performed. Historical novelty depends on the named literature comparisons and retains explicitly stated residual risks.
