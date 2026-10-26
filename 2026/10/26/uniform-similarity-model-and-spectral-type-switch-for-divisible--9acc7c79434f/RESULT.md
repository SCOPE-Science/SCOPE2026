# Uniform similarity model and spectral-type switch for divisible monomial composition products

## Finding
Let \(\alpha>-1\) and let \(m,n\ge2\) be **distinct** positive integers such that one divides the other. Write \(T_{m,n}=C_{z^m}C_{z^n}^{*}\) on the power-weighted Bergman space \(A^2_\alpha(\mathbb D)\). Set
\[
 c=(mn)^{-(\alpha+1)/2},\qquad t=\max\{m,n\}/\min\{m,n\}\ge2.
\]
There exists a bounded invertible diagonal operator with bounded inverse, in the normalized monomial basis, which gives the **exact canonical similarities**
\[
 T_{m,n}\sim
 \begin{cases}
  I_{\mathbb C}\oplus\big(c S^*\otimes I_{\ell^2}\big)\oplus0_{\ell^2},&m\mid n,\\
  I_{\mathbb C}\oplus\big(c S\otimes I_{\ell^2}\big)\oplus0_{\ell^2},&n\mid m,
 \end{cases}
\]
where \(S\) is the unilateral forward shift on \(\ell^2(\mathbb N_0)\). The two infinite-multiplicity shift models are not similar to each other: their nonzero interior spectral types differ.

In both orientations, the ordinary spectrum and Fredholm essential spectrum are respectively
\[
 \sigma(T_{m,n})=\{1\}\cup\{\lambda\in\mathbb C:|\lambda|\le c\},\qquad
 \sigma_{\rm ess}(T_{m,n})=\{\lambda\in\mathbb C:|\lambda|\le c\}.
\]
The eigenvalue \(1\) is isolated and simple; \(0\) is an eigenvalue with infinite multiplicity. Each \(\lambda\) with \(0<|\lambda|<c\) is (i) an eigenvalue of infinite multiplicity when \(m\mid n\), and (ii) in the residual spectrum, with infinite-dimensional orthogonal complement to the range closure, when \(n\mid m\). Every \(\lambda\) with \(|\lambda|=c\) belongs to the continuous spectrum. The essential norm of \(T_{m,n}\) is \(c\).

## Assumptions and scope
The unit disk is \(\mathbb D\). Use normalized area measure \(dA\) and \(\|f\|_\alpha^2=(\alpha+1)\int_\mathbb D|f(z)|^2(1-|z|^2)^\alpha\,dA(z)\). The composition operator is \(C_{z^q}f(z)=f(z^q)\), and the adjoint is Hilbert-space adjoint. The result concerns integers \(m,n\ge2\) with \(m\ne n\) and either \(m\mid n\) or \(n\mid m\); it does not claim the diagonal case or unrelated symbols. The Fredholm essential spectrum is the set where the shifted operator is not Fredholm. Continuous spectrum means injective, dense non-surjective range; residual spectrum means injective, nondense range.

## Proof
**1. Exact coefficient representation.** Put
\[
 s_k^2=\frac{\Gamma(\alpha+2)\Gamma(k+1)}{\Gamma(k+\alpha+2)},\qquad
 e_k(z)=z^k/s_k\quad (k\ge0).
\]
The \(e_k\) form an orthonormal basis. Direct substitution and the adjoint definition give \(C_{z^q}e_k=(s_{qk}/s_k)e_{qk}\); therefore
\[
 T_{m,n}e_{nk}=\beta_k e_{mk},\qquad
 \beta_k=\frac{s_{mk}s_{nk}}{s_k^2}>0\quad(k\ge0),
\]
and \(T_{m,n}e_j=0\) for \(n\nmid j\). Here \(\beta_0=1\), so constants form a reducing one-dimensional identity block. The remaining formula concerns \(k\ge1\). Gamma-ratio asymptotics, valid for every fixed \(\alpha>-1\), yield
\[
 \beta_k=c\big(1+O_{\alpha,m,n}(1/k)\big).
\]
In particular, as all weights are positive, there is a finite constant \(B\) such that
\[
 |\log(\beta_k/c)|\le B/k\quad\text{for all }k\ge1.
\]
The assertion for finitely many small \(k\) is absorbed into \(B\); no unstated positivity of a logarithm is needed.

**2. Exact graph partition.** Suppose first that \(n=mt\), with \(t\ge2\). Every positive multiple of \(m\) has a unique representation \(mh t^j\), with \(j\ge0\) and \(h\ge1\) not divisible by \(t\). For every such \(h\), the mutually orthogonal invariant/reducing chain
\[
 E_h=\overline{\operatorname{span}}\{e_{mht^j}:j\ge0\}
\]
obeys
\[
 T_{m,n}e_{mh}=0,\qquad
 T_{m,n}e_{mht^{j+1}}=\beta_{ht^j}e_{mht^j}.
\]
All positive indices not divisible by \(m\) span an infinite-dimensional zero summand. Thus the nonzero chains are weighted backward shifts. If \(m=nt\), the corresponding decomposition uses \(E_h=\overline{\operatorname{span}}\{e_{nht^j}:j\ge0\}\), and
\[
 T_{m,n}e_{nht^j}=\beta_{ht^j}e_{nht^{j+1}};
\]
the remaining indices not divisible by \(n\) give an infinite zero summand. These are weighted forward shifts. The chain multiplicity is countably infinite because there are infinitely many \(h\) with \(t\nmid h\).

**3. Uniform diagonal conjugacy.** For each \(h\), write \(w_{h,j}=\beta_{ht^j}\). The logarithm estimate gives the bound, **uniform in** \(h\) and chain length \(J\),
\[
 \left|\sum_{j=0}^{J-1}\log\frac{w_{h,j}}c\right|
 \le\frac B h\sum_{j=0}^\infty t^{-j}
 \le\frac{Bt}{t-1}.
\]
For the forward orientation choose diagonal entries \(d_{h,0}=1\) and \(d_{h,J}=\prod_{j<J}(w_{h,j}/c)\). Then on each chain the weighted forward shift is \(D(cS)D^{-1}\). For the backward orientation use the inverse product \(d_{h,J}=\prod_{j<J}(c/w_{h,j})\); the weighted backward shift is \(D(cS^*)D^{-1}\). In either case \(\exp(-Bt/(t-1))\le d_{h,J}\le\exp(Bt/(t-1))\), uniformly in all labels. Taking their orthogonal direct sum and identity on the constant and zero summands produces the claimed **single bounded invertible diagonal similarity**. The diagonal operator and its inverse are defined everywhere by uniform bounds; no formal infinite product is being substituted for an operator.

**4. Spectrum and spectral types.** On \(\ell^2(\mathbb N_0)\), the forward shift has spectrum the closed unit disk, no eigenvalues, nonzero interior residual spectrum (its adjoint has eigenvectors \((1,\overline\lambda,\overline\lambda^2,\ldots)\)), and continuous spectrum on the unit circle. Its adjoint has the conjugate point-spectrum behavior: eigenvalues of the open disk, no residual nonzero interior points, and continuous boundary. A countable infinite orthogonal multiplicity makes each interior eigen/cokernel infinite-dimensional and every point of the closed disk non-Fredholm. The two zero summands remain infinite-dimensional at eigenvalue zero. Similarity preserves spectra, Fredholmness, point spectrum, and density of ranges. Since \(c<1\), the separate identity block contributes only the simple isolated eigenvalue \(1\) outside the disk. For the **essential norm**, which is not preserved by general similarity, use a separate compact-perturbation argument: replace each positive weight \(\beta_k\) on the disjoint index arrows by \(c\), obtaining \(cV\), where \(V\) is the corresponding unit-weight partial isometry with infinitely many orthogonal arrows. The difference is compact because \(\beta_k-c\to0\) and distinct arrows have orthogonal sources and targets; the constant-block discrepancy is rank one. Thus \(\|T_{m,n}\|_{\rm ess}=\|cV\|_{\rm ess}=c\), using infinitely many orthonormal arrows to witness the lower bound. This completes every claimed equivalence and boundary classification.

## Verification
The finite checker `checks/monomial_spectrum_check.py` computes normalized gamma weights, inspects the degree-transition graph, and tests the \(\beta_k/c\to1\) asymptotics in several orientations and weight exponents. The proof of uniform similarity and the infinite-dimensional spectral statements are analytical and do **not** follow from these finite tests. Reproduce with `python checks/monomial_spectrum_check.py` using Python, NumPy and SciPy.

## Relationship to prior work
Leng and Zhao (2026), arXiv:2610.15472v1, study Schatten membership and compactness criteria for such cross-adjoint composition products; their section on Bergman spaces and Theorem 4.11 give a Schatten-class sufficient condition, not the present bounded-similarity classification or the point/residual dichotomy. Earlier work of Clifford and Zheng analyzes compactness of products on Bergman spaces. A separate previous analysis for **distinct coprime** monomial degrees and regularly varying coefficient Hilbert spaces determines a disk spectrum and continuous nonzero spectral type, and is treated as prior input rather than rediscovered here. The present **divisibility hypothesis**, with qualitatively different infinite-ray components and uniform diagonal conjugacy, is disjoint from that coprime parameter regime because distinct divisible integers cannot be coprime when both are at least two. Classical spectral results for unilateral shifts supply the model spectra; the new object-specific step is the explicit uniform similarity for the entire Bergman-product family.

## Limitations
No statement is made about arbitrary analytic symbols, non-power radial weights, or monomial degrees with neither degree dividing the other. Uniform summability of logarithmic weight defects uses the power-weight gamma asymptotic; it need not follow from mere regular variation. Historical priority for equivalent formulations of particular monomial-product similarity operators is not exhaustively certified. The argument is an analytical proof, not independent verification.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (first public 2026-10-11), https://arxiv.org/html/2610.15472v1 , Sections 3–4.
2. C. Clifford and D. Zheng, *Composition operators on Bergman spaces*, 2003, DOI:10.1142/S0252959903000438 (compactness of cross-adjoint products).
3. Z. Čučković and R. Zhao, *Weighted Composition Operators on the Bergman Space*, Journal of the London Mathematical Society 70 (2004), 499–511, DOI:10.1112/S0024610704005605 (weighted composition background, a different operator class).
