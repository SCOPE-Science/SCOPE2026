---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and limits

The proof is analytic and self-contained except for the published characterization of absolutely minimum-attaining Toeplitz symbols and the standard Toeplitz norm identity. Its essential checkpoints are:

1. The Toeplitz compression isometry \(\|T_h\|=\|h\|_\infty\) follows from normalized Hardy reproducing kernels and boundary radial limits.
2. For any continuous symbol \(h\), the constant-modulus lower bound is \((M-m)/2\); polygonal nowhere-zero approximation constructs arbitrarily close continuous constant-modulus upper witnesses. For \(m>0\), \(r h/|h|\) realizes the bound exactly.
3. The chirp's flat bump extends smoothly across both endpoints, despite oscillation of \(e^{i/t}\). The exact error radius constraints give \(\nu=1/2\), and the cosine positivity would persist at all small positive phases, contradicting phase density.
4. For \(L=\log(1/\varepsilon)\), \(s=2\arcsin((1+L)^{-1/2})\), an explicit approximation has total phase variation bounded above by \(1/s-1/(2\pi-s)+\pi\). On the lower arc defined by \(s_\alpha=2\arcsin((1+\alpha L)^{-1/2})\), every candidate has variation at least \(1/s_\alpha-1/\pi-4\pi/3\). Limits and \(\alpha\uparrow1\) prove the asymptotic coefficient \(1/2\).

Finite computations are not an infinite proof. A numerical monotone-parameter sanity check of the upper coefficient was performed, but the statements above follow analytically. The impossibility of a best continuous-symbol approximant does not imply impossibility for all discontinuous absolutely minimum-attaining Toeplitz symbols. Mathematical originality remains subject to unindexed literature. Independent audit has not been performed.
