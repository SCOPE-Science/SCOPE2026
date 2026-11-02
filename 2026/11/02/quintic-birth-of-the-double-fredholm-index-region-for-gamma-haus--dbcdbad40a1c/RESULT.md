# Quintic birth of the double-Fredholm-index region for Gamma Hausdorff operators

## Finding
For \(s>1\) and \(\alpha>0\), consider the Gamma Hausdorff operator \(\Gamma_s^\alpha\), defined on either complex BMOA or the Bloch space by the Hausdorff moment measure
\[
d\mu_{\alpha,s}(t)=\frac{s^\alpha}{\Gamma(\alpha)}t^{s-1}(\log(1/t))^{\alpha-1}\,dt,\qquad 0<t<1.
\]
For \(\lambda\) outside the Fredholm essential spectrum define \(\nu_{\alpha,s}(\lambda)=-\operatorname{Ind}(\lambda I-\Gamma_s^\alpha)\). Let \(E_{2}(\alpha,s)\) be the open subset of the complex plane on which this number equals \(2\), and write \(R=s/(s-1)\). For every \(0<\alpha\leq2\), \(E_2(\alpha,s)=\varnothing\). For every \(2<\alpha<4\), with \(\theta_0=\pi(2-\alpha/2)\),
\[
E_2(\alpha,s)=\left\{r e^{i\theta}:\ \theta_0<|\theta|\leq\pi,\quad 0<r<R^\alpha\cos^\alpha\!\left(\frac{2\pi-|\theta|}{\alpha}\right)\right\},
\]
where the negative real ray is included by taking either angular endpoint \(\theta=\pi\) or \(\theta=-\pi\), except at the essential-spectrum crossing. Its exact Euclidean area is
\[
\boxed{\operatorname{Area}(E_2(\alpha,s))=\alpha R^{2\alpha}\int_{\pi/\alpha}^{\pi/2}\cos^{2\alpha}u\,du.}
\]
In particular,
\[
\boxed{\operatorname{Area}(E_2(3,s))=\frac{5\pi-9\sqrt3}{32}\left(\frac{s}{s-1}\right)^6,}
\]
and the first double-index region emerges with the sharp fifth-order law
\[
\boxed{\lim_{\alpha\downarrow2}\frac{\operatorname{Area}(E_2(\alpha,s))}{(\alpha-2)^5}=\frac{\pi^5}{2560}\left(\frac{s}{s-1}\right)^4.}
\]
The statement and constants are identical on BMOA and on the Bloch space.

## Assumptions and scope
The operator is the analytic-function Hausdorff matrix associated with the indicated finite positive measure, as in Galanopoulos–Mahillo–Oliva-Maza–Siskakis (2026). The parameter \(s>1\) is fixed. The exact area formula concerns \(2<\alpha<4\), whereas the absence of a double-index region is proved for \(0<\alpha\leq2\). The index is defined only off the Fredholm essential spectrum; that spectral curve has planar measure zero. All areas are unnormalized two-dimensional Lebesgue areas on the complex plane. The first-public source date for the motivating paper is 2026-10-15.

## Proof
**Step 1: spectral-index reduction.** The published Gamma-operator spectral theorem gives
\[
\sigma_{\rm ess}(\Gamma_s^\alpha)=\left\{(s/(s-1+iy))^\alpha:y\in\mathbb R\right\}\cup\{0\}
\]
and states that for \(\lambda\) outside this set the operator \(\lambda I-\Gamma_s^\alpha\) is injective, with range codimension equal to the number of solutions, with multiplicities, of
\[
(s/(s-1+z))^\alpha=\lambda,\qquad\operatorname{Re}z>0.
\]
All such roots are simple because the derivative of the transform is nonzero. Thus \(\nu_{\alpha,s}(\lambda)\) is the number of these preimages.

**Step 2: a tangent disk.** Set \(w=s/(s-1+z)\). Directly solving the half-plane inequality gives
\[
\operatorname{Re}z>0\quad\Longleftrightarrow\quad |w-R/2|<R/2,\qquad R=\frac{s}{s-1}.
\]
In polar coordinates this disk is \(-\pi/2<\phi<\pi/2\) and \(0<|w|<R\cos\phi\). On it the Mellin function is \(w^\alpha=\exp(\alpha\operatorname{Log}w)\) with the principal branch.

**Step 3: exact multiplicity and boundary.** Write \(\lambda=r e^{i\theta}\) with \(-\pi\leq\theta\leq\pi\) and \(r>0\). Its admissible preimage arguments are precisely
\[
\phi_k=\frac{\theta+2\pi k}{\alpha},\qquad k\in\mathbb Z,
\]
for which \(|\phi_k|<\pi/2\) and \(r^{1/\alpha}<R\cos\phi_k\). When \(0<\alpha\leq2\), the angular interval of length \(\alpha\pi\leq2\pi\) admits at most one branch. For \(2<\alpha<4\), the branch \(k=0\) is always admissible in angle and at most one further branch occurs. When \(\theta>0\), it is \(k=-1\), and exists exactly if \(\theta>\theta_0=\pi(2-\alpha/2)\); for negative \(\theta\) it is \(k=1\). For \(\theta_0<\theta\leq\pi\), the smaller radial cap is that of the second branch, because \((2\pi-\theta)/\alpha\geq\theta/\alpha\) and the cosine decreases on \([0,\pi/2]\). This proves the asserted polar description, with the two angular endpoints identified on the negative real ray. The essential-spectrum curve is a finite-length curve: its derivative decays as \(O(|y|^{-\alpha-1})\) for large \(|y|\), so its planar area is zero.

**Step 4: area.** Integrate the area element \(r\,dr\,d\theta\) over the two symmetric angular sectors. The two factors of two (angular symmetry and radial antiderivative) cancel, giving
\[
\operatorname{Area}(E_2)=R^{2\alpha}\int_{\theta_0}^{\pi}\cos^{2\alpha}\!\left(\frac{2\pi-\theta}{\alpha}\right)d\theta=\alpha R^{2\alpha}\int_{\pi/\alpha}^{\pi/2}\cos^{2\alpha}u\,du.
\]
For \(\alpha=3\), use \(\cos^6u=(10+15\cos2u+6\cos4u+\cos6u)/32\); integrating from \(\pi/3\) to \(\pi/2\) gives \((5\pi-9\sqrt3)/96\), and multiplication by \(3R^6\) proves the exact constant.

**Step 5: sharp birth rate.** Put \(\varepsilon=\alpha-2\) and \(\delta=\pi/2-\pi/\alpha=\pi\varepsilon/(2\alpha)\). Substitution \(v=\pi/2-u\) yields
\[
\operatorname{Area}(E_2)=\alpha R^{2\alpha}\int_0^\delta\sin^{2\alpha}v\,dv.
\]
Uniformly as \(\alpha\downarrow2\), \(\sin v/v\to1\) on \([0,\delta]\), so the integral is \((1+o(1))\delta^{2\alpha+1}/(2\alpha+1)\). Since \(\varepsilon^{2\varepsilon}\to1\), dividing by \(\varepsilon^5\) yields \((2/5)R^4(\pi/4)^5=\pi^5R^4/2560\). This proves the fifth-order law without extrapolating finite sampling.

## Verification
The included `verification.py` independently checks representative root multiplicities against polar sector caps, verifies the elementary order-three area constant against numerical quadrature, and checks convergence toward the fifth-order coefficient. Those finite checks corroborate, but do not replace, the geometric argument and the source's spectral-index theorem. The exact trigonometric identity and limiting normalization are established above.

## Relationship to prior work
Galanopoulos, Mahillo, Oliva-Maza and Siskakis determine the spectrum, Fredholm essential spectrum and root-count formula on BMOA and the Bloch space, including for Gamma operators. The present contribution is the explicit planar region of nonminimal Fredholm defect, its exact area for an entire open interval of Gamma orders, and its precise fifth-order onset at the threshold; these quantitative statements are not given in that paper. The 2024 work of Abadias and Oliva-Maza provides broader background on spectral sets of subordinated Hausdorff matrices on other analytic spaces. These antecedents provide the essential spectral reduction but do not themselves evaluate the stated area integral or asymptotic coefficient.

## Limitations
Only the first index-overlap transition is addressed. At orders \(\alpha\geq4\), more angular branches can occur and this formula does not purport to classify their higher-index regions. The result does not compute resolvent norms, eigenfunctions or individual spectral points beyond the pre-existing characterization. The conclusion relies on the published spectral-index theorem; no independent validation of that theorem or of publication priority has been performed. Older treatments of power maps of tangent disks might contain related geometric area evaluations under different terminology.

## References
- P. Galanopoulos, A. Mahillo, J. Oliva-Maza, A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1 (first publicly submitted 2026-10-15), especially Theorems 1.1–1.2 and Section 5.1.
- L. Abadias and J. Oliva-Maza, *Spectral sets of generalized Hausdorff matrices on spaces of holomorphic functions on the unit disk*, Journal of Functional Analysis 286 (2024), 110298, DOI:10.1016/j.jfa.2023.110298.
