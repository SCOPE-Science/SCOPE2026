# Outer-independent double Roman weight enumerators of heterogeneous clique bouquets

## Finding

Let \(t\ge 2\) and let \(m_1,\ldots,m_t\ge 2\) be arbitrary integers. Form the *clique bouquet*
\[
B(m_1,\ldots,m_t)=K_1\vee\bigl(K_{m_1}\sqcup\cdots\sqcup K_{m_t}\bigr).
\]
Thus a hub \(v\) is joined to every vertex of \(t\) pairwise disjoint clique blades of sizes \(m_i\), and there are no edges between distinct blades. The cliques need not have equal sizes. Equal blade sizes recover generalized windmill graphs, and \(m_i=2\) for all \(i\) gives friendship graphs.

An *outer-independent double Roman dominating function* (OIDRDF) is a labeling \(f:V(B)\to\{0,1,2,3\}\) satisfying all three conditions: (a) the vertices labeled \(0\) form an independent set; (b) each \(0\)-vertex has either a neighbor labeled \(3\) or at least two distinct neighbors labeled \(2\); (c) each \(1\)-vertex has a neighbor labeled \(2\) or \(3\). Its weight is \(\omega(f)=\sum_{u\in V(B)}f(u)\).

Define its weight enumerator
\[
\mathcal D_B(z)=\sum_{f\text{ OIDRDF on }B}z^{\omega(f)}.
\]
Put \(T=z+z^2+z^3\), and for each blade size \(m\ge 2\) define
\[
\begin{aligned}
A_{0,m}&=T^m-z^m,\\
A_{1,m}&=T^m-z^m+m\bigl(T^{m-1}-z^{m-1}-(m-1)z^m\bigr),\\
A_{2,m}&=T^m+m\bigl(T^{m-1}-z^{m-1}\bigr),\\
A_{3,m}&=T^m+mT^{m-1}.
\end{aligned}
\]
**Theorem.** For all the stated integers, the complete labeled-vertex weight enumerator is
\[
\boxed{\mathcal D_{B(m_1,\ldots,m_t)}(z)
=\prod_{i=1}^t A_{0,m_i}(z)
+z\prod_{i=1}^t A_{1,m_i}(z)
+z^2\prod_{i=1}^t A_{2,m_i}(z)
+z^3\prod_{i=1}^t A_{3,m_i}(z).}
\]
Every coefficient counts all feasible labelings of that exact total weight, including labels \(1\) (which must not be silently removed). In particular,
\[
\boxed{\gamma_{oidR}(B)=3+\sum_{i=1}^t(m_i-1),\qquad
[z^{\gamma_{oidR}(B)}]\mathcal D_B(z)=\prod_{i=1}^t m_i.}
\]
Every minimum labeling puts \(3\) on the hub, chooses exactly one \(0\) in each blade, and puts \(1\) on every other vertex. No other minimum labeling exists.

There is also a distinct second-weight census. Write \(r_i=1+m_i(m_i-1)\), \(M=\prod_i m_i\), and \(w_0=3+\sum_i(m_i-1)\). Then
\[
\boxed{[z^{w_0+1}]\mathcal D_B(z)=
\sum_{i=1}^t r_i\prod_{j\ne i}m_j
+\mathbf 1_{\{t=2\}}\left(\prod_{i=1}^2r_i+M\right).}
\]
The extra two terms for precisely two blades arise from configurations with hub labels \(2\) and \(0\); for three or more blades, every next-to-minimum labeling has hub label \(3\).

## Assumptions and scope

All graphs are finite, simple, undirected, with labeled individual vertices. The bouquet contains exactly \(t\ge2\) blades, and every blade has at least two vertices. The join symbol means the hub is universal; non-hub vertices in different blades are not adjacent. The polynomial is ordinary in the weight variable, not a polynomial in a number of colors. Its degree is at most \(3(1+\sum_i m_i)\). Neither single-blade bouquets nor size-one blades are included; their boundary behavior is not asserted.

## Proof

**Local reduction.** Fix the hub label \(h=f(v)\). Since each blade is complete, the independence condition permits at most one \(0\) in each blade whenever \(h\ne0\). If \(h=0\), all blade vertices must be positive. Conversely, because distinct blades have no edges, these constraints are sufficient for the independence of the \(0\)-set. We examine all four possible hub labels, retaining the local defense requirements.

**Case \(h=3\).** Every \(0\)-vertex and every \(1\)-vertex is defended by the hub. Each blade independently has either no \(0\), with all \(m\) labels in \(\{1,2,3\}\), counted by \(T^m\), or exactly one \(0\), counted by \(mT^{m-1}\). Thus the blade factor is \(A_{3,m}\) and the hub contributes \(z^3\).

**Case \(h=2\).** All \(1\)-vertices are defended by the hub. If a blade contains no \(0\), its factor is \(T^m\). With one \(0\), that vertex sees one \(2\) at the hub; it needs a further \(2\) or a \(3\) among its \(m-1\) positive blade-neighbors. The permitted choices number \(m(T^{m-1}-z^{m-1})\), with the exponent recording weight. Consequently the factor is \(A_{2,m}\), and the hub supplies \(z^2\).

**Case \(h=1\).** A \(1\)-vertex in a blade cannot rely on the hub; that blade must contain a \(2\) or \(3\). With no \(0\) this yields \(T^m-z^m\). If there is exactly one \(0\), its neighbors inside the blade must contain either a \(3\) or at least two distinct \(2\)'s, because the hub is only \(1\). Among the \(m-1\) positive labels, precisely the all-\(1\) arrangement (weight \(m-1\)) and the \(m-1\) arrangements having exactly one \(2\) and otherwise only \(1\)'s (weight \(m\)) are forbidden. Every permitted arrangement also defends the blade's \(1\)-vertices. This produces the term \(m(T^{m-1}-z^{m-1}-(m-1)z^m)\). Since every blade has at least one \(2\) or \(3\), the hub itself is defended. The factor is \(A_{1,m}\) and hub weight \(z\).

**Case \(h=0\).** No blade vertex may be labeled \(0\). If an entire blade carried only \(1\)'s, none of those vertices could be defended, so the allowed local factor is \(T^m-z^m=A_{0,m}\). Conversely, every blade containing at least one \(2\) or \(3\) defends all its \(1\)-vertices. There are at least two blades: if any such non-\(1\) defender is a \(3\), the hub is defended by that neighbor; otherwise every blade has a \(2\), giving at least two distinct \(2\)-neighbors of the hub. Thus the hub is also defended, without any global correction term. These are precisely the allowed labelings with hub \(0\).

The cases are disjoint and exhaustive, and the independent blade contributions multiply within each case. Summing the four hub cases proves the displayed weight polynomial.

**Minimum and unique shape.** In the \(h=3\) case, each blade contributes at least \(m_i-1\) to the weight. Equality holds precisely when it has exactly one \(0\) and all remaining labels are \(1\). The resulting weight is \(w_0=3+\sum_i(m_i-1)\), with \(\prod_i m_i\) independent choices. For \(h=2\), each blade contributes at least \(m_i\): without \(0\), there are \(m_i\) positive labels, while with one \(0\), at least one of the \(m_i-1\) positive labels must be at least \(2\). Hence that hub case has weight at least \(2+\sum_i m_i=w_0+t-1>w_0\). For \(h=1\), the preceding local classification gives blade weight at least \(m_i+1\), so weight at least \(1+\sum_i(m_i+1)=w_0+2t-2>w_0\). For \(h=0\), every blade has at least one label \(2\) or \(3\), and its weight is at least \(m_i+1\), giving total at least \(\sum_i(m_i+1)=w_0+2t-3>w_0\). The strict comparisons use exactly \(t\ge2\). Thus all minimum functions were classified.

**One unit above minimum.** In \(A_{3,m}\), the coefficient of \(z^{m-1}\) is \(m\), and that of \(z^m\) is \(1+m(m-1)=r\): the latter arises either from the no-\(0\) all-\(1\) assignment or from choosing the \(0\) and then one additional \(2\). Thus the \(h=3\) contribution one unit above \(w_0\) is \(\sum_i r_i\prod_{j\ne i}m_j\). The other three hub cases begin at increments \(t-1\), \(2t-2\), and \(2t-3\) above \(w_0\), respectively. For \(t\ge3\) none reaches the next weight. For \(t=2\), the \(h=2\) case contributes \(\prod_{i=1}^2r_i\), and the \(h=0\) case contributes \(\prod_{i=1}^2m_i\), since the lowest term in \(A_{0,m}\) is \(mz^{m+1}\). This completes the second-coefficient identity.

## Verification

The standalone file `verify_oidr.py` constructs the graph from the given blade sizes, enumerates every labeling in \(\{0,1,2,3\}^{V(B)}\), tests independence and both defense conditions directly, and compares its weight histogram with the four-factor polynomial computed using integer coefficient convolution. It also checks the minimum and second-minimum coefficient formulas. It tests 10 graph-size vectors, including heterogeneous cases, with vertex counts from 5 through 9. Additional independently invoked cases included \((2,5)\), \((4,3)\), \((3,4)\), \((2,2,4)\), \((2,3,3)\), and \((2,2,2,3)\), the latter having 10 vertices. Every comparison passed. The code is a finite corroboration, not a proof of all parameter values; the four-case argument above supplies the uniform proof.

For example, \(B(2,2)\) admits 558 valid labelings in all, with exactly four of minimum weight 5 and 25 of weight 6. For \(B(2,2,2)\), the corresponding values are 7,084 in total, eight of minimum weight 6, and 36 of weight 7.

## Relationship to prior work

Outer-independent double Roman domination was introduced by Abdollahzadeh Ahangar, Chellali, and Sheikholeslami (2019 online, 2020 volume). Their research establishes the definition and general bounds and complexity results for chordal and bipartite graphs. The accessible bibliographic abstract does not present a complete weight enumerator for the one-hub clique-bouquet family, but the original article's full text was not available for a direct section-by-section comparison, so this source remains a priority risk.

Mojdeh, Samadi, Shao, and Yero (arXiv:1909.01775, first posted 20 August 2019) give scalar values, small-weight structural cases, general comparisons, and—critically—an exact optimization theorem for graph coronas (Theorem 12). **This theorem does apply here:** the present bouquet is exactly the corona \(K_1\odot H\) where \(H=\bigsqcup_i K_{m_i}\), and \(\Delta(H)\le |V(H)|-2\) because there are at least two blades. Evaluating the theorem with \(\gamma(H)=t\), \(\beta(H)=\sum_i(m_i-1)\), and the appropriate remaining minima recovers the present scalar minimum weight. Hence this scalar equality, and the canonical hub-\(3\) construction of some minimum functions, are treated as **already implied by prior work**, not as novel. The present theorem adds the exact weight histogram of *all* admissible functions, including nonoptimal hub labels, and its specific second-weight coefficient. The cited corona optimization theorem is a minimum over four scalar costs; it does not enumerate excess-weight labelings and does not imply the all-coefficient polynomial.

Rao, Kosari, Sheikholeslami, Chellali, and Kheibari (2021) study tree extremals and bounds for special minimum-degree conditions. Sheikholeslami, Esmaeili, and Volkmann (2024) investigate stability under vertex deletion. Their examined results study optimum values or stability, not complete all-weight counting on clique bouquets. General framework or unpublished results might nevertheless implicitly subsume the enumerator; publication uniqueness is not established by search alone.

The graph family is also called a *one-point union of cliques*, a *block graph with one shared cut vertex*, or, in the equal-sized case, a *generalized windmill*. The complement is an isolated vertex disjoint from a complete multipartite graph. This complement relation does not turn outer-independent double Roman protection under original edges into an ordinary Roman parameter under complement edges: the defense neighborhoods and admissible zero-sets change.

## Limitations

The result assumes at least two blades, each of size at least two. It is an exact identity for this clique-bouquet family only, not for arbitrary block graphs, arbitrary chordal graphs, or general cactus graphs. Counting vertices as labeled is essential; the formula does not count isomorphism classes of labelings. No independent mathematical review or universal publication-priority verification has been performed. An older plausible primary article was accessible at the abstract level but not in full, so undetected overlap with it or other unindexed work remains possible.

## References

1. H. Abdollahzadeh Ahangar, M. Chellali and S. M. Sheikholeslami, *Outer independent double Roman domination*, Applied Mathematics and Computation 364 (2020), Article 124617, DOI: 10.1016/j.amc.2019.124617 (online bibliographic record dated 16 August 2019).
2. D. A. Mojdeh, B. Samadi, Z. Shao and I. G. Yero, *Outer independent double Roman domination number of graphs*, arXiv:1909.01775 (first submitted 20 August 2019), https://arxiv.org/abs/1909.01775.
3. Y. Rao, S. Kosari, S. M. Sheikholeslami, M. Chellali and M. Kheibari, *On the Outer-Independent Double Roman Domination of Graphs*, Frontiers in Applied Mathematics and Statistics 6 (2021), DOI: 10.3389/fams.2020.559132.
4. S. M. Sheikholeslami, M. Esmaeili and L. Volkmann, *Outer Independent Double Roman Domination Stability in Graphs*, Ars Combinatoria 160 (2024), 21–29, DOI: 10.61091/ars-160-04.
