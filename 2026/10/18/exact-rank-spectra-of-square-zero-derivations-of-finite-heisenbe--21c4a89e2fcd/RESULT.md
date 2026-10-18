# Exact rank spectra of square-zero derivations of finite Heisenberg Lie algebras

## Finding

For every prime power \(q\), every integer \(m\ge1\), and the Heisenberg Lie algebra \(H_m=V\oplus\mathbb F_qz\) associated with a nondegenerate alternating form \(\omega\) on a \(2m\)-dimensional vector space \(V\), the following polynomial counts **all** derivations \(D\) satisfying \(D^2=0\) according to their rank on \(H_m\):

\[
\mathcal H_{m,q}(T)=\sum_{r=0}^{m}I_{m,r}(q)S_r(q)
\left(q^rT^r+\bigl(q^{2m-r}-q^r\bigr)T^{r+1}\right),
\qquad
I_{m,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2(m-j)}-1}{q^{r-j}-1}.
\]

Here \(S_r(q)\) is the number of nonsingular symmetric \(r\times r\) matrices over \(\mathbb F_q\), with \(S_0(q)=1\). It has the following characteristic-uniform closed form, valid also when \(q\) is even:

\[
S_r(q)=q^{r(r+1)/2}
\prod_{i=1}^{\lceil r/2\rceil}(1-q^{1-2i}).
\]

For a structural derivation of this same formula in characteristic two, define

\[
G_r(q)=\prod_{i=0}^{r-1}(q^r-q^i),\qquad
P_k(q)=q^{k^2}\prod_{i=1}^k(q^{2i}-1),\qquad P_0(q)=1.
\]

Then, for \(k\ge0\) in the odd-dimensional case and \(k\ge1\) in the even-dimensional case,

\[
S_{2k+1}(q)=\frac{G_{2k+1}(q)}{P_k(q)},\qquad
S_{2k}(q)=\frac{G_{2k}(q)}{P_k(q)}+
\frac{G_{2k}(q)}{q^{2k-1}P_{k-1}(q)}.
\]

Consequently the possible ranks are **exactly** \(0,1,\ldots,m\); no square-zero derivation has rank greater than \(m\), and each listed rank is attained for every \(q\). For fixed \(m\), the proportion of square-zero derivations having rank \(m\) tends to \(1\) as \(q\to\infty\) through prime powers.

In particular,

\[
\mathcal H_{2,2}(T)=1+45T+330T^2,\qquad
\mathcal H_{2,3}(T)=1+320T+8400T^2.
\]

## Assumptions and scope

The field is \(\mathbb F_q\), where \(q\) is any prime power, including characteristic two. The integer \(m\) is arbitrary and positive. The Lie bracket is specified by \([v,w]=\omega(v,w)z\) and \([z,H_m]=0\). An endomorphism \(D:H_m\to H_m\) is a derivation when \(D[x,y]=[Dx,y]+[x,Dy]\) for all \(x,y\). The condition \(D^2=0\) concerns composition as a linear operator, and rank means ordinary \(\mathbb F_q\)-linear rank on the complete \((2m+1)\)-dimensional space. No restriction to inner derivations, nilpotent Lie algebra derivations of index greater than two, or derivation conjugacy classes is imposed.

## Proof

**1. Derivation blocks.** The center equals \(\mathbb F_qz\), so every derivation is uniquely given by a scalar \(\lambda\), a functional \(f\in V^*\), and an operator \(A\in\operatorname{End}(V)\), as

\[
D(v)=Av+f(v)z,\qquad D(z)=\lambda z.
\]

The derivation law is equivalent to

\[
\omega(Av,w)+\omega(v,Aw)=\lambda\omega(v,w)
\quad (v,w\in V).
\]

With a symplectic Gram matrix \(J\), this reads \(A^{\mathsf T}J+JA=\lambda J\). Squaring the triangular block matrix for \(D\) shows

\[
D^2=0\quad\Longleftrightarrow\quad
\lambda=0,\quad A^2=0,\quad fA=0.
\]

Indeed the lower-right block is \(\lambda^2\), forcing \(\lambda=0\) over a field; the remaining two block conditions follow, and conversely suffice.

**2. Symplectic square-zero operators.** Let \(r=\operatorname{rank}A\), \(U=\operatorname{im}A\). The symplectic skew-adjoint identity implies \(\ker A=U^\perp\): for each \(x,y\), \(\omega(Ax,y)=-\omega(x,Ay)\). As \(A^2=0\), \(U\subseteq\ker A=U^\perp\), so \(U\) is totally isotropic and \(0\le r\le m\).

The map \(A\) induces an isomorphism \(V/U^\perp\to U\). Symplectic duality identifies \(V/U^\perp\) with \(U^*\). Under these identifications the identity \(\omega(Ax,y)=-\omega(x,Ay)\) says precisely that the resulting map \(U^*\to U\) is represented by a **symmetric** matrix. Nonsingularity is equivalent to \(\operatorname{rank}A=r\). Conversely, every totally isotropic \(U\) and every nonsingular symmetric form on \(U^*\) produce exactly one such \(A\). Thus the number of \(A\) with rank \(r\) is \(I_{m,r}(q)S_r(q)\); this construction is valid in characteristic two as well.

For completeness, count isotropic ordered \(r\)-frames by successive choices. After an isotropic \(j\)-space has been chosen, the next independent vector in its orthogonal complement has \(q^{2m-j}-q^j\) choices. Dividing the product by the number \(\prod_{j=0}^{r-1}(q^r-q^j)\) of ordered bases of a fixed \(r\)-space gives the displayed formula for \(I_{m,r}(q)\).

**3. Counting nonsingular symmetric matrices.** When \(q\) is odd, congruence classes of nonsingular symmetric forms have the familiar one- or two-discriminant-type orthogonal stabilizers. Summing orbit sizes using the classical finite orthogonal group orders yields \(q^{r(r+1)/2}\prod_{i=1}^{\lceil r/2\rceil}(1-q^{1-2i})\). This formula also holds at \(r=0\) via an empty product.

When \(q\) is even, finite fields are perfect. A nonsingular symmetric bilinear form is alternating or nonalternating, with just one class of each admissible dimension/type. In dimension \(2k+1\), it must be nonalternating. The unique characteristic vector \(w\) with \(b(w,v)=b(v,v)^{1/2}\) has \(b(w,w)=1\); its orthogonal complement is a \(2k\)-dimensional nondegenerate alternating space. Its isometry group therefore has order \(P_k(q)\), giving \(G_{2k+1}(q)/P_k(q)\) congruent Gram matrices.

In dimension \(2k\), the alternating type has isometry group of order \(P_k(q)\). In the nonalternating type, the characteristic vector \(w\) instead has \(b(w,w)=0\). Its isometry group preserves the flag \(\langle w\rangle\subset w^\perp\), acts symplectically on \(w^\perp/\langle w\rangle\) (of dimension \(2k-2\)), and the kernel has \(q^{2k-1}\) elements: \(2k-2\) independent shear coordinates and one remaining scalar coordinate. Its order is therefore \(q^{2k-1}P_{k-1}(q)\). Summing the two congruence-orbit sizes proves the even-dimensional formula. Algebraically the sum equals \(q^{2k}G_{2k}(q)/P_k(q)\), and the odd-dimensional expression equals \(G_{2k+1}(q)/P_k(q)\); simplifying both yields **the same product formula as in odd characteristic**, despite the two distinct even-dimensional congruence types. The classification and characteristic-vector facts can also be checked by diagonalizing a nonalternating form and reducing an alternating form to hyperbolic pairs.

**4. Counting central components and total rank.** For fixed \(A\) of rank \(r\), the equation \(fA=0\) means that \(f\) vanishes on \(U\), giving exactly \(q^{2m-r}\) choices. The rank of \(D\) equals \(r\) exactly if \(f\) vanishes on \(\ker A\), so \(f\) factors through \(V/\ker A\), a space of dimension \(r\). This gives \(q^r\) choices and rank \(r\). The remaining \(q^{2m-r}-q^r\) choices give rank \(r+1\). Summing over \(r\) proves every coefficient of \(\mathcal H_{m,q}(T)\).

When \(r=m\), the two central-function counts coincide, so the coefficient at \(T^{m+1}\) is zero. At each \(0\le r\le m\), the \(q^r\) term is positive and contributes to rank \(r\); hence all those ranks occur and no others do.

**5. Large-field behavior.** For fixed \(m\) and \(r\), \(I_{m,r}(q)S_r(q)q^{2m-r}\) is a polynomial-growth term with leading degree \(m^2+2m-(m-r)^2\) and leading coefficient \(1\) along either characteristic parity. The degree is uniquely maximized at \(r=m\). At that rank, the central functional never increases the operator rank. Thus the proportion at rank \(m\) tends to \(1\) as \(q\to\infty\) through prime powers, irrespective of parity.

## Verification

The accompanying standalone `verify.py` directly constructs symplectic Lie algebra matrices, checks the square-zero condition by direct matrix multiplication, enumerates every allowable central functional, and computes actual derivation-matrix ranks. Exhaustive direct cases are \((m,q)=(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)\), including a genuine non-prime extension field. The program separately enumerates symmetric matrices of orders one, two and three over the four tested fields and verifies their nonsingular counts against the formulas. It also checks the stated dimension-five examples and the dimension-seven polynomial \(1+189T+6930T^2+45360T^3\) over \(\mathbb F_2\). Run `python3 verify.py`; the expected terminal line is `VERIFY_OK_HEISENBERG_SQUARE_ZERO_DERIVATION_RANKS`.

These are finite consistency checks. The quantified all-field assertion is established by the symbolic correspondence and finite-form classification, not by extrapolation from the checked cases.

## Relationship to prior work

Lebedev's *Non-degenerate bilinear forms in characteristic 2, related contact forms, simple Lie algebras and superalgebras* (arXiv:math/0601536, §1.5 and §2) records the relevant symmetric-form congruence classes and Lie-algebra setting. Brouwer, Gow and Sheekey's *Counting Symmetric Nilpotent Matrices* (2014, §2.2, Theorem 2.2) gives the total number of **all nilpotent** elements of the symplectic Lie algebra, without fixing the nilpotency index or recording operator rank. Those structural results are prerequisites or comparators, not claimed here as new. Neither inspected source states the present four-part refinement: the square-zero condition, each rank of the derivation's symplectic quotient, the compatible central functional, and the rank distribution on the full Heisenberg Lie algebra. Prior general nilpotent-orbit methods might also provide alternative derivations of some marginal counts; historical priority is not certified.

## Limitations

The result counts derivations as individual linear transformations, not conjugacy classes. It applies to square-zero derivations of nondegenerate finite Heisenberg Lie algebras, not arbitrary two-step nilpotent Lie algebras. The characteristic-two form-classification and stabilizer-order inputs are necessary for the explicit count. No claim is made that this formula settles broader derivation-enumeration problems or that an independent mathematical audit has occurred. A differently named historical rank-specific calculation remains possible.

## References

1. A. Lebedev, *Non-degenerate bilinear forms in characteristic 2, related contact forms, simple Lie algebras and superalgebras*, arXiv:math/0601536v1 (public 2006-01-22), particularly §§1.5, 2. https://arxiv.org/abs/math/0601536
2. A. E. Brouwer, R. Gow, J. Sheekey, *Counting Symmetric Nilpotent Matrices*, Electronic Journal of Combinatorics 21(2) (2014), P2.4, especially §2.2. DOI:10.37236/3810. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v21i2p4
