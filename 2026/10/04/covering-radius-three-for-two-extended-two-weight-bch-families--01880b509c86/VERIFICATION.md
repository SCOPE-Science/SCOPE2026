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
# Verification

Run `python verify.py` with Python 3. The script uses only the standard library.

The infinite proof in `RESULT.md` rests on two source theorems giving two nonzero dual weights, the standard Delsarte external-distance inequality, and an exact parity-syndrome argument. The script does not replace those theorems. It checks the algebraic parameter identities and positivity of the four leader counts over representative ranges.

As independent finite sanity checks, the script constructs `GF(256)` from the primitive polynomial `x^8+x^4+x^3+x^2+1`. For Family A at `s=2`, it uses an element of order `51`, builds the `52` extended syndrome columns, and performs breadth-first search over all `512` syndromes. It obtains leader counts `(1,52,255,204)`. For Family B at `s=4`, it uses an element of order `85`, builds the `86` extended syndrome columns, and obtains `(1,86,255,170)`. It also checks full rank `9` for both extended parity-check matrices and terminates with `VERIFY_OK`.

The finite anchors verify implementation-level consistency only. They are not extrapolated to the infinite families.
