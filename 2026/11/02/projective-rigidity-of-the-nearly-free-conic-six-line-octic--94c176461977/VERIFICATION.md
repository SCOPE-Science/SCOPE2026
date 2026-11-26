---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Gałecka's syzygy lower bound and near-free upper bound force mdr=4, giving Tjurina number 36. Pairwise Bézout and the orbifold inequality give t+n_3=9, n_2=9-n_3, and 9n_3>=46. If A counts pure line triples, conic–line Bézout gives N_CL=2A-6, hence A>=3. Each line sees at most two pure triples and A=5 is excluded by the odd five pair partners of any line. If A=4, the lines are the edges of a complete quadrangle and the residual double pairs use disjoint lines. At least two of these pairs lie on the conic; all their constituent lines are transverse there and each must contribute a separate conic–line node, contradicting N_CL=2. For A=3, the nine incidences on six lines force three connectors joining the three pairs and one leaf through each triple. The residual double-point graph is the leaf triangle with three pendant edges. Now N_CL=0, so the conic triple edges must form a nonempty 2-regular subgraph, which is exactly that triangle. This forces the stated basket. In connector coordinates the three tangencies force the principal 2x2 minors to vanish; smoothness excludes zero diagonal entries and fixes the sign product of the off-diagonals. Substitution at the three leaf intersections gives the two stated linear differences (the exceptional 3r+1=0 is inconsistent) and compatibility (r-1)^2(r^2-18r+1)=0 with r=1 forbidden. Modulo the quadratic, u(1/r)=v(r) and v(1/r)=u(r), so swapping x,y identifies the two unmarked forms. I checked the smoothness determinant, tangency squares and nonincidence: the six unwanted points evaluate to u^2,v^2,1 and the three squares (v-1)^2,(u-1)^2,(ru-v)^2, all nonzero at the roots. Each secant meets the conic at two distinct designated intersections, so the triples are transverse. Existence and near freeness use the attributed exact mdr computation in the October record. The frozen verifier was inspected and not executed; the incidence exclusions and normal form are proved directly, not inferred from its enumeration markers. The prior mdr computation was not rerun.

## originality

PASS

The supported distinct result is the exclusion of all other baskets and hence the complete projective classification under near freeness for one conic plus six lines. Exact existence/near freeness of the representative is already covered by the October catalogue record. The distinct November 8 catalogue record gives equivalent rigidity of the fixed (3,3,6) basket in different coordinates, not exclusion of other baskets; that subclaim is not counted as a separate unique contribution here. Its date and the snapshot do not by themselves settle priority.

## value

PASS

A known quadratic-field example does not tell whether it is isolated even within this component type. The complete classification turns a necessary numerical range into a single realizable near-free orbit; the incidence analysis explains why the apparent alternatives cannot occur and why the two conjugate normal forms do not produce distinct unmarked arrangements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
