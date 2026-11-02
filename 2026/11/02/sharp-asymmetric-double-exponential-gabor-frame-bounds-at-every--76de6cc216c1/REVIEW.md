# Scientific review of the asymmetric exponential Gabor theorem

## Correctness — PASS

The statement covers exactly \(a,b>0\), \(a\ne b\), and integer \(q\ge3\), with standard unnormalized frame coefficients. The proof first establishes the exact scalar Zak multiplier from root-of-unity orthogonality and two geometric tails. Its explicit polyphase numerator has nonnegative coefficients, making the frequency ordering strict. Positivity and strict convexity at frequency zero give the upper bound. At the opposite phase the derivative reduces to a quadratic with one positive root; equality of the two Zak boundary values forces that root strictly inside the period. Strict Cauchy–Schwarz gives a positive lower bound. Every step is analytical for all parameters. Separately implemented direct-Zak and exact-rational checks are supplied in `CHECK.py`; finite runs do not replace the proof.

## Originality — PASS relative to inspected work

The 2026 complete frame-set theorem establishes existence, not sharp constants. The 2013 Kloos–Stöckler paper treats Zak zeros and symmetric exponential estimates. The 2022 Faulhuber–Shafkulovska full text gives exact *symmetric* two-sided-exponential constants, a genuinely different parameter domain. The redundancy-two parameter domain is explicitly excluded from the novelty claim; the present claim is the complete higher-redundancy family. No inspected statement implies the all-\(q\ge3\) skew-dependent minimizer and sharp constants. Janssen's 1996 calculation paper is a material but not decisive residual priority risk because its full text could not be retrieved; no absence of overlap is asserted on the strength of its abstract alone.

## Value — PASS

Both exact extremal frame constants quantify stable reconstruction, not just qualitative spanning. The theorem solves the natural unsolved quantitative specialization of the recent total-positivity frame-set theorem for every integer oversampling level beyond the already covered first one. The non-even window has a nontrivially displaced minimum and a fully explicit condition number; the answer covers an infinite family, not an arbitrary single numerical case.

## Closest literature and limits

Kloos–Stöckler, arXiv:1311.7359; Faulhuber–Shafkulovska, arXiv:2204.02917; de Dios Pont et al., arXiv:2608.04992; Janssen (1996), DOI:10.1016/0019-3577(96)85088-9. The proof is confined to the specified integer lattice; noninteger density, noise stability, and lattice optimization remain open here. Historical related work at redundancy two is credited, not included in the novelty scope.

Self-review: passed. Independent audit: not yet performed.

