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

Run `python3 verify.py`. The checker requires Python 3.9+ and no third-party modules. It enumerates graph edges, all 672 oriented cellular incidences for degree-one boundaries and 912 degree-two incidences, and verifies signed chain identities. The boundary ranks over 2, 3, 5, and 101 are (119,207), (119,208), (119,208), and (119,208). Nine fundamental graph cycles lift to configuration one-cycles with independent images. All 96 automorphisms act by cellular chain maps and produce the character values in RESULT.md. The eight canonical rotation powers have exactly the listed trace values.

The mathematical proof uses established suitable-subdivision and rational transfer theorems; those are not replaced by finite checks. Over characteristic two there is a rank jump consistent with the known integral two-torsion, but the novel claim is rational and does not require a new Smith-normal-form calculation.

Success marker: `MOBIUS_KANTOR_TWO_POINT_CHARACTER_CERTIFICATE_OK`.
