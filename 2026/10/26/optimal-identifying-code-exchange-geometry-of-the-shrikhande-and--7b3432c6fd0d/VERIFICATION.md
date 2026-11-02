---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The universal signature bound 2^m-1≥16 gives m≥5. A representative Shrikhande five-code was checked by its 16 nonempty distinct signatures; all 16·6 parity-coset/local-edge templates are valid, and every one of all C(16,5)=4368 candidate five-sets was independently tested, yielding exactly 96 and the same family. A single exchange preserves the unique three-member parity coset and its missing point, so each q-indexed component is the line graph of its six-neighbor C6, hence C6. In the rook graph independent closed-neighborhood signature enumeration over all subsets through size6 gives exactly 2208 minima; every pair differing by one code point was joined, yielding 28800 edges and a single component, and BFS from all 2208 states yielded eccentricity 6 each. Both supplied C++ and Python algorithms were inspected and independent Python recomputation reproduced the counts. This exhaustive finite proof has no generalization to larger Doob graphs.

## originality

PASS

Gravier–Moncel–Semri 2008 Theorem 1 already proves rook minimum size floor(3n/2), so n=4 gives 6 as known background (no claimed new gamma_ID(R)). Their even-n construction and optimal-size theorem do not enumerate 2208 labelled minima or optimum replacement connectivity. Gravier et al. 2015 discuss vertex-transitive and strongly regular identifying codes and recall Cartesian clique products, but explicitly note few known optimal SRG cases; the inspected material lacks this Shrikhande classification and both exchange graphs. Prior homology distinctions for this SRG pair in Resultary use a different invariant, not these code signatures.

## value

PASS

Identifying-code minima are standard sensor placement quantities. A graph with only 16 vertices that meets the sharp information-theoretic size bound, and the contrast between disconnected and connected optimum-preserving sensor exchange despite identical SRG(16,6,2,2) parameters, form a natural and nontrivial geometric classification, not an unmotivated arbitrary graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
