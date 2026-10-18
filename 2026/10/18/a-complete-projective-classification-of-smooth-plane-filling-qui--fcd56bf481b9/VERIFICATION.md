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

# Exact verification

The portable program `verify.py` (Python 3, SymPy) runs the exhaustive enumeration and the independent algebraic-closure checks. Command: `python3 verify.py`. It was executed successfully on the exact version included with this work.

Its finite witness phase enumerates all fourteen-bit coefficient masks and all projective points over extensions of degrees one through six. New singularity-witness counts by degree are 14196, 147, 24, 420, 0, 84, respectively. The total of 14871 witnessed singular nonzero forms is exact and checkable.

Projective linear substitution generates the complete rational linear group. It produces exactly ten orbits of the 1512 surviving forms. The representative masks in `RESULT.md` are checked by explicit algebraic-closure certificates: on the three charts obtained by setting one projective coordinate to one, the three partial derivatives have reduced Gröbner basis `{1}` in characteristic two.

**Logical boundary:** The finite extension search is not an a priori exhaustive geometric singularity bound. Geometric smoothness of the survivors is independently certified by the ten unit ideals and their projective orbits. No independent audit has been performed.
