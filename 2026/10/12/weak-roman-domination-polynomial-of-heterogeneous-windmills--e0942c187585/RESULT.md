# Weak Roman domination polynomial of heterogeneous windmills
## Finding
For integers \(r\ge2\) and \(m_1,\ldots,m_r\ge2\), let
\[
W(m_1,\ldots,m_r)=K_1\vee(K_{m_1}\cup\cdots\cup K_{m_r}).
\]
Write \(c\) for the universal center and \(B_i\cong K_{m_i}\) for the \(i\)-th clique blade. A weak Roman dominating function is a labeling \(f:V(W)\to\{0,1,2\}\) such that for every zero-labeled vertex \(u\), one can move one unit from a positive neighbor \(v\) to \(u\) and leave no undefended vertex. Equivalently, after the move the positive support must be a dominating set.

Let \(M=\sum_{i=1}^r m_i\), \(T(x)=1+x+x^2\), and
\[
A_i(x)=T(x)^{m_i}-1.
\]
Then \(f\) is weak Roman dominating exactly in one of the following three center cases:

1. \(f(c)=2\): no further restriction is imposed on the blades.
2. \(f(c)=1\): at most one blade is identically zero.
3. \(f(c)=0\): every blade contains at least one positive label.

Hence the complete weight enumerator is
\[
\mathcal W_{m_1,\ldots,m_r}(x)
=x^2T(x)^M+(1+x)\prod_{i=1}^r A_i(x)
+x\sum_{i=1}^r\prod_{j\ne i}A_j(x).
\]
Evaluating at \(x=1\) gives the exact number of weak Roman dominating functions:
\[
3^M+2\prod_{i=1}^r(3^{m_i}-1)
+\sum_{i=1}^r\prod_{j\ne i}(3^{m_j}-1).
\]

The weak Roman domination number is \(2\). For \(r=2\), the minimum functions are exactly: the center labeled \(2\) and all peripheral vertices \(0\); or the center labeled \(1\), one blade all zero, and exactly one vertex of the other blade labeled \(1\); or the center labeled \(0\) and exactly one vertex in each blade labeled \(1\). Thus there are
\[
1+m_1+m_2+m_1m_2=(m_1+1)(m_2+1)
\]
minimum functions. For every \(r\ge3\), the unique minimum function labels the center \(2\) and every peripheral vertex \(0\).

## Assumptions and scope
The graph is finite, simple, and undirected. The claimed domain is \(r\ge2\) with every \(m_i\ge2\). The lower bound on the blade sizes avoids complete-multipartite degeneracies and keeps the family in the natural clique-windmill regime. No claim is made about total weak Roman domination, higher-order protection, or other Roman-type variants.

## Proof
For any labeling \(g\), saying that no vertex is undefended is exactly saying that its positive support
\[
P(g)=\{v:g(v)>0\}
\]
is a dominating set. In the windmill graph, if the center belongs to \(P(g)\), then \(P(g)\) dominates automatically. If the center does not belong to \(P(g)\), then \(P(g)\) dominates exactly when every blade contains a positive vertex, because a peripheral vertex sees only the center and its own blade.

Suppose first that \(f(c)=2\). Every zero peripheral vertex can use the center as defender. After one unit moves from \(c\), the center still has label \(1\), so the new positive support dominates. Thus every assignment on the blades is feasible, giving \(x^2T(x)^M\).

Suppose next that \(f(c)=1\). A zero peripheral vertex in a nonempty blade can use any positive vertex from its own blade; the center stays positive, so domination is preserved. If an entire blade \(B_i\) is zero, its vertices can only use the center. After moving the center's unit into \(B_i\), the center becomes zero, so every other blade must already contain a positive vertex. Therefore an empty blade is allowed exactly when it is the unique empty blade. The center-label-one contribution is
\[
x\left(\prod_{i=1}^r A_i(x)+\sum_{i=1}^r\prod_{j\ne i}A_j(x)\right).
\]

Finally suppose that \(f(c)=0\). The initial positive support must dominate, so every blade must be nonempty. Under that condition the zero center can be defended from any positive peripheral vertex; moving a unit to the center makes the center positive. A zero peripheral vertex can be defended from a positive vertex of its own blade; the move merely keeps that blade nonempty. Hence the condition is exactly that every blade be nonempty, contributing \(\prod_i A_i(x)\).

Adding the three disjoint center cases yields the displayed polynomial. The total count follows from \(T(1)=3\) and \(A_i(1)=3^{m_i}-1\).

For the minimum layer, the center-label-two case supplies weight \(2\). If \(r=2\), the center-label-one case also has weight \(2\) by leaving one blade empty and choosing one label \(1\) in the other, while the center-label-zero case has weight \(2\) by choosing one label \(1\) in each blade. These are the stated \(1+m_1+m_2+m_1m_2\) functions. If \(r\ge3\), the least possible weight in the center-label-one and center-label-zero cases is respectively \(r\) and \(r\), both at least \(3\), so the center-label-two function is the unique minimum.

## Verification
The proof above is symbolic and applies to all parameters in the stated domain. The standalone checker `verify.py` independently constructs the graph, implements the definition of weak Roman domination by testing every allowed one-unit move, and exhaustively compares that definition with the three-case structural criterion and with every coefficient of the polynomial for six nonisomorphic parameter tuples. It also checks the minimum-weight multiplicities.

Expected output is:

`VERIFY_OK cases=6 labelings=31590 coefficient_checks=78 minimum_checks=6 max_order=9`

The finite computation is a stress test only; the infinite claim follows from the center/blade proof.

## Relationship to prior work
Henning and Hedetniemi introduced weak Roman domination in 2003 and established general inequalities and extremal characterizations. Pushpam and Mai later studied weak Roman domination for trees and split graphs and characterized equality with ordinary domination in those classes. Chellali, Haynes, and Hedetniemi developed general bounds relating weak Roman and \(2\)-rainbow domination, including results for a cactus subfamily. None of these inspected statements gives an all-function weight enumerator for clique windmills.

A later result proves that every Roman \(\{2\}\)-dominating function is weak Roman dominating, but this implication supplies only a subclass of the functions counted here. Likewise, an exact weak Roman polynomial for complete multipartite graphs does not specialize to the present family when \(r\ge2\) and every \(m_i\ge2\): vertices inside one blade are adjacent while vertices in different blades are nonadjacent, so nonadjacency is not the equivalence relation required by a complete multipartite graph.

The closest same-object enumerative comparison is the Roman domination polynomial of generalized windmills. Roman domination is strictly stronger here: for example, with center label \(1\), one empty blade, and positive labels only in the other blades, the structural criterion above can be satisfied without any label \(2\), so the function is weak Roman but not Roman. Thus that polynomial does not determine the present one.

## Limitations
The literature search located no earlier all-function formula under the aliases weak Roman domination, friendship graph, generalized windmill, heterogeneous windmill, or universal vertex joined to disjoint cliques. The especially relevant 2011 split-graph paper was available through abstract and bibliographic records, but its full text could not be read through the available access route in this run; its advertised scope does not contain the claimed windmill family, yet an unindexed family-specific remark remains a residual literature risk. No statement is made that the search proves global uniqueness.

## References
1. M. A. Henning and S. T. Hedetniemi, “Defending the Roman Empire—A new strategy,” *Discrete Mathematics* 266 (2003), 239–251. DOI: 10.1016/S0012-365X(02)00811-7.
2. P. Roushini Leely Pushpam and T. N. M. Malini Mai, “Weak Roman domination in graphs,” *Discussiones Mathematicae Graph Theory* 31 (2011), 161–170. DOI: 10.7151/DMGT.1532.
3. M. Chellali, T. W. Haynes, and S. T. Hedetniemi, “Bounds on weak Roman and 2-rainbow domination numbers,” *Discrete Applied Mathematics* 178 (2014), 27–32. DOI: 10.1016/j.dam.2014.06.016.
4. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, “Roman {2}-domination,” *Discrete Applied Mathematics* 204 (2016), 22–28. DOI: 10.1016/j.dam.2015.11.013.
