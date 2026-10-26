# Silver-ratio one-point type spectrum and linear two-sided cuts of cyclic triple-incidence posets

## Finding
For each integer \(n\ge5\), let \(P_n\) be the height-two poset with pairwise distinct minimal elements \(a_0,\ldots,a_{n-1}\) and maximal elements \(b_0,\ldots,b_{n-1}\), indexed cyclically, and with the only strict relations
\[
a_i<b_j\quad\Longleftrightarrow\quad i-j\pmod n\in\{0,1,2\}.
\]
Name every point of \(P_n\) in the countable universal homogeneous poset \(\mathbb D\). Let \(t_n\) count complete **nonalgebraic** one-types over these \(2n\) parameters. Then
\[
\boxed{t_n=2\big((1+\sqrt2)^n+(1-\sqrt2)^n\big)+12n+1.}
\]
Exactly \(12n\) of these types place the new point strictly above at least one parameter and strictly below at least one parameter. In particular, their proportion tends to zero, and
\[
\boxed{t_n\sim 2(1+\sqrt2)^n,\qquad
\frac{12n}{t_n}\sim\frac{6n}{(1+\sqrt2)^n}.}
\]
Including the \(2n\) algebraic equality types, the complete one-type count is \(t_n+2n\). The initial nonalgebraic counts for \(n=5,6,7,8,9\) are \(225,469,1041,2405,5681\).

## Assumptions and scope
The poset \(\mathbb D\) is the Fraïssé limit of all finite partial orders. The lower and upper layers of \(P_n\) each have \(n\) **individually named** points; automorphisms of the unnamed cyclic incidence structure do not identify parameter types. A nonalgebraic type is realized outside this finite named set. The cyclic length bound \(n\ge5\) ensures that cyclic adjacent pairs, distance-two pairs, and consecutive triples have the distinct incidence multiplicities used below. No claim is made for shorter cycles without separate formulas.

## Proof
**1. Extension patterns.** For any finite induced parameter poset \(P\) and new point \(x\), put \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). Transitivity is equivalent to \(L\) being a downset, \(U\) an upset, and \(l<u\) for every \(l\in L\) and \(u\in U\). Conversely these conditions define a finite poset extension, which is realized in \(\mathbb D\) and determines one complete nonalgebraic type by ultrahomogeneity. This correspondence is standard; only its ensuing cyclic enumeration is asserted as new.

Write \(J_n\) for the number of order ideals of \(P_n\). The cases \(L=\varnothing\) or \(U=\varnothing\) contribute precisely \(2J_n-1\) extension types: ideals and filters have equal cardinalities by complementation, and the doubly empty pattern is counted twice. If both \(L\) and \(U\) are nonempty, neither can contain a maximal and minimal point respectively, because every point of \(L\) must lie strictly below every point of \(U\). Thus \(L=X\subseteq\{a_i\}\) and \(U=Y\subseteq\{b_j\}\), with both subsets nonempty and \(X\times Y\) contained in the cyclic incidence relation. Such subsets automatically form a downset and an upset. Denote their number by \(M_n\); then
\[
t_n=2J_n-1+M_n.
\]

**2. Exactly linear many two-sided cuts.** Fix nonempty \(X\) among the minimal vertices, and let \(c(X)\) be the number of maximal vertices lying above **every** element of \(X\). There are \(2^{c(X)}-1\) choices for nonempty \(Y\), so \(M_n=\sum_{X\ne\varnothing}(2^{c(X)}-1)\). For \(n\ge5\), a singleton lies below three maximal elements, contributing \(7\) choices per singleton and hence \(7n\) in total. A cyclic adjacent pair has two common upper neighbors, giving \(3n\). A cyclic distance-two pair has exactly one common upper neighbor, giving \(n\). A consecutive cyclic triple also has exactly one common upper neighbor, giving another \(n\). All other nonempty subsets have no common upper neighbor. Each of these four classes has exactly \(n\) subsets. Therefore
\[
\boxed{M_n=(7+3+1+1)n=12n.}
\]

**3. Weighted cyclic binary words count ideals.** Fix the subset of maximal elements \(b_j\) included in an ideal, and let \(z_j=1\) when it is included, zero otherwise. Its three lower neighbors are then forced into the ideal. Any minimal element with none of its three upper neighbors included remains optional. Consequently
\[
J_n=\sum_{z\in\{0,1\}^n}2^{q(z)},\qquad
q(z)=\#\{i:z_i=z_{i+1}=z_{i+2}=0\},
\]
with indices modulo \(n\). Use the four two-bit states in the order \(00,01,10,11\). A transition from state \((a,b)\) to \((b,c)\) has weight two when \((a,b,c)=(0,0,0)\), and weight one otherwise. The resulting matrix is
\[
T=\begin{pmatrix}2&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&1\end{pmatrix}.
\]
Every cyclic binary word has exactly one corresponding closed state walk with this weight, and vice versa. Hence \(J_n=\operatorname{tr}(T^n)\). Direct determinant expansion yields
\[
\det(\lambda I-T)=\lambda(\lambda-1)(\lambda^2-2\lambda-1).
\]
Therefore, since \(n\ge5\),
\[
\boxed{J_n=1+(1+\sqrt2)^n+(1-\sqrt2)^n.}
\]

**4. Assemble and take limits.** From steps 1–3,
\[
t_n=2J_n-1+12n=2\big((1+\sqrt2)^n+(1-\sqrt2)^n\big)+12n+1.
\]
Since \(|1-\sqrt2|<1\) and \(1+\sqrt2>1\), the indicated asymptotic equivalences follow. This proves the theorem. \(\square\)

## Verification
The standard-library checker `verify.py` independently enumerates all three-way comparison labels on the \(2n\) named parameters for \(n=5,6,7\), testing the transitivity conditions rather than the transfer-matrix formula; it obtains \(225,469,1041\). For every \(n=5,\ldots,14\), it independently enumerates upper-layer subsets to count ideals, lower-layer subsets to count two-sided cuts, and cyclic binary words to compute their weights. All agree with the asserted formulas. Execute `python3 verify.py`; recorded output is in `verification_output.txt`. Finite tests corroborate the all-\(n\) proof but cannot replace it.

## Relationship to prior work
Dolinka and Mašulović (arXiv:1009.2892, Lemma 3.3) already encode finite-poset one-point extensions by downsets and upsets; this general principle is not new. A public result entitled *Finite-parameter 1-type counting in the random poset is #P-complete* likewise gives general extension-type counting and its counting complexity; it does not evaluate the specified cyclic family. Previously studied graph-incidence posets and ordinary cycle crowns use two-element upper incidences, not the three-element incidences used here.

A public result entitled *A Pell–Lucas vertex law and a simplicity cutoff for cyclic three-term deformations* has a related Pell–Lucas trace in the vertex count of a cyclic Minkowski-sum polytope. That different invariant contains a weighted cyclic-word trace but does not state the present random-poset one-type count or the exact \(12n\) two-sided classification. Trotter's original crown dimension paper treats dimension of cyclic height-two posets, not this finite-parameter type spectrum. The known transfer-matrix and counting techniques are acknowledged; the proposed contribution is their complete evaluation for this specific natural family and the resulting linear-versus-exponential cut dichotomy.

## Limitations
This is a specialization to cyclic length-three hyperedge incidence, \(n\ge5\), and individually named parameters. It does not give a uniform closed form for every hyperedge length or every hypergraph incidence poset. The Pell–Lucas sequence itself is classical, and the same weighted-word trace arises in other enumeration problems. Although comparison searches found no previous statement of the specific one-point type count and exact two-sided cut law, equivalent coverage in older generalized-crown or enumerative literature is not excluded. The correctness proof is mathematical; the finite checker is a consistency test. No independent scientific audit has been performed.

## References
1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892 (first posted 15 September 2010), Lemma 3.3. https://arxiv.org/abs/1009.2892
2. W. T. Trotter Jr., *Dimension of the crown \(S_n^k\)*, Discrete Mathematics 8 (1974), 85–103. https://doi.org/10.1016/0012-365X(74)90113-7
3. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly archived mathematical result (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1
4. *A Pell–Lucas vertex law and a simplicity cutoff for cyclic three-term deformations*, publicly archived mathematical result (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-pell-lucas-vertex-law-and-a-simplicity-cutoff-for-cyclic-three--402774cb80ae
