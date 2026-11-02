---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Independently reconstructed every quantified step for real n>=3,t>0. Averaging arbitrary positive definite ellipsoid pullback Q under signed permutations preserves comparison and forces scalar I, so Euclidean coordinates are BM optimal. On Euclidean sphere, N_t² equals maximum over rank-two matrices e_i e_i^T+t eps eps^T with trace 1+nt, nonzero eigenvalue product t(n−1), giving L_n(t) and one-spike eigenvector. For minimum, normalize ||x||infinity=1, fixed ℓ1 mass s=k+theta transfers maximize ||x||2² at k ones and one theta; lower H_k=(1+t(k+theta)²)/(k+theta²) has derivative sign tk(k+theta)(1−theta)−theta, strictly decreasing from positive to negative, so minimum at integer endpoints 1/k+kt. Supports switch at 1/[k(k+1)]. Universal tuning lower bound uses k=floor sqrt n, L>=max(1,nt) and m<=1/k+kt to yield d²>=kn/(n+k²); t=1/n gives L=1+1/sqrt n and m>=2/sqrt n, proving n^(-1/4) inf_t d→1/sqrt2. An independent 3600-sample/36-exact-witness check is only corroborative, not proof. All 7 current Git files were read; assigned root tree reassembled from blob entries and current same blob identities.

## originality

PASS

Best-of-knowledge: the unrestricted real n>=3 quadratic mixed-norm Banach–Mazur profile, all k-sparse support transitions, and sharp optimized n^(1/4)/sqrt(2) law are not established by the inspected two-dimensional same-norm predecessors or the broader papers on direct sums, ordinary ell_p, or linear/polyhedral mixtures. Exact two-dimensional quadratic endpoint profile and classical signed-permutation averaging are prior mathematics; no claim of absolute bibliographic priority.

## value

PASS

This natural quadratic interpolation of the two opposite classical coordinate norms has nontrivial exact Hilbert distortion in each real n>=3 and all positive weights. It resolves the competing one-spike spectral versus equal-amplitude sparse geometry, complete discrete support-change thresholds, and an optimized n^(1/4)/sqrt2 asymptotic over ALL parameters; these are mathematical benchmark quantities not determined by the planar endpoint or generic ellipsoid averaging lemma. The optimization does not falsely claim an exact finite-n optimal parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
