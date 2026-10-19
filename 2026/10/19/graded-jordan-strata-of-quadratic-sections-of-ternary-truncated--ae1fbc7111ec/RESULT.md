# Graded Jordan strata of quadratic sections of ternary truncated polynomial algebras

## Finding
For every integer \(n\ge3\), finite field \(k=\mathbb F_q\) with \(q=3^f\), \(f\ge1\), and homogeneous quadratic form \(Q\) in
\[
A=k[x_1,\ldots,x_n]/(x_1^3,\ldots,x_n^3),
\]
the **complete graded Jordan type** of multiplication \(D_Q:a\mapsto Qa\) is determined by the rank \(r\in\{0,\ldots,n\}\) of its associated symmetric bilinear form. The operator has degree two and satisfies \(D_Q^3=0\). For \(j=1,2,3\), write \(P_{n,r,j}(z)\) for the polynomial whose coefficient of \(z^d\) is the number of Jordan chains of length \(j\) starting in degree \(d\). Put \(T(z)=1+z+z^2\).

If \(r=0\), the only nonzero polynomial is \(P_{n,0,1}(z)=T(z)^n\). If \(1\le r\le n\), then
\[
\begin{aligned}
P_{n,r,1}(z)&=T(z)^{n-r}2^{r-1}z^r,\\
P_{n,r,2}(z)&=T(z)^{n-r}2^{r-1}z^{r-1},\\
P_{n,r,3}(z)&=T(z)^{n-r}\sum_{h=0}^{r-2}(2z)^hT(z)^{r-2-h},
\end{aligned}
\]
where an empty sum is zero. Thus the Hilbert polynomial of the quotient \(A/(Q)\) is
\[
H_{n,r}(z)=P_{n,r,1}(z)+P_{n,r,2}(z)+P_{n,r,3}(z).
\]
These give exactly \(n+1\) distinct Hilbert series, one for each \(r\). The number of *labeled* quadratic forms producing the series \(H_{n,r}\) is
\[
N_{n,r}(q)={n\brack r}_q S_r(q),
\]
where \({n\brack r}_q\) is the Gaussian binomial coefficient, \(S_0(q)=1\), and for \(m\ge1\)
\[
S_{2m}(q)=q^{m(m+1)}\prod_{i=1}^m(q^{2i-1}-1),
\]
while for \(m\ge0\)
\[
S_{2m+1}(q)=q^{m(m+1)}\prod_{i=1}^{m+1}(q^{2i-1}-1).
\]
In particular, \(\sum_{r=0}^nN_{n,r}(q)=q^{n(n+1)/2}\).

## Assumptions and scope
The field has characteristic exactly three. All quadratic forms are homogeneous of degree two; no claim is made about arbitrary elements of the augmentation ideal, quadratic pencils, or other characteristics. The rank \(r\) is the rank of the symmetric matrix \(B_Q\) determined by \(Q(v)=v^{\mathsf T}B_Qv\), equivalently by \(B_Q(u,v)=(Q(u+v)-Q(u)-Q(v))/2\). A graded Jordan chain \(J_j[d]\) has one generator in degree \(d\), basis in degrees \(d,d+2,\ldots,d+2(j-1)\), and the operator sends each basis element to the next, then to zero. The coefficients of \(P_{n,r,j}\) enumerate such starting degrees, not dimensions of graded pieces directly. All Gaussian and ordinary powers in the formulas are integer operations; the Hilbert coefficients are integers.

## Proof
**1. Coordinate reduction.** Ordinary congruence diagonalizes a quadratic form over any field of odd characteristic. Every invertible linear change \(x_i\mapsto\sum_j a_{ij}x_j\) induces a graded automorphism of \(A\), because in characteristic three its cube equals \(\sum_j a_{ij}^3x_j^3=0\); the inverse change does likewise. Thus the operator for a rank-\(r\) quadratic form is graded-conjugate to multiplication by \(\sum_{i=1}^r c_ix_i^2\), with \(c_i\ne0\), and is zero on the remaining \(n-r\) variables. The one-variable space \(k[x_i]/(x_i^3)\), under multiplication by \(c_ix_i^2\), is the graded sum \(J_2[0]\oplus J_1[1]\): the chain \(1\mapsto c_ix_i^2\) has length two and \(x_i\) spans a trivial length-one chain. This isomorphism does not require a square root of \(c_i\). The tensor-product operator is the sum of the operators on individual factors, by distributivity of multiplication.

**2. Graded tensor identities.** If \(t\) acts on a tensor product by \(t\otimes1+1\otimes t\), direct bases give
\[
\begin{aligned}
J_1[d]\otimes J_2[0]&\cong J_2[d],\\
J_2[d]\otimes J_2[0]&\cong J_3[d]\oplus J_1[d+2],\\
J_3[d]\otimes J_2[0]&\cong J_3[d]\oplus J_3[d+2].
\end{aligned}
\]
To verify the middle identity, write the two length-two bases as \(u_0,u_1\) and \(v_0,v_1\). The vector \(u_0v_0\) generates a length-three chain because its second image is \(2u_1v_1\ne0\); the independent vector \(u_1v_0-u_0v_1\), of degree two above the first generator, is killed by \(t\). For the last identity, use the length-three basis \(u_0,u_1,u_2\) and the length-two basis \(v_0,v_1\). The generators \(u_0v_0\) and \(u_1v_0-u_0v_1\) give two independent length-three chains starting in degrees \(d\) and \(d+2\); their images fill the six-dimensional tensor product. Here \(3=0\) and \(2\ne0\) are essential. Tensoring with \(J_1[1]\) simply shifts starting degrees by one.

**3. Solve the graded recurrence.** For the first \(r\) active variables, let \(U_{r,j}(z)\) be their starting-degree polynomials. One factor gives \(U_{1,1}=z\), \(U_{1,2}=1\), \(U_{1,3}=0\). Multiplying by \(J_2[0]\oplus J_1[1]\) and applying the identities yields
\[
\begin{aligned}
U_{r+1,1}&=zU_{r,1}+z^2U_{r,2},\\
U_{r+1,2}&=U_{r,1}+zU_{r,2},\\
U_{r+1,3}&=U_{r,2}+(1+z+z^2)U_{r,3}.
\end{aligned}
\]
Induction gives \(U_{r,1}=2^{r-1}z^r\) and \(U_{r,2}=2^{r-1}z^{r-1}\), followed by
\[
U_{r,3}=\sum_{h=0}^{r-2}(2z)^hT(z)^{r-2-h}.
\]
Each of the \(n-r\) remaining variables has zero multiplication and graded basis degrees zero, one and two, so its tensor factor multiplies each starting polynomial by \(T(z)\). This proves the three displayed formulas. A length-\(j\) chain contributes exactly its starting generator to the quotient by the image of \(D_Q\); therefore \(H_{n,r}=\sum_jP_{n,r,j}\).

**4. Distinctness.** The quotient length is \(3^n\) at rank zero. At positive rank it is
\[
H_{n,r}(1)=3^{n-1}+3^{n-r}2^{r-1}.
\]
The second summand strictly decreases when \(r\) increases, so the \(n+1\) Hilbert polynomials are distinct. Every rank occurs, e.g. with \(Q=\sum_{i=1}^r x_i^2\).

**5. Finite-field multiplicities.** A rank-\(r\) symmetric bilinear form on \(k^n\) is specified by its radical (\({n\brack r}_q\) choices) and a nonsingular symmetric form on the \(r\)-dimensional quotient. In odd characteristic the latter have two congruence types. Using the standard finite orthogonal-group orders in the congruence orbit-stabilizer formula gives \(S_{2m}\) and \(S_{2m+1}\) exactly as above. For example, the two orders in even dimension are \(2q^{m(m-1)}(q^m\mp1)\prod_{i=1}^{m-1}(q^{2i}-1)\), while the odd-dimensional order is \(2q^{m^2}\prod_{i=1}^{m}(q^{2i}-1)\). This yields the stated product formulas after cancellation with \(|\operatorname{GL}_r(k)|\). The rank strata partition the \(q^{n(n+1)/2}\) coefficient choices.

## Verification
The standalone `verify.py` performs an independent degree-by-degree multiplication-matrix calculation, rather than repeating the tensor recurrence to compute the observed ranks. It enumerates all \(3^6=729\) ternary quadratic forms in three variables and checks every graded chain-start multiplicity, with symmetric ranks distributed as \(1,26,234,468\) for \(r=0,1,2,3\). It additionally checks random full polynomials in three variables over \(\mathbb F_9\) and in four or five variables over \(\mathbb F_3\), and verifies the global rank-frequency identity for several dimensions and field sizes. Running `python3 verify.py` yields `VERIFY_OK`. These finite checks corroborate but do not substitute for the arbitrary-\(n\), arbitrary-\(f\) proof.

At \(n=3\), the four respective quotient Hilbert polynomials have coefficient vectors \((1,3,6,7,6,3,1)\), \((1,3,5,5,3,1)\), \((1,3,5,4,2)\), and \((1,3,5,4)\), with leading trailing zeros omitted.

## Relationship to prior work
Carlson, Friedlander and Pevtsova (2007), Appendix 10, give *ungraded* tensor product multiplicities for modules over \(k[t]/(t^p)\), with the primitive coproduct. These cover the underlying ungraded block arithmetic used here; they do **not** state the degree-start polynomials or the complete rank-stratified quadratic Hilbert-series distribution. Their 2011 work treats restrictions of elementary abelian-group modules to subalgebras generated by linear nilpotents; the present operator is homogeneous quadratic. Lundqvist and Nicklasson (first publicly posted 2016) classify Lefschetz properties of monomial complete intersections for multiplication by linear forms and their powers, not the full family of quadratic-form sections considered here. Classical finite-field quadratic-form counts provide the multiplicity factors, which are not claimed as new. The present contribution is the explicit *graded* synthesis and classification at every rank, together with exact frequencies.

## Limitations
No claim is made for general elements of positive degree, higher-degree forms, other characteristics, or multiple quadratic relations. The starting-degree formulas refine the ungraded tensor decomposition, but their proof uses familiar finite-dimensional module theory, so an unlocated graded tensor theorem or specialized Hilbert-function result could imply them. Finite-field experiments do not establish mathematical originality; an independent scholarly audit has not been conducted.

## References
1. J. F. Carlson, E. M. Friedlander and J. Pevtsova, *Modules of constant Jordan type*, arXiv:0707.3845 (first posted 25 July 2007), especially Appendix 10, Corollary 10.2. https://arxiv.org/abs/0707.3845
2. J. F. Carlson, E. M. Friedlander and J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474 (first posted 22 June 2011), especially the introduction and Sections 1–3. https://arxiv.org/abs/1106.4474
3. S. Lundqvist and L. Nicklasson, *On the structure of monomial complete intersections in positive characteristic*, arXiv:1604.06820 (first posted 22 April 2016), especially Sections 1–2. https://arxiv.org/abs/1604.06820
4. D. Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979 (first posted 21 November 2011). https://arxiv.org/abs/1111.4979
