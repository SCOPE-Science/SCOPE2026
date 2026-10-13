# Scientific review: unseen–doubleton occupancy dependence

## Correctness (PASS)

The joint Dirichlet–multinomial mass function gives exact one- and two-category probabilities; aggregation over distinct category labels produces the covariance factorization. The ratio of consecutive factors has denominator-minus-numerator exactly \(a(a+2)>0\); the continuous extension is strictly decreasing by concavity of the digamma function and eventually falls below one by log-convexity of the gamma function. An endpoint-corrected Riemann-sum expansion yields the constant-order threshold shift and the finite critical-window covariance limit. Exact rational composition enumeration independently confirms 170 finite instances; 8,316 further exact-rational checks confirm the successive-ratio identity and its signs. Numerical experiments are not the infinite-parameter proof.

## Originality (PASS, qualified)

Keener–Wu (2006, DOI:10.1142/9789812772558_0008) already analyze this symmetric mixture and derive the leading occupancy-count covariance asymptotics. The generic law, exact probability formula, and leading covariance scale are prior art. Independent multinomial frequency-count covariance sign laws cover a distinct boundary model reached as \(a\to\infty\), not the finite-\(a\) model. The inspected full paper does not state the complete **finite-\(k\) one-crossing sign classification**, its **constant-order threshold shift**, or the associated **critical covariance profile**. Griffiths–Spanò (arXiv:1003.5131) investigate Dirichlet–multinomial canonical correlations; Bartroff–Goldstein–Işlak (arXiv:1402.6769) investigate size-biased concentration for occupancy counts. Those inspected results do not imply the specific sign classification as stated. Keener–Rothman–Starr (1987, DOI:10.1214/aos/1176350604) is particularly plausible older coverage of joint occupancy moments, but its full text was not obtained; this residual historical-priority risk remains. No assertion of independent historical certification is made.

## Value (PASS)

The count of unseen categories measures sample coverage, and the doubleton count is a standard frequency-of-frequencies input in species richness estimation. Positive covariance at small samples reflects concentration into pairs leaving categories unseen; negative covariance in denser samples reflects competing occupancy requirements. The exact global sign change, its non-Poisson shape dependence, and its sharp finite-size location are substantive structural facts. At the critical load, a leading-order covariance theorem gives zero and does not resolve sign; the explicit constant-order shift and limiting linear profile do.

## Limits

The theorem assumes an exchangeable, symmetric Dirichlet mixture of fixed positive shape and at least three categories. It does not extend to asymmetric concentrations or jointly varying shape without further work. Earlier random-partition treatments could conceal equivalent results; an independent literature and proof audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
