# Scientific review: sharp binary Concrete log-concavity region

## Correctness: PASS

The definition gives an exactly normalized density, since \(f=F'\) for \(F(x)=x^\tau/(x^\tau+\alpha(1-x)^\tau)\). The complete logarithmic curvature identity (1) follows from explicit differentiation and is checked symbolically. The necessity of the displayed temperature bound follows at the support midpoint. The sufficiency argument compares all parameter shifts against two extremal hyperbolic functions, then proves a global minimum through an explicit derivative with a strict sign change at zero. The argument covers all real \(\tau,\alpha>0\), including the uniform boundary and the sharp parameter endpoints. The finite rational tests supplement but do not replace the analytic proof. The critical counterexample has exact curvature \(68808/10201\).

## Originality: PASS, with bibliographic risk

The 2016 binary Concrete formulation proves low-temperature log-convexity but not an if-and-only-if log-concavity region. The 2021 account makes a qualitatively stronger high-temperature claim without restricting asymmetric weights, and the exact counterexample disproves that unrestricted claim. The 2018 unit-logistic paper explicitly gives the equivalent two-parameter family, but its inspected shape and estimation sections do not state a sharp global log-concavity region. Full text of the 1982 original \(L_B\) account was not inspected, so the possibility of an earlier equivalent theorem remains; it has not been asserted away. Searches of mathematical result records and relevant public literature did not identify a covering statement. This is a self-review, not independent priority certification.

## Value: PASS

This is a sharp global, necessary-and-sufficient classification for a standard relaxed Bernoulli density, rather than a one-point counterexample. It quantitatively exposes why increasing temperature to just above one is insufficient to obtain log-concavity when class weights are unequal; the exact required threshold \(1/(2\sqrt{p(1-p)})\) diverges as the class probability becomes extreme. It clarifies the shape restriction used in density-based optimization and serves directly in the equivalent unit-logistic parameterization. The proof's hyperbolic extremal comparison is essential for sufficiency, beyond checking midpoint curvature.

## Closest literature and scientific limits

Relevant sources: Maddison–Mnih–Teh, arXiv:1611.00712, Appendix B; Beck–Bockelmann–Dekorsy, arXiv:2102.12756, Section II-B, Figure 1; Menezes–Mazucheli–Dey, DOI:10.1590/0101-7438.2018.038.03.0555. The original Tadikamalla–Johnson 1982 article is not fully inspected and remains a priority uncertainty. No multivariate Concrete analogue, numerical optimization speedup, or exhaustive bibliographic uniqueness is claimed.

Self-review: passed. Independent audit: not yet performed.
