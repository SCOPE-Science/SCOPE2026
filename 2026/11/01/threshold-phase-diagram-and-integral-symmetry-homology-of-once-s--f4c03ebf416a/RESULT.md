# Threshold phase diagram and integral symmetry homology of once-subdivided star independence complexes

## Finding

For integers \(m\geq3\) and \(r\geq2\), let \(T_m\) be the tree with vertices \(c,u_1,\ldots,u_m,v_1,\ldots,v_m\) and precisely the edges \(cu_i\) and \(u_iv_i\) for \(1\leq i\leq m\). Thus every arm from the central vertex \(c\) has exactly two edges. Write \(X_{m,r}=\operatorname{Ind}_r(T_m)\), whose faces are the subsets inducing connected components of at most \(r\) vertices. The group \(S_m\) simultaneously permutes the labels of the \(u_i\)'s and \(v_i\)'s, fixing \(c\).

The **complete homotopy-type phase diagram** is

\[
|X_{m,r}|\simeq
\begin{cases}
\mathrm{pt},&2\leq r\leq m,\\
\displaystyle\bigvee^{\binom{m-1}{r-m-1}}S^{r-1},&m+1\leq r\leq2m,\\
\mathrm{pt},&r\geq2m+1.
\end{cases}
\]

In the noncontractible range put \(q=r-m-1\), so \(0\leq q\leq m-1\), and let

\[
A_m=\ker\bigl(\mathbb Z^{m}\xrightarrow{\,\varepsilon\,}\mathbb Z\bigr),
\qquad\varepsilon(e_i)=1.
\]

Then the **entire integral \(S_m\)-homology representation** is

\[
\widetilde H_{r-1}(X_{m,r};\mathbb Z)
\cong_{\mathbb Z[S_m]}
\operatorname{sgn}_m\otimes_{\mathbb Z}\bigwedge^{q} A_m.
\]

Every other reduced integral homology group vanishes. In the two contractible ranges every reduced integral homology group vanishes. At \(r=2m\) the single top sphere has trivial \(S_m\) action; at \(r=m+1\) the single sphere carries the sign action. All statements are exact over \(\mathbb Z\), not merely rational.

## Assumptions and scope

The tree is finite and simple, all arms have length exactly two, \(m\geq3\), and the threshold is an integer \(r\geq2\). For \(r\geq2m+1\) the complex is a simplex. The action is by **simultaneous** permutations of both levels of the arms, never by independent permutations. Conventions: \(\bigwedge^0 A_m=\mathbb Z\), and a displayed wedge with one summand is a single sphere. The chosen sign character takes a permutation to its parity.

## Proof

**1. The central-vertex link.** Let \(U=\{u_1,\ldots,u_m\}\), \(V=\{v_1,\ldots,v_m\}\), and \(L=\operatorname{lk}_{X_{m,r}}(c)\). As \(r\geq2\), deletion of \(c\) leaves \(m\) disjoint edges, whose entire vertex set is admissible. Therefore \(\operatorname{del}_{X_{m,r}}(c)=\Delta(U\sqcup V)\), a simplex, and

\[
X_{m,r}=\Delta(U\sqcup V)\ \cup_L\ (c*L).
\]

The two pieces are contractible, so the ordinary homotopy-pushout argument gives \(|X_{m,r}|\simeq\Sigma|L|\). Its Mayer–Vietoris homology suspension is natural under the simultaneous \(S_m\) action.

A face \(I\sqcup J\) of \(L\), with \(I\subseteq U\) and \(J\subseteq V\), satisfies exactly

\[
|I|+|\{i:u_i\in I,\ v_i\in J\}|\leq r-1.
\tag{1}
\]

Indeed, the induced component containing \(c\) consists of \(c\), the selected \(u_i\), and those selected \(v_i\) whose \(u_i\) is also selected. Every other selected \(v_i\) is isolated.

**2. A contractible low-support part.** Let \(L^-\subseteq L\) consist of faces missing at least one of the vertices \(u_1,\ldots,u_m\). For each \(i\), the subcomplex \(D_i\) of faces omitting \(u_i\) is a cone with apex \(v_i\) by (1). Every nonempty finite intersection of the \(D_i\)'s is likewise a cone (use any \(v_i\) whose \(u_i\) is omitted). All intersections are nonempty and the nerve of this cover is the full \((m-1)\)-simplex. The simplicial nerve theorem thus makes \(L^-\) contractible.

If \(2\leq r\leq m\), no face can contain all of \(U\), by (1). Hence \(L=L^-\), and \(X_{m,r}\) is contractible. If \(r\geq2m+1\), every subset of the \(2m+1\) vertices is allowable, so \(X_{m,r}\) is again contractible.

**3. The middle-range homotopy type.** Suppose \(m+1\leq r\leq2m\) and put \(q=r-m-1\). Let \(K_q\) be the simplicial complex on \(V\) consisting of subsets of cardinality at most \(q\). Every face of \(L\) either omits some \(u_i\) or contains all of \(U\), so (1) gives

\[
L=L^-\cup\bigl(\Delta(U)*K_q\bigr),\qquad
L^-\cap\bigl(\Delta(U)*K_q\bigr)=\partial\Delta(U)*K_q.
\tag{2}
\]

Since \(L^-\) is contractible and these are inclusions of subcomplexes, collapsing \(L^-\) is a homotopy equivalence. If \(q=0\), equation (2) yields \(L/L^-\cong\Delta(U)/\partial\Delta(U)\cong S^{m-1}\). If \(1\leq q\leq m-1\), the quotient of the contractible join \(\Delta(U)*K_q\) by \(\partial\Delta(U)*K_q\) is homotopy equivalent to

\[
\Sigma\bigl(|\partial\Delta(U)*K_q|\bigr)
\simeq\Sigma^{m}|K_q|.
\]

The \((q-1)\)-skeleton of an \((m-1)\)-simplex is a wedge of \(\binom{m-1}{q}\) copies of \(S^{q-1}\); this follows, for example, by deletion–link induction on \(m\). Thus \(L\) is a wedge of \(\binom{m-1}{q}\) spheres of dimension \(m+q-1\), including the \(q=0\) case. Suspension gives the asserted wedge of spheres in dimension \(m+q=r-1\).

**4. Integral symmetry, not only Betti numbers.** Because \(L^-\) is contractible, the connecting and quotient maps give \(S_m\)-equivariant integral isomorphisms

\[
\widetilde H_{r-1}(X_{m,r};\mathbb Z)
\cong \widetilde H_{r-2}(L;\mathbb Z)
\cong H_{r-2}(L,L^-;\mathbb Z).
\]

Orient every relative face by listing \(u_1,\ldots,u_m\) first, followed by its selected \(v_i\) in increasing index order. Relative chains consist precisely of \(U\sqcup J\) with \(|J|\leq q\). In relative degree \(m+j-1\), they are the free module \(\operatorname{sgn}_m\otimes\bigwedge^{j}\mathbb Z^m\): permutation of the ordered \(U\)-block contributes the sign factor. All boundary terms deleting an element of \(U\) vanish in the relative quotient; the remaining boundary is, up to the global factor \((-1)^m\), contraction with the augmentation functional \(\varepsilon\), namely

\[
\iota_\varepsilon:\bigwedge^{j}\mathbb Z^m\longrightarrow
\bigwedge^{j-1}\mathbb Z^m.
\]

The augmentation sequence \(0\to A_m\to\mathbb Z^m\xrightarrow{\varepsilon}\mathbb Z\to0\) splits over \(\mathbb Z\) as an abelian-group sequence, so this Koszul complex is exact below its truncated top degree \(q\). Its top kernel is canonically \(\bigwedge^{q}A_m\) (with the degree-zero convention above). Consequently the unique nonzero relative homology module is \(\operatorname{sgn}_m\otimes\bigwedge^q A_m\). The claimed integral formula and all homological vanishing follow.

## Verification

The standalone script `check_subdivided_star.py` builds the simplicial chains directly from the induced-component definition, computes reduced mod-two boundary ranks, and independently evaluates signed Lefschetz traces from **all invariant faces** under arm permutations. It checks every threshold \(2\leq r\leq2m+1\) for \(1\leq m\leq5\), including the smaller path boundary cases not used in the theorem. The executed output was: `PASS: 30 independent mod-2 chain homology tests; 1438 signed Lefschetz-character tests.` The character predictions use \(\operatorname{sgn}(\sigma)\) times the coefficient of \(t^q\) in \(\prod_{C\text{ cycle of }\sigma}(1-(-t)^{|C|})/(1+t)\). These finite checks do not replace the all-parameter integral proof above.

## Relationship to prior work

Deshpande and Singh (2020/2021), especially Theorems 3.8 and 3.10, classified the homotopy types for **fully whiskered** connected graphs and for graphs in which **every** nonleaf vertex has an adjacent leaf. They do not cover \(T_m\) for \(m\geq3\): the central vertex is a nonleaf without any leaf neighbor. Adding a leaf at the center makes a fully whiskered star, whose published middle-range multiplicity is \(\binom{m}{r-m-1}\), rather than the present \(\binom{m-1}{r-m-1}\). This compares the exact assertions and hypotheses, not merely graph names.

Abdelmalek et al. (2021/2023) proved vertex decomposability for caterpillar graphs but did not give this calculation. For \(m\geq3\), deleting all leaves from \(T_m\) leaves \(K_{1,m}\), which is not a path, so \(T_m\) is not a caterpillar. Sawant (May 24, 2026) proved vertex decomposability for higher independence complexes of **all** trees, guaranteeing a sphere-wedge existence theorem but not the present threshold, multiplicity, or integral \(S_m\)-module. Related indexed results on the **discrete Morse complex** of a two-edge-arm tree concern a distinct simplicial complex and do not imply the higher-independence statement.

## Limitations

The classification is for equal two-edge arms and all thresholds \(r\geq2\), not for unequal arm lengths, arbitrary trees, or other graph complexes. The homotopy equivalence is nonequivariant; the group representation theorem concerns integral homology and is equivariant. The computational tests are finite, while the proof is for every \(m\geq3\). Independent mathematical validation has not been performed. Equivalent formulations in literature not retrieved by the stated searches remain a possibility.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first publicly posted May 24, 2026. https://arxiv.org/abs/2605.25150
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448v2, Journal of the Ramanujan Mathematical Society 36 (2021), 53–71, Theorems 3.8 and 3.10. https://arxiv.org/abs/2001.05448
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863v3, International Journal of Algebra and Computation 33 (2023), 481–498. https://arxiv.org/abs/2106.10863
