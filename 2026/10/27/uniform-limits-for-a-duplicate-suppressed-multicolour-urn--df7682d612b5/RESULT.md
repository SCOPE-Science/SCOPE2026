# Uniform limits for a duplicate-suppressed multicolour urn

## Finding

Fix an integer \(d\ge3\) and positive integer initial counts \(U_i(0)>0\) for every colour \(i\in\{1,\ldots,d\}\). At each step, draw two balls independently and uniformly with replacement. Add one ball of each distinct colour represented in the pair: one ball if both draws have the same colour, and one ball of each colour if they differ. Let \(U_i(n)\) be the count of colour \(i\), \(T_n=\sum_{i=1}^d U_i(n)\), and \(X_i(n)=U_i(n)/T_n\).

**Theorem.** For every initial composition satisfying these assumptions,
\[
X_i(n)\longrightarrow \frac1d\quad\text{almost surely for each }i=1,\ldots,d.
\]
The total increment is not constant: \(T_{n+1}-T_n\in\{1,2\}\). The theorem therefore gives an explicit non-balanced, non-affine multicolour example in which all initially present colours nevertheless converge to equal proportions.

## Assumptions and scope

Sampling is with replacement, the two draws are conditionally independent given the current composition, and the addition rule counts each distinct sampled colour once. No balls are removed. Every colour has a positive initial count. The result does not claim the same limit for sampling without replacement, for rules that add multiple copies of a sampled colour, or for other variable-total reinforcement schemes.

## Proof

Write \(\mathcal F_n\) for the history through step \(n\), \(x_i=X_i(n)\), \(Q=\sum_i x_i^2\), and let \(\Delta_i\) indicate that colour \(i\) appears at least once in the next pair. Then \(\Delta T=\sum_i\Delta_i\), with \(\Delta T\in\{1,2\}\), and
\[
\Pr(\Delta_i=1\mid\mathcal F_n)=2x_i-x_i^2,\qquad
\mathbb E[\Delta T\mid\mathcal F_n]=2-Q.
\]
Since \(U_i(n+1)=U_i(n)+\Delta_i\),
\[
X_i(n+1)-X_i(n)=\frac{\Delta_i-x_i\Delta T}{T_n+\Delta T}.
\]
The numerator is uniformly bounded. Expanding the denominator, with a uniform remainder of order \(T_n^{-2}\), gives
\[
\mathbb E[X_i(n+1)-X_i(n)\mid\mathcal F_n]
=\frac{x_i(Q-x_i)}{T_n}+O(T_n^{-2}).
\]
Here \(T_0+n\le T_n\le T_0+2n\).

Define \(V(x)=\sum_i x_i^2\) and \(G(x)=\sum_i x_i^3-(\sum_i x_i^2)^2\). The Cauchy–Schwarz inequality yields
\[
\left(\sum_i x_i^2\right)^2
=\left(\sum_i x_i^{3/2}x_i^{1/2}\right)^2
\le \left(\sum_i x_i^3\right)\left(\sum_i x_i\right)
=\sum_i x_i^3,
\]
so \(G(x)\ge0\). Equality holds exactly when all positive coordinates of \(x\) are equal. Using the preceding drift and the fact that \(\lVert X_{n+1}-X_n\rVert=O(T_n^{-1})\),
\[
\mathbb E[V(X_{n+1})\mid\mathcal F_n]
\le V(X_n)-\frac{2G(X_n)}{T_n}+\frac{C}{T_n^2}
\]
for a deterministic constant \(C\). The nonnegative almost-supermartingale convergence lemma, together with \(\sum_n T_n^{-2}<\infty\), implies that \(V(X_n)\) converges and \(\sum_n G(X_n)/T_n<\infty\) almost surely. The function \(G\) is Lipschitz on the simplex, while successive states move by \(O(T_n^{-1})\). Since \(\sum_n T_n^{-1}=\infty\), the finite weighted sum forces \(G(X_n)\to0\). Its zero set is the finite set of vectors that are uniform on a nonempty subset of colours. Because the increments tend to zero and the distance to this finite set tends to zero, \(X_n\) converges to one such vector.

It remains to exclude a proper subset. For each colour \(i\),
\[
\Pr(\Delta_i=1\mid\mathcal F_n)=2X_i(n)-X_i(n)^2
\ge X_i(n)\ge \frac{U_i(0)}{T_0+2n}.
\]
The conditional probabilities have a divergent sum, so the conditional Borel–Cantelli lemma gives infinitely many additions of every colour; hence \(U_i(n)\to\infty\) almost surely.

Set \(L_i(n)=\log X_i(n)\) and \(p_i=2X_i(n)-X_i(n)^2\). Taylor expansion of the logarithms, using \(\Delta T\le2\), gives
\[
\mathbb E[L_i(n+1)-L_i(n)\mid\mathcal F_n]
=\frac{Q-X_i(n)}{T_n}
+O\!\left(\frac{1}{U_i(n)T_n}+\frac{1}{T_n^2}\right).
\]
The conditional variance of the centered increment is at most \(C'/T_n\): indeed, its square is bounded in conditional expectation by \(2p_i/U_i(n)^2+8/T_n^2\le C'/T_n\). Since \(T_n\ge T_0+n\), the martingale strong law with normalization \(\log n\) implies that the sum of centered increments is \(o(\log n)\) almost surely.

If the limiting uniform vector omitted colour \(i\) and had \(s<d\) positive coordinates, then \(Q\to1/s\) and \(X_i(n)\to0\). The conditional drift of \(L_i\) would therefore sum to
\[
\left(\frac1s+o(1)\right)\sum_{k<n}\frac1{T_k},
\]
which grows at least as a positive constant times \(\log n\), because \(T_k\le T_0+2k\). The centered martingale sum is only \(o(\log n)\). Consequently \(L_i(n)\to+\infty\), contradicting \(L_i(n)=\log X_i(n)\le0\). No colour can be omitted from the limiting support. The only remaining equilibrium is the uniform vector on all \(d\) colours, proving the theorem.

## Verification

The one-step conditional probabilities and the normalized drift are exact consequences of the stated addition rule. The inequality \(G\ge0\) follows from Cauchy–Schwarz with \(\sum_i x_i=1\). The total-count bounds justify every summability and logarithmic normalization used in the proof. The boundary-exclusion argument is needed: the Lyapunov calculation alone permits uniform limits on proper subsets.

## Relationship to prior work

Lasmar, Mailler and Selmi study multiple-drawing multicolour urns by stochastic approximation. Their general multicolour limit theorem assumes a balanced urn, while their non-balanced theorem is one-dimensional; the paper explicitly identifies extension to non-balanced multicolour urns as an open question. The present result treats one specific \(d\)-colour rule, with \(d\ge3\), variable total addition and a nonlinear drift.

The affine multicolour urn paper develops asymptotic theory for a class that is both balanced and affine. Here the total added count depends on whether the pair repeats a colour, and the conditional expected increment \(2x_i-x_i^2\) is quadratic, so that class does not include this model. Dahiya and Sahasrabudhe study graph-coupled urns with two colours at each vertex, a different state space and interaction rule. These comparisons establish a specific gap, not a claim that general stochastic-approximation tools are new.

## Limitations

The result proves almost-sure convergence only; it gives no rate, central limit theorem, or description of the limiting fluctuations. It does not classify arbitrary non-balanced multicolour urns. A differently named prior model with exactly this distinct-colour update could still affect priority; targeted record and literature searches found no exact match, but search failure is not a uniqueness proof.

## References

1. N. Lasmar, C. Mailler and O. Selmi, “Multiple drawing multi-colour urns by stochastic approximation,” *Journal of Applied Probability* 55 (2018), 254–281. First public version: arXiv:1611.09090, 28 November 2016; DOI 10.1017/jpr.2018.16.
2. “On affine multi-color urns grown under multiple drawing,” first public version arXiv:2403.12423, 19 March 2024.
3. Y. Dahiya and N. Sahasrabudhe, “Urns with Multiple Drawings and Graph-Based Interaction,” first public version arXiv:2308.12528, 24 August 2023; DOI 10.1007/s10959-024-01365-x.
