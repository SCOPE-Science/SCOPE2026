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
# Verification

The proof was checked against the published translation-invariant system for the three-loop compatibility graph.

1. Dividing the two equal-loop equations gives \(z_1/z_2=((1+z_1)/(1+z_2))^k\). Solving this relation with \(r=e^{2s}\) yields the stated pair \((z_1,z_2)\) reversibly.
2. Substitution into \(c=z_1/(1+z_1)^k\) yields \(c_k(s)\). The nonloop coordinates then sum to \(S-m_k(s)\), which gives the exact total-activity formula and its positivity condition.
3. The merger expansion was derived through order \(s^4\). Exact rational coefficient arithmetic gives \(Q_{k,\lambda_*}=0\) and the negative quartic coefficient
\[
-\frac{\lambda_*}{c_*}\frac{k(k+1)(37k^2+110k+37)}{1080(k-1)}.
\]
4. The large-\(s\) comparison \(S_{k,\lambda}(s)=O(e^{(2-2/k)s})\) versus \(m_k(s)\sim e^{2s}\) forces a finite admissibility endpoint. For \(\lambda>\lambda_*(k)\), continuity then gives a branch maximum above the merger level and two nonsymmetric parameters for every intermediate level.
5. A separate intermediate-value argument proves existence of a symmetric positive solution for the same total activity. Summability gives membership in \(\ell^{(k+1)/k}\), so the source's normalisability criterion applies.
6. `verify_three_loop.py` replays the branch substitutions and exact coefficient identities. Its expected successful output is `VERIFY_OK exact_orders=2..100 residual_cases=39 worst_residual=5.274e-16 k2_threshold=49/9`.

Finite checks are corroborative only. No exact global count for \(k>2\), uniqueness of the branch maximum, extremality, stability, or thermodynamic dominance is asserted.
