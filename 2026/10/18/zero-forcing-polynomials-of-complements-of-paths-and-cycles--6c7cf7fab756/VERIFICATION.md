---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Let G=complement(H) for H=P_n or C_n, n≥5. With r initial whites, each blue vertex has r−|N_H(v)∩W|≥r−2 neighbors among whites in G, hence r≥4 immediately stalls; Z≥n−3. With r=2, path/cycle vertices u,w have distinct external H-neighborhoods, so some blue v sees exactly one of u,w in H and forces the other in G; remaining singleton is forced since δ(G)≥2. For r=3, first G-force happens iff a blue degree-two vertex of H has both its H-neighbors among the three whites, and then pair completion finishes. Path counting (n−2)(n−3) center–triple incidences minus n−4 double counts yields n²−6n+10. Cyclic incidences n(n−3), usually n double-center triples give n(n−4); at n=6 precisely two alternating triples have three centers and each causes multiplicity adjustment +2, giving n(n−4)+2. Thus full polynomials have low coefficient as displayed, then binom(n,2), n, 1; difference 2n−10+2*[n=6], zero at n=5. Independently enumerated all initial blue sets for n=5..10 in path/cycle complements, matched both polynomials (n=6 path 10, cycle 14 minimum sets). This bounded test does not prove all n; the incidence argument does.

## originality

PASS

Best-of-knowledge PASS for full polynomial refinement. Curl et al give the scalar n−3 for these graph complements, but no count of all minimum sets. Boyer et al compute polynomials for ordinary paths and cycles (not complements) and general top coefficients. The n=6 exact correction and minimum triple description require a separate incidence argument.

## value

PASS

The complementary path/cycle families are natural dense graphs with classical scalar forcing number n−3 but previously unenumerated minimum forcing sets. Exact complete polynomials, especially the six-cycle overlap exception and sharp effect of adding the cycle edge in H, refine the scalar result into reusable enumerative distributions across infinitely many orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
