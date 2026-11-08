---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For SPD M-matrices, Schur pivots remain positive and negative off-diagonals cannot cancel, so graphical vertex elimination creates all neighbor clique edges. If the first part is i with monochromatic run R, its first vertex completes every other part, the first outsider then completes the remaining n_i-R vertices of part i, and no more fill occurs. Thus F=M-C(n_i,2)+C(n_i-R,2) exactly; sampling without replacement proves Pr(I=i,R=s)=(n_i)_s(N-n_i)/(N)_(s+1). Missing pair indicator expectation gives E F=sum_i C(n_i,2)(N-n_i)/(N-n_i+2). Optimizing the run gives extrema. For balanced size m, R has uniformly geometric tails and tends to Geom((r-1)/r); scaled M-F and second moments give the geometric law and variance. I independently exhausted 1,012,508 labelled vertex orders on small multipartite graphs, comparing graphical elimination to the exact formula, all matching; this is corroboration only, not the unbounded proof.

## originality

PASS

The known neighbor-clique rule and deterministic minimum-fill methods do not, in inspected statements, provide the complete initial-run joint distribution or balanced geometric near-maximal-fill law. RCHOL concerns randomized approximate edge sampling and cannot be equated to uniformly random vertex order in exact Cholesky. A bounded best-of-knowledge PASS, not priority certification.

## value

PASS

The complete random-order fill polynomial, exact expectation/extremes and geometric typical near-worst-case behavior quantify how a natural sparse-factorization graph family behaves under unstructured orderings. This is a natural invariant family with unbounded part sizes, not just a restatement of clique completion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
