# Integral cohomology lattices of Schubert compactifications of matrix pencils

## Finding
Let \(L\) be a genuinely two-dimensional complex matrix pencil, and let \(Y_L\) be its Schubert compactification in the Grassmannian of graphs. Its **ordinary integral cohomology is torsion-free, concentrated in degrees \(0,2,4\)**, and its entire integral cup-product ring has the following explicit Kronecker-block formula.

Write the regular part of the Kronecker decomposition using distinct generalized eigenvalues \(\theta_i\), with distinct increasing Jordan-block sizes \(k_{i1}<\cdots<k_{ih_i}\) at eigenvalue \(\theta_i\). Set \(k_{i0}=0\), \(d_{ij}=k_{ij}-k_{i,j-1}>0\), \(r=\sum_i h_i\), and \(\kappa=\sum_{i,j}d_{ij}\). The multiplicities of the Jordan blocks are arbitrary positive integers. Empty collections are allowed in the singular-pencil case.

If \(L\) has a singular Kronecker summand, then \(H^2(Y_L;\mathbb Z)\) has an integral basis \(u_0,u_1,\ldots,u_r\), with
\[
 u_0^2=\omega,\qquad u_0u_p=0,\qquad u_pu_q=-\delta_{pq}d_p\,\omega\quad(1\le p,q\le r),
\]
where the positive integers \(d_1,\ldots,d_r\) enumerate the \(d_{ij}\), and \(\omega\) is the positive generator of \(H^4(Y_L;\mathbb Z)\). Thus the signed determinant of the degree-two intersection matrix is \((-1)^r\prod_p d_p\), with the empty product equal to one.

If \(L\) is regular (no singular Kronecker summand), then \(\kappa\ge2\), \(H^2(Y_L;\mathbb Z)\) has an integral basis \(v_1,\ldots,v_r\), and
\[
 v_pv_q=(d_pd_q-\delta_{pq}d_p)\,\omega,
 \qquad \left|\det(v_pv_q/\omega)\right|=(\kappa-1)\prod_{p=1}^r d_p.
\]
In either case, \(H^0(Y_L;\mathbb Z)=H^4(Y_L;\mathbb Z)=\mathbb Z\), while \(H^1=H^3=0\) and all degrees above four vanish. The positive-degree products are completely specified by the displayed degree-two pairings. The degree-two rank is \(r+1\) for a singular pencil and \(r\) for a regular pencil.

In particular, the integral cohomology ring depends on the distinct *sizes* of Jordan blocks and on the regular/singular dichotomy, but is independent of Jordan-block multiplicities, eigenvalue positions, and the detailed singular Kronecker indices.

## Assumptions and scope
All varieties and cohomology groups are over \(\mathbb C\), and cohomology is ordinary singular cohomology with coefficients \(\mathbb Z\). Let \(L\subset\mathrm{Mat}_{n\times m}(\mathbb C)\) have dimension exactly two. The compactification \(Y_L\subset\mathrm{Gr}(n,n+m)\) is the closure of the space of graphs of matrices in \(L\), in the convention of Galgano--Gesmundo--Keneshlou [1]. The Kronecker regular summands are Jordan pencils \(J_{k_{ij}}(\theta_i)\) occurring with arbitrary strictly positive multiplicities. Distinct values of \(i\) indicate distinct generalized eigenvalues. "Regular" means there are no left or right singular Kronecker summands; "singular" means at least one such summand occurs. The formula is insensitive to the sizes of singular summands but makes no claim about isomorphism of the varieties.

When \(r=0\), only the singular case occurs, with \(H^2=\mathbb Z\) and square-one generator. In the regular case \(\kappa\ge2\), because a single size-one scalar Jordan pencil alone does not span a two-dimensional linear matrix space.

## Proof
**(1) Resolution and its integral lattice.** By [1, Proposition 4.1 and Lemma 4.3], the compactification has a birational resolution \(f:\widetilde Y\to Y_L\) obtained by successively blowing up \(\mathbb P^2\) at the \(\kappa\) (possibly infinitely near) points indexed by \((i,\ell)\), with \(1\le\ell\le k_{i,h_i}\). Let \(H\) be the pullback of the line class and let \(E_{i\ell}\) be the *total-transform* classes of the exceptional divisors. They form a basis of \(H^2(\widetilde Y;\mathbb Z)\) with
\[
H^2=1,\qquad H\cdot E_{i\ell}=0,\qquad
E_{i\ell}\cdot E_{j t}=-\delta_{ij}\delta_{\ell t}.
\]
Here intersection numbers abbreviate cup products evaluated on the fundamental class. In particular, the resolution lattice is integral and unimodular.

By [1, Propositions 3.7, 4.5 and Theorem 4.6], the divisors contracted by \(f\) are precisely the strict transforms
\[
 A_{i\ell}=E_{i\ell}-E_{i,\ell+1}
 \quad\text{for }1\le\ell<k_{i,h_i}\text{ with }\ell\notin\{k_{i1},\ldots,k_{ih_i}\},
\]
together, **only in the regular-pencil case**, with the strict transform of the line at infinity,
\[
 B=H-\sum_{i,\ell}E_{i\ell}.
\]
Every nontrivial fiber is a tree of smooth rational curves; it has vanishing odd cohomology and free second cohomology with one generator for each irreducible component.

**(2) The integral Leray sequence.** Because \(f\) is proper with connected fibers and all nontrivial fibers are rational trees, its integral Leray spectral sequence has \(R^1f_*\mathbb Z=0\), \(R^2f_*\mathbb Z\) a skyscraper sheaf whose stalks are the second cohomology of the contracted fibers, and no higher direct images. The low-degree exact sequence identifies
\[
0\longrightarrow H^2(Y_L;\mathbb Z)
\xrightarrow{f^*}H^2(\widetilde Y;\mathbb Z)
\xrightarrow{\rho}\bigoplus_{p\in\mathrm{Sing}(Y_L)}H^2(f^{-1}(p);\mathbb Z)
\longrightarrow H^3(Y_L;\mathbb Z)\longrightarrow0.
\]
Smooth points with a one-point fiber contribute nothing. The map \(\rho\) pairs a class on \(\widetilde Y\) with each contracted curve. Furthermore \(H^1(Y_L;\mathbb Z)=0\), and the degree-one birational map induces an isomorphism \(H^4(Y_L;\mathbb Z)\simeq H^4(\widetilde Y;\mathbb Z)=\mathbb Z\).

**(3) Saturation, not just rational rank.** The contracted classes \(A_{i\ell}\) are adjacent differences among exceptional basis vectors, with only some edges of a disjoint union of paths retained. Their \(\mathbb Z\)-span is primitive: quotienting by these relations simply identifies the exceptional basis vectors within consecutive intervals \([k_{i,j-1}+1,k_{ij}]\), yielding a free abelian quotient. In the regular case the additional contracted class \(B\) has coefficient \(1\) on \(H\), so it remains primitive modulo the adjacent-difference sublattice. Thus the entire contracted-curve lattice is a primitive sublattice of the unimodular resolution lattice. Every integral homomorphism from it extends to the resolution lattice; equivalently, \(\rho\) is surjective. It follows that \(H^3(Y_L;\mathbb Z)=0\), and \(H^2(Y_L;\mathbb Z)\) is precisely the *integral* perpendicular lattice to the contracted curves, without hidden finite-index ambiguity.

**(4) An integral basis and the cup pairing.** Write a cohomology class on the resolution as \(aH+\sum_{i,\ell}b_{i\ell}E_{i\ell}\). Orthogonality to the contracted adjacent differences is exactly \(b_{i\ell}=b_{i,\ell+1}\) for every retained edge; hence the coefficients are constant, say \(b_p\), over the \(r\) intervals of lengths \(d_p\). For a singular pencil there is no other condition, so \(a,b_1,\ldots,b_r\) are free integral coordinates, and the restricted intersection pairing is \(aa'-\sum_pd_pb_pb'_p\). This yields the diagonal matrix in the finding.

For a regular pencil, orthogonality to \(B\) imposes exactly \(a+\sum_pd_pb_p=0\), with no divisibility obstruction. The coefficients \(b_1,\ldots,b_r\) form an integral basis, and inserting \(a=-\sum_pd_pb_p\) into the resolution intersection form gives the matrix \(G_{pq}=d_pd_q-\delta_{pq}d_p\). Its determinant follows from the matrix determinant lemma applied to \(G=-\operatorname{diag}(d_1,\ldots,d_r)+dd^{\mathsf T}\):
\[
\det G=(-1)^r\Bigl(\prod_pd_p\Bigr)(1-\kappa).
\]
Since \(f\) has degree one, \(f^*:H^4(Y_L;\mathbb Z)\to H^4(\widetilde Y;\mathbb Z)\) sends positive generator to positive generator; hence these computed integral pairings are exactly the cup products on \(Y_L\). All other cohomology groups and products follow from dimension and the preceding sequence. This proves the claim.

## Verification
The included `verify.py` uses only the Python standard library. It constructs the integral exceptional-curve vectors for eleven representative Kronecker block patterns; directly checks orthogonality of the displayed integral bases to all contracted curves; verifies their exact Gram determinants by the Bareiss algorithm; and checks that maximal minors of the contracted-curve matrix have gcd one in the bounded instances. Run `python3 verify.py` from the extracted directory. The expected final line is `EXACT_SAMPLE_CHECKS_OK`. This is a *finite consistency check*, not an infinite proof; saturation and the ring theorem are established algebraically above.

For example, a regular pencil with one Jordan block of size \(2\) has degree-two lattice \(\langle2\rangle\), while two distinct size-one eigenvalues give the hyperbolic plane. A singular pencil with consecutive block-size gaps \(2\) and \(3\) has pairing \(\operatorname{diag}(1,-2,-3)\). These contrast with the rational Weil-divisor intersection data in [1].

## Relationship to prior work
Galgano--Gesmundo--Keneshlou [1] give the blow-up construction, classify contracted rational curves and quotient singularities, and compute the **rational numerical Weil-divisor intersection pairing** in Theorem 4.8. Their result is an essential input, but its rational generators do not specify the primitive image of ordinary **integral singular cohomology** inside the unimodular resolution lattice. The new assertion is the full integral lattice and cup-product structure, especially the proof of saturation and the resulting absence of degree-three torsion. General studies of rational homotopy of normal projective singular varieties, such as [2], address different (rational) invariants and do not supply this explicit integral Kronecker-block classification.

## Limitations
The theorem concerns ordinary topological singular cohomology over \(\mathbb C\), **not** intersection cohomology, Chow groups, integral divisor class groups, or cohomology in positive characteristic. A claimed isomorphism of integral rings is not an isomorphism of the singular projective surfaces themselves. Standard resolution facts and the topology of rational trees are used; the original paper supplies the precise exceptional configuration. An equivalent integral reinterpretation in unindexed literature is not ruled out, and independent verification has not been performed.

## References
[1] V. Galgano, F. Gesmundo, H. Keneshlou, *Schubert compactifications of matrix pencils*, arXiv:2610.07164v1 (publicly submitted 2026-10-05), especially Propositions 3.7, 4.1, 4.5, Lemma 4.3, and Theorems 4.6, 4.8. https://arxiv.org/abs/2610.07164

[2] D. Chataur, J. Cirici, *Rational homotopy of complex projective varieties with normal isolated singularities*, arXiv:1503.05347, a distinct rational-homotopy framework. https://arxiv.org/abs/1503.05347
