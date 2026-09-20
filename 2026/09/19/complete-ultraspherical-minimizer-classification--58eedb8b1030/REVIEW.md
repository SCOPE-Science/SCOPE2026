# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The conclusion follows by retaining equality cases in the proof of Castillo--Sadigova's lower-envelope theorem.

For cells \(k\ge3\), the only new ingredient is the strict form of their Corollary 3.2:
\[
W_N^{(c,\lambda)}(\cos\theta)<1
\quad
(0<\theta\le\min\{\pi/2,4\pi\lambda/c\},\ N\ge1).
\]
The source's positive-connection coefficient of the top degree is strictly positive. In the base \(\lambda=1/2\) rotation argument, the convex combination contains with positive weight the path whose first coordinate is
\(\sin\theta\cos(N\theta)<\sin\theta\); the other paths are at most \(\sin\theta\). In the energy regimes, the endpoint comparisons are strict because
\[
\left(\frac{s}{s+1}\right)^2<\frac{s}{s+2},
\qquad
\frac{2s+1}{(s+1)^2}>\frac2{s+2},
\]
and the source's refined and exceptional-degree estimates also have strict positive margins for \(x<1\). Hence the strict auxiliary bound is valid.

Substituting it into the exact representation
\[
U_m-U_k
=
a_k(W_{m-k}^{(k,\lambda)}-1)Q_k
-b_k(W_{m-k-1}^{(k+1,\lambda)}-1)Q_{k-1}
\]
gives strict positivity for every later degree in an open cell and for every degree \(m\ge k+2\) at \(x=\xi_k\). The contiguous identity gives strict ordering of all earlier degrees.

The first two cells were checked separately against the exact formulas and inequalities in Sections 5 and Appendix B of arXiv:2609.15473. For \(n\ge7\), the source's concavity argument has a positive margin throughout \(t_0\le t<1\), and its second-cell function \(G\) has a strictly positive endpoint lower bound, so no high-degree equality can occur. For \(n\le6\), the explicit factors show that the only non-adjacent equality is degree \(5\) at \(d=2,t=t_0=1/3\). In particular
\[
U_5(-t)+t=
\frac{t(d+5)(1-t^2)((d+7)t^2+d-3)}{d(d+2)}
\]
and at \(t=t_0\) the last factor is
\[
\frac{(d-2)(d-1)(d+2)}{(d+1)^2},
\]
so equality occurs exactly at \(d=2\). Endpoint parity gives the claims at \(\pm1\).

Stress checks included direct numerical evaluation over a broad range of \(\alpha\), breakpoints, and degrees; no additional equality was found. These numerical checks are supplementary only and are not used in the proof.

## Originality

**PASS, to the best of our knowledge.** The directly relevant paper is Castillo--Sadigova, arXiv:2609.15473v1, submitted 14 September 2026. Its full theorem, auxiliary-polynomial proof, low-degree appendices, and Section 6 on minimising indices were inspected. The paper proves the value of the lower envelope on each closed cell, notes the automatic adjacent endpoint ties, and explicitly says that additional minimising degrees can occur. Section 6 exhibits the Legendre equality
\[
P_1(-1/3)=P_2(-1/3)=P_5(-1/3)
\]
and uses it to answer de Oliveira Filho's Question 1 negatively, but it does not classify all equality cases or state that this is the unique non-adjacent tie.

De Oliveira Filho's 2009 thesis was inspected at Section 3.5d, p. 47. It poses Question 1 (monotonicity up to an arbitrary minimising degree) and Question 2 (the lower-envelope cell conjecture), and records only a special affirmative case at a Jacobi-extremum point. The new 2026 paper settles Question 2; the present theorem classifies the minimising indices and thereby identifies the exact obstruction to Question 1.

Targeted searches for normalized ultraspherical/Jacobi lower envelopes, minimising-index uniqueness, breakpoint ties, the specific Legendre equality at \(-1/3\), and equivalent formulations did not locate a prior complete classification. The current SCOPE archive was also checked by source identifier and synonymous terminology, with no overlapping result found.

A residual risk remains because arXiv:2609.15473 is very recent and a contemporaneous follow-up may not yet be indexed. Koornwinder's OP-SF NET 17 (2010), Topic #11, is cited by the source as restating de Oliveira Filho's question and a proposed interval condition; that short item was not independently inspected in full here. The 2026 source describes it as an open-problem discussion rather than a classification, so it is not concrete evidence of prior coverage. No other specifically identified inaccessible source appeared likely to contain the complete equality-case theorem.

## Value

**PASS.** The source paper determines the numerical lower envelope but leaves open the multiplicity structure of its minimizers beyond one counterexample. The present result turns that qualitative caveat into a complete theorem: open cells have unique minimizers; ordinary breakpoints have exactly the expected adjacent pair; and the sole non-adjacent tie is the Legendre \(1,2,5\) coincidence at \(-1/3\). This also upgrades the negative answer to de Oliveira Filho's Question 1 into a complete obstruction classification.

The result is useful whenever the minimizing degree itself matters, including the spherical-distance linear-programming applications motivating the lower envelope, and it clarifies that the surprising Legendre counterexample is isolated rather than representative.

## Limitations

The theorem is restricted to normalized ultraspherical polynomials \(R_n^{(\alpha,\alpha)}\) with \(\alpha\ge0\). It does not classify minimizers for general asymmetric Jacobi parameters and does not give a quantitative gap from the minimum to the second-smallest value inside a cell. Originality is assessed to the best of our knowledge. No independent validation, independent audit, or formal proof-assistant verification is asserted.
