# Scientific review: conditional bridge occupation and return count

## Correctness — PASS

A walk conditioned to return to the origin after \(2n\) simple symmetric steps decomposes uniquely into signed primitive excursions. The exact generating function \(F(x,y,u)=[1-u(P(x)+P(y))]^{-1}\), with \(P(z)=(1-\sqrt{1-4z})/2\), records the positive and negative occupation half-durations and the total completed excursion count. The identity \(F(x,y,1)=\sum_{a,b\ge0}C_{a+b}x^ay^b\) reproduces the uniform Chung–Feller marginal, while \(\partial_uF|_{u=1}=F^2-F\) yields the stated conditional mean. Adjacent-level differences telescope to positive Catalan products; odd/even central modes and all endpoint exceptions follow exactly. Catalan coefficient asymptotics plus a uniform boundary tail bound give the square-root scaling function. Conditioning on unsigned excursion lengths and using independent excursion signs reduces the centered quadratic occupation to one-fourth of the sum of squared excursion half-lengths; exact marked generating functions yield the negative covariance for all \(n\ge2\).

The included `verify.py` passed 25,711 checks: exact enumeration of bridges of at most sixteen steps, independent excursion-count dynamic programming, identity tests, strictness/boundary checks, and asymptotic comparisons. Finite checks corroborate but do not prove the universal identities or asymptotic limits.

## Originality — PASS, subject to historical-priority uncertainty

Chung and Feller (1949, Theorem 2A) prove the uniform occupation law; Lachal (arXiv:1003.5009, 2010, Theorems 6.1–6.2) gives exact unmarked bridge sojourn generating functions. Banderier and Flajolet (2002) develop generic bridge and excursion machinery. Pitman (1999) treats Brownian-bridge local times, not the finite discrete occupation-conditioned return count. These results motivate and facilitate the derivation, but the inspected portions do not state the evaluated conditional excursion-count regression, strict center-peaked classification, or the exact negative quadratic covariance. In particular, a bivariate occupation generating function alone has no return-count marking, so it cannot supply the evaluated conditional regression without an additional differentiation and coefficient calculation. The original Chung–Feller PDF could not be fully rendered; its indexed Theorem 2A and the abstract-level account were assessed, and the remainder remains a priority risk.

Research-index checks returned related Brownian bridges, random-walk hitting problems, and Dyck excursion applications, but not a statement implying this conditional bridge dependence theorem. Earlier published generic generating functions could contain an implicit derivation; this is not proof of global uniqueness, and independent priority assessment is outstanding.

## Mathematical value — PASS

The number of returns to zero and the positive occupation time are standard dependent statistics of a random-walk bridge, pertinent to excursions, conditioned path sampling, and discrete local-time/occupation identities. Unconditional linear covariance vanishes identically, so it conceals the strict center-peaked conditional return profile. The exact strict classification for every sample size and the macroscopic square-root profile expose the hidden dependence; the negative centered quadratic covariance quantifies it as one natural additional identity. Neither uniform Chung–Feller occupation alone nor a generic Catalan convolution immediately gives the position-dependent direction and strength of the return-count regression. This is a complete, natural conditional dependence theorem, not an arbitrarily selected parameter slice or a numerical observation.

## Closest prior work and limitations

Principal references: Chung and Feller, *On fluctuations in coin-tossing* (PNAS 1949); Lachal, *Sojourn time in Z+ for Bernoulli random walk on Z* (arXiv:1003.5009; first posted 2010-03-25); Banderier and Flajolet (2002), *Basic analytic combinatorics of directed lattice paths*; Pitman (1999), *The distribution of local times of a Brownian bridge*. The theorem covers symmetric nearest-neighbor bridges with midpoint-positive occupation only. No global stochastic ordering of conditional return counts or nonbridge analogue is established. A stronger earlier joint-generating-function result could subsume the formulas, so historical novelty has residual risk.

Self-review: passed. Independent audit: not yet performed.
