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

From this directory, execute `python3 verify.py`. The standard-library program independently enumerates all simplices of the circulant, including the absence of five-vertex independent sets, checks every signed term in the explicit integral three-cycle, computes the complete mod-two ranks of all three boundary maps, and tests the oriented action of the sixteen rotations and sixteen reflections. It checks the complete nine-row orbit-reduced boundary matrix and the complete triangle-incidence classification. The expected output is in `verification_output.txt`.

The exact rank argument does not mistake finite experimentation for an infinite proof: the entire finite chain matrix is built and eliminated over a field. A nonzero integral three-cycle and mod-two rank seventy-nine together give rational rank exactly seventy-nine. A primitive coefficient vector then identifies the whole integral top-cycle lattice, not merely a nonzero class over one coefficient field.

The computation does not claim the quotient's integral homology, fundamental group, homeomorphism type, or the behavior of a varying family of circulants. The rational quotient conclusion separately uses the standard finite-group coinvariant argument after barycentric subdivision. No independent mathematical audit has yet occurred.
