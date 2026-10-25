---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The surface X is the specified smooth Yu–Zhu quintic at t=-1/8 over C, and the upstream published source is used only for completeness of its 85 listed lines. The 85 pairs of linear equations in pinned artifacts/verify_skew_capacity.py define incidence by vanishing of the 4x4 determinant. Exact K=Q(i,a,b), i²=-1,a⁴=2,b⁴=3 arithmetic with 32 rational basis elements returns 850 meeting pairs, degree 20, and common-neighbor census 530 (three) and 320 (zero). I inspected the full pinned finite certificate and executed an inspected exact-arithmetic transcription: the proposed 18 lines {2,6,38,...,53} are disjoint; 19 meeting-line cliques cover all 85 lines, and every 19-skew set would yield a transversal of eight explicit 4-element residual blocks, but all 65,536 transversals have meeting pairs. A second color-bound branch search visits 2575 nodes and excludes size19. This establishes alpha(G)=18 conditional on the cited source equations being the complete line set. The upstream theorem and individual formula correspondence are not independently reproved.

## originality

PASS

The reformulation is exact and used by the certificate. Spectrum and degree alone do not logically determine alpha(G)=18; the new covering/transversal obstruction is extra information.

A skew-line construction on a different surface cannot cover the maximum for this exact X; a universal upper bound of 30 does not force 18.

The underlying graph data permit deriving alpha via a further exact search, but no known table inspected already supplies the sharp capacity. A new exact invariant of a named geometric configuration can be mathematically useful even without a general method.

The prior regular/spectral results do not imply 18 from their stated bounds; direct certificate provides a strictly new exact capacity number.

## value

PASS

A fixed smooth quintic with 85 lines is a naturally distinguished geometric configuration; the exact maximum disjoint-line capacity is a nontrivial combinatorial and algebraic-geometric invariant, not inferable from rank or spectrum. The compact clique-cover obstruction and explicit witness are independently useful to compare configurations and optimize line arrangements. No general paper-sized theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
