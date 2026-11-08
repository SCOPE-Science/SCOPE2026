---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS for fixed k>=2 and fixed color rank s>=1, q=2^s. Exact parity constraint on each (k+2)-set identifies all even (k+1)-face maps with q^{C(n-1,k)} independent root k-face labels. A transposition has root coordinate orbit deficit a=C(n-3,k-1), hence fixed probability exactly q^-a. For nontranspositions with a fixed root, support/cycle orbit inequalities give >=(3/2)a for supports 3,4 and >=3t a/8 for 5<=t<=epsilon n; large support gives Omega(n^k). For derangements, equivariance of the simplicial boundary/coboundary map bounds invariant face-code dimension by number of k-subset orbits, again Omega(n^k) defect. Two distinct transpositions impose at least 2C(n-5,k-1) independent constraints and so Bonferroni overlap is lower order. Thus P(nonrigid)=C(n,2)q^-a(1+o(1)), and Burnside gives the relative isomorphism-count correction. Independently constructed rooted even-face masks and binary equation ranks for every permutation on 6 vertices with k=2; all 15 transpositions have defect C(3,1)=3; finite permutation check does not prove the asymptotic.

## originality

PASS

PASS qualified for the joint sharp general k,s nonrigidity asymptotic. Mallows–Sloane 1975 already enumerates ordinary q=2 two-graphs and is explicitly credited. Estrada 2026 constructs/extends the generic parity-even hypergraph age (read Section 3), and Cameron–Spiga 2015 addresses primitive automorphism classes, not the random transposition-dominated rate. Chung–Graham 1992 cohomological formalism remains an important possible older equivalence.

## value

PASS

PASS. Exact dominant symmetry type and rate in a natural cohomological parity-restricted higher-arity random age explain the first deviation from universal rigidity and determine the Burnside correction to unlabeled enumeration. This is a substantive asymptotic classification, not relabeling a generic random hypergraph bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
