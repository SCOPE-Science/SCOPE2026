# Independent mathematical audit

## correctness

PASS

Read the complete actual source RESULT.md, SLOGAN.txt and verifier. The halfspace definition fixes p,q≥1 and Euclidean coordinate normalization. Reflection y→−y turns pair sums into cross differences. Translating coordinates to [0,2], feasible span ≤1 contributes n+1 via ordered extrema. If span >1, both extrema must lie within one part, contributing p(p−1)∫s^{p−2}(2−s)^{q+1} and its symmetric term; terms with p or q=1 vanish. Change t=(2−s)/s yields positive factor 2^n/(1+t)^{n+1} and a numerator exactly even in d=(p−q)/2 with (a(a−1)+d²)cosh(−d log t)+(2a−1)d sinh(−d log t), a=n/2≥1. For t∈(0,1), monotonic in |d| is strict away from 0, establishing all p,q and both parities n, including p=q=1. The star evaluation follows by conditioning. For fixed p and q→∞ the q(q−1) term dominates; u=q(2−s)/2 gives normalized integrand u^{p+1}(1−u/q)^{q−2} dominated by u^{p+1}e^{−u/2} and convergence to Γ(p+2)=(p+1)!. No finite test is substituted for universal mathematics. Executed original Git-blob-verified verify.py: 36 p,q≤6 exact rational second integrations, 4≤n≤12 imbalance, seven independent SciPy halfspace/ConvexHull volumes. Additionally derived independent signed-orthant/Stanley formula (p!q!/n!)Σ binom(n,a+c) and verified exact equality for 49 (p,q)≤7. Source seven-blob Git tree was independently reconstructed and matches assigned 041db... exactly.

## originality

PASS

A best-of-knowledge comparison tested the identical rooted graph-Lipschitz ball and polar symmetric-edge formulations, not just signed-chain titles. Beck–Hlavacek give type-B signed-chain constructions and signed ORDER Ehrhart data but not this explicit entire two-level signed-chain Euclidean volume/strict imbalance/asymptotic. Gordon–Petrov give generic Lipschitz faces; D’Alì et al. evaluate primal symmetric edge families rather than the polar volume; Tsuchiya works with a different convex-hull operation. An independent sign-orthant decomposition reduces the unweighted volume to a binomial double sum via Stanley ordinary chain-polytope volumes, so one must not claim the absolute-volume formula by itself is inaccessible to classical methods. The surviving contribution is the exact strict redistribution/extremizer inequality for all fixed n and the normalized fixed-p asymptotic, jointly with the analytic evaluation. No stronger checked statement logically implies this triple. Residual priority risks are explicit; search absence is not proof of novelty.

## value

PASS

The signed-chain H-representation is a natural two-level poset family and exactly a rooted graph-Lipschitz unit ball on K_{1,p,q}, making Euclidean volume a motivated two-parameter invariant. The exact complete classification of its extremal volume at fixed n is not merely a small computed number: strict balance minimum, star maximum and the explicit asymptotic profile quantify the effect of layer imbalance for arbitrarily high dimension. The strict inequality is a nontrivial positivity theorem, and researchers studying signed poset geometry, graph Lipschitz balls or convex-body volumes can use the exact p,q profile and extremizers. The volume formula alone admits a classical sign-orthant/Stanley reduction, so value rests on the combined sharp geometric inequality and asymptotic, not novelty of integration technique. This does not claim a general arbitrary signed-poset volume theorem or an Ehrhart formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
