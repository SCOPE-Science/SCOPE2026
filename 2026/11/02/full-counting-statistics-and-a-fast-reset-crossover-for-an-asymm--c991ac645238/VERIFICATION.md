---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Exponential-time weighting gives Laplace density r k exp(-k|x|)/(2(r+z)); the asymmetric partition starts the two nonzero geometric tails at a and L-a, so the exact convergence domain is z>Dq²/L²-r. Finite-time moments follow from |K-B/L|≤1: conditional on reset times the sum of completed Gaussian increments has total diffusion time at most t, and N_t is Poisson, yielding E exp(qC_t)≤exp(Dq²t/L²) E exp(|q|N_t). The transform is strictly decreasing to zero in z and diverges at the domain edge, also at q=0. Its simple analytic root tilts the renewal kernel to a density with finite mean; the no-reset remainder becomes exp(-(r+ψ)t), an integrable decreasing forcing, so the renewal limit is strictly positive. Implicit differentiation gives curvature E_q[(K-ψ'T)²]/E_q[T]>0 since T has a density also on K=0 and both signs of K occur. The quadratic lower bound gives full slope range; exponential tightness and differentiable Gärtner–Ellis give the full LDP and the Legendre rate has positive curvature. In the fast window the dimensionless model is T'∼Exp(1), Gaussian displacement N(0,2T') and mark 1 on crossing the threshold u, 0 otherwise. Its Laplace transform decreases strictly from infinity at ζ=-1 to zero, and its simple root converges by uniform bracketing of the finite-rate roots on compact q sets. The terms discarded in the transform are exponentially small locally also on complex neighborhoods of (q,ζ)=(0,0), giving convergence of the fixed-order derivatives by the implicit equation. Expansion at zero gives the stated three cumulants, including b-3ub²+(9u²+3u)b³/4, and sub-Poisson variance/mean for u>0. At u=0 the limiting mark is an independent fair sign indicator, not a statement that the finite periodic model with nonzero remote tails is exactly a thinning. Replayed independently with `python3 /workspace/branches/replay_ratchet.py`: direct integration of Gaussian cell masses versus the resolvent agreed within 9e-15 at five interior test pairs, and nine fast-window tests at r=144 agreed with the limiting roots within 2.8e-7, with smaller errors than at r=9,36. These are bounded consistency checks only. The nested verification/ratchet_counting.py is present in the source and was inspected, not executed.

## originality

PASS

Credit the explicit asymmetric joint transform and its all-field counting law, especially the evaluated non-Poisson boundary crossover, not the mean, second-order dispersion, the symmetric nearest-site SCGF, or the standard renewal/LDP methodology in isolation. The two exact symmetric indexed records are distinct from the frozen record and materially overlap at a=L/2; their shared date does not establish order. Neither their symmetric formulas nor the exact asymmetric first/second cumulants determine the new all-field asymmetric window.

## value

PASS

The result gives an exact large-deviation description of signed completed-cell transport and identifies the diffusion-length regime in which the reset clock and success marks remain coupled. The exact non-Poisson counting law contains genuinely new predictive information beyond the established drift and dispersion, including the third rate and all-field response.

The dated certificate retains the supplied scientific assessment, sources and limitations.
