# A rank-four automorphism with ideal Whitehead graph \(K_{4,3}\)

Let \(F_4=F(a,b,c,d)\), write capital letters for inverses, and let \(f\) be the rose representative of
\[
\Phi(a)=bc,\qquad\Phi(b)=c,\qquad\Phi(c)=d,\qquad\Phi(d)=a.
\]
Its outer class is ageometric fully irreducible and atoroidal. Its ideal Whitehead graph is \(K_{4,3}\), and its rotationless index list is \(\{-5/2\}\). The construction is an explicit example, not a new general irreducibility criterion.

## Exact finite data

The inverse substitution is \(a\mapsto d,b\mapsto aB,c\mapsto b,d\mapsto c\). The transition matrix, with rows recording occurrences in the corresponding edge image, is
\[
M=\begin{pmatrix}0&1&1&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\end{pmatrix},\quad
M^{10}=\begin{pmatrix}3&1&2&3\\2&1&1&1\\1&2&3&1\\1&1&3&3\end{pmatrix}.
\]
Thus \(M\) is primitive; direct expansion gives \(\det M=-1\) and \(\det(xI-M)=x^4-x-1\). All edge iterates are positive words or their inverses, so \(f\) is an expanding train track.

The direction map has positive cycle \(a\to b\to c\to d\to a\), negative cycle \(A\to C\to D\to A\), and \(B\to C\). Its gates are \(\{a\},\{b\},\{c\},\{d\},\{A,B\},\{C\},\{D\}\); its only nondegenerate illegal turn is \(\{A,B\}\).

The taken turns are the direction-map orbit of \(\{B,c\}\):
\[
\{B,c\},\{C,d\},\{D,a\},\{A,b\},\{C,c\},\{D,d\},\{A,a\},\{C,b\},\{D,c\},\{A,d\},\{C,a\},\{D,b\},\{A,c\}.
\]
They form a connected local Whitehead graph. Deleting the nonperiodic direction \(B\) leaves exactly the twelve edges between \(\{a,b,c,d\}\) and \(\{A,C,D\}\).

## A universal no-periodic-Nielsen-path certificate

The taken-turn calculation alone does not rule out a periodic Nielsen path. The following independent cancellation argument supplies that essential hypothesis.

Put \(g=f^6\). Its negative edge images are
\[
g(A)=ADDC,\qquad g(B)=AD,\qquad g(C)=CBA,\qquad g(D)=DCCB.
\]
Take any two legal arms starting in \(A\) and \(B\), and remove the common prefix of their \(g\)-images. Initially the unmatched suffix pair is \((DC,\varnothing)\). While only one suffix is nonempty, extend the exhausted arm by its next edge and again delete the common prefix. If that edge is positive, the two first unmatched directions have opposite signs and their turn is legal. It is consequently enough to examine all four negative extensions, even if an extension is not admissible in a particular input arm.

There are exactly six reachable undecided states. In the table, an ordered pair of distinct directions denotes the terminal first-mismatch pair; otherwise the cell names the next state.

| State (unmatched suffixes) | next \(A\) | next \(B\) | next \(C\) | next \(D\) |
|---|---|---|---|---|
| 1: \((DC,\varnothing)\) | \((D,A)\) | \((D,A)\) | \((D,C)\) | 2 |
| 2: \((\varnothing,CB)\) | \((A,C)\) | \((A,C)\) | 3 | \((D,C)\) |
| 3: \((A,\varnothing)\) | 6 | 4 | \((A,C)\) | \((A,D)\) |
| 4: \((\varnothing,D)\) | \((A,D)\) | \((A,D)\) | \((C,D)\) | 5 |
| 5: \((CCB,\varnothing)\) | \((C,A)\) | \((C,A)\) | \((C,B)\) | \((C,D)\) |
| 6: \((\varnothing,DDC)\) | \((A,D)\) | \((A,D)\) | \((C,D)\) | \((C,D)\) |

The state graph is acyclic. Every terminal turn is legal: none is \(\{A,B\}\). Thus the argument handles arbitrarily long arms, not merely words up to a search cutoff. If an arm ends before a mismatch, tightening leaves a subpath of the other legal arm. Endpoints in edge interiors cause the same two alternatives: a truncated image ends before the first mismatch, or contains that mismatch, already legal. Legal arms map to legal arms under a train track.

For an expanding irreducible train track, an indivisible periodic Nielsen path has two legal arms joined at an illegal turn (Bestvina–Handel Lemma 3.4; also Kapovich–Pfaff Proposition 2.23). Here that turn must be \(\{A,B\}\). The table shows that its tightened \(g\)-image is legal. All subsequent iterates remain legal, so it cannot recur to the original illegal path. No indivisible periodic Nielsen path exists. Any periodic Nielsen path decomposes into indivisible ones, so none exists at all.

## Consequences

Pfaff's Full Irreducibility Criterion now applies: the map is PNP-free, its transition matrix is primitive, and its local Whitehead graph is connected. It follows that the outer class is fully irreducible; PNP-freeness also gives ageometricity. Its ideal Whitehead graph is its stable Whitehead graph, hence \(K_{4,3}\). There is one seven-vertex component, giving index \(1-7/2=-5/2\). The fully irreducible geometric/atoroidal dichotomy gives atoroidality. The positive periodic directions have period four and the negative ones period three, so \(Df^{12}\) fixes every periodic direction.

## Reproducibility and scope

Run `python artifacts/certify.py`. The checker uses exact integer and word operations. In particular it reconstructs the entire reachable cancellation-state graph and checks acyclicity, not a bounded-length Nielsen-path search. The theorem applications above are mathematical deductions from that certificate.

The prior literature supplies the criteria and invariant definitions. No equivalent exact substitution/graph realization was found in the literature and corpus searches; this is a best-of-knowledge statement, not proof that no unindexed example exists.

## Primary references

- C. Pfaff, [Ideal Whitehead Graphs in Out(Fr) II: The Complete Graph in Each Rank](https://catherinepfaff.com/CompleteGraphs.pdf), Proposition 4.1 and its proof.
- I. Kapovich and C. Pfaff, [A Train Track Directed Random Walk on Out(Fr)](https://web.math.ucsb.edu/~cpfaff/RandomWalk.pdf), Sections 2.7–2.10, especially Propositions 2.23, 2.25, 2.27, 2.31 and Definitions 2.32–2.33.
- M. Bestvina and M. Handel, *Train tracks and automorphisms of free groups*, Annals of Mathematics 135 (1992), 1–51.
