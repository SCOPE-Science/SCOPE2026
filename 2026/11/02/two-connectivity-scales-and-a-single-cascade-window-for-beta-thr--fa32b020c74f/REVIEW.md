# Review: Two connectivity scales for beta-threshold networks

## Correctness

PASS. The beta CDF follows by direct integration. The single-maximum theorem follows from the exact derivative of a three-term auxiliary polynomial times a beta survival factor, whose derivative changes sign only once. At \(b\ge4\), degree two is subcritical while degree three is supercritical, so the upper root is unique. Uniform binomial/Taylor expansions at degrees proportional to \(b\) and \(b^2\) prove distinct linear and quadratic scales, including the constant term \(-13/18\) for the continuous cutoff. The accompanying checker reproduces the finite exact checks; finite enumeration is not the proof. Risks: only the vulnerable branching condition is classified; it is not a full cascade-size calculation.

## Originality

PASS under qualified self-review. Watts (2002) proves the general cascade-window mechanism. Meador-Woodruff and Ghoshal (arXiv:2610.33927v1, October 24, 2026) provide the general vulnerable-branching condition and beta-threshold analysis with Poisson/beta-binomial degrees and fixed-mean rescaling; their main results do not state the unscaled \(\mathrm{Beta}(2,b)\) regular-degree unimodality or two connectivity scales. Fontanari (arXiv:2606.25921) studies a fully connected Granovetter process, not this regular-network branching optimization. The general branching formula and qualitative bounded window are not novel; the precise all-parameter shape result, linear optimum, quadratic cutoff and constant correction are the claim. Risk: an unindexed exact treatment could subsume it; Fontanari's full text was not fully accessible.

## Mathematical value

PASS. The natural one-neighbor vulnerability criterion of a canonical social contagion model has a structural shape theorem for every beta parameter and a sharp feasibility threshold. The robust separation between the linearly growing optimal connectivity and quadratically growing last viable connectivity is a genuine sensitivity-versus-feasibility distinction, not simply a recomputation of one network value. It is potentially useful as a benchmark for more complex network degree structures. It does not imply robustness for clustered networks or fixed-mean threshold families.

Self-review: passed. Independent audit: not yet performed.
