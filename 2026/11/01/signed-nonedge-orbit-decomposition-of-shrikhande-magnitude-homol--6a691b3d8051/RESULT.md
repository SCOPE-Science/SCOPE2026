# Signed nonedge-orbit decomposition of Shrikhande magnitude homology

## Finding

For the Shrikhande graph \(X\), the full automorphism group \(G=\operatorname{Aut}(X)\) has order \(192\). Its rational magnitude homology in bidegree \((3,4)\), with the natural automorphism action, admits the following **explicit isomorphism of rational representations**:

\[
\operatorname{MH}_{3,4}(X;\mathbb Q)
\cong \operatorname{Ind}_{H_{48}}^{G}\varepsilon_{48}
\oplus\operatorname{Ind}_{H_{96}}^{G}\varepsilon_{96}.
\]

Here \(H_{48}\) and \(H_{96}\) are stabilizers of ordered nonadjacent vertex pairs in the distinct orbits of sizes \(48\) and \(96\), respectively. They have orders \(4\) and \(2\), and \(\varepsilon_{48}\) and \(\varepsilon_{96}\) are the explicitly specified **nontrivial** one-dimensional rational sign representations below.

The complete character of the \(192\)-element group takes value \(144\) at the identity, value \(4\) at exactly \(12\) elements, value \(-12\) at exactly \(16\) elements, and value \(0\) at the other \(163\) elements. Consequently,

\[
\operatorname{MH}_{3,4}(X;\mathbb Q)^G=0.
\]

The total rational dimension \(144\) is **previously published**, not part of the new claim. The result is the induced-module identification, complete automorphism character and its symmetry-fixed consequence.

## Assumptions and scope

Use the standard Cayley realization \(V=(\mathbb Z/4\mathbb Z)^2\) with edges between \(x\) and \(y\) exactly when \(y-x\) belongs to
\[
S=\{\pm(1,0),\pm(0,1),\pm(1,1)\}.
\]

Graph distance is shortest-path distance. The magnitude chain group \(\operatorname{MC}_{k,\ell}(X;\mathbb Q)\) has as basis the ordered \((k+1)\)-tuples \((v_0,\ldots,v_k)\) with consecutive vertices different and total consecutive distance \(\sum_i d(v_{i-1},v_i)=\ell\). Its differential is the alternating sum of deletion of interior \(v_i\), with coefficient \((-1)^i\), **only if** the deletion preserves that total distance. This is the standard magnitude-homology convention of Hepworth--Willerton. Automorphisms act by relabeling ordered tuples, without an extra orientation sign.

The affine group acts by \(v\mapsto Mv+t\) with \(t\in V\) and \(M\in\operatorname{GL}_2(\mathbb Z/4\mathbb Z)\) preserving \(S\). Exactly \(12\) matrices do so, producing \(192\) automorphisms. These are all graph automorphisms: the six neighbors of the origin induce a hexagon, so its point stabilizer injects into the order-\(12\) dihedral group. The remaining nine vertices are distinguished by their pairwise distinct two-element intersections of their neighborhoods with that hexagon.

Use the ordered pair representatives \(u_{48}=((0,0),(0,2))\) and \(u_{96}=((0,0),(1,2))\). Matrix entries below are listed in row-major order and all stabilizer transformations have translation \((0,0)\). The stabilizer of \(u_{48}\) consists of the matrices

| Matrix \((a,b,c,d)\) | \(\varepsilon_{48}\) |
|---|---:|
| \((1,0,0,1)\) | \(+1\) |
| \((1,0,1,3)\) | \(-1\) |
| \((3,0,0,3)\) | \(-1\) |
| \((3,0,3,1)\) | \(+1\) |

The stabilizer of \(u_{96}\) consists of \((1,0,0,1)\) of sign \(+1\) and \((3,1,0,1)\) of sign \(-1\). Both sign assignments are group homomorphisms into \(\{\pm1\}\).

## Proof

**Endpoint decomposition.** The magnitude boundary deletes only interior vertices, so the ordered endpoints of every chain are fixed by the boundary. The complex decomposes as a direct sum of endpoint-pair subcomplexes. The full affine group has exactly four ordered-endpoint orbits, represented by \((0,0)\), \((0,1)\), \((0,2)\), \((0,6)\) under the indexing \(i=4x+y\) for \((x,y)\in V\). Their orbit sizes are \(16\), \(96\), \(48\), \(96\).

**Exact ranks.** In each representative endpoint subcomplex at total length four, enumerate all chain generators in degrees two, three and four; take signed boundaries and perform Gaussian elimination **over \(\mathbb Q\)**. The resulting exact data are:

| Indexed terminal vertex | Orbit size | \(\dim C_2\) | \(\dim C_3\) | \(\dim C_4\) | \(\operatorname{rank}\partial_3\) | \(\operatorname{rank}\partial_4\) | \(\dim H_3\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 16 | 9 | 54 | 96 | 9 | 45 | 0 |
| 1 | 96 | 6 | 54 | 80 | 6 | 48 | 0 |
| 2 | 48 | 4 | 66 | 80 | 4 | 61 | 1 |
| 6 | 96 | 4 | 66 | 80 | 4 | 61 | 1 |

The equality \(\partial_3\partial_4=0\) is checked on every four-chain. Thus the only nonzero endpoint summands are one-dimensional and occur at precisely the two ordered nonedge orbits. This proves the dimension \(48+96=144\).

**Local orientation signs.** In the orbit-\(48\) representative, the tuple of indexed vertices \((0,4,13,2)\) is a closed nonboundary three-chain: its two potentially nonzero deletion terms fail the distance-equality condition, and adjoining its coefficient vector to the image of \(\partial_4\) increases the exact rational rank from \(61\) to \(62\). The corresponding generator in orbit \(96\) is \((0,3,10,6)\), with the same verified properties. For each stabilizer element, transform the generator and compare it with its positive and negative copies modulo the image of \(\partial_4\), by rational row reduction. This gives exactly the two sign tables in the preceding section.

**Induction and full character.** Since the endpoint decomposition is equivariant, a one-dimensional homology fiber in a transitive orbit induces its stabilizer character to the full group. This gives the stated two induced representations. For every \(g\in G\), the character is obtained by summing the local signs over the ordered nonedge pairs fixed by \(g\), with conjugation by chosen transporters. Exhaustion of all \(192\) elements gives the stated character-value multiplicities; `CHARACTER.csv` lists all \(192\) affine matrices, translations and traces in a fixed reproducible ordering. Its average is \((144+12\cdot4-16\cdot12)/192=0\), proving that the rational invariant subspace vanishes. Equivalently, Frobenius reciprocity gives the same conclusion because both stabilizer sign representations are nontrivial.

## Verification

The accompanying standard-library-only `VERIFY.py` reconstructs the graph and the full automorphism group from integer coordinates, enumerates every chain in the four representative endpoint fibers, computes both boundary ranks over exact rational arithmetic, checks the boundary-square identity, checks that both specified cycles are nonboundaries, determines every stabilizer sign, and checks all \(192\) character-table records. Execute `python3 VERIFY.py .` from the directory containing the files. The recorded successful output is in `verification_output.txt` and ends with `VERIFY_OK`. The four representative fibers exhaust all \(256\) ordered endpoint pairs by verified group orbits, so no other fibers are silently omitted.

## Relationship to prior work

Hepworth--Willerton introduced this magnitude-homology chain theory in 2015 [1]. Gu's Proposition A.2 and Table 2 in [2] **already give the total Shrikhande rank \(144\)** in bidegree \((3,4)\) and distinguish it from the vanishing corresponding rank of the \(4\times4\) rook graph; those facts are not new here. The accepted claim instead identifies the exact full rational \(192\)-automorphism module, including the two nontrivial stabilizer characters and the vanishing fixed subspace. The graph's automorphism order and its two nonedge pair orbits are independently recorded in [3,4] but do not determine the action on homology. No general theorem in those sources directly supplies the nontrivial signs.

## Limitations

Only rational magnitude homology in the indicated bidegree is classified as a representation. This does **not** establish its integral lattice, torsion, other bidegrees, equivariant chain-homotopy type, or representation-theoretic irreducible decomposition. The character distribution does not distinguish conjugacy classes by itself, but the attached table gives the trace of **each** group element. Publication-priority verification is based on the inspected and indexed sources, not an exhaustive guarantee against unindexed equivalent work. No independent mathematical validation has been carried out.

## References

[1] R. Hepworth and S. Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125, first public 15 May 2015, https://arxiv.org/abs/1505.04125.

[2] Y. Gu, *Graph magnitude homology via algebraic Morse theory*, arXiv:1809.07240, first public 19 September 2018, Appendix A, Proposition A.2 and Table 2, https://arxiv.org/abs/1809.07240.

[3] P. J. Cameron, A. Lakshmanan S., and A. Vijayakumar, *The Shrikhande Graph*, Cambridge University Press, 2026, Chapter 5, *Further Properties*, https://doi.org/10.1017/9781009709118.010.

[4] A. E. Brouwer, *Shrikhande graph*, graph record mirrored at https://jaanos.github.io/tables/graphs/Shrikhande.html.
