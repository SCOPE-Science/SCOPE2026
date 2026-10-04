# A quantitative gap below the sharp discrete maximal-gradient constant

## Finding
Let \(M^u_{\mathbb Z}\) denote the discrete uncentered Hardy--Littlewood maximal operator and define
\[
\Delta g(n)=g(n+1)-g(n).
\]
Set
\[
\kappa_2=\sum_{r=1}^\infty\left(\frac1r-\frac1{r+1}\right)^2=\frac{\pi^2}3-3.
\]
Let \(S\subset\mathbb Z\) be finite with at least two points. Write \(m\) for the number of connected components of \(S\), let \(b=\max S\), let \(a=\max(S\setminus\{b\})\), and put \(L=b-a\ge1\). Then
\[
\frac{\|\Delta M^u_{\mathbb Z}\mathbf 1_S\|_2^2}{\|\Delta\mathbf 1_S\|_2^2}
\le
\kappa_2-
\frac{1}{mL(L+1)^2(L+2)(2L+1)}.
\]
In particular, the inequality is strict for every non-singleton finite \(S\). Since a singleton has maximal profile \(M^u_{\mathbb Z}\mathbf 1_{\{b\}}(n)=1/(1+|n-b|)\), singletons are exactly the finite characteristic-function equality cases at \(p=2\).

## Assumptions and scope
The maximal operator averages absolute values over all finite integer intervals containing the evaluation point. The statement is a quantitative refinement of the sharp first-difference inequality for characteristic functions at exponent \(p=2\). It applies to finite nonempty sets; the displayed quantitative deficit concerns sets with at least two points. No claim is made here about the best possible deficit as a function of \(m\) and \(L\), or about analogous explicit deficits for every \(1<p<\infty\).

## Proof
The recent sharp theorem of Liao, Madrid, Palsson, and Weigt gives
\[
\|\Delta M^u_{\mathbb Z}\mathbf 1_S\|_2^2
\le \kappa_2\|\Delta\mathbf 1_S\|_2^2.
\]
For a finite set with \(m\) connected components,
\[
\|\Delta\mathbf 1_S\|_2^2=2m.
\]
Their proof decomposes the integer line into component interiors, exterior tails, and complementary gaps. Each boundary jump is charged at most \(\kappa_2\), via a local Karamata majorization. We sharpen only the right exterior tail and leave every other local estimate unchanged.

Let
\[
u_j=M^u_{\mathbb Z}\mathbf 1_S(b+j),\qquad d_j=u_j-u_{j+1},\qquad j\ge0.
\]
Because \(b\) is the rightmost point of \(S\), the maximal profile is convex on the complementary right half-line, starts at \(u_0=1\), and tends to zero. Hence \(d_j\ge0\) and \(d_j\) is nonincreasing. Define the canonical singleton increments
\[
s_j=\frac1{j+1}-\frac1{j+2}=\frac1{(j+1)(j+2)}.
\]
For every \(k\ge1\), the interval \([b,b+k]\) gives \(u_k\ge1/(k+1)\), so
\[
\sum_{j=0}^{k-1}d_j=1-u_k
\le 1-\frac1{k+1}
=\sum_{j=0}^{k-1}s_j.
\]
Also \(\sum_jd_j=\sum_js_j=1\). Thus \((s_j)\) majorizes \((d_j)\), exactly the local structure used in the sharp proof.

The second-rightmost point \(a=b-L\) improves one prefix inequality. At \(k=L\), the interval \([a,b+L]\) has length \(2L+1\) and contains at least \(a\) and \(b\), whence
\[
u_L\ge\frac2{2L+1}.
\]
Therefore, with
\[
E_q=\sum_{j=0}^q(s_j-d_j),
\]
we have
\[
E_{L-1}=u_L-\frac1{L+1}
\ge\frac1{(L+1)(2L+1)}=:\delta_L.
\]

For \(p=2\), the Karamata gap admits a direct Abel-summation lower bound. Put \(A_j=s_j+d_j\). Since both \(s_j\) and \(d_j\) are nonincreasing, \(A_j\) is nonincreasing. Using \(\sum_j(s_j-d_j)=0\), summation by parts gives
\[
\sum_{j=0}^\infty(s_j^2-d_j^2)
=\sum_{q=0}^\infty E_q(A_q-A_{q+1}).
\]
Every term on the right is nonnegative. Keeping only \(q=L-1\) yields
\[
\kappa_2-\sum_{j=0}^\infty d_j^2
\ge E_{L-1}(A_{L-1}-A_L)
\ge\delta_L(s_{L-1}-s_L).
\]
The last difference is explicit:
\[
s_{L-1}-s_L=\frac2{L(L+1)(L+2)}.
\]
Hence the right-tail energy is at most
\[
\kappa_2-\frac2{L(L+1)^2(L+2)(2L+1)}.
\]

The remaining local pieces retain the original sharp upper bounds. There are \(2m\) unit boundary charges in total, one of which is the right exterior tail just sharpened. Consequently
\[
\|\Delta M^u_{\mathbb Z}\mathbf 1_S\|_2^2
\le 2m\kappa_2-
\frac2{L(L+1)^2(L+2)(2L+1)}.
\]
Dividing by \(\|\Delta\mathbf 1_S\|_2^2=2m\) gives the claimed estimate.

For a singleton, \(M^u_{\mathbb Z}\mathbf 1_{\{b\}}(n)=1/(1+|n-b|)\), so each exterior tail has the canonical increments \(s_j\) and equality holds in the sharp inequality. This proves the final equality statement.

## Verification
The proof is analytic. The packaged script `verify_p2_maximal_deficit.py` checks, with exact rational arithmetic, the telescoping prefix identities, the improved two-point prefix defect, the closed form of the resulting deficit, and finite Abel-summation identities for monotone Robin-Hood perturbations of the canonical sequence. It also checks numerically that \(\kappa_2=\pi^2/3-3\) lies in the expected range. The stored output ends with `VERIFY_OK`.

These computations are supplementary; no finite computation is used as a substitute for the infinite summation-by-parts proof.

## Relationship to prior work
Liao, Madrid, Palsson, and Weigt proved the sharp characteristic-function first-difference constant in 2026. Their Theorem 2.3 states the exact constant and records a singleton as an extremizer. Their proof uses local Karamata majorization on exterior tails and complementary gaps. The inspected theorem and proof do not state a quantitative loss for non-singletons or a geometry-dependent stability estimate.

The present result keeps their sharp local decomposition but inserts a new quantitative step: the second-rightmost support point forces a definite prefix defect in the right-tail majorization, and an Abel-summation identity converts that defect into an explicit loss of squared gradient energy. This is stronger than merely observing strictness of Karamata and gives a computable non-extremality margin from \(m\) and the final support gap \(L\).

Earlier work of Bober, Carneiro, Hughes, and Pierce concerns the endpoint \(p=1\) variation inequality for the uncentered discrete maximal operator. González-Riquelme and Madrid study different maximal-function norm and variation inequalities, including finite graphs and estimates of variation by the function norm. Those statements do not imply the interior-exponent quantitative deficit above.

## Limitations
The deficit is not claimed optimal. It uses only one exterior tail and only the second-rightmost support point; incorporating both tails and internal gaps can potentially improve the bound. The argument is specialized to \(p=2\), where the quadratic Karamata gap has an especially transparent Abel-summation identity. An unindexed or terminology-mismatched prior quantitative refinement remains a literature risk despite targeted primary-source and semantic searches.

## References
1. Sung-Yi Liao, José Madrid, Eyvindur Palsson, and Julian Weigt, *Sharp higher order regularity of discrete maximal functions*, arXiv:2607.10753v1, first posted 2026-07-12. Primary MSC 2020 includes 42B25.
2. Jonathan Bober, Emanuel Carneiro, Kevin Hughes, and Lillian B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, Proceedings of the American Mathematical Society 140 (2012), 1669--1680, DOI 10.1090/S0002-9939-2011-11008-6.
3. Cristian González-Riquelme and José Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, Journal of Mathematical Analysis and Applications 506 (2022), 125647, DOI 10.1016/j.jmaa.2021.125647.
