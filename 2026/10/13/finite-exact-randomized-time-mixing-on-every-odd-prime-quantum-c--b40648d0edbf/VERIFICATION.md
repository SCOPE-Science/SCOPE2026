---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Set p odd prime, m=(p-1)/2, b0(d)=1, bj(d)=2cos(2πjd/p), Fourier spectral eigenvalues λj=2cos(2πj/p). The character sums S0=p,Q0=2p-1,Sd=0,Qd=p-1 for d!=0 are exact. Haar independent phases have zero offdiagonal correlation; uniform permutations of (m+1)st roots give -1/m, and 50:50 mixing c=-1/(p-1). Thus E Fd=((1-c)Qd+c Sd²)/p²=1/p at each d. Irreducibility of Φp proves independent frequency gaps λj-2, hence all tails of physical phase flow are dense on (S1)^m. Haar full support puts its barycenter in ri conv K; its midpoint with finite permutation barycenter is also relative interior, permitting exact physical finite convex combination via convex-density lemma; affine Carathéodory gives <=m+1 atoms with t>T. The analytic proof, not approximate numerical examples, establishes arbitrary p and all vertex pairs.

## originality

PASS

Earlier single-time no-go, approximate time mixing, and standard Cesàro average results have different quantifiers; freely chosen finite time law with all t>T and at most (p+1)/2 atoms is not implied by any inspected theorem. Main novelty is an exact interior convex-hull certificate, not mere phase-density approximation.

## value

PASS

Quantum time-sampling exact uniformity is a natural observable for coherent transport on prime ring graphs. The proof turns known approximate one-time behavior and single-time impossibility into finite exact convex reachability with a uniform law, arbitrary time delay and linear support bound. The needed precise exactness and probability matrix matter beyond a trivial reparameterization, though explicit/optimal times remain unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
