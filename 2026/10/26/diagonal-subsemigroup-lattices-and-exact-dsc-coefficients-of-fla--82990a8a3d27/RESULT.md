# Diagonal-subsemigroup lattices and exact DSC coefficients of flat semilattices

## Finding
For every integer \(m\ge1\), let \(F_m=\{0,a_1,\ldots,a_m\}\) be the flat (height-two) meet-semilattice, with \(a_i\wedge a_j=0\) for distinct atoms and \(x\wedge x=x\). A diagonal subsemigroup is a binary relation on \(F_m\) containing all \((x,x)\) and closed under coordinatewise meet.

Every diagonal subsemigroup has a unique normal form
\[
R(L,U,E)=\Delta\cup\{(a_i,0):i\in L\}\cup\{(0,a_j):j\in U\}\cup\{(a_i,a_j):(i,j)\in E\},
\]
where \(L,U\subseteq[m]\) and \(E\) is an arbitrary subset of \(\{(i,j):i\in L,\ j\in U,\ i\ne j\}\). Conversely, every such triple defines a diagonal subsemigroup.

The inclusion lattice of diagonal subsemigroups is isomorphic to the lattice of order ideals of a specific height-two poset \(P_m\): its lower elements are \(\ell_i,r_j\) for \(i,j\in[m]\), and its upper elements are \(e_{ij}\) for \(i\ne j\), with the only strict comparabilities \(\ell_i<e_{ij}\) and \(r_j<e_{ij}\). In particular, this lattice is distributive, and union and intersection of its relations are its join and meet.

Its cardinality, symmetric-member cardinality, congruence cardinality, and DSC coefficient are exactly
\[
D_m=\sum_{L,U\subseteq[m]}2^{|L||U|-|L\cap U|},\quad
T_m=\sum_{k=0}^m\binom{m}{k}2^{\binom{k}{2}},\quad
C_m=2^m,\quad
\chi(F_m)=\frac{2^m}{D_m}.
\]
Furthermore, as \(m\to\infty\),
\[
D_m\sim 2^{m(m-1)},\qquad \chi(F_m)\sim2^{-m(m-2)}.
\]
For \(m=1,2,3,4,5,6\), the exact values of \(D_m\) are \(4,25,322,12643,2090884,1602951445\), respectively. The first non-chain flat semilattice is \(F_2\), whose exact coefficient is \(4/25\).

## Assumptions and scope
The language consists solely of the associative, commutative, idempotent binary meet operation. All cardinalities are of labeled relations on the fixed underlying set; no quotient by atom permutations is taken. The poset ideal correspondence concerns all reflexive compatible relations, not just equivalence relations. The exceptional one-element case \(m=0\) has \(D_0=T_0=C_0=1\), if included by convention.

## Proof
**Necessity of the normal form.** Fix a diagonal subsemigroup \(R\). For every off-diagonal pair of distinct nonzero atoms \((a_i,a_j)\in R\), meet with the diagonal pairs \((a_i,a_i)\) and \((a_j,a_j)\). This forces \((a_i,0)\in R\) and \((0,a_j)\in R\). There are no other off-diagonal types besides these markers and atom-to-atom pairs, so the sets \(L,U,E\) are uniquely recovered from \(R\).

**Sufficiency.** In a proposed relation of the displayed form, meeting two pairs of nonzero atoms has, in each coordinate, either the common atom or zero. If the product is diagonal, it belongs to \(\Delta\). If the product has just one nonzero coordinate, its marker is present: a nonzero first coordinate \(a_i\) can only come from factors whose first coordinates were both \(a_i\), and any off-diagonal factor with that first coordinate already requires the marker \((a_i,0)\); when both factors are diagonal \((a_i,a_i)\), the output is diagonal. The dual statement applies to a nonzero second coordinate. If both product coordinates are nonzero and distinct, both original pairs must have exactly those two coordinates, so their common pair is already in the relation. Thus closure holds. Meets with a marker or \((0,0)\) obey the same cases. This proves the bijection.

**The lattice.** Associate each selected left marker with \(\ell_i\), each selected right marker with \(r_j\), and each edge with \(e_{ij}\). Selection of \(e_{ij}\) requires precisely the two lower elements \(\ell_i,r_j\); there are no other constraints. The selected elements are therefore exactly the order ideals of \(P_m\). This bijection preserves inclusion, intersections and unions, proving the distributive-lattice assertion.

**Counting.** For fixed \(L,U\), the permissible directed off-diagonal edges are independent. Their number is \(|L||U|-|L\cap U|\), giving \(D_m\). Symmetry forces \(L=U=W\) and forces each selected directed edge to appear with its reversal. For \(|W|=k\), the choices are the \(\binom{k}{2}\) unordered atom pairs, giving \(T_m\). For a congruence, if two distinct atoms were equivalent, meeting their equivalence with the diagonal of either atom forces that atom to be equivalent to zero; hence every nonzero equivalence class is a singleton. Conversely, any subset \(W\subseteq[m]\) yields a congruence whose zero class is \(\{0\}\cup\{a_i:i\in W\}\), with all other classes singletons. There are exactly \(2^m\), giving \(C_m\) and \(\chi(F_m)\).

**Asymptotic.** The \(L=U=[m]\) contribution to \(D_m\) is \(2^{m(m-1)}\). For general \(L,U\), let \(s=|[m]\setminus L|+|[m]\setminus U|\). Each missing left marker forbids \(m-1\) directed atom-pair edges, and each missing right marker likewise forbids \(m-1\); each edge is counted at most twice in these forbidden-edge incidences. Therefore the number of forbidden edges is at least \((m-1)s/2\), and
\[
1\le\frac{D_m}{2^{m(m-1)}}\le\sum_{s=0}^{2m}\binom{2m}{s}2^{-(m-1)s/2}=\bigl(1+2^{-(m-1)/2}\bigr)^{2m}\longrightarrow1.
\]
The DSC asymptotic follows by division.

## Verification
The standalone \(\texttt{verify.py}\) independently enumerates **all** reflexive relations on \(F_m\) for \(m=0,1,2,3\), tests closure under coordinatewise meet directly, checks symmetry and transitivity, reconstructs the unique normal-form parameters, and compares all three enumerators with the formulas. It also evaluates the formulas for \(m=4,5,6,7\); these latter evaluations do not constitute exhaustive independent relation enumeration. The completed direct check reports \(\texttt{VERIFY_OK}\). No finite enumeration is used as a substitute for the preceding general proof.

## Relationship to prior work
Barber and Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups* (2026), introduce the DSC coefficient and study Rees matrix and Clifford semigroups. Their final section explicitly notes that possible DSC coefficients of semilattices are not characterized and suggests vanishing as their size increases. The present result supplies a complete and structurally transparent infinite family, including an exact quantitative vanishing law. Their 2025 paper *Semigroup Congruences and Subsemigroups of the Direct Square* studies the qualitative property of every diagonal subsemigroup being a congruence; its inverse-semigroup results do not give the formulas above. A separate exact census is known for totally ordered (chain) semilattices, but those do not imply the distinct branching normal form for \(F_m\) with \(m\ge2\). This work is a family-specific answer, not a classification of DSC coefficients for arbitrary semilattices.

## Limitations
Only flat meet-semilattices (one minimum and mutually incomparable atoms) are covered. The exact count does not classify more general rooted meet-semilattices, quotient lattices under atom permutations, or all possible DSC coefficients. The numerical verifier independently checks finitely many cases, while the infinite assertion uses the mathematical argument above. The novelty comparison is necessarily relative to identified and inspected sources; older or unindexed equivalent statements cannot be ruled out absolutely.

## References
1. C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286 (first available 2026-02-19), https://arxiv.org/html/2602.17286v2.
2. C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, arXiv:2504.02428 (first available 2025-04-03), https://doi.org/10.1017/S0004972725100166.
