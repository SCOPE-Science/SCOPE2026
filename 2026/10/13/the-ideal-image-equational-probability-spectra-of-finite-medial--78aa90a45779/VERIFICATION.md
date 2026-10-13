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
The mathematical proof of the exact spectrum is in `RESULT.md` and does not require computation. The bundled `verify.py` is a standard-library Python 3 program. Running `python verify.py` returned `VERIFY_OK` after computing coefficient rings, all binary term coefficients and all probabilities of two-variable equations in the test modules. For five examples it also exhausted ternary term coefficients. The six cases were: cyclic group of order five, cyclic group of order nine, irreducible binary block of size two, a two-dimensional Jordan block in characteristic three, a direct sum of two identical irreducible binary blocks, and a split binary block sum of degrees two and three. Expected image-size sets were respectively \(\{1,5\}\), \(\{1,3,9\}\), \(\{1,4\}\), \(\{1,3,9\}\), \(\{1,16\}\), and \(\{1,4,8,32\}\).

Every module computation is finite and exact. Exhaustion of these instances neither exhausts all fields and orders nor proves the symbolic coefficient theorem, whose finite-inverse argument is given separately. The free module result in arXiv:2602.08875 is treated as known structural literature. An independent scientific or historical overlap audit has not been performed.
