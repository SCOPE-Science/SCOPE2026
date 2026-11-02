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

For all integers m>=2, n>=32m on unit-conductance K_{m,n} with unnormalized graph Laplacian L, the four orthogonal spectral subspaces have L-eigenvalues 0,n,m,N=m+n. Taking e^{-tL^2} gives off-diagonal same-part entries -F_A/(mN) and -F_B/(nN) and nonnegative cross-part entries (1-e^{-N^2t})/N; diagonal entries stay positive by positive definiteness. Every row sums to one, hence its absolute row sum is 1+2 times the mass in negative off-diagonals, proving the exact attained l1/linfinity norm. Differentiating F_A,F_B yields one positive peak and one positive zero each. The proof bounds sup d_A<3m/(4n) for n>=32m, whereas the F_B peak exceeds this bound, proving unique global maximization at log((m+n)/m)/[n(n+2m)]. At 2/n^2, F_A<0<F_B, so the last negative entries recover exactly at the unique positive F_B root. The root bracketing t=c/(mn), with F_B/m ->1-c, gives tau~1/(mn); the explicit peak yields theta~log(n/m)/n^2 and norm excess~2m/n for arbitrary m>=2 with n/m->infinity. Independently constructed actual Laplacian matrices on four distinct (m,n) pairs and compared 56 double-precision kernel/norm statements at seven times per graph; maximum absolute kernel discrepancy 7.67e-14. These tests corroborate, but do not replace, the all-parameter spectral and inequality proof.

## originality

PASS

Best-of-knowledge PASS for the simultaneous sharp endpoint norm, unique attained maximum, precise final positivity horizon, and divergent timescale separation in squared-Laplacian flows on unbalanced K_{m,n}. Existing eventual-positivity theorems prove qualitatively different hypotheses/conclusions; the inspected complete-bipartite heat-kernel calculation concerns balanced graphs and the ordinary unsquared heat semigroup. Full text was read where accessible. An equivalent formula could be mechanically derived in broader spectral heat-kernel literature; no absolute priority claim.

## value

PASS

The model provides a sharply quantified counterpoint to the positivity of ordinary graph heat flow: a small transient norm excess of order m/n coexists with negative entries lasting order 1/(mn), far longer than the unique norm peak of order log(n/m)/n². The exact norm and positivity horizon are motivated operator-theoretic observables for graph biharmonic diffusion, and the divergence holds for the whole natural class of growing imbalance ratios, not an arbitrary one-off parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
