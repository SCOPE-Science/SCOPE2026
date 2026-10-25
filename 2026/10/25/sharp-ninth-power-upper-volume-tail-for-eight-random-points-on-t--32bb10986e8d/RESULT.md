# Sharp ninth-power upper-volume tail for eight random points on the three-sphere

## Finding
Let \(X_1,\ldots,X_8\) be independent uniformly distributed points on the Euclidean unit three-sphere \(S^3\subset\mathbb R^4\), and write \(V=\operatorname{vol}_4(\operatorname{conv}\{X_1,\ldots,X_8\})\). Then the precise upper-endpoint law is
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-9}\,\mathbb P\{V>2/3-\varepsilon\}=\frac{2916}{\pi^3}.
\]
In particular the upper endpoint is \(2/3\), the exponent is exactly nine, and the coefficient is positive and explicit. The independent uniform model is on the sphere surface rather than in the four-ball; the eight points are labelled before their convex hull is formed.

## Assumptions and scope
The random sample consists of exactly eight independent points with normalized rotation-invariant surface law on \(S^3\). Volume is four-dimensional Euclidean volume, with unit radius. The limit concerns \(\varepsilon>0\) approaching zero; it does not assert an exact finite-deficit distribution, a rate for the remainder, or an analogous result for other vertex counts. The geometric input used for global maximality and uniqueness is the theorem of Medgyes [1, Corollary 5.2], first posted October 12, 2026: every eight-vertex maximum-volume inscribed four-polytope is a regular four-dimensional cross-polytope, with volume \(2/3\). This result and its equalizers are used as prior results, not proved here.

## Proof
**1. Isolated maximizing orbits modulo rotations.** Set \(M=(S^3)^8\), a smooth compact manifold of dimension \(24\) with product round metric. For any pairing of the eight labels into four unordered pairs, its maximum configurations consist of assigning an orthonormal basis \((q_1,q_2,q_3,q_4)\) to the four pairs as the antipodes \((q_i,-q_i)\). Choosing an ordering and orientation for the pairs does not change the resulting \(O(4)\) orbit. There are exactly \(8!/(2^4 4!)=105\) distinct perfect matchings of labels. Each matching determines one embedded, disjoint orbit isometric to \(O(4)\) with its induced metric. The action is free because four labelled positive vertices determine the orthogonal transformation. Medgyes's global classification [1] implies these are precisely all configurations of maximum volume, including configurations that might otherwise have fewer than eight distinct vertices (which cannot maximize). The compactness of \(M\) implies that for sufficiently small volume deficit every configuration lies in disjoint tubular neighborhoods of the \(105\) orbits.

**2. Exact local volume identity.** Fix an orbit representative with vertices \(p_i^+=e_i\) and \(p_i^-=-e_i\), for \(1\le i\le4\). The 16 cross-polytope facets, with one vertex from each antipodal pair, persist for sufficiently small perturbations, and the origin remains interior. Decomposing the convex hull into the 16 cones from the origin to its facets, with their fixed determinant signs, gives the **exact** identity
\[
V=\frac1{24}\det(p_1^+-p_1^-,\ldots,p_4^+-p_4^-)
=\frac23\det(A),\qquad A_i=\frac{p_i^+-p_i^-}{2}.
\]
No central-symmetry assumption is made on the perturbed configurations. At the representative, introduce sphere coordinates \(u_i,v_i\in e_i^\perp\) by
\[
p_i^+=\sqrt{1-\|u_i\|^2}e_i+u_i,\qquad
p_i^-=-\sqrt{1-\|v_i\|^2}e_i+v_i,
\]
and put \(x_i=(u_i-v_i)/2\), \(y_i=(u_i+v_i)/2\), so the diagonal entries \(x_{ii}=y_{ii}=0\). Direct expansion gives
\[
\det A=1-\frac12\sum_{i=1}^4\|y_i\|^2-\frac12\sum_{1\le i<j\le4}(x_{ij}+x_{ji})^2+O(\|(u,v)\|^3).
\]
Indeed \(A_{ii}=1-(\|x_i\|^2+\|y_i\|^2)/2+O(\|(x,y)\|^4)\) and \(A_{ji}=x_{ij}\) for \(j\ne i\); applying the second-order determinant expansion proves the displayed formula. The six antisymmetric combinations of \(x\) are precisely the infinitesimal simultaneous rotations of the eight vertices.

**3. Normal quadratic form.** At this configuration the product-sphere tangent metric is \(2\sum_i(\|dx_i\|^2+\|dy_i\|^2)\). Hence orthonormal normal coordinates comprise twelve scaled \(y\)-coordinates \(z_y\in\mathbb R^{12}\) and six scaled symmetric off-diagonal \(x\)-coordinates \(z_s\in\mathbb R^6\). The volume deficit is
\[
\Delta=\frac23-V=\frac16\|z_y\|^2+\frac13\|z_s\|^2+O(\|z\|^3).
\]
Equivalently, the Hessian of \(\Delta\) has eigenvalue \(1/3\) of multiplicity twelve and \(2/3\) of multiplicity six on the normal space, and precisely six rotational zero directions. Therefore the maximal orbits are nondegenerate Morse–Bott maxima of the volume function. Since the model and metric are rotation invariant, this normal form holds uniformly along every maximizing orbit. The normal ellipsoid \(\Delta<\varepsilon\) has leading \(18\)-dimensional volume
\[
\operatorname{vol}_{18}\{\|z_y\|^2/6+\|z_s\|^2/3<\varepsilon\}
=\frac{\pi^9}{9!}\,6^6 3^3\,\varepsilon^9.
\]
The \(O(\|z\|^3)\) remainder is uniformly negligible after the substitution \(z=\sqrt\varepsilon\,w\), and Riemannian tube Jacobians converge uniformly to one. Dominated convergence on the bounded rescaled normal neighborhoods proves that the leading probability is this ellipsoid volume times the total induced orbit volume, divided by the ambient configuration volume.

**4. Orbit metric, counting, and normalization.** For any infinitesimal rotation with independent plane-angle entries \(\theta_{ij}\), the eight moving vertices have squared product-metric velocity \(4\sum_{i<j}\theta_{ij}^2\). Thus the induced metric is four times the standard orthogonal-group metric with plane-angle generators orthonormal. The standard \(O(4)\) volume, obtained from the orthonormal-frame fibration, is
\[
|S^3|\,|S^2|\,|S^1|\,|S^0|=32\pi^4.
\]
All six tangent lengths double, so each orbit has induced volume \(2^6\cdot32\pi^4=2048\pi^4\). The ambient product-sphere volume is \((2\pi^2)^8=256\pi^{16}\). Multiplying by \(105\) disjoint matching orbits yields
\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}\frac{\mathbb P(\Delta<\varepsilon)}{\varepsilon^9}
&=\frac{105\cdot2048\pi^4}{(2\pi^2)^8}\cdot\frac{\pi^9}{9!}\,6^6 3^3\\
&=\frac{2916}{\pi^3}.
\end{aligned}
\]
Since the volume-deficit level sets have probability zero sufficiently close to the endpoint (by the local positive normal quadratic form and regular levels for small positive deficit), the strict inequality in the statement is immaterial to the coefficient. This completes the proof.

## Verification
The included standalone `check_tail.py` uses exact integer and rational arithmetic to recover the 105 label matchings and \(2916\) prefactor. In 270 reproducible spherical perturbations it compares the analytic determinant-volume identity with an independent four-dimensional convex hull implementation; the largest absolute difference is below \(4\times10^{-16}\). It additionally probes the second variation, with finite perturbation remainder below \(10^{-4}\) at the tested scales. Run `python check_tail.py` after installing `numpy` and `scipy`, as listed in `requirements.txt`. The verification is supplementary finite numerical evidence; the universal tail asymptotic is derived by the analytic argument above and the stated global-extremizer theorem.

## Relationship to prior work
Medgyes [1, Corollary 5.2] supplies global maximum \(2/3\) and uniqueness of its regular-cross-polytope shapes for eight points on \(S^3\); it does not evaluate the near-maximum probability distribution. Horváth–Lángi [2] established maximality of regular cross-polytopes *within* the cross-polytope combinatorial class; that antecedent is likewise deterministic and does not compute the metric-normal Hessian or random upper-tail constant. Akopyan–Edelsbrunner–Nikitenko [3] study random polytopes on \(S^2\), including expected intrinsic volumes and their deficiencies from a ball; those are dimension-three ambient quantities, not a fixed eight-point upper-volume endpoint law in \(\mathbb R^4\). The new claim is the exact probabilistic asymptotic, its codimension-nine exponent, and the fully evaluated factor from the normal Hessian and labelled maximizing orbits.

## Limitations
The proof relies on the stated maximality-and-equality theorem [1]. Its underlying exact algebraic certificates were not independently reverified here. No claim is made about the volume law away from the upper endpoint, about other numbers of points, or about an independent review. The comparison with indexed literature and accessible manuscripts cannot rule out an older equivalent local tube-asymptotic treatment; determining historical priority requires further scholarly scrutiny.

## References
[1] C. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1 (first posted 2026-10-12), especially Corollary 5.2. https://arxiv.org/abs/2610.26886

[2] Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v3; Monatshefte für Mathematik **181** (2016), 341–354. https://arxiv.org/abs/1402.6496

[3] A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783v1, particularly Sections 5 and 7. https://arxiv.org/abs/2007.07783
