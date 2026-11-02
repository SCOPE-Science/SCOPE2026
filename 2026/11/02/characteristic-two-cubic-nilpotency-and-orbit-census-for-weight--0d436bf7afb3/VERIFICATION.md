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

# Verification record

The accompanying standalone standard-library Python 3 program `verify.py` evaluates the weight-zero Rota–Baxter identity from the algebra multiplication, enumerates small matrices and vectors, and directly computes algebra-automorphism conjugacy orbits. Execute `python3 verify.py` in the containing directory. The successful test suite reports `FULL_VERIFY_OK`.

The field/embedding cases exhausted are radical dimensions 1, 2, 3 over \(\mathbb F_2\), dimensions 1, 2 over \(\mathbb F_3\), and dimension 2 over \(\mathbb F_4\). Complete marked-square-zero conjugacy-orbit comparisons were checked in dimensions 2, 3 over \(\mathbb F_2\) and dimension 2 over \(\mathbb F_3\). The checker tests concrete finite cases; the proof in `RESULT.md` supplies every-field classification, exact symbolic counting, and the asymptotic limit. No external formal certification or independent mathematical audit was performed.
