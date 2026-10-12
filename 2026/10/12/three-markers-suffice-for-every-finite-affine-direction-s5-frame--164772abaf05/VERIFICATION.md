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

# Finite verification of the affine-direction generator theorem

Run `python verify.py` from this directory with Python 3.9 or later. No third-party modules are required. The checker implements all direction cosets and corresponding existential modalities over specified finite fields; it does **not** assume that independently named modalities can be permuted in a formula.

The `Field` arithmetic module computes addition and polynomial-remainder multiplication for primes and proper prime powers. Each nonzero element is checked to act bijectively by multiplication, ruling out a reducible modulus in these tested orders. The `Frame` module enumerates the actual one-dimensional subspaces and corresponding line partitions.

`check_triangle` evaluates the explicit depth-one corner formula, the depth-two anchor formulas, and the depth-three singleton formulas for **every** point in each tested vector space. `closure_atoms` independently refines modal-equivalence classes from the single input predicate until stable. Its success is checked against the constructive formula outcomes.

Exhaustive subsets are enumerated over \(\mathbb F_2^2\) up to size one, and over \(\mathbb F_3^2\) and \(\mathbb F_4^2\) up to size three. They confirm sharp minima and verify that exactly \(72\) and \(480\) three-point valuations respectively generate in the latter two cases. Checked dimensions include two and three; field orders include \(2,3,4,5,7,8,9,11\).

Expected standard output:

```
VERIFY_OK triangles=9 refinements=11 exhaustive_labelings=832 fields=11
```

These checks are finite empirical corroboration only. They do not independently prove the universal theorem, establish global originality, or optimize the depth-three bound. The mathematical argument in `RESULT.md` covers all finite fields and all dimensions at least two.
