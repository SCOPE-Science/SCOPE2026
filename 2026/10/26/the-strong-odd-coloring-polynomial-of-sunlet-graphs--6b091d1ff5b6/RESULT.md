# The strong odd coloring polynomial of sunlet graphs

## Finding

For every integer \(n\ge 3\), let \(S_n=C_n\circ K_1\) be the sunlet graph: the cycle on labeled vertices \(v_0,\ldots,v_{n-1}\) together with one distinct pendant vertex \(w_i\) adjacent to each \(v_i\), with cycle subscripts taken modulo \(n\). Write \(F_n(q)\) for the number of proper strong odd vertex colorings \(V(S_n)\to\{1,\ldots,q\}\), with named colors; unused colors are permitted. In a strong odd coloring, every color occurring in each open neighborhood has odd multiplicity.

Define polynomials
\[
 a=1+(q-3)(q-2),\qquad r=4-q,
\]
and an integer-polynomial sequence by
\[
 U_0=2,\qquad U_1=3-q,\qquad
 U_{j+2}=-(q-3)U_{j+1}+raU_j\quad (j\ge0).
\]
Then for every \(n\ge3\) and every integer \(q\ge0\),
\[
 \boxed{F_n(q)=a^n+(q-1)U_n+
 \frac{q(q-3)}2r^n+
 \frac{(q-1)(q-2)}2(-r)^n.}
\]
The right-hand side is a polynomial in \(q\) with integer coefficients despite its displayed fractional factors.

In particular,
\[
 F_n(4)=3^n+3(-1)^n,\qquad
 F_n(3)=3+3(-1)^n,\qquad
 F_n(2)=1+(-1)^n.
\]
Consequently, the strong odd chromatic number is \(2\) for even \(n\) and \(4\) for odd \(n\). There are exactly two optimal colorings with named optimal colors when \(n\) is even, and exactly \(3^n-3\) when \(n\) is odd. For each fixed integer \(q\ge4\), the all-palette count has the exact exponential rate \(F_n(q)\sim a^n\) as \(n\to\infty\).

## Assumptions and scope

Graphs are finite, simple and undirected. The symbol \(C_n\circ K_1\) denotes a *corona* (attachment of an individual leaf to every cycle vertex), not the lexicographic product. The parameter \(q\) is the number of *available*, individually named colors, not necessarily the number appearing in a given coloring. The graph vertices are distinguished by their cyclic indices. The polynomial formula holds for every \(n\ge3\) and every nonnegative integer \(q\), and all multiplicities count individual labeled assignments, not classes modulo graph or color permutations.

## Proof

**Pendant extension rule.** Fix a proper coloring \((c_0,\ldots,c_{n-1})\) of the rim using colors from a palette of size \(q\). The degree-one vertices create no additional neighborhood-parity restrictions, apart from being colored differently from their adjacent rim vertices. At the degree-three vertex \(v_i\), the three neighbor colors must either coincide or be pairwise distinct: a multiset of three labels is odd at every occupied label precisely in these two cases.

If \(c_{i-1}=c_{i+1}\), the color on \(w_i\) is forced to equal this common color. Properness of the rim already makes it distinct from \(c_i\). If \(c_{i-1}\ne c_{i+1}\), those two rim-neighbor colors and \(c_i\) are three distinct labels, and the pendant color can be any of the remaining \(q-3\) labels. These pendant choices are independent across positions. Thus \(F_n(q)\) is an exact weighted sum over proper cyclic rim colorings, assigning weight \(1\) at a two-step backtrack and \(q-3\) at a nonbacktrack.

**Transfer trace.** For an integer \(q\ge3\), index \(q(q-1)\) directed states by ordered pairs \((b,c)\) of distinct colors. A transition \((a,b)\to(b,c)\) with \(c\ne b\) has weight \(1\) when \(a=c\) and weight \(q-3\) otherwise; every other transition has weight zero. Let \(T\) denote the resulting matrix. A closed walk of length \(n\), with its fixed initial coordinate, is in bijection with an indexed proper rim coloring and has exactly the product of its pendant extension counts as weight. Therefore
\[
 F_n(q)=\operatorname{tr}(T^n).
\]

**Exact spectrum.** Put \(t=q-3\), so \(r=1-t\), and let \(W\) be the space of real-valued functions on the ordered unequal-color pairs. For \(f\in W\), set \(R_b=\sum_{c\ne b}f(b,c)\). The transfer operator acts by
\[
 (Tf)(a,b)=tR_b+r f(b,a).
\]
The constant functions form a one-dimensional eigenspace with eigenvalue \(a=1+t(q-2)\). The \(2(q-1)\)-dimensional space of functions \(f(a,b)=u_a+v_b\), with \(\sum_a u_a=\sum_bv_b=0\), is invariant; its coefficient transformation is
\[
 \binom{u'}{v'}=
 \begin{pmatrix}0&r\\a&-t\end{pmatrix}\binom{u}{v},
\]
acting independently on each of \(q-1\) centered color directions. Its two eigenvalues, counted with algebraic multiplicity, are the roots of
\[
 \lambda^2+t\lambda-ra=0.
\]
Their power sum is exactly \(U_n\), since \(U_0=2\), \(U_1=-t\), and the characteristic equation yields \(U_{j+2}=-tU_{j+1}+raU_j\).

The complementary subspace consists of functions with every row sum and every column sum equal to zero. It is invariant under transposition, and \(T\) acts there as \(r\) times transposition. Its symmetric part has dimension \(\binom q2-q=q(q-3)/2\), since the unsigned incidence matrix of \(K_q\) has rank \(q\) over \(\mathbb R\) for \(q\ge3\). Its antisymmetric part has dimension \(\binom q2-(q-1)=(q-1)(q-2)/2\), since the oriented incidence matrix has rank \(q-1\). These receive eigenvalues \(r\) and \(-r\), respectively. The displayed invariant subspaces are a direct sum: a centered sum-type function with zero row and column sums must vanish when \(q\ge3\), and the dimensions add to \(q(q-1)\). Taking the trace of \(T^n\) gives the boxed formula for all integers \(q\ge3\).

Each side of the claimed formula is a polynomial in \(q\) for fixed \(n\). The left side is a polynomial because one can partition all assignments of \(2n\) labeled vertices by their equality patterns and count injective labels of each admissible pattern by a falling factorial in \(q\). The two polynomials agree at every integer \(q\ge3\), so they are identical and in particular agree for \(q=0,1,2\). Directly, the nonempty graph has no valid colorings for \(q=0,1\), and its only strong odd two-colorings are the two bipartite colorings when \(n\) is even.

**Optimal palettes and growth.** For \(q=3\), the pendant extension rule makes every rim vertex's two cyclic neighbors equal, hence forces a two-periodic rim. This is possible precisely for even \(n\). For \(q=4\), \(r=0\), \(a=3\) and \(U_n=(-1)^n\) for \(n\ge1\), so \(F_n(4)=3^n+3(-1)^n\), positive for odd \(n\ge3\). This proves the optimal-palette claims. For fixed \(q\ge5\), let \(s=q-4\ge1\). Then \(a=s^2+3s+3\), while the two quadratic roots are complex conjugates of modulus \(\sqrt{sa}<a\) (their discriminant is \(-4s^3-11s^2-10s+1<0\)). Also \(|r|=s<a\). Thus every nonleading term is exponentially smaller than \(a^n\). The same conclusion holds at \(q=4\) by the explicit formula.

## Verification

The standalone file `verify.py` tests the *original* properness and open-neighborhood parity definition by exhaustive labeled color assignments in 11 small cases, examining 488356 assignments with proper rims. An independent directed-state trace algorithm checks the closed formula for all 84 pairs \((n,q)\) with \(3\le n\le14\) and \(2\le q\le8\). It also checks the low-palette specializations, and its recorded output is in `verification_output.txt`. The infinite assertions follow from the preceding invariant-subspace argument, not from bounded enumeration.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and bounds for sparse graphs [1]. Caro, Petruševski, Škrekovski and Tuza [2, Proposition 2.2] proved that connected unicyclic graphs other than the five-cycle admit strong odd four-colorings. Their theorem supplies an upper bound but not the sunlet's full all-palette counting polynomial, its recurrence, or the exact numbers of optimal assignments. In particular, the identity for \(F_n(4)\) is not equivalent to the full all-palette formula, which records the behavior for every \(q\). The transfer calculation also differs from simply evaluating the ordinary chromatic polynomial of the rim, because for \(q\ge5\), pendant extension multiplicities depend on cyclic backtracking positions.

## Limitations

The theorem applies only to cycles with exactly one pendant leaf attached to every cycle vertex. It counts named-color assignments, not symmetry orbits, and does not classify structural equivalence classes of colorings. It does not give an analogous formula for arbitrary unicyclic graphs. Independent mathematical audit and exhaustive bibliographic priority checking have not been carried out; an unindexed equivalent enumerator remains possible.

## References

[1] H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, first posted 22 January 2024, arXiv:2401.11653.

[2] Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, first posted 3 October 2024, arXiv:2410.02336, especially Proposition 2.2.
