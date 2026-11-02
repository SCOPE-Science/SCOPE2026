# Exact Ising field thresholds and coexistence counts on the snub cubical graph

## Finding
Let \(G\) be the 24-vertex, 60-edge graph of the snub cube. In the classical nearest-neighbor antiferromagnetic Ising model with \(\sigma_v\in\{-1,1\}\), \(J>0\), and real magnetic field \(h\), define
\[
H(\sigma)=J\sum_{uv\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,\qquad M(\sigma)=\sum_v\sigma_v.
\]
For \(h\ge0\), the complete zero-temperature magnetization phase diagram, including the number of distinct labelled spin configurations attaining the ground-state energy, is:

| Field region | Ground-state magnetizations \(M\) | Total ground-state count |
|---|---|---:|
| \(0\le h<J\) | \(0\) | 18 |
| \(h=J\) | \(0,2,4,6,8\) | 201 |
| \(J<h<5J\) | \(8\) | 3 |
| \(h=5J\) | \(8,10,12,14,16,18,20,22,24\) | 5302 |
| \(h>5J\) | \(24\) | 1 |

Negative-field results follow exactly by reversing all spins. In particular, the only positive field transitions are \(h=J\) and \(h=5J\), and the stable intermediate plateau has one-third saturation magnetization. The microcanonical maximum-cut profile supplies the stronger complete sector-level statement: for every integer \(0\le k\le24\), putting \(r=\min\{k,24-k\}\),
\[
B_k=\max_{|S|=k}|\delta(S)|=\min\{5r,r+32\}.
\]
Its full exact multiplicity distribution is given below. The already-known snub-cubical independence-set counts imply the high-field \(5302\) coexistence multiplicity; that particular number and the \(r\le8\) branch are **not** asserted to be novel. The assessed additional result is the full magnetization/constrained-cut classification, especially the lower critical-field coexistence of 201 configurations.

## Assumptions and scope
The graph is the simple undirected edge graph of either chiral snub cube, with 24 vertices, 60 edges, degree five at every vertex, and 32 triangular faces. All 60 bonds have the same antiferromagnetic coupling \(J>0\); every site experiences the same field \(h\). Spin configurations are labelled, not quotiented by graph automorphisms. No thermodynamic limit, continuous spins, or temperature-dependent assertion is made. The exact edge list, in the reproducible coordinate order below, is included in `snub_edges.txt`.

Let \(t>1\) be the real root of \(t^3-t^2-t-1=0\). Coordinates are signed even-parity permutations of \((1,t^{-1},t)\), retaining the sign triples whose positive-sign count has the same parity as the coordinate permutation. Order the resulting 24 vertices by their increasing real coordinate triples. The squared edge length is exactly \(2+4t-2t^2\). The verification file `verify_geometry.py` constructs these points in the cubic integer ring and exactly reconstructs the edge list. The choice of handedness changes only vertex labels, not the results.

## Proof
**Sector reduction.** For a configuration let \(S=\{v:\sigma_v=+1\}\), with \(|S|=k\), and let \(\delta(S)\) be its edge boundary. Since an antialigned edge contributes \(-J\) and an aligned edge contributes \(+J\), the energy of this configuration is exactly
\[
H=J(60-2|\delta(S)|)-h(2k-24).
\]
Thus for fixed \(k\) the minimum exchange energy is \(J(60-2B_k)\), and its degeneracy is the number \(N_k\) of \(k\)-element vertex subsets attaining \(B_k\). Complementation proves \(B_k=B_{24-k}\) and \(N_k=N_{24-k}\).

**Complete finite exhaustive certificate.** The labelled graph has exactly \(2^{24}=16,777,216\) subsets. Both following exact recurrences independently enumerate all of them with integer arithmetic. First use Gray order \(S_z\), where consecutive subsets differ at the unique bit given by the least significant set bit of the counter \(z\). If the toggled vertex has \(u\) neighbors currently in \(S\), the cut changes by \(5-2u\) for insertion and \(2u-5\) for deletion. Starting from \(S=\varnothing\), record maximum cut and count at every subset cardinality. Second, enumerate subsets by increasing binary mask: removing its least-numbered vertex \(v\) gives \(T\), and
\[
|\delta(T\cup\{v\})|=|\delta(T)|+5-2|N(v)\cap T|.
\]
Each nonempty subset has a unique such predecessor, so the recurrence visits every subset once. The two completely specified methods agree at all 25 cardinalities and yield the following exact values, with the other half fixed by complementation:

| \(k\) | \(B_k\) | \(N_k\) |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 5 | 24 |
| 2 | 10 | 216 |
| 3 | 15 | 912 |
| 4 | 20 | 1854 |
| 5 | 25 | 1680 |
| 6 | 30 | 564 |
| 7 | 35 | 48 |
| 8 | 40 | 3 |
| 9 | 41 | 24 |
| 10 | 42 | 84 |
| 11 | 43 | 72 |
| 12 | 44 | 18 |

The file `verify_field_census.py` executes both recurrences and compares every \(B_k\) and \(N_k\) exactly. This exhaustive finite proof covers all configurations of this fixed finite graph; it is not statistical sampling or an inference to larger graphs. The procedure has no unverified mathematical subroutine: each operation is an integer bit count and each subset occurs in both complete traversals. Geometry is independently checked by `verify_geometry.py` using exact ring equality; all 60 edges are listed.

**Taking the lower envelope.** If \(h>0\), global spin reversal strictly favors nonnegative \(M\). Let \(j=24-k\), the number of down spins, so \(0\le j\le12\) suffices. The verified table states
\[
B_j=\begin{cases}5j,&0\le j\le8,\\j+32,&8\le j\le12.\end{cases}
\]
In the first interval the sector energy is \(60J-24h+j(2h-10J)\); in the second it is \(-4J-24h+j(2h-2J)\). These are affine in \(j\) and are minimized at endpoints except when the coefficient vanishes. Consequently the only open-field minimizers are \(j=12\) for \(0<h<J\), \(j=8\) for \(J<h<5J\), and \(j=0\) for \(h>5J\). At \(h=J\), every \(j=8,9,10,11,12\) minimizes and the multiplicity is \(3+24+84+72+18=201\). At \(h=5J\), every \(j=0,1,\ldots,8\) minimizes and the multiplicity is \(1+24+216+912+1854+1680+564+48+3=5302\). The strict inequalities at other field values follow from the respective slopes. At \(h=0\), the only minimizer is \(j=12\) (equivalently \(k=12\)), with 18 states. This proves the stated diagram and degeneracies.

## Verification
Run the following two standard-library-only commands from the directory containing these files:

```text
python3 verify_geometry.py snub_edges.txt
python3 verify_field_census.py snub_edges.txt
```

The geometry checker computes exact cubic-ring squared distances, verifies each of the 60 edges against the embedded list, all 24 degrees, and 32 triangles. The census checker traverses \(2^{24}\) configurations twice using distinct recurrences; tests the complete symmetric sector table; checks rational field crossings; and verifies the coexistence counts. `verification_output.txt` records successful execution from the distributed source files. No floating-point calculation is used to decide edges, cuts, field transitions, or multiplicities. The 70-digit decimal approximation in the geometry checker is used only to establish a wide separation of nonedge squared distances.

## Relationship to prior work
Zhuang and Lannert (arXiv:1107.2893v1, 14 July 2011) studied this same 24-site snub-cube network as a small-network approximation to triangular-lattice Ising physics, including its zero-field specific heat. The retrievable indexed portion of their treatment describes its 60 bonds and specific-heat comparison, not the field-dependent exact cut profile, field thresholds, or critical multiplicities. The full primary PDF could not be retrieved in this examination, so coverage hidden elsewhere in that article remains a specifically acknowledged risk.

Strečka, Karľová and Madaras (arXiv:1502.04449v1, 16 February 2015) gave a graph-theoretic treatment of Ising magnetization plateaux on the five regular Platonic polyhedra. The general relation between Ising energy and graph cuts is established antecedent methodology, not new here; the snub cube is an Archimedean, non-Platonic graph and is not among their five classified graphs. Žukovič and Bobák (arXiv:1310.3298v1) examined frustrated finite triangular-lattice spin clusters with different graph geometries.

A previously published exact independence-complex classification of the snub cubical graph gives the independence-set counts \((24,216,912,1854,1680,564,48,3)\) for positive subset sizes \(1\) through \(8\). Those counts imply both \(B_j=5j\) for \(0\le j\le8\) and the high-field critical multiplicity \(5302\); neither inference is a novelty claim. They do **not** determine the fixed-cardinality maximum cuts and minimizer multiplicities for \(j=9,10,11,12\), the lower threshold \(h=J\), the 201-fold coexistence, or the complete lower envelope. The new finite magnetic classification consists of these additional facts together with their precise integration into the all-field phase diagram.

## Limitations
This is a complete exact statement for the uniform 24-site snub cubical Ising model, not an all-polyhedra theorem. The 5302 high-field count and independence-set profile are known from earlier public work; their reproduction here is for a complete phase diagram rather than claimed novelty. The field transition data do not establish finite-temperature thermodynamics, magnetocaloric rates, quantum-spin behavior, or experimental realization. Full-text access to one especially relevant primary article was restricted, and independent scientific review has not occurred; historical-priority risk accordingly remains.

## References
1. B. Zhuang and C. Lannert, *Small-Network Approximations for Geometrically Frustrated Ising Systems*, arXiv:1107.2893v1 (2011), https://arxiv.org/abs/1107.2893; Phys. Rev. E 85, 031107 (2012).
2. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449v1 (2015), https://arxiv.org/abs/1502.04449.
3. M. Žukovič and A. Bobák, *Entropy of spin clusters with frustrated geometry*, arXiv:1310.3298v1 (2013), https://arxiv.org/abs/1310.3298.
4. *The snub cubical independence complex is a wedge of twenty-six four-spheres*, published 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-snub-cubical-independence-complex-is-a-wedge-of-twenty-six-f--d067ae207579.
5. *Snub Cube*, Cartesian coordinate construction, https://en.wikipedia.org/wiki/Snub_cube.
