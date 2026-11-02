# Sharp universal future-weight envelopes for norm-bounded subnormal shifts

## Finding

Fix real numbers \(0<m<R\) and \(m\le s\le R\). Consider **every** subnormal unilateral weighted shift \(W e_n=\alpha_n e_{n+1}\) on \(\ell^2(\mathbb N_0)\), with strictly positive weights, \(\alpha_0^2=m\), \(\alpha_1^2=s\), and \(\|W\|^2\le R\). Define
\[
a=\frac{m(R-s)}{R-m},\qquad
\pi=\frac{m-a}{R-a}
=\frac{m(s-m)}{(R-m)^2+m(s-m)}.
\]
For each integer \(n\ge1\), the **sharp simultaneous bounds** are
\[
\boxed{\quad s\le\alpha_n^2\le U_n(m,s,R)
=\frac{(1-\pi)a^{n+1}+\pi R^{n+1}}
{(1-\pi)a^n+\pi R^n}.\quad}
\]
One lower-extremal shift and one upper-extremal shift respectively attain equality **at every index \(n\ge1\)**. Their Berger probability measures are
\[
\mu_-=(1-m/s)\delta_0+(m/s)\delta_s,
\qquad \mu_+=(1-\pi)\delta_a+\pi\delta_R.
\]
The upper measure is the unique upper maximizer for any fixed \(n\ge2\), and the lower measure is the unique lower minimizer for any fixed \(n\ge2\). In the degenerate cases \(s=m\) and \(s=R\) these measures coincide, and all admissible shifts coincide. At \(n=1\), every admissible shift has the same prescribed value \(s\).

For \(m<s<R\) and any fixed \(n\ge2\), the full attainable set of squared weights \(\alpha_n^2\) under the **upper norm bound** is \([s,U_n]\). If the norm is instead required to satisfy \(\|W\|^2=R\) exactly, that set is \((s,U_n]\): the sharp lower endpoint is not attained. In particular, a norm-\(\sqrt R\) subnormal shift can have an arbitrarily long initial tail approximating the flat value \(s\), but all its weights eventually approach \(R\) in square.

The upper extremizer makes the delay quantitative. Set \(s=m+\delta\) with \(\delta>0\) tending to zero, \(m,R\) fixed. For real \(t\ge0\), let
\[
\rho_\delta(t)=\frac{(1-\pi)a^{t+1}+\pi R^{t+1}}{(1-\pi)a^t+\pi R^t},\qquad
 t_\delta=\frac{\log((1-\pi)/\pi)}{\log(R/a)}.
\]
Then
\[
 t_\delta=\frac{\log((R-m)^2/(m\delta))}{\log(R/m)}+o(1),
\qquad
\rho_\delta(t_\delta+h)\longrightarrow
\frac{m+R(R/m)^h}{1+(R/m)^h}
\]
for each fixed real \(h\). This logarithmic delay with a bounded-width transition quantifies nonuniformity in near-flatness propagation.

## Assumptions and scope

A positive scalar weighted shift is subnormal if and only if its moments have a compactly supported Berger probability measure \(\mu\subseteq[0,\|W\|^2]\):
\[
 \gamma_0=1,\quad
 \gamma_n=\alpha_0^2\cdots\alpha_{n-1}^2=\int t^n\,d\mu(t),\quad
 \alpha_n^2=\gamma_{n+1}/\gamma_n.
\]
All moment denominators are positive because \(m>0\). The prescribed first two weights are equivalent to the three moment constraints \(\gamma_0=1\), \(\gamma_1=m\), \(\gamma_2=ms\). These are feasible precisely when \(m\le s\le R\) under \(0<m<R\). The assumptions restrict to the scalar subnormal class, not merely hyponormal shifts or arbitrary operator-valued weights. The operator norm is the largest absolute shift weight and its square is the upper support endpoint of \(\mu\).

## Proof

**1. Two canonical feasible measures.** The formulas for \(a,\pi\) give \(0\le a\le m\), \(0\le\pi\le1\), and
\[
(1-\pi)a+\pi R=m,\qquad
(1-\pi)a^2+\pi R^2=ms.
\]
Similarly the measure \(\mu_-\) has moments \(1,m,ms\). Hence both generate subnormal shifts with the prescribed first two weights and norm at most \(\sqrt R\). When \(m<s<R\), the upper measure has positive mass at \(R\), and its shift norm is exactly \(\sqrt R\).

**2. Lower bound and rigidity.** For every \(n\ge1\), Cauchy–Schwarz gives \(\gamma_{n+1}\gamma_{n-1}\ge\gamma_n^2\); hence \(\gamma_{n+1}/\gamma_n\) is nondecreasing. As \(\gamma_2/\gamma_1=s\), the lower bound follows. If equality holds for any \(n\ge2\), then the relevant Cauchy–Schwarz equality forces the support of \(t\,d\mu(t)\) to be a single positive point \(s\). The moment constraints then force \(\mu=\mu_-\), proving rigidity. The case \(s=m\) follows already from variance \(ms-m^2=0\).

**3. A polynomial upper dual certificate.** Fix \(n\ge2\), write \(c=U_n\), and set \(f(t)=t^{n+1}-ct^n\). Note \(0\le c\le R\), since \(c\) is a ratio of consecutive moments of \(\mu_+\). Let \(q\) be the unique polynomial of degree at most two interpolating \(f(a)\), \(f'(a)\), and \(f(R)\). The Hermite divided-difference identity, with \(h_j\) the complete homogeneous polynomial of degree \(j\) and the conventions \(h_0=1\), \(h_j=0\) for \(j<0\), gives
\[
\begin{aligned}
q(t)-f(t)&=(t-a)^2(R-t)\,f[a,a,R,t]\\
&=(t-a)^2(R-t)\left[
 h_{n-2}(a,a,t)+(R-c)h_{n-3}(a,a,R,t)
\right]\ge0
\end{aligned}
\]
for every \(0\le t\le R\). To check the identity directly, use the monomial divided-difference rule \(t^k[x_0,x_1,x_2,x_3]=h_{k-3}(x_0,x_1,x_2,x_3)\) and the recurrence \(h_j(a,a,R,t)=h_j(a,a,t)+Rh_{j-1}(a,a,R,t)\). Thus this certificate is valid for **every integer \(n\ge2\)**, even though the ordinary third derivative of \(f\) need not have one sign.

Every admissible \(\mu\) shares the first three moments of \(\mu_+\), so \(\int q\,d\mu=\int q\,d\mu_+\). At the two support points of \(\mu_+\), \(q=f\), while \(\int f\,d\mu_+=0\) by the definition of \(c\). Therefore
\[
\gamma_{n+1}-c\gamma_n=\int f\,d\mu
\le\int q\,d\mu=\int q\,d\mu_+=0,
\]
and dividing by \(\gamma_n>0\) proves \(\alpha_n^2\le U_n\). For \(m<s<R\), we have \(0<a<R\), and the displayed certificate is strictly positive at \(t\in[0,R]\setminus\{a,R\}\). Equality therefore forces \(\mu\) to be supported on \(\{a,R\}\), and the first moment fixes its masses uniquely, yielding \(\mu_+\). At the endpoints \(s=m,R\), the first two moments already force respectively \(\delta_m\) and \((1-m/R)\delta_0+(m/R)\delta_R\).

**4. Full attainable intervals and exact norm.** For \(m<s<R\), mix the two measures: \(\mu_\theta=(1-\theta)\mu_-+\theta\mu_+\), \(0\le\theta\le1\). Each has the same first three moments and therefore the prescribed two weights. The ratio \(\int t^{n+1}\,d\mu_\theta/\int t^n\,d\mu_\theta\) varies continuously between the two sharp endpoints. Its range is the whole closed interval, and no other values are possible. For \(\theta>0\) the measure has support endpoint \(R\), so its shift has exact norm \(\sqrt R\); the norm-exact range is \((s,U_n]\) for \(n\ge2\), with no lower equality by Step 2. For any measure \(\mu\), \(\gamma_{n+1}/\gamma_n\) increases to the top of its support, by moment log-convexity and \(\gamma_n^{1/n}\to\sup\operatorname{supp}\mu\). Thus every exact-norm-\(\sqrt R\) shift satisfies \(\alpha_n^2\to R\).

**5. Delayed propagation profile.** Write \(\delta=s-m\). Algebra gives
\[
 a=m-\frac{m\delta}{R-m},\quad
 \frac{\pi}{1-\pi}=\frac{m\delta}{(R-m)^2},\quad
 \rho_\delta(t)=\frac{a+RX_\delta(t)}{1+X_\delta(t)},\quad
 X_\delta(t)=\frac{\pi}{1-\pi}(R/a)^t.
\]
By the definition of \(t_\delta\), \(X_\delta(t_\delta+h)=(R/a)^h\). Since \(a\to m\), the limiting logistic profile follows. The stated asymptotic for \(t_\delta\) follows from \(\log(R/a)=\log(R/m)+O(\delta)\) and \(\delta\log(1/\delta)\to0\). This completes the proof.

## Verification

A dependency-free exact-rational checker is supplied in `checker.py`. Running `python checker.py` produced `PASS 99360 exact rational assertions`. It tests randomly chosen finite atomic Berger measures, matches their first two moments with the upper two-atomic measure, checks the bounds through multiple horizons, verifies the Hermite certificate polynomial identity at rational points, and tests both extremal measures. This finite computation tests the algebra but does not establish an infinite-horizon theorem; Steps 1–5 above do so.

## Relationship to prior work

Stampfli's scalar flatness theorem and the later operator-valued propagation results concern equality or structural propagation, not an explicit all-horizon upper envelope conditioned on the first two weights and a norm cap. The minimal-norm subnormal completion of Curto–Fialkow already supplies important lower-bound and completion structure; the **new quantitative focus here is the maximal possible future moment ratios under an externally fixed upper support bound**, the simultaneously extremal capped-norm measure, the complete fixed-index range under an exact norm constraint, and its nonuniform near-flat transition. The lower bound itself is the standard log-convex moment consequence, not independently asserted as a new fact.

The two-atomic recurrence of Lee–Yoon is also established background. Their two-variable completion results do not state this cap-constrained, all-index extremal inequality. The upper certificate is a specialized Hermite polynomial inequality whose nonnegativity persists even where a direct third-derivative sign argument would not apply.

## Limitations

The theorem is limited to **scalar subnormal unilateral shifts**, fixed first two squared weights, and an upper bound on the squared operator norm. It does not address matrix-weighted or merely hyponormal shifts, or completion with three or more initial weights. The general classical moment literature may contain the polynomial extremal step under other terminology. The full 1993 Curto–Fialkow article was not available for complete comparison; its accessible abstract establishes minimal-norm and minimal-moment completions, but cannot certify absence of a related upper-envelope result elsewhere in that article. The novelty claim is consequently provisional and subject to independent bibliographic scrutiny. The finite checker is not proof or independent mathematical certification.

## References

1. R. Curto, A. Ech-charyfy, H. El Azhar, E. H. Zerouali, *Propagation Phenomena for Operator-Valued Weighted Shifts*, Results in Mathematics **81** (2026), article 16; first online December 13, 2025. DOI: https://doi.org/10.1007/s00025-025-02572-6. Open article: https://link.springer.com/article/10.1007/s00025-025-02572-6.
2. J. Stampfli, *Which weighted shifts are subnormal?*, Pacific Journal of Mathematics **17** (1966), 367–379.
3. R. Curto and L. Fialkow, *Recursively generated weighted shifts and the subnormal completion problem*, Integral Equations and Operator Theory **17** (1993), 202–246. DOI: https://doi.org/10.1007/BF01200218.
4. S. H. Lee and J. Yoon, *Recursiveness and propagation for 2-variable weighted shifts*, Linear Algebra and its Applications **504** (2016), 228–247. DOI: https://doi.org/10.1016/j.laa.2016.04.006.
5. R. Curto, I. B. Jung and W. Y. Lee, *Extensions and extremality of recursively generated weighted shifts*, Proceedings of the American Mathematical Society **130** (2002), 565–576. DOI: https://doi.org/10.1090/S0002-9939-01-06079-8.
