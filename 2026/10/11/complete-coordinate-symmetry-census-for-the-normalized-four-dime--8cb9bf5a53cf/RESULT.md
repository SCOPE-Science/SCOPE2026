# Complete coordinate-symmetry census for the normalized four-dimensional chair search

## Finding

Kamenetsky's four-dimensional chair search assigns a coordinate permutation to each outer child of the rep-\(16\) chair substitution, with parity fixed by the corner parity. The accompanying symmetry search fixes one outer reference frame as an additional normalization.

Let
\[
U_4=\{0,1\}^4\setminus\{(1,1,1,1)\}.
\]
A **normalized homochiral outer-frame assignment** is a family
\[
\pi=(\pi_v)_{v\in U_4},
\qquad
\pi_v\in S_4,
\]
such that
\[
\pi_{(0,0,0,0)}=\operatorname{id}
\]
and, for every other \(v\in U_4\),
\[
\operatorname{sgn}(\pi_v)=(-1)^{|v|}.
\]
There are exactly \(12\) permutations of either parity, so the normalized search space has
\[
\boxed{
|\mathcal A|=12^{14}=1{,}283{,}918{,}464{,}548{,}864.
}
\]

Coordinate relabeling acts by
\[
(\sigma\cdot\pi)_{\sigma v}
=
\sigma\pi_v\sigma^{-1},
\qquad
\sigma\in S_4.
\]
The complete orbit count is
\[
\boxed{
|\mathcal A/S_4|
=
53{,}496{,}608{,}995{,}008.
}
\]

Exactly
\[
\boxed{
151{,}266{,}816
}
\]
normalized assignments have nontrivial coordinate stabilizer. They form exactly
\[
\boxed{
12{,}608{,}256
}
\]
coordinate-relabeling orbits.

The exact nontrivial stabilizer census is:

| Exact stabilizer type | assignments | \(S_4\)-orbits |
| --- | ---: | ---: |
| transposition \(C_2\) | \(7{,}958{,}016\) | \(663{,}168\) |
| double-transposition \(C_2\) | \(143{,}276{,}736\) | \(11{,}939{,}728\) |
| split \(V_4\) | \(2{,}208\) | \(368\) |
| cyclic \(C_4\) | \(20{,}640\) | \(3{,}440\) |
| normal \(V_4\) | \(9{,}120\) | \(1{,}520\) |
| dihedral \(D_8\) | \(96\) | \(32\) |

No normalized homochiral assignment is invariant under a subgroup containing a three-cycle. Hence exact stabilizers of types \(C_3\), \(S_3\), \(A_4\), and \(S_4\) do not occur.

For direct comparison with the structured searches reported in the source, the fixed-assignment counts are
\[
32,\qquad 768,\qquad 6912
\]
for the order-eight dihedral, split-Klein, and cyclic-order-four subgroup types used there. Thus the source's three nontrivial structured-family sizes are recovered as entries of one complete subgroup calculation.

## Assumptions and scope

The result concerns the **normalized symmetry-search space used by the source's `symsearch4.py` program**, not the entire unnormalized \(12^{15}\) search space stated in the open problem. In particular, the outer block \(v=(0,0,0,0)\) is fixed to the identity in this normalized search. The central translated child is also fixed as in the paper, but it is a different child from that outer block.

The result counts frame assignments and their coordinate symmetries. It does **not** assert that any counted assignment passes coarsening closure, tightness, or the enclosure test, and therefore does not solve the four-dimensional monotile problem.

The notation \(D_8\) means the group of order \(8\). The source's table uses its own dihedral notation; the numerical family size is compared rather than relying on notation conventions.

## Proof

For a subgroup
\[
\Gamma\le S_4,
\]
consider assignments fixed by every \(\gamma\in\Gamma\).

The group \(\Gamma\) acts on \(U_4\) by permuting coordinates. Fix one representative \(v\) from each \(\Gamma\)-orbit. Once \(\pi_v\) is chosen, equivariance forces
\[
\pi_{\gamma v}
=
\gamma\pi_v\gamma^{-1}.
\]
This is well-defined precisely when \(\pi_v\) commutes with every element of the stabilizer
\[
\Gamma_v
=
\{\gamma\in\Gamma:\gamma v=v\}.
\]
Therefore the number of \(\Gamma\)-fixed normalized assignments is
\[
\boxed{
F(\Gamma)
=
\prod_{\substack{[v]\in U_4/\Gamma\\v\ne(0,0,0,0)}}
\#\left\{
p\in S_4:
\operatorname{sgn}(p)=(-1)^{|v|},
\quad
pg=gp\ \text{for all }g\in\Gamma_v
\right\}.
}
\]
The normalized zero block contributes the factor \(1\).

This formula immediately explains the three-cycle obstruction. Let
\[
\tau=(123)
\]
after relabeling coordinates, so coordinate \(4\) is fixed. The weight-one block
\[
v=(0,0,0,1)
\]
is fixed by \(\tau\). Homochirality requires \(\pi_v\) to be odd. But the centralizer of a three-cycle in \(S_4\) is
\[
C_{S_4}(\tau)=\langle\tau\rangle,
\]
whose three elements are all even. Hence the corresponding factor in \(F(\langle\tau\rangle)\) is zero. Any larger subgroup containing a three-cycle has an even smaller fixed set, so it also fixes no normalized homochiral assignment.

Evaluating the displayed product on the \(30\) subgroups of \(S_4\) gives the following fixed-family table. Conjugate subgroups have the same value.

| subgroup type | number of such subgroups | \(F(\Gamma)\) |
| --- | ---: | ---: |
| trivial | \(1\) | \(1{,}283{,}918{,}464{,}548{,}864\) |
| transposition \(C_2\) | \(6\) | \(1{,}327{,}104\) |
| double-transposition \(C_2\) | \(3\) | \(47{,}775{,}744\) |
| \(C_3\) | \(4\) | \(0\) |
| split \(V_4\) | \(3\) | \(768\) |
| \(C_4\) | \(3\) | \(6{,}912\) |
| normal \(V_4\) | \(1\) | \(9{,}216\) |
| \(S_3\) | \(4\) | \(0\) |
| \(D_8\) | \(3\) | \(32\) |
| \(A_4\) | \(1\) | \(0\) |
| \(S_4\) | \(1\) | \(0\) |

Burnside's lemma now needs only element-fixed counts. The five conjugacy classes of elements of \(S_4\) have sizes
\[
1,\ 6,\ 3,\ 8,\ 6
\]
for the identity, transpositions, double transpositions, three-cycles, and four-cycles. Therefore
\[
|\mathcal A/S_4|
=
\frac{
12^{14}
+
6(1{,}327{,}104)
+
3(47{,}775{,}744)
+
8(0)
+
6(6{,}912)
}{24},
\]
which simplifies to
\[
53{,}496{,}608{,}995{,}008.
\]

To obtain exact stabilizers rather than merely fixed sets, perform subgroup-lattice Möbius subtraction. For each concrete subgroup \(H\le S_4\), in descending order of group size, define
\[
E(H)
=
F(H)
-
\sum_{K>H}E(K).
\]
Then \(E(H)\) is exactly the number of assignments whose stabilizer equals \(H\). Aggregating over conjugate subgroups gives the assignment counts in the Finding table.

An orbit with exact stabilizer \(H\) has size
\[
\frac{24}{|H|}.
\]
Dividing each aggregate assignment count by that orbit size gives the corresponding orbit counts. The trivial-stabilizer stratum contains
\[
1{,}283{,}918{,}313{,}282{,}048
\]
assignments and
\[
53{,}496{,}596{,}386{,}752
\]
free orbits. Subtracting these from the totals gives the stated nontrivial-symmetry totals.

## Verification

The bundled checker reconstructs \(S_4\) from its \(24\) permutations, generates all \(30\) subgroups without a stored subgroup list, computes every orbit and stabilizer on \(U_4\), evaluates the centralizer-parity product \(F(\Gamma)\), and performs subgroup-lattice subtraction.

It independently verifies:

\[
|\mathcal A|=12^{14},
\]
the complete fixed-family table above,
\[
|\mathcal A/S_4|=53{,}496{,}608{,}995{,}008,
\]
the exact stabilizer assignment and orbit census, and the vanishing of every fixed set containing a three-cycle.

The source's repository file `symsearch4.py` was inspected for the normalization, parity convention, coordinate action, conjugation rule, stabilizer-centralizer restriction, and the structured-family enumeration. The three reported structured-family sizes
\[
32,\ 768,\ 6912
\]
are reproduced exactly.

The checker does not run the expensive coarsening-closure test. That test is outside the claim.

## Relationship to prior work

Kamenetsky formulates the four-dimensional problem as a finite search over homochiral frame assignments. The paper reports several structured symmetry families, all failing the first self-similarity test, and explicitly identifies further symmetry-based enumeration over subgroups of \(S_4\) as a natural search reduction. The accompanying `symsearch4.py` implements the fixed-family construction for a supplied subgroup.

The source does not give the complete subgroup table, a Burnside orbit count, the exact stabilizer census, or the three-cycle impossibility criterion. Those are the statements proved here.

A separate result on the three-dimensional Chair44 hierarchy constrains Euclidean symmetries through its \(2\)-adic phase. That concerns symmetries of completed tilings, whereas the present theorem counts coordinate-conjugation symmetries of candidate four-dimensional substitution frame assignments. Neither statement implies the other.

Targeted searches by the source identifier, the frame-assignment terminology, the \(S_4\) conjugation action, and the three structured-family sizes found no published statement of the complete census.

## Limitations

This theorem is a symmetry census and a search-pruning result, not a construction of a four-dimensional aperiodic monotile.

The normalization
\[
\pi_{(0,0,0,0)}=\operatorname{id}
\]
is the one used by the source's symmetry-search program. No claim is made here that this normalized slice alone is sufficient to decide the full unnormalized \(12^{15}\) open problem.

The theorem does not test the \(12{,}608{,}256\) symmetric orbits for coarsening closure. It only proves exactly how many such inequivalent candidate assignments exist and which stabilizer types are possible.

## References

1. Dmitry Kamenetsky, *Towards Strongly Aperiodic Monotiles in Higher Dimensions*, arXiv:2610.00916v1, 1 October 2026.
2. Dmitry Kamenetsky, `symsearch4.py`, repository `dimkadimon/Monotile-RN`, accompanying arXiv:2610.00916.
3. Result on the \(2\)-adic symmetry-phase dichotomy for Chair44 tilings, published September 2026; used only as a non-covering comparison for completed-tiling symmetry.
