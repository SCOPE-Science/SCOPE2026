# The directed triangle Hom complex of every regular cyclic tournament has the homotopy type of a circle

## Finding
For each integer \(m\ge2\), let \(R_{2m+1}\) be the loop-free tournament on \(\mathbb Z/(2m+1)\mathbb Z\), with \(a\to b\) if and only if \(1\le(b-a)\bmod(2m+1)\le m\). Then the directed multihomomorphism complex of the oriented three-cycle satisfies
\[
\operatorname{Hom}(\overrightarrow C_3,R_{2m+1})\simeq S^1.
\]
The equivalence is established uniformly by identifying an explicit cyclic-interval nerve. The boundary case \(m=1\) has three isolated points instead and is excluded.

## Assumptions and scope
The complex uses the standard **directed Hom** construction, not the directed flag complex or path homology of a tournament. A cell is a triple \((A,B,C)\) of nonempty subsets of \(\mathbb Z/(2m+1)\mathbb Z\) satisfying all directed edges \(A\to B\), \(B\to C\), and \(C\to A\); its dimension is \(|A|+|B|+|C|-3\). Its face poset \(P\) is ordered by coordinatewise inclusion, and its order complex triangulates the regular CW complex.

Let \(N\) denote the simplicial complex on the same vertex set whose nonempty faces are the subsets contained in \(m\) consecutive cyclic vertices. This is a cyclic-interval complex, not the entire clique complex of a cycle power.

## Proof
**1. A map to cyclic intervals.** Define the order-preserving map \(f:P\to\mathcal F(N)\) by \(f(A,B,C)=A\), where \(\mathcal F(N)\) is the poset of nonempty faces. Given a cell, choose \(b\in B\) and \(c\in C\). Since \(b\to c\), all vertices of \(A\) lie in \(N^+(c)\cap N^-(b)\), a consecutive arc of \(d\) vertices with \(1\le d\le m\), where \(d\) is the clockwise distance from \(b\) to \(c\). Thus \(A\) is a face of \(N\). Conversely, if a nonempty face \(S\) is contained in the cyclic arc \(s,s+1,\ldots,s+m-1\), then \((S,\{s+m\},\{s+2m\})\) is a cell, all coordinates read modulo \(2m+1\).

**2. Every upper fiber is contractible.** Fix any nonempty face \(S\in N\). The set \(S\) has a unique shortest enclosing clockwise arc \([s,t]\) of length \(t-s+1\le m\), using integer lifts \(s\le t\le s+m-1\). Indeed, its complementary gap has at least \(m+1\) absent vertices, strictly longer than any other gap between successive vertices of \(S\). The common allowed choices for the other coordinates are precisely
\[
U:=\bigcap_{a\in S}N^+(a)=[t+1,s+m],\qquad
W:=\bigcap_{a\in S}N^-(a)=[t-m,s-1]
\]
with interval entries interpreted modulo \(2m+1\). Put \(b_*=s+m\). Every \(c\in W\), lifted to \([t+m+1,s+2m]\), satisfies \(1\le c-b_*\le m\). Hence \(b_*\to c\) for every \(c\in W\).

The upper fiber \(f^{-1}(\mathcal F(N)_{\ge S})\) consists of cells with \(S\subseteq A\). Within this fiber the following coordinatewise comparable, order-preserving maps yield a homotopy to a constant:
\[
(A,B,C)\ \ge\ (S,B,C)\ \le\ (S,B\cup\{b_*\},C)\ \ge\ (S,\{b_*\},C)\ \le\ (S,\{b_*\},W).
\]
Every displayed triple is a valid cell: shrinking \(A\) preserves the edge conditions, \(b_*\) dominates every permissible \(C\), and the final set \(W\) is dominated by \(b_*\) and points to all of \(S\). Thus each upper fiber is contractible. Applying the upper-fiber form of the finite-poset fiber theorem (the dual of Quillen's Theorem A) gives
\[
|P|\simeq |\mathcal F(N)|\cong |N|.
\]

**3. The cyclic-interval complex is a circle.** Regard \(\mathbb R/(2m+1)\mathbb Z\) as a circle and cover it by the \(2m+1\) open arcs
\[
U_i=\bigl(i-m+\tfrac12,\ i+\tfrac12\bigr),\qquad i\in\mathbb Z/(2m+1)\mathbb Z.
\]
These length-\(m\) arcs cover the circle when \(m\ge2\). All nonempty finite intersections are contractible: each complement is a closed connected arc of length \(m+1> (2m+1)/2\); the complements pairwise meet, so their union is connected, and its nonempty open-circle complement is one open arc. Their endpoints are half-integers, so any nonempty intersection contains an integer point. Such a point \(x\) belongs to precisely those \(U_i\) for which \(i\in\{x,x+1,\ldots,x+m-1\}\). Therefore the nerve is exactly \(N\). The nerve theorem yields \(|N|\simeq S^1\), proving the claim.

## Verification
The standalone `verify_fibers.py` tests the exact common-neighborhood descriptions, face eligibility, and distinguished contractible-fiber vertex for **every nonempty subset** at \(2m+1\in\{5,7,9,11,13,15\}\). The independently implemented `verify_chains.py` enumerates all Hom cells and builds signed cellular boundary matrices, computing mod-\(1000003\) Betti numbers at orders \(5,7,9,11,13\). All tested examples have Betti numbers \((1,1,0,\ldots)\). The finite tests check the formulas, while the argument above proves the entire infinite family without relying on extrapolation. Reproduction uses `python3 verify_fibers.py` and `python3 verify_chains.py` with Python 3.10 or newer and the standard library only.

## Relationship to prior work
Dochtermann and Singh (first available 2021, revised 2023), Sections 2.4, 5, and 7, establish the directed Hom construction, study transitive-tournament cases, and explicitly highlight nontransitive targets. Their illustrations include a seven-vertex tournament with a Möbius-strip Hom complex; the published results do not give this infinite cyclic-tournament classification. A previously published exact computation established the \(R_9\) instance with a discrete-Morse matching and explicitly limited its statement to that one tournament. The present theorem strictly extends that isolated case: it applies to every odd order at least five, by a different uniform fiber-and-nerve argument. Results about a tournament's directed **flag** complex or its **path homology** concern different functors and do not imply this Hom-complex statement.

## Limitations
The theorem concerns only the standard regular cyclic tournaments and source \(\overrightarrow C_3\). It does not classify arbitrary regular tournaments, all directed Hom complexes, or the equivariant action of source-cycle rotation on the resulting circle. No independent mathematical audit has been performed; exhaustive small instances and the written infinite-family argument are provided for reproducibility. An unindexed independent equivalent result cannot be excluded by literature searches.

## References
1. Anton Dochtermann and Anurag Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948 (first public version 24 August 2021; v2, 14 August 2023), especially §§2.4, 5, 7; European Journal of Combinatorics **110** (2023), 103704.
2. *The directed Hom complex \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) has the homotopy type of a circle*, published mathematical research record (2026), identifier `879b51cbdd1a`.
3. Daniel Quillen, *Higher algebraic K-theory I*, Lecture Notes in Mathematics **341** (1973), 85–147, Theorem A, and its standard finite-poset form.
4. Allen Hatcher, *Algebraic Topology* (2002), Corollary 4G.3 (nerve of a good open cover).
