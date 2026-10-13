# Cardinality enumerator and extremal multiplicities of maximal independent sets in \(P(n,2)\)
## Finding
Let \(P(n,2)\) be the generalized Petersen graph defined below, and let
\[
M_n(z)=\sum_{\substack{S\subseteq V(P(n,2))\\ S\text{ inclusion-maximal independent}}}z^{|S|}.
\]
For every integer \(n\ge5\), define
\[
\begin{aligned}
D(t,z)={}&1-2z^2t^3-3z^3t^4-(2z^3+z^4)t^5\\
&-4z^4t^6-z^5t^7+2z^5t^8+z^6t^9+z^6t^{10}.
\end{aligned}
\]
The **complete cardinality enumerator** is
\[
\boxed{M_n(z)=[t^n]\left(-t\frac{\partial}{\partial t}\log D(t,z)\right)\qquad(n\ge5).}
\]
Equivalently, the ordinary generating series indexed by valid graph orders is
\[
\sum_{n\ge5}M_n(z)t^n=-t\frac{\partial}{\partial t}\log D(t,z)-6z^2t^3-12z^3t^4.
\]
The smallest and largest degrees of a nonzero coefficient are, respectively,
\[
\boxed{\left\lceil\frac{3n}{5}\right\rceil\quad\text{and}\quad
\left\lfloor\frac{4n}{5}\right\rfloor.}
\]
Write \(n=5k+r\) with \(k\ge1\) and \(0\le r\le4\). The numbers of maximal independent sets attaining these two sizes are **exactly**:

| \(r\) | Coefficient at \(\lceil3n/5\rceil\) | Coefficient at \(\lfloor4n/5\rfloor\) |
|---|---|---|
| \(0\) | \(10\) | \(5\) |
| \(1\) | \(6k(5k+1)\) | \(\frac{(5k+1)(27k^3-9k^2+22k+8)}8\) |
| \(2\) | \(\frac{k(5k+2)(14k^2+6k+1)}3\) | \(\frac{(5k+2)(9k^2+3k+2)}2\) |
| \(3\) | \(2(5k+3)\) | \(\frac{(5k+3)(9k+4)}2\) |
| \(4\) | \(\frac{(5k+4)(16k^2+22k+9)}3\) | \(3(5k+4)\) |

For example, \(M_5(z)=10z^3+5z^4\), \(M_6(z)=36z^4\), \(M_7(z)=49z^5\), and \(M_8(z)=16z^5+52z^6\).

## Assumptions and scope
All graphs are finite, simple and undirected. For every integer \(n\ge5\), \(P(n,2)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with distinct edges counted once. An independent set is *maximal* when it is not properly contained in an independent set; equivalently, it is an independent dominating set. It need not have maximum cardinality. Each set is counted once; colors, rotations, and reflection orbits are **not** quotient out. Coefficients are ordinary integers. The restriction \(n\ge5\) ensures the underlying inner step-two graph is the intended simple generalized Petersen graph.

## Proof
**1. Exact local characterization.** For each index choose a symbol \(s_i\in\{0,1,2\}\): \(0\) means neither \(u_i\) nor \(v_i\) is selected; \(1\) selects \(u_i\); \(2\) selects \(v_i\). The spoke prohibits selecting both. Set \((a,b,c,d,e)=(s_{i-2},s_{i-1},s_i,s_{i+1},s_{i+2})\). A cyclic symbol word represents a maximal independent set **if and only if** for every \(i\):

- if \(c=1\), both \(b\ne1\) and \(d\ne1\);
- if \(c=2\), both \(a\ne2\) and \(e\ne2\);
- if \(c=0\), at least one of \(b,d\) equals \(1\), **and** at least one of \(a,e\) equals \(2\).

Indeed the first two conditions are exactly independence along the outer and inner edges. For an empty column, the outer vertex can only be dominated by a selected outer neighbor, and the inner vertex only by a selected inner step-two neighbor; this yields the third condition. Conversely, these cases guarantee that every unselected vertex is dominated. Thus the characterization is necessary and sufficient, without a greedy-order assumption.

**2. Cyclic transfer and an exact determinant.** Index an \(81\)-state matrix \(T\) by words of length four over \(\{0,1,2\}\). Put
\[
T_{(a,b,c,d),(b,c,d,e)}=z^{\mathbf1_{e\ne0}}
\]
when the centered condition above holds, and zero otherwise. For every \(n\ge5\), cyclic closed walks of length \(n\) are in bijection with the indexed valid cyclic words, with the correct weight, so \(M_n(z)=\operatorname{tr}(T^n)\). There is one strongly connected cyclic core with \(27\) states and \(47\) directed edges; every other strongly connected component is a singleton without a self-loop. Hence it suffices to take the determinant over the core. Exact integer-polynomial Newton identities
\[
k d_k=-\sum_{j=1}^{k}d_{k-j}\operatorname{tr}(T^j),\qquad d_0=1
\]
show that the \(27\)-degree characteristic determinant \(\det(I-tT)\) (after deletion of acyclic states) equals the displayed \(D(t,z)\), with all coefficients above degree ten zero. The `verify.py` artifact reconstructs the core, its edges, traces through order \(27\), and every integer coefficient of this identity; it does not assume the determinant as input. Jacobi's formal power-series identity \(-t\partial_t\log\det(I-tT)=\sum_{n\ge1}\operatorname{tr}(T^n)t^n\) proves the all-order enumerator. The formal traces at orders three and four are \(6z^2\) and \(12z^3\), respectively, and are excluded from the graph-order series.

**3. Sharp support bounds.** Give each core state a pair of integer potentials \(p,q\), in lexicographically sorted state order, as stored and checked in `verify.py`. For every core transition \(a\to b\) of weight \(w\in\{0,1\}\), the full certificate checks
\[
p(b)\le p(a)+5w-3,\qquad q(b)\le q(a)+4-5w.
\]
Summing along any closed walk telescopes both potentials and yields \(3n\le5|S|\le4n\). To prove both extremes occur for all orders, start with the core state \((0,1,2,1)\) for the lower endpoint and \((0,1,2,2)\) for the upper endpoint. For \(n=5+r\), \(r=0,1,2,3,4\), the following appended-symbol words are closed walks with precisely the required extremal weights:

| \(r\) | Lower-endpoint closed walk | Upper-endpoint closed walk |
|---|---|---|
| 0 | `00121` | `10122` |
| 1 | `010121` | `010122` |
| 2 | `0120121` | `0120122` |
| 3 | `00120121` | `01210122` |
| 4 | `001210121` | `012210122` |

At each anchor the length-five loop in the first row contributes weight three (lower) or four (upper). Concatenating any number of these loops with the matching residue walk proves attainability for all \(n=5k+r\), \(k\ge1\). All closed walks and weight counts are checked by the verifier.

**4. Extremal coefficient extraction.** The preceding bounds identify the exponents requiring extraction. For the upper endpoint substitute \(t=xy^4\), \(z=y^{-5}\). Up to and including degree four in \(y\), the denominator becomes
\[
D(xy^4,y^{-5})=1-x^5-3x^4y-2x^3y^2-x^7y^3-4x^6y^4+O(y^5).
\]
The relevant deficit is \(\delta=4n-5\lfloor4n/5\rfloor\in\{0,1,2,3,4\}\). For the lower endpoint substitute \(t=xy^{-3}\), \(z=y^5\), giving
\[
\begin{aligned}
D(xy^{-3},y^5)={}&(1-x^5)^2+(-2x^3+2x^8)y-4x^6y^2\\
&+(-3x^4+x^9)y^3-x^7y^4+O(y^5).
\end{aligned}
\]
Here \(\varepsilon=5\lceil3n/5\rceil-3n\in\{0,1,2,3,4\}\). In each case the wanted coefficient is \([x^ny^{\delta}]\bigl(-x\partial_x\log D\bigr)\) or \([x^ny^{\varepsilon}]\bigl(-x\partial_x\log D\bigr)\), respectively. Expand the formal reciprocal through degree four in \(y\); each coefficient has denominator a power of \(1-x^5\). The binomial identity
\[
[x^{5j}](1-x^5)^{-a}=\binom{j+a-1}{a-1},\qquad j\ge0,
\]
with zero for negative \(j\), gives exactly the five formulas in each column of the displayed table. This calculation is finite symbolic algebra, not an inference from numerical interpolation. Its results agree with the untruncated transfer enumerator through order seventy.

## Verification
Run `python3 verify.py` with Python 3.8 or later and no additional packages. It independently reconstructs all \(81\) local transitions, finds the cyclic \(27\)-state core, tests all \(47\) potential inequalities, checks the ten-term determinant with Newton's identities through order \(27\), computes polynomial coefficients by the resulting recurrence through order \(70\), checks every residue-class extremal formula through order \(70\), and exhaustively enumerates all vertex subsets of \(P(n,2)\) for \(5\le n\le8\). The script also verifies all ten explicit extremal closed walks. A successful replay prints `VERIFY_OK`. Direct exhaustive checks cover only the indicated finite orders; the unlimited-order conclusions follow from the combinatorial transfer identity, exact polynomial determinant, potential inequalities, walks, and formal coefficient extraction.

## Relationship to prior work
Besharati, Ebrahimi and Azadi's preprint (arXiv:1008.2583, first public version 2010-08-16) studies maximum *cardinality* and linear-time computation for fixed inner step, and explicitly reports the known value \(\alpha(P(n,2))=\lfloor4n/5\rfloor\). That upper support endpoint is therefore not presented as independently new. A separate 2009 article by Behzad, Hatami and Mahmoodian, *Minimum vertex covers in the generalized Petersen graphs P(n,2)* (Bull. Inst. Combin. Appl. 56:98–102), is directly related by complementation: the accessible abstract reports the known minimum cover cardinality, but its full text was not available for a decisive check of endpoint multiplicities. Nagy (arXiv:1504.03224) studies counts of independent \(k\)-dominating sets and general extremal bounds, not the all-cardinality family enumerator here. Dod (arXiv:1602.08250) introduces and studies the independent domination polynomial, with recurrence formulas and explicit path/cycle examples. The theorem here specializes the same standard polynomial to the distinct family of generalized Petersen graphs and supplies a factored all-order denominator and exact extremal multiplicities. A general identity for an arbitrary graph, or a count of all independent sets without maximality, does not itself give these expressions. Minimal vertex covers provide the exact complementary reformulation: the size enumerator of inclusion-minimal vertex covers is \(z^{2n}M_n(z^{-1})\). The claim includes that reformulation rather than treating it as a second new theorem.

## Limitations
The result is restricted to the step-two generalized Petersen family with \(n\ge5\). It does not assert all intermediate cardinalities occur or extend directly to other inner steps. Known extremal support endpoints and general polynomial definitions are not claimed as novel; priority for the new full generating function and multiplicity formulas remains subject to the possibility of earlier equivalent work under minimal-vertex-cover or independent-domination terminology. A finite verification range is not an exhaustive proof of the infinite family.

## References
1. N. Besharati, J. B. Ebrahimi and A. Azadi, *Independence number of generalized Petersen graphs*, arXiv:1008.2583v1 (2010-08-16), https://arxiv.org/abs/1008.2583 .
2. Z. L. Nagy, *On the number of k-dominating independent sets*, arXiv:1504.03224v1 (2015-04-13), https://arxiv.org/abs/1504.03224 .
3. M. Dod, *The Independent Domination Polynomial*, arXiv:1602.08250v1 (2016-02-26), https://arxiv.org/abs/1602.08250 .
4. M. Behzad, P. Hatami and E. S. Mahmoodian, *Minimum vertex covers in the generalized Petersen graphs P(n,2)*, Bull. Inst. Combin. Appl. 56 (2009), 98–102 (only abstract and bibliographic record accessible).
