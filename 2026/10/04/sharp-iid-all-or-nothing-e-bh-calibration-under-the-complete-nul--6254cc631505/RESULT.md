# Sharp iid all-or-nothing e-BH calibration under the complete null
## Finding
Let \(K\ge 1\) and \(\alpha\in(0,1)\). Under the complete null, consider iid two-point null e-values
\[
E_i=cB_i,\qquad B_i\sim\operatorname{Bernoulli}(p),\qquad pc\le 1,
\]
with the \(B_i\) independent. For the base e-BH procedure, the exact FDR envelope over all such \((p,c)\) is
\[
M_{K,\alpha}
=
\max_{1\le r\le K}
\Pr\!\left\{\operatorname{Bin}\!\left(K,\frac{r\alpha}{K}\right)\ge r}\right\}.
\]
Equivalently,
\[
M_{K,\alpha}
=
\max_{1\le r\le K}
\sum_{j=r}^K
{K\choose j}
\left(\frac{r\alpha}{K}\right)^j
\left(1-\frac{r\alpha}{K}\right)^{K-j}.
\]
If
\[
0<\alpha<\alpha_0:=\frac{1}{e^2+1/2}=0.126757876666\ldots,
\]
then the unique extremizing law is
\[
p=\frac{\alpha}{K},\qquad c=\frac{K}{\alpha},
\]
and therefore
\[
M_{K,\alpha}
=1-\left(1-\frac{\alpha}{K}\right)^K
\longrightarrow 1-e^{-\alpha}<\alpha.
\]
For \(\alpha=0.05\), this gives \(M_{100,0.05}=0.04878246975766576\) and limiting value \(1-e^{-0.05}=0.048770575499285984\).

## Assumptions and scope
The result concerns the base e-BH rule applied to \(K\) null hypotheses, all of which are true. The e-values are independent and identically distributed, and each has exactly two support points, \(0\) and \(c\). The validity condition is only \(\mathbb E[E_i]=pc\le1\). The family contains the standard all-or-nothing e-value form emphasized in the e-value literature.

The result does not claim an envelope over all independent e-value distributions, over heterogeneous two-point laws, or in mixtures of null and non-null hypotheses. The low-level closed form is proved for \(\alpha<\alpha_0\); the finite maximization formula is exact for every \(\alpha\in(0,1)\).

## Proof
Write \(N=\sum_{i=1}^K B_i\). Conditional on \(N\), the ordered e-values consist of \(N\) copies of \(c\) followed by zeros. By the definition of base e-BH, there is a rejection exactly when some \(k\le N\) satisfies
\[
\frac{kc}{K}\ge\frac{1}{\alpha}.
\]
Because the left side increases with \(k\), this is equivalent to
\[
Nc\ge\frac{K}{\alpha}.
\]
Under the complete null, the false discovery proportion is one on this event and zero otherwise. Hence
\[
\operatorname{FDR}(p,c)
=
\Pr\!\left\{N\ge\left\lceil\frac{K}{\alpha c}\right\rceil}\right\}.
\]
For fixed \(p\), this probability is nondecreasing in \(c\). Validity gives \(c\le1/p\), so the worst valid choice is \(c=1/p\). Therefore
\[
\operatorname{FDR}(p,1/p)
=
\Pr\!\left\{\operatorname{Bin}(K,p)\ge\left\lceil\frac{Kp}{\alpha}\right\rceil}\right\}.
\]
If \(p>\alpha\), the threshold exceeds \(K\), so the FDR is zero. For \(r=1,\ldots,K\), on
\[
\frac{(r-1)\alpha}{K}<p\le\frac{r\alpha}{K},
\]
the threshold equals \(r\). A binomial upper tail at fixed threshold is strictly increasing in \(p\), so the maximum on that interval occurs at \(p=r\alpha/K\). This proves the exact finite maximization formula.

It remains to identify the maximizer at small \(\alpha\). For \(r\ge2\), set \(p=r\alpha/K\) and \(N\sim\operatorname{Bin}(K,p)\). Since \(\mathbf 1_{\{N\ge r\}}\le {N\choose r}\),
\[
\Pr(N\ge r)
\le
\mathbb E{N\choose r}
=
{K\choose r}\left(\frac{r\alpha}{K}\right)^r
\le
(e\alpha)^r.
\]
When \(\alpha<1/e\), every \(r\ge2\) term is at most \(e^2\alpha^2\). For \(r=1\),
\[
F_1
=1-\left(1-\frac{\alpha}{K}\right)^K
\ge
\alpha-\frac{K-1}{2K}\alpha^2
\ge
\alpha-\frac{\alpha^2}{2},
\]
where the first inequality is the second Bonferroni bound for the union of \(K\) independent events of probability \(\alpha/K\). Thus \(F_1>F_r\) for every \(r\ge2\) whenever
\[
e^2\alpha^2<\alpha-\frac{\alpha^2}{2},
\]
which is exactly \(\alpha<1/(e^2+1/2)\). Strict monotonicity inside each threshold interval then makes \(p=\alpha/K\), \(c=K/\alpha\) the unique extremizing two-point law. Finally, the standard exponential limit yields
\[
\left(1-\frac{\alpha}{K}\right)^K\to e^{-\alpha}.
\]

## Verification
The accompanying verifier independently evaluates the binomial-tail maximization, checks the claimed one-spike optimizer for \(\alpha\in\{0.01,0.05,0.10\}\) and \(1\le K\le200\), and reproduces the reported \(\alpha=0.05\) numerical values. These finite calculations are consistency checks; the all-\(K\) and all-\(\alpha<\alpha_0\) statements are established by the analytic inequalities in the proof.

## Relationship to prior work
Wang and Ramdas define the base e-BH procedure by the threshold condition \(k e_{[k]}/K\ge1/\alpha\), prove FDR control for arbitrary dependence, and explicitly discuss all-or-nothing e-values. Their sharpness example uses a common event shared by all null e-values and attains the general FDR bound exactly. They also derive a PRDS bound that applies under independence, but it is expressed through marginal tail functionals rather than the exact joint rejection probability for this iid two-point family.

The present calculation instead resolves the complete-null FDR exactly within the canonical iid all-or-nothing family, optimizes over every valid two-point calibration, and shows that at usual FDR levels the extremizer is the one-spike law \(p=\alpha/K\), \(c=K/\alpha\). It therefore quantifies a strict independence-induced gap between this natural family and the perfectly dependent sharpness construction.

Searches for equivalent statements included combinations of “e-BH”, “iid”, “all-or-nothing”, “two-point e-values”, “complete null”, “binomial”, and “exact FDR”. The inspected primary e-BH paper and later e-BH calibration literature did not state the finite binomial envelope or the one-spike optimizer.

## Limitations
The theorem is intentionally narrow. It does not establish the sharp FDR under arbitrary independent e-value distributions, does not cover heterogeneous two-point laws, and does not address power under alternatives. The constant \(\alpha_0\) is a sufficient range obtained from a simple factorial-moment bound; no claim is made that it is the largest level for which the one-spike law is globally optimal for every \(K\).

## References
1. Ruodu Wang and Aaditya Ramdas, “False Discovery Rate Control with E-values,” arXiv:2009.02824v1, first public 2020-09-06; later Journal of the Royal Statistical Society Series B 84(3), 2022, DOI:10.1111/rssb.12489.
2. Junu Lee and Zhimei Ren, “Boosting e-BH via Conditional Calibration,” arXiv:2404.17562v1, first public 2024-04-26.
