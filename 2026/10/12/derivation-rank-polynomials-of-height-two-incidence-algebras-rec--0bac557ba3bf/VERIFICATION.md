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

# Reproducibility and validation scope

Execute `python3 verify.py` from the directory containing this file. It requires only Python 3 and standard-library modules, with no private data or network access. The script constructs the incidence-algebra derivation matrix from each choice of the two coefficients per edge, computes its linear-algebra rank by finite-field Gaussian elimination, and compares the full rank-frequency distribution against the graph-component formula. The implemented exhaustive fields are the prime fields of orders two and three; the theorem extends to nonprime prime powers by the field-independent proof, not by an exhaustive extension-field experiment.

Checks performed: full derivation-parameter enumeration on the four-cycle for \(q=2\) and \(q=3\); six-cycle for \(q=2\); a five-vertex tree for \(q=2\) and \(q=3\); four-cycle with one bridge and \(K_{2,3}\) for \(q=2\). The code independently solves the full Leibniz linear constraints for all linear operators on the four-cycle algebra over both tested fields, obtaining the expected derivation-space dimension eight. It compares all ranks to the three-state edge formula. Additional graph-state checks verify the shortest-cycle coefficient on a four-cycle, six-cycle, \(K_{2,3}\), \(K_{3,3}\), and a four-cycle with bridge, and verify no coefficient deviation for a tree. The final script run printed `VERIFY_OK` and the expected girth lines, with no failed assertions.

Sample rank frequencies in ascending order are \((1,12,54,109,80)\) for the four-cycle at \(q=2\), \((1,32,384,2064,4080)\) at \(q=3\), and \((1,18,135,543,1231,1464,704)\) for \(K_{2,3}\) at \(q=2\). These are checkable finite witnesses, not an exhaustive proof of the infinite-graph theorem. The complete proof establishes the parameterization of all derivations, the incidence-rank calculation over all fields, the counting identity, and the girth coefficient without computational assumptions.

Review status: self-review passed on the mathematical statement, its comparison to available literature, and its mathematical motivation. Independent audit and independent validation are not performed; the checks above must not be presented as such.
