# Dissociation polynomial and extremal coefficients of fan graphs
## Finding
For every fan graph \(F_n=K_1\vee P_n\) with \(n\ge4\), let \(D_{F_n}(z)=\sum_{S}z^{|S|}\), where the sum is over all dissociation sets. If \(Q_n(z)\) is defined by \(Q_0(z)=1\), \(Q_1(z)=1+z\), \(Q_2(z)=(1+z)^2\), and \[Q_n(z)=Q_{n-1}(z)+zQ_{n-2}(z)+z^2Q_{n-3}(z)\quad(n\ge3),\]then \[D_{F_n}(z)=Q_n(z)+z+n z^2.\] Moreover, for \(0\le k\le n\), \[[z^k]Q_n(z)=\sum_{b=\lceil k/2\rceil}^{\min\{k,n-k+1\}}\binom{b}{k-b}\binom{n-k+1}{b}.\] Consequently \(\operatorname{diss}(F_n)=\lceil2n/3\rceil\). Writing \(n=3q+r\) with \(r\in\{0,1,2\}\), the number of maximum dissociation sets is \((q+1)(q+2))/2\) when \(r=0\), \(q+1\) when \(r=1\), and \(1\) when \(r=2\).

## Assumptions and scope
All graphs are finite and simple. For \(n\ge4\), the fan graph is
\[
F_n=K_1\vee P_n,
\]
with cone vertex \(c\) and path vertices \(v_1,\ldots,v_n\).

A dissociation set is a vertex set whose induced subgraph has maximum degree at most \(1\). Its size enumerator is
\[
D_G(z)=\sum_{S\in\mathcal D(G)}z^{|S|}.
\]

## Proof
Split a dissociation set \(S\) according to whether it contains the cone vertex.

If \(c\in S\), then \(c\) is adjacent to every selected path vertex. Since its induced degree must be at most \(1\), at most one path vertex can belong to \(S\). Conversely, \(\{c\}\) and every \(\{c,v_i\}\) are dissociation sets. These sets contribute
\[
z+n z^2.
\]

Now suppose \(c\notin S\). Then \(S\) is a dissociation set of the path \(P_n\). Encode its path incidence vector by a binary word of length \(n\). The induced maximum degree is at most \(1\) exactly when the word has no three consecutive ones. Let \(Q_n(z)\) be the weight enumerator of such words, with a selected vertex contributing a factor \(z\).

Every admissible word ends in exactly one of the suffix types \(0\), \(01\), or \(011\). Removing that suffix gives an arbitrary admissible word of length \(n-1\), \(n-2\), or \(n-3\), respectively. Therefore
\[
Q_n(z)=Q_{n-1}(z)+zQ_{n-2}(z)+z^2Q_{n-3}(z),
\]
with \(Q_0(z)=1\), \(Q_1(z)=1+z\), and \(Q_2(z)=(1+z)^2\). Combining the two cone cases gives
\[
D_{F_n}(z)=Q_n(z)+z+nz^2.
\]

For the coefficient formula, fix a path dissociation set of size \(k\). Its selected vertices form \(b\) blocks, each of length one or two. If \(d\) blocks have length two, then \(k=b+d\), so \(d=k-b\), and the doubled blocks can be chosen in
\[
\binom{b}{k-b}
\]
ways. The \(b\) selected blocks require \(b-1\) separating zeroes. After reserving those separators, the remaining zeroes can be distributed among the \(b+1\) gaps before, between, and after the selected blocks in
\[
\binom{n-k+1}{b}
\]
ways. Summing over all feasible \(b\) gives
\[
[z^k]Q_n(z)=
\sum_{b=\lceil k/2\rceil}^{\min\{k,n-k+1\}}
\binom{b}{k-b}\binom{n-k+1}{b}.
\]

The largest binary word with no \(111\) has
\[
\left\lceil\frac{2n}3\right\rceil
\]
ones, obtained by repeating blocks of two ones followed by a zero and truncating at the end. Because \(n\ge4\), this size is at least three, so cone-containing dissociation sets cannot be maximum. Hence
\[
\operatorname{diss}(F_n)=\left\lceil\frac{2n}3\right\rceil.
\]

Finally, substitute the maximum value of \(k\) into the block formula. For \(n=3q\), only \(b=q\) and \(b=q+1\) occur, giving
\[
(q+1)+\binom{q+1}2=\frac{(q+1)(q+2)}2.
\]
For \(n=3q+1\), only \(b=q+1\) occurs and exactly one of the \(q+1\) blocks has length one, giving \(q+1\). For \(n=3q+2\), all \(q+1\) blocks have length two, giving one maximum set.

## Verification
The included checker constructs each fan graph directly for \(4\le n\le17\) and tests every vertex subset against the definition by computing induced degrees.

Independently, it checks the cone/path structural split, expands the three-term polynomial recurrence, verifies the closed coefficient formula for every \(k\), and checks the dissociation number and the three residue-class formulas for the number of maximum sets.

## Relationship to prior work
The 2023 paper that introduced the dissociation polynomial as a weighted counting object studies extremal dissociation-set counts for cubic graphs. Its full text defines
\[
D_G(\lambda)=\sum_{S\in\mathcal D(G)}\lambda^{|S|}
\]
and proves a sharp cubic-graph extremal theorem, but targeted full-text searches found no fan graph, path, or graph-join treatment.

The present result concerns the noncubic fan family and gives an exact all-coefficient formula, not merely a maximum-size parameter. Targeted searches for dissociation polynomials of fan graphs, cones over paths, and joins of a vertex with a path did not locate an equivalent formula.

## Limitations
The theorem concerns ordinary dissociation sets and the standard fan \(K_1\vee P_n\), with \(n\ge4\). The recurrence is finite and exact, but no claim is made here about roots, unimodality, or asymptotic zero distributions. Literature search cannot exclude a differently phrased or non-indexed fan enumeration.

## References
1. J. Tu, J. Xiao, R. Lang, “Counting the number of dissociation sets in cubic graphs,” AIMS Mathematics 8(5) (2023), 10021–10032, DOI 10.3934/math.2023507. Published online 23 February 2023.
