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

For the exact final claim, two real lifts solve dX=−V'(X−Y)dt+sqrt(2D1)dW1, dY=−V'(X−Y)dt+sqrt(2D2)dW2 with independent W and independent uniform stationary initial torus point, L,D1,D2>0, real V∈C²(T_L). Relative R=X−Y mod L is Brownian with generator (D1+D2)∂², so A_t=∫F(R_s)ds with F=−V' is the common drift. Conditioning on the full Brownian increment paths and averaging the independent Haar R0 gives E[A_t|W1,W2]=0; this justifies zero drift-noise cross terms, not merely stationary marginal independence. The heat semigroup gives K(s)=Σ_{n≠0}k_n²|Vhat_n|²e^{−(D1+D2)k_n²s}; C(t)=2∫_0^t(t−s)K(s)ds and the whole covariance matrix has diagonal 2D_i t+C and off-diagonal C. Since V∈C², Σ k_n²|Vhat_n|² is finite, so C''(t)=2K(t) also at 0+; stationary currents give σ=(D1⁻¹+D2⁻¹)C''(0)/2 and C(t)/(2t)→Var_Haar(V)/(D1+D2). Distinct strictly increasing λ_n for n≥1 and positive summable coefficients give unique ideal Laplace inversion of every Fourier power, not its phase. At fixed σ>0, h_t(λ)=∫_0^t(t−s)e^{−λs}ds strictly decreases for t>0 and λ>0, forcing all nonzero Fourier mass to |n|=1 for sharp finite-time and long-time bounds; only fundamental sinusoids with amplitude²=2σ/(c k1²) attain equality. σ=0 means V constant. Independently reconstructed Git tree 13cfe87... from all 7 actual Git blob IDs. Separately computed sample D1=.7, D2=1.3, L=2π, V=cos z+.4cos(2z+.37): C(1.5)=.6224468285341, σ=1.8021978021978, ΔD=.29, Kubo trapezoid .6224469723; bounded direct SDE MC of 12k paths, 500 steps gave .65913, a noisy consistency check only.

## originality

PASS

Best-of-knowledge: the all-time cross-displacement covariance itself is an application of established periodic Kubo/Green–Kubo dispersion theory, in particular the general time-dependent tensor formula of Guérin–Dean (arXiv:1509.02733, §§II–III). The chase-and-run uniform stationary distribution and exact entropy-production rate are expressly prior (Zhang–Garcia-Millan, arXiv:2209.09721, Eq. 9), and Benois et al. (arXiv:2307.05408, Sec. VI) provide overlapping long-time tracer diffusion. The assessed final claim additionally combines full ideal covariance-to-Fourier-power identification, σ=(c/2)C''(0), a sharp all-time fixed-σ waveform bound and a unique (up to phase/additive constant) fundamental sinusoid equality class. These additional coupled inverse/variational conclusions were not established in the relevant primary material inspected. Their Fourier-semigroup proof is short and classical in technique, so possible implicit priority in general inverse Taylor-dispersion or optimization literature remains a real risk. No failed search is treated as proof of novelty.

## value

PASS

The same naturally observable stationary joint unwrapped displacement curve encodes the complete phase-blind interaction power spectrum and total pathwise entropy cost in an exactly solvable nonreciprocal chase-and-run model. Its sharp, attainable spectral first-harmonic transport–dissipation frontier holds at every positive observation time and has an explicit equality class, not merely a long-time diffusion coefficient or a numerically selected waveform. The object/invariant are physically and mathematically motivated by active-matter transport, response/covariance-based inverse problems and optimal energy allocation across Fourier modes. Though the Fourier inequalities are elementary after exact reduction, the full inverse and all-time optimization classification answers specific natural questions beyond a normalization check; no general mixtures or robust inverse theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
