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
# Verification record

Mathematical verification: exact chain-rule recursion; all interior roots counted by Rolle's theorem; endpoint multiplicity tracked through every recurrence step, including beyond the original vertex multiplicity; degree count excludes missing nonreal or negative roots. A compact connected limiting core containing every leaf of a finite star must equal that star when the full shadow is contained in it. The connected-core theorem is sourced to Hägg and Shapiro, arXiv:2610.09602v1, Theorem 1.4(i).

The included `check_star.py` performs **567 finite exact symbolic cases**: every \(d=2,\ldots,7\), \(n=1,\ldots,6\), and \(0\le m<dn\). It verifies direct derivatives versus the residue recurrence, exact positive-root census via real-root isolation, endpoint powers, and interior squarefreeness. It does not establish the infinite theorem or historical novelty.

The bounded primary-source comparison distinguishes the specific all-order, high-degree regular-polygon claim from the earlier fixed-ratio and special orthogonality statements. The possibility of an earlier unindexed equivalent result remains.

Independent audit has not been performed.
