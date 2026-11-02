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

# Verification of the two-error threshold

Run `python3 verify.py`; it needs only Python 3 standard-library combinatorics and integer arithmetic. The executable checks the new finite portion of the theorem rather than attempting to replace the cited infinite-dimensional theorem.

The script computes the maximum of \(|N_4(I_M)|-(2^{n-1}+M)\) over **every** integer \(1\le M\le2^{n-2}\) without enumerating the vectors. The proof justifies its lexicographic block recurrence: a listed subset is assigned weight \(\binom{\min X}{4}-1\), and lexicographic sublists split according to their largest coordinate. Exact maximum-prefix sums of nested finite lists yield the maximum over all admissible class sizes.

The arithmetic checks are: positive maximum \(329481574\) at \(k=35\) and \(M=15771159390\); negative maximum \(-452256184\) at \(k=36\); strictly negative maxima for every \(k=36,\ldots,65\); and direct reconstruction of the 35-bit neighborhood count \(50460379332\). An independent brute-force set-of-neighbors algorithm checks **every** smaller-class size for ambient dimensions \(n=6,\ldots,11\) and agrees with the recurrence. Its exact expected terminal line is `CERTIFICATE_OK`.

The theorem's infinite range \(k\ge66\) uses Theorem 4 of Rajput–Jagatti–Rajan (arXiv:2610.09011v1), not finite extrapolation. The Harper–Räty radius-four minimization principle is also externally established and explicitly used in the source Theorem 3. No full machine-formal proof or independent external mathematical audit is claimed.
