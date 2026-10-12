# Sharp odd-copy activation law for passive equally spaced qutrits

## Finding
Let a three-level system have equally spaced nondegenerate energies \(0,\varepsilon,2\varepsilon\), with \(\varepsilon>0\), and let its initial state be diagonal with strictly positive populations \(p_0\ge p_1\ge p_2>0\). Put
\[
a=\log(p_0/p_1),\qquad b=\log(p_1/p_2),\qquad g_n=\lfloor(n-1)/2\rfloor.
\]
For every integer \(n\ge1\), the product state \(\rho^{\otimes n}\) is passive under *arbitrary global unitary operations* with respect to the noninteracting sum Hamiltonian if and only if
\[
\boxed{g_n\,|a-b|\le\min\{a,b\}.}
\]
If \(a=b\), the state is Gibbs and remains passive for every finite \(n\). Otherwise, the *first* copy number at which global unitary work extraction is possible is exactly
\[
\boxed{n_{\mathrm{act}}=2\left\lfloor\frac{\min\{a,b\}}{|a-b|}\right\rfloor+3.}
\]
In particular, first activation always occurs at an odd copy number, and adding one copy to an odd number does not change the passivity decision. All inequalities include their equality boundaries: a zero energy-population inversion does not yield strictly positive work. When the two strictly positive slopes approach a common finite value \(a_0=b_0>0\) with \(\delta=|a-b|	o0^+\), the onset count obeys the sharp staircase asymptotic \(n_{\mathrm{act}}=2\min\{a,b\}/\delta+O(1)\), exhibiting the divergence in finite-copy work-extraction resources near thermal populations.

An equivalent exact-integer form useful for rational populations is as follows. Writing \(g=g_n\), when \(p_0p_2<p_1^2\), passivity is equivalent to \(p_0^{g+1}p_2^g\ge p_1^{2g+1}\); when \(p_0p_2>p_1^2\), it is equivalent to \(p_1^{2g+1}\ge p_0^g p_2^{g+1}\); at \(p_0p_2=p_1^2\) it holds for all copies.

## Assumptions and scope
Passivity means that for *every* unitary \(U\) acting jointly on all copies,
\[
\operatorname{Tr}[U\rho^{\otimes n}U^\dagger H^{(n)}]\ge\operatorname{Tr}[\rho^{\otimes n}H^{(n)}],\qquad H^{(n)}=\sum_{j=1}^{n}H_j.
\]
No ancillary reservoir, catalyst, or work-storage model is assumed. There is no restriction on the implementing global unitary. Degenerate *total-energy* shells are allowed; they arise automatically although the single-system spectrum is nondegenerate. All population ratios are positive so that logarithms exist. No claim is made for rank-deficient states, unequal energy gaps, interacting copies, or coherence in the energy eigenbasis.

## Proof
**Population ordering.** For a diagonal density matrix, passivity is equivalent to the statement that every population in a lower-energy shell is at least every population in a higher-energy shell. Necessity follows by swapping any inverted pair of energy eigenvectors, which strictly decreases mean energy. Sufficiency follows from the rearrangement inequality: a joint unitary yields a doubly stochastic mixing of populations, and the initial matching of decreasing populations with increasing energies minimizes the mean. It is enough to compare consecutive energy shells, because these comparisons imply all more distant comparisons by transitivity.

**Exact shells.** Fix an integer \(n\ge1\). A product basis string with total energy \(E\varepsilon\), \(0\le E\le2n\), contains \(j\) symbols at the top level, \(E-2j\) middle-level symbols, and \(n-E+j\) ground-level symbols. Its feasible top-level count obeys
\[
L_n(E)=\max\{0,E-n\}\le j\le U_n(E)=\lfloor E/2\rfloor.
\]
Relative to \(p_0^n\), its negative logarithmic population is
\[
C(E,j)=aE+(b-a)j.
\]
A consecutive-shell passivity comparison requires the minimum cost among states in the higher-energy shell \(E+1\) to be at least the maximum cost in shell \(E\).

**Two slope orders.** If \(b\ge a\), \(C(E,j)\) increases with \(j\); the condition for each \(E\in\{0,\ldots,2n-1\}\) is therefore
\[
a\ge(b-a)\,[U_n(E)-L_n(E+1)].
\]
The maximum of the bracket over these integer energies is exactly \(g_n\). For odd \(n=2r+1\), it is attained at \(E=2r\) and equals \(r\); for even \(n=2r\), it equals \(r-1\), attained at \(E=2r-1\) and \(E=2r\). This proves the condition \(a\ge g_n(b-a)\).

If \(a\ge b\), the cost decreases with \(j\); consecutive-shell ordering is instead equivalent to
\[
a\ge(a-b)\,[U_n(E+1)-L_n(E)].
\]
The largest bracket is \(g_n+1\): it is attained at \(E=n\) for odd \(n\), or \(E=n-1\) for even \(n\). Consequently this is equivalent to \(b\ge g_n(a-b)\). Combining the two cases gives the asserted unified inequality, including \(a=b\) and zero logarithmic slopes. This establishes necessity and sufficiency for all integers and boundary values in the stated domain.

**Sharp activation and explicit swaps.** For \(a\ne b\), define \(q=\min\{a,b\}/|a-b|\). The largest admissible integer \(g_n\) is \(\lfloor q\rfloor\). The smallest \(n\) with \(g_n>q\) is \(n=2\lfloor q\rfloor+3\), which is odd. Since \(g_{2r+1}=g_{2r+2}=r\), the consecutive odd/even copy decision agrees.

The failure always has a constructive witness. At the first active size \(n=2r+1\), with \(r=\lfloor q\rfloor+1\), if \(b>a\), compare the lower-energy product basis string containing \(r\) top excitations and \(r+1\) ground levels (energy \(2r\varepsilon\), population \(p_2^rp_0^{r+1}\)) with the higher-energy string of \(2r+1\) middle levels (energy \((2r+1)\varepsilon\), population \(p_1^{2r+1}\)). The second population is strictly larger by the failed inequality. If \(a>b\), compare the lower-energy all-middle string (population \(p_1^{2r+1}\), energy \((2r+1)\varepsilon\)) with the higher-energy string containing \(r+1\) top levels and \(r\) ground levels (population \(p_2^{r+1}p_0^r\), energy \((2r+2)\varepsilon\)); again the higher-energy population is strictly larger. Swapping either pair decreases mean energy by exactly \(\varepsilon\) times their positive population difference, providing an explicit work-extraction unitary without needing a numerical global optimization.

As a rational example, take \((p_0,p_1,p_2)=(8,2,1)/11\). Then \(a=\log4\), \(b=\log2\), and the first activation requires five copies. At five copies, the energy-\(5\varepsilon\) all-middle string has population \(32/11^5\), while a string with three top excitations and two ground levels at energy \(6\varepsilon\) has population \(64/11^5\). Exchanging their populations extracts \(32\varepsilon/11^5\) of work.

## Verification
The accompanying `verify.py` enumerates every product-basis population for all \(n\in\{1,\ldots,9\}\) and every ordered positive integer profile \(1\le p_2\le p_1\le p_0\le11\). There are 2,574 state-copy combinations. It checks the resulting pairwise adjacent-energy population inequalities against the theorem using only exact integer arithmetic. It separately enumerates the two required shell-boundary maxima through \(n=120\), checks both onset examples, and checks Gibbs profiles. A successful run prints `VERIFY_OK 2574 exact product-spectrum tests; 120 shell-extremum tests`.

These finite checks are corroboration. The proof of the universal quantified statement is the analytic integer-shell extremization above; finite enumeration alone would not establish the theorem.

## Relationship to prior work
The multilevel-work context is motivated by Vetrano, Giovannetti, and Cavina, arXiv:2605.27369v1, which defines qudit-channel ergotropic performance, treats a qutrit explicitly, and considers asymptotically many copies. Their finite-noise-channel optimization and asymptotic capacity results do not state the present closed activation-copy criterion for fixed diagonal qutrit products in the materially inspected sections (Secs. III–V and the relevant appendix).

Koukoulekidis, Alexander, Hebdige, and Jennings, arXiv:1912.07968v3, Sec. 3.3, Lemma 7, give a general *algorithmic* characterization of finite-copy passivity by total ordering of the additive energy–surprisal ensemble; their Fig. 3 illustrates qutrit copies. That powerful general equivalence is prior work, not claimed here. The additional statement here is an evaluated, all-parameter **closed** integer threshold with odd-only first activation, an exact shell-extremum proof, and attaining swaps; it avoids a copy-by-copy ordering search. Salvia and Giovannetti, arXiv:1912.02099v4, Proposition 1, give necessary three-level population inequalities, while Sec. 5 treats the stronger property of structural stability. In the equally spaced odd-copy case, their necessary inequalities are closely related to those used here; the present proof supplies the full necessary-and-sufficient reduction and first-copy expression for ordinary passivity, with no structural-stability hypothesis. Earlier virtual-temperature results establish complete passivity of Gibbs states, not a closed smallest finite activation number in this family.

## Limitations
The universal claim is confined to positive diagonal populations and the equally spaced noninteracting qutrit spectrum. It gives the **first positive-work copy count**, not the full ergotropy magnitude or the least-depth feasible control circuit. The explicit swap generally need not be globally ergotropy-maximizing. The general additive-ensemble criterion of arXiv:1912.07968 already gives an algorithm for deciding finite-copy passivity, so the specific novelty is the evaluated sharp symbolic phase diagram rather than the general passivity principle. A differently indexed derivation of this special closed form could still exist in prior literature.

## References
1. V. Vetrano, V. Giovannetti, and V. Cavina, *Generalized multilevel amplitude damping channels and their thermodynamic performances*, arXiv:2605.27369v1 (first public 2026-05-26), https://arxiv.org/abs/2605.27369 .
2. N. Koukoulekidis, R. Alexander, T. Hebdige, and D. Jennings, *The geometry of passivity for quantum systems and a novel elementary derivation of the Gibbs state*, arXiv:1912.07968v3, https://arxiv.org/abs/1912.07968 .
3. R. Salvia and V. Giovannetti, *Energy upper bound for structurally stable N-passive states*, arXiv:1912.02099v4, https://arxiv.org/abs/1912.02099 .
4. P. Skrzypczyk, R. Silva, and N. Brunner, *Passivity, complete passivity, and virtual temperatures*, Phys. Rev. E 91, 052133 (2015), https://doi.org/10.1103/PhysRevE.91.052133 .
