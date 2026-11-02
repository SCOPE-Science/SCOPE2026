# A sharp two-pebble slack threshold for solvable pebbling transfers on the Heawood graph

## Finding

Let \(H\) be the 14-vertex, 21-edge Levi (point–line incidence) graph of the Fano plane. For a nonnegative integer distribution \(D\) of pebbles on its vertices, let \(D\) be *solvable* when for each of the 14 targets separately there exists a sequence of classical graph-pebbling moves that ends with a pebble at that target. Write \(\mathcal S_t\) for all solvable distributions of total size \(t\).

Two configurations in \(\mathcal S_t\) are **jump-neighbors** if one is obtained from the other by removing one pebble at some vertex and adding one to any *different* vertex; they are **slide-neighbors** when those vertices additionally form an edge of \(H\). A jump or slide is a same-total reconfiguration operation, **not** a classical pebbling move.

There are no solvable distributions of total size at most five. At totals six, seven, and eight, the following are exact:

| Total \(t\) | \(|\mathcal S_t|\) | Jump edges | Jump components (size × number) | Slide edges | Slide components (size × number) |
| ---: | ---: | ---: | --- | ---: | --- |
| 6 | 161 | 42 | 1 × 98; 3 × 21 | 42 | 1 × 98; 3 × 21 |
| 7 | 5,936 | 33,726 | 2,576 × 1; 3,360 × 1 | 11,970 | 24 × 21; 74 × 28; 3,360 × 1 |
| 8 | 71,323 | 1,145,396 | 71,323 × 1 | 314,496 | 71,323 × 1 |

Every solvable six-pebble distribution has a nonzero-entry multiset \((4,2)\) (98 cases), \((4,1,1)\) (42 cases), or \((3,3)\) (21 cases). At seven pebbles, the jump component of size 2,576 consists **exactly** of those distributions having at most two pebbles at every vertex; its complement is the jump component of size 3,360. In particular, unrestricted unit jumps do not cross the capacity-two barrier at that total. Both graphs first become connected at total eight, **two pebbles above the optimal total six**. This is a statement about these first three feasible totals, not about all greater totals.

## Assumptions and scope

The point vertices are \(p_i\) and line vertices are \(\ell_i\), where \(i\in\mathbb Z/7\mathbb Z\), and \(\ell_i\) is adjacent to \(p_i,p_{i+1},p_{i+3}\) (indices modulo seven). This is the Fano plane: every point lies on three lines and any pair of points belongs to precisely one line. A *classical pebbling move* from vertex \(u\) to adjacent vertex \(v\) replaces \(D\) by \(D-2e_u+e_v\), possible only when \(D(u)\ge2\), and lowers total pebbles by one. Solvability is *not simultaneous*: each target can be reached from a fresh copy of the starting distribution.

For transfer graphs, pebbles are indistinguishable, configurations are *labelled by the 14 Fano-incidence vertices*, and exchanges are undirected whenever both configurations are in \(\mathcal S_t\). An exchange decreases one coordinate by one and increases another by one, preserving total size and nonnegativity. A self-transfer is excluded. Components and undirected edges are counted exactly once.

## Proof

**1. Exact finite decision procedure.** For a distribution \(D\), define \(R(D)\) as the set of targets that can be occupied after zero or more classical pebbling moves. Let \(\operatorname{supp}(D)\) be the set of vertices initially containing a pebble. Then

\[
R(D)=\operatorname{supp}(D)\cup\bigcup_{\substack{u\sim v\\D(u)\ge2}}R(D-2e_u+e_v).
\]

This identity is exact: every successful sequence either has length zero or begins with one of the listed legal moves. Every nontrivial successor has **strictly one fewer pebble**, so the recurrence terminates with empty moves at distributions containing fewer than two pebbles in every position. Memoization does not alter the result. A distribution is solvable exactly when \(R(D)\) comprises all 14 vertices.

**2. Exhaustion of every candidate.** The programs enumerate all 14-part weak compositions of each total \(t\in\{5,6,7,8\}\), respectively

\[
\binom{t+13}{13}=8{,}568,\ 27{,}132,\ 77{,}520,\ 203{,}490.
\]

Applying the recurrence to every candidate gives respectively 0, 161, 5,936, and 71,323 solvable distributions. If a solvable distribution with total below five existed, adding pebbles at arbitrary vertices would give a solvable five-pebble distribution by monotonicity; therefore the optimal solvable total is six.

**3. Construction of the complete reconfiguration graphs.** Each member of \(\mathcal S_t\) is encoded injectively as a radix-nine integer (all coordinates lie between zero and eight). For each \(D\) and each coordinate \(u\) with \(D(u)>0\), the programs consider every distinct recipient vertex \(v\), check whether \(D-e_u+e_v\) also belongs to \(\mathcal S_t\), and count the pair if its stored index is larger. The slide graph retains only cases with \(u\sim v\). Thus every unordered legal edge is counted once, without omissions. Disjoint-set union yields the component-size multiset; at seven pebbles the programs additionally classify the jump components by whether \(\max_vD(v)\le2\). These finite enumerations give precisely the table and capacity classification above.

**4. Independent reconstruction.** A second complete implementation constructs the Fano plane by taking its seven nonzero points in \(\mathbb F_2^3\) and the seven lines \(\{a,b,a\oplus b\}\) for distinct points \(a,b\). It independently generates all weak compositions, uses the same defining first-move recurrence written separately, constructs jumps and slides directly, and recomputes all component sizes and edge counts. Its outputs match the first. The two concrete constructions realize the same abstract Fano incidence graph, so the shared conclusions are graph-invariant. The first verifier also classifies all six-pebble nonzero-entry profiles; both verifiers establish the size-seven capacity split.

The procedure is exhaustive over **finite** state spaces at each of the displayed totals, and the recurrence proves that these searches decide solvability exactly; hence the outputs establish each finite assertion, including the sharp first connectivity threshold.

## Verification

The included standalone files `verify_primary.cpp` and `verify_secondary.py` require C++17 and Python 3 respectively. In a directory containing both, run:

```sh
g++ -O2 -std=c++17 verify_primary.cpp -o verify_primary
./verify_primary
python3 verify_secondary.py
```

Both check all candidate distributions at totals five through eight, independently verify the graph descriptions and the reachability recurrence, and assert the exact edge and component signatures. The first output ends with `EXHAUSTIVE_PRIMARY_OK`; the second ends with `INDEPENDENT_FANO_CERTIFICATE_OK`. The memorized reachability state count is 319,769 in each implementation. These are executable, finite reproducibility checks, not unperformed external audits.

## Relationship to prior work

Bunde, Chambers, Cranston, Milans and West formalize optimal pebbling and solvable distributions and give general bounds and graph families. Papp studies restricted optimal pebbling (at most two pebbles per vertex) and its computational complexity. The six-pebble optimum is a scalar graph-pebbling fact and is **not** offered as the substantive novelty here. The new claim is the precise *configuration-space classification* at totals six through eight, the size-seven invariant division between capacity-bounded and heavy-pile states, and the sharp threshold for unit-jump and edge-slide connectivity. Neither a scalar optimal pebbling value nor a general existence bound determines these exchange-component counts.

Muntz and coauthors' 2007 article is relevant to diameter-three optimal-pebbling values and might already imply the scalar optimum. Its full text was not inspected; only bibliographic information and an abstract were accessible. The inspected primary text of Bunde et al. and Papp did not state or imply the Heawood exchange classification. This is a best-knowledge overlap comparison, not a priority or uniqueness guarantee.

## Limitations

Only the specified 14-vertex graph and the totals five through eight have been exhaustively classified. Nothing here proves that either exchange graph remains connected for every total \(t\ge9\), or that analogous thresholds hold for arbitrary incidence graphs. The numerical evidence is exhaustive finite computation with supplied source code, not a symbolic family theorem. A publication containing an equivalent enumeration might have escaped the literature searches; the relevant 2007 full text was inaccessible.

## References

1. D. P. Bunde, E. W. Chambers, D. Cranston, K. Milans, D. B. West, *Pebbling and Optimal Pebbling in Graphs*, first public arXiv manuscript 2005-10-28, `arXiv:math/0510621v1`.
2. L. F. Papp, *Restricted optimal pebbling is NP-hard*, `arXiv:2301.09867`.
3. J. Muntz, S. K. Narayan, N. Streib, K. Van Ochten, *Optimal pebbling of graphs*, Discrete Mathematics **307** (2007), DOI `10.1016/j.disc.2006.11.005` (abstract and bibliographic record inspected, not full text).
4. M. Chellali, T. W. Haynes, S. T. Hedetniemi, T. M. Lewis, *Restricted optimal pebbling and domination in graphs*, Discrete Applied Mathematics (2017), DOI `10.1016/j.dam.2016.12.029` (abstract-level comparison).
