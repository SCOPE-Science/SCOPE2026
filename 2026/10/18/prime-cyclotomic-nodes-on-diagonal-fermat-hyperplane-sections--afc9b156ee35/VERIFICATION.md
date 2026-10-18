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
The package includes `check_nodes.py`, an executable exact enumerator using Python and SymPy. Running `python check_nodes.py` prints `VERIFY_OK` after two independent finite checks: enumeration of all \(p\)-root labelings of equal multiplicity modulo diagonal translation and cyclotomic Galois multiplication, and evaluation of a restricted Hessian determinant modulo the exact prime cyclotomic polynomial. The tested cases are \((p,m)=(3,2)\) and \((5,1)\). Outputs are \((30,15)\) and \((24,6)\) for the numbers of geometric and closed singular points, respectively. The code also reports formula-only predictions for \((5,2)\) and \((7,1)\); these are not exhaustive computations. The all-prime theorem is justified by the symbolic proof in `RESULT.md`, which must be read independently of finite tests.

The proof addresses characteristic zero only. No independent external audit, formal theorem prover, or assertion about all reductions modulo primes was performed.
