# Rota–Baxter trichotomy and exact ternary finite-field counts for rank-one evolution algebras

## Finding
Let \(K\) be a field of characteristic different from \(2\), let \(V\) be a finite-dimensional \(K\)-space, let \(B\) be a nondegenerate symmetric bilinear form, and choose \(0\ne u\in V\). Give \(V\) the commutative (usually nonassociative) multiplication
\[
xy=B(x,y)u.
\]
For every weight \(\lambda\in K\), a linear map \(P:V\to V\) is a Rota–Baxter operator of weight \(\lambda\) **if and only if at least one** of the following conditions holds. The three families are not asserted to be disjoint.

1. **Annihilating isotropic image:** \(P(u)=0\) and \(B(Px,Py)=0\) for every \(x,y\in V\).
2. **Shifted annihilating isotropic image:** \(P(u)=-\lambda u\) and \(B((P+\lambda I)x,(P+\lambda I)y)=0\) for every \(x,y\in V\).
3. **Adjoint-complementary branch:**
\[
P+P^{\dagger}=-\lambda I,\qquad P(P+\lambda I)=0,
\]
where \(P^{\dagger}\) is the adjoint with respect to \(B\).

For \(K=\mathbb F_q\) of odd order and \(\dim V=3\), let \(\mathrm{RB}_{\lambda}(V,B,u)\) be the set of all such operators. Then, **uniformly for every nondegenerate \(B\) and every \(u\ne0\)**,
\[
\boxed{\#\mathrm{RB}_{\lambda}(V,B,u)=
\begin{cases}
q^3+q^2-q,&\lambda=0,\\
2(q^3+q^2-q),&\lambda\ne0.
\end{cases}}
\]
Among the weight-zero operators, the number satisfying \(P^2=0\) (including the zero operator) is
\[
\boxed{\#\{P\in\mathrm{RB}_{0}(V,B,u):P^2=0\}=
\begin{cases}
q^2,&B(u,u)\ne0,\\
2q^2-q,&B(u,u)=0.
\end{cases}}
\]
Thus the total number of operators does not detect whether the square generator is isotropic, but the number of square-zero operators does.

## Assumptions and scope
An evolution algebra is a commutative algebra admitting a natural basis \(e_1,\ldots,e_n\) with \(e_i e_j=0\) for \(i\ne j\). Here the fixed multiplication \(xy=B(x,y)u\) is of that type: because \(\operatorname{char}K\ne2\), the nondegenerate symmetric form has an orthogonal basis; every natural-basis square is nonzero because the diagonal entries of \(B\) are nonzero. In particular, \(\operatorname{Ann}(V)=0\) and \(\dim V^2=1\). The finite-field enumerators require dimension exactly three and \(q\) odd; the structural trichotomy is valid in every positive finite dimension under the stated field and nondegeneracy assumptions.

The weight-\(\lambda\) Rota–Baxter identity is
\[
P(x)P(y)=P\big(P(x)y+xP(y)+\lambda xy\big)
\quad\text{for all }x,y\in V.
\]
``Image totally isotropic'' means \(B(a,b)=0\) for *every* pair of vectors in that image (not merely \(B(a,a)=0\) for selected generators). Counts concern distinct \(K\)-linear maps, not conjugacy classes.

## Proof
**Bilinear reduction and all-weight trichotomy.** Substituting the rank-one product into the Rota–Baxter identity gives, for every \(x,y\),
\[
B(Px,Py)u=
\big(B(Px,y)+B(x,Py)+\lambda B(x,y)\big)P(u). \tag{1}
\]
If \(P(u)=0\), (1) is equivalent to isotropy of the image of \(P\), which is condition 1. Suppose \(P(u)=cu\) for \(c\ne0\). The adjoint identity equivalent to (1) is
\[
P^{\dagger}P=c(P^{\dagger}+P+\lambda I).
\]
Completing the square produces
\[
(P-cI)^{\dagger}(P-cI)=c(c+\lambda)I.
\]
Applying this operator to \(u\), for which \((P-cI)u=0\), gives \(c(c+\lambda)u=0\). Hence \(c=-\lambda\). Substitution shows \((P+\lambda I)^{\dagger}(P+\lambda I)=0\), equivalently condition 2. This case is absent when \(\lambda=0\) and \(c\ne0\).

Finally, if \(P(u)\) and \(u\) are linearly independent, equality (1) forces both scalar bilinear forms to vanish separately. Thus
\[
P^{\dagger}P=0,\qquad P^{\dagger}+P+\lambda I=0.
\]
Combining these equations gives \(P(P+\lambda I)=0\), yielding condition 3. Conversely, condition 3 implies both scalar forms in (1) vanish, while conditions 1 and 2 each imply (1) directly. This proves necessity and sufficiency for every linear map; no invertibility or diagonalizability of \(P\) was assumed.

**Exclusion of the third branch in dimension three.** In characteristic different from two, if \(\lambda=0\), condition 3 makes \(P\) skew-adjoint and \(P^2=0\). The bilinear form \((x,y)\mapsto B(x,Py)\) is alternating, hence its rank equals \(\operatorname{rank}P\) and is even. Since \(P^2=0\) and \(P^{\dagger}=-P\), its image is totally isotropic; in a nondegenerate ternary space a totally isotropic subspace has dimension at most one. Thus \(P=0\), already in condition 1.

If \(\lambda\ne0\), put \(Q=-P/\lambda\). Condition 3 becomes \(Q^2=Q\) and \(Q+Q^{\dagger}=I\). Both \(\operatorname{im}Q\) and \(\ker Q=\operatorname{im}(I-Q)\) are totally isotropic, since \(Q^{\dagger}Q=(I-Q)Q=0\), and similarly for \(I-Q\). They complement one another and cannot both have dimension at most one in dimension three. Therefore the third branch is empty. The remaining two families are disjoint because \(u\ne0\) and \(\lambda\ne0\).

**Isotropic-line count.** Every nondegenerate three-dimensional quadratic space over an odd finite field has precisely \(q+1\) isotropic one-spaces. For completeness, diagonalize \(B\) as \(a x^2+b y^2+c z^2\) with all coefficients nonzero. The sets \(\{ax^2:x\in\mathbb F_q\}\) and \(\{-c-by^2:y\in\mathbb F_q\}\) each have \((q+1)/2\) elements and therefore intersect, producing a nonzero isotropic vector with \(z=1\). Complete an isotropic vector to a hyperbolic pair; the quadratic form becomes \(2xy+d z^2\) for some \(d\ne0\). Its projective zeros consist of one line with \(y=0\) and one line for each of the \(q\) choices of \(z\) after normalizing \(y=1\). The Witt index is consequently one.

For weight zero, each nonzero operator belongs to condition 1 and has rank one. For every isotropic line \(L\), the operators with image exactly \(L\) and \(P(u)=0\) are the nonzero maps \(V/Ku\to L\), of which there are \(q^2-1\). Images determine their lines uniquely, so
\[
\#\mathrm{RB}_{0}=1+(q+1)(q^2-1)=q^3+q^2-q.
\]
For \(\lambda\ne0\), the condition-2 maps are exactly \(P=T-\lambda I\), where \(T\) ranges over the condition-1 maps. The disjoint families therefore double the count.

**Square-zero refinement.** Write a nonzero weight-zero operator as \(P(x)=f(x)v\), with \(v\) spanning an isotropic line \(L\) and \(0\ne f\in V^*\) satisfying \(f(u)=0\). Then \(P^2=f(v)P\). When \(L\ne Ku\), the extra condition \(f(v)=0\) cuts the \(q^2\) allowed functionals down to \(q\); precisely \(q-1\) are nonzero. When \(L=Ku\) (possible exactly when \(B(u,u)=0\)), every allowed functional vanishes on \(L\), giving \(q^2-1\) nonzero square-zero maps. Including zero and summing over the \(q+1\) isotropic lines gives \(q^2\) if \(u\) is anisotropic, or \(2q^2-q\) if \(u\) is isotropic. ∎

## Verification
The standalone Python program `verify.py` uses only the standard library. Its **direct** Rota–Baxter test substitutes every pair of standard basis elements into the original identity; its independent trichotomy test uses image-Gram conditions and the two polynomial/adjoint equations. Exhaustive matrix tests cover seven parameter cases in dimensions two and three over \(\mathbb F_3\) and \(\mathbb F_5\), for weights zero and one. In all dimension-three \(\mathbb F_3\) cases the total is \(33\) at weight zero and \(66\) at nonzero weight, with square-zero counts \(9\) or \(15\) according to the norm of \(u\). Constructive tests over \(\mathbb F_5\) and \(\mathbb F_7\) verify the exact rank-one parametrization, count, and square-zero split. Explicit examples over \(\mathbb F_5\) witness the third branch for weight zero in dimension four and nonzero weight in dimension two.

Run: `python3 verify.py`. Successful execution ends with `VERIFY_OK`. These finite tests are checks of the proof, not an extrapolation from samples to the theorem.

## Relationship to prior work
Qaralleh, Mukhamedov and Khakimov's January 2026 preprint classifies Rota–Baxter operators on **nilpotent** evolution algebras of maximal nilindex, with nonzero superdiagonal structural entries (Theorem 4.5). The present nondegenerate rank-one algebras have zero annihilator and are not in that nilpotent class. Ladra and Murodov (2019, Section 3) give explicit operator families for two-dimensional **complex** evolution algebras, rather than the all-dimensional bilinear trichotomy or the finite-field dimension-three counts above. The October 2026 evolution-algebra survey discusses both one-dimensional-square classifications via bilinear forms and operator-classification problems, but does not supply these Rota–Baxter enumerators. In particular, its Question 39 explicitly asks about perfect evolution algebras; this result concerns nonperfect algebras and is not asserted to solve that question.

The proof uses standard adjoint and orthogonal-space facts, but the combined operator classification and count/refinement are not presented as consequences of a prior listed theorem. Novelty remains contingent on unindexed equivalent literature.

## Limitations
The three structural families can overlap; the result is an exhaustive criterion, not a unique decomposition of each operator. The exact finite-field counts are proved for dimension three and odd characteristic. They do not count conjugacy classes or enumerate all operator ranks in higher dimensions. The argument does not classify Rota–Baxter operators on all evolution algebras, especially perfect ones. Published-source comparison cannot exclude every equivalent result in inaccessible or unindexed material.

## References
1. I. Qaralleh, F. Mukhamedov, and O. Khakimov, *Rota–Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669 (first posted January 13, 2026), especially Theorem 4.5 and Remark 4.6. https://arxiv.org/abs/2601.08669
2. M. Ladra and Sh. N. Murodov, *On chains and Rota–Baxter operators of evolution algebras*, arXiv:1906.09098 (2019), Section 3. https://arxiv.org/abs/1906.09098
3. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first posted October 15, 2026), Sections 1.3.2 and 2.2, Question 39. https://arxiv.org/abs/2610.22248
