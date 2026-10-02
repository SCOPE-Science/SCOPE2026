---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For the shifted-Erlang ENSO feedback normalization printed in arXiv:2609.08127v1, scaling the coefficient by \(q=|G(i\omega_f)|\) applies the attenuation twice rather than compensating it; exact one-frequency amplitude matching requires multiplication by \(q^{-1}\), phase matching uses \(\tau_m+n\arctan(\omega\Delta)/\omega\), and the same transfer function yields the stated autonomous Hopf anchor.

## Correctness — PASS

From G(iω)=exp(-iωτ_m)(1+iωΔ)^{-n}, its magnitude is q=(1+(ωΔ)^2)^{-n/2}. Linearization of the feedback therefore multiplies a sinusoid by Aκq, so the printed A=aq gives aκq^2 and exact amplitude compensation is A=a/q. The transfer phase gives τ_ph=τ_m+n arctan(ωΔ)/ω, and arctan x<x proves τ_ph<τ_m+nΔ for positive width. Substituting λ=iΩ into λ+aκ exp(-λτ_m)(1+λΔ)^{-n}=0 gives the package's amplitude and phase Hopf equations. An independent numerical recomputation reproduced q=0.784672478417 and 0.450424982227, the q^2 gain ratios, delay mismatches, and all quoted first Hopf branch values to the shown precision.

**Checked sources.** Assigned RESULT.md at tree 14324f370f7c58b9f7d5ebbefd7e00af3b95f766; artifacts/verify_frequency_match.py blob 4c3a35008ba8da9d86364442dae38351f06515a5; Steele--Keane--Krauskopf, arXiv:2609.08127v1; Morărescu--Niculescu--Gu, SIAM JADS 2007

**Residual risks.** The full source preprint was not retrievable through the available open-access route in this run, so the printed normalization formula was checked from the frozen assigned package while the source abstract independently confirms the attenuation-rescaling motivation.

## Originality — PASS

General shifted-gamma/Erlang transfer functions and stability-crossing theory are old and are not claimed as new. Searches found no prior source-specific correction showing that the particular 2026 ENSO paper's printed reciprocal scaling doubles attenuation, nor the combined corrected gain/phase comparison and source-parameter Hopf anchor. The published mathematical corpus returned only the assigned record for this specific normalization.

### Equivalent formulations

Equivalent frequency-response language was searched; the source-specific algebraic correction was not found elsewhere.

### Broader coverage

The broader literature does not imply that the source made this particular normalization error without substituting its printed parameter convention.

### Exact database or table

No numerical database controls the claim; the relevant exact check is algebraic substitution into the source's transfer function.

### Claim versus prior implication

The correction is not a corollary of a prior claim that already used the same normalization; it is a contradiction obtained from the source's own transfer function.

**Checked sources.** https://arxiv.org/abs/2609.08127; https://doi.org/10.1137/060670766; published semantic-result search

**Residual risks.** The exact source formula could not be re-extracted from the primary PDF in this run; the assigned frozen package is therefore the formula-level evidence. A later source revision could correct the normalization.

## Value — PASS

This is more than a cosmetic normalization check: at the wider parameter example the printed convention leaves about 20.3% of the intended small-signal gain, while the mean/phase mismatch is about 24.5 days, and the exact Hopf anchor changes branch admissibility. Because the scaling underlies the paper's cross-width interpretation, identifying and quantifying the mismatch is a motivated mathematical correction.

**Residual risks.** The result does not show that the source's numerical continuation itself is wrong; it corrects the interpretation of what the parameter scaling preserves.

## Limitations

- The correction concerns the linear filter interpretation and the unforced equilibrium spectrum; it does not invalidate numerical continuation for the parameter family actually computed.
- One-frequency matching does not produce global nonlinear equivalence of the seasonally forced systems.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
