# Right-annihilator dimension spectra of radical-square-zero quiver algebras

## Finding

Let \(Q\) be an arbitrary finite quiver with a nonempty vertex set \(V\) of size \(n\), an arrow multiset \(E\) of size \(m\), and any orientation, with loops and parallel arrows allowed. Let \(q\) be any prime power and let \(A=\mathbb F_q Q/J^2\), where \(J\) is the arrow ideal. For \(a\in A\), define its right annihilator
\[\operatorname{Ann}_r(a)=\{b\in A:ab=0\},\qquad d(a)=\dim_{\mathbb F_q}\operatorname{Ann}_r(a).\]

For \(S\subseteq V\), define
\[m_S=|\{e\in E:\operatorname{tail}(e)\in S\}|,\qquad
r_S(v)=|\{e\in E:\operatorname{tail}(e)\in S,\ \operatorname{head}(e)=v\}|.\]
All arrow multiplicities are counted. The *complete right-annihilator spectrum* is
\[\boxed{\mathcal A_{Q,q}(t):=\sum_{a\in A}t^{d(a)}
=\sum_{S\subseteq V}(q-1)^{n-|S|}q^{m-m_S}t^{m_S}
\prod_{v\in S}(q^{r_S(v)}-1+t)
\prod_{v\notin S}q^{r_S(v)}.}\tag{1}\]
The identity holds for all \(q\), with no restriction on characteristic or on cycles or loops in \(Q\). Consequently, the number of ordered zero-product pairs and the nullity degree are
\[Z_Q=\#\{(a,b)\in A^2:ab=0\}=\mathcal A_{Q,q}(q),\qquad
\operatorname{zp}(A)=\frac{\mathcal A_{Q,q}(q)}{q^{2(n+m)}}.\tag{2}\]
These statements give a natural field-uniform complete distribution of annihilator dimensions; evaluation of this distribution at \(q\) recovers the zero-product probability.

There is a useful refinement for any height-two poset whose comparability graph is a bipartite simple graph \(G\) with parts \(L,R\), with relations \(i<j\) exactly on the edges from \(L\) to \(R\). Put \(v=|V(G)|\) and \(m=|E(G)|\), and for \(S\subseteq V(G)\) let \(e_G(S)\) count edges with both endpoints in \(S\). Then
\[\boxed{Z_G=q^m\sum_{S\subseteq V(G)}q^{|S|+e_G(S)}(q-1)^{v-|S|}.}\tag{3}\]
This is a two-state vertex-subset (lattice-gas) partition function, not a claim that this graph polynomial itself is new.

For the two connected four-vertex height-two posets whose comparability graphs are, respectively, the three-edge star and four-vertex path, the exact difference is
\[\boxed{Z_{\mathrm{star}}-Z_{\mathrm{path}}=q^6(q-1)^3,\qquad
\operatorname{zp}(A_{\mathrm{star}})-\operatorname{zp}(A_{\mathrm{path}})=\frac{(q-1)^3}{q^8}>0.}\tag{4}\]
These algebras have the same dimension \(7\), semisimple quotient \(\mathbb F_q^4\), radical dimension \(3\), and radical square zero. Their zero-product probabilities nevertheless differ over **every** finite field.

The full annihilator spectrum is finer than zero-product probability: reversing all arrows preserves \(Z_Q\), since the opposite algebra exchanges the two factors of a zero product, but need not preserve \(\mathcal A_{Q,q}(t)\). Over \(\mathbb F_2\), the three-edge star oriented outward and the same star oriented inward have, respectively,
\[\begin{aligned}
\mathcal A_{\mathrm{out},2}(t)&=8+24t+24t^2+8t^3+27t^4+27t^5+9t^6+t^7,\\
\mathcal A_{\mathrm{in},2}(t)&=8+8t+36t^2+12t^3+42t^4+6t^5+15t^6+t^7.
\end{aligned}\tag{5}\]
Both evaluate to \(2216\) at \(t=2\), whereas the path evaluates to \(2152\). This establishes a precise boundary between the information retained by the scalar nullity degree and the full one-sided annihilator spectrum.

## Assumptions and scope

An arrow \(e:u\to v\) has canonical image \(a_e\in A\), and \(e_v\) is the length-zero path at vertex \(v\). Multiplication is path concatenation with all paths of length at least two zero; the chosen orientation convention is \(e_u a_e=a_e=a_e e_v\). Thus \(A\) has basis \(\{e_v:v\in V\}\cup\{a_e:e\in E\}\), dimension \(n+m\), and \(J^2=0\). A loop is an arrow with identical tail and head, counted once among arrows, and a parallel arrow is counted separately. A quiver can be disconnected or include isolated vertices. All formulas count **algebra elements in this fixed algebra**, not algebra isomorphism classes or conjugacy classes. The field size \(q\) is always a prime power. The variable \(t\) is an independent formal indeterminate.

## Proof

**1. Multiplication and kernel.** Write arbitrary elements as
\[a=\sum_{v\in V}\lambda_v e_v+\sum_{e\in E}x_e a_e,\qquad
b=\sum_{v\in V}\mu_v e_v+\sum_{e\in E}y_e a_e.\]
Direct path multiplication, including when an arrow is a loop, gives
\[ab=\sum_{v\in V}\lambda_v\mu_v e_v
+\sum_{e:u\to v}(\lambda_u y_e+x_e\mu_v)a_e.\tag{6}\]
Fix \(a\) and put \(S=\{u:\lambda_u=0\}\). For \(u\notin S\), equation \(\lambda_u\mu_u=0\) uniquely forces \(\mu_u=0\); for \(u\in S\) the coordinate \(\mu_u\) is initially free. For every arrow with tail outside \(S\), equation \(\lambda_u y_e+x_e\mu_v=0\) uniquely determines \(y_e\). For every arrow with tail in \(S\), its \(y_e\) is a free coordinate, and the equation becomes \(x_e\mu_{\operatorname{head}(e)}=0\). These \(m_S\) free \(y\)-coordinates are distinct even for loops and repeated arrows.

A vertex \(v\in S\) retains its free \(\mu_v\) if and only if **all** coefficients \(x_e\) on arrows from a vertex of \(S\) into \(v\) vanish. Otherwise \(\mu_v=0\). All these constraints are on disjoint sets of arrow coefficients when indexed by head vertex. Therefore
\[d(a)=m_S+|\{v\in S:\ x_e=0\text{ for every }e\text{ with tail in }S\text{ and head }v\}|.\tag{7}\]
This identity exhibits all free coordinates of the kernel of left multiplication by \(a\); it does not appeal to rank experiments.

**2. Counting.** Once \(S\) is fixed, the nonzero diagonal coordinates contribute \((q-1)^{n-|S|}\). Each of the \(m-m_S\) arrow coefficients with tail outside \(S\) is unrestricted, giving \(q^{m-m_S}\). For a vertex \(v\notin S\), the \(r_S(v)\) arrow coefficients entering it from \(S\) contribute a factor \(q^{r_S(v)}\) and no additional nullity. For a vertex \(v\in S\), of these \(q^{r_S(v)}\) assignments, precisely one (all zero) contributes one free \(\mu_v\) and hence a factor \(t\); the other \(q^{r_S(v)}-1\) assignments contribute no such free coordinate. The \(m_S\) always-free arrow coordinates contribute \(t^{m_S}\). Multiplying these independent factors and summing over all \(S\) proves (1). Since \(\#\operatorname{Ann}_r(a)=q^{d(a)}\), summing over \(a\) proves (2).

As boundary checks, \(\mathcal A_{Q,q}(1)=q^{n+m}\), the coefficient of \(t^0\) is \(q^m(q-1)^n\) (the units), and the coefficient of \(t^{n+m}\) is one (the zero element). Formula (1) satisfies all three directly.

**3. Height-two zero products.** With the vertex partition \(L\sqcup R\), choose the diagonal coordinate of \(a\) on each lower vertex and the diagonal coordinate of \(b\) on each upper vertex. Let \(S\subseteq L\sqcup R\) record exactly where these chosen coordinates vanish. A zero chosen coordinate permits \(q\) choices for the corresponding opposite diagonal coordinate; a nonzero one has \(q-1\) choices and forces the opposite diagonal to zero. Hence diagonal factors total \(q^{|S|}(q-1)^{v-|S|}\). On each edge \(i\to j\), the equation \(\lambda_i y_{ij}+x_{ij}\mu_j=0\) has \(q^2\) solutions if both chosen coordinates vanish and exactly \(q\) otherwise. Since edge variables are separate, the edge factor is \(q^{m+e_G(S)}\). Multiplication and summation yield (3). This proof also permits isolated vertices by assigning them to either part.

**4. Separating star and path.** Apply (3) to the star with edges \(\{(0,1),(0,2),(0,3)\}\), and to the path with edges \(\{(0,2),(1,2),(1,3)\}\). Direct expansion of the \(16\) vertex subsets for each graph gives
\[q^{-3}Z_{\mathrm{star}}=q^7+3q^6+3q^4-20q^3+21q^2-8q+1,\]
\[q^{-3}Z_{\mathrm{path}}=q^7+2q^6+3q^5-19q^3+21q^2-8q+1.\]
Subtracting and factoring yields (4). A standalone checker also certifies this integer polynomial identity without symbolic-algebra libraries: the difference has degree at most \(10\), and it evaluates to the asserted polynomial at eleven distinct integers \(0,1,\ldots,10\). In addition, the same checker verifies (1) by separately computing multiplication matrices over small prime fields.

**5. Opposite-algebra boundary.** Transposing the quiver reverses its arrows and gives the opposite algebra. The bijection \((a,b)\mapsto(b,a)\) preserves the number of zero products under passage to the opposite algebra. For the three-arrow star, (1) at \(q=2\) gives the two distinct polynomials in (5). Both have the same value at \(t=2\), as they must. This is a fully explicit example in which the scalar nullity degree fails to capture the one-sided annihilator dimension distribution.

## Verification

Run `python3 CHECKER.py` from this directory; only the Python standard library is used. The checker builds matrices of left multiplication directly from the canonical multiplication table and computes their finite-field ranks by Gaussian elimination. Independently it evaluates the vertex-subset formula (1). It compares every coefficient for \(37\) small configurations covering loops, parallel arrows, cycles, forks, disjoint and isolated vertices, and the two star orientations, over prime fields of orders \(2\), \(3\), and \(5\). The total number of directly inspected algebra elements is \(26595\). It also checks the zero-product specialization and the star-versus-path identity via its degree bound. `CHECK_OUTPUT.txt` records the execution. Finite enumeration is evidence for implementation and boundary cases, not the proof for all prime powers and quivers; the latter is Steps 1–5.

## Relationship to prior work

The nullity degree of a finite ring and its relation to right annihilators are established notions: Dolžan (2022) treats semisimple rings and general bounds, while Dolžan (2025), Lemma 2.3, states the generic weighted-annihilator sum identity. Neither inspected description furnishes the explicit all-quiver annihilator-dimension generating function (1), which requires the arrow-by-arrow kernel stratification above. Can (2021) studies incidence monoids, their automorphisms and torus complexity rather than zero-product or annihilator-rank distributions. The graph partition function in (3) is a familiar type of lattice-gas expression; its graph-theoretic form is not claimed as novel. The contribution assessed here is the uniform algebraic spectrum (1), its specialization to all zero-product probabilities, and the strict separation examples (4)–(5).

## Limitations

The theorem is about the radical-square-zero quotient, not unrestricted path algebras with paths of length two or more. It does not classify quivers by annihilator spectrum, prove graph reconstruction, or assert a complexity lower bound for evaluating (1). The 2022 Dolžan paper's full text was not available during source comparison, and equivalent formulas in broader quiver-representation or graph-polynomial literature remain possible. All novelty conclusions are provisional pending independent literature audit; no independent mathematical validation is claimed. The positive difference in (4) is exact and holds for every finite field but not for an arbitrary pair of nonisomorphic trees.

## References

1. D. Dolžan, *The Probability of Zero Multiplication in Finite Rings*, Bulletin of the Australian Mathematical Society 106 (2022), 83–88. DOI: 10.1017/S0004972721001246. First verified public online date: 2022-01-24.
2. D. Dolžan, *The Multiplication Probability of a Finite Ring*, arXiv:2504.12886 (2025), especially Lemma 2.3 and Theorem 4.7.
3. M. Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826 (2021), especially Theorems 1.1–1.4 and Section 4.
4. L. Chen and Z. Xiao, *Characterizations of Derivations on Incidence Algebras by Local Actions*, Communications in Algebra 52 (2024), 4380–4387. DOI: 10.1080/00927872.2024.2346302 (contextual zero-product-determined literature, not a counting formula).
