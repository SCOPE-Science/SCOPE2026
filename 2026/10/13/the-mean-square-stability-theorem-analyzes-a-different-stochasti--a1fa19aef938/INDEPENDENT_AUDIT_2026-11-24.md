# Independent mathematical audit

## correctness

PASS

For Talapatra's printed Eq. (2), translating by the strictly positive drift equilibrium adds no Itô correction and gives affine diffusion diag(alpha_i E_i*)+diag(alpha_i U_i). The nonzero constant diagonal matrix already excludes a constant equilibrium solution: its quadratic variation is strictly positive. Eq. (13) instead centers the diffusion, and Eqs. (15) and (17) and Theorems 3.1–3.2 concern the resulting centered linearized system, not directly the full nonlinear centered system or the original Eq. (2). Section 6, Eqs. (34)–(35), returns to abundance noise. For the optional short-time expansion, continuity alone needs an integrability justification. In this printed model, on the positive cone each coordinate drift is bounded above by C X_i, the drift has absolute size at most C(1+S^2) with S=sum X_i (positive saturation constants), and diffusion grows at most linearly. Localization and Itô for S^4 give uniform fourth moments on bounded time intervals by Gronwall. Positivity before explosion follows from the logarithmic coordinate equations before compact exits, and the same moment bound prevents explosion. Thus the martingale in Itô's formula for squared displacement is square-integrable on finite intervals, and its generator, of growth at most cubic in S, is uniformly integrable at time zero. Its initial expected value is the strictly positive squared Frobenius norm of the diffusion at E*, yielding the stated expansion. The frozen exact rational checker was inspected, not executed; it illustrates the affine identity but cannot verify stability or the infinite statement. No claim is made about long-time fluctuations, stationary laws, or other theorems in the article.

## originality

PASS

Pass for the source-specific obstruction in Talapatra's dual-prey article only. Neither the general nonvanishing-diffusion obstruction, its affine translation proof, nor centering noise at an equilibrium is new. The strongest indexed analogue has the same obstruction and proof pattern but identifies a defect in another published model and theorem, not this one.

## value

PASS

This is a consequential correction to a stated stability goal of a named published model. It resolves which SDE the theorem actually treats and shows that the equilibrium whose stability is discussed is not even a constant solution of the originally printed SDE. That is useful for interpretation and subsequent reuse of the theorem; the algebra alone, or a general claim about centered noise, would not justify this verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
