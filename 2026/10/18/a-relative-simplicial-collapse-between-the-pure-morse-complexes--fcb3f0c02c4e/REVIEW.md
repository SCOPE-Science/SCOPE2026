# Independent mathematical audit

## correctness

PASS

Reconstructed each Hasse diagram and enumerated all undirected matchings by recursively taking the first remaining cell as unmatched or pairing it with an available neighbor. For every matching, a three-color directed DFS tested for cycles after orienting matched incidences upward and the rest downward. This includes all sizes, so it independently proves maxima 7 and 6, with 256 optimal acyclic matchings each. Downward closure gives 11080 and 4224 nonempty faces. Translating the boundary's incidence indices gives exactly the apex-free induced subcomplex; the four links each have 1714 faces including the empty face. Independently replayed the submitted bitmasks, checking at each pair that neither face is in the target, that the larger contains the smaller with codimension one, and that the larger is the only proper coface of the smaller in the entire current complex. After all 3428 removals the remaining face set equals the naturally embedded target. Each pair belongs to just one apex since the lower face has an apex and at most one is possible. Removing the apex bit from each such pair except the last in each cone gives a link collapse to a vertex. The natural inclusion is therefore a simple-homotopy equivalence. It commutes with vertex relabelings and hence the induced integral homology isomorphism is equivariant, whether or not the sequence itself is equivariant.

## originality

PASS

Scoville already gives the two pure homotopy types and face vectors. The distinct claim is an elementary collapse of the actual embedded boundary-pure subcomplex, with all its faces simultaneously retained. The closest prior relative results apply to different complexes, inclusions or dimensions.

## value

PASS

This is the first simplex dimension in the cited comparison where the ordinary and pure constructions separate, with a motivated question left by the two independently known wedge types. A certified collapse answers the natural-map and simple-homotopy questions, and identifies the four actual apex links as collapsible even though the corresponding generalized links are not. The precise relative fact is useful independently of any higher-dimensional extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
