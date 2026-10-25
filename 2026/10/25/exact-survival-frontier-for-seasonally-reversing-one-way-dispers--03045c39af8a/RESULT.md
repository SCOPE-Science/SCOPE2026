# Exact survival frontier for seasonally reversing one-way dispersal between two sink habitats

## Finding

Consider the two-habitat, two-season linear population model specified below. For every \(0<a<b\), every migration rate \(m>0\), and every complete season-cycle duration \(T>0\), its common population growth exponent is exactly

\[
\Lambda(m,T)=\frac{a-b-m}{2}+\frac{2}{T}\operatorname{arsinh}\!\left(\frac{m}{a+b+m}\sinh\frac{(a+b+m)T}{4}\right).
\]

Both \(T\mapsto\Lambda(m,T)\), at fixed \(m\), and \(m\mapsto\Lambda(m,T)\), at fixed \(T\), are **strictly increasing**. For every \(m>0\) there is exactly one \(T_c(m)>0\) for which \(\Lambda(m,T_c(m))=0\). The population decays for \(T<T_c(m)\) and grows for \(T>T_c(m)\). The frontier is smooth and strictly decreasing in \(m\); it obeys two sharp singular limits:

\[
T_c(m)=\frac{2}{a}\log\frac{a+b}{m}+o(1)\quad(m\downarrow0),
\qquad mT_c(m)\longrightarrow4x_*\quad(m\to\infty),
\]

where \(x_*\in(0,\infty)\) is the unique positive root of \(2a x_*\coth x_*=a+b\). These statements hold simultaneously for all admissible \(a,b,m,T\), without numerical fitting.

## Assumptions and scope

Let \(a,b\) be constants with \(0<a<b\). The state \(z=(z_1,z_2)^\top\) consists of continuous nonnegative abundance in two habitats. A complete environmental cycle has duration \(T>0\) and exactly two seasons of duration \(T/2\). In the first season, habitat 1 has local rate \(a\), habitat 2 has local rate \(-b\), and individuals migrate only from 2 to 1 at per-capita rate \(m>0\). In the second season, growth rates and migration directions swap. Equivalently, \(\dot z=A_1z\) for the first half of the cycle and \(\dot z=A_2z\) for the second, repeated periodically, with

\[
A_1=\begin{pmatrix}a&m\\0&-b-m\end{pmatrix},\qquad
A_2=\begin{pmatrix}-b-m&0\\m&a\end{pmatrix}.
\]

The model includes population gain/loss through the indicated intrinsic growth rates; migration is conservative between habitats. Both habitats are sinks without migration because their time-averaged intrinsic rate is \((a-b)/2<0\). There is no density regulation, demographic stochasticity, or partial-season duration mismatch. The growth exponent is defined for every nonzero initial vector in the nonnegative cone as

\[
\Lambda(m,T)=\lim_{t\to\infty}\frac{1}{t}\log(z_1(t)+z_2(t)).
\]

## Proof

**1. Exact Floquet root.** Write \(t_0=T/2\), \(K=a+b+m\), and \(P=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). Then \(A_2=PA_1P\), and the first-half propagator is

\[
E=e^{t_0A_1}=\begin{pmatrix}u&q\\0&v\end{pmatrix},\quad
u=e^{at_0},\quad v=e^{-(b+m)t_0},\quad
q=\frac{m}{K}(u-v)>0.
\]

The period propagator \(M=e^{t_0A_2}e^{t_0A_1}=(PE)^2\) has strictly positive entries. The real eigenvalues of \(PE=\left(\begin{smallmatrix}0&v\\u&q\end{smallmatrix}\right)\) are \(\mu_+=(q+\sqrt{q^2+4uv})/2>0\) and \(\mu_-<0\), with \(|\mu_-|<\mu_+\). Therefore \(\rho(M)=\mu_+^2\); Perron–Frobenius theory gives the stated initial-state-independent long-time growth exponent. Since

\[
\frac{q}{2\sqrt{uv}}=\frac{m}{K}\sinh\frac{KT}{4},
\qquad
\mu_+=\sqrt{uv}\exp\!\left[\operatorname{arsinh}\!\left(\frac{m}{K}\sinh\frac{KT}{4}\right)\right],
\]

using \(\log(uv)=(a-b-m)T/2\) yields the displayed formula for \(\Lambda\).

**2. Strict dependence on season duration.** Hold \(m>0\) fixed. Put \(h=m/K\in(0,1)\), \(s=KT/4>0\), and \(F(s)=\operatorname{arsinh}(h\sinh s)\). Then

\[
F(0)=0,\qquad F''(s)=\frac{h(1-h^2)\sinh s}{(1+h^2\sinh^2s)^{3/2}}>0,
\qquad \Lambda=\frac{a-b-m}{2}+\frac K2\frac{F(s)}s.
\]

Strict convexity and \(F(0)=0\) imply that \(F(s)/s\) strictly increases for \(s>0\). Also, \(F(s)/s\to h\) as \(s\downarrow0\), while \(F(s)/s\to1\) as \(s\to\infty\). Hence \(\Lambda(m,0^+)=(a-b)/2<0\) and \(\Lambda(m,\infty)=a>0\).

**3. Strict dependence on migration strength.** Hold \(T>0\) fixed and put \(q_0=(a+b)/K=1-h>0\). Direct differentiation of the closed formula, with \(s=KT/4\) and \(J=\sqrt{1+h^2\sinh^2s}\), gives

\[
2\partial_m\Lambda=-1+\frac{q_0(\sinh s)/s+h\cosh s}{J}.
\]

For every \(s>0\), \(\sinh s/s>1\) and

\[
(q_0+h\cosh s)^2-J^2=2q_0h(\cosh s-1)>0.
\]

All quantities being positive, the numerator is strictly larger than \(J\), so \(\partial_m\Lambda>0\). Taking \(m\downarrow0\) in the explicit formula gives \((a-b)/2\). Taking \(m\to\infty\), for fixed \(T>0\), gives \(a\) (the cancellation is immediate using \(\operatorname{arsinh}(h\sinh s)=s+\log h+o(1)\) as \(s\to\infty\) and \(h\to1\)).

**4. The unique smooth survival frontier.** Step 2 and continuity prove the unique zero \(T_c(m)\) and the strict sign split. Since \(\partial_T\Lambda>0\) and \(\partial_m\Lambda>0\), the implicit-function theorem gives a smooth frontier with \(T_c'(m)=-\partial_m\Lambda/\partial_T\Lambda<0\). Equivalently, writing \(\operatorname{arsinh}\) as its inverse and using \(b+m-a>0\), the exact survival test is

\[
\Lambda(m,T)\gtrless0\quad\Longleftrightarrow\quad
\frac{m}{a+b+m}\sinh\frac{(a+b+m)T}{4}\gtrless
\sinh\frac{(b+m-a)T}{4}.
\]

The comparison sign is the same for growth, equality, and decay, respectively. Strict migration monotonicity and the \(m\)-limits in Step 3 imply \(T_c(m)\to\infty\) as \(m\downarrow0\) and \(T_c(m)\to0\) as \(m\to\infty\).

**5. The low-migration endpoint.** At the zero, write \(y=KT_c(m)/4\), \(d=(b+m-a)/K\). Then \(y\to\infty\) as \(m\downarrow0\), while \(d\to(b-a)/(a+b)\in(0,1)\). The threshold identity from Step 4 is

\[
\frac mK\,e^{(1-d)y}\frac{1-e^{-2y}}{1-e^{-2dy}}=1.
\]

Because \((1-d)y=aT_c(m)/2\), the ratio of the two parentheses tends to one, so \(\frac mK e^{aT_c(m)/2}\to1\). Taking logarithms gives \(T_c(m)=\frac2a\log[(a+b)/m]+o(1)\).

**6. The high-migration endpoint.** Let \(x_m=KT_c(m)/4\), and define \(\alpha=(a+b)/K\), \(\beta=2a/K\). The exact critical equation reads

\[
(1-\alpha)\sinh x_m=\sinh((1-\beta)x_m).
\]

For a fixed \(x>0\), multiply the left-minus-right expression by \(K\) and take \(m\to\infty\); the limit is

\[
G(x)=2ax\cosh x-(a+b)\sinh x.
\]

The quotient \(x\coth x\) strictly increases from \(1\) to infinity, and \((a+b)/(2a)>1\). Hence \(G\) has exactly one positive root \(x_*\), with \(G(x)<0\) below it and \(G(x)>0\) above it. Choose any \(0<x_-<x_*<x_+\). The finite-\(K\) critical-expression signs at \(x_-\) and \(x_+\) eventually agree with those of \(G\). The uniqueness of the positive critical root from Step 4 traps \(x_m\in(x_-,x_+)\) for all sufficiently large \(m\). Therefore \(x_m\to x_*\), and \(mT_c(m)=4(m/K)x_m\to4x_*\).

## Verification

An independently implemented two-matrix exponential calculation (using `scipy.linalg.expm` and the eigenvalues of their product) agrees with the formula at 128 combinations covering eight growth-rate pairs, four migration strengths, and four period lengths. The accompanying `verify.py` also checks finite monotonicity comparisons and the exact critical example below. The numerical checks are corroboration; Steps 1–6 are the infinite-parameter proof.

For \(a=1\), \(b=3\), and \(m=2\), the critical identity reduces exactly to

\[
\frac13\sinh(3T/2)=\sinh T,
\quad T_c=2\operatorname{arcosh}\left(\frac{3+\sqrt{13}}4\right)
\approx2.174140289991478.
\]

Thus the same model decays at \(T=1\) and grows at \(T=3\); the threshold is an algebraically characterized transcendental number, not inferred from a graph.

Reproduce: run `python verify.py` with Python 3, NumPy and SciPy. A successful run prints `CHECK_OK`.

## Relationship to prior work

Benaïm, Lobry, Sari, and Strickler's `arXiv:2311.04706` develops growth/persistence in sink habitats, with qualitative examples and asymptotic regimes. Their `arXiv:2407.07553` (especially version 2, Section 3.1.2, Proposition 22, equation (37), and Figure 4) studies **exactly the broader two-season directed-migration model**. It establishes existence and separate limiting growth rates, illustrates a critical curve numerically, and explicitly leaves the endpoint asymptotics of that curve as an open problem. Here the season-specific favorable/unfavorable rates are equal across seasons, yielding a natural symmetric-in-season subfamily with a complete **finite-parameter formula, strict two-variable ordering, and both sharp critical asymptotics**. Previously known qualitative dispersal-induced growth is not claimed as new.

Liu and Wang, *Dispersal-induced growth in time-periodic two-patch environments with asymmetric migration* (published December 2025), analyze principal-eigenvalue monotonicity and level sets under asymmetric migration. Its available abstract and opening-page material were compared; the full theorem statements could not be retrieved, and its possible overlap with the current special switched-direction formula remains a publication-priority risk. The current claims are limited to the matrices given above and are proved independently.

## Limitations

The proof requires identical positive and negative local growth values in both seasons, equal half-periods, zero reverse-season migration, conservative one-way travel from the current unfavorable to the favorable habitat, and two patches. It does not give a formula for seasonally unequal coefficients, nonzero reciprocal rates during a season, nonlinear population regulation, stochastic extinction, or arbitrary temporal migration. It does not assert absolute publication priority. The outcome is a deterministic long-run exponential growth criterion, not literal finite-population survival probability.

## References

1. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *When can a population spreading across sink habitats persist?* `arXiv:2311.04706`, first publicly posted 2023-11-08. https://arxiv.org/abs/2311.04706
2. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *Dispersal-induced growth or decay in a time-periodic environment. The case of reducible migration matrices.* `arXiv:2407.07553`, first publicly posted 2024-07-10; Section 3.1.2 of 2025 revision inspected. https://arxiv.org/abs/2407.07553
3. S. Liu, H. Wang, *Dispersal-induced growth in time-periodic two-patch environments with asymmetric migration*, *Journal of Mathematical Biology* 92, 20 (2026), online publication 2025-12-23. https://doi.org/10.1007/s00285-025-02325-7
