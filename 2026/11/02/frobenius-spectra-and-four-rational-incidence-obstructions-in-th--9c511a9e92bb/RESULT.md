# Frobenius spectra and four rational-incidence obstructions in the Kummer node–trope configuration

## Finding

Let \(k=\mathbb F_q\) have odd characteristic and let \(C:y^2=f(x)\) be a smooth genus-two curve with \(f\in k[x]\) separable of degree six. For the associated Jacobian Kummer quartic, let \(N\) be its 16 geometric nodes, \(T\) its 16 geometric trope planes, and \(I=\{(n,t)\in N\times T:n\in t\}\) its 96 incidences. If \(\lambda\) is the Frobenius cycle partition of the six roots of \(f\), then the Frobenius orbit spectrum on \(I\) is the eleven-row table below. There are rational nodes and rational tropes but no rational incidence **if and only if** \(\lambda\) equals \((6)\), \((4,2)\), \((3,3)\), or \((2,2,2)\). The least extension over which all 96 incidences are defined has degree \(\operatorname{lcm}(\lambda)\); the table gives all extension-field counts and the zeta function of \(I\).

| \(\lambda\) | Nodes and tropes: orbit cycles | Incidence flags: orbit cycles | Rational flags |
|---|---|---|---:|
| `(6)` | \(1^{1}\,3^{1}\,6^{2}\) | \(6^{16}\) | 0 |
| `(5,1)` | \(1^{1}\,5^{3}\) | \(1^{1}\,5^{19}\) | 1 |
| `(4,2)` | \(1^{2}\,2^{1}\,4^{3}\) | \(2^{4}\,4^{22}\) | 0 |
| `(4,1,1)` | \(1^{2}\,2^{1}\,4^{3}\) | \(1^{4}\,2^{2}\,4^{22}\) | 4 |
| `(3,3)` | \(1^{1}\,3^{5}\) | \(3^{32}\) | 0 |
| `(3,2,1)` | \(1^{2}\,2^{1}\,3^{2}\,6^{1}\) | \(1^{2}\,2^{5}\,3^{10}\,6^{9}\) | 2 |
| `(3,1,1,1)` | \(1^{4}\,3^{4}\) | \(1^{12}\,3^{28}\) | 12 |
| `(2,2,2)` | \(1^{4}\,2^{6}\) | \(2^{48}\) | 0 |
| `(2,2,1,1)` | \(1^{4}\,2^{6}\) | \(1^{8}\,2^{44}\) | 8 |
| `(2,1,1,1,1)` | \(1^{8}\,2^{4}\) | \(1^{32}\,2^{32}\) | 32 |
| `(1,1,1,1,1,1)` | \(1^{16}\) | \(1^{96}\) | 96 |

A term \(d^{c_d}\) records \(c_d\) cycles of length \(d\). Distinct terms specify the disjoint union of all Frobenius cycles. The equality of the node/trope spectra is also forced by the classical invertible rational incidence matrix of the symmetric \(16,6,2\) design; this representation-theoretic consequence is **not** claimed as new.

## Assumptions and scope

The sextic must be separable and of degree exactly six, over a finite field of odd characteristic. Its six roots need not be rational. Nodes and tropes are taken as reduced finite étale collections of geometric objects; the incidence flag records a geometric node lying in a geometric trope plane. The theorem concerns the Jacobian Kummer quartic of the displayed curve, not arbitrary twists of an abstract Kummer configuration.

## Proof

Label the six geometric branch points by \(\Omega=\{1,\dots,6\}\). The standard Kummer labels are \(p_0\) and \(p_{ij}\) for the nodes, and \(T_i\) and \(T_{A|A^c}\) for the tropes, with \(|A|=3\) and unordered complementary triples \(A|A^c\). A trope \(T_i\) contains \(p_0\) and \(p_{ij}\) for all \(j\ne i\). A trope \(T_{A|A^c}\) contains precisely those six nodes \(p_{ij}\) whose pair \(\{i,j\}\) is entirely in \(A\) or entirely in \(A^c\). These rules give \(6\cdot6+10\cdot6=96\) incidence flags and every node lies in six tropes.

Equivalently, let \(V\) be the 16 even subsets of \(\Omega\) modulo complementation, and \(\Theta\) the 16 odd subsets modulo complementation. Write \([U]\) for a complement class and \(S\) for the six singleton classes. The canonical \(S_6\)-equivariant incidence condition is
\[
([A],[B])\in I\quad\Longleftrightarrow\quad[A\mathbin{\triangle}B]\in S.
\]
The even classes label nodes and the odd classes label tropes. All definitions are independent of choices of representatives because the complement of a six-set preserves parity and the quotient operation is compatible with symmetric difference. Since the characteristic is not two, the 16 two-torsion nodes are distinct; the classical trope incidence rules remain valid for the smooth sextic in every odd characteristic. Frobenius permutes the six roots of \(f\) and acts by that same permutation on these labels.

For each of the 720 permutations of \(\Omega\), partition both 16-element sets and the 96-element incidence set into cycles. The cycle spectra are constant on each conjugacy class; all eleven classes and the orbit spectra are displayed above. The verifier enumerates **all** permutations, compares the set-theoretic and classical-label incidence rules, checks the six incidences per node and trope, and separately checks fixed points of the \(n\)-th power for each \(1\le n\le6\) against the cycle counts. Each row sums to 96, establishing completeness. In all eleven rows the least common multiple of the flag cycle lengths equals \(\operatorname{lcm}(\lambda)\).

For a flag spectrum \(c_d\) the finite étale incidence scheme satisfies
\[
Z(I/k,s)=\prod_{d\ge1}(1-s^d)^{-c_d},\qquad
\#I(\mathbb F_{q^n})=\sum_{d\mid n}d\,c_d.
\]
The rational node and trope counts are the coefficients of length-one cycles in their respective column. Comparing them with the length-one incidence counts yields precisely the four stated obstructions.

## Verification

Execute `python3 verify.py` using Python 3.9 or later without third-party packages. The accompanying `verification_output.txt` records all eleven orbit spectra and ends in `VERIFY_OK`. The exact finite permutation census proves the finite-combinatorial classification; no small-field sampling is being substituted for the proof. The geometric input is the classical Kummer labeling and incidence theorem, as recorded in the cited articles.

## Relationship to prior work

Kumar, *K3 surfaces associated to curves of genus two*, section 4.2, describes the sixteen nodes, sixteen trope planes, and the classical labels. Malmendier, *Kummer surfaces associated with Seiberg–Witten curves*, section 2.2, describes the classical \((16,6)\) incidence structure and its explicit branch-root labels. Those works supply the foundational incidence theorem, not a claimed new geometry. The contribution assessed here is the complete eleven-type arithmetic spectrum for the 96 *incidences*, including the exact four splitting types for which rational nodes and rational tropes cannot be paired rationally. The equality of the node and trope spectra is an established consequence of the classical symmetric-design incidence matrix and is not used as a novelty claim. The calculation is not the earlier classification of Göpel and Rosenhain tetrads, which concerns distinct 60- and 80-element geometrical sets.

## Limitations

The classifications concern finite étale **reduced** configurations, not nilpotent thickenings of the node/trope incidence scheme, the full Kummer-surface zeta function, or characteristic two. Historical priority is provisional: the stated orbit table can be derived from the published \(S_6\) combinatorics, and a comprehensive independent literature audit has not been performed.

## References

1. A. Kumar, *K3 surfaces associated to curves of genus two*, arXiv:math/0701669v1 (first public 2007-01-24), section 4.2; https://arxiv.org/abs/math/0701669
2. A. Malmendier, *Kummer surfaces associated with Seiberg–Witten curves*, arXiv:0912.4774v1 (first public 2009-12-24), section 2.2; https://arxiv.org/abs/0912.4774
