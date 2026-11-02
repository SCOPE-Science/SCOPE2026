# Independent mathematical audit

## correctness

PASS

For arbitrary m>=1, a chronological equal-length accepted interval of length ell is rejected exactly when m accepted jobs cover its start. In any optimum that agrees with the greedy prefix, the first disagreeing accepted interval I can replace the next future job on a free-at-start machine: equal lengths imply end(I)<=end(J), so no later job is harmed; a first rejecting disagreement is impossible because m earlier greedy accepted intervals already overlap I. Thus every prefix is cardinality optimal. Cycling labels by cumulative acceptance count is feasible because, if the previous same-label job remained live, all m preceding accepted jobs would still be live at the new start; acceptance would fail. Cumulative machine counts differ <=1, exactly unit-value EF1/EFX. For m=2, [0,1),[1,2),[2,3) and [1-delta,2+delta), delta>0 arbitrarily small rational, have optimum four with forced (3,1) loads and max fair three; any <=3-job feasible two-machine interval graph has a balanced (<=2,1) coloring. Independently checked greedy against a separately enumerated interval-capacity optimum over bounded small grids and four rational witnesses. These do not replace the universal exchange/graph arguments.

## originality

PASS

Zero-price all-prefix irreversible EFX at simultaneous equal unit lengths and the four-job arbitrarily small duration-perturbation boundary are not implied by the surveyed general EF1 interval-scheduling guarantees or static equitable recoloring. The directly relevant 2026 Borst–Shahkarami–Vaish abstract states general unweighted offline 3/2 and online 2-1/m guarantees with revocation, and equal-length weighted lower bounds, rather than this fixed-weight zero-loss theorem. The relevant 2012 Fung–Poon–Yung abstract concerns preemptive weighted equal-length throughput; its complete text is inaccessible (authorized Oxford attempt reports vpn_disconnected). This is a best-of-knowledge PASS qualified by unavailable primary full texts and possible equivalent classic scheduling formulations.

## value

PASS

All-prefix optimum acceptance under irrevocable machine assignment and EFX gives a sharp, motivated online fairness-efficiency theorem on a natural duration-homogeneous class. The four-job instance is a minimum-size boundary witness proving a discontinuous change for arbitrarily tiny positive duration dispersion. The claim intentionally does not assert a sharp ratio for nonuniform durations; both the exact zero price and minimal perturbation are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
