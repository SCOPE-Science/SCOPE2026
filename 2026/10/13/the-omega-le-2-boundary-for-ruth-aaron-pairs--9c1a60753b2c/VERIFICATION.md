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
The universal claim is established by the symbolic four-case proof in `RESULT.md`.

The executable `verify.py` is a finite regression check. It computes \(S(n)\) and \(\Omega(n)\) directly from a smallest-prime-factor sieve for every \(2\le n\le200000\), verifies that the only low-\(\Omega\) Ruth--Aaron start in that interval is \(5\), and stress-tests the semiprime--semiprime identity on a finite prime grid. Its output is stored in `VERIFY_OUTPUT.txt`.

The finite search does not prove the infinite theorem. The proof does not depend on the cutoff, on probabilistic evidence, or on an external certificate. Independent audit has not been performed.
