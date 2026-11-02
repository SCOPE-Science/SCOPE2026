# Scientific review

## Correctness

**PASS.** Translating a uniform simplex gives the exact probability for any collection of specified gaps to exceed chosen thresholds. Distinguishing coincident versus distinct gap indices gives the complete covariance formula, and the bivariate generating polynomial follows by an explicit product expansion. Factoring the covariance isolates a function strictly decreasing until the two thresholds sum to one, thereafter constant. Its terminal sign and the strictly positive nondegenerate variance at equal thresholds establish one zero, a terminal zero interval, or no zero, with every boundary handled. The standalone checker verifies 1,640 grouped exact/numerical checks, including a separate calculation using the full bivariate count distribution and direct two-spacing integration.

## Originality

**PASS, qualified.** The uniform-simplex law and limiting covariance kernel are established prior theory. In particular, the classical Shorack limiting process is stated explicitly in Lo (2014, Theorem 1, equation (2.1)) and is not claimed as new. Related surveys, empirical-spacing strong laws, extreme-spacing counting approximations and maximum-spacing papers were searched and compared. Their identified statements do not contain or imply the exact finite-sample single-zero sign phase boundary without a further finite derivation. Highly plausible historical papers inaccessible in full leave residual priority risk; searching titles or abstracts alone has not been used to certify whole-document noncoverage.

## Mathematical value

**PASS.** The object is a canonical empirical-survivor process of circular spacings; the joint behavior at two thresholds is important for multiscale goodness-of-fit statistics and extreme-gap counts. The exact covariance has a negative region despite pointwise nesting, and its full continuous parameter domain admits a sharp, explicit phase boundary valid at every sample size. It also identifies a nontrivial interval of exactly zero covariance at the critical radius, including the special deterministic two-gap case. These structural conclusions are not merely a restatement of the known first-order Gaussian limit.

## Prior work and limits

The closest available full-text comparison is Lo, *Gaussian Approximations and Related Questions for the Spacings Process* (arXiv:1406.7427v1, Sections 1–2), whose covariance is asymptotic rather than finite. Mijatović–Vysotsky (arXiv:1508.00944v1) discusses maximal spacings, not the two-threshold covariance phase. Pyke (1965), Koziol (1977), and Beirlant–van Zuijlen (1985) are relevant older sources whose full text was not accessible and whose implicit reach cannot be ruled out. The proof is for uniform circular one-step spacings only.

Self-review: passed. Independent audit: not yet performed.
