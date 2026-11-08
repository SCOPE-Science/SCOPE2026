---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

A legal vertex flip exchanges adjacent unlike edge-orientation bits 10↔01, so number k of clockwise bits is conserved. Kozlov Proposition 6.10 supplies one point component for k=0,n and one circle component for each 1<=k<=n-1, with no H>=2. For each vertex i define the integral one-cochain α_i counting signed clockwise particle transport across i; independent flip cubes commute and make α_i closed. The occupancy cochains satisfy dx_i=α_i−α_(i+1), so their cohomology classes agree. The displayed explicit path moving one particle around vacant edges, then shifting all remaining particles and closing across the boundary, crosses every vertex once positively: α_i pairs to +1 and hence is primitive in integral H1=Z on each middle component. Spatial reflection both reverses polygon order and complements the particle/hole encoding, giving positive action on flux; global arrow reversal complements without reversing geometric order, giving negative flux. This proves all integral module actions, trace formulas and zero full-group H1 invariants. Quotient rational homology is invariants for a finite simplicial action after subdivision, and component orbits are k∼n-k. The inspected finite signed cubical Lefschetz checker covers 208 group actions for n=3..10; it corroborates but does not establish all n.

## originality

PASS

Kozlov already determines every component as circle or point; only the natural symmetry maps on primitive integral cycles are newly asserted. The nearest published Resultary theorem for Flex(K_n) is another graph family with different topology and cannot imply the present cycle formula. Detailed integer flux/reflection/reversal signs, not just a Betti count, support newness on best-of-knowledge basis.

## value

PASS

The integral H1 sign representation under geometric reflection versus all-arrow reversal is a natural topological invariant of flex dynamics. Identical component permutation actions obscure genuinely opposite loop actions; the theorem resolves the complete integral D_n×C2 action for every n and yields a quotient rational-homology consequence. This is an unbounded, structurally motivated equivariant calculation, not restatement of the known rank n−1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
