---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fresh reconstruction verifies the global rigidity argument. Tabachnikov's convex bicycle lemma makes each Vi,Vi+1,Vi+4,Vi+5 an isosceles trapezoid. Comparing the same unoriented base line at indices i and i+5 gives theta_{i+5}+theta_{i+9}-theta_i-theta_{i+4} congruent to 0 mod 2pi. In turning-angle variables this is 2pi+alpha_{i+4}-alpha_{i+9}; convexity places it in [pi,3pi], so it equals 2pi and alpha_{j+5}=alpha_j. The first five turns sum to pi, hence opposite edges are negatives and the decagon is centrally symmetric. Writing centered vertices X_{i+5}=-X_i and X_{i+4}=-X_{i-1}, the common side and fourth-diagonal lengths give |X_i-X_{i-1}|^2=s^2 and |X_i+X_{i-1}|^2=d^2, hence |X_i|^2+|X_{i-1}|^2 is constant. This forces radius squares to have periods 2 and 5 and therefore to be constant. The vertices lie on one circle; equal adjacent chords in convex cyclic order then force equal central gaps pi/5 and regularity. No finite experiment is used as an infinite proof.

## originality

PASS

Best-of-knowledge PASS. The closest prior work makes this parameter pair especially nontrivial rather than covered: Tabachnikov's global convex regularity theorem lists k=2, odd n with k=3, n=2k+1, and n=3k, so (10,4) is absent. Connelly--Csikos classify the regular (10,4)-gon as first-order flexible, and Csikos proves the exceptional class B is second-order flexible but third-order rigid while explicitly asking whether such regular polygons are genuinely flexible. Since (10,4) lies in B, the submitted global convex theorem answers that open local-flexibility case negatively by showing every convex realization is regular. Resultary's closest hit is the audited record itself; no broader published SCOPE theorem was found.

## value

PASS

PASS. This closes a natural exceptional case singled out by the established bicycle-polygon rigidity program: (10,4) is locally first-order flexible and even second-order flexible, so proving global convex uniqueness is not a routine regular-polygon exercise. The proof exposes a reusable rigidity mechanism--half-turn symmetry plus a coprime period argument for centered radii--and resolves a concrete open flexibility question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
