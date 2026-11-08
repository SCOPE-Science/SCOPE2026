---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For n≥3, ell≥1, identical pendant weighted path at every vertex of a common weighted C_n, Fourier transform conjugates the graph Laplacian to H(mu_k)=J+a mu_k e0e0^T, mu_k=2−2cos(2πk/n). Each H is irreducible Jacobi, with simple eigenvalues strictly interlacing its fixed principal minor D; hence spectral branch bands are strictly disjoint for every mu and any positive conductances. Endpoint eigenvector components never vanish by tridiagonal recurrence. Hellmann–Feynman derivative d lambda_j/dmu=a|v_j(0)|²>0; only k↔n−k frequencies may coincide. On each such 2D eigenspace, leaf-actuator rows are nonzero-scaled (exp(2πiks/n),exp(−2πiks/n)); rank drops by one iff n divides 2k(s−s0) for every s∈S. Let g=gcd(n,{2(s−s0)}). Exactly floor((g−1)/2) frequency pairs satisfy this, in each of ell+1 branches, giving exact rank (ell+1)(n−floor((g−1)/2)). Single leaf insufficient for n≥3; pair succeeds iff gcd(n,2d)≤2, with counts nφ(n)/2 odd and nφ(n/2) even. Independently computed exact rational full Kalman matrices for n=3..7, ell=1,2, selected singleton/pair sets (40 cases), all matched the formula. This check is finite; the Jacobi strict interlacing and Fourier PBH proof is unrestricted.

## originality

PASS

Best-of-knowledge original scientific contribution confined to the exact theorem beyond explicitly acknowledged prior partial coverage. Meaningful searched aliases, broader-result implications, primary source materials, and access limits are documented below.

## value

PASS

Determining exactly which terminal leaf sensors actuate the full repeated-cycle network, the entire Kalman rank for every subset, and the sharp arithmetic pair count is a natural complete control-theoretic classification. Uniformity under all positive depth-wise conductances, rooted path lengths and actuator root sets makes the noncollision rank lift substantive beyond pure-cycle gcd results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
