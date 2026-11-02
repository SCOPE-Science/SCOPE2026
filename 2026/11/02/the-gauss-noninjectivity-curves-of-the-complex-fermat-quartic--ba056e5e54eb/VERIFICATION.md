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

# Direct verification

`python3 verify_gauss.py` uses exact integer modular arithmetic, no dependencies outside the Python standard library. It enumerates the \(27\) cube-root phase patterns and all projective points of the Fermat quartic over \(\mathbb F_{13},\mathbb F_{37},\mathbb F_{73}\). For every point it compares the size of the directly enumerated Gauss fibre to the exact phase-derived criterion for the existence of a distinct mate. The observed Gauss-fibre distributions (listed as fibre size: number of distinct image points) are \(\mathbb F_{13}\): \(\{2:64\}\), \(\mathbb F_{37}\): \(\{1:256,2:64,3:256\}\), and \(\mathbb F_{73}\): \(\{1:984,2:1216,3:768,5:192\}\). The generic statements in the proof follow instead from the classification of irreducible components and their finite pairwise intersections, and are not inferred from these finite-field tests.

The checker is exhaustive over the named finite prime fields but not over \(\mathbb C\). The proof's key infinite steps are the cube-root decomposition, a binary-quartic factorization, and smoothness of the diagonal plane quartics; all are explicitly established in `RESULT.md`. This is self-reviewed work. No external audit or independent validation is claimed.
