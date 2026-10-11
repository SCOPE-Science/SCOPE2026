# Independent mathematical audit

## correctness

PASS

For a selected vertex \(v\in V_i\), its neighbors outside \(D\) are exactly \(C\setminus V_i\). Thus an omitted vertex \(u\) is privately witnessed by \(v\) iff \(C\setminus V_i=\{u\}\). This makes complements of size zero and one feasible; a two-vertex complement is feasible exactly when its vertices lie in distinct non-singleton parts, so each part still supplies the other vertex's witness. If \(|C|\ge3\), a witness for one omitted vertex forces all the other omitted vertices into one part, which makes a second omitted vertex unwitnessable. The three-term enumerator, domination number, and minimum-set count follow immediately. The literal-definition verifier independently checks all multipartite profiles through order ten.

## originality

PASS

Prior work gives scalar super-domination values for complete multipartite graphs and enumerates minimum sets for complete graphs, stars, and complete bipartite graphs. The inspected 2022/2024 enumeration paper explicitly treats those special classes and contains no complete-multipartite all-set theorem. The audited complement classification yields the arbitrary-part minimum-set count and the full cardinality polynomial, neither implied by the scalar value alone.

## value

PASS

The theorem gives a natural complete classification and exact polynomial for an established domination variant, while subsuming several separately known boundary classes. Its short proof reflects the strong symmetry of complete multipartite graphs rather than an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
