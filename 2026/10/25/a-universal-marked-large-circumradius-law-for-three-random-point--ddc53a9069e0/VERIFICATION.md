---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For any compact convex planar K with area A>0, sample three independent area-uniform points. Parametrize the unoriented line through first two by theta∈[0,pi), normal offset p and scalar chord coordinates s1,s2; the exact Jacobian is |s1-s2|. Circumradius R=|X1-X3||X2-X3|/(2|h|), h transverse height of X3. Under R>T, substitute t=Th: bounded diameter implies |t|<=diam(K)^2/2, enabling dominated convergence of the convex chord-section indicators and |t|<|s3-s1||s3-s2|/2. Integration yields 3-point Vandermonde density on each chord, whose interval [0,1] integral is 1/30. Thus T P(R>T)->Q6(K)/(30 A³), line density ell^6/Q6, normalized sorted gaps 1/2 Dir(1,3,2,1)+1/2 Dir(1,2,3,1), transverse U uniform[-1,1] independently of line and gaps. Independently recalculated integral 1/30, disk Q6=2048*pi*a^7/35 and tail 1024*a/(525*pi²), square diagonal/side ratio 8sqrt(2)/7. The existing finite Monte Carlo script is not treated as an asymptotic proof.

## originality

PASS

Prior Blaschke–Petkantschin/chord-power theory includes the sixth chord integral, and the unit-disk scalar circumradius tail was already established in 2026; neither alone implies the entire marked limit for arbitrary convex K. Kendall 1985 is the key plausible same-object shape-density paper, and its publisher abstract explicitly treats i.i.d. points from convex K and near-collinearity. Full text was not acquired despite open attempts and an authorized institutional attempt blocked by disconnected VPN. Its shape-density does not visibly identify Euclidean line offset, chord-sixth-power line bias and the independent gap/transverse marks, but priority risk is substantial and retained. Best-of-knowledge originality restricted to the full marked law, not the scalar disk coefficient.

## value

PASS

The marked limit describes not just how rarely a random triangle is nearly collinear but where its supporting line lies, how its three points separate along the chord and how the small transverse displacement scales. The Dirichlet mixture and sixth-power chord bias provide natural geometric-probability data for rare-event simulation and integral-geometric tail asymptotics; this is substantive beyond a known scalar benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
