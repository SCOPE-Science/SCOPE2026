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

This record covers the exact orbit classification of ordinary derivations of the three-dimensional left Leibniz algebra whose nonzero basis products are \([e_1,e_1]=e_2\) and \([e_1,e_2]=e_3\).

The symbolic check derives the derivation matrix from the generator \(e_1\), derives automorphisms from its image, and computes conjugation using the explicit invertible triangular matrix. The proof's case split covers fixed \(a\ne0\) in odd or even field size, fixed \(a=0,b\ne0\), the remaining nonzero \(c\) case, and zero. The final orbit cardinalities add up to the total number \(q^3\) of derivations for every prime power \(q\).

For reproducibility, run `python3 verify.py` in the same directory. It requires only the Python standard library and recomputes all finite examples, without relying on previously stored outputs. Actual replay returned `VERIFY_OK` for \(q=2,3,4,5,7,8,9\); the orbit counts were \(6,8,12,12,16,24,20\) respectively. The script checks explicit automorphism and derivation identities and both the formula and cardinalities of the orbit action. Results from finite examples are evidence of correct implementation, not an infinite proof.

Historical originality depends on comparing the conjugacy-orbit classification with existing work, not on the known derivation or automorphism formulas alone. The latest 2026 primary papers were checked at abstract level but their complete text could not be inspected; an equivalent uninspected statement remains a risk. No independent audit or independent validation is claimed.
