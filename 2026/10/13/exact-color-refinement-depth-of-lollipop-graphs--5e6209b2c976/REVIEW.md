# Independent mathematical audit

## correctness

PASS

For m≥4 the initial degree partition isolates the clique attachment q0 (degree m), ordinary clique class Q (degree m−1), all degree-two path interiors and the leaf. The two path boundary fronts split from the one unresolved interval p_r..p_{n-r}, which becomes size≤1 at round ceil(n/2). For m=3 the ordinary triangle vertices have degree 2 and share a color with path interior; cases n=1,2 stabilize in rounds 1,2, and for n≥3 round three first separates Q from p1, after which the two-sided wave applies. The base cases and partition-stability convention were reconstructed. Independent WL implementation checked all 484 m=3..13,n=1..44 pairs (source also supplies independent partition checker).

## originality

PASS

Best-of-knowledge exact family-specific ordinary-WL stabilization law, with sharp exceptional m=3 degree collision. Relevant general WL iteration works and published lollipop metric results use different invariants; no stronger prior implication was established from read material.

## value

PASS

The exact stabilization time of a standard clique–path family is a motivated natural invariant for practical color refinement. The m=3 exception is not mere parameter substitution: a degree-2 collision delays separation and changes the entire small-n phase diagram. A complete formula over unbounded n clarifies the iteration mechanism and supplies sharp benchmark families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
