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

On vertices (i,a) distance is min(|i-j|,n-|i-j|)+|a-b|. The matrix separates via layer parity into circulant A+B and A-B with Fourier coefficients h_r=e^(-tr²)+e^(-t(r+1)²) and g_r=e^(-tr²)-e^(-t(r+1)²). For t>=1, the symmetric-band spectrum has a uniform positive diagonal-dominance bound. For the antisymmetric band, g_1 dominates sum_{r>=2}r²g_r, so its trigonometric function decreases strictly on θ∈(0,π), and the worst sampled angle is exactly π for even n or π-π/n for odd n. An explicit derivative estimate gives strict increase F_n'(t)>0.5e^-t; its value at t=1 is negative n>=20 and its limit is 1, proving a unique t_n>1, all t>=t_n PSD and t>t_n PD, thus also last-failure supremum t_n without claims on t<1. Endpoint anti nullity is one even, two odd. Uniform Gaussian tails yield even t_n=t*+O(e^-n²/4); Taylor at π-π/n yields odd t_n=t*-(π²Q(t*)/F'(t*))/n²+O(n^-4). Independent Fourier eigenvalue and root checks for n=20,21,22,31,40,41,60,61 produced t*=1.0378840547056853, even roots indistinguishable at quoted precision and odd n=21 root=1.0302750, n=61 root=1.0369825. These are numerical corroboration, not the global monotonicity proof.

## originality

PASS

General negative-type criteria, all-bandwidth geodesic Gaussian obstructions, and prism ordinary-distance spectra are prior art. Here the exact squared-shortest-path kernel on a discrete circular ladder yields a specific unique last-failure threshold and parity-split asymptotics via rung-mode decomposition; the inspected primary papers do not directly cover this. Priority under older circulant-covariance spectral methods remains a real but bounded uncertainty.

## value

PASS

An exact graph-Gaussian positive-semidefiniteness bandwidth cutoff is a natural non-Euclidean kernel invariant, and rung antisymmetry makes the limiting cutoff nonzero. The even/odd finite-size scale separation, endpoint rank defect, and explicit asymptotic constant provide useful sharp graph-kernel design benchmarks beyond a yes/no negative-type result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
