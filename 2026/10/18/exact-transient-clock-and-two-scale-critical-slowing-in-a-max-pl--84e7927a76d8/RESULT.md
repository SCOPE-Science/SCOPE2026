# Exact transient clock and two-scale critical slowing in a max-plus negative-feedback oscillator

## Finding
For the max-plus negative-feedback map
\[
F_{m,B}(x,y)=\bigl(y,\,B-\max(0,mx)\bigr),\qquad B>0,\quad m>1,
\]
consider the natural section \(\{(x,B):0<x<B\}\). Let \(\tau_m(x)\) be the least **positive physical iterate** at which its orbit reaches the distinguished attracting-cycle point \((B,B)\), with value \(+\infty\) if no such iterate exists. Put \(c_m=B/(m+1)\). The following complete entrance-time classification holds.

For \(0<x<B\), \(x\ne c_m\), define
\[
N_m(x)=\begin{cases}
\left\lceil\dfrac{\log(c_m/(c_m-x))}{2\log m}\right\rceil,&0<x<c_m,\\[5pt]
\left\lceil\dfrac{\log((B-c_m)/(x-c_m))}{2\log m}\right\rceil,&c_m<x<B.
\end{cases}
\]
Then
\[
\boxed{\tau_m(x)=4N_m(x)+\mathbf1_{\{x<c_m\}}.}
\]
The exceptional section point \(x=c_m\) is on a repelling primitive four-cycle and never reaches \((B,B)\). Thus every other section point is captured *exactly* in finite time, and possible capture times are precisely \(4k\) and \(4k+1\), \(k\ge1\).

For a section point \(X\) uniformly distributed over \((0,B)\), the pair \((N_m(X),J_m(X))\), where \(J_m=\mathbf1_{\{X<c_m\}}\), consists of independent random variables with
\[
\mathbb P(N_m=k)=(1-m^{-2})m^{-2(k-1)},\qquad
\mathbb P(J_m=1)=\frac1{m+1},\quad k\ge1.
\]
In particular the **original-time** probability-generating function and mean are
\[
\boxed{\mathbb E[z^{\tau_m}]=
\frac{(1-m^{-2})z^4(m+z)}{(m+1)(1-m^{-2}z^4)},\quad |z|\le1,}
\qquad
\mathbb E[\tau_m]=\frac4{1-m^{-2}}+\frac1{m+1}.
\]

The bifurcation \(m\downarrow1\) has two sharply different time scales. For any **fixed** \(0<x<B\), \(x\ne B/2\),
\[
\boxed{\lim_{m\downarrow1}(m-1)\tau_m(x)
=2\log\frac{B}{2|x-B/2|}.}
\]
At the critical central point \(x=B/2\) instead,
\[
\boxed{\lim_{m\downarrow1}
\frac{(m-1)\tau_m(B/2)}{\log(1/(m-1))}=2.}
\]
For any fixed probability density \(f\in L^1(0,B)\), if \(X\) has density \(f\), then for \(t\ge0\),
\[
\lim_{m\downarrow1}\mathbb P\{(m-1)\tau_m(X)>t\}
=\int_{\frac B2(1-e^{-t/2})}^{\frac B2(1+e^{-t/2})} f(x)\,dx.
\]
For the uniform density this limit is \(e^{-t/2}\): the rescaled hitting time has the exponential law of mean \(2\). The isolated midpoint orbit, by contrast, has an additional logarithmic critical slowdown.

## Assumptions and scope
Here \(B\) is any positive real number, \(m\) is any real number strictly greater than \(1\), and time is measured in discrete iterates of the **two-dimensional** map, not in returns of an induced map. The section is the open segment \(0<x<B\) at height \(B\). Every stated entrance time concerns the single cycle point \((B,B)\), not merely the first visit to any of the other three points of that cycle. The distributional claims are statements about ensembles of initial points on that section, not about invariant measures of the map.

## Proof
**1. Exact roof time and return branches.** Write \(a=(m-1)B/m^2\) and \(b=B/m\); then \(0<a<c_m<b<B\). From a point \((x,B)\) with \(0<x<B\), the first three iterates are
\[
(B,B-mx),\quad (B-mx,(1-m)B),\quad
((1-m)B,\,B-\max(0,m(B-mx))).
\]
If \(x\ge b\), the last displayed point equals \(((1-m)B,B)\), and the fourth iterate is \((B,B)\). If \(x<b\), the third point is \(((1-m)B,(1-m)B+m^2x)\). Thus for \(a<x<b\), the **fourth** point is \(((1-m)B+m^2x,B)\), lying again on the positive section. At \(0<x\le a\), the fourth point has nonpositive first coordinate and its **fifth** iterate is \((B,B)\). Consequently the return-or-capture map is exactly
\[
P(x)=\begin{cases}B,&0<x\le a,\\ m^2x+(1-m)B,&a<x<b,\\ B,&b\le x<B,\end{cases}
\]
with physical excursion length \(5\), \(4\), or \(4\) on the respective branches. No earlier iterate in these excursions can equal \((B,B)\).

**2. Surviving section intervals and exact entrance time.** The middle branch has the unique fixed point \(c_m=B/(m+1)\), is affine expanding with slope \(m^2\), and fixes its sign relative to \(c_m\). For every integer \(n\ge0\), the set of initial section points surviving more than \(n\) excursions without capture is exactly
\[
S_n=\left(c_m-\frac{B}{m^{2n}(m+1)},\quad
c_m+\frac{B}{m^{2n-1}(m+1)}\right).
\]
For \(n=0\) this is precisely \((0,B)\); for \(n\ge1\) it follows by pulling \((a,b)\) back \(n-1\) times through the middle affine branch. The interval length is \(B m^{-2n}\), and \(\cap_{n\ge0}S_n=\{c_m\}\). Therefore every \(x\ne c_m\) exits after a finite number \(N_m\ge1\) of excursions, given by the displayed ceiling formulas. Left exits require the one extra physical iterate, proving the complete entrance-time identity. At \(c_m\) all returns repeat \(c_m\), proving the exception.

**3. Capture-time probabilities.** Uniform measure gives \(\mathbb P(N_m>n)=|S_n|/B=m^{-2n}\), hence the stated geometric law. The left and right components of \(S_{n-1}\setminus S_n\) have length ratio \(1:m\), independently of \(n\). This proves \(\mathbb P(J_m=1\mid N_m=k)=1/(m+1)\), so \(J_m\) and \(N_m\) are independent. Summing the resulting geometric series gives the original-time generating function and mean.

**4. Two-scale limit.** For fixed \(x\ne B/2\), the relevant side of \(c_m\) is eventually fixed and the logarithmic numerator in the ceiling formula tends to \(\log[B/(2|x-B/2|)]\). Using \(\log m\sim m-1\) and that a ceiling changes its argument by less than one yields the pointwise limit. For \(x=B/2\), one has \(x>c_m\), and exactly
\[
N_m(B/2)=\left\lceil\frac{\log(2m/(m-1))}{2\log m}\right\rceil,
\quad \tau_m(B/2)=4N_m(B/2).
\]
This gives the logarithmically enhanced limit. For an arbitrary fixed integrable density \(f\), the random variables \((m-1)\tau_m(x)\) converge at every \(x\ne B/2\) to the continuous-in-\(x\) function stated above. The level sets of that function have Lebesgue measure zero. Dominated convergence of the corresponding indicators proves the survivor formula for every \(t\ge0\). Under uniform sampling, \(2|X-B/2|/B\) is uniform on \((0,1)\), giving the exponential law.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses only standard Python exact rational arithmetic. It checks the map's actual original-time orbit against the branch roof, the proposed exact entrance-time formula, nested survivor endpoints and interval lengths, and the terminal-side probability decomposition. Across six rational feedback strengths, three rational scales and section grids/boundaries, it passes \(5{,}856\) exact rational assertions. The critical limits and all-real-parameter conclusions are proved analytically above; the finite checks are not substitutes for those proofs.

## Relationship to prior work
Gibo and Ito (2015) introduced the discretized and ultradiscrete negative-feedback framework. Ohmori and Yamazaki (2023, section 3 and equation (12)) give precisely the middle-branch Poincaré map and identify the attracting and repelling four-cycles. Those results are taken as established, **not claimed new**. The present statement adds the branch-dependent **original-time roof**, a complete explicit entrance-time function, the uniform-section probability law, a pointwise singular critical limit with a distinguished logarithmic exception, and the limiting distribution for arbitrary section densities. Ohmori and Yamazaki (2024) study a more general max-plus family that includes this map but do not state these original-time transient laws. Their earlier Sel'kov return-map paper (2022) concerns a different max-plus model with a different, multi-branch return map; its self-similar basin construction does not imply the above exact constants or the critical midpoint law.

## Limitations
This theorem is confined to the specified one-dimensional section of the two-dimensional system. It gives no full-plane capture-time distribution or analogous law for the generalized map with nonzero extra feedback parameter. First hitting the **set** of the four-cycle points can occur earlier than the event studied. The entire result depends on an explicitly known 2023 Poincaré map; the new roof-time and statistical calculations are therefore an extension of that work rather than an independent classification of the orbit structure. Possible equivalent, unindexed earlier calculations have not been ruled out, and the 2015 originating article's complete text was not available for inspection.

## References
1. S. Ohmori and Y. Yamazaki, *Dynamical properties of discrete negative feedback models*, arXiv:2305.05908v1, first posted 10 May 2023, especially section 3 and equation (12). https://arxiv.org/abs/2305.05908
2. S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230v1 (2024). https://arxiv.org/abs/2402.06230
3. S. Ohmori and Y. Yamazaki, *Poincaré map approach to limit cycles of a simplified ultradiscrete Sel'kov model*, JSIAM Letters **14** (2022), 127–130. https://doi.org/10.14495/jsiaml.14.127
4. S. Gibo and H. Ito, *Discrete and ultradiscrete models for biological rhythms comprising a simple negative feedback loop*, Journal of Theoretical Biology **378** (2015), 89–95. https://doi.org/10.1016/j.jtbi.2015.04.024
