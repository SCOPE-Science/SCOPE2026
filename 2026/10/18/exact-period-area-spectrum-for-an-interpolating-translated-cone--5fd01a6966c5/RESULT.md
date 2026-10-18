# Exact period-area spectrum for an interpolating translated cone exchange

## Finding

In the identity-permutation, three-cone translated cone exchange of Cockram, Ashwin and Rodrigues, the open invariant trapezoid between the baseline and its first induced interval exchange has a complete primitive-period classification. Put \(0<\lambda<1\), let \(0<\alpha_0,\alpha_2<\pi/2\), and define
\[
C=\cot\alpha_0+\cot\alpha_2>0,\qquad
T=\{x+iy:0<y<\lambda/C,\;-1+y\cot\alpha_0<x<\lambda-y\cot\alpha_2\}.
\]
Except for the usual measure-zero cone and interval-exchange boundaries, the following results hold.

**Induced-rotation identification.** On each horizontal slice of \(T\), the exchange is the first-return transformation of rotation through \(\lambda\) on a circle of circumference \(1+\lambda\), induced onto an interval of length \(1+\lambda-Cy\). In particular, if \(\lambda\) is irrational, every slice is minimal and uniquely ergodic (with its normalized length measure), and no point of \(T\) is periodic, away from the boundary convention.

**Complete rational spectrum and areas.** If \(\lambda=p/q\) with integers \(0<p<q\), \(\gcd(p,q)=1\), the primitive periods in \(T\) are precisely
\[
\{q,q+1,\ldots,p+q\}.
\]
For \(m=0,\ldots,p\), the planar Lebesgue area occupied by points of primitive period \(p+q-m\) is exactly
\[
\boxed{A_m=\frac{p+q-m}{Cq^2}\,w_m,\qquad
w_m=\begin{cases}\frac12,&m=0\text{ or }m=p,\\1,&0<m<p.\end{cases}}
\]
All listed areas are strictly positive; they sum to \(\operatorname{area}(T)=\lambda(1+\lambda/2)/C\). The area-weighted mean primitive period is
\[
\boxed{\mathbb E_T[\operatorname{per}]=q+\frac p2+\frac{p^2+2}{6(2q+p)}.}
\]

**Individual-height staircase.** At a height \(y\), set \(s=Cy\), \(k=\lfloor qs\rfloor\), and \(\theta=qs-k\). Almost every point of that slice has one of at most two periods: \(p+q-k\) and \(p+q-k-1\). Their horizontal lengths are, respectively,
\[
\frac{(p+q-k)(1-\theta)}q,\qquad
\frac{(p+q-k-1)\theta}q.
\]
For \(\theta=0\) only the first period occurs, apart from boundary conventions.

**High-denominator law.** For any coprime rational sequence \(p_j/q_j\to\lambda_0\in(0,1)\) with \(q_j\to\infty\) and fixed outer angles, the probability distribution of the primitive period divided by \(q_j\), sampled from normalized planar Lebesgue measure on the corresponding trapezoid, converges weakly to the distribution with density
\[
\boxed{\frac{u}{\lambda_0(1+\lambda_0/2)}\;\mathbf1_{[1,1+\lambda_0]}(u).}
\]
This density does not depend on the outer cone angles.

## Assumptions and scope

The original map is the horizontal identity-cone special case of a translated cone exchange on the closed upper half-plane. Its three interior actions are \(z\mapsto z-1\), \(z\mapsto z-(1-\lambda)\), and \(z\mapsto z+\lambda\), respectively on the right outer, central, and left outer cones. The cone angular widths are \(\alpha_0,\pi-\alpha_0-\alpha_2,\alpha_2\). The stated strict inequalities specify the nondegenerate trapezoid \(T\). The map preserves every horizontal line and acts bijectively on \(T\) modulo discontinuity sets of zero area.

Our precise one-dimensional model uses half-open intervals, resolving endpoints deterministically. Original cone-boundary assignments may differ; the assertions about planar areas and almost-everywhere dynamics are independent of those assignments. There is no claim that the entire (vertically unbounded) maximal invariant set has finite area, or that the same period spectrum holds outside \(T\).

## Proof

**1. Reduction to a three-interval exchange.** Fix \(0<y<\lambda/C\), set \(s=Cy\), and introduce \(t=x+1-y\cot\alpha_0\). The horizontal section of \(T\) becomes \(J_s=[0,1+\lambda-s)\) after the harmless choice of half-open endpoints. On its three successive pieces, the map is
\[
H_s(t)=\begin{cases}
t+\lambda,&0\le t<1-s,\\
t+\lambda-1,&1-s\le t<1,\\
t-1,&1\le t<1+\lambda-s.
\end{cases}
\]
This follows directly from the locations of the two slanted cone boundaries and the three horizontal translations, or from the piecewise interval exchange in Section 3 of the originating paper.

**2. Exact first-return representation.** Let \(R(t)=t+\lambda\pmod{1+\lambda}\) on the circle \([0,1+\lambda)\). On \(J_s\) the first return of \(R\) is after one rotation for \(0\le t<1-s\) and \(1\le t<1+\lambda-s\). For \(1-s\le t<1\), the first rotation lands in the omitted terminal interval \([1+\lambda-s,1+\lambda)\), and the second lands at \(t+\lambda-1\in J_s\). Thus its first return is exactly \(H_s\). If \(\lambda\) is irrational, \(R\) is an irrational circle rotation. Every \(R\)-orbit is dense and the rotation is uniquely ergodic; inducing onto the nonempty interval preserves minimality and unique ergodicity for the normalized induced length measure. A periodic \(H_s\)-orbit would be a periodic \(R\)-orbit at the sum of its positive return times, which is impossible.

**3. Rational primitive-period formula.** Let \(\lambda=p/q\) in lowest terms. Every circle-rotation orbit consists of all \(p+q\) representatives
\[
\left\{r+\frac jq:0\le j<p+q\right\},\qquad0\le r<\frac1q,
\]
in some cyclic order, because \(\gcd(p,p+q)=1\). Exactly
\[
m(r,s)=\lfloor q(s+r)\rfloor
\]
of these representatives lie in the omitted terminal interval, using the half-open convention. Since the first-return map on a nonempty subset of a single finite cycle is itself one full cycle on the surviving points, the primitive period at each retained representative is
\[
N(r,s)=p+q-\lfloor q(s+r)\rfloor.
\]
With \(0<s<p/q\) and \(0\le r<1/q\), the floor ranges over the integers \(0,\ldots,p\); each occurs on a positive-measure subset of heights and residues. This proves completeness and the set of allowed primitive periods.

For fixed \(s\), write \(qs=k+\theta\), where \(k\) is integral and \(0\le\theta<1\). The two possible values of the floor are \(k\) on a residue interval of width \((1-\theta)/q\) and \(k+1\) on a residue interval of width \(\theta/q\). For each residue the number of retained horizontal representatives equals the primitive period. Multiplying these two residue widths by their representative counts gives the asserted horizontal lengths.

**4. Exact planar area distribution.** The map \((s,r)\mapsto(y,t)\) has area scale \(dy\,dt=ds\,dt/C\); for each discrete representative \(j\), \(t=r+j/q\) has unit derivative with respect to \(r\). Consequently, the area at period \(p+q-m\) equals
\[
\frac{p+q-m}{C}\,\operatorname{area}\left\{(s,r):0<s<\frac pq,\;0\le r<\frac1q,\;\frac mq\le s+r<\frac{m+1}q\right\}.
\]
The last region is a half-triangle of area \(1/(2q^2)\) for \(m=0,p\), and a full diagonal strip of area \(1/q^2\) for \(0<m<p\). This proves \(A_m\). Summing yields \(\lambda(1+\lambda/2)/C\), equal independently to \(\int_0^{\lambda/C}(1+\lambda-Cy)\,dy\). The weighted mean follows by summing \((p+q-m)A_m\) and using the trapezoidal sums \(\sum_m w_m=p\), \(\sum_m w_m(m-p/2)=0\), and \(\sum_m w_m(m-p/2)^2=p(p^2+2)/12\).

**5. Universal limiting density.** The normalized area mass at scaled period \(u_m=(p+q-m)/q\) is \((p+q-m)w_m/[q^2(\lambda+\lambda^2/2)]\). For \(p/q\to\lambda_0\) and \(q\to\infty\), the interior values have spacing \(1/q\), and their masses form a Riemann sum for \(u\,du/[\lambda_0(1+\lambda_0/2)]\) on \([1,1+\lambda_0]\). The two half-weight endpoint contributions tend to zero. This proves weak convergence.

## Verification

Run `python3 check_period_spectrum.py` from this directory (standard library only). Its exact-fraction tests cover every reduced \(p/q\) with \(2\le q\le31\), multiple height/residue combinations, the return-map identity and complete coset orbit closure. It also clips parameter rectangles with rational polygon arithmetic to rederive all area factors, checks area normalization and the weighted mean, and compares the interval map with the original symmetric forty-five-degree cone translations. The run produced: `PASS exact orbit samples, area polygons: 6530 3572 207445`. These finite checks supplement, but do not replace, the general proof above.

## Relationship to prior work

Cockram, Ashwin and Rodrigues, *Construction of Invariant Curves for Some Piecewise Isometries*, arXiv:2312.17412, Section 3, establish the maximal invariant set and its horizontal two-/three-interval exchanges. Their formula (3.7) provides the starting branches, and they observe that the upper boundary is a Rauzy induction of the baseline exchange. The present contribution is the explicit first-return identification at **every intermediate height**, complete rational primitive-period and planar-area spectra, area-weighted period moment, and universal high-denominator distribution; these exact distributions are not stated there. Circle-rotation induction itself is classical and is not claimed as new.

Ashwin, Goetz, Peres and Rodrigues, *Embeddings of Interval Exchange Transformations into Planar Piecewise Isometries*, arXiv:1805.00245, establish general embedding restrictions but not these parameter-dependent periodic-area laws. Cockram, Ashwin and Rodrigues, *Renormalization of Translated Cone Exchange Transformations*, DOI:10.1080/14689367.2024.2378297, address a broader renormalization mechanism, not the identity-cone trapezoid spectrum here. The cited papers are model/theory precursors, not independent verifications of the formulas in this note.

## Limitations

The area classification is restricted to the open trapezoid of the identity-cone exchange, not to all translated cone exchanges or all of their invariant sets. Original source conventions on cone boundaries may change exceptional orbits, which have zero planar area. The irrational assertion is fiberwise, not unique ergodicity of the full two-dimensional map (which preserves height). The high-denominator statement is weak convergence of normalized planar-period distributions; it makes no claim of uniform convergence or any positive periodic area at the irrational limit. A different formulation of these precise period-area formulas might exist outside the inspected literature; priority is not independently certified.

## References

1. N. Cockram, P. Ashwin, A. Rodrigues, *Construction of Invariant Curves for Some Piecewise Isometries*, arXiv:2312.17412v1, 29 December 2023; subsequently *Dynamical Systems* 40 (2025), 602–625. https://arxiv.org/abs/2312.17412
2. P. Ashwin, A. Goetz, P. Peres, A. Rodrigues, *Embeddings of Interval Exchange Transformations into Planar Piecewise Isometries*, arXiv:1805.00245v1. https://arxiv.org/html/1805.00245v1
3. N. Cockram, P. Ashwin, A. Rodrigues, *Renormalization of Translated Cone Exchange Transformations*, *Dynamical Systems* (2024), DOI:10.1080/14689367.2024.2378297. https://doi.org/10.1080/14689367.2024.2378297
