# The arcsine Hardy ball inside the pentablock and its critical commutator law

## Finding
Let \(\mathcal P\subset\mathbb C^3\) denote the pentablock in coordinates \((a,s,p)\). Endow its canonical Hardy space \(H^2(\mathcal P)\) with the normalized torus-pushforward boundary measure of Su and Tomar [1]. Put \(b=s/2\) and let \(\mathcal E\) be the closure of polynomials in \((a,b)\) in this Hardy space. The coordinate map \((a,s,p)\mapsto(a,b)\) maps \(\mathcal P\) onto the open Euclidean two-ball \(\mathbb B^2\). The induced norm on \(\mathcal E\) is the holomorphic Hardy norm on \(\mathbb B^2\) for the singular rotationally invariant probability measure
\[
d\nu(z_1,z_2)=\frac{d\sigma(z_1,z_2)}{\pi|z_1z_2|},\qquad |z_1|^2+|z_2|^2=1,
\]
where \(\sigma\) is the normalized surface measure, and the density is interpreted almost everywhere.

For all nonnegative integers \(k,\ell\), the monomials are orthogonal and
\[
\|z_1^kz_2^\ell\|^2=\frac{(1/2)_k(1/2)_\ell}{(k+\ell)!}.
\]
The reproducing kernel of this *two-coordinate subspace* (not the full pentablock Hardy kernel) is
\[
K_{\mathcal E}(z,w)=\sum_{k,\ell\ge0}\frac{(k+\ell)!}{(1/2)_k(1/2)_\ell}(z_1\overline{w_1})^k(z_2\overline{w_2})^\ell
=F_2\!\left(1;1,1;\tfrac12,\tfrac12;z_1\overline{w_1},z_2\overline{w_2}\right),
\]
where \(F_2\) is Appell's two-variable hypergeometric series, defined here by the displayed sum.

Let \(S_1\) and \(S_2\) be the restrictions of multiplication by \(a\) and \(b\) to \(\mathcal E\), and let \(C=[S_1^*,S_1]\). Then \(S_1^*S_1+S_2^*S_2=I\), and \(C\) is positive and compact. Its exact eigenvalue counting law is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^2\#\{\lambda(C)>\varepsilon\}=\frac16.}
\]
Consequently, \(C\) belongs to Schatten class \(\mathcal S_q\) exactly when \(q>2\); furthermore \(C^2\) is measurable in weak trace class and every normalized Dixmier trace of \(C^2\) is \(1/6\).

## Assumptions and scope
The canonical pentablock Hardy space is defined as the closure of coordinate polynomials in \(L^2(b\mathcal P,\mu)\), with \(\mu=\Psi_*m_3\), where \(m_3\) denotes normalized Haar measure on \(\mathbb T^3\) and
\[
\Psi(\xi,\lambda_1,\lambda_2)=\left(\frac{\xi(\lambda_1-\lambda_2)}2,\lambda_1+\lambda_2,\lambda_1\lambda_2\right).
\]
Only the closure of polynomials in the first two coordinates \(a\) and \(s/2\) is examined. All coefficients and asymptotics refer to the unweighted canonical space; they need not apply to Jacobian-weighted pentablock Hardy spaces.

## Proof
**Ball projection.** On the distinguished boundary \(b\mathcal P=\Psi(\mathbb T^3)\), writing \(b=(\lambda_1+\lambda_2)/2\), one has \(|a|^2+|b|^2=1\). Since \(b\mathcal P\) is the distinguished (Shilov) boundary, the same scalar maximum-modulus bound holds for every linear functional in \((a,b)\), hence \(|a|^2+|b|^2\le1\) throughout the closed pentablock and the inequality is strict in \(\mathcal P\). Conversely, fix \((a,b)\in\mathbb B^2\), select \(t\) with \(|a|<t<\sqrt{1-|b|^2}\), and select \(v\in\mathbb C\) of modulus \(t\) orthogonal to \(b\) in the real plane (arbitrary direction for \(b=0\)). Then \(\lambda_1=b+v\), \(\lambda_2=b-v\), and \(\xi=a/v\) are all in \(\mathbb D\), and \(\Psi(\xi,\lambda_1,\lambda_2)\in\mathcal P\) projects to \((a,b)\). This proves surjectivity without asserting that \(\Psi\) parametrizes all of \(\mathcal P\).

**Measure and moments.** Under independent Haar phases, write \(\lambda_1=e^{i(\theta+\delta)}\), \(\lambda_2=e^{i(\theta-\delta)}\). Their torus law induces uniform \(\delta\) modulo \(\pi\), so \(|a|^2=\sin^2\delta\) has density \([\pi\sqrt{t(1-t)}]^{-1}\,dt\) for \(0<t<1\). The phase of \(b\) is uniform and independent of \(t\); the independent Haar phase \(\xi\) makes the phase of \(a\) uniform and independent of the former. Normalized surface measure on \(\partial\mathbb B^2\) has uniform radial variable \(t=|z_1|^2\) and the same independent uniform coordinate phases. Therefore the two-coordinate pushforward of \(\mu\) is \(d\nu=d\sigma/(\pi |z_1z_2|)\). Integration of \(t^k(1-t)^\ell\) against its arcsine density gives
\[
\frac{B(k+\tfrac12,\ell+\tfrac12)}{B(\tfrac12,\tfrac12)}=\frac{\Gamma(k+\tfrac12)\Gamma(\ell+\tfrac12)}{\pi\Gamma(k+\ell+1)}.
\]
Independent phases give orthogonality of distinct monomials. Holomorphic polynomials are dense by definition, proving the stated isometry. Orthogonal-series summation yields the stated kernel. Its convergence holds throughout \(\mathbb B^2\times\mathbb B^2\), since \(|z_1\bar w_1|+|z_2\bar w_2|<1\).

**Exact commutator diagonal.** Let \(e_{k,\ell}=z_1^kz_2^\ell/\|z_1^kz_2^\ell\|\) and \(n=k+\ell\). The forward shift weights are
\[
S_1e_{k,\ell}=\sqrt{\frac{k+1/2}{n+1}}e_{k+1,\ell},\qquad S_2e_{k,\ell}=\sqrt{\frac{\ell+1/2}{n+1}}e_{k,\ell+1}.
\]
Their squared weights add to one. Subtracting the incoming squared \(S_1\) weight from its outgoing squared weight gives
\[
Ce_{k,\ell}=c_{k,\ell}e_{k,\ell},\qquad c_{k,\ell}=\begin{cases}
\displaystyle\frac1{2(\ell+1)},&k=0,\\[1mm]
\displaystyle\frac{\ell+1/2}{n(n+1)},&k\ge1.
\end{cases}
\]
All eigenvalues are positive and tend uniformly to zero as \(k+\ell\to\infty\). Thus \(C\) is positive and compact.

**Weyl law.** At degree \(n\ge1\), the \(n\) regular eigenvalues are \((\ell+1/2)/(n(n+1))\) for \(0\le\ell<n\), plus one exceptional eigenvalue \(1/[2(n+1)]\). The number of regular values above \(\varepsilon>0\) at degree \(n\) is
\[
 n\bigl(1-\varepsilon(n+1)\bigr)_++O(1),
\]
with an absolute error constant, uniformly in \(n\); no regular terms contribute once \(n\ge 1/\varepsilon\). The exceptional terms contribute only \(O(\varepsilon^{-1})\). Consequently,
\[
\#\{\lambda(C)>\varepsilon\}
=\sum_{1\le n<1/\varepsilon}n(1-\varepsilon(n+1))+O(\varepsilon^{-1})
=\frac1{6\varepsilon^2}+O(\varepsilon^{-1}).
\]
Equivalently the singular values of \(C^2\), in decreasing order, obey \(s_j(C^2)\sim1/(6j)\). This proves the sharp Schatten threshold and, by logarithmic Cesaro summation, \(\lim_{N\to\infty}(\log N)^{-1}\sum_{j\le N}s_j(C^2)=1/6\), hence the asserted normalized Dixmier trace.

## Verification
The included standard-library program `verification.py` checks the rational beta-moment recurrences, the spherical shift identity, and every diagonal eigenvalue formula for all total degrees up to \(29\). It also enumerates the exact eigenvalues at reciprocal-integer thresholds through \(\varepsilon=1/1280\), where the scaled count is \(0.166664429\). These are independent *finite checks* of formulas, not the proof of the infinite Weyl limit, which is the preceding uniform lattice-counting argument.

## Relationship to prior work
Su and Tomar [1, Sections 2–5] introduce the canonical Hardy space, its fibre decomposition, and the full coordinate multiplier theory. Their reproducing-kernel description uses an orthogonal projection, and they derive a lower bound on the *full* kernel diagonal; they do not identify the singularly weighted two-ball factor or its exact self-commutator counting constant. Chavan and Yakubovich [2] develop Schatten criteria for *unitarily rotationally invariant* spherical weighted shifts. Their criterion does not directly imply this statement because the arcsine moments are not invariant under all unitary rotations of the two-ball (for instance, the monomial fourth moments differ from Haar-sphere fourth moments). Arveson's general multishift work [3] and Douglas's monomial-module work [4] supply context for the critical dimension-two Schatten threshold, but do not determine the specific pentablock-induced measure, Appell kernel or exact counting coefficient. These connections limit any claim of novelty to the concrete isometric factor and quantitative identification, not the abstract existence of multishift or Schatten theory.

## Limitations
This theorem makes no claim about the corresponding commutator on the full \(H^2(\mathcal P)\), other coordinate multipliers, or Jacobian-weighted versions of the Hardy space. The self-commutator eigenvalues have infinite support and the proof does not establish an exact finite-threshold count formula beyond the displayed asymptotic. Priority remains subject to earlier unindexed equivalent treatments of Dirichlet-weighted sphere modules or the present coordinate factor; no independent audit has been performed.

## References
[1] G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Pentablock*, arXiv:2610.17729, first submitted 2026-10-13, especially Sections 2–5. https://arxiv.org/abs/2610.17729

[2] S. Chavan and D. Yakubovich, *Spherical Tuples of Hilbert Space Operators*, arXiv:1401.0487 (2014), Theorems 2.1 and 4.2. https://arxiv.org/abs/1401.0487

[3] W. Arveson, *p-Summable Commutators in Dimension d*, arXiv:math/0308104 (2003). https://arxiv.org/abs/math/0308104

[4] R. G. Douglas, *Essentially Reductive Hilbert Modules*, arXiv:math/0404167 (2004). https://arxiv.org/abs/math/0404167
