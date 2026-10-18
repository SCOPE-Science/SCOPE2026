# Sharp Heisenberg short-time Fourier Lieb and entropy constants via an exact Gaussian contraction law

## Finding

Fix any integer \(n\geq1\), and set \(d=2n+1\). With the Heisenberg short-time Fourier transform defined below, the optimal constant in the Lieb inequality, for every real \(p>2\), is exactly
\[
\sup_{f,g\ne0}\frac{\|V_gf\|_{L^p(\mathbb H^n\times\mathbb H^n)}^p}{\|f\|_2^p\|g\|_2^p}=\left(\frac2p\right)^d.
\]
This supremum is not attained by any pair of nonzero functions. Correspondingly, the optimal lower bound on the Shannon entropy of a normalized Heisenberg short-time Fourier spectrogram is exactly \(d\), understood as an infimum (no assertion of global entropy nonattainment).

More quantitatively, consider the normalized anisotropic Gaussian family specified below. Its complete \(p\)-moment is
\[
\boxed{\quad
I_{n,p}(\epsilon)=\left(\frac2p\right)^d
\frac1{\Gamma(n)}\int_0^\infty y^{n-1}e^{-y}
\left(1+\frac{\epsilon^2y}{8\pi p}\right)^{1-p/2}\,dy.\quad}
\]
For every \(\epsilon>0\) this is strictly below the optimal constant if \(p>2\), and increases to that constant as \(\epsilon\downarrow0\). The exact leading deficit is
\[
\left(\frac2p\right)^d-I_{n,p}(\epsilon)
=\left(\frac2p\right)^d\left(\frac{n(p-2)}{16\pi p}\epsilon^2+O_{n,p}(\epsilon^4)\right).
\]
For its normalized spectrogram the entropy is exactly
\[
\boxed{\quad H_n(\epsilon)=d+\frac1{\Gamma(n)}\int_0^\infty
 y^{n-1}e^{-y}\log\left(1+\frac{\epsilon^2y}{16\pi}\right)\,dy,\quad}
\]
and its entropy excess is \(n\epsilon^2/(16\pi)+O_n(\epsilon^4)\). Both formulas hold in every Heisenberg dimension.

## Assumptions and scope

Identify \(\mathbb H^n\) with \(\mathbb R^{2n}\times\mathbb R\) and equip it with Lebesgue/Haar measure and the product
\[
(u,t)\cdot(v,c)=(u+v,t+c+\tfrac12\sigma(u,v)),\qquad
\sigma(u,v)=u_p\cdot v_q-u_q\cdot v_p,
\]
where \(u=(u_p,u_q)\) and \(v=(v_p,v_q)\). Use the unitary Euclidean Fourier transform with phase \(e^{-2\pi i X\cdot\xi}\), and define the Heisenberg STFT by
\[
V_gf(Q,P)=\int_{\mathbb R^d}\widehat f(X)
\overline{e^{2\pi i Q\cdot X}\widehat g(X\cdot P)}\,dX.
\]
The two integration variables \(Q,P\) range over \(\mathbb H^n\), identified with \(\mathbb R^d\). For every \(\epsilon>0\), choose \(f_\epsilon=g_\epsilon\) so that
\[
\widehat f_\epsilon(u,t)=\widehat g_\epsilon(u,t)=
 2^{d/4}\epsilon^{1/2}e^{-\pi(|u|^2+\epsilon^2t^2)}.
\]
These functions are Schwartz and satisfy \(\|f_\epsilon\|_2=\|g_\epsilon\|_2=1\). Set \(I_{n,p}(\epsilon)=\iint|V_{g_\epsilon}f_\epsilon|^p\,dQ\,dP\) for real \(p\ge2\), and \(H_n(\epsilon)=-\iint |V_{g_\epsilon}f_\epsilon|^2\log|V_{g_\epsilon}f_\epsilon|^2\,dQ\,dP\), adopting the continuous extension at zero.

## Proof

**Step 1: remove the central Gaussian anisotropy from the integration measure.** Introduce \(x=(u,s)=(u,\epsilon t)\), write a translation as \(P=(v,c/\epsilon)\), and rescale the central modulation as \(Q=(w,\epsilon\eta)\). The Jacobians in the two phase-space variables cancel. Then
\[
V_{g_\epsilon}f_\epsilon(Q,P)=2^{d/2}\int_{\mathbb R^d}
 e^{-\pi(|x|^2+|L_vx+b|^2)}e^{-2\pi i (w,\eta)\cdot x}\,dx,
\]
where \(b=(v,c)\) and \(L_v(u,s)=(u,s+\epsilon\sigma(u,v)/2)\). In particular \(\sigma(v,v)=0\).

**Step 2: compute the Gaussian Hessian and its completed square.** Let \(j(v)\in\mathbb R^{2n}\) be defined by \(u\cdot j(v)=\sigma(u,v)\), so \(j(v)\cdot v=0\) and \(|j(v)|=|v|\). Set \(z=\epsilon j(v)/2\). The Hessian of \(|x|^2+|L_vx+b|^2\) is
\[
M=I+L_v^{\mathsf T}L_v=
\begin{pmatrix}2I_{2n}+zz^{\mathsf T}&z\\z^{\mathsf T}&2\end{pmatrix}.
\]
A Schur complement and \(z\cdot v=0\) yield, exactly,
\[
\det M=2^d\mathcal H(v),\qquad
\mathcal H(v)=1+\frac{\epsilon^2|v|^2}{16},\qquad
\min_x(|x|^2+|L_vx+b|^2)=\frac{|v|^2}{2}+\frac{c^2}{2\mathcal H(v)}.
\]
The third identity may equivalently be obtained from \(b^{\mathsf T}(I+L_vL_v^{\mathsf T})^{-1}b\). All matrices are positive definite for every \(v,c,\epsilon\), so the Gaussian integrations below are legitimate.

**Step 3: integrate the exact \(p\)-moment.** Taking the absolute value of the Fourier transform of the completed Gaussian and integrating the modulation variable gives
\[
\int_{\mathbb R^d}|V_{g_\epsilon}f_\epsilon(Q,P)|^p\,dQ
=2^{dp/2}p^{-d/2}(\det M)^{(1-p)/2}
\exp\left[-\frac{\pi p|v|^2}{2}-\frac{\pi pc^2}{2\mathcal H(v)}\right].
\]
The central translation integral contributes \(\sqrt{2\mathcal H(v)/p}\), and the horizontal translation integral is reduced by \(y=\pi p|v|^2/2\). Since the radial measure for \(v\in\mathbb R^{2n}\) gives \(y^{n-1}e^{-y}/\Gamma(n)\), this proves
\[
I_{n,p}(\epsilon)=\left(\frac2p\right)^d\mathbb E
\left(1+\frac{\epsilon^2Y}{8\pi p}\right)^{1-p/2},
\qquad Y\sim\operatorname{Gamma}(n,1).
\]
At \(p=2\) the expectation equals one. For \(p>2\) it is strictly between zero and one for each positive \(\epsilon\), strictly decreasing in \(\epsilon\), and converges to one by dominated convergence as \(\epsilon\downarrow0\). Taylor's theorem under the Gamma integral, justified by its finite moments, gives the stated quadratic deficit. This is an identity for the entire noncommutative transform, not an approximation by a Euclidean transform.

**Step 4: establish sharpness and absence of equality.** Dabra–Dasgupta–Gulia prove the universal upper bound \(I_{n,p}(f,g)\le(2/p)^d\|f\|_2^p\|g\|_2^p\) for every \(p>2\) and all \(f,g\in L^2(\mathbb H^n)\), using Hausdorff–Young and sharp convolution Young inequalities. Step 3 supplies unit-norm Schwartz examples arbitrarily close to that bound, establishing its exact best constant. Their proof contains a sharp Young-convolution step on \(\mathbb H^n\) at three interior exponents; equality in the STFT bound would force equality in that step for the nonzero pair \(\lvert\widehat f\rvert^{p'}\), \(\lvert\widehat g\rvert^{p'}\). Christ's Heisenberg Young theorem establishes that no nonzero such convolution extremizers exist. Hence the best STFT constant is not attained. This nonattainment conclusion is for \(p>2\), not for the \(p=2\) orthogonality identity.

**Step 5: determine the entropy and its sharp infimum.** For the normalized family, \(I_{n,2}(\epsilon)=1\). Gaussian decay and the explicit moment formula justify differentiation at \(p=2\):
\[
H_n(\epsilon)=-2\left.\frac{\partial I_{n,p}(\epsilon)}{\partial p}\right|_{p=2}
=d+\mathbb E\log\left(1+\frac{\epsilon^2Y}{16\pi}\right).
\]
Taylor expansion again gives the entropy excess. Dabra–Dasgupta–Gulia establish the lower bound \(H\ge d\) for every unit-norm signal and window. The preceding identity tends to \(d\) as \(\epsilon\downarrow0\), proving the lower bound optimal. The family itself never attains the lower bound for positive \(\epsilon\); possible global entropy equality is not considered.

## Verification

The accompanying standalone program `verify.py` directly constructs \(M\) in dimensions \(d=3,5,7,9,11\) and independently checks the determinant and completed-square identities at 125 randomly chosen parameter triples. It checks the Gamma moment and its monotonicity in 20 configurations, the quadratic coefficient in three, and obtains four entropy values by two-sided numerical differentiation of the independent \(p\)-moment integral. All checks passed. They are finite consistency tests; the mathematical proof uses the preceding algebra, Gaussian integrals, dominated convergence, and the two cited sharp inequalities.

## Relationship to prior work

Dabra–Dasgupta–Gulia (2026), Theorem 5.1 and Theorem 6.2, establish the universal Lieb and entropy inequalities for the Heisenberg-group STFT in this normalization. Their Remark 5.2 explicitly notes that the lack of Young extremizers leaves **sharpness of the Lieb bound unresolved by their proof**. The present Gaussian contraction computation supplies a saturating sequence, determines its exact deficit, and simultaneously establishes the sharp entropy infimum. Christ (2017), particularly Section 5, supplies the nonattainment of sharp Young convolution on nonabelian Heisenberg groups; no nonattainment of Young is claimed as a new result. More generally, Euclidean Lieb-type Gaussian sharpness does not by itself imply sharpness for a genuinely noncommutative translation law: the central Gaussian scale in the present calculation is essential.

## Limitations

The sharp constant and nonattainment conclusions cover the specified Heisenberg STFT, all \(n\ge1\), and all real \(p>2\). The exact finite-\(\epsilon\) and entropy-defect formulas concern this particular normalized Gaussian family, not arbitrary near extremizers; they do not classify all sequences saturating the inequality. No reverse inequality at \(p<2\), quantitative global stability inequality, or global nonattainment of entropy is claimed. Historical priority may be affected by equivalent unindexed work; the mathematical identity is self-contained subject to the cited sharp upper inequalities.

## References

1. A. Dabra, A. Dasgupta, P. Gulia, *Uncertainty Principles for the Short-Time Fourier Transform on the Heisenberg Group*, arXiv:2608.20952v1 (first public version, 21 August 2026), especially Sections 2, 5, 6, Theorem 5.1, Remark 5.2 and Theorem 6.2. https://arxiv.org/pdf/2608.20952
2. M. Christ, *On Young's Convolution Inequality for Heisenberg Groups*, arXiv:1706.02005v1 (2017), especially Section 5 on the optimal constant and nonexistence of extremizers. https://arxiv.org/pdf/1706.02005
