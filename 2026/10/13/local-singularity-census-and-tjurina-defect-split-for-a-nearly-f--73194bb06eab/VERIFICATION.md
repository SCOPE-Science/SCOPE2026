---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For the exact polynomial x0*Q1*Q2*Q3*Q4 all four conics have nonzero quadratic determinants. Bezout accounting isolates the five source points. At p1 the two branches share a tangent with contact 2, giving A3 and mu=tau=3; p2,p3 are three transverse branches each, D4 and mu=tau=4. At p4 and p5 the five smooth branches have one single tangent and two contact-two pairs, with eight other transverse pairs, hence delta=12 and mu=2delta-5+1=20. A fresh independently assembled saturated Groebner basis in the p4 chart has leading exponents (1,0,0),(0,4,0),(0,3,1),(0,2,3),(0,1,6),(0,0,8), giving exactly 18 local Tjurina monomials. The involution exchanges p4,p5. The first exceptional blow-up has multiplicity 5; the two subsequent triple-point blow-ups have multiplicities 7 and 7, and each punctured exceptional has Euler characteristic -1, yielding the stated A'Campo monodromy polynomial (t-1)(t^5-1)(t^7-1)^2 (degree mu=20). Thus global (mu,tau)=(51,47) and defect 4. The local Jacobian/Groebner and contact checks independently passed; these checks do not replace the resolution argument.

## originality

PASS

Best-of-knowledge new local numerical/topological refinement of the exact nearly free example. The originating primary paper supplies its polynomial, five points, near-freeness, tau=47 and a binary non-quasihomogeneity diagnosis, but not the two mu=20/tau=18 local algebras, resolution 5-7-7 or the local monodromy. A related previously published four-branch Type-II germ concerns another singularity and does not cover the five-branch two-tangency structure.

## value

PASS

The result answers the source's explicit qualitative defect question quantitatively: each of two difficult non-quasihomogeneous points contributes exactly 2 to the global Milnor–Tjurina discrepancy, and the resolution supplies a checkable local monodromy invariant. This naturally refines an example central to a syzygy-based quasihomogeneity theorem; it is not merely an unmotivated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
