# Two-hole local domination profiles and sharp stochastic overlap order

## Finding

Let \(G\) be any connected finite simple graph on \(n\ge5\) vertices, and let \(v\) have degree \(n-3\). Write \(u,w\) for its two nonneighbors and \(R=N_G(v)\), with \(|R|=m=n-3\). Set
\[
 k=|N_G(u)\cap R|,\quad \ell=|N_G(w)\cap R|,\quad
 t=|N_G(u)\cap N_G(w)\cap R|,\quad
 e=\mathbf 1_{\{uw\in E(G)\}},
\]
\[
 a=k+e+1,\qquad b=\ell+e+1,\qquad c=2+k+\ell-t.
\]
Let \(D_v(G,z)=\sum_{S\ni v,\ S\text{ dominates }G}z^{|S|}\). Then the **entire conditional domination polynomial** is
\[
\boxed{D_v(G,z)=z\big[(1+z)^{n-1}-(1+z)^{n-1-a}-(1+z)^{n-1-b}+(1+z)^{n-1-c}\big].}
\]
In particular, the polynomial is independent of the edges internal to \(R\). Let \(X_t\) denote the size of a uniformly selected dominating set containing \(v\). For fixed \(n,k,\ell,e\), the feasible integer overlap values obey
\[
\max(0,k+\ell-m)\le t\le\min(k,\ell).
\]
All those profiles are realized by connected graphs whenever \(e=0\) and \(k,\ell\ge1\), or \(e=1\) and \(k+\ell\ge1\). If \(t_1<t_2\) are two feasible values for these fixed parameters, then
\[
\boxed{\Pr(X_{t_1}\ge q)\ge\Pr(X_{t_2}\ge q)\text{ for every integer }q,}
\]
with strict inequality for at least one \(q\). Thus decreasing the shared-neighbor overlap strictly increases the conditional size distribution in first-order stochastic order, not just its mean.

The **exact local average size** is
\[
\boxed{\mathbb E X_t=\frac{n+1}{2}+\frac{a2^{-a}+b2^{-b}-c2^{-c}}{2(1-2^{-a}-2^{-b}+2^{-c})}.}
\]
Consequently, the smallest conditional mean at fixed \(n,k,\ell,e\) occurs precisely at maximal feasible overlap \(t=\min(k,\ell)\), and the largest at minimal feasible overlap \(t=\max(0,k+\ell-m)\), with strict comparisons whenever distinct feasible values exist. A second, sharp bound is
\[
\boxed{\mathbb E X_t\le\frac{n+1}{2}+\frac{a}{2(2^a-1)}+\frac{b}{2(2^b-1)},}
\]
with **equality if and only if** \(e=t=0\), equivalently the two closed neighborhoods \(N_G[u]\) and \(N_G[w]\) are disjoint. The upper bound itself is a specialization of a more general published degree-sum bound; the equality classification in this two-hole family is part of the present result.

The least size of a dominating set that contains \(v\) is \(2\) if \(t+2e>0\), with exactly \(t+2e\) such sets; otherwise it is \(3\), with exactly \(ab\) such sets.

## Assumptions and scope

All graphs are finite, undirected, loopless, simple, connected and have \(n\ge5\). A dominating set \(S\) satisfies \(N_G[S]=V(G)\). The condition on \(v\) forces exactly two nonneighbors \(u,w\). No restrictions on edges within \(R=N_G(v)\) are imposed. Connectivity is equivalent to the stated conditions on \(e,k,\ell\); namely, either \(u,w\) are nonadjacent and both meet \(R\), or they are adjacent and at least one meets \(R\). The parameter \(t\) is an integer in the displayed interval. The stochastic-order statement compares separate graphs or vertex-rooted graphs having identical \(n,k,\ell,e\), but possibly different overlap \(t\) and different edges inside \(R\). It is not an order assertion for all dominating sets without conditioning on \(v\).

## Proof

**Exact polynomial.** Let \(U=V(G)\setminus\{v\}\), with \(|U|=n-1\), and let \(A=N_G[u]\), \(B=N_G[w]\). Both are subsets of \(U\), and direct counting gives \(|A|=a\), \(|B|=b\), \(|A\cup B|=c\), \(|A\cap B|=t+2e\). Any set containing \(v\) already dominates \(\{v\}\cup R\). Hence \(\{v\}\cup T\) dominates if and only if \(T\subseteq U\) meets each of \(A\) and \(B\). Inclusion-exclusion over subsets of \(U\) missing one or both sets gives the claimed polynomial. This also proves independence from the internal edges of \(R\) and the exact minimum-size/count assertions.

**Strict stochastic order.** Write \(T_0=n-1\), and let \(h_c(z)=D_v(G,z)/z\) for the parameter configuration with union size \(c\), holding \(a,b\) fixed. For consecutive possible values \(c\) and \(c+1\), the polynomial identity is
\[
 h_c(z)-h_{c+1}(z)=z(1+z)^{T_0-c-1}.
\]
Each coefficient on the right is nonnegative. Its normalized coefficient distribution is the law of \(1+Y\), where \(Y\sim\mathrm{Binomial}(T_0-c-1,1/2)\). To analyze \(h_{c+1}\), partition the \(T_0\) potential selected vertices into the \(c+1\)-element union \(A\cup B\) and its \(T_0-c-1\) outside vertices. Under uniform selection subject to meeting \(A\) and \(B\), choices outside the union are independent fair coin flips. Inside the union at least one vertex must be selected, and with positive probability at least two are selected. Therefore its selected-vertex count stochastically dominates \(1+Y\), and differs strictly. The normalized distribution of \(h_c\) is a proper convex mixture of the normalized \(h_{c+1}\) distribution and the normalized right-hand distribution; so the \(h_{c+1}\) size law strictly stochastically dominates the \(h_c\) law. Adding the always-selected \(v\) retains this order. A smaller overlap \(t\) means larger \(c\). Iteration proves the assertion for every pair of distinct feasible overlaps. The positive-probability strictness follows, for instance, by selecting at least two vertices of \(A\cup B\), which is possible since \(A\) and \(B\) are nonempty and \(|A\cup B|\ge2\).

**Mean and sharp bound.** Evaluate \(h_c(1)\) and its derivative, or condition independent fair subsets of \(U\) on meeting both \(A\) and \(B\). Writing \(P_c=1-2^{-a}-2^{-b}+2^{-c}>0\) gives
\[
\mathbb E X_t=1+\frac{T_0}{2}+\frac{a2^{-a}+b2^{-b}-c2^{-c}}{2P_c}.
\]
This is the mean formula. Because all feasible overlap values are realized, strict stochastic ordering proves the exact extremal-overlap assertions.

For the degree-sum inequality, extend the displayed rational expression algebraically to integer \(c\) between \(\max(a,b)\) and \(a+b\), even when its value no longer represents a realizable union. Both \(P_c>0\) and \(N_c=a2^{-a}+b2^{-b}-c2^{-c}>0\) in this range, since \(a,b\ge2\) and \(j2^{-j}\) decreases for integers \(j\ge2\). Moreover
\[
N_{c+1}-N_c=(c-1)2^{-(c+1)}>0,\qquad P_{c+1}-P_c=-2^{-(c+1)}<0.
\]
Thus \(N_c/(2P_c)\) is strictly increasing in \(c\). Since \(c\le a+b\), comparison with the endpoint \(c=a+b\) yields
\[
\frac{N_c}{2P_c}\le\frac{a}{2(2^a-1)}+\frac{b}{2(2^b-1)}.
\]
Equality holds exactly when \(c=a+b\), or \(A\cap B=\varnothing\), which is exactly \(t+2e=0\). Nonnegativity of \(t,e\) makes this equivalent to \(t=e=0\). Such graphs exist for every feasible pair of disjoint positive neighbor sets, so the bound is sharp in its stated equality regime.

**Realizability and the minimum count.** Choose subsets \(K,L\subseteq R\) of sizes \(k,\ell\) whose intersection has size \(t\); they exist exactly in the displayed integer range. Join \(u\) to \(K\), \(w\) to \(L\), join \(u,w\) precisely when \(e=1\), and join \(v\) to all of \(R\). Arbitrary edges within \(R\) do not alter the above. The graph is connected precisely in the cases stated. A set containing \(v\) with exactly one additional vertex dominates iff that vertex lies in \(A\cap B\), giving \(t+2e\) solutions. If the intersection is empty, choose one vertex from each disjoint nonempty set \(A\) and \(B\); there are \(ab\) distinct three-vertex solutions, and no smaller one.

## Verification

The standalone Python 3 program `verify.py` constructs every graph on \(4\le n\le7\) with one designated vertex of degree \(n-3\). It does **not** use the two-set characterization for its direct graph-level test: it independently checks domination against each vertex's closed-neighborhood bitmask for each candidate set containing the designated vertex, then compares the resulting size histogram with the formula. This covers 33,864 graphs and 2,131,008 such subsets, including all graph-edge patterns among the other vertices and some disconnected graphs beyond the theorem's domain.

An additional exact-rational calculation checks 360 connected parameter profiles up to \(n=9\), including all 140 consecutive feasible-overlap comparisons, stochastic tail inequalities, strict mean differences, the sharp degree-sum inequality, and its equality condition. Running `python3 verify.py` reproduces the stored `verification_output.txt`. Finite enumeration illustrates and stress-tests, but the preceding argument proves the theorem for all permitted integers.

## Relationship to prior work

The March 5, 2026 article of Chen and He [1], published online with DOI `10.12677/aam.2026.153090`, defines the same vertex-conditioned domination statistic and computes it when the designated vertex has degree \(n-2\). Its conclusion explicitly identifies degree \(n-3\), with two nonneighbors and their shared-neighborhood relations, as the next case to investigate. The theorem here resolves that specified two-hole regime, not just for the mean but for the entire generating polynomial, strict overlap stochastic order, sharp attainable overlap extrema, and equality in the degree-sum upper bound. The single-hole result from [1] is acknowledged as prior art, and its method of polynomial differentiation is not claimed as novel.

A subsequent October 8, 2026 preprint of Chen, He, Lai and Li [2] states a general upper bound and a degree-\(n-2\) formula; its inspected Sections 3–5 do not supply this two-hole polynomial or stochastic comparison. Its broader **inequality alone is not claimed new**. Farhan and collaborators' September 25, 2026 study [3] concerns vertices common to all globally minimum dominating sets, a different question from uniform cardinality distributions **conditional** on one vertex. Beaton and Brown [4] concern the unconditioned average over all dominating sets. No implication from those statements determines the present stochastic-order theorem.

Published research-record comparisons located formulas for ordinary or restrained domination polynomials of restricted graph classes (including chain graphs), but none of the named results states the present degree-defect-two root-conditioned law or its overlap ordering. Those comparisons and their limits are detailed in `AUDIT.json`.

## Limitations

The distribution is conditional on containing a specified vertex; it does not give the unrestricted domination polynomial, characterize vertices present in every globally minimum dominating set, or determine the entire graph from the polynomial. Different internal edge sets on \(R\) may have the same distribution. Strict stochastic comparison requires two distinct feasible overlap values; when the overlap range consists of one integer there is no nontrivial comparison. The sharp degree-sum inequality is established here with a new equality characterization in this family, not asserted to be a new general inequality. Unindexed equivalent formulations in the domination-polynomial literature remain an originality risk; no independent external audit has been performed.

## References

1. T. Chen and W. He, *The Local Average Order of Dominating Sets Containing a Fixed Vertex*, Advances in Applied Mathematics (Yingyong Shuxue Jinzhan), 15(3), 87–94 (published online March 5, 2026), DOI: `10.12677/aam.2026.153090`; freely accessible PDF: https://pdf.hanspub.org/aam_2624940.pdf. In particular see the theorem and proof for degree \(n-2\) and the final paragraph of Section 4, which proposes degree \(n-3\).
2. T. Chen, W. He, H.-J. Lai and J. Li, *On the local average order of dominating sets*, arXiv:2610.11446v1 (first public October 8, 2026; later comparative source), https://arxiv.org/html/2610.11446v1, Theorems 3.8 and 4.1.
3. M. Farhan, D. Kuziak, I. Peterin and I. G. Yero, *Vertices that belong to every minimum dominating set of a graph and their connection with transportation sharing systems*, arXiv:2609.31818v1 (September 25, 2026), https://arxiv.org/html/2609.31818v1.
4. I. Beaton and J. I. Brown, *The average order of dominating sets of a graph*, Discrete Mathematics 344 (2021), 112595, DOI: `10.1016/j.disc.2021.112595`.
