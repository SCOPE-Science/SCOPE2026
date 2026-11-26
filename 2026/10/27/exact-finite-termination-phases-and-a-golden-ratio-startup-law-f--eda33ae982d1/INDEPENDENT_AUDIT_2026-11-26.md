# Independent mathematical audit

## correctness

PASS

The versioned primary PDF verifies the three branch tests and Eq. (36); Algorithm 1 is recovered by choosing Option II in both optional branches of Algorithm 2. On every nonterminal step the gradient displacement is c times the nonzero iterate displacement, so the short BB quotient is 1/c and x^(k+1)=(1-a_k)x^k. The first index with a_j=1 therefore gives K=j+1. Independently, an a>=2 resets to (1/sqrt(2),t) with 0<t<=1/(2sqrt(2)); the following first-branch steps have a'=sqrt(1+t)/sqrt(2)<1 and a''=sqrt(1+t)*sqrt(1+sqrt(1+t))/sqrt(2) strictly between 1 and 2, so the reset reaches zero after exactly five updates including the original oversized step. For informed a<=1/sqrt(2), a_1=1/sqrt(2) and a_2^2=(1+1/(sqrt(2)a))/2, giving the exact reset boundary a=1/(7sqrt(2)) (included), the equality a_2=1 at 1/sqrt(2), and K=4 in between. For 1/sqrt(2)<a<1 the first adaptive step repeats a and the next is sqrt(2)a in (1,2), so K=4. Starting at 1 gives K=1, at 1<a<2 gives K=2, and at a>=2 gives K=5. For arbitrary theta_0>=0, consecutive first branches have multipliers at least sqrt(2) from the second such branch onward; the first crossing of 1 must occur, and all crossing cases terminate. For theta_0=0 the crossing multipliers q_j are below phi<2, so a strict crossing cannot invoke the oversized branch. The product equals phi^j times a positive convergent factor because sqrt(1+t) contracts with derivative at most 1/2 on t>=0. This proves the exact equality-versus-overshoot index and O(1) startup error in exact arithmetic. Decimal support was inspected, not used at irrational boundaries. No floating-point or anisotropic claim is supported.

## originality

PASS

The normalization and the informed start are direct specializations of the primary algorithm, and the nested-radical growth mechanism is not independently credited as new. The supported distinct result is the first exact zero index for the original safeguarded iteration: its informed switching phases and its precise crossing-to-termination law without initialization information. Inspected lower-step bounds and other BB finite termination theorems do not give that classification.

## value

PASS

This is a natural one-spectrum benchmark where an unsafeguarded exact short BB step is already optimal. The informed start still has a sharp jump from four to seven steps from invoking the oversized safeguard, while the admissible zero-memory start can have unbounded logarithmic delay. The exact boundaries and index law distinguish safeguards and initialization even on the simplest nondegenerate quadratic, beyond a check that the BB quotient equals 1/c.

The dated certificate retains the supplied scientific assessment, sources and limitations.
