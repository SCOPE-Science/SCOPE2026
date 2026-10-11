# Universal Bowen-ball volume law for irrational skew Dehn twists

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) and equip \(\mathbb T^2\) with the product metric \(d_\infty((x,y),(x',y'))=\max\{\|x-x'\|_{\mathbb T},\|y-y'\|_{\mathbb T}\}\) and normalized Haar area \(\lambda\). Fix an irrational \(\alpha\), a nonzero integer \(k\), and a real-valued one-periodic \(C^1\) function \(\psi\). Consider the area-preserving skew Dehn twist
\[
F(x,y)=(x+\alpha,\ y+kx+\psi(x))\pmod{1}.
\]
For \(n\ge 2\), write the strict Bowen ball
\[
B_n(z,\varepsilon)=\{w\in\mathbb T^2:\max_{0\le j<n}d_\infty(F^jz,F^jw)<\varepsilon\}.
\]
Put \(L=|k|+\|\psi'\|_\infty\) and \(\varepsilon_0=\min\{1/8,1/(8L)\}\). For **every** \(0<\varepsilon<\varepsilon_0\),
\[
\boxed{\displaystyle\lim_{n\to\infty}\ \sup_{z\in\mathbb T^2}\left|n\lambda(B_n(z,\varepsilon))-\frac{4\varepsilon^2}{|k|}\right|=0.}
\]
More precisely, rescaling the initial base displacement by \(a=n(x'-x)\) gives a uniform limiting Bowen-ball shape
\[
\mathcal P_{\varepsilon,k}=\{(a,\eta)\in\mathbb R^2:|\eta|<\varepsilon,\ |\eta+ka|<\varepsilon\},
\]
a parallelogram of area \(4\varepsilon^2/|k|\). As a consequence, the topological polynomial entropy of \(F\) is exactly \(1\).

## Assumptions and scope
The integer \(k\) is nonzero and the base rotation \(x\mapsto x+\alpha\) is irrational. The perturbation \(\psi\) is arbitrary among real \(C^1\), one-periodic functions; no smallness or Diophantine hypothesis is imposed. The metric and normalized Haar measure are fixed as above. All assertions about Bowen-ball area concern fixed \(\varepsilon\) in the stated open interval as \(n\to\infty\). Polynomial entropy uses any standard equivalent separated-set or spanning-set definition on the compact torus.

## Proof
**1. Lifted displacement identity.** Choose lifts of two points differing by \((\delta,\eta)\), where \(|\delta|,|\eta|<\varepsilon<1/8\). The base difference stays \(\delta\). The real lifted fiber difference after \(j\) iterates is
\[
v_j=\eta+jk\delta+\delta\int_0^1 S_j\psi'(x+s\delta)\,ds,\qquad
S_j\psi'(u)=\sum_{\ell=0}^{j-1}\psi'(u+\ell\alpha),
\]
with \(S_0\psi'=0\). This follows by summing the exact mean-value integral of \(\psi(u+\delta)-\psi(u)\), without truncating a Taylor series.

**2. Uniform cancellation of the periodic derivative.** The mean of \(\psi'\) over the circle is zero. Irrationality of \(\alpha\) implies
\[
e_n=\frac1n\sup_{u\in\mathbb T}\max_{0\le j<n}|S_j\psi'(u)|\longrightarrow0.
\]
For completeness, approximate the continuous zero-mean function \(\psi'\) uniformly by a trigonometric polynomial with zero constant coefficient. Each nonzero Fourier mode has uniformly bounded rotation sums because \(1-e^{2\pi i\ell\alpha}\ne0\) for \(\ell\ne0\). The approximation error is at most \(j\) times the chosen uniform error. First taking \(n\to\infty\) and then the approximation error to zero proves the displayed maximum-over-prefixes estimate.

**3. No hidden integer winding in small Bowen balls.** Suppose \(w\in B_n(z,\varepsilon)\). The initial displacement has \(|\delta|,|\eta|<\varepsilon\), and
\[
|v_{j+1}-v_j|\le (|k|+\|\psi'\|_\infty)|\delta|<1/8.
\]
Each \(v_j\) has circle distance below \(\varepsilon\) from an integer. Starting with \(v_0\in(-\varepsilon,\varepsilon)\), it is impossible to jump to the \(\varepsilon\)-neighborhood of a different integer in one step: distinct such neighborhoods have gap \(1-2\varepsilon>3/4\). Induction gives \(|v_j|<\varepsilon\) as real numbers for all \(0\le j<n\).

**4. The rescaled shape.** The final-index displacement identity and Step 2 yield
\[
2\varepsilon>|v_{n-1}-\eta|\ge |\delta|\big((n-1)|k|-n e_n\big).
\]
For all sufficiently large \(n\), uniformly over the Bowen center, this forces \(|a|=n|\delta|\le4\varepsilon/|k|\). Conversely, for \(|a|\le4\varepsilon/|k|\), set \(\delta=a/n\). Uniformly in the starting base point \(x\) and in all \(0\le j<n\),
\[
\left|v_j-\left(\eta+ka\frac jn\right)\right|\le |a|e_n\longrightarrow0.
\]
Consequently the rescaled Bowen-ball indicator converges outside the boundary of the parallelogram to the indicator of \(\mathcal P_{\varepsilon,k}\), with the same uniform error for every center. Indeed, for any fixed margin \(\gamma>0\), once \(n\) is sufficiently large, all points with \(|\eta|,|\eta+ka|<\varepsilon-\gamma\) belong to the rescaled ball, while every point of the rescaled ball satisfies \(|\eta|<\varepsilon\) and \(|\eta+ka|<\varepsilon+\gamma\). These inclusions follow from the elementary identity \(\max_{0\le t\le1}|\eta+kat|=\max\{|\eta|,|\eta+ka|\}\) and the fact that the final sampled time tends to \(1\).

The change of variables from \(\delta\) to \(a=n\delta\) has Jacobian \(1/n\). Since the limiting parallelogram is bounded and its boundary has area zero, the preceding uniform sandwich proves uniform convergence of the rescaled areas. Finally,
\[
\operatorname{area}(\mathcal P_{\varepsilon,k})
=\int_{-\varepsilon}^{\varepsilon}\frac{2\varepsilon}{|k|}\,d\eta
=\frac{4\varepsilon^2}{|k|}.
\]
The limit is independent of both the rotation angle and the periodic perturbation.

**5. Polynomial entropy.** The Bowen-ball area asymptotic forces any \((n,\varepsilon)\)-spanning collection to have at least \(1/\sup_z\lambda(B_n(z,\varepsilon))\), which is bounded below by a positive constant times \(n\). For an upper bound, choose a regular torus grid with base spacing at most \(\varepsilon/(4Ln)\) and fiber spacing at most \(\varepsilon/4\). Any point has a grid point whose first \(n\) iterates remain at \(d_\infty\)-distance below \(\varepsilon\), by the one-step Lipschitz bound and telescoping. The grid has \(O_\varepsilon(n)\) points. Thus the logarithmic growth exponent of spanning numbers is both at least and at most \(1\), proving \(h_{\mathrm{pol}}(F)=1\).

## Verification
Every displayed identity is exact except the explicitly marked uniform limit \(e_n\to0\), proved in Step 2. The only area computation is the integral over two independent interval inequalities in \(\eta\) and \(\eta+ka\). The lifted-difference argument is valid for the stated explicit small-radius condition, including both signs of \(k\). No numerical experiment, finite simulation, or external computational certificate is used as an infinite proof. The supplied argument establishes asymptotic area and polynomial-entropy exponent, not a finite-\(n\) error bound independent of arithmetic properties of \(\alpha\).

## Relationship to prior work
Corrêa's 2026 article studies polynomial entropy of torus maps homotopic to the identity, proving a lower bound for non-singleton rotation sets; it also recalls an existing linear lower bound for toral Dehn-twist homotopy classes and discusses degree-zero skew products with rational base rotation. The present skew maps have nontrivial Dehn-twist homology action, and the claim is the **exact, center-uniform Haar area coefficient and limiting local shape**, not merely the already-motivated linear growth exponent. Correa and Pujals proved growth-class results for toral Dehn twists and annular twist maps, but those do not state an area-asymptotic coefficient for irrational-base, nonzero-degree skew twists. Grycan-Gérard and Marco developed polynomial torsion and bounds for fibered systems and angle-action models; their entropy-scale statements do not supply this metric-specific local area law.

## Limitations
The coefficient depends on the chosen product metric and Haar normalization; it is not asserted to be an invariant of arbitrary topological conjugacy. The theorem requires \(k\ne0\), irrational \(\alpha\), and \(C^1\) regularity of \(\psi\). No assertion is made at the boundary \(\varepsilon=\varepsilon_0\), for rational base rotations, for general merely continuous perturbations, or about a universal convergence rate. The polynomial-entropy corollary is included as a check on the geometry rather than claimed as the novel component by itself.

## References
1. H. Corrêa, *Polynomial entropy and rotation sets*, Archiv der Mathematik (first public version verified 12 September 2026), DOI: 10.1007/s00013-026-02286-3; particularly Theorem 1.1, Corollary 1.2, Sections 3–5.
2. J. Correa and E. R. Pujals, *Orders of growth and generalized entropy*, arXiv:2003.01257 (first preprint 3 March 2020); Journal of the Institute of Mathematics of Jussieu 22 (2023), 1581–1613, DOI: 10.1017/S1474748021000463; particularly Corollary 2 and Section 3.4.
3. F. Grycan-Gérard and J.-P. Marco, *Polynomial entropy and polynomial torsion for fibered systems*, Regular and Chaotic Dynamics 28 (2023), 613–627, DOI: 10.1134/S156035472304007X; particularly Sections 3 and 4.
