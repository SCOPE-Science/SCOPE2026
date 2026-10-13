# Characteristic polynomial and uniform non-freeness of the cyclic four-cycle arrangement

## Finding
For every integer \(m\ge 2\), let \(\mu_m\subset\mathbb C^*\) be the group of \(m\)-th roots of unity. Let \(\mathcal A_m\) be the central arrangement in \(\mathbb C^4\) with defining polynomial
\[
Q_m=\prod_{i\in\{0,1\}}\prod_{j\in\{2,3\}}(x_i^m-x_j^m),
\]
and put \(U_m=\mathbb P^3_{\mathbb C}\setminus V(Q_m)\).
Its characteristic polynomial is
\[
\chi_{\mathcal A_m}(T)=(T-1)\bigl[T^3+(1-4m)T^2+(6m^2-3)T-3m^3-2m^2+4m+1\bigr].
\]
The integral Betti numbers of the projective complement are encoded by
\[
\sum_{i\ge0}b_i(U_m)t^i=1+(4m-1)t+(6m^2-3)t^2+(3m^3+2m^2-4m-1)t^3.
\]
Moreover, \(\mathcal A_m\) is not free for **any** \(m\ge2\). In particular, for the twelve-hyperplane arrangement giving the Michałek–Pokora counterexample to the refined Purdy inequality (\(m=3\)),
\[
\chi_{\mathcal A_3}(T)=(T-1)(T^3-11T^2+51T-86),\qquad (b_0,b_1,b_2,b_3)(U_3)=(1,11,51,86).
\]

## Assumptions and scope
All arrangements and Betti groups are over \(\mathbb C\). The integer \(m\) ranges over \(m\ge2\), and the four labeled coordinates and bipartition \(\{0,1\}\sqcup\{2,3\}\) are fixed. The arrangement is essential because distinct members of \(\mu_m\) force every coordinate to vanish in the total intersection. The displayed Betti numbers are ranks of singular integral cohomology (which is torsion-free for complex hyperplane-arrangement complements).

## Proof
**Finite-field count.** Fix \(m\ge2\). For every sufficiently large prime \(q\equiv1\pmod m\), outside the finite set where an intersection-lattice determinant could vanish after reduction, identify \(\mu_m\) with the distinct \(m\)-th roots in \(\mathbb F_q\). Such primes are infinite by Dirichlet's theorem. The reduced arrangement has the same intersection lattice as the complex arrangement: for fixed \(m\), all nonzero minors of its cyclotomic coefficient matrices are algebraic integers, and only finitely many rational primes can annihilate one. The finite-field method therefore identifies \(\chi_{\mathcal A_m}(q)\) with the number of complement points in \(\mathbb F_q^4\).

For a coordinate \(z\in\mathbb F_q\), the value \(z^m\) is either zero (one preimage) or one of \(k=(q-1)/m\) nonzero values (each with \(m\) preimages). Choose the values of \(x_2^m,x_3^m\), then choose \(x_0,x_1\) whose \(m\)-th powers avoid both selected values. Four disjoint cases give:

1. Both right-hand values zero: \((q-1)^2\).
2. Both equal and nonzero: \(m(q-1)(q-m)^2\).
3. Exactly one zero: \(2(q-1)(q-m-1)^2\).
4. Distinct and nonzero: \((q-1)(q-1-m)(q-2m)^2\).

Their sum is
\[
(q-1)\bigl[q^3+(1-4m)q^2+(6m^2-3)q-3m^3-2m^2+4m+1\bigr].
\]
Equality at infinitely many primes \(q\) proves the polynomial identity over \(\mathbb Z[T]\) for each fixed \(m\).

**Cohomology.** The Orlik–Solomon characteristic-polynomial identity gives the Poincaré polynomial of the central complement as \(t^4\chi_{\mathcal A_m}(-1/t)\). Because one defining linear form is nowhere zero on the complement, projectivization identifies that complement with \(\mathbb C^*\times U_m\). Dividing by \(1+t\) yields the asserted projective polynomial, with no integral torsion.

**Non-freeness.** Set \(F_m(T)=\chi_{\mathcal A_m}(T)/(T-1)\). Its discriminant is
\[
\operatorname{Disc}(F_m)=-3m^6-8m^5-32m^4+16m^3+224m^2-256m+32.
\]
Writing \(n=m-2\ge0\) transforms this into
\[
-\bigl(3n^6+44n^5+292n^4+1040n^3+1808n^2+1408n+416\bigr)<0.
\]
Thus \(F_m\) has a nonreal conjugate pair and cannot be a product of integer linear factors. Terao's factorization theorem would force such a splitting if \(\mathcal A_m\) were free. Therefore none of these arrangements is free.

## Verification
The accompanying standard-library checker `check.py` performs direct \(\mathbb F_q^4\) complement enumerations for \((m,q)=(2,5),(2,11),(3,7),(3,13),(4,13)\), checks their agreement with the formula, and checks the discriminant shift identity for \(2\le m<300\). Actual execution returned `GAIN_FOUR_CYCLE_CHARACTERISTIC_CHECK_OK`. These finite tests corroborate, but do not replace, the infinite finite-field and discriminant arguments above.

## Relationship to prior work
Michałek and Pokora (arXiv:2607.08463, first posted July 9, 2026) construct the root-of-unity four-cycle family, enumerate incidence flats, and identify \(m=3\) as the unique member violating the refined Purdy inequality. Their treatment does not state this characteristic polynomial, the projective-complement Betti numbers, or uniform non-freeness.

Berthomé, Cordovil, Forge, Ventos, and Zaslavsky give a universal gain-graph chromatic-polynomial calculation in their 2009 article (notably their general subset expansion, Equation (5.5)). It supplies a broad *method* that can be specialized to this family. The finding here is the explicit closed evaluation, its uniform negative-discriminant consequence, and the resulting complement topology; the universal gain-graph formula itself is not new. Suyama–Torielli–Tsujie's 2024 gain-graph freeness results primarily treat bias arrangements with all coordinate hyperplanes present, rather than this exact subarrangement without those hyperplanes. The 2026 work on affine/additive gain-graph deformations proves four-cycle non-freeness in a different arrangement class.

## Limitations
No classification of the fundamental groups, cohomology rings, or mixed Hodge structures is asserted. The basic finite-field method, Orlik–Solomon theory, Terao's factorization theorem, and general gain-graph chromatic formulas are established earlier results. It is possible that the particular closed evaluation is implicit in specialized gain-graph literature not found in the comparisons; the explicit evaluation, rather than an abstract general computation algorithm, is the claimed increment. The freeness statement is only for \(m\ge2\) with the specified four bipartite coordinate pairs.

## References
- M. Michałek and P. Pokora, *A counterexample to Purdy's inequality for hyperplane arrangements in projective three-space*, arXiv:2607.08463v1 (2026-07-09), https://arxiv.org/abs/2607.08463.
- P. Berthomé, R. Cordovil, D. Forge, V. Ventos, and T. Zaslavsky, *An Elementary Chromatic Reduction for Gain Graphs and Special Hyperplane Arrangements*, Electronic Journal of Combinatorics 16 (2009), R121, https://arxiv.org/abs/1001.4216.
- D. Suyama, M. Torielli, and S. Tsujie, *Freeness of Hyperplane Arrangements Associated with Gain Graphs*, arXiv:2403.08304 (2024), https://arxiv.org/abs/2403.08304.
- *Nice Partitions, Supersolvability, and Freeness in Deformations of Graphic Arrangements*, arXiv:2609.39407v1 (2026), https://arxiv.org/html/2609.39407v1.
- P. Orlik and H. Terao, *Arrangements of Hyperplanes*, Springer (1992), standard Orlik–Solomon and factorization theorems.
