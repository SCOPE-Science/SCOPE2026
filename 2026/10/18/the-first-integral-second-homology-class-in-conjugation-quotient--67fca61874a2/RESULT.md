# The first integral second-homology class in conjugation quotients of symmetric-group clique complexes

## Finding

For every integer \(n\ge 1\), let \(X_{S_n}\) be the group clique complex of the symmetric group: its vertices are nonidentity elements of prime-power order, and a nonempty face is a set of pairwise commuting vertices whose orders involve pairwise distinct primes. Such a face is exactly the set of nonidentity prime-primary components of its product. Conjugation acts simplicially. Put \(Y_n=|X_{S_n}|/S_n\), where the quotient is the **geometric** orbit space, not a quotient graph clique complex.

Then the sharp first occurrence of integral second homology is

\[
H_2(Y_n;\mathbb Z)=0\quad(1\le n\le14),\qquad
H_2(Y_{15};\mathbb Z)\cong\mathbb Z.
\]

The generator is represented by a geometrically embedded tetrahedral boundary. Let \(T_{pqr}\) be the oriented orbit two-cell corresponding to a permutation with one \(p\)-cycle, one \(q\)-cycle, one \(r\)-cycle and \(15-p-q-r\) fixed points, where \(p<q<r\) are distinct primes in \(\{2,3,5,7\}\). Orient it by the increasing prime order. The primitive generator is

\[
z=T_{235}-T_{237}+T_{257}-T_{357}.
\]

Its four triangles have exactly the six shared pair-orbit edges of a tetrahedron and no filling three-cell. In degree two it generates the **entire** integral homology of \(Y_{15}\).

## Assumptions and scope

All symmetric groups are on the indicated number of letters, and a cycle-type partition includes every fixed point as a part of length one. For a nonidentity permutation with cycle type \(\lambda\), write \(P(\lambda)\) for the strictly increasing set of primes dividing at least one part of \(\lambda\). A cell of dimension \(j\) in \(Y_n\) corresponds to one conjugacy class \(\lambda\vdash n\) with \(|P(\lambda)|=j+1\). The construction and the assertion concern integral singular/cellular homology, not sheaf homology.

## Proof

**(1) Exact quotient cellular chains.** By the unique decomposition of a finite-order group element into commuting primary parts, nonempty faces of \(X_{S_n}\) correspond bijectively to nonidentity permutations. Conjugation sends such a face to the face of the conjugate permutation. A face has at most one vertex associated with each prime. Hence any conjugation stabilizer of a face fixes each vertex, acts pointwise on that geometric simplex, and cannot reverse its orientation. Therefore \(Y_n\) is a finite CW complex with one oriented open \(j\)-cell per conjugacy class \(\lambda\) having \(|P(\lambda)|=j+1\), and all its incidence coefficients are the usual alternating simplicial ones.

**(2) An explicit integral boundary matrix.** For a prime \(p\in P(\lambda)\), define \(d_p(\lambda)\) by replacing a cycle of length \(L\) by \(p^{v_p(L)}\) cycles of length \(L/p^{v_p(L)}\). This is the cycle type of the prime-to-\(p\) part of the original permutation: the \(p^{v_p(L)}\) powers of a length-\(L\) cycle split into exactly that many cycles. If \(P(\lambda)=\{p_0<\cdots<p_j\}\), then

\[
\partial_j[\lambda]=\sum_{i=0}^{j}(-1)^i[d_{p_i}(\lambda)].
\]

Distinct primes label distinct vertices, so the formula has no unrecorded stabilizer multiplicities. This description is valid integrally, with no rational-transfer assumption.

**(3) No filling cells before seventeen letters.** A permutation whose order is divisible by four distinct primes uses at least \(2+3+5+7=17\) letters. Indeed, assigning the distinct primes to cycles that contain them, a cycle containing several distinct primes has length at least their product, at least their sum; summing over cycles gives the bound. Consequently \(C_3(Y_n;\mathbb Z)=0\) for \(n\le16\), and in particular every integral two-cycle for \(n\le15\) survives to homology.

**(4) The four-triangle cycle.** For \(n=15\), the four cycle types of the cells \(T_{235},T_{237},T_{257},T_{357}\) are respectively

\[
(5,3,2,1^5),\quad (7,3,2,1^3),\quad
(7,5,2,1),\quad(7,5,3).
\]

The boundary formula in step (2) identifies the edge resulting from deleting a prime with the unique orbit edge represented by the remaining two prime-length cycles and the corresponding fixed points. Every edge in \(z\) therefore occurs twice with opposite signs. Thus \(\partial_2 z=0\). The coefficient of \(T_{235}\) is \(+1\), so \(z\) is primitive in the integral two-chain lattice.

**(5) Exhaustive finite free-edge and rank certificates for the cutoff.** For \(n<10\) there are no two-cells: the smallest three distinct primes have sum ten, and putting distinct primes into a common cycle cannot lower the total support. For \(10\le n\le15\), enumerate all integer partitions \(\lambda\vdash n\), group by \(|P(\lambda)|\), and form the full integer matrix in step (2). There is also an integral free-edge elimination: whenever an orbit edge belongs to exactly one of the currently retained orbit triangles, the coefficient of that triangle must be zero in every two-cycle. Delete all such triangles and repeat. This does not assume mod-two coefficients or any numerical rank theorem. Complete enumeration gives the following exact sequences of simultaneous deletion-batch sizes, together with independent residue-field ranks (moduli \(101\) and \(103\)):

| \(n\) | Number of two-cells | Deleted per peeling round | Remaining | Rank modulo each of \(101,103\) |
|:--:|--:|:--|--:|--:|
| 10 | 1 | 1 | 0 | 1 |
| 11 | 2 | 2 | 0 | 2 |
| 12 | 5 | 5 | 0 | 5 |
| 13 | 9 | 8, 1 | 0 | 9 |
| 14 | 15 | 12, 3 | 0 | 15 |
| 15 | 24 | 15, 4, 1 | 4 | 23 |

The direct peeling certificate forces all coefficients of a two-cycle to vanish for \(n\le14\). At \(n=15\), the four retained cells are **exactly** \(T_{235},T_{237},T_{257},T_{357}\); their six shared edges form a tetrahedron boundary, whose integral two-cycle group is generated by \(z\). As an independent rank check, full column rank modulo a prime proves injectivity over \(\mathbb Z\) below fifteen; at fifteen the modular rank \(23\) and the primitive kernel vector force integral kernel rank one. Both arguments agree. As \(\partial_3=0\), it generates \(H_2(Y_{15};\mathbb Z)\), finishing the proof.

## Verification

The self-contained `verify.py` enumerates every integer partition for \(1\le n\le15\), forms the complete quotient boundary matrices using the prime-part cycle rule, verifies \(\partial_1\partial_2=0\), performs exact integral free-edge elimination and modular elimination over both fields, and checks the displayed four-triangle cycle as an **integer** vector. `verification_output.txt` contains its observed output. This finite exhaustive verification matches the exact domain of the theorem; no extrapolation to larger \(n\) is claimed.

## Relationship to prior work

Bate, Everitt and Ford introduced and developed the group clique complex in their 2026 preprint, including its prime-primary decomposition, a conjugacy-class schematic (Section 1.4), and structural calculations for symmetric groups (Section 2.1). Their schematic supplies the correct combinatorial point of departure. Their discussion and the associated order-sheaf homology calculations do **not** provide the displayed first integral second-homology threshold or the unique spherical generator of the geometric conjugation quotient. The earlier construction attributed to Donkin is acknowledged as a definitional antecedent. This finding concerns the topology of the geometric orbit space, not the homology of \(X_{S_n}\) or of its order sheaf.

## Limitations

This is a sharp finite cutoff result, not an all-ranks classification. It does not determine lower homology groups, higher homotopy groups, or the topology of \(Y_n\) for \(n>15\). The embedded sphere is shown to generate integral \(H_2\); the argument does not assert a wedge decomposition. Overlap risk remains for unindexed equivalent analyses of the earlier group-clique construction.

## References

1. M. Bate, B. Everitt and S. Ford, *Clique complexes of groups and order sheaves*, arXiv:2607.22369, first publicly posted 2026-07-24; see Sections 1.2, 1.4, 2.1, 3.3 and 4.1. https://arxiv.org/abs/2607.22369
2. S. Donkin, *K-0 of Hall's universal group*, Journal of Algebra 306 (2006), 47–61, doi:10.1016/j.jalgebra.2006.03.041 (earlier construction cited in Reference 1; full text not reviewed here).
