# Exact four-phase excursion statistics after a large BCZ index

## Finding

Let \(\Omega=\{(a,b)\in(0,1]^2:a+b>1\}\), let \(T(a,b)=(b,\kappa(a,b)b-a)\), where \(\kappa(a,b)=\lfloor(1+a)/b\rfloor\), and let \(m\) be normalized planar Lebesgue measure, so \(dm=2\,da\,db\). For every integer \(k\ge12\), condition on \(\kappa(a,b)=k\). The next index is then \(\kappa(T(a,b))=1\). Let \(L\) denote the length of the **initial uninterrupted run of index \(2\)** beginning at time \(2\):
\[
L=\min\{j\ge0:\kappa(T^{2+j}(a,b))\ne2\}.
\]
Write \(k=4q+r\), \(0\le r\le3\). Conditional on the initial index \(k\), \(L\) has the following *exact finite-\(k\)* two-point distribution (with one degenerate case):

| \(r\) | Value(s) of \(L\) | Exact conditional probabilities |
| --- | --- | --- |
| \(0\) | \(q-2\), \(q-1\) | \(\frac{k}{2(3k+2)}\), \(1-\frac{k}{2(3k+2)}\) |
| \(1\) | \(q-1\) | \(1\) |
| \(2\) | \(q-1\), \(q\) | \(1-\frac{k+2}{2(3k+4)}\), \(\frac{k+2}{2(3k+4)}\) |
| \(3\) | \(q-1\), \(q\) | \(1-\frac{(k+2)(9k+5)}{2(3k+1)(3k+5)}\), \(\frac{(k+2)(9k+5)}{2(3k+1)(3k+5)}\) |

In particular the less-common event in the \(r=0\) case tends to probability \(1/6\), the higher value in the \(r=2\) case tends to \(1/6\), and the higher value in the \(r=3\) case tends to \(1/2\). The \(r=1\) length is deterministic. Thus \(L/k\to1/4\) uniformly on these conditioned events while the centered integer length retains four distinct residue-class laws.

## Assumptions and scope

The statement concerns the precisely defined BCZ map and its absolutely continuous invariant probability, not arbitrary expanding or mixing maps. All index conditions hold outside sets of planar measure zero where a floor-function boundary is hit. The cutoff \(k\ge12\) ensures a nonempty initial run and avoids small-digit exceptions. No uniform mixing-rate assertion is made.

## Proof

Fix \(k\ge12\). On the cylinder \(\kappa(a,b)=k\), set
\[
t=\frac{1-(kb-a)}b=\frac{1+a-kb}{b},\qquad s=\frac{1-a}{b}.
\]
The original inequalities \(0<a,b\le1\), \(a+b>1\), and \(k\le(1+a)/b<k+1\) are equivalent, up to null boundary sets, to \(0<t,s<1\) together with
\[
a=\frac{k+t-s}{k+t+s},\qquad b=\frac2{k+t+s}.
\]
Indeed \((1+a)/b=k+t\), while \(s>0\) is \(a<1\), and \(s<1\) is \(a+b>1\); for \(k\ge12\) all remaining coordinate inequalities follow. Write \(c=kb-a=(k+s-t)/(k+t+s)=1-bt\). The coordinate change has absolute Jacobian \(4/(k+t+s)^3\), so its image of \(m\) has density \(8/(k+t+s)^3\) on the unit square. Direct twofold integration yields
\[
m\{\kappa=k\}=8\int_0^1\!\int_0^1(k+t+s)^{-3}\,ds\,dt=\frac8{k(k+1)(k+2)}.
\]

The first iterate is \((b,c)\). Since \((1+b)/c=(k+t+s+2)/(k+s-t)\in[1,2)\) for \(k\ge12\), its index is exactly \(1\) off the boundaries. The second iterate is \((c,c-b)\). While its successive indices are \(2\), the points at times \(2+j\) are
\[
(c-jb,\;c-(j+1)b),\qquad j=0,1,\ldots.
\]
For these points the quotient defining the index is always at least \(2\); it is strictly below \(3\) precisely when
\[
1+c-jb<3(c-(j+1)b)
\iff j<\frac{2c-1-3b}{2b}=\frac{k+s-3t-6}{4}=:R.
\]
This run remains in the positive-coordinate region through its first non-\(2\) value: for \(j\le\lceil R\rceil\) one has \(c-(j+1)b>0\) by substitution of the expressions above. Since \(R>0\), this proves the **exact pointwise identity**
\[
L=\left\lceil\frac{k+s-3t-6}{4}\right\rceil
\quad\text{for almost every }(a,b)\text{ with }\kappa(a,b)=k.
\]

The rest is a weighted area calculation, not a probabilistic independence approximation. Let \(J_k=\int_0^1\int_0^1(k+t+s)^{-3}\,ds\,dt=1/[k(k+1)(k+2)]\). For \(k=4q\), the low-length triangle is \(\{2/3<t<1,\ 0<s<3t-2\}\), of weighted mass
\[
I_0=\frac12\int_{2/3}^1\left((k+t)^{-2}-(k+4t-2)^{-2}\right)dt,
\qquad \frac{I_0}{J_k}=\frac{k}{2(3k+2)}.
\]
For \(k=4q+1\), the ceiling is identically \(q-1\). For \(k=4q+2\), the high-length triangle is \(\{0<t<1/3,\ 3t<s<1\}\), of weighted mass
\[
I_2=\frac12\int_0^{1/3}\left((k+4t)^{-2}-(k+t+1)^{-2}\right)dt,
\qquad \frac{I_2}{J_k}=\frac{k+2}{2(3k+4)}.
\]
For \(k=4q+3\), the high-length region is the union of \(0<t<1/3\) with all \(s\in(0,1)\), and \(1/3<t<2/3\) with \(3t-1<s<1\). Its weighted mass is
\[
\begin{aligned}
I_3={}&\frac12\int_0^{1/3}\left((k+t)^{-2}-(k+t+1)^{-2}\right)dt\\
&+\frac12\int_{1/3}^{2/3}\left((k+4t-1)^{-2}-(k+t+1)^{-2}\right)dt,\\
\frac{I_3}{J_k}={}&\frac{(k+2)(9k+5)}{2(3k+1)(3k+5)}.
\end{aligned}
\]
These three one-variable integrals are elementary evaluations of rational antiderivatives; the complementary probabilities complete the table. Taking \(k\to\infty\) within the residue classes proves the limiting phase laws. Every \(L\) in the table differs from \(k/4\) by a bounded amount, proving \(L/k\to1/4\).

## Verification

An exact rational checker, `check.py`, independently iterates the floor map on the \((t,s)\) rational grid for each \(12\le k\le79\). It reconstructs the entire initial \(2\)-run rather than using the formula and checks the ceiling and support assertions. The analytic triangle integrals above supply the infinite-parameter proof; finite checks alone do not. A separate weighted Monte Carlo experiment is unnecessary for the proof.

## Relationship to prior work

Artiles, Best and Bordignon (2026) prove strong mixing for this same BCZ map, but strong mixing for fixed measurable sets does not specify finite-time itineraries after conditioning on a rare, growing digit. Hall and Shiu (2003) derive the one-point Farey index distribution, whereas the present table concerns a run of length proportional to the initial rare index. Augustin, Boca, Cobeli and Zaharescu (2001) study fixed finite spacing patterns. Korolev (2025) uses BCZ itinerary polygons for arithmetic coloring of Farey denominators; the exact moving-length conditional law above is not asserted by the material available for comparison. The construction uses elementary BCZ cylinder geometry, not a new mixing theorem.

## Limitations

The distribution is for the initial \(2\)-run after one exceptional digit only; later return blocks, correlations at macroscopic times, and quantitative mixing rates are not determined. The area calculation is mathematically self-contained, but completeness of the prior-literature comparison is limited by inability to inspect the 89-page full text of Korolev (2025); generic polygon formulas there may provide other ways to compute these probabilities. No independent scientific audit is claimed.

## References

1. A. Artiles, A. Best, M. Bordignon, *Mixing of the BCZ Map*, arXiv:2610.07347v1, first posted 2026-10-05, https://arxiv.org/html/2610.07347v1.
2. R. R. Hall, P. Shiu, *The index of a Farey sequence*, Michigan Math. J. 51 (2003), 209–223, DOI:10.1307/MMJ/1049832901.
3. V. Augustin, F. P. Boca, C. Cobeli, A. Zaharescu, *The h-spacing distribution between Farey points*, Math. Proc. Camb. Phil. Soc. 131 (2001), 23–38, DOI:10.1017/S0305004101005187.
4. M. A. Korolev, *A distribution related to Farey sequences—I*, arXiv:2502.19881v2 (2025), https://arxiv.org/abs/2502.19881.
