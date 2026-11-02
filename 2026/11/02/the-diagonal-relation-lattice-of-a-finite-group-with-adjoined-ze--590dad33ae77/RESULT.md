# The diagonal-relation lattice of a finite group with adjoined zero

## Finding
Let \(G\) be any finite group, \(0\notin G\) a new absorbing element, and \(S=G^0=G\sqcup\{0\}\). A **diagonal subsemigroup** on \(S\) is a reflexive relation \(R\subseteq S\times S\) closed under coordinatewise multiplication. Write \(\mathcal N(G)\) for the lattice of normal subgroups, and \(k=|\mathcal N(G)|\). The inclusion lattice of diagonal subsemigroups is canonically
\[
\operatorname{Diag}(G^0)\cong\mathcal N(G)\times\mathsf B_2,
\]
where \(\mathsf B_2\) is the four-element Boolean lattice. In particular,
\[
|\operatorname{Diag}(G^0)|=4k,\qquad
|\operatorname{SymDiag}(G^0)|=2k,\qquad
|\operatorname{Cong}(G^0)|=k+1.
\]
There are exactly \(2k\) asymmetric diagonal subsemigroups and \(k-1\) symmetric, nontransitive ones. Thus the **DSC coefficient** equals
\[
\chi(G^0)=\frac{|\operatorname{Cong}(G^0)|}{|\operatorname{Diag}(G^0)|}
=\frac{k+1}{4k}=\frac14+\frac1{4k}.
\]
Its exact range for all finite groups is \(\{(k+1)/(4k):k\ge1\}\). The value \(1/2\) characterizes the trivial group, the value \(3/8\) characterizes nontrivial finite simple groups, and \(1/4\) is the strict infimum. Every allowed value occurs.

## Assumptions and scope
The group \(G\) is finite, possibly trivial, and the new element \(0\) is two-sided absorbing, so \(0x=x0=0\) for every \(x\in G^0\). Relations are subsets of \(S^2\), not equivalence relations unless explicitly stated. A congruence is a diagonal subsemigroup that is symmetric and transitive. For \(N\trianglelefteq G\), define the group congruence
\[
\rho_N=\{(g,h)\in G^2:gh^{-1}\in N\}.
\]
The two parameters of the Boolean lattice record whether the full nonzero-to-zero row and full zero-to-nonzero column are present.

## Proof
**1. Restriction to the group square.** Let \(R\subseteq(G^0)^2\) be a diagonal subsemigroup. Its intersection \(Q=R\cap G^2\) is a finite subsemigroup of the finite group \(G\times G\), and contains its diagonal subgroup \(\Delta_G\). Any nonempty finite subsemigroup of a group is a subgroup: positive powers of every element eventually give its inverse. Thus \(Q\) is a subgroup of \(G^2\) containing \(\Delta_G\). Put \(N=\{g\in G:(g,1_G)\in Q\}\). Multiplication by diagonal group elements establishes \(Q=\rho_N\); conjugation by \(\Delta_G\) gives \(N\trianglelefteq G\), uniquely.

**2. Cross-stratum rigidity.** If \((g,0)\in R\) for any \(g\in G\), then \((g,0)(h,h)=(gh,0)\in R\) for every \(h\in G\), because \(\Delta_G\subseteq R\). Hence the nonzero-to-zero row is either empty or all of \(G\times\{0\}\). Similarly the zero-to-nonzero column is either empty or all of \(\{0\}\times G\). The pair \((0,0)\) is always present.

**3. Every parameter tuple is realized.** For any \(N\trianglelefteq G\) and booleans \(a,b\in\{0,1\}\), let
\[
R(N,a,b)=\rho_N\cup\{(0,0)\}\cup
\begin{cases}G\times\{0\},&a=1,\\\varnothing,&a=0,\end{cases}
\cup\begin{cases}\{0\}\times G,&b=1,\\\varnothing,&b=0.\end{cases}
\]
All four cross-stratum choices are multiplication-compatible: multiplying a row or column by any group-pair remains in that same row or column, multiplying a row by a column gives \((0,0)\), and products within \(\rho_N\) stay inside \(\rho_N\). Step 1 and Step 2 prove these are all possibilities, uniquely. Inclusion is exactly \(N\subseteq N'\), \(a\le a'\), and \(b\le b'\), yielding the claimed lattice product and \(4k\) relations.

**4. Congruence and defect counts.** The restriction \(\rho_N\) is always symmetric and transitive. Reversal interchanges the cross row and column, so \(R(N,a,b)\) is symmetric precisely when \(a=b\). This gives \(2k\) symmetric relations, with exactly \(2k\) asymmetric relations. When \(a=b=0\), the relation is a congruence with zero in a singleton class, for every \(N\). When \(a=b=1\), the relation relates zero to every group element. Transitivity then forces all group elements equivalent, hence \(N=G\); conversely \(R(G,1,1)=S^2\) is the universal congruence. Thus precisely \(k+1\) relations are congruences and \(k-1\) are symmetric but nontransitive.

**5. Coefficient spectrum and sharp boundaries.** Each \(G\) has at least one normal subgroup, and for each integer \(k\ge1\), the cyclic group \(C_{p^{k-1}}\) has exactly \(k\) normal subgroups, with \(C_{p^0}\) interpreted as the trivial group. Consequently all and only the stated coefficient values occur. The normal-subgroup count equals one exactly for the trivial group, and equals two exactly for a nontrivial simple group. The sequence is strictly decreasing in \(k\) with infimum \(1/4\), which no finite group attains.

## Verification
The accompanying standalone `verify.py` builds concrete multiplication tables for cyclic groups of orders \(1\) through \(5\) and for the nonabelian symmetric group \(S_3\). It enumerates normal subgroups, constructs all predicted relations, checks coordinatewise multiplication closure for each, and tests the congruence counts. For cyclic groups of orders \(1,2,3\), it also exhaustively enumerates **every** reflexive relation on the enlarged semigroup and verifies that the predicted list is complete. Running `python3 verify.py` terminates with `VERIFY_OK`. The mathematical proof, not the finite computations, establishes the result for every finite group.

## Relationship to prior work
Barber and Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups* (arXiv:2602.17286, first version 19 February 2026), introduce the DSC coefficient, classify diagonal subsemigroups for completely simple Rees matrix semigroups, and prove an upper bound in terms of the idempotent semilattice for Clifford semigroups. Their Section 4 explicitly notes that the displayed family of diagonal subsemigroups does not exhaust Clifford semigroups and uses the **different** construction of adjoining a *new identity* to a group. Their general bound does not determine the exact count, lattice, defect partition, or coefficient spectrum for absorbing-zero extensions.

Barber and Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square* (arXiv:2504.02428, first version 3 April 2025), establish general DSC results, including the finite-group case; these do not determine the quantitative defect for \(G^0\). The group-level classification of subgroup relations is standard, and is used here rather than asserted as new. The contribution is the complete diagonal-relation lattice and sharp coefficient range for the absorbing-zero extension of **every** finite group.

## Limitations
The result concerns finite groups with a *single new absorbing zero*, not arbitrary Clifford semigroups, unrelated zero extensions of general semigroups, or infinite groups. The coefficient distinguishes only the number of normal subgroups, not all isomorphism types of groups. Mathematical priority beyond the inspected sources and mathematical-record searches is not independently certified.

## References
1. C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286v1 (2026-02-19), https://arxiv.org/abs/2602.17286.
2. C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, arXiv:2504.02428v1 (2025-04-03), https://arxiv.org/abs/2504.02428.
