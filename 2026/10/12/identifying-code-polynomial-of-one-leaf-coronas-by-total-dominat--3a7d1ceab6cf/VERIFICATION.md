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

# Finite reproducibility checks

The attached `verify_identifying_corona.py` is standalone Python standard-library code. Run it with `python verify_identifying_corona.py`. It checks the identifying-code definition directly from all closed-neighborhood signatures, compares each subset with the structural total-domination/twin criterion, and independently computes the polynomial by summing the theorem's twin-class factors. The pseudorandom seed for sample graphs is fixed at 1729.

Every labeled simple graph on one through five vertices was exhausted (1,099 labeled bases). On six vertices, 120 pseudorandom graph edge masks plus the empty and complete graph were tested. On seven vertices, 16 pseudorandom graphs plus the empty and complete graph were tested. This is 1,239 base-graph instances and 1,860,132 initial vertex subsets. All comparisons passed; actual captured program output is included in `verification-output.txt`.

Separately, the complete-graph polynomial was symbolically evaluated for sizes two through twelve, and the star minimum-code coefficient was evaluated for two through ten leaves. Those tests passed, but finite enumeration cannot certify an infinite theorem. The theorem's independent proof is contained in `RESULT.md`; there is no external proof assistant or independent mathematical audit.
