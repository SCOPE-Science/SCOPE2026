# Two leading exponential volume corrections for fixed-label partial permutohedra

## Finding

Let \(n\ge5\) be a **fixed integer** and \(m\ge n\) an integer. Let the partial permutohedron be
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{the nonzero coordinates of }x\text{ are pairwise distinct}\},
\]
and set \(v(m,n)=m!\operatorname{Vol}_{m}(\mathcal P(m,n))\). Define
\[
S=\binom{n+1}{2},\qquad A=\binom n2,\qquad B=\binom{n-1}{2},\qquad C=\binom{n-2}{2}.
\]
Then, as \(m\to\infty\) with \(n\) fixed,
\[
\boxed{v(m,n)=S^{m}-mA^{m}-\binom m2(m-B)B^{m-1}+O_n\!\left(m^{2n-3}C^{m}\right).}
\]
In particular, since \(C<B<A<S\),
\[
\lim_{m\to\infty}\frac{S^m-mA^m-v(m,n)}{\binom m2(m-B)B^{m-1}}=1.
\]
The coefficient \(m-B\) therefore determines the entire second nontrivial exponential volume scale in arbitrary fixed label range \(n\ge5\); the remaining error occurs at the **next** conjectured exponential base. This is an asymptotic theorem, not a closed formula for all \(m,n\).

## Assumptions and scope

All volumes are ambient coordinate Lebesgue volumes in \(\mathbb R^m\), normalized by \(m!\). The label bound \(n\) is fixed, and all implicit constants may depend on \(n\). No bound uniform in growing \(n\) is asserted. The result uses the known facet inequalities for partial permutohedra [1, Proposition 2.8]. In the relevant regime \(m\ge n\), these inequalities give
\[
\mathcal P(m,n)=T\cap\bigcap_{k=1}^{n-1}\bigcap_{\substack{I\subseteq[m]\\ |I|=k}}\left\{x:\sum_{i\in I}x_i\le H_k\right\},
\quad T=\left\{x_i\ge0:\sum_{i=1}^{m}x_i\le S\right\},
\quad H_k=S-\binom{n+1-k}{2}.
\]
In particular \(H_1=n\), \(H_2=2n-1\), and \(H_3=3n-3\). The condition \(m\ge n\) is only to make this a clean complete description; the limit takes \(m\to\infty\).

## Proof

**1. Simplex-tail lemma.** For any fixed \(k\in\{1,\ldots,m\}\), \(I\subseteq[m]\) of cardinality \(k\), and \(0<h<S\), let \(\mathcal E(I,h)=\{x\in T:\sum_{i\in I}x_i>h\}\). Writing \(\mathcal V(E)=m!\operatorname{Vol}_m(E)\), uniform volume in \(T\) has Dirichlet coordinates, including the unused slack coordinate. Therefore \(S^{-1}\sum_{i\in I}x_i\) has beta distribution with shape parameters \((k,m+1-k)\), and
\[
\mathcal V(\mathcal E(I,h))=\sum_{j=0}^{k-1}\binom mj h^{j}(S-h)^{m-j}.\tag{1}
\]
One can also obtain (1) directly by integrating the \((m-k)\)-simplex of remaining coordinates. When \(h\ge S\), the event is null. For fixed \(n\) and \(1\le k\le n-1\), the positive-residual case of (1) is \(O_n(m^{k-1}(S-h)^m)\); its constant is allowed to depend on the fixed positive integer residual \(S-h\).

**2. Single-coordinate truncations.** Let \(D_i=\{x\in T:x_i>n\}\). Translating its \(i\)-th coordinate by \(n\) gives \(\mathcal V(D_i)=A^m\). Similarly \(\mathcal V(D_i\cap D_j)=(S-2n)^m=(B-1)^m\). Bonferroni bounds and the analogous triple-coordinate translation imply
\[
\mathcal V\left(\bigcup_iD_i\right)=mA^m-\binom m2(B-1)^m+O_n\!\left(m^3(C-3)_+^m\right),\tag{2}
\]
where a nonpositive residual gives zero volume. The identity \(S-3n=C-3\) is used here.

**3. Two-coordinate truncations with both coordinate caps imposed.** For \(i<j\), put
\[
E_{ij}=\{x\in T:x_i\le n,\ x_j\le n,\ x_i+x_j>2n-1\}.
\]
Integrating over \(u=x_i+x_j\) and using the cross-section length \(2n-u\) gives the exact normalized volume
\[
\begin{aligned}
\mathcal V(E_{ij})
&=m(m-1)\int_{2n-1}^{2n}(2n-u)(S-u)^{m-2}\,du\\
&=m(m-1)\int_0^1(1-t)(B-t)^{m-2}\,dt\\
&=(m-B)B^{m-1}+(B-1)^m.\tag{3}
\end{aligned}
\]
The integral is valid since \(S\ge2n\) for \(n\ge3\). Its last equality follows by an elementary antiderivative, including the boundary terms; the right-hand side is nonnegative even for small \(m\).

**4. Overlaps are exponentially smaller.** In \(E_{ij}\cap D_\ell\) with \(\ell\notin\{i,j\}\), the sum of the three indicated coordinates exceeds \(3n-1\). In \(E_{ij}\cap E_{i\ell}\), it exceeds \(3n-2\), since the shared coordinate does not exceed \(n\). For two disjoint pairs, the sum of the four indicated coordinates exceeds \(4n-2\). Thus all these events have simplex-tail residual at most
\[
S-(3n-2)=C-1<C.
\]
Equation (1), summing over at most \(O(m^4)\) choices and at most four constrained coordinates, yields
\[
\mathcal V\left[\left(\bigcup_{i<j}E_{ij}\right)\setminus\left(\bigcup_iD_i\right)\right]
=\binom m2\bigl((m-B)B^{m-1}+(B-1)^m\bigr)
+O_n\!\left(m^7(C-1)^m\right).\tag{4}
\]
This follows from the union bounds in both directions: the difference between the sum of individual volumes and the union is bounded by the sum of pairwise intersections, and deleting the coordinate-cap union is bounded by the cap overlaps. No independence assumption is made.

**5. All higher subset inequalities.** For a facet set \(I\) of cardinality \(k\ge3\), the threshold satisfies \(H_k\ge H_3=3n-3\), so \(S-H_k\le C\). Equation (1), followed by a union bound over the \(\binom mk\) subsets for each \(3\le k\le n-1\), gives
\[
\mathcal V\left(\bigcup_{k=3}^{n-1}\ \bigcup_{|I|=k}\mathcal E(I,H_k)\right)
=O_n\!\left(m^{2n-3}C^m\right).\tag{5}
\]
The union of the coordinate-cap events, the pair events outside those caps, and the higher-rank violations is exactly the complement of \(\mathcal P(m,n)\) in \(T\), up to null boundaries. Subtracting (2) and (4) from \(\mathcal V(T)=S^m\), and using (5), makes the two \(\binom m2(B-1)^m\) terms cancel. Since \(n\ge5\) gives \(C\ge3\), the smaller error terms in (2) and (4) are subsumed into (5), proving the boxed expansion.

Finally, the third displayed term has magnitude asymptotic to \(m^3B^{m-1}/2\), whereas the remainder divided by this term tends to zero exponentially because \(C/B<1\). This proves the limiting ratio.

## Verification

The independent finite-geometry checks in `check_two_scale.py` compare the exact one-pair expression (3) with direct numerical quadrature in 66 parameter cases, compute independent convex-hull volumes in 12 low-dimensional cases, and compare them with published exact volumes for \(n=2,3,4\). Each generated vertex also satisfies the facet inequalities. The checker uses a deterministic finite enumeration for the vertex sets. It does not establish the infinite asymptotic bound; the proof above supplies that bound.

A separate check using a convex hull of 326 vertices in dimension five obtains normalized volume \(262410\) for \(\mathcal P(5,5)\), and a six-dimensional hull check obtains \(5295150\) for \(\mathcal P(6,5)\). These are finite consistency tests, not claimed coefficients of an exact general formula.

## Relationship to prior work

Behrend, Castillo, Chavez, Diaz-Lopez, Escobar, Harris and Insko [1] gave the complete inequality description, exact normalized volumes for fixed \(n\le4\), and an open problem for \(n>4\) (Problem 5.14). Their Conjecture 5.15 proposes an exponential-polynomial decomposition whose first bases are \(S\), \(A\), \(B\), and \(C\), but does not establish the arbitrary-fixed-\(n\) expansion above. The present result verifies the first **three** exponential layers, with an error already confined to the fourth base, for every fixed \(n\ge5\). In particular, if the conjectured exact polynomial-layer decomposition exists, its coefficient of \(\binom m2 B^{m-1}\) must be \(m-B\), by exponential separation. This conditional statement does **not** prove the full conjecture.

Heuer and Striker [2] introduced partial permutohedra. Subsequent work on generalized parking-function polytopes [3] gives exact volumes in a different parameter regime, while Liu and Zhang [4] study magic positivity and discuss fixed labels \(n\le3\) in the complementary regime. Neither yields the displayed fixed-label two-correction expansion in \(n\ge5\). Related published results on metric balls and diameter of partial permutohedra concern different invariants and do not imply their normalized volumes.

## Limitations

The result holds with \(n\) fixed and \(m\to\infty\); there is no uniform error in a growing-label regime. The \(O_n\)-constant is not optimized. The exact lower exponential layers at base \(C\) and below, the full Ehrhart polynomial, and the full exact normalized volume for \(n>4\) remain unproved here. Independent mathematical assessment has not been carried out. The novelty comparison is based on inspected primary literature and indexed research, so an unindexed equivalent derivation is a residual risk.

## References

[1] R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial Permutohedra*, arXiv:2207.14253 (first posted 2022-07-28), Proposition 2.8 and Section 5 (especially Problem 5.14 and Conjecture 5.15), https://arxiv.org/abs/2207.14253.

[2] D. Heuer and J. Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, SIAM Journal on Discrete Mathematics 36 (2022), 2863–2888, arXiv:2012.09901, https://arxiv.org/abs/2012.09901.

[3] M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, Annals of Combinatorics 28 (2024), 575–613, arXiv:2212.06885, https://arxiv.org/abs/2212.06885.

[4] F. Liu and Z. Zhang, *Magic Positivity for the Ehrhart Polynomials of Partial Permutohedra*, arXiv:2607.03854 (2026), https://arxiv.org/abs/2607.03854.
