# Independent audit — 2026/09/14/046

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `b36a62de7fdcb00cdff40235ba9e801ce7b0f4fb` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**REPAIRED** — The environmental transfer is plausible and the Cox Laplace exponent has the expected time-reversed BPRE weights, but two filed statements were wrong as written. First, with the record's translation convention T_b x=x+b, a PPP with intensity a e^{-x}dx shifted by -log c has intensity (a/c)e^{-x}dx, whereas the filed Laplace functional and maximum law require a c e^{-x}dx. The coordinate must therefore be iota_k + log(upsilon W). The same sign inconsistency is visible between equation (18) and Corollary 3.2 / the marked intensity in the homogeneous Dyszewski-Gantert source. Second, deterministic centering is not impossible under the stated E1 alone: a deterministic environment is a counterexample, and sqrt(n) fluctuation requires at least nonzero finite variance of log m_0 (or another explicit fluctuation hypothesis). The corrected claim scopes this statement and fixes the artifact path.

## Originality

**PASS_WITH_CAUTION** — The closest inspected prior is the homogeneous Weibull BRW theorem of Dyszewski-Gantert; the BPRE prior of Bhattacharya-Palmowski treats regularly varying tails. I found no source stating the corrected Weibull-BPRE Cox limit with random d_n(Y), the r=2/3 correction, and time-reversed environment decoration. Search absence is not a priority proof, so the repair does not claim absolute priority.

## Value

**PASS** — A correct Weibull-BPRE extremal-process theorem would connect two established but distinct lines of work and the environment-dependent centering and reversed decoration are scientifically substantive. The corrected statement removes overclaims without reducing the main theorem to a routine finite computation.

## Literature/evidence checked

- [Dyszewski–Gantert, The extremal point process for branching random walk with stretched exponential displacements](https://arxiv.org/abs/2212.06639): Homogeneous Weibull BRW; equation (18), Corollary 3.2, and marked intensity were compared directly.
- [Bhattacharya–Palmowski, Extreme positions of regularly varying branching random walk in random environment](https://arxiv.org/abs/2101.05369): BPRE extremes for regularly varying displacements; nearest environment prior.

## Limitations of this audit

Literature comparisons are claim-specific and do not constitute an exhaustive priority proof. GitHub was read only. Computations described as independent were reconstructed from stated finite data or supplied artifacts; no inaccessible paper is claimed as read.
