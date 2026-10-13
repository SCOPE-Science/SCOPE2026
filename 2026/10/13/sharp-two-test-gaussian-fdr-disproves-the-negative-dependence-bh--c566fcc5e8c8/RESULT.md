# Sharp two-test Gaussian FDR disproves the negative-dependence BH conjecture

## Finding

**Theorem.** Fix \(0<\alpha<1/2\). Apply the ordinary Benjamini--Hochberg (BH) step-up procedure at level \(\alpha\) to two one-sided normal-test \(p\)-values, one under a true null and the other under a false null. Among all such bivariate normal models with unit marginal variances, arbitrary positive mean for the nonnull statistic, and strictly negative correlation \(-1<\rho<0\), the exact supremum of false discovery rate is

\[
\sup_{\mu>0,\,-1<\rho<0}\operatorname{FDR}_{\mathrm{BH},2}(\alpha;\mu,\rho)=\frac{3\alpha}{4}.
\]

This supremum is approached as \(\rho\downarrow-1\) for a specific, finite, positive nonnull mean. At \(\alpha=1/20\), the explicit positive-definite model with

\[
\rho=-\frac{99999999}{100000000},\qquad
\mu=-\Phi^{-1}(1/40)-\Phi^{-1}(1/20)>0
\]

satisfies the rigorous, nonasymptotic inequalities

\[
\operatorname{FDR}_{\mathrm{BH},2}\geq\frac{317}{10000}
>\frac{30307}{1088000}
>\frac12\widetilde s_2(1/20).
\]

Here \(\Phi\) is the standard normal distribution function and \(\widetilde s_2\) is the proposed bound in equation (26) and the final-section BH conjecture of Chi, Ramdas, and Wang [1]. Consequently, **that Gaussian negative-dependence BH conjecture is false, even for two tests, with one true null and a nonsingular Gaussian covariance matrix**.

## Assumptions and scope

A true-null \(p\)-value \(U\) is uniform on \([0,1]\). A false-null \(p\)-value \(V\) need not be uniform. For the Gaussian subclass take \((Y_1,Y_2)\) jointly normal with

\[
\mathbb E Y_1=0,\quad \mathbb E Y_2=\mu>0,\quad
\operatorname{Var}(Y_1)=\operatorname{Var}(Y_2)=1,\quad
\operatorname{Corr}(Y_1,Y_2)=\rho<0,
\]

and set \(U=\Phi(-Y_1)\), \(V=\Phi(-Y_2)\). These are one-sided upper-tail tests of zero-mean normal null hypotheses; only the first null is true. For \(-1<\rho<0\) the Gaussian covariance is positive definite. False discovery rate means \(\mathbb E[F/(R\vee1)]\), where \(F\) is the number of rejected true nulls and \(R\) the total number of rejections. No assumption on the joint law of \((U,V)\) is needed for the first lemma.

The BH step-up thresholds for exactly two hypotheses are \(\alpha/2\) and \(\alpha\). Values on thresholds have probability zero in our continuous Gaussian models. The theorem concerns the supremum over admissible parameters, not an asserted interior maximizer.

## Proof

**1. Universal two-test inequality.** For any uniform \(U\) and arbitrary \(V\), both hypotheses are rejected iff \(\max(U,V)\leq\alpha\). When both are not rejected, the sole rejected hypothesis is the null exactly when \(U\leq\alpha/2\) and \(V>\alpha\). Hence

\[
\begin{aligned}
\operatorname{FDR}
&=\Pr(U\leq\alpha/2,V>\alpha)
 +\tfrac12\Pr(U\leq\alpha,V\leq\alpha)\\
&=\frac\alpha2+\frac12\left[
\Pr(\alpha/2<U\leq\alpha,V\leq\alpha)
-\Pr(U\leq\alpha/2,V\leq\alpha)
\right]\\
&\leq\frac\alpha2+\frac12\Pr(\alpha/2<U\leq\alpha)
=\frac{3\alpha}{4}.
\end{aligned}
\]

This is a universal inequality, also implied numerically by the two-test Benjamini--Yekutieli harmonic bound. The issue addressed here is whether a *negatively Gaussian* null/nonnull pair can attain it arbitrarily closely.

**2. Gaussian negative-dependence extremizer at the boundary.** Let \(q(t)=\Phi^{-1}(t)\) and set

\[
 a=q(\alpha/2)+q(\alpha)<0,\qquad \mu=-a>0.
\]

For one standard normal \(Z\), take \(Y_1=-Z\) and \(Y_2=Z-a\); the centered correlation is \(-1\). Thus \(U=\Phi(Z)\) and \(V=\Phi(-Z+a)\). Monotonicity of \(\Phi\) gives the threshold identity

\[
\{V\leq\alpha\}=\{Z\geq q(\alpha/2)\}
=\{U\geq\alpha/2\}\quad\text{almost surely}.
\]

The two events subtracted in the universal identity then have probabilities \(\alpha/2\) and zero, respectively. Therefore \(\operatorname{FDR}=3\alpha/4\) exactly in this (possibly singular) boundary model.

To obtain positive-definite covariance, let \(Z,W\) be independent standard normals and for \(-1<\rho<0\) set

\[
Y_1=-Z,\qquad Y_2=\rho Y_1+\sqrt{1-\rho^2}\,W+\mu.
\]

Then the means are \((0,\mu)\), both variances are one, and the correlation is \(\rho\). As \(\rho\downarrow-1\), \(Y_2\to Z+\mu\) almost surely. Each normal marginal has zero mass on either BH threshold \(\alpha/2\) or \(\alpha\). Thus the rejection indicators and false discovery proportion converge almost surely to the boundary model; bounded convergence yields \(\operatorname{FDR}\to3\alpha/4\). Together with step 1, this proves the exact supremum in the stated strictly negative, positive-definite Gaussian family.

**3. An explicit nonsingular counterexample with rational bounds.** Fix \(\alpha=1/20\), set \(\mu=-q(1/40)-q(1/20)\), and select

\[
\rho=-1+10^{-8}=-\frac{99999999}{100000000}.
\]

Compare the Gaussian \(Y_2=\rho Y_1+\sqrt{1-\rho^2}\,W+\mu\) with the boundary version \(Y_2^*=Z+\mu\), on the same underlying pair \((Z,W)\). Their difference is

\[
\Delta=Y_2-Y_2^*=(\rho+1)Y_1+\sqrt{1-\rho^2}\,W,
\qquad \mathbb E\Delta^2=2(1+\rho)=2\cdot10^{-8}.
\]

Let \(B=\{\Phi(-Y_2)\leq\alpha\}\), \(B^*=\{\Phi(-Y_2^*)\leq\alpha\}\). If \(|\Delta|\leq\varepsilon\), the truth of these events can differ only if \(|Z-q(1/40)|\leq\varepsilon\). As the standard normal density is everywhere less than \(1/2\), and by Chebyshev's inequality,

\[
\Pr(B\triangle B^*)
\leq\Pr(|Z-q(1/40)|\leq\varepsilon)
+\Pr(|\Delta|>\varepsilon)
<\varepsilon+\frac{2\cdot10^{-8}}{\varepsilon^2}.
\]

Take \(\varepsilon=1/200\). The right-hand side is

\[
\frac1{200}+\frac1{1250}=\frac{29}{5000}.
\]

The exact two-test FDR formula in step 1 depends on \(V\) only through the indicator \(\mathbf 1_{\{V\leq\alpha\}}\), and the absolute change in false discovery proportion when this indicator changes is at most one. Since \(U\) is coupled identically, the FDRs differ by at most \(\Pr(B\triangle B^*)\). Therefore

\[
\operatorname{FDR}(\rho)
\geq\frac{3}{80}-\frac{29}{5000}
=\frac{317}{10000}.
\]

Equation (26) of [1] defines

\[
\widetilde s_K(\alpha)=\min\!\left\{
\alpha+2\alpha^2+\frac92\alpha^3+
\frac{(e\alpha)^4}{\sqrt{8\pi}\,(1-e\alpha)_+},\ 1\right\}.
\]

Using only \(e<3\) and \(\pi>2\), at \(\alpha=1/20\) its first branch is strictly less than

\[
\frac1{20}+\frac2{20^2}+\frac9{2\cdot20^3}
+\frac{81}{4\cdot20^4(1-3/20)}
=\frac{30307}{544000}.
\]

With exactly one true null and two hypotheses, the conjectured RHS is \(\widetilde s_2(1/20)/2<30307/1088000\). Direct cross multiplication proves \(317/10000>30307/1088000\), completing the explicit strict violation. The source uses the Gaussian negative-dependence definition permitting shifted joint normals with nonpositive off-diagonal correlations [1, Section 2, equation (11)]; this model satisfies that definition even without the limiting singular case.

## Verification

The accompanying `verify.py` uses Python standard-library `fractions.Fraction` arithmetic to check the nonasymptotic rational lower bound, the upper bound for the conjectured expression, and their strictly positive gap, together with independent normal-CDF threshold identities and optional numerical quadrature checks. Run `python3 verify.py` with Python 3.10 or later. Numerical integration is diagnostic and is not used in any proof. The general \(0<\alpha<1/2\) supremum follows from steps 1 and 2, and the explicit nonsingular counterexample follows from the exact rational bounds in step 3.

## Relationship to prior work

Chi, Ramdas, and Wang [1] developed negative-dependence bounds for Simes and BH and in their Section 7 explicitly proposed \(\operatorname{FDR}\leq(K_0/K)\widetilde s_K(\alpha)\) for negatively Gaussian dependent \(p\)-values. Their Section 3 Simes results concern uniform null \(p\)-values, whereas their BH conjecture includes nonnull coordinates. The present example exploits that distinction: its second coordinate has a shifted normal distribution and is not null-uniform. Their published upper bound under only weak negative dependence of the null coordinates is not contradicted.

Benjamini and Yekutieli [2] already provide the arbitrary-dependence harmonic correction. The universal \(3\alpha/4\) upper bound is therefore **not claimed to be new**. The substantive new assertion is that this worst-case constant remains the exact *supremum in the strictly negatively Gaussian null/nonnull subclass*, and that a fully specified positive-definite Gaussian pair violates the stronger conjectured Gaussian bound.

A separate published mathematical record on the size of the Simes test under pairwise independence for three uniform nulls addresses a different class (three true nulls and non-Gaussian pairwise independence), and does not imply the two-test null/nonnull Gaussian claim [3]. Results on two-sided Gaussian BH concern \(p\)-values that need not be Gaussian-dependent after taking absolute values; they do not cover this one-sided construction.

## Limitations

The theorem covers exactly two tests with exactly one true null and one shifted Gaussian false null, at \(0<\alpha<1/2\). It does not assert a dimension-free envelope for arbitrary numbers of tests, or a new proof of the classic arbitrary-dependence correction. The supremum over nonsingular Gaussian covariances is shown by a limiting family, not asserted to be attained at a finite interior correlation. The explicit fixed-correlation witness has strong negative correlation near \(-1\), but remains positive definite. An earlier, equivalently formulated special Gaussian sharpness example cannot be excluded solely from bibliographic searches; independent priority adjudication has not occurred.

## References

[1] Ziyu Chi, Aaditya Ramdas, and Ruodu Wang, *Multiple testing under negative dependence*, arXiv:2212.09706 (initial public version 2022-12-19; full text version 4, 2024-05-08), Section 2 equation (11), Section 3 equation (26), Section 5 and Section 7. https://arxiv.org/abs/2212.09706 ; https://arxiv.org/html/2212.09706v4 .

[2] Yoav Benjamini and Daniel Yekutieli, *The control of the false discovery rate in multiple testing under dependency*, The Annals of Statistics **29** (2001), 1165--1188. DOI:10.1214/aos/1013699998. The harmonic arbitrary-dependence bound is also reviewed in [1, Section 5].

[3] *Sharp Simes size under pairwise independence for three uniform p-values*, published mathematical research record, 2026-09-20, identifier `2026/9/20/SCOPE-sharp-simes-size-under-pairwise-independence--9fdb218c11c0` (only the scientific result is used as an overlap comparator).
