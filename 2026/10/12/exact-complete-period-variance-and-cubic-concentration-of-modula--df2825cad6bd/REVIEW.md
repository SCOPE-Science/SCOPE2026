# Scientific review: complete-period modular-energy variance

## Correctness — PASS

The stated domain is all integers \(m\ge1\) and uniform complete periods. Conditional on the shared residue modulo the gcd, the quotient remainders are independent by the Chinese remainder theorem; their shared residue creates exactly the covariance \((\gcd(a,b)^2-1)/12\). Mean and Jordan-totient formulas follow by finite summation. The Möbius–Jordan summatory estimate, the layer expansion of the square of a floor, and absolutely convergent zeta series give the stated cubic coefficient with controlled \(O(m^2\log(2m))\) error. Chebyshev proves the probability bound. Rational-arithmetic checks independently reproduce all covariance pairs through moduli 20 and all full-period variance formulas through parameter 9. No finite check is treated as proof of the infinite estimates.

## Originality — PASS, subject to residual risks

The complete source article by En-naoui (arXiv:2509.10592v1) defines this energy and proves periodicity, but does not determine its covariance or complete-period variance; Section 10 explicitly calls for analysis of its statistical behavior. The comparison with Kaltenböck–Kiuchi–Saad Eddin–Ueda (DOI:10.1007/s00025-021-01357-x) distinguishes weighted gcd-sum averages from the second moment of aggregate remainders. Related indexed mathematical claims concerning gcd sums, residue distributions and exact variances do not imply this theorem. Classical Jordan and CRT formulas are known tools, not independent novelty. An equivalent calculation hidden in other literature remains possible.

## Value — PASS

The exact second moment and its positive, explicit asymptotic constant identify the \(m^{3/2}\) fluctuation scale and yield a quantitative complete-period concentration law. This directly addresses the motivating source's distributional program for a natural arithmetic sum without asserting a stronger limiting law.

## Closest literature and limitations

En-naoui, *The Modular Energy Function: Exact Identities and a Primality Equivalence* (arXiv:2509.10592v1); Kaltenböck et al., *Sums of Averages of GCD-Sum Functions II* (2021). Uniform full-period sampling, not shorter intervals, is established; equivalent unindexed work is a residual priority risk. The independent formal or external review has not taken place.

Self-review: passed. Independent audit: not yet performed.
