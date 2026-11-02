# Frobenius spectra of the sixty node–plane incidence flags of trace Segre cubics

## Finding
Let \(k=\mathbb F_q\) have characteristic at least seven, and let \(E/k\) be a degree-six finite étale algebra. On the five-dimensional \(k\)-vector space \(V=\ker(\operatorname{Tr}_{E/k})\), define the projective cubic threefold
\[
 X_E=\{[z]\in\mathbb P(V):\operatorname{Tr}_{E/k}(z^3)=0\}.
\]
After base extension to \(\overline k\), its ten ordinary nodes are indexed by unordered splittings of six labels into two triples, and it contains fifteen distinguished planes indexed by perfect matchings of the six labels. There are sixty incident pairs \((n,\Pi)\) consisting of one of these nodes and one of these planes containing it. Write \(\mathcal N_E,\mathcal P_E,\mathcal F_E\) for the three *reduced* finite étale \(k\)-schemes with these geometric points (nodes, distinguished planes, and incident flags). This avoids assuming anything about possible nonreduced structures on the entire Fano scheme.

The factor degrees of \(E\) form a partition \(\lambda\) of six. In the table, \(d:c\) means exactly \(c\) Frobenius orbits of size \(d\). Columns \(N\), \(P\), and \(F\) give the **complete** spectra on \(\mathcal N_E\), \(\mathcal P_E\), and \(\mathcal F_E\), respectively; the final column lists their respective \(k\)-rational point counts.

| \(\lambda\) | \(N\) | \(P\) | \(F\) | \((N_1,P_1,F_1)\) |
|---|---|---|---|---|
| \((6)\) | 1:1, 3:1, 6:1 | 1:1, 2:1, 3:2, 6:1 | 1:1, 2:1, 3:5, 6:7 | \((1,1,1)\) |
| \((5,1)\) | 5:2 | 5:3 | 5:12 | \((0,0,0)\) |
| \((4,2)\) | 1:2, 4:2 | 1:1, 2:1, 4:3 | 2:2, 4:14 | \((2,1,0)\) |
| \((4,1,1)\) | 2:1, 4:2 | 1:1, 2:1, 4:3 | 2:2, 4:14 | \((0,1,0)\) |
| \((3,3)\) | 1:1, 3:3 | 1:3, 3:4 | 1:3, 3:19 | \((1,3,3)\) |
| \((3,2,1)\) | 1:1, 3:1, 6:1 | 3:1, 6:2 | 6:10 | \((1,0,0)\) |
| \((3,1,1,1)\) | 1:1, 3:3 | 3:5 | 3:20 | \((1,0,0)\) |
| \((2,2,2)\) | 1:4, 2:3 | 1:7, 2:4 | 1:16, 2:22 | \((4,7,16)\) |
| \((2,2,1,1)\) | 1:2, 2:4 | 1:3, 2:6 | 1:4, 2:28 | \((2,3,4)\) |
| \((2,1,1,1,1)\) | 1:4, 2:3 | 1:3, 2:6 | 2:30 | \((4,3,0)\) |
| \((1,1,1,1,1,1)\) | 1:10 | 1:15 | 1:60 | \((10,15,60)\) |

**Arithmetic incidence obstruction.** Both a \(k\)-rational distinguished plane and a \(k\)-rational node exist while no rational node lies on any rational distinguished plane **if and only if** \(\lambda=(4,2)\) or \(\lambda=(2,1,1,1,1)\). The two cases have respectively two nodes and one plane, or four nodes and three planes, but zero rational incident flags.

If \(c_d(\lambda)\) denotes the entries of the flag-spectrum column, then the exact zeta function of the finite étale flag scheme and every extension count are
\[
 Z(\mathcal F_E,T)=\prod_{d}(1-T^d)^{-c_d(\lambda)},\qquad
 \#\mathcal F_E(\mathbb F_{q^m})=\sum_{d\mid m}d\,c_d(\lambda).
\]
All sixty geometric flags become rational together for the first time over \(\mathbb F_{q^L}\), where \(L=\operatorname{lcm}(\lambda)\). These statements hold for every permitted \(q\), not just the eleven representative algebras.

## Assumptions and scope
The characteristic is \(p\ge7\), ensuring that two, three, and every nonzero integer of magnitude at most six behave as required in the singularity argument. Every finite étale algebra \(E\) of dimension six is allowed, with repeated factor degrees allowed. The exact field \(k=\mathbb F_q\) is arbitrary within the stated characteristic range; the theorem concerns the canonical geometrically defined ten nodes, the fifteen pairing planes, and their sixty incidence flags. Statements about planes refer specifically to this canonical set, without claiming reducedness of the full Hilbert or Fano scheme or any birational classification of the threefold.

## Proof
**1. Geometric model and nodes.** The base change \(E\otimes_k\overline k\) splits as \(\overline k^6\). Thus the cubic becomes the symmetric Segre model \(\sum_i x_i=\sum_i x_i^3=0\) inside \(\mathbb P^5\). A singular point satisfies \(3x_i^2=\alpha\) for all six coordinates because the cubic gradient is proportional to the gradient of the linear equation. Since the projective point is nonzero, \(\alpha\ne0\). Accordingly, each coordinate is \(\pm a\) for some nonzero \(a\). The equation \(\sum_i x_i=0\) forces exactly three plus and three minus signs: no other nonzero even difference in the interval from minus six to six vanishes in characteristic at least seven. Modulo global sign, these give precisely \(\binom63/2=10\) points. The diagonal quadratic tangent form \(\sum_i (\pm1)u_i^2\) has kernel, on the tangent hyperplane \(\sum_i u_i=0\), equal to the radial line; hence each projective singularity is an ordinary node.

**2. Distinguished planes and incidence.** For any perfect matching \(M=\{\{a,b\},\{c,d\},\{e,f\}\}\), the three linear equations \(x_a+x_b=x_c+x_d=x_e+x_f=0\) define a projective plane contained in the cubic: both the sum of coordinates and the sum of cubes vanish in opposite pairs. There are \(6!/(2^3 3!)=15\) such distinct planes, the classical Segre planes. A node determined by \(A\sqcup A^c\), with \(|A|=3\), lies in this plane exactly when every matching edge contains one vertex of \(A\) and one of \(A^c\). For each node this gives \(3!=6\) matching planes; for each plane it gives \(2^3/2=4\) nodes. Thus there are exactly sixty flags. This explicit incidence rule does not require an unproved global classification of arbitrary planes in positive characteristic.

**3. Arithmetic descent.** The six embeddings of \(E\) into \(\overline k\) are permuted by arithmetic Frobenius. If \(E\cong\prod_j\mathbb F_{q^{\lambda_j}}\), its permutation \(\sigma\) has cycle partition \(\lambda\). It acts on triples, matchings, and flags by relabeling. A geometric node, pairing plane, or flag descends to \(\mathbb F_{q^m}\) precisely when fixed by \(\sigma^m\). This is standard finite Galois descent for the three reduced parameter schemes.

**4. Exhaustive eleven-class calculation.** All \(720\) permutations of six labels fall into exactly the eleven partitions in the table. The supplied standalone verifier independently constructs the ten unordered triple partitions, fifteen perfect matchings, and sixty flags. It computes their permutation cycles for **every** element of \(S_6\), not a statistical sample. For every cycle type, the results agree across all representatives and give the three tabulated spectra. As an independent internal identity, it compares the fixed points of every positive power of a permutation with \(\sum_{d\mid m}d c_d\) for each of the three actions. The derived spectra have total degrees ten, fifteen, and sixty in every case. These finite combinatorial equalities, together with the descent in Step 3, prove the formulas for all \(q\) and every \(m\ge1\).

**5. Obstruction and exact splitting degrees.** The table shows rational nodes and rational planes but no fixed incidence flags precisely in the two partitions specified above. This also has a direct geometric explanation for \(\lambda=(2,1,1,1,1)\): a transposition stabilizes exactly the four triple partitions in which its swapped labels lie in the same triple, and exactly the three perfect matchings that pair those two labels. Since an incident matching must cross the two halves of a node partition, none of these stable pairs is incident. For the other exceptional type \(\lambda=(4,2)\), take Frobenius permutation \(\sigma=(0\,1\,2\,3)(4\,5)\). Its unique invariant pairing plane is represented by \(\{\{0,2\},\{1,3\},\{4,5\}\}\). Its two invariant node partitions are \(\{0,2,4\}\mid\{1,3,5\}\) and \(\{0,2,5\}\mid\{1,3,4\}\). The pairing edge \(\{0,2\}\) lies in one half of each partition, so this unique rational plane contains neither rational node. Finally, the least common multiple of the flag orbit lengths in every table row equals \(\operatorname{lcm}(\lambda)\). A field extension contains all sixty flags precisely when its degree is divisible by all those orbit lengths. This proves the stated minimal degree and the zeta function.

## Verification
Run `python3 verify.py` from the directory containing that standalone file. No third-party packages or input files are required. The script checks the complete set of \(720\) permutations, all eleven conjugacy types, the incidence bi-degrees \((6,4)\), the orbit counts and their fixed-point identities, and the two and only two rational-incidence-obstruction types. The included output file `verify_output.txt` concludes `VERIFY_OK`; the same script was run against its actual embedded-source candidate path before packaging. The computer enumeration is finite and exhaustive, and the general-field theorem follows from algebraic descent, not experimental extrapolation.

## Relationship to prior work
Dolgachev's 2015 account of the Segre cubic establishes the ten-node, fifteen-plane \((15_4,10_6)\) geometric configuration and the coordinate formulas used here, but it does not give the eleven-type arithmetic spectra of the sixty incident flags. Cheltsov–Tschinkel–Zhang (2023) study finite-subgroup actions, invariant nodes/planes, and equivariant birational linearizability; this is broader geometric group theory but does not state these field-of-definition cycle tables or their flag zeta functions. Pokora–Szemberg (2026) recover the classical fifteen planes via a Pascal-type construction, without providing Frobenius descent of node–plane flags. The node/plane geometry and \(S_6\) action are not claimed as novel. The asserted contribution is the complete arithmetic *joint incidence* classification, including the two cases where rational nodes and rational planes fail to form a rational incident pair.

## Limitations
The result is a classification of the reduced canonical finite incidence configurations, not a calculation of the Hasse–Weil zeta function of the threefold itself. It makes no claim for characteristics two, three, or five, nor does it classify all possible linear spaces or scheme-theoretic multiplicities of the full Fano scheme in those characteristics. The entries are exact, but the historical-priority check cannot exclude an unindexed equivalent tabulation or a broader character formula from which these data follow immediately. No independent scientific validation has been performed.

## References
1. I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432 (first submitted 2015-01-26), Section 2, especially Proposition 2.2 and the coordinate equations, https://arxiv.org/abs/1501.06432.
2. I. Cheltsov, Y. Tschinkel and Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, arXiv:2308.15271 (first submitted 2023-08-29), Sections 1, 2 and 6, https://arxiv.org/html/2308.15271v2.
3. P. Pokora and T. Szemberg, *A Pascal-type construction of the Segre cubic and the Cremona--Richmond configuration*, arXiv:2606.18387 (first submitted 2026-06-16), Sections 2 and 3, https://arxiv.org/abs/2606.18387.
