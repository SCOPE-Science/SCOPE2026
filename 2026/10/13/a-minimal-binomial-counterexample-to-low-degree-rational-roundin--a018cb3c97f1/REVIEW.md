# Review

## Correctness

PASS. For \(X\sim\operatorname{Bin}(3,p)\), direct pushforward under \(x\mapsto\lfloor3x/2\rfloor\) gives positive masses at \(0,1,3,4\) and zero mass at \(2\). If its PGF factored into degree-at-most-three nonnegative-coefficient PGFs, positivity of the constant term and vanishing of the quadratic coefficient force the only nonconstant support pattern to be \({0,1}+{0,3}\). Such a product satisfies \(a_0a_4=a_1a_3\), while the exact binomial coefficients satisfy \(a_1a_3=9a_0a_4\). The contradiction is uniform for every \(0<p<1\). The \(n\le2\) minimality statement follows because the rounded variable then has maximum at most \(3\) and can itself serve as the single summand.

## Originality

PASS, with an explicit unpublished-source risk. The public Tang--Tang preprint was inspected at Corollary 4.2, Theorem 4.7, Conjecture 4.8, and the immediately following comparison of the polynomial classes \(P_3\) and \(Q_3\). It formulates the universal factorization claim after noting that the ambient classes are incomparable, but does not state the special rounded-binomial counterexample above. Candidate-specific published-finding corpus and web searches for Conjecture 4.8, \(\lfloor3X/2\rfloor\), \(\operatorname{Bin}(3,p)\), and the coefficient pattern returned no covering statement. The unpublished Liggett manuscript cited by the source could not be inspected directly and is retained as residual risk.

## Value

PASS. The source presents \(j=1\) and \(j=2\) as the positive low-degree cases and explicitly conjectures the extension to all \(j\). The counterexample occurs at the first new numerator \(j=3\), uses the canonical binomial subfamily of strongly Rayleigh laws, is minimal in the binomial trial count for \((j,k)=(3,2)\), and works for every nondegenerate success probability. It therefore gives a substantive boundary for the rational-rounding program rather than an arbitrary isolated computation.

Self-review: passed. Independent audit: not yet performed.
