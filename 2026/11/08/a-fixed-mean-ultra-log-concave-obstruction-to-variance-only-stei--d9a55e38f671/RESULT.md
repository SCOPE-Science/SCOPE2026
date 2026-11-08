# A fixed-mean ultra-log-concave obstruction to variance-only Stein sup-norm bounds

## Finding

**Theorem.** Fix \(w>0\). For \(0<\varepsilon\le 1/2\), let \(B_\varepsilon\) and \(P_\varepsilon\) be independent, with \(B_\varepsilon\sim\operatorname{Bernoulli}(1-\varepsilon)\) and \(P_\varepsilon\sim\operatorname{Poisson}(\varepsilon)\). Write \(X_\varepsilon=B_\varepsilon+P_\varepsilon\), and \(p_n=\Pr(X_\varepsilon=n)\). Define the constant-birth death rates \(d(0)=0\) and \(d(n)=w p_{n-1}/p_n\) for \(n\ge1\). For each subset \(A\subseteq\mathbb Z_{\ge0}\), let the bounded Stein solution satisfy \(g_A(0)=0\) and
\[
w g_A(n+1)-d(n)g_A(n)=\mathbf1_A(n)-\Pr(X_\varepsilon\in A),\qquad n\ge0.
\]
Then \(p_n>0\) for all \(n\), the mass function is **strictly ultra-log-concave**, \(\mathbb E X_\varepsilon=1\), and \(\operatorname{Var}(X_\varepsilon)=2\varepsilon-\varepsilon^2\). Moreover its exact indicator sup-norm Stein factor is
\[
\boxed{\Gamma_\varepsilon:=\sup_A\sup_{n\ge1}|g_A(n)|=\frac{1-\varepsilon e^{-\varepsilon}}{w}}.
\]
The maximizer occurs at \(n=1\), using \(A=\{0\}\) or its complement. Consequently,
\[
\boxed{\frac{w\Gamma_\varepsilon}{\sqrt{\operatorname{Var}(X_\varepsilon)}}=\frac{1-\varepsilon e^{-\varepsilon}}{\sqrt{2\varepsilon-\varepsilon^2}}\sim\frac1{\sqrt{2\varepsilon}}\longrightarrow\infty\quad(\varepsilon\downarrow0).}
\]
Thus there is **no** absolute constant \(C\) such that \(\Gamma\le C\sigma/w\) for every full-support log-concave target, even when the mean is identically one and the laws are strictly ultra-log-concave. This disproves the **second**, variance-only factor inequality in DeSalvo's Open Problem 8.2, not its first-difference inequality.

## Assumptions and scope

All parameters are fixed real numbers with \(w>0\) and \(0<\varepsilon\le1/2\). The state space is the entire set of nonnegative integers. The suprema range over **all** subsets \(A\) and all integer indices \(n\ge1\). The normalization is the density-form operator with **constant birth rate \(w\)**, death rate \(d(n)=w p_{n-1}/p_n\), and indicators (not arbitrary unit-norm signed test functions). The fixed mean equals one by construction. Strict ultra-log-concavity means \((n!p_n)^2>((n-1)!p_{n-1})((n+1)!p_{n+1})\) for every \(n\ge1\).

## Proof

**1. Exact mass function, variance, and ultra-log-concavity.** Convolving the independent Poisson and Bernoulli variables gives, for every integer \(n\ge0\),
\[
p_n=e^{-\varepsilon}\frac{\varepsilon^{n-1}}{n!}\bigl(\varepsilon^2+n(1-\varepsilon)\bigr).
\]
At \(n=0\), the formula reads \(p_0=\varepsilon e^{-\varepsilon}\), so it is valid without an exception. Put \(a=\varepsilon^2\), \(b=1-\varepsilon>0\), and \(q_n=n!p_n=e^{-\varepsilon}\varepsilon^{n-1}(a+bn)\). For every \(n\ge1\),
\[
q_n^2-q_{n-1}q_{n+1}=e^{-2\varepsilon}\varepsilon^{2n-2}b^2>0.
\]
This is strict ultra-log-concavity and implies ordinary strict log-concavity. Independence yields \(\mathbb E X_\varepsilon=(1-\varepsilon)+\varepsilon=1\) and \(\operatorname{Var}(X_\varepsilon)=\varepsilon(1-\varepsilon)+\varepsilon=2\varepsilon-\varepsilon^2\).

**2. General exact indicator envelope.** Let \(F_m=\sum_{i=0}^m p_i\) and \(G_{m+1}=\sum_{i=m+1}^{\infty}p_i=1-F_m\). Detailed balance gives \(d(n)p_n=w p_{n-1}\). Multiplying the centered Stein equation by \(p_n\) and telescoping gives, for every \(m\ge0\),
\[
g_A(m+1)=\frac{1}{wp_m}\sum_{i=0}^{m}p_i\bigl(\mathbf1_A(i)-\Pr(X_\varepsilon\in A)\bigr).
\]
The numerator is the covariance of \(\mathbf1_A(X_\varepsilon)\) with \(\mathbf1_{\{X_\varepsilon\le m\}}\). Its largest absolute value over all sets \(A\) is exactly \(F_m(1-F_m)\), attained by the lower-tail set or its complement. Therefore
\[
w\sup_A|g_A(m+1)|=\frac{F_mG_{m+1}}{p_m}.
\]
For the present distribution all tails decay geometrically past some index (the ratios in Step 3 decrease to zero), so these solutions are uniformly bounded, and recurrence gives their uniqueness among solutions with \(g_A(0)=0\).

**3. The first positive site dominates every later site.** Direct division of the mass formula gives, for \(j\ge1\),
\[
r_j:=\frac{p_j}{p_{j-1}}=\frac{\varepsilon}{j}\frac{\varepsilon^2+j(1-\varepsilon)}{\varepsilon^2+(j-1)(1-\varepsilon)}.
\]
Ordinary strict log-concavity gives \(r_{j+1}<r_j\). Moreover \(r_2<\varepsilon\) and \(r_3\le\varepsilon/2\): the latter is equivalent to \(2(a+3b)\le3(a+2b)\), which follows from \(a\ge0\). For any \(j\ge2\), geometric comparison of the decreasing ratios yields
\[
\frac{F_{j-1}G_j}{p_{j-1}}\le\frac{G_j}{p_{j-1}}\le\frac{r_j}{1-r_{j+1}}\le\frac{\varepsilon}{1-\varepsilon/2}\le\frac23.
\]
At \(j=1\), the exact envelope is \(F_0G_1/p_0=1-p_0=1-\varepsilon e^{-\varepsilon}\). On \((0,1/2]\), the function \(\varepsilon e^{-\varepsilon}\) is increasing, so
\[
1-\varepsilon e^{-\varepsilon}\ge1-\tfrac12 e^{-1/2}>\tfrac23,
\]
where the final strict inequality follows from \(e^{1/2}>1+1/2=3/2\). Thus the unique maximizing positive index is \(j=1\), proving the exact formula for \(\Gamma_\varepsilon\).

**4. Failure of variance-only scaling.** Since \(w\Gamma_\varepsilon=1-\varepsilon e^{-\varepsilon}\to1\) whereas \(\sigma_\varepsilon=\sqrt{2\varepsilon-\varepsilon^2}\to0\), their quotient diverges with the displayed sharp asymptotic. No uniform \(C\) can satisfy the proposed inequality on this class.

## Verification

Run `python3 checks/check.py` with a standard Python installation. The checker uses exact rational arithmetic for 10 parameter values and 80 ratio locations, plus 80-digit decimal arithmetic for truncated sums at 10 parameter values. It produced **1,170 passed assertions**. The numerical truncation is diagnostic only. All infinite-support statements are proved by Steps 1–4, including the exact maximizer at the first positive index.

## Relationship to prior work

DeSalvo (2026), Open Problem 8.2, explicitly conjectures both a first-difference bound and the uniform variance-scaled sup-norm estimate \(\Gamma\le C\sigma/w\) for all log-concave constant-birth targets. The theorem here **negates only the second** by giving strictly ultra-log-concave full-support targets with fixed mean and vanishing variance. Its pointwise envelope is the standard telescoping Stein-solution formula, also present in the Bessel special case of DeSalvo's Theorem 2.5; that identity is not claimed as new. The distinct contribution is the complete fixed-mean ultra-log-concave obstruction family and its exact sup-norm factor.

Brown and Xia (2001) and Eichelsbacher and Reinert (2008) develop general birth–death and Gibbs Stein bounds. The inspected latter work, especially its Lemma 2.4 and proof, gives nonuniform estimates in a unit-death normalization rather than the variance-only universal assertion refuted here. This manuscript does not claim priority for elementary Bernoulli–Poisson convolution identities or for the general Stein solution. A dedicated comparison with Brown and Xia's original full text remains an access limitation.

## Limitations

The theorem supplies a counterexample and the exact factor in its specified family, **not** a positive replacement theorem. It does not rule out \(\Gamma\le C\sigma/w\) under additional variance lower bounds or anti-concentration hypotheses, nor does it dispute the separate first-difference conjecture. The checker does not certify an infinite theorem and historical priority has not been independently adjudicated.

## References

1. S. DeSalvo, *Two moments suffice for Bessel approximation: Conditioned differences, contingency tables, and probabilistic divide-and-conquer*, arXiv:2611.00263v1, first submitted 2026-10-30, especially Theorem 2.5, Open Problem 8.2, and §§9–10. https://arxiv.org/html/2611.00263v1
2. P. Eichelsbacher and G. Reinert, *Stein's method for discrete Gibbs measures*, Annals of Applied Probability 18 (2008), 1588–1618, arXiv:0808.2877, especially Lemmas 2.1 and 2.4. https://arxiv.org/pdf/0808.2877
3. T. C. Brown and A. Xia, *Stein's method and birth–death processes*, Annals of Probability 29 (2001), 1373–1403, DOI:10.1214/aop/1015345606. Original full text was not accessible for inspection.
