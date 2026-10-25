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

# Reproduction and boundaries
Run `python3 verify_moments.py` in a directory containing this file and `verify_moments.py`. The script requires the Python standard library only and uses `fractions.Fraction` throughout. It verifies exact binomial expectations, the two parameter-collision identities, the reflected normalized-sixth-moment polynomial on a rational grid, and numerous separate positive-parameter triples. All checks must pass with no floating-point tolerance.

An independent symbolic integration over \(0\le u\le C/2\) and \(0\le v\le H\), with densities \(2/C\) and \(2(H-v)/H^2\), yields the displayed second, fourth, and sixth moment polynomials. The proof's strictly positive reflected-difference quadratic is algebraic and valid for every positive parameter choice. The finite loops alone do not certify the universal statement or historical novelty.

The lateral surface carries the intrinsic flat product metric. Sampled points are independent and uniform by area. There are no filled endcaps and no use of ambient Euclidean chords. The two moment measurements can be ambiguous; the third resolves that ambiguity, without asserting recovery for broader surface classes. External independent scientific audit has not been performed.
