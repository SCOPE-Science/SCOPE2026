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
# Verification and reproducibility

The result concerns a mathematically exact open interval and closed-system invariant initial measure. Its key independently checkable algebraic identity is \(x\mapsto u=x^{-\alpha}\), under which the LSV left branch acts as \(u\mapsto u(1+2^\alpha/u)^{-\alpha}=u-\alpha2^\alpha+O(u^{-1})\). Since each survivor remains below \(h_n\), the Taylor remainder is bounded uniformly by \(C_\alpha h_n^\alpha\) per iterate. Repeating at the endpoint gives \(a_n^{-\alpha}=h_n^{-\alpha}+\alpha2^\alpha n+O(nh_n^\alpha)\); the error relative to \(h_n^{-\alpha}+n\) is \(o(1)\) for **every** sequence \(h_n\to0\).

The analytic input about the closed invariant density is recorded explicitly in RESULT.md with source Korepanov–Wei–Wormell, §6, equations (6.1)–(6.3), Lemma 6.3. The leading coefficient is \(\rho_\alpha(1/2)/2^{\alpha+1}\), and integration yields \(K_\alpha\). The conditional beta law follows from ratios of this regularly varying interval mass. The path convergence uses the displayed uniform estimate after multiplication by \(h_n^\alpha\) or division by \(n\), on beta-parameter compact sets excluding only limiting probability-zero endpoints.

As a supplemental finite sanity check, at \(\alpha=1/2\), \(n=4000\), \(\lambda=1\), and cutoffs \(h_n=n^{-\beta}\) for \(\beta\in\{1,2,3\}\), repeated numerical inversion of the increasing left branch gave ratios \(a_n/(h_n^{-\alpha}+\alpha2^\alpha n)^{-1/\alpha}\) approximately \(1.002804\), \(1.000166\), and \(1.00000009\), respectively. These computations support the algebra but are not the proof of the asymptotic claim; no numerical certificate is required for the main theorem.

No result is asserted for \(\alpha\ge1\), for cutoffs failing to tend to zero, or for within-orbit varying absorbing boundaries. Path convergence by itself does not establish convergence of expectations for unbounded observables. Literature comparisons do not constitute formal priority certification.
