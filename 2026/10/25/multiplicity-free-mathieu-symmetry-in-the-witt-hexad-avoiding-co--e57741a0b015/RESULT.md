# Multiplicity-free Mathieu symmetry in the Witt hexad-avoiding complex

## Finding

Let \(X=\mathbb F_{11}\cup\{\infty\}\), and let \(\mathcal B\) be the \(132\) hexads of the classical Witt Steiner system \(S(5,6,12)\). Define the simplicial complex
\[
K=\{\sigma\subseteq X:\text{no hexad }B\in\mathcal B\text{ is contained in }\sigma\}.
\]
Let \(M_{12}=\operatorname{Aut}(X,\mathcal B)\) act naturally on \(K\). Then
\[
K\simeq\bigvee^{330}S^5,
\qquad
\widetilde H_i(K;\mathbb Z)=
\begin{cases}\mathbb Z^{330},&i=5,\\0,&i\ne5.\end{cases}
\]
More particularly, its complexified rational top homology is the following **multiplicity-free Mathieu representation**:
\[
\widetilde H_5(K;\mathbb Q)\otimes_{\mathbb Q}\mathbb C
\cong V_{55}^{(7)}\oplus V_{99}^{(11)}\oplus V_{176}^{(14)},
\]
where the superscripts identify character-table rows \(\chi_7,\chi_{11},\chi_{14}\) in Vanchinathan–Radha–Das, and the subscripts are the irreducible degrees. In particular,
\[
\widetilde H_5(K;\mathbb Q)^{M_{12}}=0.
\]
There is also an integral, automorphism-equivariant short exact sequence
\[
0\longrightarrow\widetilde H_5(K;\mathbb Z)
\longrightarrow\bigwedge^{6}U
\longrightarrow\mathbb Z_{\mathrm{or}}[\mathcal B]
\longrightarrow0,
\]
where \(U=\ker(\mathbb Z^X\xrightarrow{\mathrm{sum}}\mathbb Z)\), and \(\mathbb Z_{\mathrm{or}}[\mathcal B]\) is the free lattice on oriented hexads; an automorphism preserving a hexad acts on its generator by the sign of the induced six-point permutation.

## Assumptions and scope

All complexes are finite abstract simplicial complexes, and \(\bigvee\) denotes a based wedge up to ordinary homotopy equivalence. The action is the full incidence-preserving Mathieu group in its canonical faithful permutation representation of degree twelve; there is no assumption that a wedge equivalence itself is equivariant. The irreducible decomposition is over \(\mathbb C\), not a claim about separate integral direct summands. The earliest verified public date among directly relevant inspected simplicial-complex sources is 25 November 2004, for Fløystad’s preprint on enriched homology and Alexander duals of Steiner systems. Later sources supply the specific Witt design and the Mathieu character table.

For exact reproduction, identify \(\infty\) with label \(11\), and residues modulo \(11\) with labels \(0,\ldots,10\). Begin with the hexad \(B_0=\{\infty,1,3,4,5,9\}\). Its orbit under the permutations
\[
T(x)=x+1,\quad T(\infty)=\infty;\qquad
S(x)=-x^{-1}\ (x\ne0,\infty),\quad S(0)=\infty,\quad S(\infty)=0
\]
is exactly \(\mathcal B\). Here arithmetic is modulo \(11\). The third permutation, displayed as one-line images of labels \(0,\ldots,11\), is
\[
E=(0,1,2,3,5,9,10,8,6,11,7,4).
\]
The three permutations \(T,S,E\) preserve \(\mathcal B\) and generate its full \(95\,040\)-element automorphism group.

## Proof

**1. The design and matroid.** An exact orbit calculation gives \(|\mathcal B|=132\), and every five-point subset of \(X\) lies in exactly one block. Thus any two distinct blocks intersect in at most four points. Every seven-point set contains *exactly one* hexad: two different contained hexads would intersect in at least five points, while the total number of incidences between blocks and containing seven-sets is
\[
132\binom{6}{1}=792=\binom{12}{7}.
\]
Consequently \(K\) has dimension five. Its five-dimensional facets are precisely the \(\binom{12}{6}-132=792\) nonhexad six-subsets. Every set of size at most five extends to one of these facets, since a five-set lies in only one forbidden six-set among its seven one-point extensions.

These facets satisfy the basis-exchange axiom. Given two allowed six-sets \(A,B\) and \(a\in A\setminus B\), if \(|B\setminus A|=1\), exchanging \(a\) produces \(B\). Otherwise there are at least two possible replacements \(b\in B\setminus A\); at most one exchange \(A-a+b\) can be forbidden, as two forbidden exchanges would be distinct hexads sharing the five-set \(A-a\). Hence \(K\) is the rank-six sparse-paving matroid independence complex with the hexads as circuit-hyperplanes. By the classical lexicographic shellability theorem for matroid complexes (Björner), \(K\) is homotopy equivalent to a wedge of five-spheres. Its face vector in dimensions zero through five is
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,220,495,792,792).
\]
Its reduced Euler characteristic is \(-330\), proving the claimed integral homotopy type and ranks.

**2. The equivariant integral sequence.** Let \(Y\) be the full five-skeleton of the simplex on \(X\). Its five-dimensional oriented chain cycle group is canonically \(\bigwedge^6U\), via the exterior-algebra boundary \(\iota_{\mathrm{sum}}\); since \(Y\) has no six-cells, this is \(H_5(Y;\mathbb Z)\). The pair \((Y,K)\) has precisely one relative five-cell for each hexad and no other relative cells, hence \(H_5(Y,K;\mathbb Z)=\mathbb Z_{\mathrm{or}}[\mathcal B]\). The long exact sequence, together with \(\widetilde H_4(K;\mathbb Z)=0\) from Step 1, gives the displayed short exact sequence. Every identification commutes with the Mathieu group action, including the orientation signs.

**3. The group character.** For a permutation \(g\in M_{12}\), write \(\mathcal C(g)\) for its multiset of cycle lengths in the twelve-point action. Exterior-power traces and the short exact sequence give
\[
\chi_{K}(g)=
[t^6]\frac{\prod_{\ell\in\mathcal C(g)}(1-(-t)^\ell)}{1+t}
-\sum_{\substack{B\in\mathcal B\\gB=B}}\operatorname{sgn}(g|_B).
\]
The sign in the second term uses the ordering on the six vertices of each stabilized block. Enumerating all products of \(T,S,E\) yields \(95\,040\) distinct permutations; all stabilize the \(132\) hexads. The following table records all fourteen distinct cycle structures (the two Mathieu conjugacy classes with cycle type \(1\,11\) have identical value); the middle column is the number of permutations and the last column is \(\chi_K\).

| Twelve-point cycle structure | Count | \(\chi_K\) |
| --- | ---: | ---: |
| \(1^{12}\) | 1 | 330 |
| \(1^4 2^4\) | 495 | 10 |
| \(2^6\) | 396 | -10 |
| \(1^3 3^3\) | 1,760 | -3 |
| \(3^4\) | 2,640 | 3 |
| \(1^4 4^2\) | 2,970 | -2 |
| \(2^2 4^2\) | 2,970 | -2 |
| \(1^2 5^2\) | 9,504 | 0 |
| \(1\,2\,3\,6\) | 15,840 | 1 |
| \(6^2\) | 7,920 | -1 |
| \(1^2 2\,8\) | 11,880 | 0 |
| \(4\,8\) | 11,880 | 0 |
| \(2\,10\) | 9,504 | 0 |
| \(1\,11\) | 17,280 | 0 |

Comparing every value with the published Mathieu character table (Vanchinathan–Radha–Das, Section 3.2, page 8582) identifies exactly the sum of the three irreducible rows \(\chi_7+\chi_{11}+\chi_{14}\), of dimensions \(55+99+176=330\). The character has zero inner product with the trivial character and self-inner product three; in particular the decomposition is multiplicity-free and has no invariant vectors.

## Verification

The companion `verify.py` is a standalone Python 3 script requiring only the standard library. Running `python verify.py` checks: all \(132\) generated hexads and the unique containing-hexad property on each of the \(792\) five-sets; all \(792\) seven-sets; the face vector; the preservation of blocks by \(E\); exact enumeration of the \(95\,040\)-element group; the signed hexad and exterior-power character on every group element; class-size and published character-row comparison; and an independently evaluated signed simplicial Lefschetz character on a representative of every one of the fourteen cycle structures. A successful run prints `VERIFY_OK`; the actual recorded output accompanies the script. Finite exhaustive computations are used only on finite specified sets; matroid shellability and homological consequences are proved by the stated theorems and exact sequence.

## Relationship to prior work

The Witt design, its Mathieu automorphism group, and the matroid-shellability theorem are classical. The existence and symmetry of the design are documented in Huber (2007) and Bierbrauer–Marcugini–Pambianco (2016). The complex here is the **Alexander dual of the simplicial complex generated by the 132 hexads**, since Witt hexads occur in complementary pairs; Fløystad (2004) already treats Alexander duals of Steiner systems within a much broader homological framework. Björner's theorem already implies concentration and torsion-freeness for any such matroid independence complex; the numerical wedge multiplicity follows from elementary face counts. The published Mathieu character table, including the three irreducible rows, is available in Vanchinathan–Radha–Das (2020). The specifically computed homology **representation** and equivariant integral kernel sequence are the additional conclusions here; the latter are not claims of an equivariant wedge splitting. Related Steiner-design constructions, ordinary Mathieu group representations, or general matroid shellability do not by themselves display this three-constituent topological module.

## Limitations

The wedge equivalence is nonequivariant. The complexified top homology is identified by its full character; no integral decomposition into Mathieu irreducible lattices, Steenrod operations, or homotopy-coherent action is claimed. Source searches and inspection cannot rule out an unindexed equivalent computation. The character-table attribution is to a later reference and does not change the first-public-source date of the design.

## References

1. G. Fløystad, *Enriched homology and cohomology modules of simplicial complexes*, arXiv:math/0411570v1 (public 25 November 2004), especially Section 4 on Alexander duals of Steiner systems and simplicial homology. https://arxiv.org/abs/math/0411570
2. M. Huber, *A Census of Highly Symmetric Combinatorial Designs*, arXiv:math/0702872v1 (public 28 February 2007), especially the classification of the Witt \(5\)-\((12,6,1)\) design. https://arxiv.org/html/math/0702872v1
3. J. Bierbrauer, S. Marcugini, and F. Pambianco, *A combinatorial construction of an \(M_{12}\)-invariant code*, arXiv:1606.04857v1 (public 15 June 2016), Section 2. https://arxiv.org/abs/1606.04857
4. A. Björner, *The Homology and Shellability of Matroids and Geometric Lattices*, in *Matroid Applications*, Cambridge University Press (1992), pp. 226–283, Theorem 7.3.4. https://doi.org/10.1017/CBO9780511662041.008
5. P. Vanchinathan, S. Radha, and S. Das, *Dimensional Formulae for the Relative Invariants of Pre-Mathieu and Mathieu Groups*, *Advances in Mathematics: Scientific Journal* **9** (2020), 8575–8585, Table in Section 3.2, p. 8582. https://doi.org/10.37418/amsj.9.10.82
