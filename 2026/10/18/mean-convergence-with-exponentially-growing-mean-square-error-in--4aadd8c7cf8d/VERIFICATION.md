---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the stated (x,h,e) coordinates the two updates are exactly A and B_eta, with independent equiprobable branches. A fresh rational calculation found positive leading minors for W and H=E[BᵀWB]−1.3W and reproduced both unit Lyapunov differences and positive minors for R and Q. Thus the full-feedback quadratic energy grows at least as (61/5000)1.3^t, the full-feedback mean contracts in R-energy, and the moderated mean-square Q-energy contracts by at least the factor 1−1/λ_max(Q). To get the stated iterate bound, write M_t=max_{j≤t} E x_j². The iterate update gives E h_t²≤4M_t/s² also at t=0; at η=1 only dropout contributes to E e_{t+1}². Applying (e+d)²≤(3/2)e²+3d² to d=x−h gives E e_{t+1}²≤(3/4)E e_t²+3(1+4/s²)M_t. Since e_0=0, this bounds E||v_t||² by (13+52/s²)M_t=5213M_t. Using tr(W)=4771/5000 now gives 61/(4771·5213) times 1.3^t. No claim of pointwise second-moment divergence is inferred.

## originality

PASS

Pass for the quantitative separation of first- and second-moment behavior together with exact same-step recovery in the same EControl recursion. Do not credit qualitative maximal-feedback nonconvergence on its own: the later indexed erasure frontier covers that component, and an earlier different error-feedback model exhibited the general moment-gap phenomenon. The inspected sources do not give the combined fixed-initialization 1.3^t iterate bound, geometric mean convergence, and η=1/2 recovery at the identical compressor and step.

## value

PASS

The example isolates the effect of the feedback coefficient while holding the standard initialization, compressor, objective and step fixed. It shows why stability of the expected model is an unreliable diagnostic of mean-square behavior even in a scalar quadratic and supplies exact reproducible certificates for the unstable and stable regimes, without claiming to contradict a sufficient small-step theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
