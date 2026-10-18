# Mod-three selection rules and exact blocked-state polynomial for the three-spin Ising ring

## Finding

Consider the classical periodic three-spin Ising chain of length \(N\geq3\) with positive coupling \(J\). Write \(s_i\in\{-1,+1\}\), with indices modulo \(N\), and set
\[
H(s)=-J\sum_{i=0}^{N-1}s_{i-1}s_is_{i+1},\qquad
\tau_i=s_{i-1}s_is_{i+1},\qquad
k(s)=|\{i:\tau_i=-1\}|.
\]
A configuration is **strictly one-flip blocked** when flipping any single spin increases \(H\). Let its defect-count polynomial be
\[
B_N(z)=\sum_{s\,\mathrm{strictly\ blocked}}z^{k(s)}.
\]
Define the explicit matrix
\[
T(z)=\begin{pmatrix}0&1&0\\0&0&1\\z&0&1\end{pmatrix},
\qquad Q(z)=T(-z)^2T(z).
\]
The exact answer for **every** \(N\geq3\), including all periodic-size congruence classes, is
\[
\boxed{B_N(z)=
\begin{cases}
\operatorname{tr}(T(z)^N),&3\nmid N,\\
\operatorname{tr}(T(z)^N)+3\operatorname{tr}(Q(z)^{N/3}),&3\mid N.
\end{cases}}
\]
The correction is not an arbitrary counting convention: it is forced by which local defect words are realizable by periodic Ising spins.

In particular, every length not divisible by three has one ground state and precisely \(N\) one-defect strictly blocked states, while a length divisible by three has four ground states and **no one-defect spin configurations whatsoever**. When \(N=3m\geq6\), the first excited level has excess energy \(4J\), multiplicity \(2N(m-1)\), and all its states are strictly blocked; when \(3\nmid N\), the first excited level has excess energy \(2J\), multiplicity \(N\), and all its states are strictly blocked. At the exceptional length \(N=3\), the next energy level lies \(6J\) above the ground state and contains no blocked states.

The full (unrestricted) defect-energy density-of-states polynomial is also exactly
\[
\sum_{s\in\{-1,+1\}^N}z^{k(s)}=
\begin{cases}
(1+z)^N,&3\nmid N,\\
(1+z)^N+3(1+z)^{N/3}(1-z)^{2N/3},&3\mid N.
\end{cases}
\]
This last identity is a direct corollary of the same periodic-image selection rule; the main contribution is the blocked-state polynomial and its implications.

Let \(\lambda\) be the positive root of \(\lambda^3-\lambda^2-1=0\), and let \(p\) be the positive root of \(p^3-p-1=0\). The total number of blocked spin configurations has entropy density \(\log\lambda\) in all length classes. More sharply, along \(N=3m\),
\[
\boxed{B_{3m}(1)=\lambda^{3m}+3p^m+O(p^{-m/2})},
\qquad
\lambda\approx1.4655712319,\quad p\approx1.3247179572.
\]
Thus an exponentially growing, but subleading, commensurability term survives even though the leading blocked-state entropy is length-class independent.

## Assumptions and scope

There are exactly \(N\geq3\) labeled periodic sites. The Hamiltonian contains only consecutive three-spin ferromagnetic terms and has \(J>0\); there is no field, disorder, additional interaction, or kinetic constraint. Zero-temperature single-spin-flip dynamics is understood to assign positive rate to any strictly energy-decreasing move, and cannot leave a strictly blocked configuration. For the present odd-three-body Hamiltonian the single-spin energy change is never zero. Nothing is asserted about dynamical hitting probabilities of individual blocked configurations.

The polynomial counts spin configurations, not unconstrained formal \(\tau\)-strings. This distinction is essential on rings whose length is a multiple of three. Energy levels are \(-JN+2Jk\) with nonnegative integer \(k\); the phrase *first excited level* means the lowest strictly higher energy among all physical spin configurations.

## Proof

**1. Local blocked condition.** Flipping \(s_i\) changes exactly three interaction products. Hence
\[
H(s^{(i)})-H(s)=2J(\tau_{i-1}+\tau_i+\tau_{i+1}).
\]
The parenthesis is an odd integer. Its positivity is equivalent to having at most one negative \(\tau\) in every three consecutive cyclic positions. Equivalently, any two defect positions have cyclic separation at least three. This is the local metastability characterization already motivated by the original three-spin-chain study [1].

**2. Global periodic-spin compatibility.** Write \(s_i=(-1)^{b_i}\) and \(\tau_i=(-1)^{t_i}\), with bits in \(\mathbb F_2\). The map from spins to interaction variables is
\[
t_i=b_{i-1}+b_i+b_{i+1}\pmod2.
\]
Its homogeneous equation gives \(b_{i+1}=b_i+b_{i-1}\), whence \(b_{i+3}=b_i\). If \(3\nmid N\), a period-three solution satisfying the period-\(N\) boundary condition must be constant; the homogeneous equation then forces that constant to vanish. Thus the map is bijective.

If \(N=3m\), its kernel consists of the four three-periodic bit patterns specified by two free initial bits. Summing \(t_i\) over each residue class modulo three shows that each residue sum equals \(\sum_i b_i\pmod2\), because each spin bit occurs once in each residue-class sum. Therefore the necessary image restrictions are
\[
\sum_{i\equiv0\;(3)}t_i
\equiv\sum_{i\equiv1\;(3)}t_i
\equiv\sum_{i\equiv2\;(3)}t_i\pmod2.
\]
They are two independent linear constraints. Since the image has codimension two, they are also sufficient, and every allowed \(\tau\)-word has exactly four spin preimages. No other global constraints occur.

**3. Cyclic transfer matrix.** Use three memory states: immediately after a defect, one plus after a defect, and at least two pluses after a defect. An allowed plus advances the first two states or leaves the third fixed; a defect is permitted only from the third state and contributes weight \(z\). In this state order the transition matrix is precisely \(T(z)\). Each cyclic admissible defect word has one compatible closed state trajectory (including the defect-free word), so its generating polynomial is \(\operatorname{tr}(T(z)^N)\).

For \(N=3m\), let \(c_r\) denote the number of defects at indices congruent to \(r\) modulo three. The indicator that all three parities agree satisfies
\[
4\mathbf1_{c_0\equiv c_1\equiv c_2\;(2)}=
1+(-1)^{c_0+c_1}+(-1)^{c_0+c_2}+(-1)^{c_1+c_2}.
\]
The factor four on the left is exactly the spin preimage multiplicity. The first term gives \(\operatorname{tr}(T(z)^{3m})\); each other term gives \(\operatorname{tr}((T(-z)^2T(z))^m)\), since the three sign patterns are cyclic rotations. This proves the claimed polynomial.

**4. Low-energy selection rule.** For \(3\nmid N\), a single negative \(\tau\) is realizable in exactly one spin state at each of \(N\) possible positions, and is locally blocked. For \(3\mid N\), one negative cannot satisfy the three residue parities. With two defects, equality of the three parities is possible only when both positions belong to the same residue class. Writing \(N=3m\), this gives \(3\binom m2\) admissible defect pairs; all are separated by at least three sites and each has four spin preimages. Thus their total multiplicity is \(12\binom m2=2N(m-1)\). For \(N=3\), no such pair exists, and the only non-ground-state interaction word is all negative, with four preimages and energy excess \(6J\). This proves all stated gap and blocked-state facts.

**5. Full density of states and asymptotics.** Without the local blocked condition, the same parity projector can be summed over all independent defect bits. Its four character contributions are \((1+z)^N\) and three copies of \((1-z)^{2m}(1+z)^m\), proving the full energy polynomial.

At \(z=1\), the characteristic polynomials of \(T(1)\) and \(Q(1)\) are respectively \(u^3-u^2-1\) and \(u^3-u-1\). Each has one dominant positive real root, \(\lambda\) and \(p\). The other two roots of the first have modulus \(\lambda^{-1/2}\), and those of the second have modulus \(p^{-1/2}\). Taking traces of matrix powers gives
\[
\operatorname{tr}(T(1)^{3m})=\lambda^{3m}+O(\lambda^{-3m/2}),
\qquad
\operatorname{tr}(Q(1)^m)=p^m+O(p^{-m/2}).
\]
Since \(\lambda^{3}>p\), the displayed asymptotic and the common entropy density follow. For nonmultiples of three, the first trace alone gives the same entropy density.

## Verification

The included standalone \(\texttt{verify.py}\) directly evaluates the Hamiltonian and all single-spin energy changes on every spin configuration for \(3\le N\le15\), totaling 65,528 states. It independently compares the integer matrix-trace formulas against spin enumeration and, for \(16\le N\le24\), independent cyclic-defect subset enumeration. It also verifies the unrestricted energy polynomial and the first-excited multiplicities. The script passed all 201 integer polynomial evaluations and structural assertions when executed from the attached package. These finite checks corroborate, but do not replace, the all-size proof above.

## Relationship to prior work

Kisker, Rieger, and Schreckenberg [1] introduced this classical three-spin model, its \(\tau\)-variables and local metastability rule, and reported the asymptotic exponential metastable growth constant \(\lambda\). They explicitly assumed lengths divisible by three when discussing ground-state multiplicity. Those ingredients are acknowledged as prior results. The new finite-volume statement adds the **global periodic-image restriction**, the corrected all-size blocked-spin polynomial, the exact low-energy selection and multiplicity rules, and the explicit subleading plastic-constant term, none of which is stated in the material inspected from [1].

De Smedt, Godrèche, and Luck [2] analyze blocked-state statistics and energy distributions for different one-dimensional kinetically constrained spin models. Their transfer/counting methods motivate the comparison but their Hamiltonians and admissible spin sectors differ. Related work on one-dimensional random-bond Ising metastability [3] likewise concerns two-spin random interactions rather than the periodic three-spin map. These source comparisons do not establish global bibliographic uniqueness.

## Limitations

This is an exact equilibrium/state-space and strictly blocked-state census, not a derivation of trapping probabilities after a quench, lifetimes at positive temperature, transition rates, or any infinite-volume dynamical limit. The subleading asymptotic is for the a priori count of blocked configurations only. The lowest excited physical level at \(N=3\) is not blocked. Bibliographic searches cannot exclude an unindexed equivalent periodic-sector enumeration, and no independent scientific audit has been performed.

## References

[1] J. Kisker, H. Rieger, and M. Schreckenberg, *Escape from Metastability via Aging: Non-Equilibrium Dynamics in a One-Dimensional Ising Model*, arXiv:cond-mat/9408060, first public version 1994-08-19. https://arxiv.org/abs/cond-mat/9408060

[2] G. De Smedt, C. Godrèche, and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465, first public version 2002-02-26. https://arxiv.org/abs/cond-mat/0202465

[3] S. Masui, B. W. Southern, and A. E. Jacobs, *Metastable states of Ising spin glasses and random ferromagnets*, Physical Review B 39, 6925 (1989), DOI:10.1103/PhysRevB.39.6925. https://doi.org/10.1103/PhysRevB.39.6925
