# An asymptotic Bergman boundary torus for simple horn Reinhardt domains

## Finding
Let \(\Omega\subset\mathbb C^n\), \(n\ge2\), be a simple horn Reinhardt domain of order \(a>n+1\) in the sense of [1, Definition 2.1]. Use a threshold \(R\) as in that definition, and let \(X^*=(x_1,\ldots,x_n)\) be the distinguished positive unit vector. Set
\[
m=\max\{j\in\mathbb Z_{\ge0}:j<a-n\},\qquad c_p=\|z^p\|_{A^2(\Omega)}^{-2},\qquad A_j=\sum_{|p|=j}c_p\prod_k x_k^{2p_k}\quad(0\le j\le m).
\]
Here \(m\ge1\) and every \(A_j>0\). We use the Bergman length convention \(g_{k\bar\ell}=\partial_{z_k}\partial_{\bar z_\ell}\log K_\Omega(z,z)\), with squared tangent norm \(\sum g_{k\bar\ell}v_k\bar v_\ell\).

For each \(\theta\in\mathbb T^n=(\mathbb R/2\pi\mathbb Z)^n\), the ray tail
\[
\gamma_\theta(t)=t(x_1e^{i\theta_1},\ldots,x_ne^{i\theta_n}),\qquad t>R,
\]
lies in \(\Omega\). It has finite remaining Bergman length, with
\[
\operatorname{Length}_B(\gamma_\theta|_{[t,\infty)})=\sqrt{\frac{A_{m-1}}{A_m}}\,t^{-1}+O(t^{-3}),
\qquad t\to\infty,
\]
uniformly in \(\theta\). Two ray tails converge to the same point of the Bergman metric completion if and only if their phases differ by a common rotation. These points lie outside \(\Omega\), and the limit map embeds \(\mathbb T^n/\mathbb T_{\rm diag}\cong\mathbb T^{n-1}\) as a topological torus in the completion boundary. In particular, \(\Omega\) is Bergman-metrically incomplete.

The angular tensor on the fixed-radius phase tori converges to the constant form
\[
Q(v)=\sum_{|p|=m}\frac{s_p}{A_m}(p\cdot v)^2-\left(\sum_{|p|=m}\frac{s_p}{A_m}(p\cdot v)\right)^2,
\qquad s_p=c_p\prod_k x_k^{2p_k}.
\]
Its kernel is exactly \(\mathbb R(1,\ldots,1)\); the resulting positive tensor on the quotient torus is flat.

## Assumptions and scope
By [1, Definition 2.1], \(\Omega\) is connected and Reinhardt and contains a ball about zero. For large radii, its slices in the radial image of coordinate moduli have the designated horn volume and satisfy \(\bigcap_{\rho\ge R}U(\rho)=\{X^*\}\subset S^+_\varepsilon\). Thus the modulus tuple \(tX^*\) occurs for each \(t>R\), and Reinhardt invariance supplies every phase at that radius. No membership at intermediate radii below \(R\) is needed or asserted. By [1, Theorem 3.1], \(A^2(\Omega)=\operatorname{span}\{z^p:|p|\le m\}\). Integration in the phase variables gives monomial orthogonality.

## Proof
The Bergman kernel on the diagonal is \(\sum_{|p|\le m}c_p|z^p|^2\). Hence the Bergman tensor is the Fubini–Study pullback under
\[
\Phi(z)=[\sqrt{c_p}z^p]_{|p|\le m}\in\mathbb{CP}^{\binom{n+m}{n}-1}.
\]
This is the pullback normalization from \(\partial\bar\partial\log\sum|Z_p|^2\). The constant and linear coordinates make \(\Phi\) an injective immersion, so the metric is positive definite.

Let \(P(t)=\sum_{j=0}^m A_j t^{2j}\) and \(w_p(t)=s_p t^{2|p|}/P(t)\). For a path of projective lifts \(u\), the squared Fubini–Study speed is \(\|u'\|^2/\|u\|^2-|\langle u',u\rangle|^2/\|u\|^4\). The ray lift has entries \(\sqrt{s_p} t^{|p|} e^{ip\cdot\theta}\). In the radial derivative each entry is multiplied by \(|p|/t\); in an angular direction \(v\) it is multiplied by \(i p\cdot v\). Therefore the squared radial speed is \(t^{-2}\operatorname{Var}_{w(t)}(|p|)\) and the squared angular speed is \(\operatorname{Var}_{w(t)}(p\cdot v)\), both independent of the base phase.

The total weight of layer \(m-1\) is \((A_{m-1}/A_m)t^{-2}+O(t^{-4})\); the total of the lower layers is \(O(t^{-4})\) (zero when \(m=1\)). Consequently the second moment of \(m-|p|\) has leading term \((A_{m-1}/A_m)t^{-2}\), while the square of its mean is \(O(t^{-4})\). Taking the square root gives radial speed \(\sqrt{A_{m-1}/A_m}\,t^{-2}+O(t^{-4})\). Integration proves the length estimate and the Cauchy property. For the common phase direction \((1,\ldots,1)\), the speed of rotation by unit angle is \(\sqrt{\operatorname{Var}_{w(t)}(|p|)}=O(t^{-1})\). Bounded-angle common rotations at fixed \(t>R\) thus connect ray points at length tending to zero, so their limits coincide.

Ambient projective distance is bounded by Bergman distance, since the pullback preserves lengths of smooth curves. Thus \(\Phi\) extends continuously to the completion. On a ray tail its limit has only the top-degree coordinates, \([\sqrt{s_p}e^{ip\cdot\theta}]_{|p|=m}\). All these coordinates are nonzero. Comparing the ratios indexed by \(me_i\) and \((m-1)e_i+e_j\) detects each \(e^{i(\theta_j-\theta_i)}\). Therefore phases not related by a common rotation have distinct projective limits and positive limiting Bergman distance. The limiting projective point never has a nonzero constant coordinate, so the completion limit is not a point of \(\Omega\). The fixed-radius phase maps for \(t>R\) are continuous in the Bergman length distance (join nearby phases by short angular paths), and the uniform tail bound makes their limits continuous. The induced map on the compact quotient is an injection into a Hausdorff metric space, hence an embedding.

Finally \(w_p(t)\) tends to \(s_p/A_m\) in degree \(m\) and to zero below. This yields \(Q\) by the angular-speed formula. Since each top-layer weight is positive, zero variance means \(p\cdot v\) is constant over that layer. Using the same pair of exponents as above then gives \(v_i=v_j\) for all \(i,j\). Conversely a diagonal vector gives constant values. The induced positive quotient tensor is constant in angular coordinates, hence flat.

## Verification
The argument is analytic. To check the leading normalization directly, divide \(P(t)\) by \(t^{2m}\) and expand it as \(A_m+A_{m-1}t^{-2}+O(t^{-4})\). For example when \(m=1\) the squared radial speed is exactly \(A_0A_1/(A_0+A_1t^2)^2\), yielding the displayed tail. The top-coordinate ratio criterion is used for projective separation, not to equate the intrinsic distance with the ambient distance.

## Relationship to prior work
The horn slices and polynomial Bergman space come from [1, Definition 2.1 and Theorem 3.1]. The use of [1] here requires only the eventual radial inclusion supplied by the definition, not the full-line observation in [1, Eq. (5.2)]. When \(m=1\), [1, Theorem 4.1] already gives the constant positive curvature model. The projective pullback construction is standard; see also [2, §2]. The additional conclusions concern the sharp escape coefficient, the identification of which phase tails give the same point of the metric completion for every allowed degree, and the explicit angular tensor. The projective limit alone does not establish collapse of the diagonal direction in the length metric.

## Limitations
This describes only the completion points of the prescribed tails, not the full completion. The length is the length of the prescribed ray tail, not necessarily the shortest distance to its boundary point. The flat tensor is a limit of tensors on phase tori and is not identified with any intrinsic boundary metric. The leading coefficient uses the monomial norms from the two highest adjacent degree layers. No priority claim is made against unindexed work.

## References
[1] C. Hayashida, J. Kamimoto and N. Van Thu, *On horn-shaped Reinhardt domains*, arXiv:2610.17527v1, https://arxiv.org/abs/2610.17527.

[2] G. Heier, R. Mudaliar and H. Zuo, *Biholomorphic rigidity and symmetry breaking for domains with Bergman metric of constant positive holomorphic sectional curvature*, arXiv:2610.13831v1, https://arxiv.org/abs/2610.13831.
