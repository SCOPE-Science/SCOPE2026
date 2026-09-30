# One-step girth-frozen Ramanujan 2-lifts: a certified branch-choice obstruction

## Context

For a finite \(d\)-regular bipartite graph \(G\), a 2-lift is specified by signs \(s_e\in\{\pm1\}\). Marcus--Spielman--Srivastava guarantee a signing whose new eigenvalues lie in the Ramanujan interval, but that theorem does not require the same signing to raise girth. This record isolates an exact one-step obstruction to doing both greedily.

## Exact girth calculus

Let \(g=\operatorname{girth}(G)\) and let \(H\) be any 2-lift.

1. \(g\le \operatorname{girth}(H)\le 2g\).
2. A \(g\)-cycle \(C\) in \(G\) lifts to two \(g\)-cycles exactly when
   \(\prod_{e\in C}s_e=+1\); if the product is \(-1\), it lifts to one
   \(2g\)-cycle.
3. Therefore
   \[
   \operatorname{girth}(H)>g
   \quad\Longleftrightarrow\quad
   \prod_{e\in C}s_e=-1
   \text{ for every }g\text{-cycle }C.
   \]
   Writing \(x_e=(1-s_e)/2\in\mathbb F_2\), this is the linear system
   \(\sum_{e\in C}x_e=1\) for every shortest cycle \(C\).

Thus a base graph is *one-step girth-frozen* precisely when this system is inconsistent.

## Explicit Ramanujan witnesses

Use \(K_{3,3}\) with left vertices \(0,1,2\), right vertices \(3,4,5\), and edge order
\[
(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5).
\]
The signing
\[
(+1,+1,-1,+1,-1,+1,+1,-1,+1)
\]
has a connected 2-lift \(H_0\) on 12 vertices. Independent reconstruction gives

- \(\operatorname{girth}(H_0)=4\);
- exactly ten 4-cycles;
- signed spectral radius \(2.5615528128<2\sqrt2\), so the new eigenvalues are Ramanujan;
- the ten odd-product equations on the 18 edges of \(H_0\) have rank 6 over
  \(\mathbb F_2\) and are inconsistent.

Hence every immediate 2-lift of \(H_0\) still has girth 4. The second signing
\[
(-1,+1,-1,+1,-1,+1,+1,+1,+1)
\]
has the same certified properties.

For \(K_{d,d}\), \(d\ge3\), three appropriately chosen 4-cycle equations already sum to \(0=1\), so the odd-product system is inconsistent. As a contrasting raisable example, exhaustive enumeration of all \(2^{12}=4096\) signings of the cube \(Q_3\) gives exactly 128 signings whose lifts are connected, Ramanujan, and have girth 6.

## Scientific interpretation

The result is a one-step branch-choice obstruction, not an obstruction to all infinite 2-lift towers. Sampling children of a frozen witness finds many connected girth-4 children whose own shortest-cycle systems are satisfiable, so a longer tower can escape after a stalled step.

The exact criterion follows from standard covering/signing facts; the scientific content is the explicit small Ramanujan frozen witness and the accompanying frozen/raisable comparison. Searches of the Ramanujan 2-lift and graph-lift literature found general spectral-existence and lift-girth results but no source stating this 12-vertex rank-6 inconsistent witness or its one-step frozen status.

## Reproducibility

Run from the record directory:

- `python3 artifacts/certify_emergent.py`
- `python3 artifacts/kdd_obstruction.py`
- `python3 artifacts/enumerate_lifts.py`

The finite-field inconsistency checks are exact. Spectral certification uses floating point but has a margin about \(0.267\) below \(2\sqrt2\).

## Limitations

The obstruction is only one step. It neither proves nor disproves existence of logarithmic-girth Ramanujan 2-lift towers. The explicit nontrivial witnesses are degree 3; the \(K_{d,d}\) statement is a shortest-cycle obstruction independent of a full tower classification.

## References

- A. Marcus, D. Spielman, N. Srivastava, *Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees*, Annals of Mathematics 182 (2015).
- S. Hoory, *On the Girth of Graph Lifts*, arXiv:2401.01238.
