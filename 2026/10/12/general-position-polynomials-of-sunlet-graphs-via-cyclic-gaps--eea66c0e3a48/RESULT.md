# General-position polynomials of sunlet graphs via cyclic gaps

## Finding

For every integer \(n\ge3\), form the **sunlet** \(S_n=C_n\circ K_1\) by attaching a distinct degree-one leaf \(\ell_i\) to each vertex \(v_i\) of the cycle \(C_n\), with indices \(i\in\mathbb Z/n\mathbb Z\). Write
\[
\Psi_n(x)=\sum_{S\subseteq V(S_n)\atop S\text{ in general position}}x^{|S|}=\sum_{k=0}^{n}a_{n,k}x^k.
\]
The first coefficients are
\[
a_{n,0}=1,\qquad a_{n,1}=2n,\qquad a_{n,2}=4\binom n2+n.
\]
For \(3\le k\le n\), choose a \(k\)-element subset \(I\subseteq\mathbb Z/n\mathbb Z\). In increasing cyclic order write \(I=(i_1,\ldots,i_k)\), its positive clockwise gaps as \(g_j=i_{j+1}-i_j\pmod n\), and \(g_0=g_k\). Then
\[
\boxed{a_{n,k}=\sum_{I\in\binom{\mathbb Z/n\mathbb Z}{k}}
2^{\,|\{j:2(g_{j-1}+g_j)>n\}|}.}
\tag{1}
\]
Equivalently, in terms of cyclic compositions, 
\[
\boxed{a_{n,k}=\frac nk\sum_{g_1+\cdots+g_k=n\atop g_j\ge1}
2^{\,|\{j:2(g_{j-1}+g_j)>n\}|}.}
\tag{2}
\]
These identities count **every** general-position set at **every** cardinality; they are not merely maximum-set formulas. An explicit finite-sum coefficient formula requiring polynomially many arithmetic operations is given below. In particular, \(\operatorname{gp}(S_n)=n\) for all \(n\ge3\); for \(n\ge4\), the set of all \(n\) leaves is the **unique** set of maximum cardinality. At \(n=3\), there are exactly eight maximum sets.

## Assumptions and scope

Graphs are finite, simple, undirected, and unweighted. A set of vertices is **in general position** when no three distinct selected vertices occur on one shortest path. Equality in the shortest-path triangle inequality is forbidden even if there is an alternative shortest path avoiding the third vertex. No result is claimed about all graph coronas, nor about unimodality of \(\Psi_n\) for arbitrary \(n\).

A binomial coefficient \(\binom ab\) is interpreted as zero unless \(a\ge0\) and \(0\le b\le a\). Empty sums are zero. To evaluate the coefficients without summing over all index subsets, define for \(3\le k\le n\):
\[
U_{n,k}=n\sum_{d=k-2}^{\lfloor(n-1)/2\rfloor}
(n-1-d)\binom{d-1}{k-3}.
\tag{3}
\]
For \(k=3\), define
\[
V_{n,3}=n\sum_{\substack{a,b,c\ge1\\a+b+c=n\\2(a+b)>n\\2(a+c)>n}}1,
\quad
W_{n}=\frac n3\left[\binom{n-1}{2}-3\binom{\lfloor n/2\rfloor}{2}\right].
\tag{4}
\]
For \(4\le k\le n\), define
\[
V_{n,k}=n\sum_{\substack{a,b,c\ge1\\2(a+b)>n\\2(a+c)>n}}
\binom{n-a-b-c-1}{k-4}.
\tag{5}
\]
The ranges are finite because terms with an out-of-range upper binomial argument vanish; one can equivalently demand \(a+b+c\le n-(k-3)\). The all-cardinality coefficient identity is
\[
\boxed{a_{n,k}=\binom nk+U_{n,k}+V_{n,k}+\mathbf1_{\{k=3\}}W_n,\qquad3\le k\le n.}
\tag{6}
\]
Thus each coefficient is obtainable by an \(O(n^3)\) triple sum, and the entire polynomial by at most \(O(n^4)\) elementary integer arithmetic operations, apart from integer-bit complexity.

## Proof

**1. Reduction to one selection per cycle site.** If a set \(S\) has cardinality at least three and contains both \(v_i\) and its leaf \(\ell_i\), then any third selected vertex \(w\) makes \(v_i\) lie on the unique first edge of every shortest path from \(\ell_i\) to \(w\). Hence no general-position set of cardinality at least three selects two vertices at one site. Conversely, for each choice of supporting sites \(I\), choosing one root or one leaf at each supporting site gives all possible sets of cardinality \(k=|I|\ge3\).

**2. The cyclic-gap criterion.** A selected leaf cannot be an interior point of any simple path, so only selected roots can violate general position. Fix a supporting site \(i_j\) whose root is selected, and let \(g_{j-1},g_j\) be the clockwise gaps immediately preceding and following this site in the cyclic ordering of all supported sites. The clockwise arc between the supported predecessor and successor that passes through \(i_j\) has length \(g_{j-1}+g_j\). A shortest path between selected vertices at those predecessor and successor sites uses \(v_{i_j}\) whenever \(2(g_{j-1}+g_j)\le n\), because the two possible routes around the cycle have lengths summing to \(n\); attaching leaves to endpoints adds the same constant to both lengths. This includes the equality case, when *both* cycle arcs are geodesics.

Conversely, every cycle arc between two other supported sites that contains \(i_j\) has length at least \(g_{j-1}+g_j\). If \(2(g_{j-1}+g_j)>n\), every such arc is strictly longer than the alternative complementary arc, so no geodesic between two other selected vertices passes through \(v_{i_j}\). Thus the root at site \(i_j\) may be selected **if and only if** \(2(g_{j-1}+g_j)>n\). A leaf may always be selected instead. Different sites impose no further constraints. For fixed \(I\), there are therefore exactly \(2^{e(I)}\) choices, where \(e(I)\) is the number of sites satisfying this strict inequality. This proves (1).

To obtain (2), mark one of the \(k\) cyclically ordered selected sites. There are \(k\) markings per selected index set, and \(n\) choices for the location of the marked site for each positive ordered gap composition summing to \(n\). The weight is invariant under rotating the gaps, hence the factor \(n/k\). The cases \(k=0,1,2\) follow separately because every set of at most two vertices is automatically in general position: for \(k=2\) there are four cross-site choices for each pair of distinct sites and one root-leaf pair at each same site.

**3. Counting root-eligible markings.** Fix \(k\ge3\). Let \(e(I)\) denote the number of root-eligible sites of \(I\). Then the total \(\sum_I e(I)\) is \(U_{n,k}\). Indeed, mark a root-eligible site, and denote by \(a,b\ge1\) its following and preceding gaps. Put \(d=n-a-b\). Eligibility says \(d<n/2\), so \(k-2\le d\le\lfloor(n-1)/2\rfloor\). There are \(n\) choices for the marked vertex, \(n-1-d\) positive ordered solutions of \(a+b=n-d\), and \(\binom{d-1}{k-3}\) ways to distribute the remaining \(k-3\) supported sites inside the arc of \(d\) edges between these two neighbors. This is (3).

**4. Counting pairs of eligible sites.** If \(k\ge4\), two nonadjacent supported sites cannot both be eligible: their respective pairs of neighboring gaps are disjoint, and each pair would have sum strictly exceeding \(n/2\), contradicting the total gap sum \(n\). Consequently, for \(k\ge4\), every pair of eligible sites consists of consecutive sites around the selected cyclic order; moreover \(e(I)\le2\). To count a marked adjacent pair, let \(a\) be its internal gap, \(b\) the gap immediately preceding its first site, and \(c\) the gap immediately following its second. Eligibility is exactly \(2(a+b)>n\) and \(2(a+c)>n\). Once the first vertex is chosen in \(n\) ways, the remaining arc length \(n-a-b-c\) is split into \(k-3\) positive gaps in \(\binom{n-a-b-c-1}{k-4}\) ways. Each unordered eligible pair is marked once in clockwise consecutive order. Therefore \(\sum_I\binom{e(I)}2=V_{n,k}\) for \(k\ge4\).

When \(k=3\), every pair of selected sites is adjacent in the cyclic order. Mark the first site in clockwise order for each eligible pair, and call the three successive cyclic gaps \(a,c,b\). The three gaps sum to \(n\), and the same two strict inequalities apply, giving \(\sum_I\binom{e(I)}2=V_{n,3}\). A triple has all three roots eligible precisely when **all three gaps are strictly smaller than \(n/2\)**. There are \(\binom{n-1}{2}\) positive compositions of \(n\) into three parts; exactly \(\binom{\lfloor n/2\rfloor}{2}\) have a specified part at least \(n/2\). These exceptional events are pairwise disjoint because the third gap must be positive. After choosing a starting vertex in \(n\) ways and dividing by three choices of marked site, this yields \(\sum_I\binom{e(I)}3=W_n\).

Finally, for every nonnegative integer \(e\), \(2^e=\sum_{j=0}^{e}\binom ej\). For \(k\ge4\), \(e(I)\le2\), and for \(k=3\), \(e(I)\le3\). Summing the binomial identity and using the preceding counts proves (6).

**5. Maximum size.** Every general-position set of size at least three supports distinct sites, so it has cardinality at most \(n\). The set of all \(n\) leaves attains this bound. If \(n\ge4\) and all sites are selected, all cyclic gaps equal one; then \(2(g_{j-1}+g_j)=4\le n\), so no root can be used. Thus the all-leaf set is the unique maximum. For \(n=3\), all three sites have \(2(g_{j-1}+g_j)=4>3\), yielding eight maximum sets. This completes the proof.

## Verification

The accompanying standalone Python program \(`verify.py`\) constructs sunlets, computes all-pairs graph distances by breadth-first search, and directly tests the three possible betweenness equalities for every selected vertex triple in every subset of \(V(S_n)\) for \(3\le n\le9\). It independently computes the cyclic-gap sum (1) and the binomial formula (6). All three enumerations agree in **349,504 exhaustive vertex-subset tests**. For \(10\le n\le16\), all \(2^n\) supporting-site subsets are compared to (6). For \(17\le n\le32\), further arithmetic sanity checks include nonnegative integer coefficients and the unique top-degree coefficient. The output is supplied in \(`verification_output.txt`\). Finite verification supports, but does not substitute for, the proof for arbitrary \(n\).

For example,
\[
\Psi_5(x)=1+10x+45x^2+60x^3+20x^4+x^5,
\]
\[
\Psi_6(x)=1+12x+66x^2+88x^3+39x^4+6x^5+x^6,
\]
\[
\Psi_7(x)=1+14x+91x^2+196x^3+140x^4+49x^5+7x^6+x^7.
\]
The \(n=6\) polynomial agrees with a **previously published example**, not a new finite-case calculation.

## Relationship to prior work

Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial in 2024, treated several graph families including cycles and path coronas (combs), and posed the corona-unimodality question. The present result supplies an explicit all-cardinality enumerator for **cycle coronas**, a different natural family not resolved by the cited comb formulas. Rather's 2026 work gives exactly the above polynomial for \(C_6\circ K_1\) as an example showing failure of log-concavity and analyzes corona behavior in other families. That \(n=6\) example and its log-concavity observation are **known**, not a new contribution; the theorem here is the structural cyclic-gap criterion and all-\(n\) coefficient enumeration. The 2025–2026 survey catalogs general-position polynomials and general results but does not state this sunlet all-\(n\) formula. A generic inclusion-exclusion identity for an arbitrary graph does not by itself supply the gap classification or its polynomial-time coefficient expression.

## Limitations

The result applies to \(C_n\circ K_1\) with one leaf per cycle vertex and \(n\ge3\). It does not establish unimodality or log-concavity for every \(n\), nor resolve the general corona question. Exhaustive tests stop at finite orders and should not be interpreted as an infinite certificate. A differently indexed or implicit earlier derivation of the all-\(n\) formula may exist. The origin paper's generic inclusion-exclusion principle is older, while the stated all-\(n\) gap criterion and coefficient formulas are the claimed distinct contribution.

## References

1. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, **General position polynomials**, arXiv:2401.05696v1 (first publicly posted 2024-01-11), subsequently *Results in Mathematics* 79, article 110 (2024). https://arxiv.org/abs/2401.05696 ; https://link.springer.com/article/10.1007/s00025-024-02133-3 .
2. B. A. Rather, **Explicit Formulas and Unimodality Phenomena for General Position Polynomials**, arXiv:2603.06930v3 (2026), especially Section 7, including the explicit \(C_6\circ K_1\) example. https://arxiv.org/html/2603.06930v3 .
3. U. Chandran S. V., S. Klavžar, and J. Tuite, **The General Position Problem: A Survey**, arXiv:2501.19385v4 (2026), especially Section 2.3.4. https://arxiv.org/html/2501.19385v4 .
