# A node–cusp–tacnode trichotomy for genus-five Howe plane sextics

## Finding

Let \(k\) be algebraically closed of characteristic zero or characteristic \(p\geq7\). Choose \(a,b,c,d,e\in k\) such that \(0,1,a,b,c,d,e\) are pairwise distinct. Define
\[
\phi(T)=T(T-1)(T-a),\quad Q_1(T)=(T-b)(T-c),\quad Q_2(T)=(T-d)(T-e).
\]
Let \(D\subset\mathbf P^2_{[U:V:W]}\) be the cubic image of
\[
\nu:[s:t]\longmapsto[t(s-bt)(s-ct):t(s-dt)(s-et):s(s-t)(s-at)],
\]
write \(H(U,V,W)\) for its irreducible homogeneous cubic equation (unique up to scaling), and define the irreducible plane sextic
\[
C: H(Y^2,Z^2,X^2)=0\quad\text{in}\quad\mathbf P^2_{[Y:Z:X]}.
\]
This is the genus-five Howe plane sextic associated to the two genus-two covers branched at \(\{0,1,a,b,c,\infty\}\) and \(\{0,1,a,d,e,\infty\}\) as in Moriya–Kudo (2023).

The cubic \(D\) has one and only one singularity, which is either an ordinary node or an ordinary cusp. Its location and type determine the **complete analytic singularity basket** of \(C\):

| Singular point of \(D\) | Singularities of \(C\) | Global Tjurina length |
| --- | --- | ---: |
| Node away from \(UVW=0\) | \(5A_1\) | \(5\) |
| Cusp away from \(UVW=0\) | \(A_1+4A_2\) | \(9\) |
| Node on exactly one coordinate axis | \(A_1+2A_3\) | \(7\) |

The point \([0:0:1]\) of \(C\) is always the indicated \(A_1\). The three possibilities are mutually exclusive and exhaustive. For an explicit algebraic criterion, put
\[
W_i(T)=Q_i'(T)\phi(T)-Q_i(T)\phi'(T)\quad (i=1,2).
\]
Then \(D\) is cuspidal exactly when \(\gcd(W_1,W_2)\) has positive degree (equivalently their resultant vanishes). A common zero is necessarily away from the zeros of \(\phi Q_1Q_2\). If the resultant does not vanish, \(D\) is nodal, and the distinction between the first and third rows is whether its node lies on the coordinate triangle.

In particular, the cusp stratum is **nonempty in characteristic zero**. Taking
\[
\phi=T^3-T,\quad Q_1=T^2-15T+20,\quad Q_2=T^2+7T-12,
\]
leads to the quotient cubic
\[
\begin{aligned}
H={}&12U^3+62U^2V+106UV^2+60V^3\\
&-U^2W-18UVW-25V^2W-2UW^2+2VW^2.
\end{aligned}
\]
Its unique singularity is an ordinary cusp at \([-1:1:1]\). The resulting integral sextic \(H(Y^2,Z^2,X^2)=0\) has exactly four \(A_2\) cusps at \([\pm i:\pm1:1]\), with independent sign choices, and one \(A_1\) node at \([0:0:1]\), where \(i^2=-1\).

## Assumptions and scope

All geometric claims are over an algebraically closed field \(k\) of characteristic zero or \(p\geq7\). Every parameter tuple must satisfy the seven-point distinctness condition. The polynomial \(H\) is defined as the cubic *image* relation of \(\nu\), not by a chosen normalization of a resultant; multiplying \(H\) by a nonzero constant does not change any claim. Analytic types \(A_1,A_2,A_3\) refer respectively to completed local equations \(uv\), \(u^2-v^3\), and \(u^2-v^4\), up to invertible formal changes of coordinates. The global Tjurina length is the sum of the local Tjurina dimensions. This result classifies this specified sextic model, not all plane sextic models of the same smooth curve.

## Proof

**1. The rational cubic and its sole singularity.** Homogenized sections \((tQ_1,tQ_2,\phi)\) have degree three and no common zero. They are linearly independent: if \(\alpha Q_1+\beta Q_2+\gamma\phi=0\), the degree-three term forces \(\gamma=0\); the two distinct monic quadratic polynomials then force \(\alpha=\beta=0\). Thus the image is not a line. The map has degree three, hence its image is an irreducible cubic and its generic degree is one. An irreducible rational plane cubic in characteristic not two or three has precisely one singularity, of type node or cusp.

For finite \(T\), in affine chart \(W\ne0\) the parametrization is \((U/W,V/W)=(Q_1/\phi,Q_2/\phi)\). The immersion fails exactly when both derivatives vanish, namely \(W_1=W_2=0\). At a zero of \(\phi\), the two nonzero values \(Q_1,Q_2\) give a simple first-order variation of their ratio; at the zero of one \(Q_i\), its simple zero gives a nonzero first derivative in the corresponding affine chart. Thus \(\nu\) is immersive on the inverse images of coordinate axes. At infinity, the local forms \(tQ_1/t?\) are better read directly from the homogeneous sections: \(U/W\) and \(V/W\) each have a simple zero in the local parameter \(t/s\), proving immersion there. The image point is \([0:0:1]\); it is smooth, with tangent \(U=V\). In particular the unique cubic cusp can only lie in the coordinate torus, and the vanishing resultant exactly detects it. When the parametrization is immersive everywhere the singularity must be nodal; the only other possibility for a rational irreducible cubic is a cusp.

**2. The normalized cover and its genus.** On the open locus where the denominators are nonzero, adjoining square roots of \(Q_1/\phi\) and \(Q_2/\phi\) yields the function field of \(C\). The two square classes are independent: each \(Q_i\) has two distinct simple zeros that do not occur in the divisor of the other ratio. Consequently \(C\) is geometrically integral and its degree-four cover of the normalization of \(D\), namely \(\mathbf P^1\), has Galois group \((\mathbf Z/2)^2\). The branch divisor consists of the two roots of each quadratic, the three roots of \(\phi\), and infinity, eight distinct branch points. At each, tame inertia has order two. Riemann–Hurwitz yields \(2g(C^{\nu})-2=4(-2)+8\cdot2=8\), hence \(g(C^\nu)=5\). An irreducible sextic has arithmetic genus \(10\), so the sum of all local \(\delta\)-invariants is \(5\).

**3. The point over the coordinate vertex.** The image cubic meets \([U:V:W]=[0:0:1]\) in one smooth point, with local equation \(V-U+O((U,V)^2)=0\); the linear coefficients of \(U\) and \(V\) agree since \(Q_1,Q_2\) are monic. The coordinate-square pullback has local equation \(Z^2-Y^2+O((Y,Z)^4)=0\), an ordinary node at \([Y:Z:X]=[0:0:1]\). At all other smooth points of \(D\) on precisely one coordinate axis, the cubic meets that axis transversely, because the relevant numerator or denominator has a simple zero; the simple branch of the squaring map thus pulls back smoothly. There are no additional singularities above the axes or coordinate vertices.

**4. A singularity of the cubic in the coordinate torus.** The squaring map \([Y:Z:X]\mapsto[Y^2:Z^2:X^2]\) is étale of degree four on the torus. Therefore a node of \(D\) produces four nodes of \(C\), and a cusp produces four cusps. Together with step 3, the baskets are \(5A_1\) and \(A_1+4A_2\). The corresponding \(\delta\)-sums are both five, so there can be no further singularities.

**5. A node on one coordinate axis.** Such a node cannot be at a coordinate vertex. Its two preimages under \(\nu\) are distinct simple zeros of the same coordinate section, so both node branches meet the axis *transversely*. Choose formal local coordinates \((u,w)\) with the axis \(w=0\); the node has two smooth branches \(u=\alpha(w)\) and \(u=\beta(w)\), where \(\alpha(0)=\beta(0)=0\) and \(\alpha'(0)\ne\beta'(0)\). At either of the two points in the square-map inverse image, one local coordinate of the square map is invertible and the ramified coordinate is \(w=v^2\), up to formal units and coordinate changes. The pullback branches are \(u=\alpha(v^2)\) and \(u=\beta(v^2)\); they are smooth and have *exactly order two* contact, because the difference begins with the nonzero term \((\alpha'(0)-\beta'(0))v^2\). Therefore each pullback point is an ordinary tacnode \(A_3\), and the two contribute \(2+2\) to \(\delta\). With the central \(A_1\), the basket is \(A_1+2A_3\), exhausting the \(\delta\)-sum.

**6. Tjurina lengths.** In the assumed characteristics, the isolated plane-curve singularities \(A_1,A_2,A_3\) have respective Tjurina numbers \(1,2,3\). Summing over the three baskets gives \(5,9,7\).

**7. Exact nonempty cusp example.** The five branch parameters of the displayed example are \(a=-1\), the two roots of \(Q_1\), and the two roots of \(Q_2\). Quadratic discriminants \(145\) and \(97\) are nonzero; \(\phi,Q_1,Q_2\) are pairwise coprime, so the seven branch parameters are distinct over \(\mathbf C\). Exact polynomial arithmetic gives \(\gcd(W_1,W_2)=T-2\). Substitution yields \(H(Q_1,Q_2,\phi)=0\) and \((U:V:W)=(-1:1:1)\) at \(T=2\). Writing \(U=-1+u\), \(V=1+v\), \(W=1\), the cubic equation becomes
\[
(5u+7v)^2+12u^3+62u^2v+106uv^2+60v^3=0.
\]
Its cubic term on the tangent line \(u=-7t,v=5t\) is \(24t^3\), proving an ordinary cusp. The inverse images of \([-1:1:1]\) are exactly the four points \([\pm i:\pm1:1]\). The central point is a node by step 3 and no others occur by steps 2–4.

## Verification

The standalone standard-library Python script `verify_howe_types.py` verifies the exact characteristic-zero witness: pairwise-coprime branch polynomials, the common Wronskian root, the implicit-cubic identity, the cusp's quadratic and cubic jets, and the nonzero central-node differential. It also checks the Wronskian coprimality for a published nodal example over \(\mathbb F_{31}\) and the nondegenerate quotient node on a coordinate axis in another published example over \(\mathbb F_{31}\). Run `python3 verify_howe_types.py` in the same directory. The expected output is `HOWE_SEXTIC_NODE_CUSP_TACNODE_WRONSKIAN_AND_CUSP_WITNESS_EXACT_PASS`. These are finite exact checks supporting a complete geometric proof; the finite checks alone do not establish the universal result.

## Relationship to prior work

Moriya and Kudo (arXiv:2310.15993v1, first posted 2023-10-24) derive the genus-five Howe sextic in the \((g_1,g_2,r)=(2,2,4)\) situation and prove that it has three or five multiplicity-two points, with five generically. Their Lemma 4.2.4 handles some axis cases by a local normal form with an exponent only bounded below by four. The present statement refines the *analytic type* in every case, identifies the exact Tjurina lengths, gives a resultant criterion for a new four-cusp stratum, and supplies an exact admissible characteristic-zero witness. It does not claim the sextic construction, geometric genus, the multiplicity-two count, or generic five-point count as new. Kudo's sequel arXiv:2401.00760 studies the complementary \((1,1,0)\) Howe construction, not this explicit genus-two-pair sextic. The 2021 generalized-Howe literature provides background on fiber products, not this analytic stratification.

## Limitations

The proof assumes characteristic zero or at least seven; no assertion is made for characteristics two, three, or five. The result concerns a fixed plane sextic realization, not a moduli-invariant set of plane singularities. The cusp witness is proved in characteristic zero; nonemptiness in each positive characteristic is not asserted. The novelty assessment compares available published sources and research records, but cannot establish that no unindexed equivalent result exists. No independent external audit or validation has been performed.

## References

1. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1, first public 2023-10-24, §§3.2, 4.1–4.2. https://arxiv.org/html/2310.15993v1
2. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1, 2024-01-01, introduction and §2. https://arxiv.org/html/2401.00760v1
3. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of genus-3 curves and generalized Howe curves*, arXiv:2108.06936v1, 2021 (background). https://arxiv.org/abs/2108.06936
