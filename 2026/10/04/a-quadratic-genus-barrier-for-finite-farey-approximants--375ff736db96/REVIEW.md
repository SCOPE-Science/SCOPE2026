# Review

## Correctness

PASS. Under \(\varphi_0\), the induced closed neighborhood of any vertex \(v\) has minimum degree at least \(3\): the center has degree at least \(3\), and every neighbor \(w\) of \(v\) has two distinct additional common neighbors with \(v\) coming from the two triangles on the edge \(\{v,w\}\). Hence that closed neighborhood has no removable vertex. The axiom \(\psi_n\) therefore forces its size to exceed \(n\), giving \(\deg(v)\ge n\) for every \(v\).

Every component consequently has at least \(n+1\) vertices and at least \(n|V|/2\) edges. Combining this with the standard orientable-surface bound \(|E|\le3|V|-6+6g\) gives \((n-6)|V|\le12(g-1)\), and then \(|V|\ge n+1\) yields the stated integer genus bound.

## Originality

PASS. Lockhart proves only the planar obstruction explicitly and then constructs approximants on higher-genus surfaces. The checked full text does not state the general minimum-degree consequence \(\delta(G)\ge n\) or a quantitative genus lower bound. Tent--Mohammadi provide the underlying axioms but do not study finite approximants or genus growth.

Candidate-specific published-finding and literature searches using Farey pseudofiniteness, finite approximants, minimum degree, orientable genus, and quadratic genus growth did not locate an equivalent theorem.

## Value

PASS. The primary paper's pseudofiniteness proof necessarily moves from planar graphs to higher-genus triangulations, but it leaves the amount of topological complexity unquantified. The theorem shows that higher genus is forced for every finite approximant, not merely for the chosen construction, and that the necessary genus grows at least quadratically with the axiom depth. This gives a natural structural constraint on all possible pseudofinite approximation schemes.

## Closest literature and limitations

Lockhart (2026) is the direct source: Proposition 4 proves the \(g=0\) obstruction, while the later construction uses high-genus triangulations. Tent--Mohammadi (2025/2026) supply the complete-theory axiomatization and removable-vertex notion. Standard surface graph theory supplies the Euler edge bound.

No optimality or matching upper bound is claimed.

Same-model review: passed. Independent audit: not yet performed.
