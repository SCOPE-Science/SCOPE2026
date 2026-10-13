# The sharp zero-regression boundary for Chatterjee rank dependence

## Finding

Let \((U,V)\) have an arbitrary bivariate copula, so that both margins are uniform on \([0,1]\). Define the directional Chatterjee rank coefficient \(\xi=\xi(V\mid U)\) and the copula correlation ratio \(\eta=12\operatorname{Var}(\mathbb E[V\mid U])\). The following is a sharp boundary theorem:

\[
\boxed{\eta=0\quad\Longrightarrow\quad 0\le \xi\le\frac14.}
\]

The upper endpoint is attained exactly when, for almost every \(u\), the regular conditional distribution \(\mathcal L(V\mid U=u)\) has support containing at most two points. In particular, no absolutely continuous copula with \(\eta=0\) attains equality. Nevertheless, the sharp supremum over absolutely continuous copulas satisfying \(\eta=0\) is \(1/4\), and it is approached by explicit step-density copulas below.

The existence of a singular extremizer with \((\xi,\eta)=(1/4,0)\), and the attainability of the whole segment \(\{(\xi,0):0\le\xi\le1/4\}\), were already established in Example 2.8 and Proposition 2.10 of Ansari and Rockel [1]. The contribution here is **universal optimality**, the conditional-support equality characterization, and the explicit nonattainment-versus-sharp-supremum result for absolutely continuous copulas.

## Assumptions and scope

Work on any probability space supporting uniform \(U,V\) with an arbitrary copula, including singular laws. A regular conditional distribution of \(V\) given \(U\) exists because the variables are real-valued. Write \(V'\) for a conditionally independent copy of \(V\) given \(U\). With the continuous uniform response margin the population coefficient admits the equivalent representations

\[
\xi(V\mid U)=1-3\mathbb E|V-V'|=6\int_0^1 \operatorname{Var}\big(\Pr(V\le t\mid U)\big)\,dt,
\qquad
\eta(V\mid U)=12\operatorname{Var}(\mathbb E[V\mid U]).
\]

Both \(\xi\) and \(\eta\) refer to the **response** \(V\) and the **predictor** \(U\); no symmetry in their roles is asserted. The zero-ratio hypothesis is equivalent to \(\mathbb E[V\mid U]=1/2\) almost surely, i.e. mean independence of the uniform rank response, and is stronger than vanishing Spearman correlation.

## Proof

**A conditional absolute-difference lemma.** Let \(\nu\) be any probability law on \([0,1]\) with finite mean \(a\), and take independent \(Z,Z'\sim\nu\). Conditional Jensen gives

\[
\mathbb E|Z-Z'|\ge\mathbb E|Z-a|.
\]

Moreover, equality holds if and only if the topological support of \(\nu\) has at most two points. To see sufficiency, if \(\nu\) is concentrated on \(z_-\le z_+\), then for each possible \(Z\) the random difference \(Z-Z'\) has a constant sign, so Jensen is an equality. For necessity, if \(\nu\) charges three ordered disjoint intervals, the middle interval has positive mass of \(Z\), and conditional on any \(Z\) in a suitable middle subinterval, the difference \(Z-Z'\) takes strictly positive and strictly negative values, each with positive probability. The conditional Jensen inequality is then strict. Every support of cardinality at least three admits such intervals. The argument also covers one-point laws.

**Universal upper bound.** Since \(\eta=0\), the conditional mean \(\mathbb E[V'\mid U]=\mathbb E[V\mid U]=1/2\) almost surely. Conditional Jensen, now given \((U,V)\), yields

\[
\mathbb E(|V-V'|\mid U,V)\ge\left|V-\mathbb E[V'\mid U,V]\right|=|V-1/2|.
\]

The conditional independence in the definition of \(V'\) justifies the displayed conditional expectation. Integrating and using the uniform marginal gives

\[
\mathbb E|V-V'|\ge\mathbb E|V-1/2|=\int_0^1|v-1/2|\,dv=\frac14.
\]

Therefore \(\xi=1-3\mathbb E|V-V'|\le1/4\). The second representation of \(\xi\) in the preceding section proves \(\xi\ge0\). By the lemma, equality in the integrated Jensen inequality holds exactly when the conditional law of \(V\) has at most two support points for almost every \(u\). This is a full necessary-and-sufficient characterization, not merely an existence assertion.

**Sharpness for general copulas.** As explicitly calculated in [1, Example 2.8], let \(V\) be uniform and \(U=|2V-1|\). Given \(U=r\), the response takes the two values \((1-r)/2\) and \((1+r)/2\), equally likely. Hence its conditional mean is \(1/2\), and the equality criterion gives \(\xi=1/4\). This previously known example completes the optimality statement without being presented as a new construction.

**Absolutely continuous sharp-approach family.** For each integer \(m\ge1\), partition the predictor range into

\[
I_j=[j/m,(j+1)/m),\qquad j=0,\ldots,m-1,
\]

with the harmless endpoint convention at \(1\). Partition the response range into paired sets

\[
J_j=\left[j/(2m),(j+1)/(2m)\right)
\ \cup\
\left(1-(j+1)/(2m),1-j/(2m)\right],
\]

and define the step density

\[
c_m(u,v)=m\sum_{j=0}^{m-1}\mathbf{1}_{I_j}(u)\mathbf{1}_{J_j}(v).
\]

Each \(J_j\) has measure \(1/m\), the \(J_j\) are pairwise disjoint modulo null sets and cover \([0,1]\), and the \(I_j\) form an equal-measure partition. Direct integration therefore gives both uniform margins. Conditional on \(U\in I_j\), the law of \(V\) is uniform on \(J_j\), symmetric about \(1/2\), hence \(\mathbb E[V\mid U]=1/2\) and \(\eta(c_m)=0\).

To compute \(\xi\) exactly, set \(h=1/(2m)\). With probability \(1/2\), the conditionally independent responses lie in the same length-\(h\) interval, in which case the expected absolute difference is \(h/3\). Otherwise they are in opposite intervals, whose midpoints have distance \(1-(2j+1)/(2m)\). Thus for a predictor in \(I_j\),

\[
\mathbb E(|V-V'|\mid U\in I_j)
=\frac{1}{12m}+\frac12-\frac{2j+1}{4m}.
\]

Averaging over \(j=0,\ldots,m-1\) gives

\[
\mathbb E|V-V'|=\frac14+\frac{1}{12m},\qquad
\boxed{\xi(c_m)=\frac14-\frac{1}{4m},\quad\eta(c_m)=0.}
\]

Every \(c_m\) is absolutely continuous. For any absolutely continuous copula, the conditional response law is non-atomic for almost every predictor value, so it cannot satisfy the equality criterion. Consequently \(\xi<1/4\) for each such copula, while \(\xi(c_m)\uparrow1/4\). This proves the sharp unattained absolutely continuous supremum.

## Verification

The included standalone `checker.py` uses exact rational arithmetic to reconstruct the paired interval partitions, their uniform margins, their conditional mean, and all four within-pair contributions to \(\mathbb E|V-V'|\). It verifies the displayed closed formulas for each \(1\le m\le128\) and named boundary instances. Execute `python checker.py` with Python 3.9 or later. These finite checks corroborate the explicit witnesses; the unrestricted copula inequality and equality classification are established analytically above and do not depend on finite enumeration.

## Relationship to prior work

Ansari and Rockel [1] derive the conditional-i.i.d. expressions for \(\xi\) and \(\eta\) in their Equation (43), construct the point \((1/4,0)\) in Example 2.8, and in Proposition 2.10 establish a larger attainable inner region containing the entire segment \(\eta=0,\ 0\le\xi\le1/4\). They explicitly leave sharpness of the full region unresolved in Remark 2.11. Their Theorem 2.6 supplies outer bounds not sufficient to prohibit values \(\xi>1/4\) at \(\eta=0\). The new universal Jensen envelope closes precisely that unresolved zero-\(\eta\) boundary; it does not determine the rest of the region.

Ansari and Rockel [2] classify a different \(\xi\)–Spearman-\(\rho\) region. Spearman's rho equal to zero does not imply mean independence, so its zero-correlation slice cannot substitute for the zero-copula-correlation-ratio slice established here. The equality lemma is a self-contained elementary argument; no priority is claimed for conditional Jensen's inequality or for the singular sharpness example from [1].

## Limitations

This theorem assumes a continuous uniform response rank and \(\eta=0\) exactly. It does not determine sharp upper bounds when \(\eta>0\), provide finite-sample statistical inference, or characterize all absolutely continuous approximations beyond the displayed explicit family. The absolute continuity conclusion is strict nonattainment; no uniform positive deficit can hold across all absolutely continuous copulas, as the witnesses show. Priority over unindexed or inaccessible related work cannot be established by search alone. Independent scientific validation has not been performed.

## References

[1] Jonathan Ansari and Marcus Rockel, *The exact Spearman rho–footrule region via optimal transport with applications to finite rankings, mixability, and Chatterjee's rank correlation*, arXiv:2608.20176v1, first public 2026-08-20, especially Theorem 2.6, Example 2.8, Proposition 2.10, Remark 2.11, Equation (43). https://arxiv.org/abs/2608.20176

[2] Jonathan Ansari and Marcus Rockel, *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, arXiv:2506.15897, first public 2025-06-18. https://arxiv.org/abs/2506.15897
