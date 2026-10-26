# An asymptotic Bergman boundary torus for simple horn Reinhardt domains

## Finding
Let \(\Omega\subset\mathbb C^n\), \(n\ge2\), be a **simple horn Reinhardt domain** of order \(a>n+1\) in the sense of Hayashida--Kamimoto--Thu, and let \(X^*=(x_1,\ldots,x_n)\) be its distinguished unit vector with every \(x_j>0\). Write \(m=\max\{j\in\mathbb Z_{\ge0}:j<a-n\}\ge1\), \(c_p=\|z^p\|_{A^2(\Omega)}^{-2}\), and
\[
 A_j=\sum_{|p|=j}c_p\prod_{k=1}^nx_k^{2p_k}\qquad(0\le j\le m).
\]
All \(A_j\) are strictly positive. Give \(\Omega\) its Bergman length metric normalized by \(g_{k\bar\ell}=\partial_{z_k}\partial_{\bar z_\ell}\log K_\Omega(z,z)\), so a tangent vector \(v\) has squared norm \(\sum g_{k\bar\ell}v_k\bar v_\ell\).

For every phase \(\theta=(\theta_1,\ldots,\theta_n)\in\mathbb T^n\), the ray
\[
 \gamma_\theta(t)=t(x_1e^{i\theta_1},\ldots,x_ne^{i\theta_n}),\qquad t>0,
\]
lies in \(\Omega\) and has **finite remaining Bergman length** with the asymptotic expansion, uniform in \(\theta\),
\[
 \boxed{\operatorname{Length}_B(\gamma_\theta|_{[t,\infty)})
       =\sqrt{\frac{A_{m-1}}{A_m}}\,t^{-1}+O(t^{-3})}\quad(t\to\infty).
\]
Each ray converges in the metric completion \(\widehat\Omega^B\) to a point outside \(\Omega\). Two rays have the same completion limit **if and only if** their phases differ by a common rotation. Consequently, \(\widehat\Omega^B\setminus\Omega\) contains a canonically embedded topological torus \(\mathbb T^n/\mathbb T_{\mathrm{diag}}\cong\mathbb T^{n-1}\). In particular, every such \(\Omega\) is Bergman-metrically incomplete.

The induced angular quadratic form on the fixed-radius phase tori converges to the constant form
\[
 Q(v)=\sum_{|p|=m}\frac{s_p}{A_m}(p\cdot v)^2
 -\left(\sum_{|p|=m}\frac{s_p}{A_m}(p\cdot v)\right)^2,
 \quad s_p=c_p\prod_{k=1}^nx_k^{2p_k}.
\]
Its kernel is exactly \(\mathbb R(1,\ldots,1)\), and it induces a positive definite flat *limiting angular tensor* on the quotient torus. No claim is made that this tensor is the intrinsic length metric on the completion boundary.

## Assumptions and scope
The horn hypotheses are those of Definition 2.1 of [1]: \(\Omega\) is connected and Reinhardt, contains a ball about zero, and its large-radius radial slices \(\rho U(\rho)\) satisfy the prescribed horn-volume condition and \(\bigcap_{\rho\ge R}U(\rho)=\{X^*\}\subset S^+_\varepsilon\). Thus each \(x_j\) is strictly positive and every point on each ray \(\gamma_\theta\) belongs to \(\Omega\). Theorem 3.1 of [1] provides exactly \(A^2(\Omega)=\operatorname{span}\{z^p:|p|\le m\}\); monomial orthogonality follows from Reinhardt invariance. The order range \(a>n+1\) is necessary for the linear monomials to occur and for the Bergman form to be nondegenerate by this argument. All statements concern these prescribed rays and phase directions, not an identification of the full completion.

## Proof
**1. Projective metric.** Orthogonality supplies the diagonal kernel
\[
 K_\Omega(z,z)=\sum_{|p|\le m}c_p|z^p|^2,
\]
with each \(c_p>0\). Its normalized monomial map
\[
 \Phi(z)=[\sqrt{c_p}z^p]_{|p|\le m}\in\mathbb{CP}^{N-1},
 \qquad N=\binom{n+m}{n},
\]
pulls the Fubini--Study metric \(\partial\bar\partial\log\sum|Z_p|^2\) back to the Bergman metric. Since the coordinates include \(1,z_1,\ldots,z_n\), this map is an injective holomorphic immersion; in particular the Bergman form is positive definite. The classical Fubini--Study pullback identity, in this normalization, is also recorded in [2, Section 2].

**2. Exact variance formulas.** For fixed phase \(\theta\), a representative of \(\Phi\circ\gamma_\theta\) has coordinates \(u_p(t)=\sqrt{s_p}\,t^{|p|}e^{i p\cdot\theta}\). Let
\[
 P(t)=\sum_{j=0}^mA_jt^{2j},\qquad
 w_p(t)=\frac{s_pt^{2|p|}}{P(t)}.
\]
These weights are nonnegative and sum to one. The Fubini--Study speed identity
\[
 \|u'\|^2/\|u\|^2-{|\langle u',u\rangle|^2}/{\|u\|^4}
\]
(the scalar product is Hermitian) therefore gives the **exact** radial identity
\[
 \|\dot\gamma_\theta(t)\|_B^2
 =t^{-2}\left(\sum_pw_p(t)|p|^2-\big(\sum_pw_p(t)|p|\big)^2\right).
\]
Similarly, for a phase-direction \(v\in\mathbb R^n\), the squared length of \(\partial_u\gamma_{\theta+uv}(t)|_{u=0}\) is exactly \(\operatorname{Var}_{w(t)}(p\cdot v)\). Both identities are independent of the base phase.

**3. Sharp radial tail.** Since \(A_m,A_{m-1}>0\), the total probability of degree \(m-1\) is
\[
 \sum_{|p|=m-1}w_p(t)=\frac{A_{m-1}}{A_m}t^{-2}+O(t^{-4}),
\]
while degree at most \(m-2\) has probability \(O(t^{-4})\) (zero if \(m=1\)). The variance of \(|p|\), centered at the dominant value \(m\), is consequently
\[
 \operatorname{Var}_{w(t)}(|p|)
 =\frac{A_{m-1}}{A_m}t^{-2}+O(t^{-4}).
\]
Thus \(\|\dot\gamma_\theta(t)\|_B=\sqrt{A_{m-1}/A_m}\,t^{-2}+O(t^{-4})\). Integrating from \(t\) to infinity proves the displayed \(t^{-1}\) asymptotic and uniformity.

**4. Boundary identification and embedded torus.** Finite tail length makes each ray Cauchy in the Bergman metric completion. Along a common phase shift \(\theta\mapsto\theta+u(1,\ldots,1)\), the exact angular-speed formula equals \(|u'|\sqrt{\operatorname{Var}_{w(t)}(|p|)}=O(t^{-1})|u'|\). Hence common rotations give the same limit in the completion.

Conversely, \(\Phi\) is length-nonincreasing from \((\Omega,d_B)\) into the complete projective Fubini--Study space. Its image along the rays converges to
\[
 \Phi_\infty(\theta)
 =[\sqrt{s_p}\,e^{i p\cdot\theta}]_{|p|=m},
\]
with all lower-degree homogeneous coordinates zero. If \(\Phi_\infty(\theta)=\Phi_\infty(\varphi)\), comparing the nonzero degree-\(m\) coordinates indexed by \(p=me_i\) and \(q=(m-1)e_i+e_j\) forces \(e^{i(\theta_j-\theta_i)}=e^{i(\varphi_j-\varphi_i)}\) for every \(i,j\). Thus the phase vectors differ by one diagonal rotation. If they do not, their positive projective distance bounds below the limiting Bergman distance, and the completion points are distinct.

The map from the compact quotient phase torus to the completion is continuous: the radial tails have a common \(O(t^{-1})\) length bound, while at every fixed radius the phase map is continuous and its induced length distances tend to zero with the phase difference. A continuous injection of a compact space into the Hausdorff metric completion is a topological embedding. None of these completion points comes from \(\Omega\), because the constant-monomial homogeneous coordinate of \(\Phi(z)\) is \(\sqrt{c_0}\ne0\) throughout \(\Omega\), but it vanishes at every \(\Phi_\infty\).

**5. Limiting angular tensor.** The weights converge to \(s_p/A_m\) on \(|p|=m\) and to zero elsewhere, yielding \(Q\). It vanishes for \(v=(1,\ldots,1)\) because all top exponents have equal total degree. Conversely, every top-degree exponent occurs with positive weight; if \(Q(v)=0\), the numbers \(p\cdot v\) are constant over all \(|p|=m\). Comparing \(me_i\) with \((m-1)e_i+e_j\) gives \(v_i=v_j\) for all \(i,j\). The constant coefficients make the resulting positive quotient tensor flat. This completes the proof.

## Verification
The formulas follow from the stated polynomial kernel and finite weighted variances, not from numerical experiments. The exact asymptotic can be independently checked by expanding the rational quantities \(P(t)\), \(\sum_p s_pt^{2|p|}|p|\), and \(\sum_p s_pt^{2|p|}|p|^2\) at infinity. For a symbolic degree-two diagnostic, \(P(t)=1+ut^2+vt^4\), \(u,v>0\), yields
\[
 \operatorname{Var}(|p|)=
 \frac{t^2(uvt^4+u+4vt^2)}{(1+ut^2+vt^4)^2},
 \qquad\lim_{t\to\infty}t^2\operatorname{Var}(|p|)=u/v.
\]
This check does not replace the general proof. The distinction between the ambient Fubini--Study distance, the intrinsic Bergman distance, and the limiting angular tensor is essential.

## Relationship to prior work
The monomial basis, horn definition, and the entire diagonal complex line inside a simple horn are from [1, Definition 2.1; Theorem 3.1; Proposition 5.2, equation (5.2)]. Its Theorem 4.1 also identifies Fubini--Study-type constant curvature for the lowest nontrivial polynomial degree. The projective Bergman map and its isometry property are standard, and [2, Section 2] explicitly records them. The present additional assertion is the **metric-completion boundary torus with its if-and-only-if phase identification**, its sharp degree-adjacent coefficient in the escape-length asymptotic, and the general higher-degree limiting covariance tensor. In particular, mere Bergman incompleteness in the degree-one case is not presented as independently surprising or as the entire novelty claim.

## Limitations
No statement is made about the *full* metric completion, about geodesic minimizing rays, or about equality between the limiting angular tensor and intrinsic distances along the completed boundary. The length expansion is for prescribed rays with coordinates proportional to \(X^*\), not arbitrary approaches to infinity. Its coefficient depends on all Bergman monomial norms of the domain. The order threshold and simplicity assumptions are retained. No priority claim is made against unpublished or unindexed special-case computations of toric projective boundary geometry.

## References
[1] C. Hayashida, J. Kamimoto, N. Van Thu, *On horn-shaped Reinhardt domains*, arXiv:2610.17527v1 (first posted 2026-10-13), https://arxiv.org/abs/2610.17527 .

[2] G. Heier, R. Mudaliar, H. Zuo, *Biholomorphic rigidity and symmetry breaking for domains with Bergman metric of constant positive holomorphic sectional curvature*, arXiv:2610.13831v1 (first posted 2026-10-09), https://arxiv.org/abs/2610.13831 .
