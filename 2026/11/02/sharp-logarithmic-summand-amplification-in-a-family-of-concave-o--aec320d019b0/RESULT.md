# Sharp logarithmic summand amplification in a family of concave Orlicz sequence gauges

## Finding
For every real \(\alpha>0\), define \(F_\alpha(0)=0\) and
\[
F_\alpha(t)=t\left[\log\left(e^\alpha+\frac1t\right)\right]^\alpha,\qquad t>0.
\]
Let \(X_\alpha\) be the real or complex sequence space equipped with the Luxemburg gauge
\[
\|x\|_\alpha=\inf\left\{\rho>0:\sum_{j=1}^\infty F_\alpha(|x_j|/\rho)\le1\right\},
\]
where \(X_\alpha\) consists of sequences of finite gauge. Define the exact \(n\)-summand amplification constant
\[
C_\alpha(n)=\sup_{x_1,\ldots,x_n\in X_\alpha\atop\sum_i\|x_i\|_\alpha>0}
\frac{\|\sum_{i=1}^n x_i\|_\alpha}{\sum_{i=1}^n\|x_i\|_\alpha}.
\]
Let \(a_\alpha>0\) be the unique solution of \(F_\alpha(a_\alpha)=1\). Then \(X_\alpha\) is a complete quasi-normed sequence space and
\[
\boxed{\displaystyle\lim_{n\to\infty}\frac{C_\alpha(n)}{(\log n)^\alpha}=a_\alpha.}
\]
In particular, every \(X_\alpha\), \(\alpha>0\), is nonnormable; its finite-summand deviation from the triangle inequality grows at the sharp logarithmic rate \((\log n)^\alpha\). At \(\alpha=0\), interpreted by \(F_0(t)=t\), the gauge is the usual \(\ell_1\) norm and \(C_0(n)=1\).

## Assumptions and scope
All logarithms are natural; \(n\ge2\) in asymptotic expressions. Countably indexed scalar sequences have counting measure. The gauge is exactly the displayed Luxemburg functional, without unspecified equivalence constants or rescaling. The claimed sharp constant depends on that normalization. The comparison of rates concerns fixed \(\alpha>0\), not a joint limit in \(\alpha\) and \(n\). No formula for finite \(n\) beyond the explicit lower bound below is asserted.

## Proof
**1. Concavity, quasi-norm, and completeness.** Write \(L(t)=\log(e^\alpha+1/t)\). Direct differentiation gives
\[
F_\alpha'(t)=L(t)^{\alpha-1}\left(L(t)-\frac\alpha{1+e^\alpha t}\right)>0,
\qquad
F_\alpha''(t)=\frac{\alpha L(t)^{\alpha-2}(\alpha-1-L(t))}{t(1+e^\alpha t)^2}<0.
\]
Thus \(F_\alpha\) is continuous, strictly increasing, concave, unbounded, and subadditive, with \(F_\alpha(0)=0\). For \(0<s\le1\), \(t>0\),
\[
\frac{F_\alpha(st)}{F_\alpha(t)}
=s\left(\frac{L(st)}{L(t)}\right)^\alpha
\le s\left(1+\frac{\log(1/s)}\alpha\right)^\alpha.
\tag{1}
\]
In particular the right side tends to zero as \(s\downarrow0\), uniformly in \(t\). Taking \(s=K^{-1}\) sufficiently small that the right side is at most \(1/2\), subadditivity of \(F_\alpha\) yields \(\|x+y\|_\alpha\le K(\|x\|_\alpha+\|y\|_\alpha)\). The gauge is positive definite and absolutely homogeneous. Since \(F_\alpha(2t)\le 2F_\alpha(t)\), its modular is continuous under positive scale changes wherever finite; for nonzero \(x\), the modular equals one at \(\rho=\|x\|_\alpha\). A gauge-Cauchy sequence is coordinatewise Cauchy; Fatou's lemma applied to its normalized differences gives convergence in gauge to the coordinatewise limit. Consequently \(X_\alpha\) is complete.

**2. Disjoint-vector lower bound.** The standard coordinate vectors satisfy \(\|e_i\|_\alpha=1/a_\alpha\). Their sum of length \(n\) has gauge \(1/F_\alpha^{-1}(1/n)\). Hence
\[
C_\alpha(n)\ge\frac{a_\alpha}{n F_\alpha^{-1}(1/n)}.
\tag{2}
\]
Since \(F_\alpha(t)\sim t[\log(1/t)]^\alpha\) at zero, direct substitution and monotonicity show
\[
F_\alpha^{-1}(1/n)\sim\frac1{n(\log n)^\alpha}.
\tag{3}
\]
Equations (2)–(3) give \(\liminf C_\alpha(n)/(\log n)^\alpha\ge a_\alpha\).

**3. Uniform upper bound via entropy.** Take nonzero vectors \(x_1,\ldots,x_n\), set \(b_i=\|x_i\|_\alpha\), \(B=\sum_i b_i\), \(w_i=b_i/B\), and \(z_{ij}=|x_{i,j}|/b_i\). Zero vectors may be discarded. Then \(\sum_jF_\alpha(z_{ij})\le1\) and \(z_{ij}\le a_\alpha\). Put \(r_\alpha=L(a_\alpha)\), so \(r_\alpha^\alpha=1/a_\alpha\). The refined version of (1), using \(L(z_{ij})\ge r_\alpha\), says that for \(C\ge1\)
\[
F_\alpha\left(\frac{w_i z_{ij}}C\right)
\le\frac{w_i}{C r_\alpha^\alpha}
\left(r_\alpha+\log C+\log(1/w_i)\right)^\alpha F_\alpha(z_{ij}).
\]
Monotonicity and subadditivity therefore yield
\[
\sum_j F_\alpha\left(\frac{|\sum_i x_{i,j}|}{BC}\right)
\le \frac{a_\alpha}{C}\sum_i w_i
\left(r_\alpha+\log C+\log(1/w_i)\right)^\alpha.
\tag{4}
\]
For arbitrary positive weights \(w_i\) summing to one, let \(W\) take value \(\log(1/w_i)\) with probability \(w_i\). Put \(H=\log n\). For every \(u\ge0\),
\[
\Pr\{W>H+u\}=\sum_{w_i<e^{-H-u}}w_i\le ne^{-H-u}=e^{-u}.
\tag{5}
\]
Thus \(W\) is stochastically bounded by \(H+E\), where \(E\) has the exponential distribution of mean one. In particular, for \(D=r_\alpha+\log C\) and \(H+D>\alpha\),
\[
\mathbb E(D+W)^\alpha\le
\frac{(H+D)^\alpha}{1-\alpha/(H+D)},
\tag{6}
\]
because \((1+v)^\alpha\le e^{\alpha v}\) for \(v\ge0\).

Fix \(\varepsilon>0\) and choose \(C=(1+\varepsilon)a_\alpha H^\alpha\) for all sufficiently large \(n\). Then \(D=O_\alpha(\log H)\), so (4)–(6) give, uniformly over all summands,
\[
\sum_j F_\alpha\left(\frac{|\sum_i x_{i,j}|}{BC}\right)
\le\frac1{1+\varepsilon}(1+o(1))<1.
\]
Therefore \(\|\sum_i x_i\|_\alpha\le(1+\varepsilon)a_\alpha(\log n)^\alpha\sum_i\|x_i\|_\alpha\) for all sufficiently large \(n\). Letting \(\varepsilon\downarrow0\) proves the sharp limit.

**4. Nonnormability.** If the gauge were equivalent to any norm, there would be a constant independent of \(n\) bounding \(C_\alpha(n)\). The sharp limit contradicts this for every \(\alpha>0\).

## Verification
The analytic proof checks the derivative signs, normalizes each summand at exact Luxemburg modular one, and proves a uniform (not sample-specific) tail bound (5). The finite checker in `verify.py` separately tests the exact derivative identity and positivity conditions, the disjoint-vector modular relation, and entropy inequality (5) on finite weight sets. It is supplementary evidence only: the limit and completeness are proved above, not by numerical extrapolation. Run with `python verify.py` using Python 3 (standard library only); no external data is needed.

## Relationship to prior work
Kameník (2026) examines Orlicz and Lorentz–Zygmund sequence spaces, including fundamental functions and Banach-space parameter thresholds. Mayoral (2025), especially Section 5 and Theorem 5.3, studies normability versus nonnormability for convexifications of \(L\log L\) and \(L_{\exp}\), with a disjoint-support method for qualitative nonnormability. Kamińska and Żyluk (2019), especially Theorem 4.2, characterize normability and upper estimates for general quasi-normed Orlicz spaces via growth conditions. These qualitative and structural results are prior mathematics, not claimed here. The present specific contribution is the leading coefficient of the optimal \(n\)-term triangle-amplification function for the concave logarithmic family, obtained by a uniform entropy bound matching disjoint-coordinate vectors. The newly considered gauge is not asserted to be the same Luxemburg functional as any of those prior papers.

## Limitations
The result fixes \(\alpha>0\) before taking \(n\to\infty\), uses the discrete counting-measure gauge, and does not determine the exact finite-\(n\) maximizing configurations. Quantitative equivalences may exist in broader regularly varying modular literature; priority is assessed only against the literature inspected and is not an independence certificate. Kameník's full preprint could not be inspected beyond the available abstract, leaving a specific comparison risk. No independent mathematical validation has been performed.

## References
1. H. Kameník, *On Certian Fine Properties of Sequence Spaces*, arXiv:2609.17143v1 (first submitted 15 September 2026), https://arxiv.org/abs/2609.17143.
2. F. Mayoral, *On L_exp and L log L Zygmund's spaces and its r-convexifications: the Orlicz–Luxemburg point of view*, Adv. Oper. Theory 10 (2025), Article 60, https://doi.org/10.1007/s43036-025-00450-0.
3. A. Kamińska and M. Żyluk, *Local geometric properties in quasi-normed Orlicz spaces*, Banach Center Publ. 119 (2019), 197–221, https://doi.org/10.4064/bc119-12.
