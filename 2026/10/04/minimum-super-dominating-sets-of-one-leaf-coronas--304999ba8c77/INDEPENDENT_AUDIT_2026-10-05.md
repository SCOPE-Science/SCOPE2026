# Independent mathematical audit

## correctness

PASS

The standard half-order lower bound and the original-vertex witness give gamma_sp=n. Any minimum set has exactly one selected vertex from each private pair {v,u_v}; otherwise an omitted private leaf has no selected neighbor, while n selected vertices leave no room for a double-selected pair. If v itself is selected and its leaf omitted, v must be the private defender of that leaf, so no H-neighbor of v may be omitted. Hence the base vertices whose leaves are selected form a union of connected components. Conversely, choosing all leaves on any component union and all original vertices off it supplies a valid private defender for every omitted vertex. This proves the exact bijection and count. The inspected verifier exhausts every labeled base graph through order five and directly tests the definition, but the all-order conclusion comes from the structural proof.

## originality

PASS

Klein--Rodriguez-Velazquez--Yi already determine the scalar super-domination number for ordinary corona products, which specializes to gamma_sp(H circle K1)=|V(H)|, but they do not classify the minimum sets. Ghanbari--Jager--Lehtila materially distinguish the ordinary and neighborhood corona, enumerate minimum super dominating sets only for selected graph classes, and explicitly list counting minimum super dominating sets in trees as future work. The audited component-union classification and exact 2^{c(H)} multiplicity were not found in those full primary sources or in the Resultary search.

## value

PASS

Counting and classifying all minimum super dominating sets is a natural refinement of the established corona number. The theorem solves the full one-private-leaf family for arbitrary base graphs and, for connected trees, supplies an infinite tree family in a direction explicitly identified in the later enumeration paper.

The dated certificate retains the supplied scientific assessment, sources and limitations.
