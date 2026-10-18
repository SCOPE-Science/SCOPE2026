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

# Verification and scientific scope

Run `python3 check_source.py > replay.json` and compare the generated UTF-8 bytes with `certificate.json` including its final newline. Only the standard Python library is required. The code exhausts all rooted-tree isomorphism types through ten vertices, groups them into unrooted-tree classes by canonical rooted-code minimization, and checks every source automorphism orbit distance histogram. The two exceptional orbit-pairs are then checked against all \(2^9=512\) equally weighted retained-edge masks. The certificate provides both exact moment numerators and full component-size distributions. Independent direct calculation on the first explicitly labeled ten-vertex witness and independent unrooted-tree enumeration agree.

Rooted and free tree type totals at order ten are respectively 719 and 106. There are zero distinct same-tree root-orbit mean-curve collisions through nine vertices, exactly two at ten, and the two half-transmissibility variance differences are both nonzero. The elementary induction on rooted-code multisets supplies completeness of the finite search, not an assertion about larger trees.

The proof does not establish source recovery from finite noisy observations or from the mean curve at a single transmissibility. No external or independent audit has been performed.
