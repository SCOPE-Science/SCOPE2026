# A four-mode counting law for proper conflict-free colorings of hairy cycles

## Finding
For integers \(n\ge3\), \(a\ge1\), let \(H_{n,a}=C_n\odot\overline{K_a}\): start from the simple cycle with indexed core vertices \(v_0,\ldots,v_{n-1}\), and attach \(a\) **distinct, labelled pendant vertices** to each core vertex. A coloring with palette \([q]=\{1,\ldots,q\}\) is *proper conflict-free* (PCF) when adjacent vertices receive different colors and every non-isolated vertex has a color occurring exactly once in its **open** neighborhood. Colorings need not use all colors. Let \(F_{n,a}(q)\) count them, for integers \(q\ge3\).

Define the two nonnegative integer local weights
\[
\begin{aligned}
r_a(q)&=(q-1)^a-a![z^a]e^z(e^z-z)^{q-2},\\
s_a(q)&=(q-1)^a-a![z^a](e^z-1)^2(e^z-z)^{q-3},
\end{aligned}
\]
where \([z^a]\) means an ordinary coefficient of the stated exponential generating series. Set \(r=r_a(q)\), \(s=s_a(q)\), \(h=r+(q-2)s\), and define integer-polynomial quantities by \(U_0=2\), \(U_1=-s\), and
\[
U_j=-sU_{j-1}-(s-r)hU_{j-2}\qquad(j\ge2).
\]
Then, for every \(n\ge3\), \(a\ge1\), and integer \(q\ge3\), **the complete labeled-palette PCF coloring count** is
\[
\boxed{F_{n,a}(q)=h^n+(q-1)U_n+\frac{q(q-3)}2(r-s)^n+\frac{(q-1)(q-2)}2(s-r)^n.}
\]
The right-hand side is an integer polynomial in \(q\) for fixed \(n,a\); indeed, it is the PCF chromatic counting polynomial. Its three-color specialization is especially simple:
\[
r_a(3)=a,\quad s_a(3)=2,\quad
F_{n,a}(3)=(a+2)^n+2U_n+(2-a)^n,
\]
where \(U_0=2\), \(U_1=-2\), and \(U_j=-2U_{j-1}-(4-a^2)U_{j-2}\). At \(a=2\), every proper three-coloring of the core \(C_n\) has **exactly \(2^n\) PCF extensions**, independent of its pattern, and therefore
\[
\boxed{F_{n,2}(3)=2^n\bigl(2^n+2(-1)^n\bigr).}
\]
For \(a\ne2\), the two local extension weights differ. The minimum number of colors is three for these graphs, but that numerical chromatic fact is not part of the novelty assertion.

## Assumptions and scope
All graphs are finite, simple, undirected; indices on the core cycle are modulo \(n\). Pendant leaves are distinguished, as are the \(q\) colors, and the PCF condition refers to **open**, not closed, neighborhoods. The expression is proved for all integer parameters \(n\ge3\), \(a\ge1\), \(q\ge3\); its polynomial interpretation extends uniquely to the counting polynomial. No surjectivity of the palette is required. In particular, an ordinary proper coloring with all distinct colors always satisfies PCF, but proper colorings in general need not.

## Proof
**1. Two local extension weights.** Fix a proper coloring \(c_0,\ldots,c_{n-1}\) of the core. Each leaf at \(v_i\) has \(q-1\) available colors, all different from \(c_i\); every leaf already has its unique core neighbor, so the PCF constraint is automatic at leaves. At \(v_i\), the \(a+2\) neighbors consist of the two core neighbors and the \(a\) leaves. Since \(c_{i-1}\ne c_i\ne c_{i+1}\), the two neighboring core colors lie among the \(q-1\) allowable leaf colors. There are two cases.

If \(c_{i-1}=c_{i+1}\), one color has a preexisting multiplicity of two and all other \(q-2\) available colors have multiplicity zero. For the neighborhood to have **no** singleton, the first color can occur an arbitrary number of additional times, whereas every other color must occur zero or at least twice. Exponential generating functions for these choices are \(e^z\) and \(e^z-z\), respectively. Multiplying and extracting \(a![z^a]\) gives exactly the number of forbidden assignments, so the valid number is \(r_a(q)\).

If \(c_{i-1}\ne c_{i+1}\), each of two specified colors begins with multiplicity one, hence must occur at least once among the leaves to avoid being a singleton; the remaining \(q-3\) colors must occur either zero or at least twice. The forbidden-assignment exponential generating function is \((e^z-1)^2(e^z-z)^{q-3}\), yielding \(s_a(q)\). All leaf clusters are disjoint, so their choices multiply. Thus
\[
F_{n,a}(q)=\sum_{\substack{c_0,\ldots,c_{n-1}\in[q]\\c_i\ne c_{i+1}\ (\mathrm{mod}\ n)}}\ \prod_{i=0}^{n-1}\begin{cases}
r_a(q),&c_{i-1}=c_{i+1},\\
s_a(q),&c_{i-1}\ne c_{i+1}.
\end{cases}
\tag{1}
\]
Every coloring is counted exactly once through its restriction to the core and its independently chosen labeled leaf colors.

**2. Closed-walk transfer.** Index matrix coordinates by ordered pairs \((u,v)\in[q]^2\) with \(u\ne v\). Put
\[
T_{(u,v),(v,w)}=\begin{cases}r,&w=u,\\s,&w\ne u,v,\end{cases}
\]
with all other entries zero. A closed walk of length \(n\) specifies a unique indexed proper cyclic core-color sequence, including the permitted reversal at a vertex. Consequently, equation (1) is \(F_{n,a}(q)=\operatorname{tr}(T^n)\).

**3. Four invariant spectral families.** Regard the vector space as the set of functions \(f(u,v)\) on ordered distinct-color pairs. With \(h=r+(q-2)s\),
\[
(Tf)(u,v)=s\sum_{w\ne v}f(v,w)+(r-s)f(v,u).
\tag{2}
\]
Constant functions form an invariant one-dimensional subspace with eigenvalue \(h\). For each \(x\in\mathbb C^q\) with \(\sum_u x_u=0\), functions \(f(u,v)=\alpha x_u+\beta x_v\) form a two-dimensional invariant block, with coefficient matrix
\[
\begin{pmatrix}0&r-s\\h&-s\end{pmatrix}.
\]
It has characteristic polynomial \(\lambda^2+s\lambda+(s-r)h\) and \(q-1\) copies. Write its two eigenvalues formally as \(\lambda_+\), \(\lambda_-\); then \(U_j=\lambda_+^j+\lambda_-^j\), including when the roots coincide, by the stated recurrence.

The remaining subspace consists of functions with zero sums in every row and column. On it the first term in (2) vanishes and transposition \(f(u,v)\mapsto f(v,u)\) acts as \(+1\) on the symmetric subspace and \(-1\) on the antisymmetric subspace. Their dimensions are \(q(q-3)/2\) and \((q-1)(q-2)/2\), respectively: symmetric off-diagonal arrays have \(q(q-1)/2\) entries and \(q\) independent zero-row-sum conditions, while antisymmetric arrays have \(q-1\) independent such conditions. Their eigenvalues are \(r-s\) and \(s-r\). The constant, standard, symmetric and antisymmetric dimensions sum to \(q(q-1)\), giving a direct-sum decomposition for every integer \(q\ge3\). Summing \(n\)-th powers of these eigenvalues proves the boxed formula.

**4. Polynomial and three-color consequences.** For fixed \(n,a\), each permissible equality partition of the \(n(a+1)\) vertices contributes a falling factorial in \(q\); hence the coloring count is a polynomial. The coefficient formulas for \(r_a,s_a\) likewise reduce by binomial expansion to finite polynomials for fixed \(a\). Since the two polynomials agree on all integers \(q\ge3\), the formula is the counting polynomial. For \(q=3\), only two leaf colors remain. If the two core-neighbor colors agree, exactly one leaf must carry the other color: \(r_a(3)=a\). If they disagree, PCF holds exactly when all leaves use one or the other neighbor color: \(s_a(3)=2\). Therefore the local extension count is independent of the core-neighbor equality relation precisely when \(a=2\), and each core coloring then has \(2^n\) extensions. Every proper two-coloring of a hairy cycle (possible only when \(n\) is even) gives every neighbor of each core vertex the same color, because its leaves and cycle neighbors must all oppose its color. Thus no open neighborhood at a core vertex has a uniquely occurring color. Three colors suffice: every cycle has a proper three-coloring and \(r_a(3)=a>0\), \(s_a(3)=2>0\) ensure that the leaf clusters can be extended. This proves the stated minimum of three but does not claim novelty for it. The ordinary chromatic polynomial of a cycle is \((q-1)^n+(q-1)(-1)^n\); substituting \(q=3\) gives the last boxed identity.

## Verification
Run `python3 verify_sunlet.py` with Python 3 and no third-party packages. `verification_output.txt` records the exact output. The checker compares the local coefficient formula against direct enumeration of pendant assignments for 30 parameter pairs, the spectral recurrence against a separately constructed explicit integer transition matrix for 96 parameter triples, and the direct enumeration of proper core-colorings for 27 parameter triples. It additionally enumerates pendant colors and verifies the PCF condition from scratch for ten small graph/palette instances, encompassing 1,496,305 ambient color assignments before properness filtering. These finite tests corroborate, rather than replace, the proof of the infinite statement.

## Relationship to prior work
Qi, Song and Cao (2026), arXiv:2609.11249, prove degree-dependent **list-colorability** for sparse graphs of large girth; their theorem does not enumerate PCF colorings. This motivates exact distributions in a sparse planar unicyclic family. Caro, Petruševski and Škrekovski (2022), arXiv:2203.01088, Observation 3, already study the PCF **chromatic number** of ordinary coronas, including the one-leaf case; consequently the fact that three colors suffice here is not asserted to be new. Their theorem supplies neither the \(q\)-palette count nor the spectral decomposition or constant-extension identity. Ordinary proper-coloring counts of corona graphs likewise do not encode open-neighborhood uniqueness. Published related results concerning other graph families or different coloring invariants do not directly imply the counting formula. The relevant literature searches found no covering statement, which is not proof of absolute novelty.

## Limitations
This is an exact result for uniform pendant-multiplicity cycle coronas, not arbitrary unicyclic graphs, arbitrary attached trees, or arbitrary list assignments. It counts labeled palette assignments, not color-orbits or equivalence classes of graph automorphisms. No closed-form root classification or asymptotic zero distribution of the resulting polynomials is asserted. A related formula in unindexed literature may exist; only self-review, not independent external verification, has been completed.

## References
1. X. Qi, H. Song, Z. Cao, *Proper conflict-free choosability of sparse graphs with girth at least seven*, arXiv:2609.11249 (first version 2026; version 2 inspected), https://arxiv.org/pdf/2609.11249v2.
2. Y. Caro, M. Petruševski, R. Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088 (2022), https://arxiv.org/pdf/2203.01088.
3. I. Fabrici, B. Lužar, S. Rindošová, R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, arXiv:2202.02570 (2022).
