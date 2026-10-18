# A sharp three-agent phase boundary and an all-transmissibility obstruction to variance submodularity in social cascades

## Finding

Let \(G=(V,E)\) be a finite connected simple undirected graph. Activate a seed set \(S\subseteq V\). Each active vertex has one independent chance, with common probability \(0<p<1\), to activate each as-yet-inactive neighbor. Activated vertices stay active. Let \(X_G(S)\) be the final number of active vertices and \(W_G(S)=\operatorname{Var}(X_G(S))\). Define the submodularity gap for distinct \(a,b\notin S\) by
\[
\Gamma_G(S;a,b)=W_G(S\cup\{a\})+W_G(S\cup\{b\})-W_G(S)-W_G(S\cup\{a,b\}).
\]

**Theorem.** Let \(p_*\in(0,1)\) denote the unique root of \(2p^3-5p+1=0\), numerically \(p_*=0.203364213796905\ldots\). For every connected graph on at most three vertices, \(W_G\) is submodular if and only if \(p\le p_*\), with the qualification that connected one- and two-vertex graphs are submodular for all \(p\). More precisely, on the three-vertex path the threshold is \(1/3\); on the triangle it is \(p_*\). Consequently, three is the minimum graph order exhibiting failure of variance submodularity.

**No universal small-transmission rescue.** For every \(0<p<1\), there is a finite star \(K_{1,m}\) on which \(W_G\) fails submodularity. In fact, for the submodularity inequality involving the final two previously unseeded leaves, its reversal occurs exactly when
\[
(1-p)^{m-2}<R(p):=\frac{5+4p}{14-4p-p^2}.
\]
The smallest integer \(m\ge2\) satisfying this explicit inequality is
\[
m_*(p)=3+\left\lfloor\frac{\log R(p)}{\log(1-p)}\right\rfloor,
\quad\text{and}\quad
\lim_{p\downarrow0}p\,m_*(p)=\log(14/5).
\]
The minimum \(m_*(p)\) is for **this specified two-leaf inequality**; it is not claimed to be the minimum star order for every possible inequality.

These statements concern the *variance* of random cascade size. The classical expected cascade size remains monotone and submodular.

## Assumptions and scope

The graph is finite, simple, connected, and undirected; every oriented attempted contact uses an independent success with probability \(p\), and there is no recovery before the final active set is determined. The selected initial seeds are active with certainty. Variance includes the randomness of all subsequent activation attempts but no randomization of the seed set or of \(p\). No normalization by network order is used. At \(p=0\) or \(p=1\) the variance is identically zero, so the strict statements intentionally concern \(0<p<1\).

The final active-set law coincides with the union of components meeting \(S\) in independent undirected bond percolation at retention \(p\). To see this, explore outward from the seed set, testing each edge at most once when its first endpoint enters the explored set; conditional on the exploration history, each newly tested edge succeeds independently with probability \(p\). This has exactly the same revealed-component law as pre-sampling all undirected edges as independent open or closed bonds. This is a statement of equality in distribution for each fixed \(S\), not an assertion that directed attempt outcomes are identical edge by edge to undirected bonds.

## Proof

**1. Exhaustive order-at-most-three calculation.** In a set function on three vertices, submodularity is equivalent to nonnegativity of \(\Gamma_G(S;a,b)\) for every pair \(a\ne b\) and every \(S\subseteq V\setminus\{a,b\}\). Up to isomorphism the only connected graphs on three vertices are the path \(P_3\) and the triangle \(K_3\). For two vertices there is a single edge and its only gap is \(2p(1-p)>0\); for one vertex there is no gap.

Label the path \(0-1-2\). The complete list of gap types under path reflection is
\[
\begin{aligned}
\Gamma_{P_3}(\varnothing;0,1)&=p(1-p)(p+1)(p+2),\\
\Gamma_{P_3}(\varnothing;0,2)&=p^2(1-p)(p+9),\\
\Gamma_{P_3}(\{1\};0,2)&=0,\\
\Gamma_{P_3}(\{2\};0,1)&=2p(1-p)(1-3p).
\end{aligned}
\]
All omitted gaps are reflections of these. Hence \(W_{P_3}\) is submodular exactly when \(p\le1/3\).

For the triangle, every pair is equivalent, and there are only two types:
\[
\begin{aligned}
\Gamma_{K_3}(\varnothing;0,1)&=p(1-p)^2(2+17p-8p^3),\\
\Gamma_{K_3}(\{2\};0,1)&=2p(1-p)^2(1-5p+2p^3).
\end{aligned}
\]
The first factor is strictly positive because \(2+17p-8p^3>2+9p\) for \(0<p<1\). Write \(h(p)=1-5p+2p^3\). On \((0,1/3]\), \(h'(p)=6p^2-5<0\), while \(h(0)=1\) and \(h(1/3)<0\), so it has exactly one root \(p_*\in(0,1/3)\). For \(p\ge1/3\), \(h(p)\le1-3p\le0\), strictly except possibly at an endpoint, because \(p^3<p\). Thus \(p_*\) is the only root in \((0,1)\) and the triangle is submodular exactly for \(p\le p_*\). Since \(p_*<1/3\), the three-vertex universal boundary is the triangle's.

Each displayed polynomial follows from enumerating the \(2^{|E|}\) bond configurations. For every \(S\) and each configuration, let \(z\) be the size of the union of components intersecting \(S\); summing \(z\) and \(z^2\) with weight \(p^j(1-p)^{|E|-j}\) gives \(W_G(S)=\mathbb E[z^2]-(\mathbb E[z])^2\). The full exhaustive identities are reproduced by the supplied verifier.

**2. A star obstruction at every \(p>0\).** Let the star have center \(c\) and \(m\ge2\) leaves, and seed precisely \(k\) of its leaves but not the center. Put \(q_k=1-(1-p)^k\). The center activates with probability \(q_k\); conditional on its activation, each of the remaining \(m-k\) leaves activates independently with probability \(p\). Consequently, if \(F_m(k)\) denotes the cascade-size variance for this seed set,
\[
F_m(k)=q_k(1-q_k)[1+(m-k)p]^2+q_k(m-k)p(1-p).
\]
For the two unseeded leaves when \(k=m-2\), the ordinary submodularity gap is \(2F_m(m-1)-F_m(m-2)-F_m(m)\). Put \(u=(1-p)^{m-2}\). Substitution and exact factorization yield
\[
F_m(m)-2F_m(m-1)+F_m(m-2)
=p^2u\bigl[(5+4p)-(14-4p-p^2)u\bigr].
\]
The coefficient \(14-4p-p^2\) is positive, and \(0<R(p)<1\) since its denominator exceeds its numerator by \((1-p)(9+p)>0\). Thus the submodularity gap is *negative* exactly when \(u<R(p)\). As \(m\to\infty\), \(u\downarrow0\), proving failure on a finite star for every fixed \(p\in(0,1)\).

Because \(0<1-p<1\), the least admissible integer \(m\) has \(m-2>\log R(p)/\log(1-p)\), giving the stated floor formula, including the case of exact integer equality. Finally, \(\log R(p)\to\log(5/14)\) and \(\log(1-p)/p\to-1\) as \(p\downarrow0\), so \(p\,m_*(p)\to\log(14/5)\).

## Verification

Run `python verify_influence_risk.py` with SymPy. The script independently enumerates every undirected bond state for both connected three-vertex topologies; checks all displayed curvature expressions; enumerates independent **directed** activation arcs on both three-vertex topologies and a five-vertex star at two rational transmission probabilities; and cross-checks the star moment formula through six leaves. It also checks the general algebraic factorization at several symbolic star sizes, identifies the unique cubic root numerically, and checks strictly positive obstructions for rational witnesses. The symbolic all-size star identity and the uniqueness of the cubic root are proved in the preceding paragraphs rather than inferred from finite tests. The script's successful execution was recorded before packaging.

## Relationship to prior work

Kempe, Kleinberg, and Tardos (2003) prove the **expectation** of terminal influence is submodular for independent cascades; this is a first-moment statement and does not constrain the variance's signs. Khanna and Lucier (2014) obtain stronger greedy approximation results for **expected** influence on undirected networks, likewise without determining second-moment seed-set curvature. Staib and Jegelka (2017), Appendix D, investigate variance under uncertainty in the **edge-probability parameters** of a continuous bipartite budget-allocation model and exhibit a different nonsubmodularity phenomenon for standard deviation, not the fixed-parameter propagation variance addressed here. Wilder (2018) studies risk-sensitive optimization via conditional value-at-risk; it neither implies nor contradicts the sharp polynomial and finite-star classifications here.

No direct covering result was identified in the consulted indexed research and inspected texts. This is evidence of a specific gap, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The theorem does not say variance-submodularity always fails on every graph, nor does it bound the quality of any particular risk-aware greedy algorithm. The star formula specifies a sufficient family and the **exact first star size for one chosen two-leaf certificate**, not the global minimum graph size for each \(p\). No conclusion is drawn for heterogeneous directed networks, dependence between attempted transmissions, or CVaR/other dispersion objectives. Related results may exist under stochastic coverage or reliability-polynomial terminology; independent bibliographic validation has not been performed.

## References

1. D. Kempe, J. Kleinberg, and É. Tardos, *Maximizing the spread of influence through a social network*, KDD 2003, pp. 137–146, DOI: 10.1145/956750.956769, published 2003-08-24. Full text: https://www.cs.cornell.edu/home/kleinber/kdd03-inf.pdf
2. S. Khanna and B. Lucier, *Influence maximization in undirected networks*, SODA 2014, DOI: 10.1137/1.9781611973402.109.
3. M. Staib and S. Jegelka, *Robust budget allocation via continuous submodular functions*, arXiv:1702.08791v2 (2017), Appendix D, https://arxiv.org/html/1702.08791v2
4. B. Wilder, *Risk-sensitive submodular optimization*, AAAI 2018, DOI: 10.1609/aaai.v32i1.12121, https://ojs.aaai.org/index.php/AAAI/article/view/12121/11980
