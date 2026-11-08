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

The Bloch map is diag block M=[[lambda^2 cos(theta),sin(theta)],[-lambda^2 sin(theta),cos(theta)]] and independent y multiplier lambda^2. The standard unital-qubit EB iff sum of Bloch singular values <=1 criterion is applied (not claimed new). det M=lambda^2 and tr M=2lambda x, x=(lambda+lambda^-1)cos(theta)/2. Cayley--Hamilton gives M^n=lambda^n[T_n(x)I+U_{n-1}(x)(lambda^-1 M-xI)]. For real 2x2 matrices ||A||_*^2=||A||_F^2+2|det A|, and Chebyshev identity reduces ||M^n||_* to lambda^n sqrt(4+(lambda^-1-lambda)^2 U_{n-1}(x)^2), with no division at x=±1. For sin theta=0 the norm remains 1+2lambda^(2n)>1. Otherwise norm M^2_op<1 because the sole one-step nonshrinking vector is rotated out of the z axis, guaranteeing finite EB iteration. For fixed c>0 the scaled M powers converge on compact time intervals to exp(t B_c), B_c=[[-2,c],[-c,0]], whose norm is strict contraction at t>0 because d||v||^2/dt=-4v_x^2 and c>0. This proves a unique positive crossing and convergence of discrete first index. Its limiting nuclear norm is 2e^-t sqrt(1+S_c(t)^2); lower bound S^2>=0 forces threshold >=L, with equality only at oscillatory sin(L sqrt(c^2-1))=0, precisely all c_k. No claim of uniform c(delta) or finite-delta optimum.

## originality

PASS

The exact 2026 exceptional-channel model is prior in Brandão, the unital EB nuclear norm criterion and index definition are prior in Lami--Giovannetti and Ruskai, and Cuevas et al. treat a two-use rotated damping experiment. These jointly motivate but do not entail the Chebyshev all-power criterion plus singular scaling resonance classification. No covering restricted fixed-axis optimization was established; unrestricted unitary control differs.

## value

PASS

The EB index measures operational disappearance of all reference entanglement under repeated hardware-fixed maps, not merely spectrum or defectivity. Exact all-power criterion, finite/infinite boundary, weak-noise continuum crossover and discrete resonant optimal drive ratios are a substantive classification for a canonical exceptional-point qubit channel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
