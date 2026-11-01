# Exact transient-shell equidistribution for three-state excitation on book graphs

## Finding

Let \(B_m=K_2\vee\overline K_m\) be the labelled triangular book with \(m\ge1\) pages: two adjacent hubs, each adjacent to all \(m\) mutually nonadjacent page vertices. For either synchronous three-color cyclic cellular automaton (CCA) or synchronous three-state Greenberg–Hastings dynamics (GHM), write \(T\) for the smallest nonnegative update time at which the complete labelled state is periodic, \(P\) for its least eventual period, and \(D_{M,t,p}(m)\) for the number of initial three-colorings with \((T,P)=(t,p)\) under model \(M\).

The **complete** first-periodic-entry census, valid for every \(m\ge1\), is as follows. In the table set \(u=2^m\), \(v=3^m\), and \(q=2(v-2u+1)\); all entries not displayed are zero.

| \((T,P)\) | CCA | GHM |
|:--|--:|--:|
| \((0,1)\) | \(3\) | \(1\) |
| \((0,3)\) | \(6(u-1)\) | \(6(u-1)\) |
| \((1,1)\) | \(9u\) | \(4u-1\) |
| \((1,3)\) | \(3q\) | \(q\) |
| \((2,1)\) | \(3(v-u-1)\) | \(v+2u\) |
| \((2,3)\) | \(0\) | \(q\) |
| \((3,1)\) | \(0\) | \(v+u+1\) |
| \((3,3)\) | \(0\) | \(q\) |
| \((4,1)\) | \(0\) | \(v-u-1\) |

Both models have exactly \(2(2^m-1)\) primitive three-cycle orbits, **the same recurrent three-cycle configurations, and the same next-state map on that recurrent set**. The fixed configurations are the three monochromatic states in CCA and the all-zero state in GHM. No other eventual periods occur. The maximum first-periodic-entry time is one for CCA when \(m=1\), two for CCA when \(m\ge2\), three for GHM when \(m=1\), and four for GHM when \(m\ge2\).

For every \(m\ge2\), conditional on eventual period three **and on not already being periodic**, GHM has the exactly uniform law
\[
\Pr(T=j\mid P=3,T>0)=\tfrac13\quad(j=1,2,3),
\]
whereas every corresponding CCA state enters the three-cycle at precisely \(T=1\). The two models nevertheless have the identical period-three attraction-basin size \(6(3^m-2^m)\) and identical uniform-initial-state oscillation probability \(\frac23(1-(\frac23)^m)\). Under uniformly random initial colors, \(T\) converges in distribution to the CCA law \(\Pr(T=1)=2/3\), \(\Pr(T=2)=1/3\), versus the GHM law \(\Pr(T=1)=2/9\), \(\Pr(T=2)=1/3\), \(\Pr(T=3)=1/3\), \(\Pr(T=4)=1/9\).

## Assumptions and scope

All graphs are simple and all page vertices are individually labelled; no division by graph automorphisms is made. The color alphabet is \(\{0,1,2\}\), interpreted cyclically modulo three. Updates are simultaneous. In CCA, a vertex of color \(c\) changes to \(c+1\pmod3\) exactly when it has a neighbor of that successor color. In GHM, colors one and two advance automatically (to two and zero), while a zero changes to one precisely when it has a neighbor of color one, remaining zero otherwise. The first-periodic-entry time \(T\) means the least \(t\ge0\) for which there is some \(p\ge1\) with \(F^{t+p}(x)=F^t(x)\); \(P\) is the least such \(p\) at this \(t\). Counts refer to all \(3^{m+2}\) labelled initial states.

## Proof

**1. Exact support compression.** Let the two initial hub colors be \((a,b)\), and let \(S\subseteq\{0,1,2\}\) be the **nonempty** set of initial page colors. Each initial color \(s\in S\) occurs on at least one page, and all pages of that initial color have identical neighborhoods and therefore evolve identically. At any subsequent time, let \(\phi(s)\) denote their common color. Hence the full labelled state is represented *injectively along this trajectory* by
\[
(a_t,b_t,(\phi_t(s))_{s\in S}),
\]
starting at \((a,b,(s)_{s\in S})\). This representation remains exact even when two distinct initial color classes merge, since \(S\) is retained as a set of distinct original labels. Thus repetition times and least periods in this representation agree with those of the full microscopic configuration, for every positive multiplicity of each color in \(S\).

Define \(L_M(c;N)\) for a present color \(c\) and a collection of neighboring colors \(N\) by the update rules above (only set membership matters). A single reduced update is the *exact deterministic map*
\[
(a,b,\phi)\longmapsto\bigl(L_M(a;\{b\}\cup\phi(S)),\ L_M(b;\{a\}\cup\phi(S)),\ (L_M(\phi(s);\{a,b\}))_{s\in S}\bigr).
\]
There are exactly nine ordered hub pairs and seven nonempty original page supports. All future states and first-repeat times for these 63 initial classes can therefore be checked independently of \(m\).

**2. Exhaustive finite transition lemma.** In the following complete transition tables, a cell `t/p` means \(T=t\) and \(P=p\). The hub-pair columns are, in order, `00 01 02 10 11 12 20 21 22`. Each row is the original support \(S\), not the support after any update. Applying the displayed reduced update until its first repeated state gives:

| \(S\) | CCA: ordered values in the nine hub-pair columns |
|:--|:--|
| `0` | `0/1 1/1 1/1 1/1 1/1 0/3 1/1 0/3 1/1` |
| `1` | `1/1 1/1 0/3 1/1 0/1 1/1 0/3 1/1 1/1` |
| `2` | `1/1 0/3 1/1 0/3 1/1 1/1 1/1 1/1 0/1` |
| `01` | `2/1 1/1 1/3 1/1 1/1 0/3 1/3 0/3 2/1` |
| `02` | `1/1 0/3 1/1 0/3 2/1 1/3 1/1 1/3 2/1` |
| `12` | `2/1 1/3 0/3 1/3 2/1 1/1 0/3 1/1 1/1` |
| `012` | `2/1 1/3 1/3 1/3 2/1 1/3 1/3 1/3 2/1` |

| \(S\) | GHM: ordered values in the nine hub-pair columns |
|:--|:--|
| `0` | `0/1 3/1 1/1 3/1 3/1 0/3 1/1 0/3 1/1` |
| `1` | `3/1 3/1 0/3 3/1 2/1 2/1 0/3 2/1 2/1` |
| `2` | `1/1 0/3 1/1 0/3 2/1 2/1 1/1 2/1 1/1` |
| `01` | `4/1 3/1 1/3 3/1 3/1 0/3 1/3 0/3 2/1` |
| `02` | `1/1 0/3 1/1 0/3 3/1 2/3 1/1 2/3 1/1` |
| `12` | `4/1 3/3 0/3 3/3 2/1 2/1 0/3 2/1 2/1` |
| `012` | `4/1 3/3 1/3 3/3 3/1 2/3 1/3 2/3 2/1` |

These are explicit 126 short finite computations, not sampled large-graph simulations. For reproducibility, `verify_book.py` implements exactly the reduced transition expression, checks every table entry and separately simulates the actual graph. In particular the table proves the upper bounds on \(T\) and the exclusion of all other periods for *all* \(m\).

**3. Count initial page assignments.** For a specified original support with cardinality \(k\in\{1,2,3\}\), the number of labelled assignments is the number of onto functions from an \(m\)-element set onto that support:
\[
W_k(m)=\sum_{j=0}^k(-1)^{k-j}\binom kjj^m.
\]
Explicitly \(W_1=1\), \(W_2=2^m-2\), and \(W_3=3^m-3\cdot2^m+3\). In CCA, the 63-cell table has support-size one class multiplicities \(3,6,18\) for \((0,1),(0,3),(1,1)\); size-two multiplicities \(6,9,6,6\) for \((0,3),(1,1),(1,3),(2,1)\); and size-three multiplicities \(6,3\) for \((1,3),(2,1)\). In GHM, the corresponding support-size one multiplicities are \(1,6,7,7,6\) for \((0,1),(0,3),(1,1),(2,1),(3,1)\); size-two multiplicities are \(6,4,2,5,2,4,2,2\) for \((0,3),(1,1),(1,3),(2,1),(2,3),(3,1),(3,3),(4,1)\); and size-three multiplicities are \(2,1,2,1,2,1\) for \((1,3),(2,1),(2,3),(3,1),(3,3),(4,1)\). Multiplication by \(W_k(m)\) and collection of terms gives *every* formula in the finding table. Summing the entries in each model gives \(9\cdot3^m\), as required.

**4. Identify the shared recurrent skeleton.** The `0/3` cells coincide in both finite tables. More explicitly, a primitive three-cycle state occurs exactly when the hubs have the two distinct colors \(c+1\) and \(c+2\), in either order, and all pages have colors in \(\{c,c+1\}\) with **at least one page of color \(c\)**, for some \(c\in\{0,1,2\}\). Under either rule each vertex then advances its color by one at every update. There are \(3\cdot2\cdot(2^m-1)=6(2^m-1)\) such states and each primitive orbit contains three, giving \(2(2^m-1)\) primitive three-cycle orbits. The `0/1` cells give the stated fixed states.

**5. Equidistribution and limits.** The GHM table contains exactly two size-two and two size-three original-support classes for *each* of \((T,P)=(1,3),(2,3),(3,3)\). Their common weighted count is \(2W_2(m)+2W_3(m)=2(3^m-2^{m+1}+1)=q\). For \(m\ge2\) this is positive, proving the exact three-way conditional uniformity. The CCA table has no nonperiodic three-cycle basins beyond \(T=1\). The shared three-cycle basin is \(6(2^m-1)+3q=6(3^m-2^m)\). Dividing all counts by \(3^{m+2}\) and letting \(m\to\infty\) yields the stated limiting distributions.

## Verification

Run `python3 verify_book.py` (Python standard library only). It checks the 126 support/hub/model table entries via the explicit reduced transition, checks their weighted closed-form sums for page counts one through twelve (the underlying expressions all belong to the span of \(1,2^m,3^m\), so this is an additional consistency check rather than the proof), and independently simulates explicit graph adjacency for every labelled coloring for page counts one through eight, checking each \((T,P)\), identical recurrent state sets and identical recurrent transitions. The finite reduction and its complete table, not bounded brute force over graph sizes, justify the all-\(m\) result. The run records `BOOK_CCA_GHM_VERIFY_OK`.

## Relationship to prior work

Gravner, Lyu and Sivakoff (arXiv:1610.07320, first posted 2016-10-24) establish on every finite connected graph a criterion for oscillation using the nonzero circulation of an initial three-coloring, and a general diameter bound for synchronization (their Theorem 3). That framework already governs the existence of oscillation and should not be mistaken for a new criterion here. It does not state the complete book-graph first-periodic-entry shell census, the exact equidistribution of the three GHM oscillatory transient shells, or the shared explicit recurrent-orbit census. The conditional three-way **first-periodic-entry** equality is the main additional finding.

Matamala and Goles (LATIN 1995) study cyclic automata networks on finite graphs and give structural bounds on transient times and periods; their available bibliographic record and abstract do not resolve the present exact comparison. Its full text could not be inspected, and no conclusion of noncoverage is drawn from that limited access. The finite graph here is a family of triangles sharing an **edge**; it is not the friendship-graph family of triangles sharing one **vertex**. Corresponding graph-specific stopping-time formulas for one family do not imply the present ones for the other.

## Limitations

This theorem applies only to synchronous, unthresholded, three-state rules on the specified labelled book graphs. Its exact claims concern first-periodic-entry counts, primitive three-cycle orbits, and their basins; they do not extend to other color counts, nonuniform thresholds, or arbitrary graphs. The old Matamala–Goles article remains a historical-coverage risk because a complete lawful copy was not accessible. The present verification is a fully explicit finite-state mathematical reduction and same-source executable replay, not independent external validation.

## References

1. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public version 2016-10-24, https://arxiv.org/abs/1610.07320, especially Theorem 3 and discussion of finite connected graphs.
2. M. Matamala and E. Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN '95, Lecture Notes in Computer Science 911 (1995), pp. 398–410, DOI 10.1007/3-540-59175-3_105. Full text not inspected.
