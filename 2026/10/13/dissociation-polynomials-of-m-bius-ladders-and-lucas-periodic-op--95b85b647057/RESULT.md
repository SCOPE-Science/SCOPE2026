# Dissociation polynomials of Möbius ladders and Lucas-periodic optimal covers

## Finding

For every integer \(n\ge3\), let \(M_{2n}\) be the Möbius ladder with vertex set \(\mathbb Z/(2n)\) and edges joining \(i\) to \(i+1\), \(i-1\), and \(i+n\), modulo \(2n\). Its dissociation polynomial is
\[
\mathcal D_n(z)=\sum_{\substack{S\subseteq V(M_{2n})\\\Delta(M_{2n}[S])\le1}}z^{|S|}.
\]
Define the explicit polynomials
\[
\begin{aligned}
Q_+(t,z)&=1-(1+z)t-(z+2z^2)t^2+(z^3-z^2)t^3+z^4t^4,\\
Q_-(t,z)&=1+zt+z^2t^2.
\end{aligned}
\]
The complete enumerator for every \(n\ge3\) is characterized by the formal power-series identity
\[
\boxed{\sum_{n\ge3}\mathcal D_n(z)t^n=
-t\frac{\partial}{\partial t}\log\frac{Q_+(t,z)}{Q_-(t,z)}
-(1+2z)t-(1+4z+6z^2)t^2.}
\]
In particular, the dissociation number is exactly \(n\), and the number of maximum dissociation sets is
\[
\boxed{[z^n]\mathcal D_n(z)=L_n+1+2\mathbf1_{2\mid n}-3\mathbf1_{3\mid n},}
\]
where \(L_0=2\), \(L_1=1\), and \(L_n=L_{n-1}+L_{n-2}\). Complementation identifies the counted maximum dissociation sets with the **minimum three-vertex-path covers** (vertex sets meeting every simple path on three vertices); those covers have size exactly \(n\) and the same multiplicity.

## Assumptions and scope

The result concerns finite simple, labeled Möbius ladders with \(n\ge3\), including \(M_6\cong K_{3,3}\). The integer \(n\) counts *rungs*, so the graph has \(2n\) vertices. A dissociation set induces only isolated vertices and isolated edges, with no selected vertex adjacent to two other selected vertices. Every such set, not just inclusion-maximal sets, contributes once. All generating functions are formal power series in \(t\) with coefficients in \(\mathbb Z[z]\); \(\mathbf1\) is an indicator. No analytical convergence assumption is used.

## Proof

**The twisted column trace.** Represent a rung by the two-bit mask \(b\in\{0,1,2,3\}\); bit \(j\in\{0,1\}\) says whether its row-\(j\) vertex was selected. Put \(b_j\in\{0,1\}\) for the bit and \(|b|=b_0+b_1\). Let \(f(b)\) swap the two bits. The Möbius boundary joins row \(j\) at one end to row \(1-j\) at the other. Consequently an \(n\)-rung selection is exactly a sequence of masks \(b_0,\ldots,b_{n-1}\), extended by \(b_n=f(b_0)\) and \(b_{-1}=f(b_{n-1})\), for which, at each rung \(i\) and each occupied bit \(j\),
\[
(b_{i-1})_j+(b_i)_{1-j}+(b_{i+1})_j\le1.
\]
This condition is necessary and sufficient: the three summands count the selected neighbors of the selected row-\(j\) vertex (the preceding rail, its rung-mate, and the following rail).

Index sixteen states by ordered pairs \((a,b)\in\{0,1,2,3\}^2\). Define a \(16\)-by-\(16\) weighted integer-polynomial matrix \(T\) by
\[
T_{(a,b),(b,c)}=z^{|b|}\quad\text{if for each selected bit }j\text{ of }b,
\quad a_j+b_{1-j}+c_j\le1,
\]
and let all other entries vanish. The matrix has \(41\) nonzero entries. Let \(F\) be the permutation matrix of \((a,b)\mapsto(f(a),f(b))\). The mask condition gives an exact weight-preserving bijection between valid selections and length-\(n\) state walks from \((b_{-1},b_0)\) to its flipped image. Hence, for every \(n\ge3\),
\[
\mathcal D_n(z)=\operatorname{tr}(F T^n).
\]
The bound \(n\ge3\) ensures that the prescribed Möbius ladder is simple and the three neighbors in the displayed condition are distinct.

**Exact finite determinant step.** Simultaneous row interchange preserves the transition condition, so \(TF=FT\). Among the sixteen states, four are fixed by \(F\) and the remaining twelve form six two-element orbits. The \(+1\) and \(-1\) eigenspaces of \(F\) have dimensions \(10\) and \(6\). Choose the four fixed state vectors, the six sums of paired state vectors, and the six differences as a change-of-basis matrix \(P\). This gives a block diagonal conjugate \(P^{-1}TP=\operatorname{diag}(T_+,T_-)\). Direct *exact polynomial* determinant expansion gives
\[
\det(I-tT_+)=Q_+(t,z),\qquad\det(I-tT_-)=Q_-(t,z).
\]
These are finite identities of integer polynomials, not estimated numerical equalities. The full state construction, the basis, and a runnable exact symbolic determinant computation appear in `verify.py`; this is a reproducible certificate for the nonstandard finite step. For every matrix \(B\), the formal identity \(-t\partial_t\log\det(I-tB)=\sum_{n\ge1}\operatorname{tr}(B^n)t^n\) follows from the formal log-determinant series (or Newton identities). Applying it to the two blocks with opposite signs proves the claimed trace series. The first two formal trace terms are \(1+2z\) and \(1+4z+6z^2\), and must be removed, as those two orders are excluded from the simple-ladder domain.

**Maximum degree and Lucas multiplicity.** Every monomial \(t^kz^j\) occurring in either \(Q_+\) or \(Q_-\) satisfies \(j\le k\). Inversion and formal logarithms preserve this degree filtration, so \(\deg_z\mathcal D_n(z)\le n\). To extract the top degree, substitute \(t=u/z\) and take the constant term in \(1/z\). The two determinant polynomials tend to
\[
q_+(u)=(1-u^2)(1-u-u^2),\qquad q_-(u)=\frac{1-u^3}{1-u}.
\]
Thus the top-degree generating series (the first two order corrections vanish after restricting to \(n\ge3\)) is
\[
\sum_{n\ge3}[z^n]\mathcal D_n(z)u^n
=\left[-u\frac{d}{du}\log\left(\frac{(1-u^2)(1-u-u^2)(1-u)}{1-u^3}\right)\right]_{u^{\ge3}}.
\]
The coefficient of \(-u\frac{d}{du}\log(1-u-u^2)\) is \(L_n\). The other logarithms contribute respectively \(2\mathbf1_{2\mid n}\), \(1\), and \(-3\mathbf1_{3\mid n}\). This yields the stated exact multiplicity. The expression is positive for every \(n\ge3\) (at \(n=3\) it equals \(2\), and thereafter Lucas numbers increase), so the upper degree bound is attained. A vertex set meets every three-vertex path if and only if its complement induces maximum degree at most one. The complementary minimum-cover assertion follows immediately, with no additional hypothesis.

## Verification

The included `verify.py` requires Python 3.10 or later and SymPy 1.14. It forms the sixteen-state matrix, verifies the commuting row swap, constructs the explicit symmetry basis, and computes **both polynomial determinants exactly**. Separately, it builds the graph on the cyclic vertex set and tests all \(2^{2n}\) selected masks for each \(n=3,\ldots,10\), comparing **every** coefficient: \(1{,}398{,}080\) subsets in total. A sparse, integer-polynomial propagation independently checks the twisted traces through \(n=32\), and the top-degree formula is checked through \(n=100\). Those finite tests support the construction; the formal trace/determinant and coefficient arguments, not extrapolation from checked orders, prove the unrestricted claim.

## Relationship to prior work

Orlovich, Dolgui, Finke, Gordon and Werner formalized dissociation-set questions and studied their complexity and tractable graph classes. Tu, Xiao and Lang obtained a universal *upper bound* on the dissociation polynomial for cubic graphs, but their theorem does not supply this family-specific coefficient formula. Zhou, Chen, Deng and Tu enumerated dissociation sets for rectangular Cartesian grids by transfer matrices; ordinary open-grid boundary vectors do not impose the Möbius flip. Tian and Tu count **inclusion-maximal** dissociation sets on several grid variants, which is a different quantity from all dissociation sets. The cyclic prism, with an untwisted seam, provides a natural comparison, but its ordinary trace does not determine the **twisted trace** without additional flip-eigenspace information. The present exact formula resolves that nonorientable boundary explicitly.

## Limitations

This is an exact result for the specified width-two Möbius-ladder family, not an assertion about all circular ladders, all generalized Petersen graphs, or higher-width twisted strips. It does not classify the internal isomorphism types of each dissociation set, and it does not imply a universal dissociation bound sharper than published cubic-graph bounds. An earlier equivalent calculation under one-dependence or three-path-cover terminology may exist and has not been ruled out by literature searches. The 2024 maximal-dissociation paper was available only at abstract level for the present comparison; its different invariant does not directly settle the present polynomial. No independent mathematical audit is claimed.

## References

1. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, “The complexity of dissociation set problems in graphs,” *Discrete Applied Mathematics* **159** (2011), 1352–1366. DOI: 10.1016/j.dam.2011.04.023.
2. J. Tu, J. Xiao and R. Lang, “Counting the number of dissociation sets in cubic graphs,” *AIMS Mathematics* **8** (2023), 10021–10032. DOI: 10.3934/math.2023507.
3. W. Zhou, G. Chen, H. Deng and J. Tu, “Enumeration of dissociation sets in grid graphs,” *AIMS Mathematics* **9** (2024), 14899–14912. DOI: 10.3934/math.2024721.
4. Y. Tian and J. Tu, “Enumerating maximal dissociation sets in three classes of grid graphs,” *Applied Mathematics and Computation* **474** (2024), 128711. DOI: 10.1016/j.amc.2024.128711.
