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

In the bi-infinite extension any two specified cyclic edge types, even two copies of one type, can be realized disjointly by translation. Thus admissibility is exactly exclusion of all four self-dual edges and simultaneous use of either pair of distinct reverse-complement edge types; this also treats n=1,2. The pairwise indicator expansion is exact, the trace of each surviving adjacency matrix counts positioned closed walks, and the formal trace-determinant identity gives the signed determinant product. Independently, review_checks/periodic_alphabet_certificate.py built the union of the 64 maximal graphs by successive inclusion-exclusion and extracted determinants by trace/Newton identities: all 18 signed nonzero entries and the exact cross-multiplied identity agreed. It reproduced the first 18 counts from the product and direct word/rotation-class counts through length 8. Burnside applies because repeating a block does not change the bi-infinite extension; the divisor formula counts fixed words rather than just primitive periods. The cubic has one simple root alpha>2 and the other roots in (-1,0) and (0,1); the other factors have reciprocal roots of modulus at most 2 (in particular |x|>2 is impossible for x^4-x^3-1=0). Logarithmic differentiation gives multiplicity eight and O(2^n), and proper-period divisor terms are O(n alpha^(n/2)) before division by n.

## originality

PASS

The asymptotic exponential rate and compatible generating graphs are prior. The all-length overlap-corrected zeta function, exact positioned and rotation-class counts, and leading multiplicity eight are distinct from the strongest statements inspected. In particular an extremal generating graph's spectral radius does not enumerate the union or determine its leading coefficient.

## value

PASS

This is the fixed-point zeta function of a natural periodic four-letter avoidance language, not a rerun of the finite-linear capacity computation. The compatible graphs have overlapping cycle languages, and even the leading multiplicity is not supplied by optimizing a spectral radius. The simplified rational invariant resolves the all-length census and determines both positioned words and rotation classes, useful when counting or comparing periodic constraint languages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
