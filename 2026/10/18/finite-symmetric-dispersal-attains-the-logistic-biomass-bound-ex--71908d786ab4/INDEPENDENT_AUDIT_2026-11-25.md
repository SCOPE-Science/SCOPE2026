# Independent mathematical audit

## correctness

PASS

Positive constant sub- and supersolutions trap solutions by cooperativity and give monotone limits, including on disconnected graphs. If p_i/q_i attains a maximum alpha>1 at positive equilibria, subtracting alpha times the q-equation at i gives a strictly negative logistic contribution plus a nonpositive diffusion contribution, contradicting stationarity. Scaling the unique positive equilibrium above and below gives strict super- and subsolutions, hence convergence from any positive state. Symmetry cancels migration in the total balance, giving the stated ellipsoid, unique gradient-aligned maximizing point and exact squared-distance deficit. At the target, each unequal-density edge supplies one nonnegative downhill flux and equal-density edges supply zero; equilibrium requires outflow minus inflow to equal g*. A cut with no outgoing arc therefore has nonpositive net production. Conversely all such inequalities make every source–sink cut have capacity at least P=total positive production: cuts crossing any downhill edge have its capacity P, and others have capacity P−g*(U). The saturated max flow gives the required divergences; division by each strictly positive density difference realizes finite rates with no constraint violated. When P=0, every production vanishes and zero rates work. As an independent check of sufficiency, the dual cone of the downhill incidence columns consists of potentials nonincreasing along arcs; their sublevel sets are sink-closed. Since sum g*=0, the inner product of such a potential with g* is the negative integral of the net production on its sublevel sets, hence nonnegative, which is the finite cone feasibility condition. The complete distinct graph has exactly prefix closed sets. Independent rational witness checks (python /workspace/replay.py 5) give positive fluxes 21/16 and 15/8 along the chain, total 23/2, and a singleton obstruction of +17/100 in the second example; p1*−p2*=1+5c/4 and p3*−p2*=1/2+c/12 there. This is exact finite equality only, not optimization of a submaximal total or an assertion about approaching the bound with unbounded rates.

## originality

PASS

Best of knowledge the surviving distinct claim is the arbitrary prescribed graph finite symmetric attainment test, including optional edges, ties and disconnected corridors. The universal ellipsoid bound and maximizer, equilibrium comparisons, classical flow feasibility, and the two-patch single-diffusion-rate optimization are not new. The comparison in RESULT.md line 91 understates the two-patch overlap: Jorba-Cuscó et al. optimize over D and give conditions on positive D*, not just an analysis at a fixed rate. Their result does not settle general-graph feasibility. Full primary text of the motivating 2020 source could not be inspected independently; the cited equality ceiling is credited, not inferred absent.

## value

PASS

The known upper bound by itself cannot distinguish realizable finite corridor designs from unattainable ones. The characterization turns that distinction into a yes/no test with an explicit feasible construction or local cut obstruction, on arbitrary fixed networks even with ties. Exact instances include attainable equality on a sparse chain and nonattainability despite complete corridor choice; these make topology and the admissible flux directions substantive rather than a relabeling of the ceiling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
