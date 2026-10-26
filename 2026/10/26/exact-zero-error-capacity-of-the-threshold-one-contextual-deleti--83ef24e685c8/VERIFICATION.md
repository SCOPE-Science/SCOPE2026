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

# Verification evidence

The mathematical argument in `RESULT.md` proves the output characterization by a monotonicity-of-transitions lemma and an explicit preimage construction. Counting output words with prescribed transitions gives the exact finite-length formula, while a two-term recurrence and its characteristic roots prove the asymptotic rate. These are all-length deductions for every integer alphabet size \(q\ge2\).

Run `python3 verify.py` with Python 3 standard library only. The checker enumerates the channel image and the inequality-defined image by separate methods; evaluates the closed count; and reconstructs input preimages for short lengths. Its observed counts were:

- \(q=2\), lengths \(1\)–\(14\): `2, 4, 8, 14, 24, 40, 66, 108, 176, 286, 464, 752, 1218, 1972`.
- \(q=3\), lengths \(1\)–\(9\): `3, 6, 15, 30, 63, 126, 255, 510, 1023`.
- \(q=4\), lengths \(1\)–\(7\): `4, 8, 24, 52, 128, 288, 676`.
- \(q=5\), lengths \(1\)–\(6\): `5, 10, 35, 80, 225, 550`.

The program terminated with `VERIFY_OK`. Exhaustive computation is finite evidence, not an independent certificate of the unrestricted statement; the unrestricted result rests on the explicit proof. No separate independent audit or formal verification has been performed.
