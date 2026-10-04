# Same-model review

## Correctness
**PASS.** The endpoint proof is exact. Near \(z=0\), the printed density is asymptotic to a positive constant times \(z^{-2+2r/\sigma_{11}^2}\), giving local integrability exactly when \(r>\sigma_{11}^2/2\). Near infinity the combined power is exactly \(-4\), so no additional tail restriction is needed. Section 4 then uses the density in both \(R_0^E\) and Theorem 4.2. The packaged exact-rational checker independently confirms the exponent identities and critical witness.

## Originality
**PASS.** The general noise-shifted logistic threshold is established background and is not claimed as new. The accepted claim is narrower: Xu and Wang's particular Section 4 threshold is undefined on part of its printed theorem domain because the cited density is not normalizable there. Exact DOI/title/alias/condition searches in the scientific database and web literature found no correction or prior record stating this source-specific implication. The cited 2018 predecessor could not be inspected in full after public and authorized-access attempts; this remains a residual priority risk rather than evidence for novelty.

## Value
**PASS.** The issue changes the valid parameter domain of a principal extinction criterion and the claimed weak-convergence conclusion. It is especially relevant in the high susceptible-noise regime, exactly where stochastic extinction criteria are meant to differ from deterministic ones. The correction is also minimally invasive: adding \(r>\sigma_{11}^2/2\) makes the displayed invariant density normalizable, while the paper's numerical extinction examples already satisfy it.

## Closest literature and limitations
The closest source is Liu, Jiang, Hayat, and Ahmad (2018), DOI 10.1016/j.amc.2017.09.030, cited by Xu and Wang for Lemma 4.1. Its full text was not available in the completed checks. Zhang and Yang (2022), DOI 10.3934/dcdsb.2021177, confirms that threshold classification for one-dimensional logistic systems with nonlinear perturbations is established background but does not imply the source-specific correction. The present result does not determine epidemic dynamics when \(r\le\sigma_{11}^2/2\), nor does it invalidate the reported examples with \(r=0.5\) and \(\sigma_{11}=0.6\).

Same-model review: passed. Independent audit: not yet performed.
