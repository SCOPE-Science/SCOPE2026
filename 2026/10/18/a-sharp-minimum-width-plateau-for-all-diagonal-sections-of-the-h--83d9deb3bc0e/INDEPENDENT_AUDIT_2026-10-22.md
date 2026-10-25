# Independent mathematical audit

## correctness

PASS

For nonconstant sorted a, its permutahedron Q(a) has width in a sorted zero-sum normal u with increments delta_j>=0: u=sum delta_j v_j, and the rearrangement formula gives width=sum delta_j B_j. Triangle inequality bounds |u| <=sum delta_j |v_j|, so the least width is min_j B_j/|v_j|; distinct two-level v_j are strictly noncollinear, proving all minimizers are single-cut normals. The cube fixed-sum section vertices are coordinate permutations of (1^floor t, r,0...), with r=t-floor t; subset extrema give B_j=min(j,n-j,t,n-t) and |v_j|=sqrt(j(n-j)/n). Among j<=floor n/2 the two components j/sqrt(j(n-j)) and m/sqrt(j(n-j)) are respectively strictly increasing and decreasing, so all minimizing cuts are j=1 or j=floor n/2; comparing them gives formula min(sqrt(n/(n-1)),m sqrt(n/floor(n^2/4))), threshold tau=sqrt(floor(n^2/4)/(n-1)), central plateau, and exact minimizer orbits including coexistence at threshold. Independent exact rational support-width enumeration across n=4,5,8,9 with rational t reproduced candidate minima; n=4..89 tested threshold branch inequalities in reviewed checker. The argument, not finite sampling, proves real t and all n>=4.

## originality

PASS

Har-Peled–Robson analyze the regular simplex (which is a t=1 cube section), whereas the claim determines every continuous t and sharp change in minimizing normal orbit. The classical rearrangement/cut lemma alone and capped-simplex projection methods do not provide this full phase portrait in cited work. The novelty is the exact all-t plateau and equality orbits, not two-level rearrangement itself.

## value

PASS

The fixed-sum hypercube slice (generalized hypersimplex) is a canonical symmetric polytope arising in constrained allocation and geometry. Its *minimum* Euclidean width controls slenderness and conditioning; an explicit plateau and jump between balanced and singleton split normal directions is a sharp, natural geometric phase boundary not a gratuitous numeric slice. All real level parameters and equality-orbit classification make it useful beyond the known simplex endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
