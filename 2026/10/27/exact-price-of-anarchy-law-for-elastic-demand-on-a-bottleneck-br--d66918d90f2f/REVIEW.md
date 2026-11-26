# Independent mathematical audit

## correctness

PASS

The frozen Finding fails as stated. At B=6/5, (0,6/5,6/5) is Nash with travel 12/5, above the optimal 2; the three route costs and the outside option are all 6/5. Under no-profitable-deviation Nash, at B=7/4 the full-travel flow (0,3/2,3/2) costs 9/2, not 21/4. Even if indifference is imposed at full participation, the first counterexample still applies. The replacement proves the complete Nash family for 1<B<2: the common used cost exceeds 1 (it equals B with nonparticipants, and it is at least 3/2 with full participation because r<=u+v<=2c). Unequal variable-edge loads would make every route using the larger load strictly worse than the other outer route, so u=v=w. This yields w=B below full participation and 3/2<=w<=B at full participation, and the shortcut-only flow attains worst Nash cost 3B. The objective is affine in shortcut flow at fixed u,v. Using both extended endpoint values as lower bounds, not claiming both are feasible for each u,v, gives two sharp minima 2(1-B) and -B^2/4 after subtracting 3B. They occur at different (u,v) and feasible flows, proving uniqueness off the threshold and exactly two optimizers at the threshold. The ratio and the benchmark survive; the universal demand reversal does not.

## originality

PASS

Best of current knowledge for the corrected network-specific Nash classification, sharp optimum switch and worst-equilibrium cost ratio. The established model and Braess latency pattern are not new. The closest primary bounds use different hypotheses and do not specify the equilibrium correspondence or optimize the combined objective on this network.

## value

PASS

A sharp topology-specific optimizer switch and full equilibrium demand interval quantify precisely what can and cannot be inferred from elastic participation. In the upper regime equilibria occur on both sides of optimal travel despite a determinate worst cost. This gives an exact benchmark for the low-equilibrium-travel, non-subpath-optimal bottleneck regime and distinguishes it from a global welfare bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
