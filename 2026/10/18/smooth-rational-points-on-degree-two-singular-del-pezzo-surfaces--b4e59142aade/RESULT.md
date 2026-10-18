# Smooth rational points on degree-two singular del Pezzo surfaces over \(\mathbf F_4\)

## Finding

**Theorem.** Every geometrically integral singular del Pezzo surface of degree \(2\) over \(\mathbf F_4\) with only rational double point singularities has a smooth \(\mathbf F_4\)-rational point. Combined with the finite-field result of Uppal [1], every such degree-two surface over a finite field \(\mathbf F_q\) has a smooth rational point whenever \(q\ne2\). The restriction is sharp: examples over \(\mathbf F_2\) without smooth rational points are given in [1, §9.5].

The key auxiliary statement concerns *any* geometrically integral separable double-plane model with a quadratic coefficient whose zero conic has only one rational point: such a surface has a smooth rational point outside its ramification divisor over \(\mathbf F_4\).

## Assumptions and scope

A singular del Pezzo surface here is geometrically integral, normal, projective, has ample anticanonical class, and has only rational double point singularities. Degree is \(K_X^2\). Write \(k=\mathbf F_4=\mathbf F_2[\omega]/(\omega^2+\omega+1)\). The anticanonical model in characteristic \(2\) is a double plane in weighted projective space:
\[
 X:\quad W^2+WQ_2(X,Y,Z)+G_4(X,Y,Z)=0\subset\mathbf P(1,1,1,2),
\]
with homogeneous \(Q_2\) and \(G_4\) of degrees \(2\) and \(4\), respectively. For the cases below, \(Q_2\ne0\).

Uppal [1, Theorem 1.2 and §9.3] proves existence over fields of size other than \(2,4\), and reduces the unresolved degree-two case over \(\mathbf F_4\) to geometrically singularity types \(A_2\) and \(A_4\), each having exactly one geometric singular point. Its Proposition 9.5 implies separability of their anticanonical maps, since the minimal resolutions contain respectively \(2\) and \(4\) exceptional \((-2)\)-curves. Thus it suffices to treat geometrically integral models of these two types over \(k\).

## Proof

**1. Branch points.** At each \(P\in\mathbf P^2(k)\) satisfying \(Q_2(P)=0\), the equation \(W^2=G_4(P)\) has a unique solution in \(k\), since squaring is a bijection of \(k\). Hence each rational zero of \(Q_2\) lifts to a rational point of \(X\). An \(A_2\) or \(A_4\) surface has exactly one geometric singular point. If \(Q_2=0\) has two or more rational projective points, one lift is therefore smooth.

**2. The only remaining conic.** A nonzero ternary quadratic form over \(k\) whose projective zero locus has exactly one \(k\)-point is the union of two conjugate nonrational lines meeting in that point. Indeed, a smooth conic has \(5\) rational points, a rational line or double line has at least \(5\), and two distinct rational lines have \(9\). Up to \(k\)-linear coordinates and nonzero scalar multiple, the unique-point case is
\[
Q_2=X^2+XY+\omega Y^2,
\]
with unique rational zero \([0:0:1]\). Set \(Q=Q_2\), and let \(T=\mathbf P^2(k)\setminus\{[0:0:1]\}\), so \(|T|=20\) and \(Q(P)\ne0\) for all \(P\in T\).

**3. A trace-evaluation lemma.** Let \(V_d=k[X,Y,Z]_d\) be the space of homogeneous degree-\(d\) polynomials, viewed as a vector space over \(\mathbf F_2\). Define
\[
 L:V_4\longrightarrow\mathbf F_2^{T},\qquad
 L(G)_P=\operatorname{Tr}_{k/\mathbf F_2}\!\left(\frac{G(P)}{Q(P)^2}\right).
\]
This is well-defined on projective points because numerator and denominator both have degree \(4\). The exact \(20\times30\) binary matrix of \(L\) has rank \(19\). A complete finite-field computation proving this small numerical lemma appears in `verify.py`, using normalized points \((1,y,z)\) for \(y,z\in k\) and \((0,1,z)\) for \(z\in k\), and quartic monomials \(X^iY^jZ^{4-i-j}\) in lexicographic exponent-loop order. The verifier exhibits \(19\) independent columns, and a separate row elimination returns the same rank. The concrete column indices and bit masks are also fixed in that file.

Define the \(\mathbf F_2\)-linear map
\[
 A:V_2\longrightarrow V_4,\qquad A(H)=H^2+QH.
\]
For any \(P\in T\), the quantity \(A(H)(P)/Q(P)^2\) is \(u^2+u\) with \(u=H(P)/Q(P)\), and hence its trace is zero. Thus \(\operatorname{im}A\subseteq\ker L\). In the polynomial domain \(k[X,Y,Z]\), the equation \(H^2+QH=H(H+Q)=0\) forces \(H=0\) or \(H=Q\). Therefore \(\ker A=\{0,Q\}\) has binary dimension \(1\), while \(V_2\) has binary dimension \(12\), so \(\dim_{\mathbf F_2}\operatorname{im}A=11\). Since \(V_4\) has binary dimension \(30\) and \(\operatorname{rank}L=19\), we also have \(\dim\ker L=11\). Consequently,
\[
 \ker L=\{H^2+QH:H\in V_2\}.
\]

**4. Geometric integrality forces a rational unramified point.** Suppose for contradiction that \(X\) has no \(k\)-point above any \(P\in T\). At each such \(P\), the polynomial \(W^2+Q(P)W+G_4(P)\) has no root in \(k\); the Artin--Schreier criterion says precisely
\[
 L(G_4)_P=1.
\]
Because \(\operatorname{Tr}_{k/\mathbf F_2}(\omega)=1\), the quartic \(\omega Q^2\) has that same constant-one evaluation vector. Thus \(L(G_4+\omega Q^2)=0\). By Step 3 there is \(H\in V_2\) with
\[
 G_4=\omega Q^2+H^2+QH.
\]
Choose \(\beta\in\overline{k}\) satisfying \(\beta^2+\beta=\omega\). Then the defining quartic in weighted coordinates factors as
\[
W^2+WQ+G_4=(W+H+\beta Q)(W+H+(\beta+1)Q).
\]
This contradicts geometric integrality of \(X\). Hence some \(P\in T\) has \(L(G_4)_P=0\), and above it lie two \(k\)-rational points. Both are smooth because the partial derivative with respect to the weighted variable \(W\) is \(Q(P)\ne0\).

Steps 1--4 establish a smooth \(k\)-point for both residual \(A_2\) and \(A_4\) types. All other degree-two cases over \(\mathbf F_4\) are covered by [1, §9.3--9.4]. The theorem follows, as does the asserted all-field corollary by combining the \(\mathbf F_4\) case with [1, Theorem 1.2].

## Verification

Run `python3 verify.py` with Python \(3\) and no external packages. It constructs \(\mathbf F_4\) directly, enumerates the \(21\) normalized projective points, checks that \(Q\) has exactly one rational zero, forms all \(30\) binary trace-evaluation columns and certifies rank \(19\) in two elimination orders. It additionally verifies \(19\) explicitly identified independent columns and the defining Artin--Schreier trace identities. See `VERIFICATION.md` for exact computer-assisted and non-computational proof boundaries.

## Relationship to prior work

Uppal [1] proves that a singular degree-two del Pezzo over \(\mathbf F_q\) has a smooth rational point for \(q\notin\{2,4\}\), exhibits counterexamples for \(q=2\), and leaves precisely two singularity types unresolved for \(q=4\). The theorem settles this residual field by a trace-code obstruction to a geometrically integral double cover with no unramified rational point. Tamanoi [2] gives unirationality results for rational-double-point del Pezzo surfaces, including finite-field bounds, but these do not imply the claimed \(\mathbf F_4\) smooth-point existence for the residual types. Blache--Hallouin [3] classify arithmetic types in degrees at least \(3\), not the present degree-two point-existence statement.

## Limitations

The geometric reduction to singularity types \(A_2\) and \(A_4\) and the separability statement are imported from the cited primary literature, rather than reclassified by the finite computation here. The trace-code rank has a finite exact computational certificate and a short standalone verifier; the remaining argument is algebraic. There is no claim that every such surface over \(\mathbf F_2\) has a smooth rational point; counterexamples are known. No claim of unirationality is made. Independent mathematical audit has not been performed.

## References

1. H. Uppal, *Singular del Pezzo surfaces over finite fields*, arXiv:2311.07317v1, first posted 2023-11-13. See Theorem 1.2, Proposition 9.5, §9.3, §9.4, and §9.5. https://arxiv.org/html/2311.07317v1
2. R. Tamanoi, *Unirationality of RDP Del Pezzo surfaces of degree 2*, arXiv:2101.03350v4 (2021), especially Theorem 1.3 and its scope. https://arxiv.org/html/2101.03350v4
3. R. Blache and E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields*, arXiv:2301.13582v1 (2023). https://arxiv.org/abs/2301.13582
