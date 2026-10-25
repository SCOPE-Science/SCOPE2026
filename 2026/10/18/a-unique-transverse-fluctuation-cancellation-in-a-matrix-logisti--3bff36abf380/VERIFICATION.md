---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For H=[[x,z],[conj(z),y]], the map F_b=D_b H(I-H)D_b has z+=2b(1-x-y)z, and the invariant diagonal orbit y=c_b=1-b^-2 is logistic x+=4x(1-x) with stationary arcsine. Circle conjugacy x=(1-cos(theta))/2 gives log-normal cocycle log|b(cos theta-cos beta)|, beta=acos(2c_b-1), mean log(b/2) by exact log-sine Fourier series. Transfer P kills odd cosine modes and halves even frequencies, so ||P^j psi||_2=O(2^-j), yielding an L2 martingale-coboundary decomposition and the standard stationary reverse-martingale CLT with σ²=2 sum_{q odd>=1}q^-2(sum_{j>=0}2^-j cos(2^j q beta))². Nonnegative terms plus Fourier uniqueness show σ²=0 iff the weighted even orbit-point measure is π-rotation invariant; its mass-one level-0 pair must consume all mass-one tail on shifted atoms, which forces β=π/3 or the self-shift β=π/2. Here β>acos(1/3)>π/3, hence only β=π/2, i.e. b=sqrt2. At b=sqrt2 log-cocycle telescopes via double-angle sine product and is L2 bounded; at b=2/sqrt3 β=2π/3 gives σ²=π²/3. Independently checked truncated special cosine spectrum approaching π²/3; this finite number is not the CLT proof.

## originality

PASS

Pawela–Życzkowski 2023 introduces Hermitian matrix logistic map, diagonal chaotic channel and spectral/transfer behavior. Its model and the logistic circle conjugacy are prior, as are Gordin-type martingale CLTs. The model-specific off-diagonal normal derivative variance formula and classification of a unique cancellation parameter are not stated in inspected original PDF including Appendix A. An earlier singular-observable CLT/coboundary theorem might imply this specialized zero locus, but not identified in actual targeted searches.

## value

PASS

The transverse Lyapunov exponent log(b/2) is constant-form throughout a stable diagonal channel family, but intermittent finite-time contraction fluctuations can vanish at precisely one natural resonance. The full variance function, exact zero set and explicit π²/3 contrasting value are meaningful quantitative normal-hyperbolicity diagnostics, rather than an arbitrary numerical slice. Scope is stationary infinitesimal normal dynamics only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
