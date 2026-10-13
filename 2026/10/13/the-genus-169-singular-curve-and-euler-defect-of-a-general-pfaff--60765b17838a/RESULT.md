# The genus-169 singular curve and Euler defect of a general Pfaffian quartic sixfold

## Finding
Let \(V\) be an eight-dimensional complex vector space and \(L\subset\bigwedge^2 V^*\) a general eight-dimensional linear subspace. The Pfaffian quartic sixfold \(Y=\{[\omega]\in\mathbb P(L):\operatorname{Pf}(\omega)=0\}\) has **scheme-theoretic** singular locus \(C\) a smooth irreducible curve. Its invariants, transverse analytic type, and smoothing defect are
\[
\deg C=84,\qquad \omega_C\simeq\mathcal O_C(4),\qquad g(C)=169,\qquad
\chi_{\mathrm{top}}(Y)=1312,\qquad \chi_{\mathrm{top}}(Y_{\mathrm{sm}})=1648.
\]
The germ of \(Y\) normal to \(C\) is a nondegenerate six-variable quadratic hypersurface germ. Here \(Y_{\mathrm{sm}}\) denotes any smooth quartic sixfold in \(\mathbb P^7\), including a general smoothing of \(Y\).

## Assumptions and scope
The ground field is \(\mathbb C\). “General” means that \(\mathbb P(L)\cong\mathbb P^7\) belongs to a nonempty Zariski-open subset of the Grassmannian of projective seven-planes in \(\mathbb P(\bigwedge^2 V^*)\cong\mathbb P^{27}\). A skew form has even rank; the Pfaffian hypersurface consists of forms of rank at most six. Curve degree is with respect to \(\mathcal O_{\mathbb P^7}(1)\); its canonical bundle is intrinsic. Euler characteristics refer to complex classical topology. No assertion concerns special, non-general Pfaffian linear systems.

## Proof
**1. The singular scheme and its smoothness.** In the ambient \(\mathbb P^{27}\), let \(R_4\) and \(R_2\) denote the loci of alternating forms of rank at most four and two. The gradient of the order-eight Pfaffian consists of its order-six sub-Pfaffians, hence its ambient singular locus is exactly \(R_4\). Standard rank-counting gives \(\dim R_4=21\) and \(\dim R_2=12\), while \(R_4\setminus R_2\) is smooth. A general \(\mathbb P^7\) misses \(R_2\) and meets the smooth stratum of \(R_4\) transversely in dimension one. Repeated Bertini and connectedness for a general proper linear section of the irreducible \(R_4\) show the intersection \(C\) is smooth and irreducible. Away from \(C\), Bertini makes \(Y\) smooth. At rank four, the six remaining local alternating entries are independent normal coordinates, and the Pfaffian is a unit times the Pfaffian of a \(4\times4\) alternating block, i.e.
\[
q=z_{12}z_{34}-z_{13}z_{24}+z_{14}z_{23}.
\]
This is a nondegenerate quadratic in six variables. Consequently the restricted Jacobian ideal is the ideal of the reduced smooth curve \(C\), and the sixfold has transverse ordinary quadratic singularity at every point of \(C\).

**2. Resolution and canonical bundle.** Let \(G=\operatorname{Gr}(4,V)\) parametrize four-dimensional quotients \(Q\) of \(V\), with tautological quotient bundle also written \(Q\). Put \(E=\bigwedge^2 Q^*\) (rank six) and \(P=\mathbb P_G(E)\) in the *lines-in-the-fibres* convention, with \(\xi=c_1(\mathcal O_P(1))\). The natural map \(P\to R_4\) is an isomorphism over the rank-four stratum: the quotient is uniquely \(V/\ker\omega\). Thus \(C\) is identified with a smooth complete intersection of twenty general divisors of class \(\xi\) in the smooth \(21\)-fold \(P\). Since \(K_G\simeq(\det Q)^{-8}\) and \(\det E\simeq(\det Q)^{-3}\), the relative Euler sequence yields
\[
K_P\simeq\mathcal O_P(-6)\otimes(\det Q)^{-5},\qquad
K_C\simeq\mathcal O_C(14)\otimes(\det Q|_C)^{-5}.
\]
On the rank-four locus, the universal alternating form is symplectic on \(Q\) with values in \(\mathcal O_C(1)\). Its Pfaffian is a nowhere vanishing section of \(\det Q^*\otimes\mathcal O_C(2)\). Hence \(\det Q|_C\simeq\mathcal O_C(2)\), and therefore
\[\boxed{\omega_C\simeq\mathcal O_C(4).}\]

**3. Degree and genus.** Let \(x_1,\dots,x_4\) be formal Chern roots of \(Q\). The six roots of \(E\) are \(-x_i-x_j\) for \(i<j\). By the projective-bundle push-forward formula,
\[
\deg C=\int_P\xi^{21}=\int_G s_{16}(E)
=\int_G h_{16}\bigl(x_i+x_j:1\le i<j\le4\bigr)=84.
\]
The final equality follows by exact integral Schubert calculus, using the coefficient formula
\[
\int_{\operatorname{Gr}(4,8)} f(x)=
[x_1^7x_2^6x_3^5x_4^4]\!\left(f(x)\prod_{i<j}(x_i-x_j)\right)
\]
for symmetric homogeneous \(f\) of degree sixteen. The accompanying exact-integer checker independently expands the six pair sums and obtains \(84\), while verifying \(\int_G (x_1+\cdots+x_4)^{16}=24024\). As \(\deg\omega_C=4\deg C=336\), adjunction for smooth curves gives \(2g(C)-2=336\) and \(g(C)=169\).

**4. Euler defect.** A transverse nondegenerate quadratic hypersurface in six complex variables has Milnor fibre homotopy equivalent to \(S^5\), of Euler characteristic zero, whereas the singular transverse cone has Euler characteristic one. The holomorphic Morse–Bott normal form along smooth compact \(C\), equivalently constructibility of vanishing cycles, therefore gives
\[
\chi_{\mathrm{top}}(Y_{\mathrm{sm}})-\chi_{\mathrm{top}}(Y)
=-\chi_{\mathrm{top}}(C)=2g(C)-2=336.
\]
For a smooth quartic hypersurface \(Y_{\mathrm{sm}}\subset\mathbb P^7\), its tangent Chern class is \((1+h)^8/(1+4h)\); hence
\[
\chi_{\mathrm{top}}(Y_{\mathrm{sm}})=4[h^6]\frac{(1+h)^8}{1+4h}=1648,
\qquad \chi_{\mathrm{top}}(Y)=1648-336=1312.
\]
This completes the one combined singular-curve and smoothing-defect determination.

## Verification
The standalone code `verification/check_pfaffian.py` computes, over exact integers, the Grassmannian coefficient extraction for \(\deg C=84\), the auxiliary integral \(\int_G c_1(Q)s_{15}(E)=168\), the genus and the smooth/singular Euler numbers. It also checks the benchmark Grassmannian degree \(24024\). Its output must be `PFAFFIAN_SINGULAR_CURVE_NUMERICS_OK`. The curve's generic smoothness, scheme structure, normal form and adjunction are proven symbolically above; the finite code does not certify these geometric arguments independently.

## Relationship to prior work
The September 18, 2026 work of Bolognesi–Ciliberto–Verra introduces the adjacent general eight-by-eight Pfaffian quartic in \(\mathbb P^6\) as a birational model for index-one Fano linear sections, motivating the first next-dimensional Pfaffian case with a positive-dimensional singular locus. Iliev–Markushevich describe the general rank stratification of the universal Pfaffian quartic and smooth lower-dimensional sections. Harris–Tu provide the general degeneracy-locus degree formula; thus the rank bound and degree \(84\) alone are **not** originality claims. A later October 8, 2026 paper of Bolognesi–Ciliberto–Verra also explicitly recalls the universal singular-stratum degree. The present integrated claim additionally determines the canonical bundle, genus, complete transverse type and topological smoothing defect for the \(\mathbb P^7\) section. No comparison source inspected gives that integrated determination. General determinantal techniques underlie the proof; previous implied coverage has not been eliminated in every possible source.

## Limitations
The result applies only to a general linear system over \(\mathbb C\). It does not determine Hodge numbers of a resolution, arbitrary special Pfaffian quartics, or higher-order degeneracy loci. A complete full-text comparison with the inaccessible September 2026 initiating preprint and Harris–Tu's original paper remains outstanding; this is a residual originality risk, not an independent audit. Smoothing Euler uses ordinary topological Euler characteristic, not a derived or motivic invariant.

## References
1. M. Bolognesi, C. Ciliberto and A. Verra, *On Fano varieties of index one that are linear sections of Grassmannians of lines*, arXiv:2609.21503v1 (first public September 18, 2026), https://arxiv.org/abs/2609.21503.
2. A. Iliev and D. Markushevich, *Quartic 3-fold: Pfaffians, instantons and half-canonical curves*, arXiv:math/9910133 (1999), https://arxiv.org/pdf/math/9910133.
3. J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, Topology 23 (1984), 71–84, DOI:10.1016/0040-9383(84)90026-0.
4. M. Bolognesi, C. Ciliberto and A. Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1 (first public October 8, 2026; cited only as a subsequent coverage comparison), https://arxiv.org/html/2610.11925v1.
