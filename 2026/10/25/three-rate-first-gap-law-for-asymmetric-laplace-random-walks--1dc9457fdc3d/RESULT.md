# Three-rate first-gap law for asymmetric Laplace random walks

## Finding
Fix any two rates \(a,b>0\), not necessarily equal, and an integer \(n\ge1\). For the walk specified below, its first descending gap from the largest visited height has the exact three-exponential survival law
\[
\Pr(G_n>w)=q_n^+e^{-aw}+q_n^-e^{-bw}+(1-q_n^+-q_n^-)e^{-(a+b)w},\quad w\ge0.
\]
The weights are explicit through
\[
Q_+(z)=\sum_{n\ge0}q_n^+z^n=\frac{\sqrt{(a+b)^2-4abz}-(a-b)}{2b(1-z)},\qquad
Q_-(z)=\frac{\sqrt{(a+b)^2-4abz}+(a-b)}{2a(1-z)}.
\]
They are nonnegative and sum to at most one for every \(n\ge1\). A notable boundary is the drift transition in the *sharp* total variation rate. At \(a=b\),
\[
d_{\rm TV}(\mathcal L(G_n),\operatorname{Exp}(2a))=\frac{1}{2}\frac{\binom{2n}{n}}{4^n}\sim\frac{1}{2\sqrt{\pi n}}.
\]
At \(a\ne b\), set \(\rho=4ab/(a+b)^2<1\), and define
\[
C(a,b)=\frac{a+b}{(a-b)^2\sqrt\pi}\max_{w\ge0}\big\{a(e^{-aw}-e^{-(a+b)w})+b(e^{-bw}-e^{-(a+b)w})\big\}>0.
\]
Then, for the limiting random variable \(G_\infty\) described below,
\[
d_{\rm TV}(\mathcal L(G_n),\mathcal L(G_\infty))\sim C(a,b)\rho^n n^{-3/2}.
\]

## Assumptions and scope
Let \(X_1,X_2,\ldots\) be independent, identically distributed real random variables, with density
\[
f(x)=\frac{ab}{a+b}\begin{cases}e^{-ax},&x>0,\\ e^{bx},&x<0,\end{cases}\quad a,b>0.
\]
Let \(S_0=0\), \(S_j=\sum_{i=1}^jX_i\) and define \(G_n\) as the largest minus second-largest of the \(n+1\) numbers \(S_0,\ldots,S_n\), for each integer \(n\ge1\). Heights are distinct almost surely. Define the strict persistence probabilities \(q_0^+=q_0^-=1\), and, for \(n\ge1\),
\[
q_n^+=\Pr(S_1>0,\ldots,S_n>0),\qquad q_n^-=\Pr(S_1<0,\ldots,S_n<0).
\]
All statements hold for every real \(a,b>0\); the distinct-rate asymptotics hold with these rates fixed as \(n\to\infty\). There are no lattice increments, ties, or conditioning on eventual return.

## Proof
**1. Gap decomposition at the unique maximum.** For \(w\ge0\) and integer \(j\ge1\), define \(q_j^+(w)=\Pr(S_1>w,\ldots,S_j>w)\), and define \(q_j^-(w)\) analogously with all inequalities \(S_i<-w\). Put \(q_0^\pm(w)=1\). If the walk's largest value occurs at time \(k\), the event \(G_n>w\) is exactly that its backward increments' partial sums are all \(>w\) and its forward increments' partial sums are all \(<-w\). These independent blocks give
\[
\Pr(G_n>w)=\sum_{k=0}^{n}q_k^+(w)q_{n-k}^-(w).
\]
Given \(X_1>w\), the memoryless property gives \(X_1-w\sim\operatorname{Exp}(a)\), exactly the law of \(X_1\) conditional on positivity. Independence of subsequent increments then yields \(q_j^+(w)=e^{-aw}q_j^+\) for each \(j\ge1\). Likewise \(q_j^-(w)=e^{-bw}q_j^-\). Splitting the convolution into \(k=0\), \(k=n\), and \(1\le k\le n-1\) gives
\[
\Pr(G_n>w)=q_n^+e^{-aw}+q_n^-e^{-bw}+e^{-(a+b)w}\sum_{k=1}^{n-1}q_k^+q_{n-k}^-.
\]
At \(w=0\), the disjoint events that the unique maximum is at \(k\) partition the sample space; thus \(\sum_{k=0}^{n}q_k^+q_{n-k}^-=1\), proving both the three-rate law and nonnegativity of its weights.

**2. Exact persistence generating functions.** Write \(\tau_+=\inf\{j\ge1:S_j>0\}\), \(\tau_-=\inf\{j\ge1:S_j<0\}\). For \(|z|<1\), let \(F_+(z)=\mathbb E[z^{\tau_+};\tau_+<\infty]\) and \(F_-(z)\) similarly. Overshoots at either first strict crossing are exponential with rates \(a\) or \(b\), respectively, by the same memorylessness argument. The elementary ascending–descending ladder factorization (or geometric stopping at the first crossing on each side), on the imaginary transform axis, is
\[
1-z\frac{ab}{(a-t)(b+t)}
=\left(1-F_+(z)\frac a{a-t}\right)\left(1-F_-(z)\frac b{b+t}\right).
\]
The numerator roots are \(t_\pm=[a-b\pm\sqrt{(a+b)^2-4abz}]/2\). Each factor vanishes at its root on the corresponding side, hence
\[
1-F_+(z)=\frac{t_+}{a},\qquad 1-F_-(z)=-\frac{t_-}{b}.
\]
Since \(q_n^+=\Pr(\tau_->n)\) and \(q_n^-=\Pr(\tau_+>n)\), their generating functions equal \((1-F_-)/(1-z)\) and \((1-F_+)/(1-z)\), yielding the stated square-root formulas. For a direct coefficient recipe, set \(\rho=4ab/(a+b)^2\) and
\[
c_j=(-1)^{j+1}\binom{1/2}{j}\rho^j>0\quad(j\ge1),\qquad H_n=\sum_{j=1}^n c_j.
\]
Then
\[
q_n^+=1-\frac{a+b}{2b}H_n,\qquad q_n^-=1-\frac{a+b}{2a}H_n\quad(n\ge0).
\]
These exact expressions also follow independently from the generalized Sparre–Andersen recurrence \(nq_n^+=\sum_{k=1}^nq_{n-k}^+\Pr(S_k>0)\) (and its negative counterpart), with \(\Pr(S_k>0)=\Pr(\operatorname{Bin}(2k-1,b/(a+b))\ge k)\), because \(X_i\) is a difference of independent exponentials.

**3. Limits and sharp rates.** If \(a\ne b\), \(\rho<1\), the binomial series gives \(H_\infty=1-\sqrt{1-\rho}=1-|a-b|/(a+b)\). Therefore
\[
q_\infty^+=\frac{(b-a)_+}{b},\qquad q_\infty^-=\frac{(a-b)_+}{a},
\]
and replacing \(q_n^\pm\) with these constants gives the nondegenerate limiting survival law. Standard binomial asymptotics yield \(c_j\sim\rho^j/(2\sqrt\pi j^{3/2})\). Summing the geometrically decaying remainder gives
\[
q_n^+-q_\infty^+\sim\frac{a(a+b)}{(a-b)^2\sqrt\pi}\rho^n n^{-3/2},\quad
q_n^--q_\infty^-\sim\frac{b(a+b)}{(a-b)^2\sqrt\pi}\rho^n n^{-3/2}.
\]
The survival-function difference is positive for every \(w>0\), and equals
\[
h_n(w)=(q_n^+-q_\infty^+)(e^{-aw}-e^{-(a+b)w})+(q_n^--q_\infty^-)(e^{-bw}-e^{-(a+b)w}).
\]
Its derivative changes sign exactly once, since multiplying by \(e^{(a+b)w}\) gives a strictly decreasing function of \(w\) with one zero. Hence the density difference changes sign exactly once and total variation is \(\max_{w\ge0}h_n(w)\). Boundedness of each basis function and uniform asymptotics of the two coefficients imply the stated positive sharp constant \(C(a,b)\).

When \(a=b\), \(q_n^+=q_n^-=\binom{2n}{n}/4^n\), by the central binomial expansion of \((1-z)^{-1/2}\), and the limiting survival is \(e^{-2aw}\). Then \(h_n(w)=2q_n^+(e^{-aw}-e^{-2aw})\), maximized at \(w=(\log2)/a\) with value \(q_n^+/2\). Stirling's formula gives the exact TV identity and its sharp \(n^{-1/2}\) asymptotic.

## Verification
The accompanying standalone script `verify_gap.py` uses exact rational arithmetic for \((a,b)=(1,1),(2,1),(1,3),(3,5)\) and each \(1\le n\le12\). It compares the square-root generating-function coefficients against an algebraically independent generalized Sparre–Andersen recurrence using exact binomial tails. It checks positivity, normalization, monotonicity, and the central-binomial specialization. Run `python3 verify_gap.py` with Python's standard library. This finite computation is a cross-check, not the proof of the all-\(n\) claim. The proof above establishes the infinite assertion.

## Relationship to prior work
Pitman and Tang [1] prove general random-walk convergence of near-extreme order statistics and a nonsharp quantitative bound; their later symmetric Laplace analysis [2] identifies the limiting extreme gap and related exact finite expectations. Majumdar, Mounaix, and Schehr [3] give gap generating functions under **symmetric** jump assumptions. De Bruyne, Majumdar, and Schehr [4] give finite-horizon gap distributions for **symmetric** continuous jumps (with a convention omitting \(S_0\)); their symmetric result does not cover unequal exponential rates. Our finite-horizon **asymmetric** three-rate law and explicit geometric-versus-polynomial total-variation crossover are different statements. The symmetric specialization is stated only as a consistency check and should not be construed as claiming prior discovery of symmetric gap formulas.

## Limitations
The result is exact only for the bilateral-exponential increment family, not general asymmetric increments; it makes no joint-gap or argmax-time claim. Rates \(a,b\) are fixed when taking asymptotics; no uniform near-critical scaling with \(a-b\to0\) is asserted. A related unindexed asymmetric walk paper could establish this formula, so a bounded search cannot establish worldwide priority. The numerical script checks finitely many parameter cases and horizons and supplies no independent audit.

## References
[1] J. Pitman and W. Tang, *Extreme order statistics of random walks*, arXiv:2007.13991, first posted 28 July 2020, https://arxiv.org/abs/2007.13991.

[2] J. Pitman and W. Tang, *Hidden symmetries and limit laws in the extreme order statistics of the Laplace random walk*, arXiv:2107.05095, first posted 11 July 2021, https://arxiv.org/abs/2107.05095.

[3] S. N. Majumdar, P. Mounaix, and G. Schehr, *On the gap and time interval between the first two maxima of long random walks*, arXiv:1405.1222, 2014, https://arxiv.org/abs/1405.1222.

[4] B. De Bruyne, S. N. Majumdar, and G. Schehr, *Universal order statistics for random walks and Lévy flights*, arXiv:2206.15057, 2022, https://arxiv.org/abs/2206.15057.
