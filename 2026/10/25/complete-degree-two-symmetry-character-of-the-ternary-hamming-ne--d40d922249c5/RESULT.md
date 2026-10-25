# Complete degree-two symmetry character of the ternary Hamming neighborhood complex

## Finding

Let \(G=H(3,3)=K_3\mathbin{\square}K_3\mathbin{\square}K_3\), on \(V=\{0,1,2\}^3\), with distinct vertices adjacent precisely when they differ in exactly one coordinate. Let \(K=\mathcal N(G)\) be the **open** Lovász neighborhood complex: a nonempty subset of \(V\) is a face if all its vertices have a common graph neighbor. The natural full graph-automorphism group \(W=S_3\wr S_3=(S_3)^3\rtimes S_3\), of order \(1296\), acts simplicially on \(K\).

**The complete rational character of \(W\) on \(\widetilde H_2(K;\mathbb Q)\) is the 22-class character displayed below.** A group element is written \(g(x)_i=\sigma_i(x_{\rho(i)})\), with \(\rho\in S_3\) and \(\sigma_i\in S_3\). For each cycle of \(\rho\) of length \(h\), label the cycle by the conjugacy type of the ordered product of its \(\sigma_i\): `I` for the identity, `T` for a transposition, and `C` for a three-cycle. A class label is the unordered collection of its colored cycles, such as `1I 2T`. The table records the number of group elements in that class and the traces on degrees one and two. In particular, the degree-two representation has dimension \(56\).

| Colored cycle type | Class size | \(\operatorname{tr}_{H_1}\) | \(\operatorname{tr}_{H_2}\) |
|---|---:|---:|---:|
| `1C 1C 1C` | 8 | 3 | 2 |
| `1C 1C 1I` | 12 | 3 | 2 |
| `1C 1C 1T` | 36 | 1 | 0 |
| `1C 1I 1I` | 6 | 3 | 2 |
| `1C 1I 1T` | 36 | 1 | 0 |
| `1C 1T 1T` | 54 | -1 | -2 |
| `1C 2C` | 72 | 1 | 0 |
| `1C 2I` | 36 | 1 | 0 |
| `1C 2T` | 108 | 1 | 0 |
| `1I 1I 1I` | 1 | 3 | 56 |
| `1I 1I 1T` | 9 | 1 | 0 |
| `1I 1T 1T` | 27 | -1 | 4 |
| `1I 2C` | 36 | 1 | 0 |
| `1I 2I` | 18 | 1 | -18 |
| `1I 2T` | 54 | 1 | 0 |
| `1T 1T 1T` | 27 | -3 | 4 |
| `1T 2C` | 108 | -1 | -2 |
| `1T 2I` | 54 | -1 | -2 |
| `1T 2T` | 162 | -1 | 0 |
| `3C` | 144 | 0 | -1 |
| `3I` | 72 | 0 | 5 |
| `3T` | 216 | 0 | 1 |

There is a particularly compact consequence. For the normal ternary-translation subgroup \(A=(\mathbb Z/3\mathbb Z)^3\), the rational restricted representation is

\[
\widetilde H_2(K;\mathbb Q)\mathord{\downarrow}_A\cong 2\mathbb Q[A]\oplus2\mathbb Q.
\]

The translation character equals \(56\) at the identity and \(2\) at all 26 nonidentity elements. Every nonidentity translation acts without fixed points on the geometric realization. Consequently the quotient by translations has reduced rational Betti numbers \((0,3,4)\) in degrees \((0,1,2)\). The full quotient \(K/W\) is rationally acyclic. These are statements over \(\mathbb Q\), not classifications of the integral homology representations.

## Assumptions and scope

The three coordinate symbols are numbered \(0,1,2\), and a graph vertex \((a,b,c)\) has integer ID \(9a+3b+c\). Every simplex uses the usual increasing-ID orientation. Every occurrence of \(H_j\) in the character table means \(\widetilde H_j(K;\mathbb Q)\). The group acts by independent permutations of the three symbols in each coordinate and permutations of coordinate positions. All 22 colored-cycle classes of this particular finite wreath product are included. No general assertion about \(H(d,q)\) outside \((d,q)=(3,3)\) is made.

## Proof

**Exact simplicial reconstruction and low-dimensional reduction.** Each of the 27 graph vertices has six neighbors. Enumerating all nonempty subsets of the 27 open neighborhoods and deduplicating gives exactly 1404 faces, with face vector

\[
(27,243,540,405,162,27).
\]

Their Euler characteristic is \(54\). An exact exhaustive elementary-collapse procedure repeatedly chooses a codimension-one face with a unique maximal coface, checks that no higher coface contains it, then removes the pair. It makes 486 valid collapses and leaves a two-dimensional complex with vector \((27,189,216)\). A lexicographic spanning tree in the original one-skeleton has 26 edges, leaving 217 non-tree edge coordinates. Taking each of the 540 signed triangular boundaries in these coordinates produces an exact \(217\times540\) integral matrix \(D\). Direct rational nullspace reduction gives \(\dim\ker D^{\mathsf T}=3\), with all gauge-fixed cocycle equations satisfied. Hence \(\widetilde H_1(K;\mathbb Q)\cong\mathbb Q^3\); connectedness and Euler characteristic then imply \(\widetilde H_2(K;\mathbb Q)\cong\mathbb Q^{56}\), with all other reduced rational homology zero. This independently reconstructs the rational homology ranks already available in the literature.

**Degree-one group action.** For a cocycle represented by its 217 non-tree edge values, the pullback under \(g\) is computed on all 243 original edges, and a spanning-tree potential is subtracted to restore the gauge. Exact rational calculations produce a three-dimensional basis in which each independent symbol transposition reverses precisely its own basis vector, each symbol three-cycle is the identity, and a coordinate transposition permutes the corresponding basis vectors. These eight elementary generators generate \(W\). Thus

\[
\operatorname{tr}(g\mid\widetilde H_1(K;\mathbb Q))
=\sum_{i:\rho(i)=i}\operatorname{sgn}(\sigma_i).
\]

This coordinate-orientation behavior is compatible with the already published ground-walk description of Hamming graph fundamental groups. It is an input to determining the new degree-two character, not an independently claimed new homology-rank theorem.

**Full degree-two character.** For each element of \(W\), enumerate all faces \(s\) fixed *setwise* under the vertex permutation. If \(\epsilon_g(s)\) denotes the sign of the induced permutation of its ordered vertices, the unreduced simplicial Lefschetz number is the exact integer

\[
L(g)=\sum_{s\ne\varnothing,\ g(s)=s}(-1)^{\dim s}\epsilon_g(s).
\]

Since only degrees zero, one and two have homology, the Hopf trace formula gives

\[
\operatorname{tr}(g\mid\widetilde H_2)=L(g)-1+
\operatorname{tr}(g\mid\widetilde H_1).
\]

The standalone verifier applies this identity to all 1296 elements without sampling or floating point. It verifies preservation of all 27 neighborhood facets, identifies exactly 22 colored-cycle classes, checks trace constancy inside every class, and reproduces each table entry and class size. In characteristic zero a character determines the rational isomorphism class of this finite-group representation (and every value is integral).

**Translations and quotients.** For \(A\) every nonidentity element cyclically permutes each vertex in orbits of length three. A complete check finds that no nonempty simplex is setwise invariant, so its unreduced Lefschetz number is zero. Translations act trivially on degree one by the above coordinate-orientation description. Therefore their degree-two trace is \(2\). The character \(56\) at identity and \(2\) elsewhere equals \(2\chi_{\mathrm{reg}}+2\chi_{\mathrm{triv}}\), proving the stated \(A\)-module decomposition. Over \(\mathbb Q\), homology of a quotient by a finite simplicial group action identifies with invariants after barycentric subdivision. Averaging all character values gives \(\dim H_1(K;\mathbb Q)^W=\dim H_2(K;\mathbb Q)^W=0\), while averaging over \(A\) gives dimensions three and four. The translation action on \(|K|\) is free, since a fixed point would lie in a setwise invariant simplex.

## Verification

Run `python3 verify.py` with Python 3.10 or later and SymPy 1.14.0. The program reconstructs the original graph and every face, checks each elementary collapse, builds the spanning-tree-gauge cochain matrix and its exact rational nullspace, independently checks the eight group generators on the cohomology basis, and enumerates all 1296 automorphisms with integer signed Lefschetz traces. It asserts all 22 conjugacy-class sizes and both characters, all 27 translation traces, the absence of invariant nonempty simplices for nontrivial translations, and group-fixed dimensions. `character_table.csv` records the same complete character in a machine-readable form; `verify_output.txt` records one successful exact execution. No random sample or numerical floating-point rank is used.

## Relationship to prior work

Kozlov's simple-homotopy result links neighborhood complexes with \(\operatorname{Hom}(K_2,G)\) but does not compute an equivariant character for this graph. Behal and Chih identify the ternary Hamming graph's graph-walk fundamental group as \(\mathbb Z^3\), with coordinate-loop generators; that source already implies the natural degree-one signed coordinate behavior. A previously published exact discrete-Morse analysis of this same neighborhood complex supplies the 1404-face model and nonequivariant \(H_1\) and \(H_2\) ranks, but does not state the 22-class homology character. Those nonequivariant claims are **not** presented here as new. The present result refines them by determining every element's action on degree-two rational homology, including the nonuniform values \(-18\), \(5\), and \(56\), and the complete ternary Fourier restriction. Related Rips and Čech complexes built on the same graph have different simplex definitions and cannot substitute for the open-neighborhood complex.

## Limitations

The result is a finite, exactly reproducible rational-character calculation. It does not determine the integral \(\mathbb Z[W]\)-lattice structure of second homology, its integral torsion in quotient spaces, or the equivariant homotopy type. The degree-one action and nonequivariant Betti numbers are largely entailed by prior structural results; the contribution here is the full degree-two symmetry character and its consequences. Literature searches and inspection of close papers cannot exclude an equivalent unindexed representation calculation. The exact calculation is a proof for this 27-vertex graph only.

## References

1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first submitted 2005-03-28, https://arxiv.org/abs/math/0503613.
2. K. Behal and T. Chih, *Fundamental Groups of Hamming Graphs*, arXiv:2308.02938, first submitted 2023-08-05, https://arxiv.org/html/2308.02938v3.
3. *A perfect discrete-Morse matching for the ternary three-cube neighborhood complex*, published mathematical result and full proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-perfect-discrete-morse-matching-for-the-ternary-three-cube-nei--ae99e924c723.
4. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first submitted 2005-12-04, https://arxiv.org/abs/math/0512077.
