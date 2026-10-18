---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The star center Schur complement is P=I-J/n. Under the specified ordered SampleClique law each i<n independently chooses a uniform later parent and creates a tree edge of conductance (n-i)/n. Each possible edge has expected conductance 1/n, proving E[T]=P. Backward induction on pendant arrivals yields E[R_T(i,j)]=n/(n-i)+(n-i-1)n/(n-i)=n for all distinct vertices and every n>=2. Double-centering E[R] yields E[T^dagger]=(n/2)P, and deterministic last edge (n-1,n) of resistance n gives Rayleigh quotient n/2 and lambda_min(T|1perp)<=2/n. Independently replayed exact fraction enumeration over all (n-1)! parent maps for n=2..7; no finite cutoff is used as the infinite proof. Nullspace centered on 1 and reciprocal weight conventions are explicit.

## originality

PASS

The primitive and unbiased mean Schur complement were known, but the exact isotropic n/2 pseudoinverse inflation and deterministic resistance obstruction are not statements of the inspected algorithm descriptions. Other sparse elimination results control different algorithms or repeated samples. The new backward tree resistance induction, not merely Jensen convexity, supplies the sharp observable. Open-source limitations remain.

## value

PASS

Effective resistance and the pseudoinverse are standard inverse-sensitive invariants of Laplacian solvers. A dimension-growing exact inverse bias for the actual one-tree local replacement exposes a sharp mathematical boundary of primal unbiasedness. It is a structural identity on all n, not an arbitrary test instance and not a claim about entire factorization performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
