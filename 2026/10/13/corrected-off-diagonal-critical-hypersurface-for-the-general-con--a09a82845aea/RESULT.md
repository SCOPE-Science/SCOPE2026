# Corrected off-diagonal critical hypersurface for the general-contact Smilansky–Solomyak model
## Finding
For the general-contact Hamiltonian \(H_{\alpha,\beta,\gamma}\) introduced by Exner and Lipovský, assume \(\beta>0\) and put \(g=|\gamma|^2\). Their reduction gives
\[
\mu_1=\frac{2\sqrt2\,\beta}{4+\alpha\beta+g-\Delta},\qquad
\mu_2=\frac{2\sqrt2\,\beta}{4+\alpha\beta+g+\Delta},
\]
where
\[
\Delta=\sqrt{(\alpha\beta+g-4)^2+16g}.
\]
For \(\beta\ne2\sqrt2\), the unique finite critical value relevant to Theorem 7.3 is
\[
\boxed{\alpha_c(\beta,g)=\frac{2\beta-\sqrt2\,(g+4)}{\sqrt2\,\beta-4}}.
\]
If \(0<\beta<2\sqrt2\), then \(\mu_1(\alpha_c)=1\). If \(\beta>2\sqrt2\), then \(\mu_2(\alpha_c)=1\). Moreover,
\[
\left.\frac{d}{d\alpha}\mu_j^{-1}\right|_{\alpha=\alpha_c}
=\frac{1}{\sqrt2}\,
\frac{(\beta-2\sqrt2)^2}{(\beta-2\sqrt2)^2+2g}>0,
\]
for the selected channel \(j\), so \(\alpha\uparrow\alpha_c\) implies \(\mu_j\downarrow1\) from above.

The open preprint and the independent mp_arc copy print instead
\[
\widehat\alpha=\frac1\beta\left[
\frac{g}{2\sqrt2(2\sqrt2-\beta)}-(g-4)-\sqrt2(2\sqrt2-\beta)
\right]
\]
in Theorem 7.3(i)–(ii). Direct simplification gives
\[
\boxed{\widehat\alpha-\alpha_c=
\frac{7g}{2\beta(\sqrt2\,\beta-4)}}.
\]
Thus the displayed center is correct on the no-mixing slice \(g=0\), but it misses the transition for every \(g>0\) and \(\beta\ne2\sqrt2\). For example, at \(\beta=1\) and \(g=1\), the printed value is approximately \(0.6075783325\), whereas the exact crossing is approximately \(1.9611317231\); at the printed value \(\mu_1\approx2.9876342512\), not \(1\).

At \(\beta=2\sqrt2\), the squared crossing equation reduces to \(g=0\). Hence for \(g>0\) there is no finite \(\alpha\) with either Jacobi parameter equal to \(1\). For \(g=0\), one channel is identically equal to \(1\), and the other crosses at \(\alpha=\sqrt2\).

## Assumptions and scope
The statement concerns the four-real-parameter contact interaction of arXiv:2207.03713v1, with \(\beta>0\), using the source's Jacobi parameters \(\mu_1\) and \(\mu_2\). The correction is to the explicit \(\alpha\)-location in parts (i) and (ii) of Theorem 7.3 in the inspected open version. It does not change Theorems 6.2–6.3, which characterize the transition implicitly through \(\mu_j=1\), and it does not re-prove the Jacobi eigenvalue-count asymptotic used downstream by the source.

The case \(\beta=0\) is governed by the separate formula in Theorem 6.3 and is outside this claim. The singular line \(\beta=2\sqrt2\) is treated separately above. No claim is made about a silently corrected publisher version that was not available as full text in the inspected public sources.

## Proof
Write
\[
r_1=\mu_1^{-1}=\frac{4+\alpha\beta+g-\Delta}{2\sqrt2\,\beta},\qquad
r_2=\mu_2^{-1}=\frac{4+\alpha\beta+g+\Delta}{2\sqrt2\,\beta}.
\]
A crossing \(r_j=1\) forces
\[
\Delta=\left|4+\alpha\beta+g-2\sqrt2\,\beta\right|.
\]
Squaring this identity and subtracting the defining expression for \(\Delta^2\) gives
\[
(4+\alpha\beta+g-2\sqrt2\,\beta)^2-igl((\alpha\beta+g-4)^2+16g\bigr)
\]
\[
=-4\beta\bigl(\sqrt2\,\alpha\beta-4\alpha-2\beta+\sqrt2 g+4\sqrt2\bigr).
\]
Because \(\beta>0\), and because \(\beta\ne2\sqrt2\), the unique solution is
\[
\alpha=\alpha_c(\beta,g)=\frac{2\beta-\sqrt2(g+4)}{\sqrt2\beta-4}.
\]
At this value,
\[
S:=4+\alpha_c\beta+g-2\sqrt2\beta
=-\frac{2\bigl((\beta-2\sqrt2)^2+2g\bigr)}{\sqrt2\beta-4}.
\]
Hence \(S>0\) when \(0<\beta<2\sqrt2\), so \(\Delta=S\) and \(r_1=1\). When \(\beta>2\sqrt2\), \(S<0\), so \(\Delta=-S\) and \(r_2=1\). This also removes the possible extraneous root introduced by squaring and proves uniqueness of the finite crossing in each regime.

Differentiating the appropriate reciprocal parameter at the crossing gives
\[
\left.\frac{dr_j}{d\alpha}\right|_{\alpha_c}
=\frac{1}{\sqrt2}\,
\frac{(\beta-2\sqrt2)^2}{(\beta-2\sqrt2)^2+2g}>0.
\]
Therefore, with \(\delta=\alpha_c-\alpha>0\),
\[
r_j=1-c\delta+O(\delta^2),\qquad
\mu_j=1+c\delta+O(\delta^2),
\]
where \(c>0\) is the displayed derivative. Thus the left-hand approach is indeed the supercritical side \(\mu_j>1\).

Finally, algebraic reduction of the value printed in Theorem 7.3 gives
\[
\widehat\alpha-\alpha_c=\frac{7g}{2\beta(\sqrt2\beta-4)}.
\]
For \(g>0\) and \(\beta\ne2\sqrt2\), this is nonzero, so the printed point cannot satisfy the selected equation \(\mu_j=1\). If \(\beta=2\sqrt2\), the squared crossing identity above becomes a nonzero multiple of \(g\); hence no finite crossing exists when \(g>0\). If \(g=0\), direct substitution into the source formulas yields one parameter identically equal to \(1\) and the other equal to \(\sqrt2/\alpha\), with equality at \(\alpha=\sqrt2\).

## Verification
The exact derivation above uses only equations (4.6a)–(4.6b) from the primary source. The standalone script `verify.py` evaluates the original radical formulas at representative points on both sides of \(2\sqrt2\), checks the corrected root, checks the exact difference from the printed center numerically at high precision, verifies the left-hand direction, and checks the singular-line behavior. These calculations corroborate the algebra; the all-parameter statement follows from the symbolic identities in the proof, not from finite sampling.

## Relationship to prior work
The primary source, arXiv:2207.03713v1, correctly gives the two Jacobi parameters in equations (4.6a)–(4.6b), and Theorems 6.2–6.3 correctly locate the spectral transition implicitly at \(\mu_j=1\). Theorem 7.3 then gives an explicit \(\alpha\)-limit intended to make \(\mu_1\to1^+\) for \(0<\beta\le2\sqrt2\) and \(\mu_2\to1^+\) for \(\beta\ge2\sqrt2\). The same displayed expression appears in the independent mp_arc copy. The calculation here shows that expression agrees with the true crossing only when \(g=0\).

A prior result on the diagonal slice \(\gamma=0\) already simplifies the two channels to the unordered pair \(\{\sqrt2/\alpha,\beta/(2\sqrt2)\}\). That special case is consistent with the present formula because \(\alpha_c(\beta,0)=\sqrt2\) whenever \(\beta\ne2\sqrt2\). It does not imply the present off-diagonal correction: the discrepancy is exactly proportional to \(|\gamma|^2\) and vanishes on that earlier slice.

Targeted searches for the source identifier, theorem number, an erratum, the corrected rational expression, and equivalent \(\mu_j=1\) formulations found no published correction. The publisher chapter was located bibliographically, but a statement-level full text was not used; a silent correction there therefore remains a residual literature risk.

## Limitations
This finding corrects the explicit critical \(\alpha\)-location in the inspected open version; it does not challenge the source's implicit \(\mu_j=1\) criterion or independently re-prove the deep Jacobi spectral asymptotics cited by that paper. It does not classify every spectral region of the full parameter space, and it makes no assertion about corrections that might exist in inaccessible or weakly indexed later versions.

## References
1. P. Exner and J. Lipovský, *Spectral transition model with the general contact interaction*, arXiv:2207.03713v1 (2022), especially equations (4.6a)–(4.6b), Theorems 6.2–6.3, and Theorem 7.3.
2. P. Exner and J. Lipovský, *Spectral transition model with the general contact interaction*, mp_arc 22-34 (2022), independent public copy of the preprint.
3. P. Exner and J. Lipovský, *Spectral Transition Model with the General Contact Interaction*, in *From Complex Analysis to Operator Theory: A Panorama* (2023), DOI:10.1007/978-3-031-31139-0_19. Bibliographic metadata only was used for the published chapter.
