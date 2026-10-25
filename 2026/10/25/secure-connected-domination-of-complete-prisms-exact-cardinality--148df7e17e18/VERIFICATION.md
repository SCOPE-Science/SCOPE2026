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

# Reproducibility

The standalone script `verify.py` requires only Python 3 and the standard library. Run `python verify.py` from the directory containing the script. It constructs each graph from the two-clique and perfect-matching definition, tests connectivity and domination by explicit graph traversal, and for every omitted vertex enumerates all legal defenders to verify the original single-replacement condition. No library routine for secure connected domination or the theorem's classification is used inside that predicate.

The checker then independently evaluates the proposed layer-intersection classification and each coefficient of the all-set and inclusion-minimal cardinality polynomials. Exhaustive labeled subset spaces have sizes 64, 256, 1024, 4096, 16384, and 65536 for \(n=3,4,5,6,7,8\), totaling 87,360. Recorded admissible-set counts were, respectively, 22, 123, 636, 3001, 13322, and 56951. Minimal-size distributions were \(\{4:15\}\), \(\{4:30,5:8\}\), \(\{4:70,6:10\}\), \(\{4:135,7:12\}\), \(\{4:231,8:14\}\), and \(\{4:364,9:16\}\). All assertions passed.

These are finite corroboration checks only. The proof in RESULT.md establishes every \(n\ge3\); no inference from the finite checks to infinitely many parameters is needed. The script makes no external calls and generates no external certificate. No independent audit has been performed.
