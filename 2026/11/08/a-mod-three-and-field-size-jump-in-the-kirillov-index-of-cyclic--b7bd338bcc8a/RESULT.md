# A mod-three and field-size jump in the Kirillov index of cyclic graph Lie algebras

## Finding
Let \(k\) be an arbitrary field, \(n\ge3\), and let \(L_n(k)=\mathfrak n_{C_n}(k)\) be the three-step graph Lie algebra defined by Gallo and Videla. Write \(\operatorname{ind}_kL_n\) for the least dimension of the radical of a Kirillov form \(B_\varphi(x,y)=\varphi([x,y])\), over all \(\varphi\in L_n(k)^*\). Then
\[
\boxed{\operatorname{ind}_k L_n=\begin{cases}n,&3\mid n\text{ and }|k|>2,\\ n+2,&3\nmid n\text{ or }k=\mathbb F_2.\end{cases}}
\]
Thus the central lower bound is attained precisely at cyclic lengths divisible by three over fields other than the two-element field. In particular, at lengths divisible by three the index differs between \(\mathbb F_2\) and \(\mathbb F_4\), even though both fields have characteristic two.

There is also an exact finite-field count. Suppose \(3\mid n\), let \(q\) be a prime power, set \(m=n/3\), \(A=q^m-(q-1)^m\), and \(B=(q-1)^{m-1}\). The number of linear functionals \(\varphi\in L_n(\mathbb F_q)^*\) whose Kirillov radical equals the center (equivalently, whose form has rank \(2n\)) is exactly
\[
\boxed{q^{2n}\bigl[3(q-1)(q-2)AB^2+(q-1)(q-2)(q-3)B^3\bigr].}
\]
For \(3\nmid n\) this count is zero. The displayed count is also zero at \(q=2\).

## Assumptions and scope
The graph \(C_n\) is the undirected simple cycle of length \(n\), with \(C_3=K_3\). The Lie algebra is the specific graph construction in arXiv:2610.33963v1, not the earlier Dani--Mainkar two-step graphical Lie algebra. Its basis consists of vertex vectors, edge vectors, and unoriented two-edge-path vectors; the latter form the center when the cycle has at least three vertices. All fields and all prime powers in the stated ranges are included; no assumption on characteristic, algebraic closure, or infinitude is made. For the counting statement, different linear functionals are counted separately, not modulo automorphisms or coadjoint orbits.

For \(n\ge4\), indices below are in \(\mathbb Z/n\mathbb Z\). Let \(x_i\) be vertex vectors, \(a_i=[x_i,x_{i+1}]\) the oriented edge vectors, and \(w_i\) the central vector of the path \(x_i-x_{i+1}-x_{i+2}\). The defining relations include
\[
[x_i,a_{i+1}]=[a_i,x_{i+2}]=w_i,
\]
with other vertex--edge brackets zero. The vector-space dimension is \(3n\) and \(Z(L_n)=\langle w_i\rangle\) has dimension \(n\). For \(n=3\), use the separate triangle brackets from the same source; they likewise give a nine-dimensional Lie algebra with three-dimensional center.

## Proof
**1. The block criterion.** A functional \(\varphi\) has unrestricted coefficients on the vertex and edge bases and central coefficients \(t_i=\varphi(w_i)\). Relative to \(V\oplus A\oplus W\), its Kirillov matrix has a zero \(W\) part and the noncentral block
\[
K_\varphi=\begin{pmatrix}C_\varphi&D(t)\\-D(t)^{\mathsf T}&0\end{pmatrix},
\]
where \(C_\varphi\) is alternating. Hence \(\operatorname{rank}B_\varphi\le2n\). This rank equals \(2n\) if and only if \(D(t)\) is invertible: if \(D(t)\) is singular, any nonzero vector of \(\ker D(t)\) in the edge component lies in the radical, whereas invertibility of \(D(t)\) makes the full block nonsingular. If \(D(t)\) is always singular, alternation (including in characteristic two) bounds the rank by \(2n-2\). A witness with \(\operatorname{rank}D(t)=n-1\) attains that bound, because its \(2n\)-dimensional alternating block has rank at least twice the rank of \(D(t)\).

**2. The cyclic determinant.** For \(n\ge4\), the source brackets give exactly two nonzero-position contributions for each \(i\):
\[
D(t)_{i,i+1}=t_i,\qquad D(t)_{i+2,i}=-t_i.
\]
Every column has two possible matched rows, separated by three cyclic steps. The bipartite support graph therefore decomposes into \(g=\gcd(n,3)\) even cycles. Within each component, only its two alternating perfect matchings contribute to its determinant; their signed products subtract. If \(g=1\), the products of the two matchings are both \(\prod_i t_i\), so \(\det D(t)=0\) identically. If \(g=3\), set
\[
P_r=\prod_{\substack{0\le i<n\\i\equiv r\ (3)}}t_i\quad (r=0,1,2).
\]
After permuting rows and columns into the three support components, the three determinants are, up to signs, \(P_0-P_1\), \(P_1-P_2\), and \(P_2-P_0\). Consequently
\[
\det D(t)=\pm(P_0-P_1)(P_1-P_2)(P_2-P_0),
\]
so it is nonzero precisely when the three products are pairwise distinct. These determinant identities are polynomial identities with integer coefficients and remain valid after reduction to any characteristic.

For \(n=3\), let the vertex basis be \(x_0,x_1,x_2\), the edge basis \(a_{01},a_{02},a_{12}\), and the path basis \(w_{012},w_{021},w_{102}\). With \(t_0=\varphi(w_{012})\), \(t_1=\varphi(w_{021})\), and \(t_2=\varphi(w_{102})\), the source's triangle brackets show that the only nonzero entries of the mixed matrix, in these orders, are
\[
D_{0,2}=t_0-t_1,\qquad D_{1,1}=t_2-t_1,\qquad D_{2,0}=t_2-t_0.
\]
Thus its determinant is nonzero precisely when \(t_0,t_1,t_2\) are pairwise distinct. This is the preceding three-product criterion with \(m=1\).

**3. Upper and lower rank witnesses.** If \(3\mid n\) and \(|k|>2\), choose any \(u\in k\setminus\{0,1\}\). For \(n\ge6\), take all \(t_i=1\) except \(t_0=0\) and \(t_2=u\); then \((P_0,P_1,P_2)=(0,1,u)\). For \(n=3\), simply choose \((t_0,t_1,t_2)=(0,1,u)\). In either case \(D(t)\) is invertible, and \(\operatorname{rank}B_\varphi=2n\), giving index \(n\).

If \(3\nmid n\), choose all \(t_i=1\). The mixed matrix becomes a difference of two cyclic permutation matrices, so \(\ker D(t)\) consists of vectors constant along steps of three. Since three generates the cyclic index set, the kernel has dimension one over every field. Hence \(\operatorname{rank}D(t)=n-1\).

If \(3\mid n\) and \(k=\mathbb F_2\), the three values \(P_0,P_1,P_2\) cannot be pairwise distinct, so all mixed determinants vanish. For \(n\ge6\), choose \(t_0=0\) and all other \(t_i=1\). Then \((P_0,P_1,P_2)=(0,1,1)\); two support components have invertible matrices, and the remaining component is a cyclic difference-of-permutations matrix of corank one. Thus \(\operatorname{rank}D(t)=n-1\). For \(n=3\), the choice \((0,1,1)\) gives two nonzero mixed diagonal entries, hence rank two. The block criterion now gives maximal Kirillov rank \(2n-2\) in both singular-determinant cases and index \(3n-(2n-2)=n+2\).

**4. Counting central-radical functionals.** For \(n=3m\), each of the three products \(P_r\) depends on a disjoint block of \(m\) central coefficients. Over \(\mathbb F_q\), a specified nonzero product has exactly \(B=(q-1)^{m-1}\) preimages, while zero has \(A=q^m-(q-1)^m\) preimages. Among ordered triples of pairwise distinct products, either exactly one product is zero or all three are nonzero. Their weighted counts are respectively
\[
3(q-1)(q-2)AB^2\quad\text{and}\quad (q-1)(q-2)(q-3)B^3.
\]
The coefficient values of \(\varphi\) on the \(2n\) noncentral basis vectors are arbitrary, supplying a factor \(q^{2n}\). The determinant criterion then proves the counting formula. There are no center-radical functionals when the mixed determinant is identically zero.

## Verification
The file `verify_cycle_index.py` constructs Kirillov matrices directly from the source brackets, performs exact Gaussian elimination over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), and independently enumerates the central coefficients in finite cases. Over \(\mathbb F_4\), arithmetic is implemented in \(\mathbb F_2[z]/(z^2+z+1)\).

The checker verifies 64 explicit maximal-rank witness cases across \(n=3,\ldots,18\) and all four test fields; exhaustively tests 6,419 central coefficient assignments and compares the exact full-rank counts with the formula; and exhaustively tests 12,730 pairs of edge and central coefficient assignments for selected small cases. Its recorded output is `verification_output.txt`. These checks are finite corroboration, not the proof of the arbitrary-field statement.

## Relationship to prior work
Gallo and Videla, arXiv:2610.33963v1 (October 25, 2026), define precisely this three-step Lie algebra, explicitly give the cycle brackets and the dimension and center of the cycle family, and discuss tensor and graph-isomorphism descriptions. Their full preprint does not give the Kirillov index, the support-cycle determinant, or the exact central-radical functional count.

Burde and Dekimpe, arXiv:2505.08331 (first posted May 13, 2025), give an index formula for the **two-step** Dani--Mainkar graph Lie algebra in terms of graph matchings. Their Section 4 applies to a different algebra and does not imply the three-step result here. Previous calculations for three-step paths, stars, subdivided stars, and complete bipartite graphs address other graph families. In particular, \(C_4=K_{2,2}\) is already covered at the index level by the complete-bipartite calculation; the new infinite-cycle theorem does not claim this single specialization as original. Its mod-three and field-size criterion for the other cycles, and its exact full-rank-functional enumerator, are the substantive contributions.

## Limitations
The theorem concerns this specific three-step graph Lie algebra and not arbitrary graphical or cyclic Lie algebras. The finite-field count enumerates linear functionals, not distinct coadjoint orbits. The index over an algebraically closed field does not determine the index over the two-element field: the exception is genuinely field-size sensitive. No novelty assertion is made for the previously covered four-cycle index, and an unindexed equivalent result remains a possible historical-priority risk. The stated proof is a mathematical argument, not an independently audited certification.

## References
1. A. L. Gallo and D. E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, first posted October 25, 2026, especially Sections 2–4. https://arxiv.org/html/2610.33963v1
2. D. Burde and K. Dekimpe, *The index of nilpotent Lie algebras*, arXiv:2505.08331, first posted May 13, 2025, especially Section 4 on two-step graph Lie algebras. https://arxiv.org/abs/2505.08331
