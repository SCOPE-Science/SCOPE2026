# Diophantine Stability of Isoptic-Chord Rigidity

## Finding

Let \(K\subset\mathbb R^2\) be a \(C^2\) strictly convex body with support function \(p\), and fix \(0<\alpha<\pi\). Define the isoptic-chord function
\[
c_\alpha(t)=\frac{p(t)+p(t-2\alpha)+2\cos\alpha\,p(t+\pi-\alpha)}{\sin\alpha}.
\]
Suppose \(\theta=\alpha/\pi\) is badly approximable, with
\[
\kappa(\theta)=\inf_{q\ge1}q\|q\theta\|_{\mathbb R/\mathbb Z}>0,
\qquad
\eta_\alpha=\sin\!\left(\frac12\min\{\alpha,\pi-\alpha\}\right).
\]
Writing \(\hat p_n\) for the Fourier coefficients and \(p_{\ge2}(t)=\sum_{|n|\ge2}\hat p_n e^{int}\), use the normalized \(L^2(\mathbb T)\) norm and the Sobolev norm
\[
\|f\|_{H^{-1}}^2=\sum_{n\in\mathbb Z}(1+n^2)^{-1}|\hat f_n|^2.
\]
Then
\[
\boxed{\ \|p_{\ge2}\|_{H^{-1}}\le
\frac{\sin\alpha}{2\kappa(\theta)\eta_\alpha}
\|c_\alpha-\bar c_\alpha\|_{L^2}\ }.
\]
Here \(\bar c_\alpha\) is the mean of \(c_\alpha\). The one-derivative loss is sharp: for every \(s<1\), no constant depending only on \(\alpha\) can replace \(H^{-1}\) by \(H^{-s}\) on the left for all smooth strictly convex bodies.

## Assumptions and scope

The support function is \(2\pi\)-periodic. The isoptic-chord function is the length between the two corresponding points of the \(\alpha\)-isoptic used in Jerónimo-Castro, Jimenez-Lopez, and Morales-Amaya; its support-function formula is displayed above. The arithmetic hypothesis is the explicit bad-approximability condition \(\kappa(\alpha/\pi)>0\). The estimate controls the shape modes \(n\ge2\) after removing the constant mode (radius) and the first modes (translation). It is not a Hausdorff- or \(L^2\)-stability statement.

## Proof

For the Fourier basis \(e^{int}\), shifting the argument in the displayed definition gives
\[
\widehat{c_\alpha}_n=m_n\hat p_n,\qquad
m_n=\frac{2e^{-in\alpha}}{\sin\alpha}
\bigl(\cos(n\alpha)+(-1)^n\cos\alpha\bigr).
\]
Thus \(m_1=0\), and the constant coefficient only contributes to \(\bar c_\alpha\). For \(n=2k+1\ge3\),
\[
|m_n|=\frac4{\sin\alpha}
|\sin(k\alpha)\sin((k+1)\alpha)|,
\]
whereas for \(n=2k\ge2\),
\[
|m_n|=\frac4{\sin\alpha}
\left|\cos\!\left(\frac{(n+1)\alpha}{2}\right)
\cos\!\left(\frac{(n-1)\alpha}{2}\right)\right|.
\]

Put \(\delta=\min\{\alpha,\pi-\alpha\}\), so \(\eta_\alpha=\sin(\delta/2)>0\). The zero sets of the two sine factors (and likewise of the two cosine factors) are separated modulo \(\pi\) by \(\delta\); hence the larger absolute factor in either adjacent pair is at least \(\eta_\alpha\). Bad approximability gives, for every integer \(q\ge1\),
\[
|\sin(q\alpha)|=|\sin(\pi q\theta)|\ge2\|q\theta\|\ge\frac{2\kappa(\theta)}q.
\]
For odd \(j\), the distance from \(j\theta\) to every odd integer is at least \(\|j\theta\|\ge\kappa(\theta)/j\); consequently
\[
|\cos(j\alpha/2)|\ge\frac{\kappa(\theta)}j.
\]
Using the smaller factor's lower bound and the larger factor's \(\eta_\alpha\) bound in each parity case yields, for every \(n\ge2\),
\[
|m_n|\ge\frac{2\kappa(\theta)\eta_\alpha}{n\sin\alpha}.
\]
Since \((1+n^2)^{-1/2}\le n^{-1}\), coefficientwise comparison and Parseval's identity give the boxed inequality.

To prove sharpness, choose infinitely many convergent denominators \(q_j\) of \(\theta\), for which \(\|q_j\theta\|\le1/q_j\), and set \(n_j=2q_j+1\). The odd-mode factorization gives
\[
|m_{n_j}|=\frac4{\sin\alpha}
|\sin(q_j\alpha)\sin((q_j+1)\alpha)|
\le\frac{4\pi}{q_j\sin\alpha}=O_\alpha(n_j^{-1}).
\]
Fix \(R>0\), and let
\[
p_j(t)=R+\varepsilon_j\cos(n_jt),\qquad
\varepsilon_j=\frac{R}{2(n_j^2-1)}.
\]
Then \(p_j+p_j''=R-\frac R2\cos(n_jt)\ge R/2>0\), so \(p_j\) is the support function of a smooth strictly convex body. Its nonconstant shape part has \(H^{-s}\) norm comparable to \(\varepsilon_j n_j^{-s}\), while its chord-length defect has \(L^2\) norm at most a constant times \(\varepsilon_j/n_j\). Their ratio therefore grows at least as \(n_j^{1-s}\), which diverges for every \(s<1\). No uniform stronger Sobolev estimate of that form is possible.

## Verification

The shift multiplier was derived directly on each Fourier mode. The lower bound treats even and odd frequencies separately and uses the stated Diophantine constant at every frequency, not a finite truncation. The sharpness sequence consists of actual support functions with strictly positive radius of curvature. The argument is analytic; no numerical experiment or finite enumeration is used.

## Relationship to prior work

Jerónimo-Castro, Jimenez-Lopez, and Morales-Amaya give the same support-function formula and prove qualitative disk rigidity when \(\alpha/\pi\) is irrational; their Fourier analysis also identifies the exact resonant modes. The present statement adds a quantitative lower bound on nonzero multipliers under bad approximability, an \(H^{-1}\)-to-\(L^2\) stability estimate, and sharpness of the derivative loss. The result does not assert stability in a stronger support-function norm.

## Limitations

The constant depends on \(\kappa(\alpha/\pi)\) and degenerates as this Diophantine constant tends to zero. The theorem does not provide a uniform estimate for all irrational angles, nor does it imply Hausdorff, \(L^\infty\), or \(L^2\) control of the support-function shape. It treats the stated isoptic-chord function and does not extend automatically to other chord or section transforms.

## References

J. Jerónimo-Castro, F. G. Jimenez-Lopez, and E. Morales-Amaya, “Some results about equichordal convex bodies,” arXiv:2108.12753v1 (first public 2021-08-29); *Discrete & Computational Geometry* 70 (2023), 1741–1750. DOI: 10.1007/s00454-023-00543-8.
