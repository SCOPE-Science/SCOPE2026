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

Using z(root)=u-v, z(leaf)=v forces mean(u)=0 and gives exact 2×2 Fourier symbols (A,E;E,L) for nonzero frequencies plus L_0. At p=1 E=0, L=-2, and exact cycle Fourier eigenvalues have zeros for even n and strict negative modes for odd. Li–Weston strict-exponent implication excludes p>1 for even; odd strictness and p=2 L_0=2(n-2)>0 put wp in (1,2). For p=1+c/n², uniform Taylor expansion, bounded-variation 1/k Fourier tail, and E=O(log n/n), L=-2+O(log n/n²) show first even mode k=2 controls threshold c*=2pi²/Cin(2pi). Independent full distance-eigenvalue comparisons checked n=3,5,7,9,11,13 at p=0,1,1.05 and numerical odd n=31,71,131 scaled cutoff approaching constant; finite checks not asymptotic proof.

## originality

PASS

Bare odd cycles share the leading cosine-integral coefficient and classical strict-negative-type principles are known. Novelty assessed is its survival under pendant decoration plus exact two-orbit full finite-order criterion, rather than original discovery of the constant.

## value

PASS

Sunlet is a natural full-density geometric perturbation of the cycle, changing distances among a macroscopic fraction of vertices. The all-frequency analysis gives a two-orbit exact finite-order test and a sharp quantitative odd-parity stability law for Schoenberg PSD kernels; significant preservation rather than an isolated numeric coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
