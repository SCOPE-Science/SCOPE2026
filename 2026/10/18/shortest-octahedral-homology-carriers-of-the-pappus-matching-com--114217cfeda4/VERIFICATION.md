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
# Reproducible verification

Run `python3 -m pip install -r requirements.txt` in a separate environment, then run `python3 verify_pappus_carriers.py`. This script independently reconstructs the labeled 18-vertex, 27-edge Pappus graph and all 35,368 augmented faces, checks the 17,661-pair Morse matching is globally acyclic, computes the signed 43-by-3 critical boundary and unit minor, and confirms that all 5,319 original degree-six boundaries lie in its primitive image. The program enumerates all 54 centered length-two paths and all 297 six-block partitions of 18 vertices, verifies every 64-simplex fundamental cycle has zero boundary and represents a primitive nonzero integer homology class, enumerates all 216 graph automorphisms, and checks orbit sizes 108,36,108,36,9 and Smith ranks 40,25,35,31,5 with unit invariants. Its 40 selected carriers from the first orbit have exact quotient determinant -1. Success ends with `VERIFY_OK_PAPPUS_MINIMAL_CARRIERS`.

Run `python3 verify_pappus_mod2.py` separately. It uses Python's standard library and a different enumeration order to recompute all matching faces and mod-two augmented simplicial boundary ranks (1,26,271,1448,4195,6362,4335,984,42), so the only reduced degree-five mod-two homology dimension is 40. Success ends with `VERIFY_OK_PAPPUS_MOD2`.

These are finite exact certificates, not a claim of exhaustive literature coverage, a general theorem for all cubic graphs, independent external validation or a computerized proof assistant. The flag-complex lower-bound/equality argument and the integral Morse lattice interpretation are explained in RESULT.md; the standalone checkers independently implement all nontrivial object-specific combinatorial steps.
