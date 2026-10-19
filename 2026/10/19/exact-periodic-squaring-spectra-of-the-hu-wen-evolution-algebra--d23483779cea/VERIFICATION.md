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

The theorem is proved by the exact coordinate substitutions and iterate recurrences displayed in `RESULT.md`. The two nonstandard identities used for all periods are
\[
(c,y)\mapsto(c^{2^m},t^m c^{2^m-1}y),\qquad
(c,a)\mapsto(c^{2^m},c^{2^m-1}a-(m/4)c^{2^m}).
\]
The second formula applies precisely to \(\lambda=2\) in odd characteristic, and must not be replaced by the first formula at the singular parameter.

Run `python verify.py` with Python 3 (standard library only). The verifier directly multiplies the natural-basis coordinates, enumerates fixed points for 636 field/parameter/iterate instances, and finds periodic loci separately by orbit detection. It includes extension fields represented by irreducible quadratic polynomials. Successful execution ends in `VERIFY_OK`.

The finite tests do not establish the unrestricted result. The symbolic proof establishes all \(m\ge1\), all odd prime powers \(q\), and every \(\lambda\ne0\). No independent audit has been performed.
