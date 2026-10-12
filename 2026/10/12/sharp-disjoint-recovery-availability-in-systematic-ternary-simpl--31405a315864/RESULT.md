# Sharp disjoint recovery availability in systematic ternary simplex LCD codes

## Finding
For each integer \(n\ge 2\), the systematic ternary LCD family constructed by Mondal and Lee has an explicit, coordinate-dependent spectrum of **minimal two-helper recovery sets** and an exact maximum number of **pairwise disjoint recovery sets**. Let \(L_n=(3^{n-1}-1)/2\), and let \(h\) be the number of nonzero entries of a normalized generator column representing the target's projective point. Then the number \(R_2(h)\) of unordered two-helper sets that recover the target, with neither helper alone sufficient, equals
\[
R_2(h)=\begin{cases}
12L_n+4(n-1),&h=1,\\
12L_n+4n+1,&h=2,\\
12L_n+4n,&3\le h\le n.
\end{cases}
\]
The largest pairwise disjoint family of these two-helper sets has size
\[
A_2(h)=3L_n+\mathbf{1}_{\{h=2\}}.
\]
There are exactly \(a_1(h)=2\) singleton recovery sets for \(h=1\), and exactly \(a_1(h)=1\) otherwise. Consequently the sharp number of pairwise disjoint recovery sets using **at most two helpers** is \(3L_n+2\) for \(h=1,2\) and \(3L_n+1\) for \(h\ge3\). Thus ordinary locality is one for every coordinate, but the more informative two-helper repair spectrum is nonuniform.

The three coordinate classes contain, respectively, \(3n\), \(2n(n-1)\), and \(3^n-1-2n^2\) coordinates. The number of distinct three-coordinate circuits in the dual matroid is
\[
T_n=\frac{3n[12L_n+4(n-1)]+2n(n-1)[12L_n+4n+1]+(3^n-1-2n^2)[12L_n+4n]}{3}.
\]
For \(n=2,3,4\), this gives \(T_n=60,572,4808\).

## Assumptions and scope
Work over \(\mathbb F_3\). For every integer \(n\ge2\), let \(G_n\) be an \(n\)-row matrix whose columns comprise each vector of \(\mathbb F_3^n\setminus\{0\}\) exactly once, with any fixed ordering. Let \(C_n\) be the row space of \([I_n\mid G_n]\). These are the codes in Mondal–Lee Theorem 3.7, with parameters \([n+3^n-1,n,2\cdot3^{n-1}+1]_3\). A recovery set for coordinate \(i\) is a subset of other coordinates from which \(c_i\) is a fixed linear combination for all \(c\in C_n\). A two-helper set is **minimal** if neither of its singleton subsets recovers \(i\). We count sets, not scalar choices for their recovery equations. Two recovery sets for a given target are disjoint when their helper coordinates have empty intersection; the target is not included in either set. The weight \(h\) refers to any nonzero representative of a projective generator column: scaling does not change its zero pattern.

## Proof
**Projective multiplicities.** The nonzero vectors form the two nonzero representatives of each point in \(\mathrm{PG}(n-1,3)\). The added systematic block contributes one extra copy at each of the \(n\) coordinate-axis points. Therefore the generator-column multiplicity is \(m(P)=3\) for a coordinate axis and \(m(P)=2\) otherwise. Every coordinate has exactly \(m(P)-1\) singleton recovery helpers, its other copies at \(P\).

**Characterization of minimal pairs.** A target column at \(P\) is spanned by two columns from projective points \(Q\) and \(R\), with neither alone sufficient, if and only if \(P,Q,R\) are three distinct points on one projective line. Indeed, three distinct points in a two-dimensional vector subspace are pairwise independent but linearly dependent. This also shows each such triple is a minimal support of a weight-three dual word; pairs involving a column parallel to the target are excluded by minimality.

**Exact count.** Exactly \(L_n=(3^{n-1}-1)/(3-1)\) projective lines pass through a fixed \(P\), and each has precisely three other projective points. If each point has two column copies, each line contributes three choices of the distinct other point pair and four copies per pair: \(12\) sets. Each coordinate-axis point \(Q\ne P\) on a line adds one extra copy and hence four extra helper pairs. A line containing two such axes gains a further one from their simultaneous multiplicity increase. No line contains three distinct coordinate axes. If \(P\) itself is an axis, its \(n-1\) other axes lie on distinct lines through \(P\). If \(P\) has weight two, the line joining its two nonzero-coordinate axes is the unique line through \(P\) containing two axes: all \(n\) axes contribute four each plus one additional pair. For weight at least three, the lines from \(P\) to the \(n\) axes are all distinct. These three cases give the displayed \(R_2(h)\) formulas.

**Sharp disjoint matching.** The other projective points on two different lines through \(P\) are disjoint, so recovery pairs on different lines cannot share a helper. On one line the recovery-helper graph is complete tripartite, with vertex-part sizes corresponding to the three other projective points. These sizes are \((2,2,2)\), \((3,2,2)\), or \((3,3,2)\); the exact maximum matching sizes are respectively \(3\), \(3\), and \(4\). Each value follows from the vertex-count upper bound and explicit matching of unlike classes (for example, for \(3,3,2\), match two vertices of the first size-three class to two of the second, and pair each remaining size-three-class vertex with a distinct vertex in the size-two class). Thus every line normally contributes \(3\) and the unique two-axis line through a weight-two \(P\) contributes \(4\). Hence \(A_2(h)=3L_n+\mathbf 1_{\{h=2\}}\). All parallel copies of \(P\) supply singleton recovery sets disjoint from every minimal two-helper set, establishing the additive optimum \(a_1(h)+A_2(h)\).

**Class and circuit counts.** A coordinate-axis point has three copies, so there are \(3n\) weight-one coordinates. There are \(\binom n2\cdot2^2/2= n(n-1)\) projective points of weight two, each with two copies, giving \(2n(n-1)\) coordinates. The remaining count follows by subtracting from length \(n+3^n-1\). Finally every distinct three-coordinate dual circuit is counted exactly three times among all targets, giving the stated \(T_n\). This completes the all-parameter proof.

## Verification
Run the standalone standard-library script `verify.py` with Python 3. It constructs the actual generator columns from scratch and, for each \(n\in\{2,3,4\}\), independently enumerates every target and all of its minimal two-helper pairs, computes maximum matching sizes of the per-line helper graphs via exhaustive subset dynamic programming, checks projective multiplicities and the three predicted target classes, and recomputes the total circuit count. Successful execution ends with `VERIFY_OK`. These finite checks test boundary cases and formulas; the proof above, rather than finite enumeration, establishes the claim for every \(n\ge2\).

## Relationship to prior work
Mondal and Lee, *Infinite families of LCD codes and their weight distributions* (published 4 September 2026), Theorem 3.7, establish this exact systematic code and its distance, optimality, and ordinary weight distribution. Those statements do not determine the number or disjoint packing of local two-helper recovery sets. Grezet and Hollanti, *The complete hierarchical locality of the punctured Simplex code* (2020), analyze punctured simplex codes and hierarchical locality rather than this identity-augmented full-vector code with unequal projective multiplicities. Jurrius, *Weight enumeration of codes from finite spaces* (2011), studies simplex subcode-support geometry, not per-coordinate minimal repair triples or their sharp disjoint matching numbers. The present result is an invariant of the explicitly defined, already-known code family, not a claim to invent its construction.

## Limitations
The code has ordinary locality one owing to parallel column copies, so no improvement of minimum repair locality is asserted. The two-helper counts intentionally exclude redundant pairs containing singleton helpers. Exact two-helper availability is not by itself a reliability probability under any specified failure model, and no performance gain or independent certification is claimed. A mathematical rederivation from general projective incidence methods is possible; previously overlooked equivalent formulas remain a literature risk.

## References
1. N. K. Mondal and Y. Lee, *Infinite families of LCD codes and their weight distributions*, Applicable Algebra in Engineering, Communication and Computing, published 4 September 2026, https://doi.org/10.1007/s00200-026-00756-3. See Theorem 3.7 and its proof.
2. M. Grezet and C. Hollanti, *The complete hierarchical locality of the punctured Simplex code*, Designs, Codes and Cryptography 89 (2021), 105–125, first published 2020, https://doi.org/10.1007/s10623-020-00810-2.
3. F. Jurrius, *Weight enumeration of codes from finite spaces*, Designs, Codes and Cryptography (2011), https://doi.org/10.1007/s10623-011-9557-2.
