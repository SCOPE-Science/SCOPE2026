# Exact relaxation shells and a logarithmic typical clock for cyclic Rule 178

## Finding

For elementary cellular automaton Rule 178 on every binary cyclic ring of length \(n\ge3\), the complete distribution of the *first time of entry into an eventual periodic orbit* has a closed finite formula. The maximal entry time is \(\lfloor(n-2)/2\rfloor\), but for a uniformly random configuration, the entry time is asymptotic in probability to \((\log_2 n)/2\). Exact terminal-shell and primitive-orbit counts are given below. This is a census of transient *entry times*, not merely a classification of eventual periods.

For the nonnegative integer \(t\), put \(C_n(t)=\#\{x:T(x)\le t\}\). Then

\[
C_n(t)=2+2\sum_{\substack{2\le k\le n\\ k\text{ even}}}\frac nk[z^{n-k}](1+z+\cdots+z^{2t+1})^k.
\]

The number entering precisely at time \(t\ge1\) is \(C_n(t)-C_n(t-1)\), and \(C_n(0)\) configurations are periodic from the start. The formula contains only integers, despite its convenient rational prefactors.

For \(n\ge4\), the maximal shell has exactly \(2n\) configurations when \(n\) is even and \(4n\) when \(n\) is odd. For \(n=3\) the system is already periodic on all eight configurations. If \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\), the exact number of *primitive two-cycle orbits* is

\[
B_n=\frac{L_n+2\cos(2\pi n/3)}2.
\]

The two uniform configurations are the only fixed points. Every other periodic configuration lies on one of these two-cycles.

## Assumptions and scope

Let \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\in\{0,1\}^n\) with all indices cyclic. Under *synchronous* updates, Rule 178 is the local Boolean rule

\[
(Fx)_i=\begin{cases}
 x_{i-1}\wedge x_{i+1},&x_i=1,\\
 x_{i-1}\vee x_{i+1},&x_i=0.
\end{cases}
\]

It is equivalently the binary two-threshold rule with up-threshold one and down-threshold three in the closed three-vertex neighborhood. Define \(T(x)\) as the least integer \(t\ge0\) for which \(F^t(x)\) is periodic under \(F\). The statements concern finite cyclic rings, not fixed-boundary paths, asynchronous updates, noise, or arbitrary graph topology. Uniform randomness means each of the \(2^n\) labelled configurations is equally likely.

## Proof

**1. Exact wall evolution.** Define \(d_i=x_i\oplus x_{i+1}\in\{0,1\}\) and \(a_i=d_{i-1}\vee d_i\). Direct substitution of all local Boolean possibilities gives \((Fx)_i=x_i\oplus a_i\). Consequently

\[
 d'_i=d_i\oplus(a_i\oplus a_{i+1}).
\]

If \(d_i=1\), then \(a_i=a_{i+1}=1\), hence \(d'_i=1\). If \(d_i=0\), then \(a_i=d_{i-1}\) and \(a_{i+1}=d_{i+1}\), hence \(d'_i=d_{i-1}\oplus d_{i+1}\). In other words, walls persist, each positive-length interval of zero walls is filled from both ends, and a single zero sandwiched between two walls remains a zero. A zero gap of initial length \(g\) requires exactly \(\lfloor g/2\rfloor\) updates to become one of the stable gaps of size zero or one.

The cyclic parity condition \(\bigoplus_i d_i=0\) implies that every nonconstant configuration has a positive *even* number of walls. Write their cyclic positions in increasing circular order, and let \(g_j\) be the number of zeros strictly between wall \(j\) and its successor, for \(j=1,\dots,k\), with \(\sum_j g_j=n-k\). After exactly \(\max_j\lfloor g_j/2\rfloor\) updates, every remaining zero is isolated and \(d\) is fixed. Before this time some gap contains two adjacent zeros and at least one new wall appears, so the time is minimal. Once the wall word is fixed and nonzero, each vertex sees at least one adjacent wall; therefore every vertex flips, \(F(x)=\bar x\), and the orbit has period two. Zero walls correspond to the two fixed uniform configurations. This proves the deterministic entry-time formula, the period classification, and the bound \(T\le\lfloor(n-2)/2\rfloor\). A wall pair bounding one gap of length \(n-2\) attains the bound.

**2. Enumerating every entry-time shell.** A configuration has entry time at most \(t\) if and only if it has no walls or every zero gap has length at most \(2t+1\). With exactly \(k>0\) walls, a rooted wall word is specified by a chosen marked wall position (\(n\) choices) and a cyclic ordered \(k\)-tuple \((g_1,\ldots,g_k)\) of nonnegative gaps summing to \(n-k\) and bounded above by \(2t+1\). Each unrooted labelled wall word is counted exactly \(k\) times by marking one of its walls. Each even-parity wall word lifts to precisely two binary configurations, determined by the arbitrary value of \(x_0\). There are \([z^{n-k}](1+z+\cdots+z^{2t+1})^k\) admissible gap tuples. Adding the two constant words proves the displayed formula.

The coefficient can be computed with ordinary integer binomial coefficients by inclusion–exclusion:

\[
[z^m](1+\cdots+z^w)^k=\sum_{j=0}^{\lfloor m/(w+1)\rfloor}(-1)^j\binom{k}{j}\binom{m-j(w+1)+k-1}{k-1}.
\]

Set \(m=n-k\), \(w=2t+1\); terms with \(j>k\) are zero. The formula is valid also for \(n=3\), where every configuration is immediately periodic.

**3. The sharp terminal shell.** For \(n\ge4\), the maximum \(\lfloor(n-2)/2\rfloor\) can occur only with two walls, as four or more walls leave at most \(n-4\) zeros in any gap. For even \(n\), the unique maximizing gap multiset is \(\{n-2,0\}\), giving \(n\) labelled wall words and, after the two lifts, \(2n\) configurations. For odd \(n\ge5\), the possible gap multisets are \(\{n-2,0\}\) and \(\{n-3,1\}\), giving \(2n\) wall words and \(4n\) binary configurations. (For \(n=4\) this gives the even count as stated.)

**4. Periodic orbit census.** Wall configurations with no adjacent zeros are precisely those periodic from time zero, apart from the constant configurations. Give each one-wall digit fugacity \(u\) and use the transfer matrix \(M(u)=\left(\begin{smallmatrix}0&u\\1&u\end{smallmatrix}\right)\), whose entry for a transition from preceding wall digit to current digit vanishes only for \(0\to0\). The trace \(\operatorname{tr}M(u)^n\) counts cyclic admissible wall words by their number of ones. Projecting to even wall parity yields half the sum of traces at \(u=1\) and \(u=-1\). The first trace is the Lucas number \(L_n\); the second equals \(2\cos(2\pi n/3)\), since the two eigenvalues are primitive cube roots of unity. Every admissible wall word lifts to two configurations and each nonconstant periodic orbit contains two configurations, so their factors cancel and \(B_n\) follows.

**5. Logarithmic typical versus linear maximal time.** Under a uniformly chosen binary configuration, the wall vector \(d\) is uniformly distributed among length-\(n\) even-parity bit strings. Any selection of at most \(n-1\) wall coordinates is therefore independent and fair. If \(T_n\ge t\), there must exist a cyclic block of \(2t\) zero wall coordinates (except the all-zero vector, which contributes \(T_n=0\), so omitting it only strengthens the bound). A union bound gives \(\Pr(T_n\ge t)\le n2^{-2t}\). Taking \(t=\lceil(1/2+\varepsilon)\log_2 n\rceil\) makes this tend to zero. Conversely, choose \(r=\lfloor(n-1)/(2t)\rfloor\) disjoint length-\(2t\) windows inside the first \(n-1\) wall coordinates. Their all-zero events are independent, each with probability \(2^{-2t}\). With \(t=\lfloor(1/2-\varepsilon)\log_2 n\rfloor\), \(r2^{-2t}\to\infty\); hence the chance that none is zero is at most \(\exp(-r2^{-2t})\to0\). Any such all-zero window, except the exponentially unlikely all-zero wall word, forces \(T_n\ge t\). Thus \(T_n/\log_2 n\to1/2\) in probability for the uniform initial distribution.

## Verification

The accompanying Python standard-library program `verify_rule178.py` independently constructs trajectories of the local rule until a repeated state occurs. It checks the domain-gap first-entry formula, the exact cumulative-shell formula, the terminal-shell counts, the Lucas-periodic census, and the assertion that only the two constant points are fixed, **exhaustively for \(3\le n\le17\)**, totaling 262,136 labelled initial configurations. The recorded output is `verification_output.txt`, ending with `RULE178_ALL_CHECKS_PASSED`. This finite independent test corroborates, but does not replace, the all-size mathematical proof above. Reproduce with `python3 verify_rule178.py` from the directory containing the code.

## Relationship to prior work

Inokuchi and Sato (2000) classify limit cycles and transient lengths for *fixed-boundary* threshold cellular automata, including Rule 232, not the cyclic Rule 178 entry-time distribution. Kuhlman, Mortveit, Murrugarra and Kumar (2011) establish a general fixed/two-cycle restriction for synchronous symmetric bi-threshold systems; that restriction is not asserted as new here. Betel (2012, Theorem 59) proves a two-step conjugacy between Rule 178 and majority Rule 232 for even ring sizes; it does not state cyclic exact first-entry shell counts for arbitrary sizes. Fukś supplies a general Rule 178 iterate description. Donoso Leiva and coauthors (2023) prove relative-wall properties and the maximal period two under parallel update, while contrasting asynchronous schedules. A separate openly available Rule 178 domain-wall analysis identifies persistent walls and inward invasion of zero gaps; these qualitative wall phenomena are therefore prior work. Muñoz and Nuño (2026) analyze a stochastic interpolation including Rule 178, with exact finite-volume results for small rings. These sources inform the definitions and approach but the checked statements do not imply the complete labelled cyclic entry-time census, its two parity-dependent terminal shells, and the typical logarithmic scaling without further counting and probability arguments.

## Limitations

This theorem concerns only fully synchronous binary Rule 178 on a simple labelled cycle of length at least three. In particular, the asymptotic is a convergence-in-probability law, not a fluctuation limit or an explicit finite-\(n\) expectation. The novelty comparison is bounded by the accessible inspected literature and research indices. Known local solubility, wall-front dynamics, eventual period bounds and the even-size Rule 232 conjugacy are **not** claimed as new. Prior results might imply pieces through additional derivations; no assertion of exhaustive historical uniqueness or independent validation is made.

## References

- S. Inokuchi and T. Sato, *On limit cycles and transient lengths of cellular automata with threshold rules*, Bulletin of Informatics and Cybernetics 32 (2000), DOI: 10.5109/13492. https://doi.org/10.5109/13492
- C. Kuhlman, H. S. Mortveit, D. Murrugarra and S. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974 (first version 2011-08-15). https://arxiv.org/abs/1108.2974
- H. Betel, *Properties and Behaviours of Fuzzy Cellular Automata* (2012), section 8.5, Theorem 59. https://ruor.uottawa.ca/bitstreams/400aaa1a-e55d-4708-abf4-32eb7489579d/download
- H. Fukś, *Solvable Cellular Automata*, Rule 178 iterate entry. https://lie.ac.brocku.ca/~hfuks/solvableca.html
- I. Donoso Leiva, E. Goles, M. Ríos Wilson and S. Sené, *ECA asymptotic (a)synchronism sensitivity and complexity*, arXiv:2312.15078 (2023), section 3.2 and Theorem 7. https://arxiv.org/abs/2312.15078
- D. Youvan, *Cellular Algebraic Abiogenesis: Consolidated Scientific Report*, discussion of Rule 178 domain-wall propagation. https://github.com/DougYouvan/Cellular-Algebraic-Abiogenesis
- F. J. Muñoz and L. Nuño, probabilistic interpolation of Rules 23, 77, 178 and 232, arXiv:2603.27799 (2026), section 2.3. https://arxiv.org/abs/2603.27799
