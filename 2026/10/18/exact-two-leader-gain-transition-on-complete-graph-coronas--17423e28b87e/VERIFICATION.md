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

# Verification procedure and limits

The self-contained `verify.py` requires Python 3 and SymPy. Execute `python verify.py` from the folder containing the file. It symbolically forms the exact Schur-complement resolvent of the pinned corona Laplacian, recovers the rational objective values for all four pair orbits, and checks the exact comparison identities that prove the classification for every admissible parameter. For separate reproducibility, it builds the full \(2m\)-vertex combinatorial Laplacian from edges and directly inverts its exactly pinned rational matrix for every two-vertex leader set for \(m=3,4,5,6,7\) and \(\kappa=1/5,1,5,100\).

The program was run against its actual packaged source before acceptance; it printed successful general symbolic resolvent identities, three comparison identities, and exhaustive exact-rational pair checks for each of the five orders, finishing with `All checks PASS`. There are exactly \(4\sum_{m=3}^{7}\binom{2m}{2}=980\) direct pair/gain checks. One sample lies precisely at the tie, \(m=5,\kappa=5\). A finite test cannot certify an infinite graph family; the analytical orbit exhaustion and strict rational inequalities in `RESULT.md` do that work.

The empirical and symbolic checks do not establish research priority, independent replication, or application to unequal gains, nonunit weights, or graphs outside the specified corona family. The absolute physical steady-state variance is one-half the objective used in the theorem.
