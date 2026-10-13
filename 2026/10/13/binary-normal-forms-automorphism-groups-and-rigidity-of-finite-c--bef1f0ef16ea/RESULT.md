# Binary normal forms, automorphism groups, and rigidity of finite chain-indexed Bochvar algebras

## Finding

Let \(\mathsf{BCA}_{\mathrm{chain}}\) consist of finite Bochvar algebras with **linearly ordered canonical Płonka index semilattice**. There is **exactly one isomorphism class in every positive cardinality**:
\[
\#\{\mathbf A\in\mathsf{BCA}_{\mathrm{chain}}/\cong:\ |A|=N\}=1\qquad(N\ge1).
\]
In particular, if the binary expansion is
\[
N=2^{e_0}+2^{e_1}+\cdots+2^{e_{r-1}},\qquad e_0>e_1>\cdots>e_{r-1}\ge0,
\]
then the canonical Boolean fibers have exactly the listed cardinalities, in precisely this order, and there are \(r=\operatorname{popcount}(N)\) of them. Writing \(e_r=0\), the full symmetry group is
\[
\operatorname{Aut}(\mathbf B_N)\cong\prod_{i=0}^{r-1}S_{e_i-e_{i+1}}.
\]
Consequently
\[
\operatorname{Aut}(\mathbf B_N)=1\quad\Longleftrightarrow\quad
N\in\{2^t-1:t\ge1\}\cup\{2^t-2:t\ge2\}.
\]
The ordinary generating function for the number of isomorphism types, graded by total cardinality, is \(z/(1-z)\). For fixed number \(k\) of atoms in the first Boolean fiber, the size generating polynomial is
\[
\sum_{N=2^k}^{2^{k+1}-1} z^N
=z^{2^k}\prod_{j=0}^{k-1}(1+z^{2^j}),
\]
with the empty product understood as \(1\) for \(k=0\).

## Assumptions and scope

A Bochvar algebra here means a member of the quasivariety \(\mathsf{BCA}\) in the signature \(\langle\wedge,\vee,\neg,J_0,J_1,J_2,0,1\rangle\). Its involutive-bisemilattice reduct has the **canonical** Płonka-sum representation over a join-semilattice \(I\) with least element; the class under study consists exactly of finite algebras where \(I\) is totally ordered. Fiber copies are disjoint even when their abstract Boolean algebras are isomorphic. The one-element algebra is included; if a convention excludes it, start all cardinality statements at \(N=2\). Symmetric groups \(S_0\) and \(S_1\) are trivial.

We use Theorems 3.15 and 3.17 of Bonzio–Pra Baldi [1]: the direct-system homomorphisms are surjective, the Boolean fibers can be identified with intervals below elements \(a_i=J_2(1_i)\) of the first fiber, distinct indices have distinct \(a_i\), and a later index in the chain yields a strictly smaller \(a_i\). Conversely such proper, surjective, interval-isomorphism data admit Bochvar operations. The decomposition is unique up to isomorphism.

## Proof

**Necessity and binary uniqueness.** Let \(I=\{i_0<\cdots<i_{r-1}\}\) index the canonical decomposition of a finite member. Let the first Boolean fiber have \(k\) atoms, so after a Boolean isomorphism it is \(\mathcal P([k])\). The interval-isomorphism condition in [1, Thm. 3.15] supplies supports \(S_j\subseteq[k]\), one for each fiber, with \(S_0=[k]\) and
\[
S_0\supsetneq S_1\supsetneq\cdots\supsetneq S_{r-1}.
\]
Put \(e_j=|S_j|\). The fiber at \(i_j\) is isomorphic to the Boolean algebra \(\mathcal P(S_j)\), hence has \(2^{e_j}\) elements. Strict nesting gives \(e_0>\cdots>e_{r-1}\ge0\). Because Płonka fibers are disjoint, \(|A|=\sum_j2^{e_j}\) is a binary expansion with no repeated powers. Its exponent list is thus determined by \(|A|\). The same source's uniqueness theorem ensures the index and fiber data are invariants of the algebra.

**Existence.** Given any \(N\ge1\), write its binary expansion as above. Let \(S_j=\{1,\ldots,e_j\}\subseteq[e_0]\), with \(S_j=\varnothing\) when \(e_j=0\), and take the ordered Płonka index \(I=\{0<\cdots<r-1\}\). Put \(A_j=\mathcal P(S_j)\) and, for \(i\le j\), set \(p_{ij}(U)=U\cap S_j\). These Boolean homomorphisms are surjective and proper when \(i<j\), and the restriction of \(p_{0j}\) to \([\varnothing,S_j]\) is an isomorphism. Thus [1, Thm. 3.17] equips their Płonka sum with Bochvar operations. An explicit presentation, writing \((j,U)\) for the element \(U\subseteq S_j\) in its fiber, is
\[
J_2(j,U)=(0,U),\quad J_0(j,U)=(0,S_j\setminus U),\quad
J_1(j,U)=(0,S_0\setminus S_j).
\]
The internal binary operations are evaluated in the fiber with larger index, after intersecting both operands with its support; negation complements within the original fiber. The cardinality is \(N\).

**Uniqueness within one cardinality.** Two chains of subsets of a \(k\)-point set having the same cardinalities \(e_0>\cdots>e_{r-1}\) are conjugate by a permutation: match the successive disjoint layers \(S_j\setminus S_{j+1}\) and the last set \(S_{r-1}\). Such a permutation conjugates the entire family of restriction maps, and the displayed external operations are equivariant under it. Thus the associated Bochvar algebras are isomorphic. This and necessity prove the one-per-cardinality claim.

**Automorphisms.** An algebra automorphism preserves the canonical ordered index; a finite chain has no nontrivial order automorphisms. Its restriction to the first fiber is a Boolean automorphism, hence permutes the \(k\) atoms, and it must fix each support \(S_j=J_2(1_j)\). Conversely every permutation preserving each \(S_j\) induces a compatible automorphism of all fibers and all external operations. The stabilizer of the nested chain is the product of the full symmetric groups on its disjoint layers, giving the group formula. This stabilizer is trivial exactly when all layer sizes are \(0\) or \(1\); the strict differences force consecutive exponents, and the final exponent is \(0\) or \(1\). Summing those consecutive powers gives precisely the two displayed rigid-cardinality families.

## Verification

Run `python3 verify.py` using Python's standard library. It exhaustively enumerates every strictly descending chain of labeled subsets on up to seven base atoms, checks the complete binary cardinality interval for each base rank, confirms all transition restrictions and the rigidity formula, and tests stabilizer orders against every base-atom permutation through rank five. Separately, it constructs full operation tables for all canonical chains through rank three and tests all nineteen equations/quasi-equations from [1, Def. 3.1]. The deterministic output ends in

`VERIFY_OK 15154351 exact assertions; binary uniqueness through k=7; stabilizer symmetries through k=5`

`VERIFY_AXIOMS_OK 156475 exact checks of all 19 Bochvar axioms/quasi-axiom over all canonical forms with k<=3`

These bounded checks corroborate, but do not replace, the general proof by finite Boolean interval structure and binary expansion.

## Relationship to prior work

Bonzio and Pra Baldi [1], first made public on May 9, 2023, prove the necessary-and-sufficient Płonka decomposition used as input, including its uniqueness. The inspected full text does not state the chain-index cardinality classification or automorphism/rigidity spectrum; the new step is the **complete binary normal form and group invariant** of this natural finite subclass. Bonzio–Pra Baldi–Valota [2] count linearly indexed **involutive bisemilattices**, whose transition systems need not carry the extra Bochvar external operators or strict interval-support condition, and obtain a substantially more involved enumeration. Bonzio–Paoli–Pra Baldi [3], first public in December 2024, give a later, stronger categorical equivalence with Boolean-algebra/meet-subsemilattice pairs; it conceptually encompasses the representation, but the inspected manuscript does not present this binary fine spectrum, automorphism product, or rigidity criterion. Paoli et al. [4], published August 2026, explore a different regular-double-Stone-algebra categorical connection; its abstract does not assert these exact finite-chain invariants.

## Limitations

This concerns finite algebras with **chain-shaped canonical Płonka index**, not all Bochvar algebras or all algebras whose *underlying lattice order* is a chain. It is an elementary enumerative and symmetry refinement of established structure theorems, not a new general representation theorem. The 2024 categorical equivalence supplies a broader framework and could make this an unstated folklore corollary; no claim of exhaustive literature coverage or independent expert audit is made. The experiments verify ranks at most seven and direct axioms at most three, not an infinite theorem computationally.

## References

[1] S. Bonzio and M. Pra Baldi, *On the Structure of Bochvar Algebras*, arXiv:2305.05457 (first submitted 2023-05-09), Theorems 3.15 and 3.17, Corollary 3.18; *Review of Symbolic Logic* 18 (2025), 273–299. https://arxiv.org/abs/2305.05457 ; https://doi.org/10.1017/S175502032400008X.

[2] S. Bonzio, M. Pra Baldi and D. Valota, *Counting Finite Linearly Ordered Involutive Bisemilattices*, RAMiCS 2018, pp. 166–183, arXiv:2107.10540; https://arxiv.org/abs/2107.10540.

[3] S. Bonzio, F. Paoli and M. Pra Baldi, *Bochvar Algebras: A Categorical Equivalence and the Generated Variety*, arXiv:2412.14911 (2024-12-19), Theorem 16; https://arxiv.org/abs/2412.14911.

[4] F. Paoli, G. Vergottini, N. Zamperlin and D. Fazio, *On Bochvar Algebras and Regular Double Stone Algebras*, *Studia Logica*, published 2026-08-21; https://doi.org/10.1007/s11225-026-10262-9.
