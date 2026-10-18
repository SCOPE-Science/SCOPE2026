# A compact non-Hilbert--Schmidt weighted composition operator on the Gaussian Fock space: an exact transition

## Finding

Let \(\mathcal F^2\) be the classical Gaussian Fock space with norm
\[
\|f\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
Fix any real \(0<\lambda<1\), put \(a=1-\lambda^2\), and, for each \(\gamma>0\), define the entire function and weighted composition operator
\[
g_\gamma(z)=\int_0^1 t^{\gamma-1}e^{itz}\,dt,\qquad
(W_\gamma f)(z)=e^{az^2/2}g_\gamma(z)f(\lambda z).
\]
Then **every** \(W_\gamma:\mathcal F^2\to\mathcal F^2\) is bounded and compact, but
\[
\boxed{\quad W_\gamma\in\mathcal S_2\quad\Longleftrightarrow\quad\gamma>\tfrac12.\quad}
\]
For \(\gamma>1/2\), its squared Hilbert--Schmidt norm is exactly
\[
\boxed{\quad\|W_\gamma\|_{\mathcal S_2}^2
=\sqrt{\frac{2\pi}{a}}\int_0^1 t^{2\gamma-2}e^{t^2/(2a)}\,dt.\quad}
\]
In particular, all \(0<\gamma\le 1/2\) give explicit **compact non-Hilbert--Schmidt weighted composition operators**, answering Question 7.1 of Barik--Sen--Paul negatively already in the classical member of their weighted-Fock family.

The transition has the exact critical residue
\[
\boxed{\quad\lim_{\gamma\downarrow1/2}(2\gamma-1)\|W_\gamma\|_{\mathcal S_2}^2=\sqrt{\frac{2\pi}{a}}.\quad}
\]
More constructively, let \(W_{\gamma,\varepsilon}\) replace the integral defining \(g_\gamma\) by integration over \([\varepsilon,1]\), for \(0<\varepsilon<1\). These operators are Hilbert--Schmidt and satisfy
\[
\|W_\gamma-W_{\gamma,\varepsilon}\|
\le \frac{\varepsilon^\gamma}{\lambda\gamma}
\exp\!\left(\frac{\varepsilon^2}{4a}\right),
\qquad
\|W_{\gamma,\varepsilon}\|_{\mathcal S_2}^2
=\sqrt{\frac{2\pi}{a}}\int_\varepsilon^1 t^{2\gamma-2}e^{t^2/(2a)}\,dt.
\]
Thus the operator-norm convergence to a compact but non-Hilbert--Schmidt limit occurs with an explicit rate, while the squared Hilbert--Schmidt norms diverge logarithmically at \(\gamma=1/2\) and as a power for \(0<\gamma<1/2\).

## Assumptions and scope

The complex Fock space is normalized by \(dA/\pi\), with orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\) for \(n\ge0\). All parameters \(\lambda\) and \(\gamma\) are real, with \(0<\lambda<1\) and \(\gamma>0\). No claim is made for other Fock weights, nonlinear composition maps, or Schatten exponents other than two. The normalization \(a=1-\lambda^2>0\) is essential. The symbols are entire because
\[
g_\gamma(z)=\sum_{n=0}^\infty\frac{(iz)^n}{n!(n+\gamma)},
\]
with locally uniform convergence.

## Proof

**Step 1 (weighted embedding and the operator norm).** Write \(z=x+iy\). For an arbitrary entire function \(h\), let \(T_hf(z)=e^{az^2/2}h(z)f(\lambda z)\). Substituting \(w=\lambda z\) in the Fock norm gives the exact identity
\[
\|T_h f\|_{\mathcal F^2}^2
=\frac1\pi\int_{\mathbb C}|f(w)|^2 e^{-|w|^2}
\underbrace{\lambda^{-2}|h(w/\lambda)|^2e^{-2a(\Im w)^2/\lambda^2}}_{\rho_h(w)}\,dA(w).
\]
Indeed, \(\Re z^2-|z|^2=-2y^2\). Whenever \(\sup_{z\in\mathbb C}|h(z)|e^{-a(\Im z)^2}<\infty\), it follows that
\[
\|T_h\|\le\lambda^{-1}\sup_{z\in\mathbb C}|h(z)|e^{-a(\Im z)^2}.
\]

**Step 2 (explicit compact approximation).** Define \(g_{\gamma,\varepsilon}(z)=\int_\varepsilon^1t^{\gamma-1}e^{itz}\,dt\). For every \(y\in\mathbb R\),
\[
|g_\gamma(z)-g_{\gamma,\varepsilon}(z)|
\le\int_0^\varepsilon t^{\gamma-1}e^{|y|t}\,dt
\le \gamma^{-1}\varepsilon^\gamma e^{\varepsilon|y|}.
\]
Applying Step 1 and maximizing \(\exp(-ay^2+\varepsilon|y|)\) gives
\[
\|W_\gamma-W_{\gamma,\varepsilon}\|
\le(\lambda\gamma)^{-1}\varepsilon^\gamma
\exp(\varepsilon^2/(4a)).
\]
The same estimate with integration over \([0,1]\) shows the original operator is bounded. Step 3 proves that the monomial images of every cutoff have summable squared norms; by bounded point evaluations and polynomial density, the resulting Hilbert--Schmidt extension agrees with the given weighted composition formula on all of \(\mathcal F^2\). Therefore each cutoff is compact, and their operator-norm limit \(W_\gamma\) is compact for every \(\gamma>0\). Independently, the compactness profile \( |g_\gamma(x+iy)|^2e^{-2ay^2}\) tends to zero as \( |x+iy|\to\infty\): one has \( |g_\gamma(x+iy)|\le\gamma^{-1}e^{|y|}\), while for bounded \(y\) the Riemann--Lebesgue lemma applies uniformly to the compact family of \(L^1\) functions \(t^{\gamma-1}e^{-yt}\mathbf1_{(0,1)}(t)\).

**Step 3 (exact Hilbert--Schmidt identity and threshold).** For \(h=g_\gamma\) or \(g_{\gamma,\varepsilon}\), Tonelli's theorem and \(\sum_{n\ge0}|\lambda z|^{2n}/n!=e^{\lambda^2|z|^2}\) yield
\[
\|T_h\|_{\mathcal S_2}^2
=\sum_{n\ge0}\|T_h e_n\|_{\mathcal F^2}^2
=\frac1\pi\int_{\mathbb R}\int_{\mathbb R}
|h(x+iy)|^2e^{-2ay^2}\,dx\,dy,
\]
with the possibility of the value \(+\infty\).
For each fixed real \(y\), the function \(x\mapsto g_\gamma(x+iy)\) is the Fourier transform, under the convention \(\widehat F(x)=\int_{\mathbb R}F(t)e^{ixt}\,dt\), of
\[
F_{\gamma,y}(t)=\mathbf1_{(0,1)}(t)t^{\gamma-1}e^{-yt}.
\]
This function is integrable for all \(\gamma>0\). It lies in \(L^2(\mathbb R)\) precisely for \(\gamma>1/2\). Conversely, if its Fourier transform were in \(L^2\) for \(\gamma\le1/2\), inverse Plancherel in the sense of tempered distributions would force \(F_{\gamma,y}\in L^2\), a contradiction. Consequently the integral in \(x\) diverges for every \(y\) when \(\gamma\le1/2\). For \(\gamma>1/2\), Plancherel gives
\[
\int_{\mathbb R}|g_\gamma(x+iy)|^2dx
=2\pi\int_0^1t^{2\gamma-2}e^{-2yt}\,dt.
\]
For cutoffs, the same equality holds with lower limit \(\varepsilon\), **for every \(\gamma>0\)**. Finally, by Tonelli and completing a square,
\[
\int_{\mathbb R}e^{-2ay^2-2ty}dy
=\sqrt{\frac\pi{2a}}e^{t^2/(2a)}.
\]
Substitution proves both claimed exact Hilbert--Schmidt formulas and the sharp threshold.

**Step 4 (critical residues and cutoff divergence).** For \(\gamma>1/2\), multiply the formula by \(2\gamma-1\). Since \(t\mapsto e^{t^2/(2a)}\) is continuous with value one at zero, the elementary Abelian limit
\[
\lim_{\delta\downarrow0}\delta\int_0^1t^{\delta-1}e^{t^2/(2a)}\,dt=1
\]
proves the asserted critical residue. Moreover \(e^{t^2/(2a)}=1+O(t^2)\) at zero, so the cutoff formulas give, as \(\varepsilon\downarrow0\),
\[
\|W_{1/2,\varepsilon}\|_{\mathcal S_2}^2
=\sqrt{\frac{2\pi}{a}}\log(1/\varepsilon)+O(1),
\]
and, for each fixed \(0<\gamma<1/2\),
\[
\|W_{\gamma,\varepsilon}\|_{\mathcal S_2}^2
=\sqrt{\frac{2\pi}{a}}\frac{\varepsilon^{2\gamma-1}}{1-2\gamma}+O(1).
\]
This completes the proof. \(\square\)

## Verification

The accompanying `checker.py` uses only the Python standard library. It compares direct finite-interval quadratures of the Fourier transforms of truncated exponential weights with the Plancherel predictions, checks the sign and growth of the exact cutoff Hilbert--Schmidt formulas on both sides of the threshold, and evaluates the near-critical residue for several positive parameters. To run it, execute `python3 checker.py`. Its output is `PASS: finite Gaussian-Fourier cutoff quadratures, cutoff behavior, and critical residue diagnostics`. These checks are **finite numerical diagnostics** only; Steps 1--4 establish the full theorem analytically without relying on the computed values.

## Relationship to prior work

Barik--Sen--Paul (2026), arXiv:2607.17170v1, prove general boundedness, compactness and Hilbert--Schmidt criteria on weighted Fock spaces and explicitly pose in their Section 7, Question 7.1 whether compact weighted composition operators must be Hilbert--Schmidt. Their Section 6 examples do not exhibit a compact, non-Hilbert--Schmidt weighted composition operator. The present result answers that question negatively already at the classical Gaussian specialization, supplying concrete entire symbols and a sharp Fourier-endpoint threshold.

Ueki (2007) gives the classical Gaussian Hilbert--Schmidt integral test, recovered here at the start of Step 3; this characterization is **prior**, not a newly claimed criterion. Mengestie's 2012 preprint and 2013 and 2015 papers give general compactness/Schatten-type characterizations; those broad criteria are also prior. The new assertion is existence of compact yet non-Hilbert--Schmidt weighted composition symbols of the displayed explicit form, together with the exact sharp parameter transition, compact approximation rate and logarithmic/power spectral-energy divergence. Tien--Khoi's full accessible 2017 preprint studies general boundedness and compactness but supplies no covering explicit non-Hilbert--Schmidt construction.

## Limitations

The result does not classify the remaining Schatten ideals, does not address the general \(m\ne2\) weighted-Fock situation, and does not rule out distinct equivalent constructions elsewhere. Prior general characterization theorems may offer alternative routes to testing these symbols. The full 2013 and 2015 Mengestie articles could not be inspected; comparison of those works rests on their available abstracts and their relation to the earlier accessible preprint. Publication priority should therefore be checked independently.

## References

1. S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1 (first submitted 2026-07-19), Section 7, Question 7.1. https://arxiv.org/abs/2607.17170
2. S.-I. Ueki, *Hilbert-Schmidt Weighted Composition Operator on the Fock space*, International Journal of Mathematical Analysis **1** (2007), 769--774. https://www.m-hikari.com/ijma/ijma-password-2007/ijma-password13-16-2007/uekiIJMA13-16-2007.pdf
3. T. Mengestie, *Product of Volterra type integral and composition operators on weighted Fock spaces*, arXiv:1210.4038 (2012). https://arxiv.org/abs/1210.4038
4. T. Mengestie, *Schatten class weighted composition operators on weighted Fock spaces*, Archiv der Mathematik **101** (2013), 349--360. https://doi.org/10.1007/s00013-013-0568-2
5. T. Mengestie, *On trace ideal weighted composition operators on weighted Fock spaces*, Archiv der Mathematik **105** (2015), 453--459. https://doi.org/10.1007/s00013-015-0827-5
6. P. T. Tien and L. H. Khoi, *Weighted composition operators between different Fock spaces*, arXiv:1704.03752 (2017), later in Potential Analysis (2019). https://arxiv.org/abs/1704.03752
