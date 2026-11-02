---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Read the actual six minimal presentations in Robles-Perez/Rosales Proposition 33 and checked the generator ordering matches. Every presentation move has distance bounded by its largest side length, giving the six matching upper bounds. For classes 1,2,4 mod 6 the pure (n+3)e1 factorization is disjoint from any other factorization by uniqueness of (n+2)e1; the known ne2 alternative forces a step >=n+3. For classes 3,5, pure (n+2)e4 is disjoint and any other factorization uses generators <=g3, hence has at least n+5 atoms. For class 0, complete presentation moves from (n+4)e2 cannot create simultaneous e2/e3 needed for the e4 relation, so the fiber has no e4; pure (n+1)e3 is isolated and every other uses g1,g2 and length >=n+4. All coefficients were verified nonnegative integers. Independently checked equality of all relation weights and maximum side lengths for n=4..33 and exact bottleneck catenary degree in all critical Betti fibers for representative n=4..9. These finite tests are supplementary to the all-n presentation/completeness argument.

## originality

PASS

PASS, with substantial acknowledged premise: the six minimal presentations of precisely these tetrahedral semigroups were already published in 2017. The new statement is the exact ordinary catenary degree across all residue classes, including a bottleneck proof; no inspected earlier paper states or mathematically entails it without an additional fiber argument.

## value

PASS

PASS, modest but substantive: the ordinary catenary degree is a natural factorization invariant for a canonical infinite family whose presentations are known, and its exact six-residue closed law fills the tetrahedral instance next to the recently treated square and triangular cases. The necessity of a bottleneck, especially the no-mixed-coordinate fiber for n divisible by 6, is a mathematical step beyond reprinting the existing presentation; not a large general theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
