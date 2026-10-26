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

Run `python3 verify.py` with Python 3 and standard library, from a directory containing this file and the script. The script independently constructs divisor-sum posets and counts congruence-restricted prime pairs for each prime pair with \(pq\le10000\), verifies agreement of direct and progression counts at \(X=100,1000,10000\), and reports counts through \(X=10^7\). Expected final output: `VERIFY_OK`.

The calculation does **not** certify any infinite asymptotic. Those depend on the fixed-modulus prime number theorem in arithmetic progressions, Brun–Titchmarsh and Landau's semiprime asymptotic. A finite partial sum of the constant is not the infinite sum with an explicit tail error. Only the displayed counting and joint weak-limit claim receives the self-review; independent audit has not been performed.
