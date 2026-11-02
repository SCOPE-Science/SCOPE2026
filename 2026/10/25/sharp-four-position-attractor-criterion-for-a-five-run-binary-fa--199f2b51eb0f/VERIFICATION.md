---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For W=0 1^b 0^c 1 0^e, check zero-indexed markers (0,b,b+c,b+c+2) provide a four-position attractor: all gaps are monochromatic except a lone one; all missing factors can shift to a marked run. Explicit three-marker constructions apply respectively to e≤c, e>c with b≤3, and e>c,b≥4,c≤2. In the complementary b≥4,c≥3,e>c regime, 011,110,001,0^e each occur uniquely in pairwise disjoint intervals, forcing four markers. Substitution b=4+k,c=3+i,e=c+1+j yields n=13+k+2i+j and generating function z^13/[(1−z)^2(1−z²)]. Independently exhaustively computed smallest attractors for all 125 triples 1≤b,c,e≤5, matching theorem. No finite check is used to infer all triples.

## originality

PASS

The exact gamma=4 iff and rational length enumerator for the specified free run-family are not directly included or implied by the inspected generic algorithmic and other fixed-family attractor results; originality is best-of-knowledge.

## value

PASS

A minimal contiguous-factor attractor is a standard compression-related invariant. This natural three-parameter two-singleton five-run motif gives a sharp structural transition from three to four markers and an exact nontrivial density 1/2. The family restriction isolates competition of central and terminal zero runs, rather than an unmotivated numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
