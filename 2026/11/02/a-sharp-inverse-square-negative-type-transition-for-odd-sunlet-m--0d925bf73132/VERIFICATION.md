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

The two circulant layers have Fourier blocks M_k=[[a,b],[b,c]] and one zero-mode contrast. At p=1, b=a,c=a−2, a_even=−1/[4cos²(pi k/(2n))], a_odd=−1/[4sin²(pi k/(2n))], giving all blocks uniformly negative definite and H=−2; a three-prong metric star bounds p≤log_2 3. Set p=1+t/n²; after separating the common linear/log n factor, each nonzero block receives t F_{n,k}J+o(1) uniformly, with F_{n,k} discrete coefficient of xlog x on circle. Fixed odd k have huge negative eigencomponent, and fixed even k converge to (−1/4+t A_k)J−2 diag(0,1), determinant 1/2−2tA_k. For even k≥2, A_k=I(pi k)/(2pi² k²), strictly maximized at k=2 by monotonic I(u)/u² for u≥2pi; uniformly high k controlled by trig-polynomial approximation and spectral margin. Thus T=1/(4A_2)=8.097627..., below T strict negative type eventually, above T mode k2 positive eventually; sandwich yields limit. The 8 independently diagonalized complete finite distance matrices at p=1 corroborate but do not establish the asymptotic.

## originality

PASS

Robertson (2020) supplies finite-metric maximal generalized-roundness/determinantal framework, but the inspected primary results do not address the growing odd sunlet two-layer Fourier family or the asymptotic coefficient. Published odd-cycle fourth-power spectral work concerns a different invariant and does not imply powered-distance negative-type threshold for sunlets.

## value

PASS

Maximal generalized roundness/negative type governs Hilbert snowflake embeddings of a natural two-orbit unicyclic graph metric. The n^(−2) transition and explicit mode-selection constant are nontrivial spectral asymptotics not an arbitrary finite test. It does not claim every finite n has mode 2 critical or exact wp_n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
