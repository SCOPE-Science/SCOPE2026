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

# Finite and symbolic verification

The theorem is supported by the explicitly quantified Boolean-algebra proof in `RESULT.md`; the following finite computations are checks, not a proof for infinite Boolean algebras.

Invoke `python3 verify.py` from the directory containing this package. Python standard library only; no network or nonstandard dependencies. The program enumerates every map on the powerset algebras with one and two atoms and checks agreement of the quasi-identity and binary-join preservation, giving 3 out of 4 and 25 out of 256 satisfying maps respectively. Since the quasi-identity implies monotonicity symbolically, testing all 8,000 monotone maps on the three-atom powerset algebra exhausts every possible satisfying map there; precisely 729 satisfy both. Finally, the exact operator printed in arXiv:2603.17724v1, Example 2.2, violates the quasi-identity on the explicitly stated triple.

The locally rerun output ends with `VERIFY_OK`. The code is complete and works as printed. No computational experiment addresses arbitrary infinite Boolean algebras, CEP of the example, or the paper's other constructions.
