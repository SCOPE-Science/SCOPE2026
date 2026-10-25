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

The checks below concern only the mathematical claim in this package.

- **Point selection:** Hoeffding's inequality gives a fixed-frequency tail \(4e^{-Nt^2/4}\). A grid with \(O(N^4)\) points and threshold \(A\sqrt{\log N/N}\), for sufficiently large \(A\), has positive probability of satisfying the desired bound at every grid point. The derivative estimate \(|D_N'|\le7\pi\) extends the bound to all \(|\xi|\le N^3\).
- **Fourier calculation:** Direct integration gives the exact sinc-times-empirical-sum formula with \(r_N=\varepsilon N^{-1-b}\). The frequency ranges below \(N^{1+b}\), between \(N^{1+b}\) and \(N^3\), and above \(N^3\) give the exponent \(\alpha=1/[2(1+b)]\) with a logarithmic factor. Choosing \(\rho<\alpha\) absorbs that factor.
- **Finite-scale obstruction:** The mean-zero atom has support in an interval of length \(4/N\) and \(L^\infty\) norm \(N/4\). The small bump radius ensures its own contribution remains positive for \(\theta L\le k\le bL\); the center-gap condition eliminates earlier bumps, and later bumps cannot enter the negative interval.
- **Mixture:** The weights \((q-1)q^{-m}\) sum to one. The earlier components are suppressed by \(2^{-k}\|K_{N_\ell}\|_\infty\), and the later components have \(L^1\) tail \(O(q^{-m})\). The remaining level sets have measure \(\gtrsim(b-a)L_m\), giving a weak-\(L^1\) lower bound \(\gtrsim q^{m+1}\).
- **Limits:** The construction is one-dimensional and existential. It gives a separate measure for each \(\rho<1/2\), not a single measure for all such exponents, and it does not include \(\rho=1/2\).

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
