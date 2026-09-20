# Review: exact fifth-power reciprocal Fibonacci floor formula

## Correctness

**PASS.** The proof separates into four independently checkable components.

1. Binet expansion gives an exact analytic series \(S_n=C\alpha^{-5n}H(z_n)\), and inversion through quadratic order produces the displayed three-term algebraic approximant.
2. Taking the quadratic-field trace yields the stated Fibonacci--Lucas rational quantity \(G_n=A_n/31958\).
3. Reduction modulo \(19\) shows \(A_n\not\equiv0\pmod{19}\) for every \(n\), so \(G_n\) is uniformly separated from the integers by at least \(1/31958\).
4. The analytic remainder is bounded by \(10\alpha^{-n}\), which is below that separation for \(n\ge27\). The finitely many cases \(4\le n\le26\) are enclosed by exact rational tail bounds in the standalone verifier.

Adversarial checks focused on denominator cancellation, the sign coming from \(\beta=-\alpha^{-1}\), whether the trace correction itself could cross an integer, and whether a numerical truncation was being mistaken for a proof. The mod-19 argument rules out cancellation globally; the finite cases use rational interval enclosures with a proved geometric tail majorant rather than floating-point approximations.

## Originality

**PASS, to the best of our knowledge.** The closest literature found was inspected in the following directions:

- Hwang--Park--Song (arXiv:2609.18179, submitted 16 September 2026) determine the cubic exact floor and explicitly state in their concluding remarks that constructing explicit formulas for higher powers \(s\ge5\) is substantially more challenging.
- Wan--Liang--Liao (arXiv:2510.13472; Mathematica Bohemica, online 10 April 2026) prove asymptotic estimates for arbitrary positive exponent \(d\) and generalized Fibonacci subsequences. Their general theorem covers the asymptotic setting of \(d=5\), so no novelty is claimed for the existence of an asymptotic expansion. Their explicit corollaries are developed for \(d=1,2,3,4\), and no exact floor determination was found there.
- Hwang--Park--Song (2022) give the exact fourth-power formula, while Li--Yang--Yuan (2025) develop generalized asymptotic formulas for powers \(1\) through \(4\).
- Searches for the fifth-power reciprocal tail, equivalent integer-part/floor wording, the denominator \(31958\), and the displayed Fibonacci--Lucas correction found no prior matching formula. The current SCOPE archive was also checked for the object and synonymous claim families, with no overlap found.

No inaccessible paper was identified that was specifically close enough to be singled out as likely to contain this exact theorem. Residual risk remains from very recent or incompletely indexed work, particularly because the cubic paper was posted only recently, and from older literature not surfaced by the searches.

## Value

**PASS.** The result advances the exact-floor sequence from the previously treated low powers to the first untreated higher power identified by the newest cubic paper. It is not merely a finite computation: the theorem holds for all \(n\ge4\), with an explicit closed Fibonacci--Lucas expression, a global modular obstruction, and a certified finite completion.

## Review status

Same-model review: passed. Independent audit: not yet performed.
