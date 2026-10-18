# Sharp logarithmic high-server crossover in stochastic-reset search queues

## Finding

The resetting rate at which resetting stops reducing the stable-queue starting-position region and begins enlarging it has an exact, logarithmically corrected high-server asymptotic. With \(C=c\mu L^2/D\), the equalizing rate obeys

\[\boxed{\sqrt{r_{\mathrm{eq}}(c)}=\frac{c\mu L}{\sqrt D}\left(\log C+2\log\log C+o(1)\right)}\qquad(c\to\infty).\]

Equivalently,

\[\boxed{\lim_{c\to\infty}\frac{D\,r_{\mathrm{eq}}(c)}{c^2\mu^2L^2(\log C)^2}=1.}\]

For the range where the unreset critical starting site exists, a strictly positive equalizing rate exists **if and only if** \(C>5/2\), and is unique. This sharpens the source paper's numerical classification of its equalizing rate: the growth is asymptotically quadratic times a logarithmic factor, rather than a fixed exponent strictly greater than two.

## Assumptions and scope

Let \(D,L,\mu>0\) be fixed, and let the integer server count \(c\ge1\) vary. A Brownian searcher moves on \([0,L]\), is absorbed at zero, reflected at \(L\), and is returned independently at exponential rate \(r\ge0\) to its starting point between absorption events. After each absorption it immediately starts an independent new search at the same site; there is no refractory delay. Its independent passage times form the interarrival intervals of a \(G/M/c\) queue, whose servers have independent exponential service times of rate \(\mu\).

Write \(T_r(x)\) for the mean search duration from \(x\in(0,L]\). The queue is stable precisely when \(T_r(x)>1/(c\mu)\). A critical starting point is a solution of equality. For \(C=c\mu L^2/D>2\), the no-reset point is

\[x_c=L-\sqrt{L^2-\frac{2D}{c\mu}}.\]

An *equalizing resetting rate* is a number \(r>0\) such that \(T_r(x_c)=T_0(x_c)=1/(c\mu)\); this is equivalent to resetting and no resetting having the same critical starting point, since \(T_r(x)\) is strictly increasing in \(x\). The special boundary value \(C=2\) has \(x_c=L\). For \(C<2\) no no-reset critical starting point lies within the open interval.

## Proof

**1. Exact crossover equation.** The standard absorbing/reflecting Brownian first-passage calculation and Poisson resetting renewal identity give

\[T_0(x)=\frac{x(2L-x)}{2D},\qquad T_r(x)=\frac1r\left[\frac{\cosh(L\sqrt{r/D})}{\cosh((L-x)\sqrt{r/D})}-1\right]\quad(r>0).\]

Fix \(C>2\), and define \(z=x_c/L=1-\sqrt{1-2/C}\), \(b=1-z=\sqrt{1-2/C}\), and \(k=L\sqrt{r/D}\). Thus \(1/C=(1-b^2)/2\). The exact equalization equation is

\[\frac{\cosh k}{\cosh(bk)}=1+\frac{k^2}{C}.\tag{1}\]

Since the hyperbolic cosine denominator is positive, its positive roots are precisely the positive zeros of

\[H(k)=\left(1+\frac{k^2}{C}\right)\cosh(bk)-\cosh k.\]

**2. A single positive root when \(C>5/2\).** Expand the entire even function as \(H(k)=\sum_{n\ge2}a_n k^{2n}\); its constant and quadratic coefficients vanish. Put \(t=b^{-2}\) and \(S_n(t)=\sum_{j=0}^{n-1}t^j\). Coefficient extraction gives

\[a_n=\frac{(1-b^2)b^{2n-2}}{(2n)!}\bigl[n(2n-1)-S_n(t)\bigr].\tag{2}\]

If \(C>5/2\), then \(1<t<5\). Let \(g_n=S_n(t)-n(2n-1)\). We have \(g_1=0\), \(g_2=t-5<0\), and

\[g_{n+1}-g_n=t^n-(4n+1),\qquad (g_{n+2}-g_{n+1})-(g_{n+1}-g_n)=(t-1)t^n-4.\]

The second difference is strictly increasing and eventually positive. Since the first difference starts negative and tends to positive infinity, the sequence \(g_n\) decreases and then increases, and eventually crosses zero exactly once. Consequently the nonzero coefficients \(a_n\) have one sign change: positive at smaller indices, negative at larger indices. Choose an integer separating these signs. Dividing \(H(k)\) by the corresponding positive power of \(k\) makes every nonconstant summand strictly decreasing in \(k>0\), so this quotient is strictly decreasing. It is positive near zero because \(a_2>0\), while \(H(k)\sim-\cosh k<0\) as \(k\to\infty\). The intermediate-value theorem therefore yields exactly one positive zero of (1).

For \(2<C\le5/2\), \(t\ge5\). Both the initial first difference \(t-5\ge0\) and all later second differences \((t-1)t^n-4>0\) are nonnegative, giving \(g_n\ge0\) for all \(n\ge2\), and at least one strictly positive value. Thus \(H(k)<0\) for every \(k>0\) and there is no positive crossover. At \(C=2\), \(b=0\) and \(H(k)=1+k^2/2-\cosh k<0\), also excluding a positive root.

**3. Locate the unique crossover on the logarithmic scale.** As \(C\to\infty\), \(z=1/C+O(C^{-2})\). Let \(y=kz\) and set \(k=y/z\). For \(y=(1\pm\varepsilon)\log C\), where any fixed \(\varepsilon\in(0,1)\), we have \(k\to\infty\), \(bk\to\infty\), and

\[\frac{\cosh k}{\cosh(bk)}=e^y(1+o(1)),\qquad 1+\frac{k^2}{C}=Cy^2(1+o(1)).\]

The left side is smaller than the right for the lower test value and larger for the upper test value. Existence and uniqueness established in Step 2 trap the unique root between them for all sufficiently large \(C\). Thus its value \(y_C\) satisfies \(y_C/\log C\to1\).

At the exact root, the preceding approximations remain valid uniformly in this bracket. Taking logarithms yields

\[y_C=\log C+2\log y_C+o(1)=\log C+2\log\log C+o(1).\]

Finally, since \(\sqrt{r_{\mathrm{eq}}}=\sqrt D\,k/L=\sqrt D\,y_C/(Lz)\) and \(1/z=C(1+O(C^{-1}))\), substitution yields the boxed two-term result. Every limit here keeps \(D,L,\mu\) fixed and sends the integer \(c\) to infinity.

## Verification

The accompanying executable `queue_crossover_checker.py` implements the log-domain root equation and checks sign changes in the coefficients across several parameter choices. It passed 75 assertion groups in the recorded execution. The checker uses finite computations to test numerical instances; the existence, uniqueness, and asymptotic assertions are proved analytically above. The provided source equation is exact for the stated physical model.

For reproducibility, install the versions specified in `requirements.txt` and run `python queue_crossover_checker.py` from the directory containing the embedded files. This calculation involves no external data files or inaccessible certificates.

## Relationship to prior work

Giral-Barajas and Bressloff (2026), arXiv:2602.05009v1 and v2, derive the absorbing/reflecting mean first-passage formula and the implicit critical-resetting-rate equation, and report numerical growth fitted to a fixed positive power with exponent greater than two; the paper also characterizes the equalizing and maximizing rates. Those formulas, the stability criterion and existence of a crossover in numerical regimes are prior work. The contribution here is an analytic one-positive-root argument for the equalizing equation in the entire applicable parameter region, and especially the **sharp two-term large-server scale with a squared-logarithmic factor**, which is not present in the inspected source sections or appendices. The earlier 2025 search-and-capture queue treatment is a no-reset comparison and does not supply this high-reset asymptotic.

## Limitations

The theorem is confined to one-dimensional Brownian search with one absorbing and one reflecting wall, point Poisson resetting, homogeneous exponential service with \(c\) servers, and no refractory period. It concerns the critical starting-position equality, not a heavy-traffic stationary queue-length distribution, service-delay fluctuations, a universal bound for other reset rules, or a finite-\(c\) uniform error bound for the displayed asymptotic. The numerical checker alone does not prove the infinitely many parameter cases. General asymptotic inversion methods may simplify the proof, and independent literature validation remains outstanding.

## References

1. J. Giral-Barajas and P. C. Bressloff, *Resetting-induced instability in queues fed by a search process in an interval*, arXiv:2602.05009v1 (first posted 2026-02-04), arXiv:2602.05009v2 (2026-05-05), *Physical Review E* **113**, 064101 (2026), DOI: 10.1103/pzz6-3hzf.
2. J. Giral-Barajas and P. C. Bressloff, *Stochastic 1D search-and-capture as a G/M/c queueing model*, *Journal of Physics A: Mathematical and Theoretical* **58**, 355001 (2025), cited for the pre-reset queue stability framework.
3. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, *Physical Review E* **99**, 032123 (2019), cited for interval-resetting first-passage motivation.
