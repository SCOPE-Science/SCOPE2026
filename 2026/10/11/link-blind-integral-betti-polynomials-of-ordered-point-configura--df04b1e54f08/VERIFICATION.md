---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For L with n smooth circle components and s extra finite point punctures, Alexander duality in S^3 removes L, Q and infinity, so cohomology is Z in degree zero, Z^n degree one, Z^(n+s) degree two, zero above. Excision and local orientation at s punctures split old H^2 classes from s small-sphere generators. In the Fadell–Neuwirth fibration forgetting the kth point, last-coordinate pullbacks of integral H^1/H^2(M_L) and global Gauss maps g_ik to S^2 produce fiberwise integral additive bases, since each g_ik has degree +1 on one puncture sphere and zero on the others. Integral Leray–Hirsch multiplies the Poincare polynomial by 1+nt+(n+k-1)t^2 for each k, proving torsion-freeness for every smooth link/k. For n=1,k=2 it expands to 1+2t+4t^2+3t^3+2t^4. Removing codimension-three diagonals preserves pi1, so unknot complement has abelian Z^k and trefoil complement has nonabelian direct-power group (surjects to S3); same additive cohomology does not force homotopy equivalence.

## originality

PASS

Best-of-knowledge the uniform INTEGRAL ORDERED link-complement product is not stated by the inspected mixed-configuration, unordered knot-complement, or unordered rational configuration results. Classical Fadell–Neuwirth/Leray–Hirsch make proof natural but do not by themselves provide an indexed previously published exact formula. Remaining risk: forgotten ordered-configuration theorem in classical topology.

## value

PASS

Natural mixed-configuration fiber has all integral additive cohomology ranks classified uniformly across number of particles and arbitrary smooth links, and a clean knot-independent-cohomology versus knot-dependent fundamental-group distinction; this precise invariant can be reused in configuration-topology research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
