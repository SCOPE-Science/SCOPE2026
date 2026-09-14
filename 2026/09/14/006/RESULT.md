# Certified type-(5,5) rational approximant to |x-1/2| on [-1,1] with uniform error below 0.01

## Context

Best uniform rational approximation of the absolute value is a classical benchmark stemming from Newman (1964) and Stahl's sharp asymptotics: type-(n,n) error for |x| on [-1,1] decays like exp(-pi sqrt(n)). Finite-n explicit certified bounds at small type for a shifted kink are nevertheless not recorded in tables: shifting the kink to x=1/2 makes the interval asymmetric in the natural coordinate t=x-1/2 in [-3/2,1/2], so symmetric-interval values do not transfer. The admitted target asks for a decision of E_{5,5}(f1) <= 0.01 for f1(x)=|x-1/2| on [-1,1], either by exhibiting an explicit pole-free real type-(5,5) rational with certified error at most 0.01 or by a rigorous alternation lower bound above 0.01.

## Definitions

Let f1(x)=|x-1/2| on [-1,1]. Let E_{5,5}(f1) be the infimum of max_{x in [-1,1]} |f1(x)-r(x)| over real rational functions r=p/q with deg p <= 5, deg q <= 5 and q nonzero on [-1,1]. Work in t=x-1/2 in [TL,TR]=[-3/2,1/2]. Define ascending-coefficient polynomials with exact rational coefficients P(t)=sum_{k=0}^5 p_k t^k and Q(t)=sum_{k=0}^5 q_k t^k by p = (5165/588261, -29350/900759, 5123448/301135, -3363915/284231, 116388085/763311, 4583207/428422) and q = (1, -980828/725017, 67281667/791723, -21172161/949118, 78611567/924091, 21943815/890896), and r(x)=P(x-1/2)/Q(x-1/2).

## Result

The function r is a real rational function of exact type (5,5), Q is bounded below by 0.94 (in fact 0.9401) on the whole interval, hence pole-free there, and max_{x in [-1,1]} |f1(x)-r(x)| <= 0.008785 < 0.01. Consequently E_{5,5}(f1) <= 0.01: the target inequality holds on the "prove" side.

## Proof / evidence

The certificate is computer-assisted but fully rigorous in exact rational arithmetic. Lemma A (denominator): exact evaluation of Q at 40001 uniform nodes gives minimum at least 0.9946; with the exact majorant |Q'| <= sum k|q_k|(3/2)^{k-1} approx 2178.78, the half-gap 1/40000 contributes under 0.0545, so min Q >= 0.9401 > 0. Lemma B (cell estimate): partition [TL,TR] into K=2000 uniform cells of half-width rho=1/2000; the kink t=0 is a cell boundary (index 1500), so the error E(t)=P(t)/Q(t)-|t| is C^infinity inside each cell with E''(t)=U(t)/Q(t)^4 for an exact degree-18 polynomial U=W'Q^2-2WQQ' with W=P'Q-PQ'. On each cell with midpoint c, exact Taylor shift of Q and U gives local bounds m_c=|Q(c)|-Q_{1,loc} rho > 0 and M_{2,c}=sum|u~_j|rho^j/m_c^4 >= sup|E''|, and standard Taylor remainder yields max_cell|E| <= max(|E(a)|,|E(b)|)+M_{2,c} rho^2/2 with endpoints evaluated as exact rationals. The computed max over nodes is 0.0087808627 at t=0.139 and the max correction is 4.09e-06, for a total 0.00878495 <= 0.008785 < 0.01. The archived verifier replays both lemmas end-to-end using only exact Fraction arithmetic and asserts the threshold. An independent audit recomputation reproduced minQ 0.994605, m 0.940136, the same maxend location and correction, and a dense floating-point scan agrees to 9 digits.

## Limitations

The certificate is a computer-assisted exact-arithmetic bound rather than a hand-checkable analytic estimate; the approximant was found numerically (variable projection with Lawson reweighting) and is near-optimal but not proved optimal; no lower bound on E_{5,5} beyond the exhibited upper bound is claimed.

## Reproducibility

Inputs output/artifacts/candidate_exact.json (exact P, Q fraction strings) and output/artifacts/verify_certificate.py (exact replay of Lemmas A and B, runtime about 1-2 min) suffice to reproduce the bound; record the printed TOTAL and the assertion TOTAL <= 0.01.

## References

D. J. Newman, Rational approximation to |x|, Michigan Math. J. 11 (1964). H. Stahl, Best uniform rational approximation of x^alpha on [0,1] (1993) and related asymptotics. R. S. Varga, A. Ruttan, A. Carpenter, best uniform rational approximation tables for |x|. Chebfun minimax/AAA examples for rational approximation of abs(x) (Filip-Nakatsukasa-Trefethen; Trefethen AbsoluteValue).
