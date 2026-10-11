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

The general proof is given in RESULT.md; no finite enumeration is used as an infinite proof. The paper's comparison theorem supplies the integral isomorphism after verifying the graph satisfies the hypotheses.

Reproduce the finite checks by running `python3 verify.py` (Python 3 standard library, no external packages). Expected stdout contains `VERIFY_OK:`. The program independently inspects all singular three-cube maps whose designated bottom face is a fixed square, checks all four-cycles for sizes 5--7, and certifies boundary orientation plus connectedness of square-face dual adjacency; the four-cycle boundary experiments show an explicit failure of monophobicity. The tested finite sizes do not imply exhaustive verification for arbitrary sizes. The nullhomotopy-to-vanishing-cellular-2-chain step is the crucial noncomputational lemma, independently justified in the proof.

Independent audit has not been performed.
