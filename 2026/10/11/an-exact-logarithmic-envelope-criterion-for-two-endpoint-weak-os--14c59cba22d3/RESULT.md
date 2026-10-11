# An exact logarithmic-envelope criterion for two endpoint weak oscillation tests

## Finding

Two derivative-free weak-type quantities that cease to characterize arbitrary first-order Sobolev functions at the exponent-one endpoint nevertheless have the **same complete membership criterion** on a natural, infinite-dimensional class of one-sided logarithmic cusp profiles.

Define \(U:\mathbb R\to[0,1/2]\) by
\[
U(t)=\begin{cases}
[\log(e/t)]^{-1},&0<t\le 1/e,\\
1-et/2,&1/e<t<2/e,\\
0,&\text{otherwise}.
\end{cases}
\]
This is the explicit profile in Chen--Yang--Yuan--Zhang, equation (2.1), and \(U\in W^{1,1}(\mathbb R)\cap C_c(\mathbb R)\).

Let \(\Phi:[0,1/2]\to[0,\infty)\) be continuous and nondecreasing with \(\Phi(0)=0\), locally Lipschitz on \((0,1/2]\), and such that there exist \(K<\infty\) and \(s_0\in(0,1/2)\) with
\[
|s\Phi'(s)|\le K\Phi(s)\quad\text{for almost every }0<s<s_0.
\]
Put \(f=\Phi\circ U\). Let
\[
D(f)=\sup_{\lambda>0}\lambda\iint_{\substack{x,y\in\mathbb R\\|f(x)-f(y)|>\lambda}}\frac{dx\,dy}{|x-y|^2}.
\]
For \(I(a,r)=(a-r,a+r)\), write \(f_{I(a,r)}=(2r)^{-1}\int_{I(a,r)}f\) and
\[
m_f(a,r)=\frac1{2r}\int_{I(a,r)}|f(t)-f_{I(a,r)}|\,dt,
\qquad
O(f)=\sup_{\kappa>0}\kappa\int_{\mathbb R}\int_0^\infty \mathbf 1_{\{m_f(a,r)>\kappa\}}\frac{dr\,da}{r^2}.
\]
The integral in \(D\) is precisely the one-dimensional exceptional BSVY quantity for \(\gamma=-1\), and the measure in \(O\) is Frank's endpoint ball-oscillation measure.

**Theorem.** For every \(\Phi\) satisfying the preceding assumptions, \(f\in W^{1,1}(\mathbb R)\cap C_c(\mathbb R)\), and
\[
D(f)<\infty\ \Longleftrightarrow\ O(f)<\infty\ \Longleftrightarrow\ \sup_{0<s\le1/2}\frac{\Phi(s)}s<\infty.
\]
If the last supremum is infinite, each of \(\lambda\iint_{|f(x)-f(y)|>\lambda}|x-y|^{-2}\,dx\,dy\) and \(\kappa\iint_{m_f(a,r)>\kappa}r^{-2}\,da\,dr\) has infinite limsup as its level tends to zero.

In particular, for every \(\alpha>0\), \(\beta\in\mathbb R\), take \(\Phi_{\alpha,\beta}(s)=s^\alpha[\log(e/s)]^{-\beta}\) for sufficiently small positive \(s\), continued nondecreasingly and locally Lipschitz on the remainder of \([0,1/2]\). Both weak endpoint functionals are finite **if and only if** \(\alpha>1\), or \(\alpha=1\) and \(\beta\ge0\). Thus a second logarithm resolves the exact boundary inside the first-logarithm critical line.

## Assumptions and scope

The domain is the real line, with Lebesgue measure and the **absolute mean deviation**, not a median or a supremum over balls. All parameters and quantifiers are as stated. The hypotheses on \(\Phi\) are structural: monotonicity gives lower bounds from the side of the cusp, and \(|s\Phi'|\lesssim\Phi\) ensures a bounded linear envelope forces genuine Lipschitz regularity. Away from zero, the locally Lipschitz requirement is essential to that implication. At \(\Phi\equiv0\) all three conditions hold. No uniform constant over all admissible \(\Phi\) is asserted.

The function \(\Phi\) is absolutely continuous on \([0,1/2]\): it is monotone, continuous at zero, and Lipschitz on every compact subinterval of \((0,1/2]\). Since \(U\) is absolutely continuous and monotone on each of the two intervals where it is nonzero, \(\Phi\circ U\) is absolutely continuous on each such interval by the one-dimensional monotone change-of-variables property. Its total variation is at most \(2\Phi(1/2)\), and it has compact support and continuous endpoints. Consequently \(f\in W^{1,1}\cap C_c\), even in the nonmembership regime for the weak tests.

## Proof

**1. The linear cusp has bounded ball weak oscillation.** Fix \(r_*\in(0,1/(24e))\). For \(0<r<r_*\), split centers into \(|a|\le2r\) and \(|a|>2r\). In the former region, \(I(a,r)\subset(-3r,3r)\), so monotonicity of \(U\) near the origin gives
\[
m_U(a,r)\le U(3r)=[\log(e/(3r))]^{-1}.
\]
For any \(\kappa>0\), the inequality \(m_U(a,r)>\kappa\) in this region requires \(r>(e/3)e^{-1/\kappa}\). The center section has length \(4r\), and therefore
\[
\kappa\int_0^{r_*}\int_{|a|\le2r}\mathbf1_{\{m_U>\kappa\}}\frac{da\,dr}{r^2}
\le4\kappa\bigl[\log(3r_*/e)+1/\kappa\bigr]_+\le C.
\]
For \(|a|>2r\), a negative center sees only the zero portion of \(U\). If \(a>2r\), the interval lies in \([a/2,3a/2]\), where the derivative \(U'(t)=1/[t\log(e/t)^2]\) near zero has a local essential supremum bounded by an integrable majorant \(G(a)\), independent of \(r\). For instance, use \(C/[a\log(e/a)^2]\) when \(0<a<\varepsilon\), a finite bound when \(\varepsilon\le a\le2/e+r_*\), and zero elsewhere, for fixed small \(\varepsilon>0\). Thus \(m_U(a,r)\le2rG(a)\). Integration first in \(r\) yields
\[
\kappa\int_{\mathbb R}\int_0^{r_*}\mathbf1_{\{2rG(a)>\kappa\}}\frac{dr\,da}{r^2}
\le2\int_{\mathbb R}G(a)\,da<\infty.
\]
For \(r\ge r_*\), \(U\) is integrable with support \([0,2/e]\), and
\[
m_U(a,r)\le\|U\|_1/r.
\]
Moreover \(m_U(a,r)>0\) entails \(a\in[-r,2/e+r]\), a set of length \(2r+2/e\). Consequently the remaining weak-level contribution is bounded by
\[
\kappa\int_{r_*}^{\|U\|_1/\kappa}(2r+2/e)r^{-2}\,dr\le C
\]
when the upper endpoint exceeds \(r_*\), and is zero otherwise, because \(\kappa\log(C/\kappa)\) stays bounded for \(0<\kappa<C\). Therefore \(O(U)<\infty\).

**2. A bounded envelope suffices for both tests.** Suppose \(M=\sup_{0<s\le1/2}\Phi(s)/s<\infty\). For almost every \(0<s<s_0\), the derivative condition gives \(|\Phi'(s)|\le KM\). Local Lipschitz regularity away from zero and continuity at zero imply \(\Phi\) is globally Lipschitz on \([0,1/2]\), with some constant \(L<\infty\). Then \(|f(x)-f(y)|\le L|U(x)-U(y)|\). By Lemma 2.5 of Chen--Yang--Yuan--Zhang, \(D(U)<\infty\), so \(D(f)\le LD(U)<\infty\).

For any interval \(I\), since the average of \(U\) belongs to \([0,1/2]\), the triangle inequality and the Lipschitz property give
\[
\frac1{|I|}\int_I|\Phi(U)-(\Phi(U))_I|\le2L\frac1{|I|}\int_I|U-U_I|.
\]
Thus \(m_f(a,r)\le2Lm_U(a,r)\), and hence \(O(f)\le2L O(U)<\infty\). For \(L=0\), both quantities vanish directly.

**3. An unbounded envelope forces divergence of both tests.** Assume \(\sup_{0<s\le1/2}\Phi(s)/s=\infty\). Since \(\Phi\) is locally Lipschitz away from zero, there exists \(s_n\downarrow0\) with \(\Phi(s_n)/s_n\to\infty\). Write \(x_s=e\exp(-1/s)\), so \(U(x_s)=s\) for sufficiently small \(s\).

For the BSVY functional, take \(\lambda_s=\Phi(s)/2\) and integrate over \(x_s<x<\delta\) and \(-x<y<0\), where \(\delta\in(0,1/e)\) is fixed. On this set \(f(y)=0\), \(f(x)\ge\Phi(s)>\lambda_s\), and
\[
\lambda_s\iint_{|f(x)-f(y)|>\lambda_s}\frac{dx\,dy}{|x-y|^2}
\ge\frac{\Phi(s)}4\log(\delta/x_s)
=\frac{\Phi(s)}{4s}+O(\Phi(s)).
\]
For the mean-oscillation functional, restrict to \(r_s=8x_s<r<r_0\) and \(|a|<r/4\), for a fixed \(r_0>0\) small enough. The interval \(I(a,r)\) contains a negative subinterval of length \(r/4\) where \(f=0\) and a positive subinterval of length \(r/4\) with arguments at least \(r/8\), hence \(f\ge\Phi(s)\). Therefore \(m_f(a,r)\ge\Phi(s)/64\). With \(\kappa_s=\Phi(s)/128\), the center section has length \(r/2\), so
\[
\kappa_s\int_{\mathbb R}\int_0^\infty\mathbf1_{\{m_f>\kappa_s\}}\frac{dr\,da}{r^2}
\ge\frac{\Phi(s)}{256}\log(r_0/r_s)
=\frac{\Phi(s)}{256s}+O(\Phi(s)).
\]
Both lower bounds diverge along \(s=s_n\), while \(\lambda_{s_n},\kappa_{s_n}\to0\). This proves necessity and the asserted infinite-limsup strengthening.

**4. Two logarithmic scales.** For \(\alpha>0\), \(\beta\in\mathbb R\), on sufficiently small positive arguments let
\[
\Phi_{\alpha,\beta}(s)=s^\alpha[\log(e/s)]^{-\beta}.
\]
Its logarithmic derivative satisfies \(s\Phi'_{\alpha,\beta}(s)/\Phi_{\alpha,\beta}(s)=\alpha+\beta/\log(e/s)\), which stays positive and bounded near zero. Extend it beyond a sufficiently small cutoff by any nondecreasing locally Lipschitz continuation. Then
\[
\frac{\Phi_{\alpha,\beta}(s)}s=s^{\alpha-1}[\log(e/s)]^{-\beta}
\]
is bounded as \(s\downarrow0\) exactly for \(\alpha>1\), or \(\alpha=1\) and \(\beta\ge0\). The main equivalence yields the claimed sharp two-scale phase diagram.

## Verification

The proof uses only analytic comparisons, changes of variables, interval lengths, and the previously proved base-cusp BSVY estimate (Chen--Yang--Yuan--Zhang, Lemma 2.5). The critical near-tip weight is \(r^{-2}\), and integrating a length-\(r\) center section gives \(\int dr/r\); this logarithm is the source of the exact envelope \(\Phi(s)/s\). The constants \(1/4\), \(1/64\), and \(1/256\) in the lower bounds follow respectively from integrating \((x-y)^{-2}\) across a negative half-interval and from two disjoint length-\(r/4\) test subintervals. No numerical experiment or unstated exhaustive search is used as proof.

## Relationship to prior work

Chen--Yang--Yuan--Zhang (2026), Lemma 2.5, prove finite critical BSVY seminorm for the single logarithmic profile \(U\), and Lemma 3.10 analyzes a log-coordinate weak-\(L^1\) component; neither states a two-functional equivalence or an if-and-only-if nonlinear profile envelope. Frank (2026), Proposition 4, proves divergence of the weak ball-oscillation limit for particular powers strictly below the logarithmic exponent one, without an endpoint positive classification. The original Brezis--Seeger--Van Schaftingen--Yung paper (2024), including the exceptional \(p=1\), \(\gamma=-1\) discussion, develops the BSVY framework and its generic limitations, not the present joint envelope criterion. The present result combines a new boundedness argument for the critical mean-oscillation test with matching necessary cross-cusp lower bounds and extends to all profiles obeying the stated local logarithmic regularity.

## Limitations

The equivalence holds on the one-dimensional, nonnegative, monotone-composition class specified above, not across all \(W^{1,1}(\mathbb R)\), all \(BV\), higher dimensions, or arbitrary nonlinear compositions. The local derivative hypothesis on \(\Phi\) is essential for the supplied sufficiency argument, and no necessity claim is made without it. Neither sharp numerical constants nor the exact finite limits of the weak-level expressions are computed. Other endpoint parameters \(\gamma\in(-1,0)\) are not classified by this theorem.

## References

- Y. Chen, D. Yang, W. Yuan, Y. Zhang, *On Two Questions by Brezis et al Concerning the Critical Difference Quotient Characterization of First-Order Sobolev Spaces*, arXiv:2609.19029v1, Sections 2 and 3, particularly Lemmas 2.5 and 3.10, https://arxiv.org/html/2609.19029v1.
- R. L. Frank, *Another characterization of \(\dot W^{1,p}(\mathbb R^d)\)*, arXiv:2610.03426v1, Section 3, particularly Proposition 4, https://arxiv.org/html/2610.03426v1.
- H. Brezis, A. Seeger, J. Van Schaftingen, P.-L. Yung, *Families of functionals representing Sobolev norms*, *Analysis & PDE* **17** (2024), 943–979; arXiv:2109.02930v1, especially the exceptional endpoint discussion, https://arxiv.org/pdf/2109.02930.
