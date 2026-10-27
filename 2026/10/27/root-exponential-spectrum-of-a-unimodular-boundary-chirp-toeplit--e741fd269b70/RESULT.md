# Root-exponential spectrum of a unimodular boundary-chirp Toeplitz operator

## Finding

Let \(d\geq1\) be an integer, \(\alpha>-1\), and \(c\in\mathbb R\setminus\{0\}\). On the normalized weighted Bergman space \(A^2_\alpha(\mathbb B_d)\), take the bounded radial symbol
\[
\phi_c(z)=\exp\!\left(\frac{ic}{1-\|z\|^2}\right).
\]
Although \(|\phi_c|=1\) everywhere in the unit ball, its Toeplitz compression \(T_{\phi_c}=P_\alpha M_{\phi_c}|_{A^2_\alpha}\) belongs to **every** Schatten class \(S_p\), \(0<p<\infty\), and has infinite rank. More precisely, if \(\lambda_k\) denotes its eigenvalue on the homogeneous holomorphic polynomials of total degree \(k\), then, with \(N=k+d-1\), \(a=-ic\), and all complex powers and square roots on their principal branches,
\[
\boxed{\lambda_k=\frac{\sqrt\pi}{\Gamma(\alpha+1)}a^{(2\alpha+1)/4}N^{(2\alpha+1)/4}\exp\!\left(\frac{ic}{2}-2\sqrt{aN}\right)(1+o(1)).}
\]
The equivalent sharp magnitude law is
\[
\boxed{\ |\lambda_k|\sim\frac{\sqrt\pi\,|c|^{(2\alpha+1)/4}}{\Gamma(\alpha+1)}N^{(2\alpha+1)/4}\exp\!\left(-\sqrt{2|c|N}\right).\ }
\]
Each \(\lambda_k\) occurs with multiplicity \(\binom{k+d-1}{d-1}\). Thus the singular-value counting function \(\mathcal N(s)=\#\{j:s_j(T_{\phi_c})>s\}\) satisfies the sharp law
\[
\boxed{\mathcal N(s)\sim\frac{(\log(1/s))^{2d}}{d!(2|c|)^d},\qquad s\downarrow0.}
\]
In contrast, \(T_{|\phi_c|}=I\) is not compact.

## Assumptions and scope

Write \(\mathbb B_d=\{z\in\mathbb C^d:\|z\|<1\}\). The weighted measure is
\[
d\mu_\alpha(z)=\frac{\Gamma(d+\alpha+1)}{\pi^d\Gamma(\alpha+1)}(1-\|z\|^2)^\alpha\,dV(z),
\]
which has total mass one. The Bergman projection \(P_\alpha\) is the orthogonal projection in \(L^2(d\mu_\alpha)\) onto its holomorphic subspace. For \(0<p<1\), \(S_p\) refers to the usual Schatten quasi-class. No real-valuedness, positivity, or boundary limit of \(\phi_c\) is asserted; the phase oscillates without a limit as the boundary is approached. The asymptotic is for fixed \(d,\alpha,c\), as \(k\to\infty\), and is not claimed uniformly as \(c\to0\).

## Proof

**1. Exact diagonalization.** Radiality makes distinct holomorphic monomials mutually orthogonal under the symbol-weighted sesquilinear form. Angular integration on the unit sphere cancels when their multiindices differ. For a monomial \(z^\nu\) with \(|\nu|=k\), the common angular factor cancels between numerator and denominator of its eigenvalue. With \(N=k+d-1\), the variable \(t=\|z\|^2\) has beta moment weight \(t^N(1-t)^\alpha\); hence
\[
\lambda_k=\frac{1}{B(N+1,\alpha+1)}\int_0^1 t^N(1-t)^\alpha e^{ic/(1-t)}\,dt. \tag{1}
\]
There are \(\binom{k+d-1}{d-1}\) linearly independent homogeneous monomials of degree \(k\).

**2. Exact Laplace–Bessel representation.** Put \(x=(1-t)/t\), \(a=-ic\), and \(v=N+\alpha+2\). Direct substitution gives
\[
\int_0^1 t^N(1-t)^\alpha e^{ic/(1-t)}dt
=e^{ic}\int_0^\infty x^\alpha(1+x)^{-v}e^{-a/x}\,dx. \tag{2}
\]
Insert the gamma identity \((1+x)^{-v}=\Gamma(v)^{-1}\int_0^\infty s^{v-1}e^{-s(1+x)}ds\). For \(\Re a>0\), Fubini and the classical Macdonald integral yield
\[
H_a(s):=\int_0^\infty x^\alpha e^{-sx-a/x}dx
=2\left(\frac a s\right)^{(\alpha+1)/2}K_{\alpha+1}(2\sqrt{as}). \tag{3}
\]
For the desired \(a=-ic\), take \(a=\varepsilon-ic\) and let \(\varepsilon\downarrow0\). Absolute domination in (2) is by \(x^\alpha(1+x)^{-v}\), integrable for \(\alpha>-1\) and \(N\ge0\). On the gamma-integral side, the same domination after integrating over \(s\) gives a justified Abel limit, so (3) is valid in the required integral representation. If \(S_N\) is gamma distributed with shape \(v\) and unit scale, equations (1)–(3) yield the exact identity
\[
\lambda_k=e^{ic}\frac{\Gamma(v)}{\Gamma(N+1)\Gamma(\alpha+1)}\,\mathbb E[H_a(S_N)]. \tag{4}
\]

**3. Critical asymptotics and the Gaussian correction.** For \(s\to\infty\) along the positive real axis, the principal square root has \(\arg\sqrt a=\pm\pi/4\). The standard sectorial expansion of the Macdonald function therefore gives
\[
H_a(s)=\sqrt\pi\,a^{(2\alpha+1)/4}s^{-(2\alpha+3)/4}e^{-2\sqrt{as}}(1+O(s^{-1/2})). \tag{5}
\]
Set \(Y_N=(S_N-N)/\sqrt N\). The gamma central limit theorem gives \(Y_N\Rightarrow G\), where \(G\) is standard normal. Since \(\sqrt{S_N}=\sqrt N+Y_N/2+o_{\mathbb P}(1)\), (5) and gamma concentration imply
\[
\mathbb E[H_a(S_N)]\sim \sqrt\pi\,a^{(2\alpha+1)/4}N^{-(2\alpha+3)/4}e^{-2\sqrt{aN}}\mathbb E[e^{-\sqrt a G}]
=\sqrt\pi\,a^{(2\alpha+1)/4}N^{-(2\alpha+3)/4}e^{-2\sqrt{aN}}e^{a/2}. \tag{6}
\]
For completeness, this convergence is valid in the *complex relative* sense, not merely in probability: on \(|Y_N|\le N^{1/8}\), the square-root Taylor remainder is \(O(Y_N^2/\sqrt N)\) and the power ratio in (5) tends to one. The exact gamma moment generating function
\[
\mathbb E[e^{tY_N}]=e^{-t\sqrt N}(1-t/\sqrt N)^{-v}
\]
(for any fixed complex \(t\) and all sufficiently large \(N\)) supplies uniform exponential moments of \(|Y_N|\). Gamma Chernoff bounds suppress \(|Y_N|>N^{1/8}\); on \(S_N\notin[N/2,2N]\), the tails are exponentially small in \(N\), whereas the displayed main term has only root-exponential suppression. The Bessel representation has at most polynomial growth as \(s\downarrow0\), so the lower gamma tail is harmless. These estimates justify dominated convergence after the indicated normalization. Finally,
\[
\frac{\Gamma(v)}{\Gamma(N+1)}\sim N^{\alpha+1},\qquad e^{ic+a/2}=e^{ic/2}.
\]
Substituting (6) into (4) proves the complex eigenvalue formula and its strictly positive magnitude asymptotic. In particular, \(\lambda_k\ne0\) for all sufficiently large \(k\).

**4. Schatten classes and counting.** Because the operator is diagonal and normal, its singular values are \(|\lambda_k|\), with the indicated multiplicities. The bound \(|\lambda_k|\le C N^M e^{-\sqrt{|c|N}}\) for large \(N\) implies \(\sum_k\binom{k+d-1}{d-1}|\lambda_k|^p<\infty\) for every \(p>0\). For \(L=\log(1/s)\), the magnitude formula gives the superlevel degree cutoff \(k\sim L^2/(2|c|)\); this assertion follows by sandwiching all sufficiently large degrees between the thresholds \((1\pm\varepsilon)L^2/(2|c|)\), without needing monotonicity of the actual \(|\lambda_k|\). Summing multiplicities, \(\sum_{k\le K}\binom{k+d-1}{d-1}=\binom{K+d}{d}\sim K^d/d!\), proves the counting law. Finally \(|\phi_c|=1\) pointwise gives \(T_{|\phi_c|}=I\).

## Verification

The included standalone `verify_chirp.py` compares independent oscillatory quadratures with the exact Macdonald/gamma integral for nine combinations of parameters and degrees, and performs twelve further quantitative asymptotic comparisons at degrees \(100\), \(300\), and \(1000\). All tests passed in a SciPy execution. The code checks finite cases and rates; the universal claims depend on the proof above. The checker is reproducible with NumPy and SciPy, without external data.

## Relationship to prior work

Cao, He and Zhang (arXiv:2609.24614; first posted 2026-09-21) establish qualitative compactness criteria for bounded disk Bergman Toeplitz symbols by vanishing local averages. Their inspected statements do not supply eigenvalue constants, a sharp singular-value counting asymptotic, or the all-Schatten result for this boundary chirp. Looi (arXiv:2603.10879, sections 3–4) analyzes much slower logarithmic radial oscillations and noncompact essential-spectrum behavior, rather than the inverse-boundary phase or root-exponential decay. Rozenblum (J. Spectr. Theory 1 (2011), section 5, Theorems 5.1–5.2) studies oscillatory *decaying* radial symbols on unbounded Bargmann domains, with different asymptotic scales; its section does not give the stated weighted-ball result. The common diagonal radial reduction is classical, and is not claimed as new.

## Limitations

The result is restricted to a fixed inverse-boundary phase \(c/(1-\|z\|^2)\), fixed \(c\ne0\), and radial symbols. It neither classifies all unimodular symbols that yield Schatten Toeplitz operators nor extends compactness characterizations. An older 2020 article by Bendaoud and collaborators on radial Toeplitz operators and Schatten classes could not be inspected in full; it remains a historical-priority risk, particularly for broader qualitative membership statements. No independent mathematical audit has been performed.

## References

1. Guangfu Cao, Li He, Shuqing Zhang, *Compactness of Toeplitz Operators on the Bergman Space*, arXiv:2609.24614 (first public 2026-09-21), https://arxiv.org/abs/2609.24614 .
2. Sam Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (first public 2026-03-11), https://arxiv.org/abs/2603.10879 .
3. Grigori Rozenblum, *On lower eigenvalue bounds for Toeplitz operators with radial symbols in Bergman spaces*, J. Spectr. Theory 1 (2011), 299–325, https://doi.org/10.4171/JST/13 .
4. Bendaoud and collaborators, *Toeplitz operators with radial symbols on Bergman space and Schatten-von Neumann classes* (2020), https://doi.org/10.15407/mag16.01.003 (full text not reviewed).
5. NIST Digital Library of Mathematical Functions, §§10.32 and 10.40 (integral representation and sectorial asymptotic of the modified Bessel function), https://dlmf.nist.gov/10.32 and https://dlmf.nist.gov/10.40 .
