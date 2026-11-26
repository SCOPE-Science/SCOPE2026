---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditional on seed x in T−v, the two complementary cases are that all incident edges are closed, or exactly one edge xy is open and all remaining edges incident to either endpoint are closed. This yields the frozen formula after averaging over n−1 post-deletion seeds, including isolated seeds and order two. I inspected the proof, verification notes and checker, and independently generated tree shapes by adding a leaf at every location of each previous shape; deduplication by the smallest recursively sorted rooted encoding over all choices of root is complete up to isomorphism. I summed seed counts for components of size at least three by exhaustive edge-state enumeration, padding ignored incident edges so all candidates share the same degree n−1 Bernstein basis. Coefficientwise comparisons certify a common minimizer in 23 of 24 shapes; nonzero nonnegative differences are strictly positive on the open interval. The only exception is the subdivided double claw at order seven. Its bridge, hub and leaf numerators (denominator 6) are 6p², 9p²−5p³ and 15p²−11p³+2p⁴. Leaf-minus-bridge and leaf-minus-hub are strictly positive throughout (0,1), and hub-minus-bridge is p²(3−5p)/6, giving the stated three-way tie and both strict phases. Replay: python3 -I /workspace/review_math.py 3. The proof uses independent bonds, not independent outgoing Markov SIR transmissions.

## originality

PASS

The distinct claim is the first tree order, unique exceptional shape, and exact change in optimal pre-exposure vertex removal for the three-case tail event under iid bonds and a uniform surviving seed. The closest same-day mean-objective result gives a different classification, and the same-day exact three-case result optimizes over unvaccinated tree shapes rather than choices within a tree. The reviewed work does not establish priority beyond the comparisons made.

## value

PASS

Size three is the first outbreak threshold that tests more than whether any transmission occurred. The exact bridge-versus-hub switch resolves when targeting that tail event requires tuning the intervention to transmissibility, and separates the answer from that for mean case count in the same simple model. The tight order and single exceptional topology provide a motivated benchmark for finite-tree risk optimization, not a claim about practical vaccine efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
