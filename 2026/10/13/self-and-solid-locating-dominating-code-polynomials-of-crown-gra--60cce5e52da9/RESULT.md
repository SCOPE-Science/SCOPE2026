# Self- and solid-locating-dominating code polynomials of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,\qquad n\ge3,
\]
have bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where \(M=\{a_i b_i:1\le i\le n\}\). For a code \(C\), put
\[
P=\{i:a_i\notin C\},\qquad Q=\{i:b_i\notin C\}.
\]

The code \(C\) is solid-locating-dominating exactly when either \(P\cap Q=\varnothing\), except for
\[
P=\{i\},\quad Q=[n]\setminus\{i\}
\]
and the symmetric \(2n\) domination failures, or when
\[
P=Q=\{i\}.
\]
Therefore
\[
D_{\mathrm{DLD}}(\operatorname{Cr}_n;z)
=
z^n(z+2)^n-2nz^n+nz^{2n-2}.
\]

The code \(C\) is self-locating-dominating exactly when
\[
P=\varnothing,\qquad Q=\varnothing,
\]
or
\[
P=Q=\{i\}.
\]
Hence
\[
D_{\mathrm{SLD}}(\operatorname{Cr}_n;z)
=
2z^n(1+z)^n-z^{2n}+nz^{2n-2}.
\]

Consequently
\[
\gamma_{\mathrm{DLD}}(\operatorname{Cr}_n)
=
\gamma_{\mathrm{SLD}}(\operatorname{Cr}_n)
=
n.
\]
There are exactly \(2^n-2n\) minimum solid-locating-dominating codes and exactly two minimum self-locating-dominating codes, the two bipartition classes.

## Assumptions and scope
For a nonempty code \(C\), write
\[
I(C;u)=N[u]\cap C.
\]
A code is solid-locating-dominating when every non-codeword is dominated and, for distinct non-codewords \(u,v\),
\[
I(C;u)\setminus I(C;v)\ne\varnothing.
\]
It is self-locating-dominating when, for every non-codeword \(u\),
\[
I(C;u)\ne\varnothing
\quad\text{and}\quad
\bigcap_{c\in I(C;u)}N[c]=\{u\}.
\]
The polynomials count codes by cardinality.

## Proof
For every omitted \(a_i\),
\[
I(C;a_i)=C_B\setminus\{b_i\},
\]
and symmetrically
\[
I(C;b_i)=C_A\setminus\{a_i\}.
\tag{1}
\]

For solid location-domination, if distinct \(i,j\in P\), then
\[
I(C;a_i)\setminus I(C;a_j)\ne\varnothing
\]
exactly when \(b_j\in C\). Thus \(|P|\ge2\) forces \(P\cap Q=\varnothing\), and symmetrically \(|Q|\ge2\) does the same. Hence any overlap can occur only as \(P=Q=\{i\}\), which is feasible.

When \(P\cap Q=\varnothing\), all identifying sets in (1) are pairwise ordered-incomparable except when domination itself fails. An omitted \(a_i\) is undominated exactly when \(C_B=\{b_i\}\), which under disjointness is
\[
P=\{i\},\qquad Q=[n]\setminus\{i\}.
\]
There are \(n\) such cases and \(n\) symmetric ones. This proves the solid classification.

For counting, each matched index in a disjoint omission pattern has three possibilities: select both endpoints, omit only \(a_i\), or omit only \(b_i\), contributing \(z^2+2z=z(z+2)\). Thus the disjoint patterns contribute \(z^n(z+2)^n\). Removing the \(2n\) bad size-\(n\) codes and adding the \(n\) exceptional matched-pair omissions of size \(2n-2\) gives the solid polynomial.

For self location-domination, suppose both \(P\) and \(Q\) are nonempty. Fix \(i\in P\). Comparing the non-codeword \(a_i\) with every codeword \(a_j\), \(j\notin P\), forces \(b_j\in C\), hence \(Q\subseteq P\). Symmetry gives \(P\subseteq Q\), so \(P=Q\). Since every self-locating-dominating code is solid-locating-dominating, the solid classification reduces this to \(P=Q=\{i\}\).

Conversely, if \(Q=\varnothing\), all vertices of \(B\) are codewords. Formula (1) and the availability of a third index when \(n\ge3\) distinguish every omitted \(a_i\) from every other vertex. Thus every code with \(Q=\varnothing\) is self-locating-dominating; the case \(P=\varnothing\) is symmetric, and \(P=Q=\{i\}\) is checked the same way. Counting these families yields the self polynomial.

The lowest nonzero power of each polynomial is \(z^n\). Its coefficients are \(2^n-2n\) and \(2\), respectively.

## Verification
The included verifier exhaustively constructs every crown graph for
\[
3\le n\le8
\]
and tests every vertex subset from the defining identifying-set conditions. It compares direct feasibility with the two structural classifications, every polynomial coefficient, both minima, and the minimum-code counts.

## Relationship to prior work
Self-locating-dominating and solid-locating-dominating codes were introduced in 2018. The introducing work studies rook graphs and binary Hamming spaces rather than crown graphs.

A later primary treatment develops equivalent identifying-set characterizations, bounds, trees, Cartesian products, and realization results. It notes that complete bipartite graphs with both parts nontrivial are extreme for self-location-domination: every vertex is forced into a self-locating-dominating code. Its searchable full text contains no crown occurrence.

Thus deleting only a perfect matching from \(K_{n,n}\) changes self-location-domination from complete-bipartite rigidity to minimum size \(n\), with exactly the two bipartition classes as bases. Solid location-domination also drops to \(n\), but has the much richer minimum-code count \(2^n-2n\).

Targeted literature searches under the crown name, \(K_{n,n}\) minus a perfect matching, and both stronger location-domination names did not locate these all-code classifications or polynomials.

## Limitations
The theorem concerns connected crowns \(n\ge3\). It treats self- and solid-locating-domination, not ordinary locating domination, identifying codes, or open locating domination. The exhaustive computation through \(n=8\) is corroborative; the arbitrary-\(n\) result follows from (1). A differently phrased or non-indexed crown treatment may exist.

## References
1. V. Junnila, T. Laihonen, T. Lehtilä, “On regular and new types of codes for location-domination,” Discrete Applied Mathematics 247 (2018), 225–241, DOI 10.1016/j.dam.2018.03.050; available online 13 April 2018.
2. V. Junnila, T. Laihonen, T. Lehtilä, M. L. Puertas, “On Stronger Types of Locating-Dominating Codes,” arXiv:1808.06891v1, 21 August 2018; Discrete Mathematics & Theoretical Computer Science 21:1 (2019), DOI 10.23638/DMTCS-21-1-1.
