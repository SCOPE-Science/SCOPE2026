# Finite first-return moments for the one-dimensional Friedman-urn walk

## Finding

For the Friedman urn begun with one white ball and zero blue balls, every draw is returned and accompanied by one ball of the **opposite** color. Let \(X_0=0\), and increment \(X_n\) by \(+1\) on a white draw and \(-1\) on a blue draw. The first draw is necessarily white, so \(X_1=1\). Define the first-return time
\[
T=\inf\{n\ge2:X_n=0\}.
\]

**Theorem.** There exists a finite numerical constant \(C\) such that, for every integer \(n\ge1\),
\[
\mathbb P(T>n)\le C n^{-3/2}.
\]
In particular \(T\) is almost surely finite, \(\mathbb E[T]<\infty\), and \(\mathbb E[T^{\theta}]<\infty\) for every real \(0<\theta<3/2\). The finite-mean assertion answers the explicit first-return conjecture of Balaji and Mahmoud [1, Section 5] for exactly their initial urn and one-dimensional process.

## Assumptions and scope

Time is the number of **draws**. At time \(n\), the two draw counts are \(W_n\) and \(B_n\), and \(X_n=W_n-B_n\). The urn contains \(B_n+1\) white balls and \(W_n\) blue balls, a total of \(n+1\). Therefore for any possible positive state \(x\) at time \(n\ge1\),
\[
\begin{aligned}
\mathbb P(X_{n+1}=x+1\mid X_n=x)&=\frac{n+2-x}{2(n+1)}\le\frac12,\\
\mathbb P(X_{n+1}=x-1\mid X_n=x)&=\frac{n+x}{2(n+1)},\\
\mathbb E[X_{n+1}\mid X_n=x]&=\frac{nx+1}{n+1}.
\end{aligned}
\]
The theorem concerns the first return after the deterministic first step. It does not use the stationary-state definition of positive recurrence, which need not apply to a time-inhomogeneous position chain.

## Proof

**1. A killed first-moment identity.** Write \(s_n=\mathbb P(T>n)\) and \(a_n=\mathbb E[X_n\mathbf1_{\{T>n\}}]\) for \(n\ge1\). Both equal one at \(n=1\). Up to its first return, the walk is strictly positive, and an endpoint at the first return contributes zero to its first moment. Thus conditioning on time \(n\) and using the displayed conditional expectation gives
\[
(n+1)a_{n+1}=na_n+s_n,
\qquad
na_n=1+\sum_{k=1}^{n-1}s_k.\tag{1}
\]
The second equality follows by telescoping, with no asymptotics or stopping-limit exchange.

**2. Comparison with an absorbed simple walk.** Let \(S_m\) be a simple symmetric nearest-neighbor random walk starting at zero and let \(Q_m(x)\) be the probability that one started at an integer \(x\ge1\) remains strictly positive over the next \(m\) moves. The reflection principle gives
\[
Q_m(x)=\mathbb P(-x<S_m\le x),\qquad m\ge0.
\]
For \(m\ge1\), the interval \((-x,x]\) contains exactly \(x\) possible sites of the parity of \(S_m\). The central-binomial bound therefore gives
\[
Q_m(x)\le\min\{1,2x/\sqrt m\}.\tag{2}
\]
At every strictly positive state, the Friedman walk's probability of a right step is at most \(1/2\). Use common independent uniforms to drive its steps and those of the symmetric walk, with a right step chosen below the respective thresholds. As long as the Friedman path is positive, the symmetric path started at the same site stays greater than or equal to it. Indeed, their separation is even; when it is zero the symmetric walker never steps below the Friedman walker, and when it is at least two one-step updates cannot reverse their order. Hence, conditioned on any surviving state \(X_n=x\), the probability of another \(m\) surviving steps is at most \(Q_m(x)\).

For \(n\ge1\), conditional comparison at time \(n\) and (1)–(2) yield the main bootstrap inequality
\[
s_{2n}\le\mathbb E[\mathbf1_{\{T>n\}}Q_n(X_n)]
\le\frac{2a_n}{\sqrt n}
=\frac{2}{n^{3/2}}\left(1+\sum_{k=1}^{n-1}s_k\right).\tag{3}
\]

**3. Three successive bounds.** Comparison directly from \(X_1=1\) gives \(s_n\le Q_{n-1}(1)\le2/\sqrt{n-1}\) for \(n\ge2\). Accordingly \(\sum_{k<n}s_k=O(\sqrt n)\). Inequality (3) now implies \(s_{2n}=O(n^{-1})\). The survival sequence is nonincreasing, so this also implies \(s_m=O(m^{-1})\) for all integers \(m\).

The improved estimate yields \(\sum_{k<n}s_k=O(\log n)\). A second use of (3) gives \(s_{2n}=O((\log n)n^{-3/2})\), hence the same order for all \(m\) by monotonicity. Since \(\sum_{m\ge2}(\log m)m^{-3/2}<\infty\),
\[
\mathbb E[T]=\sum_{m=0}^{\infty}\mathbb P(T>m)<\infty.
\]
In particular \(K=1+\sum_{k=1}^{\infty}s_k=\mathbb E[T]-1<\infty\). Finally (3) yields \(s_{2n}\le2K n^{-3/2}\). For \(m\ge2\), setting \(n=\lfloor m/2\rfloor\ge m/3\) and using monotonicity gives
\[
s_m\le2K(3/m)^{3/2}.
\]
Increasing the constant to cover \(m=1\) proves the theorem. For \(0<\theta<3/2\), the discrete tail-sum identity
\[
\mathbb E[T^{\theta}]=\sum_{m=0}^{\infty}
((m+1)^{\theta}-m^{\theta})s_m
\]
converges because its summands are \(O(m^{\theta-5/2})\) for large \(m\). This proves the stated moment range.

## Verification

The accompanying standalone `check_friedman.py` uses only Python's standard library. Run `python check_friedman.py`. Its exact-fraction survivor recursion is checked independently against an enumeration by urn draw counts, the killed first-moment identity is checked at twenty successive times, and the reflection comparison is checked for finite horizons. The checker passes 889 finite assertions, using exact fractions for the model identities and a numerical check only for elementary square-root bounds. This is corroboration of the algebra and initial conditions; the infinite tail estimate follows from the three-step analytic bootstrap above, not from finite testing.

## Relationship to prior work

Balaji and Mahmoud [1], Sections 4–5, prove recurrence from Eulerian marginals but explicitly leave the finiteness of the *first-return expectation* as a conjecture supported by simulation. This proof supplies that missing expectation result and a polynomial survival upper bound. Menshikov and Volkov [2] analyze drift-dependent recurrence/transience and Friedman-type urns, particularly an **outward-drift** regime; their displayed theorems do not give first-return moments for the present opposite-reinforcement inward-drift model. Bercu, Bonnefont and Richou [3] analyze marginal deviations and concentration of Eulerian descents (including a Friedman-urn representation), not its time-dependent first-passage law. Standard symmetric-walk reflection bounds themselves are classical and are not claimed as new.

## Limitations

The exponent \(3/2\) is established only as a survival **upper-bound exponent**; neither a matching lower bound nor a leading asymptotic constant is proved. The endpoint moment \(\mathbb E[T^{3/2}]\), behavior after successive returns, other initial compositions, and two-dimensional first return remain undecided by this theorem. The finite-return result is about a time-inhomogeneous process, not an assertion of a stationary invariant probability measure.

## References

[1] S. Balaji and H. Mahmoud, *Urn-driven random walks*, arXiv:2504.14813v1 (first publicly posted April 21, 2025), Sections 4–5. https://arxiv.org/abs/2504.14813

[2] M. Menshikov and S. Volkov, *Urn-related random walk with drift*, arXiv:0711.2373v1 (2007), especially Sections 5–6. https://arxiv.org/abs/0711.2373

[3] B. Bercu, B. Bonnefont and A. Richou, *Sharp large deviations and concentration inequalities for the number of descents in a random permutation*, Journal of Applied Probability, including its Friedman-urn discussion. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/sharp-large-deviations-and-concentration-inequalities-for-the-number-of-descents-in-a-random-permutation/A2AE11B0B9D1BAD3285F3CC212F37D3F
