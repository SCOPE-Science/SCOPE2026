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

The normalized Laurent basis has shift weights squared (1+q^{n+1})/(1+q^n). Taking diagonal entries of kernel equation gives g_{n+2}−(1+q)g_{n+1}+qg_n=0 for g_n=(1+q^n)t_n, hence t_n=(A+Bq^n)/(1+q^n). Comparing zero tails with any block peak 1 forces ||K−T||≥1/2 for every kernel T, and T=I/2 is a Toeplitz attaining equality. For diagonal K the residual differs from ℓ_n=k_{n+2}−(1+q)k_{n+1}+qk_n by (1−q²)q^n/(1+q^n)(k_{n+1}−k_{n+2}), exponentially small. Increment recurrence and total variation ≥2 give liminf ≥2(1−q); smooth boundary-layer hat profiles give limsup ≤2(1−q). Bounded inverse theorem on B(H)/ker D_q turns the distant small-residual sequence into nonclosed range.

## originality

PASS

Best-of-knowledge comparison of actual mathematical statements and implications, not titles. None of the inspected exact results supplies the claim in this final scope; all four comparison types and materially read primary sources are documented. Inaccessible plausible sources are disclosed as risks rather than falsely excluded or used as automatic failure.

## value

PASS

The quadratic polynomial is determined by the two annular boundaries, hence its norm stability is a natural operator question. Distant positive Laurent windows are dictated by convergence of annular weights to the outer unilateral limit, not an arbitrary slice. The exact 2(1−q) coefficient and nonclosed-range consequence are structural and quantitatively sharp even though finite-N exact minimizers are not classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
