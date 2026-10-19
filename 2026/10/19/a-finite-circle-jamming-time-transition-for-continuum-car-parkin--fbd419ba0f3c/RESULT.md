# A finite-circle jamming-time transition for continuum car parking

## Finding

For unit-length rods deposited by homogeneous Poisson attempts at intensity one per unit length per unit time on a circle of circumference \(L\geq1\), let \(T_L\) be the physical time of the **last accepted deposition**, starting with an empty circle. Although \(T_L\) is finite almost surely for every \(L\), its expectation obeys the sharp trichotomy

\[
\mathbb E[T_L]=\begin{cases}
1/L,&1\leq L\leq2,\\
1/L+1/(L-2),&2<L\leq3,\\
+\infty,&L>3.
\end{cases}
\]

For every \(3<L\leq4\), write \(U\) and \(V\) for the waiting times to the first and second accepted rods, and \(Z\) for the subsequent waiting time to the third, with \(Z=0\) if two rods already jam the circle. Then \(U,V,Z\) are independent, \(U\sim\operatorname{Exp}(L)\), \(V\sim\operatorname{Exp}(L-2)\), and for all \(t>0\),

\[
\Pr(Z>t)=\frac{2(1-e^{-(L-3)t})}{(L-2)t}.
\]

In particular, \(T_L=U+V+Z\), and

\[
\lim_{t\to\infty}t\Pr(T_L>t)=\frac{2}{L-2},\qquad
\mathbb E[\min\{T_L,t\}]=\frac{2}{L-2}\log t+O_L(1).
\]

The last limit is for each fixed \(3<L\leq4\), so it is not uniform as \(L\downarrow3\). The threshold at circumference three is attained on the finite-mean side.

## Assumptions and scope

A rod of length one on the circle occupies an arc of intrinsic length one. A proposal specifies its center \(x\in\mathbb R/L\mathbb Z\); proposals form a Poisson point process on \((0,\infty)\times(\mathbb R/L\mathbb Z)\) of intensity \(dt\,dx\). A proposed rod is accepted precisely when the interior of its arc is disjoint from those of all accepted rods. End-point contacts have probability zero; they are immaterial to all asserted laws. Accepted rods remain fixed. A configuration is jammed when the set of admissible centers has zero length, equivalently when no open interval admits another rod. The physical time \(T_L\) is the time of its last accepted rod, *not* the number of proposed rods or an accelerated algorithm's completion time.

For two or more accepted rods, order their centers clockwise and let \(g_i\) denote the clockwise intercenter gaps. Each gap is at least one. The total admissible center length is

\[
A=\sum_i (g_i-2)_+,
\]

where \((a)_+=\max\{a,0\}\). With one accepted rod it is \((L-2)_+\); for the empty circle it is \(L\). Conditionally on a current configuration with \(A>0\), the physical waiting time to the next accepted rod is \(\operatorname{Exp}(A)\), and its center is uniform on the admissible subset.

## Proof

**Almost-sure finiteness.** Each accepted rod occupies disjoint physical arclength one. Therefore the total number accepted is at most \(\lfloor L\rfloor\); a full tiling requires exact contacts and has probability zero when relevant. Whenever a finite configuration is not jammed, some admissible arc is open and hence \(A>0\). Independent Poisson thinning then gives a finite exponential wait to the next acceptance almost surely. Inducting over the bounded number of acceptances proves \(T_L<\infty\) almost surely.

**The first two thresholds.** Initially the accepted rate is \(L\), so the first wait is \(\operatorname{Exp}(L)\). After the first acceptance the admissible length is \((L-2)_+\). If \(1\leq L\leq2\), the first rod jams the circle. If \(2<L\leq3\), the second rod arrives after an independent \(\operatorname{Exp}(L-2)\) wait. Its clockwise separation \(Y\) from the first center lies uniformly in \([1,L-1]\), and both cyclic gaps, \(Y\) and \(L-Y\), are at most two. The second rod therefore jams the circle. These observations give the two finite expectation formulas, including the equality endpoints.

**Exact distribution above three.** Suppose \(3<L\leq4\). The first and second waiting times are again independent exponentials of rates \(L\) and \(L-2\), with second clockwise separation \(Y\sim\operatorname{Uniform}[1,L-1]\), independently of those waits. No fourth rod can be accepted with positive probability in this range. The remaining admissible length after the second acceptance is

\[
A(Y)=(Y-2)_++(L-Y-2)_+.
\]

Since \(L\leq4\), at most one of these terms is positive, except on a null boundary. On \(Y\in[1,L-2)\) and \(Y\in(2,L-1]\), each of length \(L-3\), the admissible rate runs uniformly from zero to \(L-3\), and elsewhere \(A(Y)=0\). If \(A(Y)>0\), the next waiting time is exponential of that rate; otherwise define \(Z=0\). Thus for \(t\geq0\), with its continuous extension at \(t=0\),

\[
\Pr(Z>t)=\frac1{L-2}\int_1^{L-1}{\bf1}_{\{A(y)>0\}}e^{-A(y)t}\,dy
=\frac{2}{L-2}\int_0^{L-3} e^{-at}\,da.
\]

This proves the stated survival formula. The strong Markov property and spatial homogeneity make \(U\), \(V\), and \(Z\) mutually independent. The integral gives \(\Pr(Z>t)=2/((L-2)t)+O_L(t^{-1}e^{-(L-3)t})\). Convolution with the independent light-tailed \(U+V\) preserves the leading \(1/t\) coefficient: for example, split on \(U+V\leq\sqrt t\), where \(\Pr(Z>t-U-V)\) is uniformly asymptotic to its value at \(t\), and bound the complement exponentially. More precisely, since \(U+V\) has exponential moments, the same splitting with the bound \(1/(t-U-V)=1/t+O((U+V)/t^2)\) on \(U+V\leq t/2\) gives \(\Pr(T_L>t)=2/((L-2)t)+O_L(t^{-2})\). Integration of this survival tail proves the logarithmic truncated-mean expansion with bounded remainder and \(\mathbb E[T_L]=\infty\).

**All larger circumferences.** Fix \(L>4\), and put \(k=\lfloor L/2\rfloor+1\). Directly, \(k+1<L<2k\). Consequently there exist cyclic gaps \(g_1,\dots,g_k\) summing to \(L\) of the form

\[
g_1=2+\varepsilon,\qquad 1<g_i<2\ (2\leq i\leq k),
\]

for every sufficiently small \(\varepsilon>0\): take the remaining gaps near \((L-2-\varepsilon)/(k-1)\), which lies strictly between one and two. Each gap exceeds one, so these \(k\) centers are mutually nonoverlapping, and precisely one gap admits an additional center, in an interval of length \(\varepsilon\). The \((k+1)\)-st accepted rod, which must eventually arrive, therefore has conditional waiting time \(\operatorname{Exp}(\varepsilon)\).

To make the expectation argument measure-theoretic, parameterize the first \(k\) **proposed** centers by the first center's circle coordinate and their cyclic spacings. Restrict to a fixed open interval for the first coordinate, a fixed small open box for \(g_2,\ldots,g_{k-1}\), and \(g_1\in(2,2+\varepsilon_0)\), chosen so that the resulting last gap \(g_k=L-\sum_{i<k}g_i\) stays strictly between one and two. This is an open region of positive joint Lebesgue density in which every one of the first \(k\) proposals is accepted. The change of variables to \(\varepsilon=g_1-2\) has unit Jacobian; the density is bounded below uniformly as \(\varepsilon\downarrow0\). Given these accepted centers, the next accepted waiting time has mean \(1/\varepsilon\). Since \(T_L\) exceeds this waiting time,

\[
\mathbb E[T_L]\ \geq\ c\int_0^{\varepsilon_0}\frac{d\varepsilon}{\varepsilon}=\infty
\]

for some \(c>0\). Combining with the exact calculation for \(3<L\leq4\) completes the all-\(L\) assertion.

## Verification

The standalone `checks.py` independently computes admissible-circle lengths from ordered centers, compares midpoint quadrature over both nonempty two-gap intervals to the exact survival integral, evaluates the tail constants, checks seeded random samples, and constructs near-pinched gap witnesses at multiple larger circumferences. All included checks pass under Python 3 using only its standard library. The proof of the continuum theorem is the analytic argument above; these tests are finite numerical consistency checks rather than a proof of the all-\(L\) statement.

To reproduce, run `python checks.py` in a directory containing this document and the standalone script.

## Relationship to prior work

Privman and Yan (2016) investigate irreversible deposition on imprecisely patterned one-dimensional substrates and identify slow power-law approaches to jamming via nearly fitting gaps. Their Section 4 develops a Pomeau-type small-gap mechanism; it does not derive the stopping-time expectation trichotomy or finite-circle exact terminal-event distribution proved here. Purvis, Reeve, Wattis, and Mao (2015) study coverage and availability near jamming, including continuous intervals, rather than the finite-circle final-deposition time. Huillet (2003) examines random deposition configurations on circles but explicitly distinguishes the resulting free-gas/selected-configuration process from Rényi's random sequential adsorption. The older Pomeau and Swendsen work motivates late-time small-gap asymptotics, without supplying the particular finite-volume phase boundary and coefficient claimed here in the accessible material. Kumar (2026) studies exact finite-**interval** parking configuration laws and absorption counts; only its abstract was accessible, leaving a residual priority check.

The novelty assertion is limited to the specific finite-ring stopping-time law and sharp circumference threshold, not to the established \(1/t\) Pomeau mechanism or the classical car-parking model itself.

## Limitations

The exact terminal-time tail coefficient is established only for \(3<L\leq4\); no coefficient is claimed for larger circles. For \(L>4\), the proof gives an infinite-mean conclusion by a positive-volume geometric event, not a complete tail distribution. The process is the unit-intensity *physical-time* Poisson continuum model, not a lattice adsorption process, a fixed-number proposal model, or a proposal-skipping saturation algorithm. No independent mathematical review has been performed. Certain plausible literature was accessible only through abstracts or summaries; bibliographic priority remains subject to further checking.

## References

1. V. Privman and H. Yan, *Random Sequential Adsorption on Imprecise Lattice*, Journal of Chemical Physics **144**, 244704 (2016). arXiv:1606.01823; DOI: 10.1063/1.4954332. First publicly submitted 2016-06-06.
2. B. Purvis, L. Reeve, J. A. D. Wattis, and Y. Mao, *Scaling behavior near jamming in random sequential adsorption*, Physical Review E **91**, 022118 (2015). DOI: 10.1103/PhysRevE.91.022118.
3. T. Huillet, *Random covering of the circle: the configuration-space of the free deposition process*, Journal of Physics A **36**, 12143–12155 (2003). DOI: 10.1088/0305-4470/36/49/002.
4. Y. Pomeau, *Some asymptotic estimates in the random parking problem*, Journal of Physics A **13**, L193–L196 (1980).
5. R. H. Swendsen, *Dynamics of random sequential adsorption*, Physical Review A **24**, 504–508 (1981).
6. G. P. Kumar, *Exact Finite-Length Theory of Uniform Car Parking: Spatial Laws, Absorption, and Aggregation* (2026), arXiv:2608.22671. Finite-interval study; abstract consulted.
