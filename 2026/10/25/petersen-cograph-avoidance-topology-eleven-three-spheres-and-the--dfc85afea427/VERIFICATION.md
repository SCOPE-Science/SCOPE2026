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

# Reproduction of the exact finite checks

Run `python3 evidence/verify_petersen_cograph.py` from the package root with Python 3.8 or newer. It uses only the standard library; no third-party packages, external services or network connection are needed. The companion `evidence/verification_output.txt` records an actual clean execution of this script.

The checker constructs Petersen as the disjointness graph on five-label pairs, enumerates all 1024 subsets by independent forbidden-P4 and direct-path predicates, and checks every dimension/facet count. It builds all 187 discrete-Morse pairs, validates the reversed-pair orientation on the full Hasse diagram, executes an exact integer chain cancellation for every pair, and verifies the displayed 13-by-2 boundary matrix and a unit determinant. Independently, it computes the ordinary simplicial boundary ranks modulo 2, 3, 5 and 13, and verifies signed Lefschetz values on every element of S5 and the full irreducible character decomposition via Murnaghan–Nakayama.

Successful execution ends with `VERIFY_OK`. All enumerations cover the full finite combinatorial input, not sampled instances. The rational representation result does not specify an integral group-lattice decomposition, and the homotopy classification does not assert any theorem for larger graph families.
