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

For fixed endpoints a,b on a finite tree, deleting any edge gives a cut. A covering walk must traverse an off-path edge at least twice and each a-to-b path edge at least once; performing subtree tours along that path attains 2e-d(a,b). In the Munn model (P,g), the range and domain idempotents are (P,1) and (g^(-1)P,1), so R fixes the initial-rooted tree, L the terminal-rooted tree, and H both endpoints. D allows translations: if Q=kP and h belongs to Q, the representative (P,k^(-1)h) links (P,g) by R to (Q,h) by L. Conversely such a link forces the translated-tree condition. For a covering walk starting at a nonidentity vertex a, the resulting Munn tree placed at identity is a^(-1)P and its terminal vertex is a^(-1)b; translation preserves distances. Thus maximizing d(a,b) gives the four displayed minima with the fixed endpoints, the initial or terminal eccentricity, or the diameter. For fixed rank, the verified graph-group shortlex theorem applies to the free group (no commutations); the reduced length of w[i+1..j] equals the Cayley-tree distance between the corresponding prefixes. Because the connected Munn subtree lies in a tree, this is also its internal distance. Simulating the logspace transducer on a virtual substring, counting output letters as emitted, and reusing its workspace makes each equality or distance query logarithmic space. Nested scans of prefix indices count first occurrences for e and maximize distances for the eccentricities and diameter, using only logarithmic counters. The final length comparisons, including the empty input, follow. The finite checker was inspected, not rerun; the logspace bound is analytic.

## originality

PASS

The supported contribution is simultaneous deterministic logarithmic-space computation of the class minima from the input word, including the consequent logarithmic-space recognition; it is not the geometric minima themselves or the first context-sensitive upper bound. The exact earlier indexed geometry and linear-space recognition are credited. A later indexed statement of logspace recognition overlaps for R/L/D with a different argument; the text comparison demonstrates overlap but does not establish independent discovery or provenance.

## value

PASS

The improvement from explicit deterministic linear space to logarithmic workspace for these natural languages is substantive. The method outputs exact class minima without storing the Munn tree, not just testing acceptance, and applies even to the classes with neither context-free nor co-context-free geodesic languages. Its value is the stronger resource bound and uniform method over the four classes at each fixed rank, not rederiving the known geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
