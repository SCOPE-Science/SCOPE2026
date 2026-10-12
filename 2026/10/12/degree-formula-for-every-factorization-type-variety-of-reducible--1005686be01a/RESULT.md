# Degree formula for every factorization-type variety of reducible hypersurfaces
## Finding
Let \(V\) be a complex vector space of dimension \(m\ge3\), let \(d\ge2\), and let
\[
\lambda=(d_1,\ldots,d_r)
\]
be a partition of \(d\) with \(r\ge2\). Write
\[
X_\lambda(V)\subset\mathbb P(\operatorname{Sym}^dV^*)
\]
for the projective variety of degree-\(d\) forms admitting a factorization into factors of degrees
\[
d_1,\ldots,d_r.
\]

Put
\[
N_i=\binom{m+d_i-1}{m-1}-1,
\qquad
D=\sum_{i=1}^r N_i,
\]
and for every positive integer \(e\) put
\[
\mu_e=\#\{i:d_i=e\}.
\]
Then
\[
\boxed{
\deg X_\lambda(V)
=
\frac{D!}
{\left(\prod_{i=1}^r N_i!\right)
 \left(\prod_{e\ge1}\mu_e!\right)}.
}
\]

Consequently, if \(R_{m,d}\) is the full projective locus of reducible degree-\(d\) forms in
\[
\mathbb P(\operatorname{Sym}^dV^*),
\]
then
\[
\boxed{
\deg R_{m,2}
=
\frac12\binom{2m-2}{m-1}
}
\]
and, for \(d\ge3\),
\[
\boxed{
\deg R_{m,d}
=
\binom{\binom{m+d-2}{m-1}+m-2}{m-1}.
}
\]

## Assumptions and scope
The base field is \(\mathbb C\). The restriction \(m\ge3\) is essential for the generic-fiber statement used below: a general positive-degree form in at least three variables is irreducible. Binary forms behave differently because every form splits into linear factors over \(\mathbb C\).

The projective degree is taken with respect to the standard embedding
\[
X_\lambda(V)\subset\mathbb P(\operatorname{Sym}^dV^*).
\]

The full reducible locus \(R_{m,d}\) is generally not equidimensional. Its projective degree means the degree of its top-dimensional cycle, equivalently the leading coefficient of its Hilbert polynomial with the standard normalization.

## Proof
For each part \(d_i\), let
\[
P_i=\mathbb P(\operatorname{Sym}^{d_i}V^*)
\cong\mathbb P^{N_i}.
\]
Multiplication of forms gives a finite morphism
\[
\pi_\lambda:
P_1\times\cdots\times P_r
\longrightarrow
X_\lambda(V),
\qquad
([F_1],\ldots,[F_r])
\longmapsto
[F_1\cdots F_r].
\]

Let \(H\) denote the hyperplane class of the ambient projective space, and let \(h_i\) denote the hyperplane class on \(P_i\). Because every coefficient of the product is multihomogeneous of degree one in the coefficients of each factor,
\[
\pi_\lambda^*H=h_1+\cdots+h_r.
\]

A general point of \(X_\lambda(V)\) can be represented by a product in which every factor is irreducible. Unique factorization then shows that the only preimages arise by permuting factors having equal degree. Hence the generic degree of \(\pi_\lambda\) is
\[
\delta_\lambda=\prod_{e\ge1}\mu_e!.
\]

Since
\[
\dim(P_1\times\cdots\times P_r)=D,
\]
the projection formula gives
\[
\delta_\lambda\deg X_\lambda(V)
=
\int_{P_1\times\cdots\times P_r}
(h_1+\cdots+h_r)^D.
\]
Only the monomial
\[
h_1^{N_1}\cdots h_r^{N_r}
\]
survives integration, and its multinomial coefficient is
\[
\frac{D!}{\prod_iN_i!}.
\]
Therefore
\[
\deg X_\lambda(V)
=
\frac{D!}
{\left(\prod_iN_i!\right)\left(\prod_e\mu_e!\right)}.
\]

For the full reducible locus, the archival source proves that, when \(m\ge3\), the unique component of maximal dimension has factorization type
\[
(d-1,1).
\]
Thus the degree of the full reducible locus is the degree of that component.

If \(d=2\), the two parts are equal. Hence
\[
N_1=N_2=m-1
\]
and the generic degree of the multiplication map is \(2\), giving
\[
\deg R_{m,2}
=
\frac{(2m-2)!}{2((m-1)!)^2}.
\]

If \(d\ge3\), the two parts \(d-1\) and \(1\) are distinct, so the generic degree is \(1\). Here
\[
N_{d-1}=\binom{m+d-2}{m-1}-1,
\qquad
N_1=m-1,
\]
and therefore
\[
\deg R_{m,d}
=
\binom{\binom{m+d-2}{m-1}+m-2}{m-1}.
\]

## Verification
The bundled checker enumerates every integer partition of
\[
2\le d\le10
\]
for
\[
3\le m\le7.
\]
For every partition it independently computes the intersection coefficient
\[
[h_1^{N_1}\cdots h_r^{N_r}]
(h_1+\cdots+h_r)^D
\]
as a multinomial number, divides by the exact equal-degree permutation count, and checks integrality.

It also verifies the closed formula for the maximal component \((d-1,1)\), the split-form specialization \((1,\ldots,1)\), and the concrete values
\[
\deg R_{3,2}=3,\qquad
\deg R_{4,2}=10,\qquad
\deg R_{3,3}=21,\qquad
\deg R_{4,3}=220.
\]

These finite checks are regression evidence only. The all-parameter proof is the intersection-theoretic argument above.

## Relationship to prior work
Catalisano, Geramita, Gimigliano, Harbourne, Migliore, Nagel, and Shin define exactly the varieties \(X_\lambda(V)\) and explicitly record the finite multiplication morphism from a product of projective spaces. They also state that a general point is represented by irreducible factors.

In their further-questions section they explicitly say that Mammana gave a degree formula for reducible plane curves but that they had no generalization to reducible hypersurfaces beyond the plane-curve case. The formula above supplies such a generalization for every factorization type in at least three variables and, by using their unique maximal-component result, for the full reducible locus itself.

The completely decomposable case \(\lambda=(1,\ldots,1)\) was already treated separately in the literature on split forms. It is only a special case of the formula here and is not the novelty claim.

Targeted semantic and web searches for degree formulas under the aliases “varieties of reducible forms,” “factorization-type varieties,” “reducible hypersurfaces,” and the notation \(X_{n-1,\lambda}\) did not locate a later general formula. A 2018 survey still presents these varieties through their multiplication parametrization and cites the same body of work without supplying the formula above.

## Limitations
The theorem concerns ordinary projective degree, not defining equations, secant degrees, multidegrees, singularities, or Chow classes in a larger parameter space.

The argument does not apply unchanged to binary forms because generic factors there are themselves reducible.

The proof is short once the finite multiplication morphism and its generic degree are isolated, so an unindexed or folklore observation remains a residual originality risk.

## References
M. V. Catalisano, A. V. Geramita, A. Gimigliano, B. Harbourne, J. Migliore, U. Nagel, and Y. S. Shin, *Secant Varieties of the Varieties of Reducible Hypersurfaces in \(\mathbb P^n\)*, arXiv:1502.00167, first submitted 31 January 2015; later published in *Journal of Algebra* 528 (2019), 381--438, DOI 10.1016/j.jalgebra.2019.03.014.

A. Bernardi, E. Carlini, M. V. Catalisano, A. Gimigliano, and A. Oneto, *The Hitchhiker Guide to: Secant Varieties and Tensor Decomposition*, *Mathematics* 6 (2018), Article 314.
