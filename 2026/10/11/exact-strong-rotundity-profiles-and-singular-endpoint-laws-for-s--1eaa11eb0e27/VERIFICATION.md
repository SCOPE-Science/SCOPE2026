---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Read the exact local pairwise definition eta(epsilon)=dist(f^{-1}(1), B\U(x,epsilon)); the closed outside-distance constraint matters. The hyperplane distance from (t,y) equals 1-t, attained at (1,y). For finite p, for fixed t the maximum distance to x is [(1-t)^p+1-|t|^p]^(1/p), attained with y of norm (1-|t|^p)^(1/p). This envelope is nonincreasing in t and for slice depth d has sharp radius G_p(d)^(1/p), G_p(d)=d^p+1-|1-d|^p. At p=1, G=2min(d,1) and eta=epsilon/2. At p>1 finite G is strictly increasing 0..2^p, giving inverse eta=G_p^{-1}(epsilon^p). At p=infinity the sharp radius is max(1,d), yielding eta=0 through epsilon=1 and eta=epsilon above; exact witnesses use any unit u in nonzero Y. G_p(1/2)=1 gives finite-p pivot; G_p(d)=p d+o(d) gives eta~epsilon^p/p. All endpoints and nonreflexive Y allowed; saved rational/sampled verify.py is only a consistency check.

## originality

PASS

Best-knowledge PASS for the non-Hilbert full local profile and exact slice-radius identity. Direct primary 2023 text covers eta_p2(epsilon)=epsilon^2/2 and one p-infinity coordinate-vector value at epsilon=2, while Theorem 2.6 concerns stereographic projection rather than the index. Follow-up 2024 core paper gives endpoint and qualitative criteria. Those published special cases are conceded, not counted as original; the complete p-family and different p=1/infinity transitions are the distinct claim.

## value

PASS

The exact local index, introduced and studied for Lp summand points in the focal primary work, is natural. The full radius function, attained witnesses, epsilon^p/p exposure order, universal epsilon=1 pivot and two qualitatively different endpoint jumps offer substantive exact benchmarks beyond the previously known Hilbert case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
