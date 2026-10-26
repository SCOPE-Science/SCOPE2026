# Optimal Schmidt-rank conversion by controlled Hermitian involutions

## Finding
Let \(m,n\ge 1\), \(d=\min\{m,n\}\), and let \(0\ne v\in\mathbb C^m\otimes\mathbb C^n\) have Schmidt rank \(p\). For each integer \(1\le q\le d\), the smallest operator Schmidt rank of a **Hermitian involution** \(U\) taking \(v\) to a vector of Schmidt rank \(q\) is
\[
\boxed{\min_{U=U^*=U^{-1},\ \operatorname{SR}(Uv)=q}\operatorname{OSR}(U)
=\left\lceil\max\left\{\frac pq,\frac qp\right\}\right\rceil.}
\]
Moreover, a minimizer can always be chosen as a controlled reflection
\[
U=\sum_{r=1}^{k}P_r\otimes V_r,
\qquad k=\left\lceil\max\left\{\frac pq,\frac qp\right\}\right\rceil,
\]
where the \(P_r\) are pairwise orthogonal projections summing to identity and every \(V_r\) is a self-adjoint permutation unitary in an orthonormal basis extending the second-factor Schmidt basis. In particular, restricting from arbitrary bipartite unitaries to self-adjoint, order-two controlled gates does not increase the minimum operator Schmidt rank needed for any Schmidt-rank transition. No assertion is made that any *prescribed target vector* can be reached at this rank.

## Assumptions and scope
The tensor product is the usual Hilbert tensor product over \(\mathbb C\); dimensions are finite. The Schmidt rank \(\operatorname{SR}(z)\) of a nonzero bipartite vector is the minimum number of nonzero simple tensors expressing it. The operator Schmidt rank \(\operatorname{OSR}(T)\) is the minimum number of elementary operators \(A_j\otimes B_j\) expressing \(T\); equivalently it is the matrix rank of its realignment. A Hermitian involution is an operator satisfying both \(U^*=U\) and \(U^2=I\). A self-adjoint permutation unitary is a permutation of a fixed orthonormal basis whose cycles have length one or two. There are no assumptions on the nonzero Schmidt coefficients of \(v\) beyond positivity in its Schmidt decomposition.

## Proof
**Lower bound.** If \(T=\sum_{j=1}^k A_j\otimes B_j\), then every bipartite vector \(z\) obeys \(\operatorname{SR}(Tz)\le k\operatorname{SR}(z)\), by expanding a shortest Schmidt decomposition. For a Hermitian involution \(U\), both \(q=\operatorname{SR}(Uv)\le kp\) and \(p=\operatorname{SR}(U(Uv))\le kq\) hold. Since \(k\) is integral, \(\operatorname{OSR}(U)\ge\lceil\max\{p/q,q/p\}\rceil\).

Fix a Schmidt decomposition \(v=\sum_{a=1}^p\alpha_a e_a\otimes f_a\), where all \(\alpha_a>0\), and both displayed families are orthonormal. The following constructions use only elementary orthogonal decompositions.

**Case \(q\le p\).** Put \(k=\lceil p/q\rceil\). Partition the \(p\) indices into nonempty sets \(G_1,\ldots,G_k\) such that \(G_1\) has exactly \(q\) members and each later group has at most \(q\) members. Write \(G_r=\{j_{r,1},\ldots,j_{r,s_r}\}\), so \(s_1=q\), and put \(g_a=f_{j_{1,a}}\) for \(1\le a\le q\). On the first factor let \(P_r\) for \(r\ge2\) be the projection onto the span of \(e_{j_{r,a}}\), and let \(P_1=I-\sum_{r=2}^kP_r\). Set \(V_1=I\). For \(r\ge2\), let \(V_r\) swap the pairs \(f_{j_{r,a}}\longleftrightarrow g_a\) for \(1\le a\le s_r\) and fix the orthogonal complement. Those transpositions have pairwise disjoint supports within each \(V_r\), since \(G_r\cap G_1=\varnothing\) and indices in a group are distinct. Consequently all \(V_r\) are Hermitian involutions. The controlled sum \(U=\sum_rP_r\otimes V_r\) satisfies \(U=U^*\) and \(U^2=\sum_rP_r\otimes I=I\), and has \(\operatorname{OSR}(U)\le k\). Its output is
\[
Uv=\sum_{a=1}^{q}\left(\sum_{r:\,a\le s_r}\alpha_{j_{r,a}}e_{j_{r,a}}\right)\otimes g_a.
\]
The first-factor bracketed vectors are nonzero, mutually orthogonal (they have disjoint supports), and the \(g_a\) are orthonormal. Therefore \(\operatorname{SR}(Uv)=q\).

**Case \(p<q\).** Put \(k=\lceil q/p\rceil\). Choose index subsets \(J_1,\ldots,J_k\subseteq\{1,\ldots,p\}\) with \(J_1=\{1,\ldots,p\}\), every other \(J_r\) nonempty, and \(\sum_{r=1}^k|J_r|=q\); for example take full groups until the last, which holds the remaining one through \(p\) indices. Put \(\nu_a=|\{r:a\in J_r\}|\). We require a family of \(q\) orthonormal vectors \(\{u_{r,a}:a\in J_r\}\) in \(\mathbb C^m\) obeying
\[
e_a=\frac{1}{\sqrt{\nu_a}}\sum_{r:\,a\in J_r}u_{r,a}
\qquad(1\le a\le p).
\]
Such a family exists because, on an abstract \(q\)-dimensional space with orthonormal coordinate vectors labelled by pairs \((r,a)\), the \(p\) normalized sums displayed on the right form an orthonormal family (their supports are disjoint as \(a\) varies). An isometry sending that family to \(e_1,\ldots,e_p\) extends to an isometric embedding into \(\mathbb C^m\) as \(m\ge q\); its images of the \(q\) coordinate vectors provide the required \(u_{r,a}\).

On the first factor let \(P_r\) for \(r\ge2\) project onto \(\operatorname{span}\{u_{r,a}:a\in J_r\}\) and set \(P_1=I-\sum_{r=2}^kP_r\). On the second factor choose \(q-p\) additional orthonormal vectors from the orthogonal complement of \(\{f_1,\ldots,f_p\}\), which is possible because \(n\ge q\), and label them \(g_{r,a}\) for \(r\ge2\), \(a\in J_r\). Put \(g_{1,a}=f_a\). Set \(V_1=I\); for each \(r\ge2\), let \(V_r\) swap the pair \(f_a\longleftrightarrow g_{r,a}\) for every \(a\in J_r\) and fix the rest of the second-factor basis. Again the swaps within a single \(V_r\) are disjoint, so \(V_r^*=V_r^{-1}=V_r\). The controlled sum \(U=\sum_rP_r\otimes V_r\) is a Hermitian involution with \(\operatorname{OSR}(U)\le k\). By the defining decomposition of each \(e_a\),
\[
Uv=\sum_{r=1}^k\sum_{a\in J_r}\frac{\alpha_a}{\sqrt{\nu_a}}\,u_{r,a}\otimes g_{r,a}.
\]
Both families \(\{u_{r,a}\}\) and \(\{g_{r,a}\}\) are orthonormal and every coefficient is strictly positive. Thus this is a Schmidt decomposition with exactly \(\sum_r|J_r|=q\) terms.

The cases \(q\le p\) and \(p<q\) exhaust all possibilities. Both constructions attain the lower bound, so their operator Schmidt ranks actually equal \(k\), completing the proof.

## Verification
An independent finite-dimensional consistency calculation is supplied as `check_involutions.py`. Execute `python3 check_involutions.py` in an environment with NumPy installed. It constructs the operators and tests Hermitian symmetry, \(U^2=I\), target Schmidt rank, and realignment rank across every pair \(1\le p,q\le\min\{m,n\}\) for square factors of dimensions one through eight, plus four rectangular factor pairs. It reports `PASS 254 dimensions/ranks; reflection, Schmidt rank, and exact OSR each.` The script is a finite check only. The all-dimensional theorem rests on the two explicit constructions and the rank-product inequality above, not on numerical enumeration.

## Relationship to prior work
Kian and Moslehian (2026), Theorem 2.1, determine the same minimum **over all unitary operators**, without a Hermitian-involution requirement. Their construction of the increasing-rank case uses a separate local unitary alignment. The present result establishes that this alignment can be absorbed into a choice of the controlled projection frame, leaving a single Hermitian involution with an optimal number of controlled sectors. This is not a formal consequence of the unrestricted minimum: adding a self-adjointness constraint can in general change constrained minimization problems. The controlled-unitary structure studied by Cohen and Yu (2013) concerns operator Schmidt rank two and local equivalence; Müller-Hermes and Nechita (2018) classify attainable operator Schmidt ranks of general unitaries. Neither theorem as stated provides the claimed sharp Hermitian-involution state-transition construction.

## Limitations
The theorem prescribes the **Schmidt rank** of the output, not its Schmidt coefficients or its full target vector. The constructed \(V_r\) are permutation reflections relative to a basis extending the input Schmidt basis, but the control projections in the increasing-rank case need not be diagonal in that input Schmidt basis. The statement is finite-dimensional over \(\mathbb C\) (the construction itself also uses real orthogonal frames in Schmidt coordinates). It does not optimize gate count or circuit depth. Historical priority relative to specialized reflection-gate constructions remains a residual risk; literature searches alone cannot establish novelty.

## References
1. M. Kian and M. S. Moslehian, *Operator Schmidt Rank and the Geometry of Schmidt Profiles*, arXiv:2610.09794v1, first posted 2026-10-07, especially Theorem 2.1 and its proof. https://arxiv.org/abs/2610.09794
2. S. M. Cohen and L. Yu, *All unitaries having operator Schmidt rank 2 are controlled unitaries*, Phys. Rev. A 87, 022329 (2013), arXiv:1211.5201. https://doi.org/10.1103/PhysRevA.87.022329
3. A. Müller-Hermes and I. Nechita, *Operator Schmidt ranks of bipartite unitary matrices*, Linear Algebra Appl. 557 (2018), 174–187. https://doi.org/10.1016/j.laa.2018.07.018
