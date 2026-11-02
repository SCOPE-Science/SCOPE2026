# Exact optimal spacing of partial river filters and integer-site efficacy thresholds

## Finding

A continuously and uniformly loaded, nondecaying river with \(k\) identical partial point filters admits a unique and explicit global minimizer of integrated downstream pollutant load. For length \(L>0\) and removal fraction \(\eta\in(0,1]\), the optimal filter positions and minimum are

\[
t_j^*=\frac{L[1+(j-1)\eta]}{2+(k-1)\eta},\quad j=1,\ldots,k,
\qquad
\min\int_0^L C(x)\,dx=\frac{L^2(2-\eta)}{2[2+(k-1)\eta]}.
\]

The inlet-to-first-filter and last-filter-to-exit gaps both have length \(L/[2+(k-1)\eta]\), whereas each internal gap has length \(\eta L/[2+(k-1)\eta]\). Consequently weak filters concentrate near the midpoint, whereas perfect filters are spaced at equal intervals.

There is also an exact integer-location counterpart. For \(n\ge2\) unit-loading sites and two filters, all maximizing placements of pollution reduction are determined by a centered gap and a strictly increasing staircase of rational efficacy thresholds. The complete classification, including endpoint ties, is given below.

## Assumptions and scope

**Continuous model.** Fix \(L>0\), integer \(k\ge1\), and \(0<\eta\le1\). Choose real \(0<t_1<\cdots<t_k<L\). A nonnegative transported mass load \(C\) satisfies \(C(0)=0\), \(C'(x)=1\) away from filters, and \(C(t_j^+)=(1-\eta)C(t_j^-)\). The integrated exposure functional is \(J=\int_0^L C(x)\,dx\), ignoring the value of \(C\) at jump points (a null set). This is a load under fixed-flow normalization, not a hydrodynamically modeled concentration. The filter number and removal fraction are fixed; costs are not optimized. There is no longitudinal decay or dilution.

**Discrete model.** Fix integer \(n\ge2\), \(0<\eta\le1\), and exactly two distinct treatment indices \(1\le a<b\le n\). Sites contribute one unit of new load, then any treatment at that site removes fraction \(\eta\) of its just-updated load. Write \(c_0=0\), \(c_i=(c_{i-1}+1)(1-\eta\mathbf1_{\{i=a\lor i=b\}})\); minimize \(E(a,b)=\sum_{i=1}^n c_i\). This is a separate unit-site model with its own postsite objective, not a numerical quadrature certification of the continuous model.

## Proof

### Continuous theorem and uniqueness

Let \(u_j=C(t_j^-)\) and \(v=C(L)\). Because each filter removes \(\eta u_j\) and the distributed source contributes \(L\), conservation gives

\[L=v+\eta\sum_{j=1}^k u_j.\tag{1}\]

Between jumps, \((C^2)'=2C\). At the \(j\)-th filter the squared load drops by \([1-(1-\eta)^2]u_j^2=\eta(2-\eta)u_j^2\). Summation over all segments yields the exact telescoping identity

\[2J=v^2+\eta(2-\eta)\sum_{j=1}^k u_j^2.\tag{2}\]

Apply the ordinary Cauchy--Schwarz inequality to (1), using \(\sqrt{\eta(2-\eta)}u_j\) as the other vector coordinates:

\[
L^2\le\left(1+\frac{k\eta}{2-\eta}\right)
\left[v^2+\eta(2-\eta)\sum_{j=1}^k u_j^2\right].\tag{3}
\]

Combining (2)--(3) gives \(J\ge L^2(2-\eta)/[2(2+(k-1)\eta)]\). Equality in (3) requires every \(u_j=v/(2-\eta)\). Conservation then fixes

\[u_j=\frac{L}{D},\qquad v=\frac{(2-\eta)L}{D},\qquad D=2+(k-1)\eta.\tag{4}\]

The initial gap has length \(u_1=L/D\). After filtering, the next pre-filter load is \((1-\eta)u_j+(t_{j+1}-t_j)=u_{j+1}\), hence every internal gap is \(\eta L/D\). The final exit gap is \(v-(1-\eta)u_k=L/D\). These positive gaps uniquely reconstruct the stated \(k\) ordered positions, even at \(\eta=1\); at these positions equality holds in Cauchy--Schwarz, proving existence, uniqueness, and the sharp value. For \(k=1\), the unique optimum is the midpoint for every positive efficiency. The limit \(\eta\downarrow0\) is not part of the domain; at \(\eta=0\) every location is equally ineffective and uniqueness fails.

### Two-filter integer-site theorem

Put \(N=n+1\). Without filters the postsite sum is \(E_0=nN/2\). The contribution from filtering at site \(a\), before accounting for the later filter, is \(\eta a(N-a)\); the analogous contribution from \(b\) is \(\eta b(N-b)\), and the earlier removal of material that the later filter would otherwise remove is counted twice. Therefore the **exact** reduction is

\[
E_0-E(a,b)=\eta\big[a(N-a)+b(N-b)-\eta a(N-b)\big].\tag{5}
\]

For \(s=a+b\) and \(d=b-a\), completing both squares in (5) shows that maximizing reduction is equivalent to minimizing

\[
Q(s,d)=(2-\eta)(s-N)^2+(2+\eta)
\left(d-\frac{\eta N}{2+\eta}\right)^2.\tag{6}
\]

Valid pairs have integers \(1\le d\le n-1\), \(s\equiv d\pmod2\), and \(d+2\le s\le2n-d\). For every fixed valid \(d\), its minimum in \(s\) is at \(s=N\) when \(d\equiv N\pmod2\), otherwise at both \(s=N-1\) and \(s=N+1\). All listed choices obey the endpoint constraints, including \(n=2\). Thus put

\[
\varepsilon_d=\begin{cases}0,&d\equiv N\pmod2,\\1,&d\not\equiv N\pmod2,\end{cases}
\qquad Q_d=(2+\eta)\left(d-\frac{\eta N}{2+\eta}\right)^2+(2-\eta)\varepsilon_d.\tag{7}
\]

A direct subtraction yields

\[
Q_{d+1}-Q_d=\begin{cases}
2[2(d+1)-\eta(N-d)],&d\equiv N\pmod2,\\
2[2d-\eta(N-d-1)],&d\not\equiv N\pmod2.
\end{cases}\tag{8}
\]

Define, for \(1\le d\le n-2\),

\[
\tau_d=\begin{cases}
\dfrac{2(d+1)}{N-d},&d\equiv N\pmod2,\\
\dfrac{2d}{N-d-1},&d\not\equiv N\pmod2.
\end{cases}\tag{9}
\]

All denominators are positive. Equation (8) has sign \(\operatorname{sign}(\tau_d-\eta)\). The thresholds are strictly increasing: when \(d\equiv N\) the next value is \(2(d+1)/(N-d-2)>\tau_d\); when \(d\not\equiv N\) the next value is \(2(d+2)/(N-d-1)>\tau_d\). Consequently \(Q_d\) strictly decreases up to the unique crossing and strictly increases afterwards, with a two-adjacent-gap tie when a threshold is hit. For every \(0<\eta\le1\), the winning gap is therefore

\[d_* =1+\#\{j:1\le j\le n-2,\;\tau_j<\eta\},\tag{10}\]

plus gap \(d_*+1\) if \(\eta=\tau_{d_*}\) (when such a threshold exists). For each optimal gap, take the center sums specified after (6) and recover \(a=(s-d)/2\), \(b=(s+d)/2\). This classifies every optimum without enumeration. If \(n=2\), the threshold set is empty and the only pair is optimal.

**Examples.** For \(L=1\), \(k=3\), and \(\eta=1/2\), the optimal positions are \((1/3,1/2,2/3)\) and \(J_{\min}=1/4\); equally spacing the filters gives the strictly larger \(J=33/128\). For \(n=6\), threshold \(\tau_1=2/3\) separates optimal gap one from gap two, and at perfect removal a final tie with gap three occurs. These are exact rational computations.

## Verification

The standalone standard-library program `verify.py` replays the load recurrences and compares directly calculated finite-site objectives to the square-completion score, exact reduction identity, center law, monotone thresholds, and tie cases for all two-site pairs at sampled rational efficacies, including exact thresholds and nearby values, for \(2\le n\le13\). It also tests the continuous sharp formula, mass identity, and squared-load telescoping identity for positive rational lengths, \(1\le k\le17\), and several efficiencies, including perfect filtering. At preparation, it passed 7,193 exact-rational assertions. Run `python3 verify.py` from the extracted package; only Python's standard library is needed.

These are finite consistency checks, **not** an exhaustive mathematical proof. The global statements for arbitrary real \(L\), all integers \(k,n\), and all real \(\eta\) rest on equations (1)--(10) and the inequality/ordering arguments above.

## Relationship to prior work

Weller, Jordan and Correll (1998) model landscape riparian buffer cells that each transmit a fixed fraction, and derive formulas for **transverse buffer width and discharge**, especially the effects of variable width (their equation (1), pp. 1157--1158; uniform versus random width in the results). Their material sources and filters are arranged across the land-to-stream flow direction. The present problem instead asks for **longitudinal point treatment placement inside a continually loaded river** and minimizes the integral of transported load over position. Neither the specific all-\(k\) position formula nor the discrete two-treatment efficacy staircase follows from their width comparison as stated.

Voß et al. (2012) present distributed source and in-stream transport equations in WorldQual, but do not optimize identical point-filter positions. Brand and Ostfeld (2011) address wastewater-treatment network location through a genetic-algorithm design approach; the accessible abstract does not establish these idealized exact formulas, but their full text could not be examined. Liu et al. (2019) study *floating treatment islands in series* and an optimum separation influenced by flow blockage, residence and root-zone hydrodynamics; their physical removal-per-length objective and variable-island-count tradeoff differ from the fixed-\(k\), constant-efficiency, distributed-loading exposure theorem here. No claim of global bibliographic novelty or independent priority certification is made.

## Limitations

The model fixes homogeneous loading, unit longitudinal transfer between filters, a common constant removal fraction independent of load, and a fixed filter count. It omits hydrodynamics, natural decay, tributaries, changing flow rates, nonlinear treatment kinetics, capital cost, ecological impacts, and variable removal efficiency. The mathematical exposure quantity is not a measured field concentration or a predicted ecological effect. The discrete classification applies to a separately specified unit-site postprocessing model, not automatically to all discretizations. The related Brand--Ostfeld article was inaccessible in full, and unindexed equivalent results in linear cascade, facility-location or process-optimization literature remain possible. The derivation is suitable as an exact benchmark, not as a site-specific treatment prescription.

## References

1. Weller, D. E., Jordan, T. E., and Correll, D. L. (1998). *Heuristic Models for Material Discharge from Landscapes with Riparian Buffers*. Ecological Applications 8, 1156--1169. DOI: 10.1890/1051-0761(1998)008[1156:HMFMDF]2.0.CO;2. Author-uploaded complete article: https://www.researchgate.net/publication/246366284_Heuristic_Models_for_Material_Discharge_from_Landscapes_with_Riparian_Buffers
2. Voß, A., et al. (2012). *Continental scale modelling of in-stream river water quality: a report on methodology, test runs, and scenario application*. Hydrological Processes 26, 2370--2384. DOI: 10.1002/hyp.9445. Author manuscript: https://nora.nerc.ac.uk/id/eprint/18635/1/N018635PP.pdf
3. Brand, N., and Ostfeld, A. (2011). *Optimal Design of Regional Wastewater Pipelines and Treatment Plant Systems*. Water Environment Research. DOI: 10.2175/106143010X12780288628219. Source metadata and abstract, full article not examined.
4. Liu, C., Shan, Y., Lei, J., and Nepf, H. (2019). *Floating treatment islands in series along a channel: The impact of island spacing on the velocity field and estimated mass removal*. Advances in Water Resources 129, 222--231. DOI: 10.1016/j.advwatres.2019.05.011. MIT record: https://dspace.mit.edu/entities/publication/3017dc6f-27fd-4c1c-85eb-002620c9a218
