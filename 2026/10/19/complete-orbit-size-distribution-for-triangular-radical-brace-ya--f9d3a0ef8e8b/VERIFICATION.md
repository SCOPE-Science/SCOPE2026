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

# Verification of the orbit-size spectrum

Run `python verify.py` from the directory containing the standalone checker. No third-party Python dependencies are required.

The checker independently obtains ranks from the matrix images of the explicit action \(B\mapsto B+AB\) under the standard matrix units, using Gaussian elimination over the actual coefficient field. It compares these ranks with independent row-span ranks and with the proposed two-branch recurrence for all matrices at the tested sizes. For four test pairs it also explicitly enumerates the full group-action orbits of every element and validates the predicted multiplicities. For \(\mathbb F_4\), multiplication uses the irreducible polynomial \(t^2+t+1\); the finite field is not approximated by integers modulo four.

Checked \((n,q)\): \((2,2),(3,2),(4,2),(4,3),(4,4),(5,2),(6,2)\). Expected full orbit totals in order: \(2,6,26,129,388,158,1330\). The executable returned `VERIFY_OK` with these values. There is no claim that this finite enumeration proves the theorem for untested sizes or finite fields.

The proof's critical universal steps are (i) identifying the brace permutation orbit as an affine image of a linear map; (ii) decomposing the map's image by independent matrix rows; (iii) exact containment counts inside nested row spaces; and (iv) orbit-size division. These steps are written in `RESULT.md` and do not depend on computer output.

Only a self-review was performed. Independent examination of the mathematical argument, code, and priority is still outstanding.
