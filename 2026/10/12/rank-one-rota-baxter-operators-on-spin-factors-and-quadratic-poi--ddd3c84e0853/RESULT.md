# Rank-one Rota–Baxter operators on spin factors and quadratic-point counts

## Finding

For every field \(K\) with \(\operatorname{char}K\ne2\), every integer \(n\ge2\), and every nondegenerate symmetric bilinear form \(B\) on \(V=K^n\), the nonzero weight-zero Rota–Baxter operators of rank one on the spin-factor Jordan algebra \(J=K1\oplus V\) are precisely
\[
R(b,v)=\phi(v)(a,u),\qquad
c=(a,u),\quad u\ne0,\quad B(u,u)=a^2,
\quad 0\ne\phi\in V^*,\quad \phi(u)=0.
\]
The triples describe the same operator exactly under
\[
(a,u,\phi)\sim(\lambda a,\lambda u,\lambda^{-1}\phi),
\quad\lambda\in K^\times.
\]
Every such operator satisfies \(R(1)=0\) and \(R^2=0\). The locus is a punctured rank-\(n-1\) vector bundle over the nondegenerate projective quadric
\[
Q_B:\ B(u,u)-a^2=0\ \subseteq\ \mathbf P^n_K,
\]
with geometric dimension \(2n-2\).

For \(K=\mathbf F_q\), \(q\) odd, put \(\chi_q(0)=0\) and let \(\chi_q\) be the quadratic character. The exact number of rank-one operators is
\[
\#\mathrm{RB}^{(1)}_0(J)=(q^{n-1}-1)P_{n,q}(B),
\]
where
\[
P_{n,q}(B)=\begin{cases}
\dfrac{q^n-1}{q-1},&n\ \mathrm{even},\\[3pt]
\dfrac{q^n-1}{q-1}+q^{(n-1)/2}\chi_q\!\left((-1)^{(n+3)/2}\det B\right),&n\ \mathrm{odd}.
\end{cases}
\]
Here \(\det B\) means the determinant of a Gram matrix; its quadratic character is basis-independent. For \(n=3\), the counts are \((q^2-1)(q+1)^2\) and \((q^2-1)(q^2+1)\) for the two discriminant types, revealing arithmetic dependence of the rank-one stratum.

## Assumptions and scope

The product is \((a,u)\cdot(b,v)=(ab+B(u,v),av+bu)\) and the operator is \(K\)-linear. The weight-zero Rota–Baxter identity means
\[
R(x)\cdot R(y)=R\bigl(R(x)\cdot y+x\cdot R(y)\bigr)
\qquad\text{for all }x,y\in J.
\]
All ranks refer to rank as a linear endomorphism on the fixed \((n+1)\)-dimensional vector space. The counts are for individual maps, not conjugacy classes. The form \(B\) need not be split, and no algebraic-closedness assumption is made.

## Proof

Let \(R\) have rank one, so \(R(x)=f(x)c\) with \(0\ne f\in J^*\), \(0\ne c\in J\). Its image is a subalgebra by the defining identity, so \(c\cdot c=\lambda c\) for some \(\lambda\in K\). Define \(g(x)=f(c\cdot x)\). Substituting the rank-one expression into the identity gives, for all \(x,y\),
\[
\lambda f(x)f(y)=f(x)g(y)+f(y)g(x).
\]
Choosing \(x\) with \(f(x)=1\) and \(y\in\ker f\) proves \(\ker f\subseteq\ker g\), hence \(g=\mu f\) for a scalar \(\mu\). The identity reduces to \(\lambda=2\mu\).

Write \(c=(a,u)\). If \(u=0\), then \(a\ne0\), and multiplication by \(c\) is multiplication by \(a\). Thus \(\lambda=a\) and \(\mu=a\), which contradict \(\lambda=2\mu\). Therefore \(u\ne0\). Comparing the vector components of \(c^2=\lambda c\) gives \(\lambda=2a\); comparing scalar components yields \(B(u,u)=a^2\). Consequently \(g=af\), or \(f(c\cdot x)=af(x)\) for all \(x\).

Write \(f(b,v)=sb+\phi(v)\). Direct multiplication gives
\[
f(c\cdot(b,v))-af(b,v)=sB(u,v)+b\phi(u).
\]
Thus \(\phi(u)=0\) and \(sB(u,v)=0\) for all \(v\). Since \(u\ne0\) and \(B\) is nondegenerate, \(s=0\); then \(\phi\ne0\) because \(f\ne0\). All the stated conditions are necessary. Conversely, those conditions imply \(c^2=2ac\) and \(f\circ L_c=af\), which make the rank-one identity true for every pair. Also \(R(1)=0\) and \(R^2(b,v)=\phi(v)\phi(u)c=0\).

The tensor description of a nonzero rank-one map is unique up to simultaneous rescaling of its nonzero image generator \(c\) and functional \(f\), giving precisely the displayed equivalence. The quadric \(Q_B\) is smooth because \(B\) and the scalar coefficient \(-1\) are nondegenerate and the characteristic is not two. Its \(K\)-points have \(u\ne0\). For each projective point \([a:u]\), the allowable \(\phi\) form the kernel of the nonzero evaluation map \(\phi\mapsto\phi(u)\), of dimension \(n-1\); removing \(\phi=0\) yields the claimed punctured vector bundle (with the natural twisting induced by the image line).

Over \(\mathbf F_q\), each point of \(Q_B\) therefore gives \(q^{n-1}-1\) distinct nonzero operators. Counting projective zeros of the nondegenerate quadratic form \(B(u,u)-a^2\) in \(n+1\) variables gives \((q^n-1)/(q-1)\) for even \(n\). For odd \(n\), the standard finite-field quadratic Gauss-sum count adds \(q^{(n-1)/2}\chi_q((-1)^{(n+3)/2}\det B)\): the Gram determinant of the enlarged form is \(-\det B\). Multiplication by the fiber size proves the count.

## Verification

The standalone `verify.py` exhaustively represents each rank-one endomorphism exactly once by a projective image generator and a nonzero functional. It checks the defining identity on all pairs of basis elements, independently of the proved criterion, and compares every accepted map with the criterion and the finite-field formula. It returned `VERIFY_OK` for the eight prime-field diagonal-form cases: \(q=3,5,7\) in dimension \(n=2\), \(q=3,5\) for both quadratic types in dimension \(n=3\), and \(q=3,n=4\). The corresponding counts are \(8,24,48,80,128,864,624,1040\). These computations test finite cases; the proof, not enumeration, establishes the all-field theorem.

## Relationship to prior work

Benito, Gubarev, and Pozhidaev study Rota–Baxter operators on quadratic algebras, including bilinear-form Jordan algebras; their general preliminary lemma includes the fact that weight-zero operators with scalar unit image are square-zero. Their detailed bilinear-form results concern principally nonzero weight. Gubarev's earlier study treats weight-zero operators on Jordan algebras of Clifford type and proves global nilpotency bounds; the full text of that particularly close antecedent was unavailable for complete comparison. The present exact rank-one parameterization, projective-quadric fibration, and finite-field count are not established by those known bounds. This claim is restricted to the rank-one stratum and does not supersede classifications of all operators in special dimensions.

## Limitations

This is an explicit description of rank-one operators only; it neither classifies higher-rank operators nor their automorphism-conjugacy classes. The proof assumes characteristic different from two. Its geometric statement concerns the rank-one constructible locus and its bundle structure; no scheme-theoretic assertion about the full operator scheme is made. An equivalent rank-one parameterization in the inaccessible full text of closely related earlier work cannot be ruled out.

## References

1. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037v1 (first posted 22 January 2018), *Mediterranean Journal of Mathematics* 15 (2018), article 189; DOI: 10.1007/s00009-018-1234-5. https://arxiv.org/abs/1801.07037 ; https://doi.org/10.1007/s00009-018-1234-5
2. V. Gubarev, *Rota-Baxter operators of zero weight on simple Jordan algebra of Clifford type*, arXiv:1710.02377v1 (6 October 2017). https://arxiv.org/abs/1710.02377
3. Standard Gauss-sum formula for the zero count of nondegenerate quadratic forms over finite fields; the sign and dimension conventions used here are explicitly stated in the proof.
