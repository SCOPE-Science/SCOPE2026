# Square-zero derivation rank spectra of quadratic-jet algebras

## Finding

Fix a prime power \(q\), an integer \(d\ge2\), and the commutative local algebra
\[
A_{d,q}=\mathbb F_q[x_1,\ldots,x_d]/(x_1,\ldots,x_d)^3.
\]
A *square-zero derivation* means an ordinary \(\mathbb F_q\)-linear Leibniz derivation \(D:A_{d,q}\to A_{d,q}\) satisfying \(D\circ D=0\). Here “square-zero” refers to the **operator**, not to elements on which a map obeys a special identity. Write
\[
\mathcal F_{d,q}(T)=\sum_{\substack{D\in\operatorname{Der}_{\mathbb F_q}(A_{d,q})\\D^2=0}}T^{\operatorname{rank}D},\qquad N=\binom{d+1}{2}.
\]
For integers \(a,b,k\ge0\), put
\[
R_{a,b,k}(q)={a\brack k}_q{b\brack k}_q\prod_{j=0}^{k-1}(q^k-q^j),
\]
with \(R_{a,b,k}=0\) for \(k>\min(a,b)\), and with empty products equal to \(1\). Thus \(R_{a,b,k}(q)\) is the number of \(a\)-by-\(b\) matrices over \(\mathbb F_q\) of rank \(k\).

**Theorem.** When \(q\) is odd,
\[
\boxed{\mathcal F_{d,q}(T)=\sum_{k=0}^{d}R_{N,d,k}(q)T^k.}
\]
When \(q\) is even, for every \(0\le r\le\lfloor d/2\rfloor\) define
\[
t_r=d-2r,\quad h_r=r(d-r),\quad s_r=r+\binom{t_r+1}{2},\quad
C_{d,r}(q)={d\brack r}_q{d-r\brack r}_q\prod_{j=0}^{r-1}(q^r-q^j).
\]
Then the *complete* operator-rank distribution is
\[
\boxed{\mathcal F_{d,q}(T)=
\sum_{r=0}^{\lfloor d/2\rfloor}
C_{d,r}(q)\,q^{d h_r+r s_r}\,T^{r+h_r}
\sum_{k=0}^{t_r}R_{s_r,t_r,k}(q)T^k.}
\]
There are no additional strata. In particular the largest occurring rank is \(d\) for odd \(q\), and is
\[
\boxed{\left\lfloor\frac{(d+1)^2}{4}\right\rfloor}
\]
for even \(q\). Consequently, already at \(d=3\), characteristic two permits a square-zero derivation of rank \(4\), while odd characteristic permits no rank above \(3\). All displayed ranks occur, over every stated field including extension fields.

For \(d=2\), the spectra are \(\mathcal F_{2,2}(T)=1+21T+66T^2\) and \(\mathcal F_{2,3}(T)=1+104T+624T^2\). For \(d=3,q=2\), the spectrum is
\[
1+441T+27342T^2+239736T^3+16128T^4.
\]
Each square-zero operator gives a differential vector space on the underlying vector space; its homology dimension is \(\dim A_{d,q}-2\operatorname{rank}D\), so the same polynomial also determines the complete homology-dimension distribution.

## Assumptions and scope

The ring is commutative, unital, and defined by *all* monomials of total degree at least three, not by separate relations \(x_i^3=0\). The integer \(d\) must be at least two. A derivation is ungraded: its Leibniz rule has no Koszul sign. Every characteristic and every finite-field extension is included. The maximal ideal \(\mathfrak m\) has vector-space decomposition \(\mathfrak m=V\oplus W\), where \(V=\operatorname{span}(x_i)\) and \(W=\operatorname{Sym}^2(V)\) have dimensions \(d\) and \(N\) respectively. The unit is always killed by a derivation and never contributes to its rank.

## Proof

**(1) All derivations have the required two-block form.** First, the constant part of each \(D(x_j)\) vanishes. Indeed choose \(i\ne j\), differentiate the defining relation \(x_i^2x_j=0\), and project the result to the quadratic homogeneous component. The coefficient of \(x_i^2\) there is precisely the constant coefficient of \(D(x_j)\); the remaining term is a multiple of the distinct monomial \(x_ix_j\). This argument works even in characteristics two and three. Conversely arbitrary choices
\[
D(x_j)=\sum_iP_{ij}x_i+\sum_{i\le k}Q_{(i,k),j}x_ix_k
\]
extend uniquely to a derivation, because the derivative of every cubic relation again has degree at least three. Relative to \(V\oplus W\), its matrix is
\[
D=\begin{pmatrix}P&0\\Q&S(P)\end{pmatrix},
\qquad S(P)(uv)=(Pu)v+u(Pv).
\]
The matrix \(Q\) is unrestricted before imposing \(D^2=0\).

**(2) Odd characteristic.** For every generator, the Leibniz identity gives
\[
D^2(x_j^2)=2D(x_j)^2+2x_jD^2(x_j).
\]
If \(D^2=0\) and the characteristic is odd, the degree-two component forces \((Px_j)^2=0\) in \(\operatorname{Sym}^2V\). The symmetric square of a nonzero linear form is nonzero over any field, so \(P=0\). Then \(S(P)=0\) and \(D^2=0\) automatically for every \(Q:V\to W\). The standard finite-field matrix-rank count proves the first formula, including all ranks from zero through \(d\).

**(3) Characteristic two and the induced complex.** Here the square of any ordinary derivation is again a derivation. Hence \(D^2=0\) is equivalent to its vanishing on generators, or equivalently to
\[
P^2=0,\qquad S(P)Q+QP=0.
\]
(The identity \(S(P)^2=0\) follows from \(P^2=0\), because in characteristic two \(S(P)^2(uv)=(P^2u)v+u(P^2v)\).) Suppose \(P\) has rank \(r\). Since \(P^2=0\), it has \(r\) size-two nilpotent blocks and \(t=d-2r\) zero blocks. Choosing its image, kernel, and the induced isomorphism from \(V/\ker P\) to \(\operatorname{im}P\) proves that the exact number of such \(P\) is \(C_{d,r}(q)\).

Choose generators \(a_i,b_i\) for the size-two blocks, satisfying \(Pb_i=a_i\), \(Pa_i=0\), and generators \(c_j\) for the zero blocks. On \(W=\operatorname{Sym}^2V\), the differential \(S(P)\) is the direct sum of: a three-space \(\langle a_i^2,a_ib_i,b_i^2\rangle\) of differential rank one for each \(i\); a four-space of rank two for each pair of distinct size-two blocks; a two-space of rank one for each block/singleton pair; and a zero-differential space of dimension \(\binom{t+1}{2}\) for the singleton products. These spaces use disjoint quadratic monomial bases. Thus
\[
\operatorname{rank}S(P)=r+2\binom r2+rt=h_r=r(d-r),
\]
and \(W\), viewed as a complex with differential \(S(P)\), has exactly \(h_r\) indecomposable size-two blocks and \(s_r=r+\binom{t_r+1}{2}\) singleton blocks. In particular \(s_r\ge t_r\).

**(4) Counting compatible quadratic terms and operator ranks.** The equation \(S(P)Q+QP=0\) says that \(Q\) is a chain map between the square-zero complexes \((V,P)\) and \((W,S(P))\). A chain map from a size-two block to another size-two block has two free coefficients; one involving exactly one singleton block has one coefficient; and a singleton-to-singleton map has one coefficient. Therefore the unconstrained non-homology coefficients number
\[
2rh_r+rs_r+t_rh_r=dh_r+rs_r.
\]
The remaining \(s_r t_r\) coefficients give an arbitrary linear map between homology spaces of dimensions \(t_r\) and \(s_r\). Exactly \(R_{s_r,t_r,k}(q)\) such maps have rank \(k\). A direct block elimination, or the quotient by \(\operatorname{im}S(P)\), shows that the full block operator \(D\) then has rank \(r+h_r+k\): its image contains \(\operatorname{im}S(P)\), acquires \(r\) independent components in \(V\), and acquires precisely \(k\) further classes from the map on homology. Hence the number of choices of \(Q\) at this rank is \(q^{dh_r+rs_r}R_{s_r,t_r,k}(q)\). Multiplying by \(C_{d,r}(q)\), then summing over \(r,k\), proves the second formula without omitted cases.

Finally \(s_r\ge t_r\) makes every \(0\le k\le t_r\) attainable, so the greatest rank at fixed \(r\) is \(r+h_r+t_r=(d-r)(r+1)\). Maximizing for integer \(0\le r\le\lfloor d/2\rfloor\) gives \(\lfloor(d+1)^2/4\rfloor\), as claimed.

## Verification

The standalone `verify.py` reconstructs the monomial-basis action \(S(P)\) and the entire derivation matrix independently from the counting formula. It tests the operator identity by matrix squaring, and computes ranks by finite-field elimination. It exhaustively enumerates all candidate coefficient choices at \(d=2\) over \(\mathbb F_2\) and \(\mathbb F_3\), and separately enumerates all compatible quadratic terms for a nonzero canonical \(P\) at \(d=3\) over \(\mathbb F_2\). It checks the induced-complex block ranks at a second canonical type and normalizes the symbolic counts for further dimensions and field sizes. Run `python verify.py` from a directory containing only the supplied file; no third-party package is required. Tests over prime fields do **not** prove the all-extension-field theorem; the proof above does.

## Relationship to prior work

Hoffmann and Kowalski (arXiv:1212.5788, first public version 2012-12-23) study the integration of positive-characteristic nilpotent derivations into Hasse–Schmidt systems, primarily over fields; their criteria motivate studying the square-zero locus but do not enumerate derivations on the nonreduced quadratic-jet ring or give its rank law. Premet (arXiv:1405.2426, first version 2014-05-10) studies regular derivations and invariant-theoretic geometry for a *different* truncated polynomial ring defined by the separate \(p\)-power relations, in odd characteristic. Its theorems do not imply the characteristic-two term or this rank enumeration. Zhou, Wang and Zhang (2009, DOI 10.1080/03081080802443091) use “square-zero derivations” for maps obeying an identity at square-zero **elements**, a different condition. Standard Gaussian counts and square-zero Jordan-block counts provide the explicitly cited ingredients, not the final rank distribution. A related finite-field calculation for \(d=2\) of the **unrestricted** derivation rank distribution does not determine the intersection with \(D^2=0\), and does not address arbitrary \(d\).

## Limitations

This is an exact statement only for ordinary derivations of \(\mathbb F_q[x_1,\ldots,x_d]/\mathfrak m^3\) with \(d\ge2\). It is not a classification of differential graded algebra structures with a signed Leibniz rule, higher-order nilpotent derivations, or jets of greater depth. Its originality rests on targeted source and semantic database comparisons, not on a proof of historical uniqueness. An equivalent enumeration under different language could exist. The finite computations are corroboration only; the characteristic-uniform conclusion is established algebraically. No independent mathematical validation has been performed.

## References

1. D. Hoffmann and P. Kowalski, “Integrating Hasse-Schmidt derivations,” arXiv:1212.5788 (first submitted 2012-12-23), *Journal of Pure and Applied Algebra* 219 (2015), 875–896. https://arxiv.org/abs/1212.5788
2. A. Premet, “Regular derivations of truncated polynomial rings,” arXiv:1405.2426 (first submitted 2014-05-10), *Contemporary Mathematics* 652 (2015), 123–139. https://arxiv.org/abs/1405.2426
3. J. Zhou, D. Wang and Q. Zhang, “Square-zero derivations of matrix algebras over commutative rings,” *Linear and Multilinear Algebra* 58 (2010), 239–243; online 2009-01-02. https://doi.org/10.1080/03081080802443091
4. Standard finite-field counts: Gaussian binomial coefficients, ranks of rectangular matrices, and size-two nilpotent Jordan blocks, proved as needed by elementary image/kernel choices in this note.
