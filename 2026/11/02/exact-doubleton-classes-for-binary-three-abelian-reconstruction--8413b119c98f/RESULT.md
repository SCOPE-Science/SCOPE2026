# Exact doubleton classes for binary three-abelian reconstruction

## Finding

For an integer \(n\ge2\), declare two binary words of length \(n\) equivalent when every contiguous factor of length at most three occurs equally many times in the two words. Let \(T_n\) count equivalence classes with **exactly two distinct words**. Then \(T_2=T_3=T_4=T_5=0\), and

| \(n\) | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(T_n\) | 4 | 18 | 52 | 78 | 106 | 106 | 116 | 122 |

For **every** \(n\ge14\),
\[
\boxed{T_n=10n-14+2\mathbf1_{2\mid n}+2\mathbf1_{n\equiv1\pmod3}.}
\]
Equivalently the complete generating function is
\[
\begin{aligned}
\sum_{n\ge2}T_nz^n={}&4z^6+18z^7+50z^8+58z^9+48z^{10}+20z^{11}+10z^{12}+4z^{13}\\
&+\frac{2z^8+18z^9+36z^{10}+24z^{11}+8z^{12}+2z^{13}}{1-z}\\
&+\frac{2z^{10}}{1-z^2}+\frac{6z^{11}+4z^{12}}{(1-z)^2}+\frac{2z^{13}}{1-z^3}.
\end{aligned}
\]
The growth is linear, even though the number of distinct binary three-abelian classes grows as a polynomial of degree six.

## Assumptions and scope

All words are indexed linear words over \(\{0,1\}\), with overlaps counted and with multiplicity. Length-two words have no three-letter factor. For \(n\ge3\), the length-three factor counts together with the first and last two letters determine the complete three-abelian observation, because the shorter-factor counts follow by summing extensions and the endpoints. The endpoint pair must always be retained; three-letter counts alone can conflate different three-abelian classes.

Let the four vertices of a directed de Bruijn graph be \(00,01,10,11\), and number its eight edges in order \(000,001,010,011,100,101,110,111\). Edge \(abc\) goes from \(ab\) to \(bc\). A word defines an Euler trail with prescribed initial and final vertices and with multiplicity vector \(m=(m_0,\ldots,m_7)\in\mathbb Z_{\ge0}^8\), whose sum is \(n-2\). Distinct words are exactly distinct trails when parallel edges of the same type are indistinguishable.

## Proof

**1. An exact local count.** Fix endpoints \(s,t\) and a balanced nonnegative edge-multiplicity vector. Let an active vertex be one incident to a positive edge or an endpoint. Root all directed spanning in-arborescences of the active support at \(t\). For each such tree choose the *type* of final outgoing edge from each nonroot active vertex, and arrange all other outgoing edges by type; at \(t\) arrange all outgoing edges. The last-exit algorithm is bijective with distinct Euler trails. Each vertex has at most two outgoing edge types. If its two remaining multiplicities are \(a,b\), its local ordering factor is \(\binom{a+b}{a}\). Summing the products over distinct type-arborescences gives the exact number of words in the class. The integer, saturated-at-three implementation `enumerate.cpp` computes whether that number is zero, one, two, or at least three. A final-edge tree is checked to reach \(t\), and directed self-loops never belong to an arborescence.

**2. Only one repeated outgoing type.** If a vertex had two distinct outgoing edge types each of multiplicity at least two, the corresponding local factor for any admissible final-edge tree would be at least three (at the root it is at least six). Hence a class of size at most two has at most one multiplicity-\(\ge2\) outgoing edge type at each vertex. Call these the *heavy edges*. The heavy-edge digraph is functional; its directed cycles are vertex-disjoint. For any noncycle heavy edge \(e\), take the set of heavy predecessors draining through \(e\). Across its boundary \(e\) is the sole outgoing heavy edge, and no heavy edge enters. Each nontrivial cut of the binary two-bit de Bruijn graph has at most two incoming ordinary edge types. The flow equation gives \(m_e\le3\), accounting for at most two unit-count edges and one endpoint imbalance.

**3. Canonical cycle reduction.** In each heavy directed cycle \(C\), subtract \(\min_{e\in C}m_e-2\) from every edge of \(C\). The reduced multiplicities remain positive, preserve the balance equations and the support, and have minimum two on every heavy cycle. For a cycle of length \(c\ge2\), applying flow balance to a consecutive segment of cycle vertices bounds the difference of any two cycle-edge counts by \(3(4-c)+3\): at most \(4-c\) incoming heavy-tree edges, each of weight at most three; at most two crossing unit edges; and one endpoint imbalance. Thus reduced cycle entries are at most eleven (and loops reduce to two). Noncycle heavy entries are at most three, so **every reduced profile has each entry between zero and twelve**.

When a heavy cycle is enlarged uniformly by a nonnegative integer \(h\), its edge support and its set of type-arborescences remain unchanged. Each local multinomial factor is either constant or increases with \(h\), and its increase is strict already from \(h=0\) to \(h=1\) whenever that factor is nonconstant. Since the heavy cycles are vertex-disjoint, increasing different cycles affects disjoint local factors. A reduced class containing exactly two words can therefore be enlarged along **only** the cycles for which a one-unit enlargement preserves class size two; those cycles can then be enlarged arbitrarily and independently. A reduced singleton cannot enlarge into a doubleton: with only one local ordering per tree, any heavy edge must occur in a local ordering whose remaining outgoing edges have only that same type, so enlargement preserves uniqueness. These observations are reversible; every doubleton has one canonical reduced profile and one tuple of permitted pumping amounts.

**4. Complete bounded census.** For all \(s,t\) and all multiplicity vectors in \(\{0,\dots,12\}^8\), `enumerate.cpp` enforces flow balance, evaluates the local-ordering sum, retains precisely the two-trail profiles, and performs the canonical reductions. Linear balance eliminates three edge variables, so only five are explicitly iterated. The code records exactly **316 distinct reduced doubleton profiles**. Their complete, individually reproducible records are in `PROFILES.tsv`. Grouped by reduced length and the lengths of their independently pumpable heavy cycles, the exact counts are:

| Reduced length | No pump | One cycle of length 1 | One cycle of length 2 | One cycle of length 3 | Two cycles of length 1 |
|---:|---:|---:|---:|---:|---:|
| 6 | 4 | 0 | 0 | 0 | 0 |
| 7 | 18 | 0 | 0 | 0 | 0 |
| 8 | 50 | 2 | 0 | 0 | 0 |
| 9 | 58 | 18 | 0 | 0 | 0 |
| 10 | 48 | 36 | 2 | 0 | 0 |
| 11 | 20 | 24 | 0 | 0 | 6 |
| 12 | 10 | 8 | 0 | 0 | 4 |
| 13 | 4 | 2 | 0 | 2 | 0 |

For a reduced length \(d\) and pump lengths \(c_1,\ldots,c_r\), the contribution is \(z^d/\prod_{i=1}^r(1-z^{c_i})\). Summing this table gives the displayed rational generating function. For \(n\ge14\), the constant pump contributions total \(90\), the two loop pumps contribute \(6(n-10)+4(n-11)\), and length-two and length-three pumps contribute \(2\mathbf1_{2\mid n}\) and \(2\mathbf1_{n\equiv1\pmod3}\). The formula follows.

## Verification

Run `python3 verify.py` with a C++17 compiler. It compiles and executes `enumerate.cpp`, checks that the output reproduces all 316 embedded profiles exactly, checks all 18 nonzero table cells and the rational-series coefficients through length 120, and separately compiles and executes `direct_census.cpp`. The latter enumerates every binary word at lengths 4 through 21 and independently groups words by three-mer counts **and both endpoints**. All checks passed from these packaged files. `PROFILES.tsv` is a complete finite certificate of the bounded step; neither finite verification nor the table alone substitutes for the structural reduction above.

## Relationship to prior work

The 2016 conference paper by Cassaigne, Karhumäki, Puzynina and Whiteland proves rationality for the *total* class-count sequence and for singleton classes, and explicitly evaluates their binary three-abelian formulas (Propositions 14 and 15). In particular, the singleton law is known and is **not** claimed here. The May 11, 2016 preprint of Karhumäki, Puzynina, Rao and Whiteland studies class cardinalities primarily through singleton structure and general bounds. Neither inspected primary text establishes the count of classes of cardinality **exactly two** for every length. The total number of classes together with the singleton number does not determine the number of doubletons because classes of three or more words coexist. The result refines, rather than rederives, those earlier statistics.

## Limitations

The theorem concerns binary, linear, exact three-abelian equivalence only; it does not provide complete class-size distributions, noisy observation results, or analogous formulas for other factor lengths. An expanded 2017 journal version of the 2016 conference paper was not fully accessible; this leaves a historical-priority risk despite the direct 2016 comparison. The proof relies on a finite exhaustive calculation of the 316 canonical profiles, reproduced in the standalone source and explicit certificate; the boundary reduction is necessary to make that finite step cover every input length.

## References

1. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *k-Abelian Equivalence and Rationality*, Developments in Language Theory (DLT 2016), LNCS 9840, 77–88. DOI: 10.1007/978-3-662-53132-7_7.
2. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319, first posted 2016-05-11.
3. OEIS A289657, count of all binary three-abelian classes, a different statistic.
