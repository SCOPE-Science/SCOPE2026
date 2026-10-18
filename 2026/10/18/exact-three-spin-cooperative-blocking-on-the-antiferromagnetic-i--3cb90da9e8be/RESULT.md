# Exact three-spin cooperative blocking on the antiferromagnetic Ising wheel

## Finding

For every integer \(n\ge5\) and coupling \(J>0\), place Ising spins on the wheel consisting of a rim cycle \(C_n\) and one hub joined to every rim vertex. All \(2n\) edges carry the same antiferromagnetic coupling. Define \(r\)-spin stability to mean that **no simultaneous flip of any nonempty set of at most \(r\) distinct spins strictly decreases energy**; neutral moves are allowed. Let \(Z_n^{(r)}(y)\) count labeled stable configurations with weight \(y^m\), where \(m\) is the number of rim spins aligned with the hub (equivalently, the energy is \(-2Jm\) on such configurations).

The first two stability levels coincide, but the third is strictly smaller for infinitely many sizes. Precisely, with \(j=n-2m\),

\[
Z_n^{(1)}(y)=Z_n^{(2)}(y)=2\!\sum_{\lceil n/3\rceil\le m\le\lfloor n/2\rfloor}
\frac{n}{m}\binom{m}{j}y^m,
\]

and

\[
\boxed{Z_n^{(3)}(y)=2\!\sum_{\substack{\lceil n/3\rceil\le m\le\lfloor n/2\rfloor\\0\le j=n-2m\le\lfloor m/2\rfloor}}
\frac{n}{m-j}\binom{m-j}{j}y^m.}
\]

All coefficients shown are integers. In particular, the complete ordinary generating functions, interpreted for coefficients of rim length \(n\ge5\), are

\[
\sum_n Z_n^{(1)}(y)z^n=-2z\,\partial_z\log(1-yz^2-yz^3),
\qquad
\sum_n Z_n^{(3)}(y)z^n=-2z\,\partial_z\log(1-yz^2-y^2z^5).
\]

The second expression also gives the formal counts for lengths other than \(n\ge5\); those artificial small-length coefficients are not assertions about degenerate wheel graphs. Let \(\alpha>1\) be the real root of \(\alpha^3-\alpha-1=0\), and let \(\beta>1\) be the real root of \(\beta^5-\beta^3-1=0\). Then

\[
\lim_{n\to\infty}\frac{\log Z_n^{(1)}(1)}n
=\lim_{n\to\infty}\frac{\log Z_n^{(2)}(1)}n=\log\alpha
=0.281199574322962\ldots,
\]

whereas

\[
\boxed{\lim_{n\to\infty}\frac{\log Z_n^{(3)}(1)}n=\log\beta=0.212289420497203\ldots.}
\]

Thus the uniformly sampled one-spin minima surviving every three-spin move constitute an exponentially vanishing fraction, with exponent

\[
\lim_{n\to\infty}-\frac1n\log\frac{Z_n^{(3)}(1)}{Z_n^{(1)}(1)}
=\log(\alpha/\beta)=0.068910153825759\ldots.
\]

The new structural statement is the **three-spin obstruction** and its exact energy-resolved and exponential census. The one-spin Perrin-type cyclic-word count is a baseline, not an independent novelty assertion.

## Assumptions and scope

The graph has vertices \(h,0,\ldots,n-1\), rim edges \(\{i,i+1\pmod n\}\), and spokes \(\{h,i\}\). Every spin \(s_v\) lies in \(\{-1,+1\}\); the Hamiltonian is

\[
H(s)=J\left(\sum_{i=0}^{n-1}s_is_{i+1\pmod n}+s_h\sum_{i=0}^{n-1}s_i\right),\qquad J>0.
\]

All spin subsets of size at most three are admitted, whether or not their induced graph is connected. Spins are labeled, and global spin reversal counts as a distinct configuration. No external field, disorder, uneven coupling, or stochastic quench law is assumed. A neutral energy increment of zero does not violate stability. Only the exact finite graph, fixed \(J>0\), and its \(n\to\infty\) counting limit are addressed.

Call a rim spin \(A\) when it agrees with the hub, and \(B\) otherwise. A cyclic word is written in those relative symbols, even when the hub is negative. A \(B\)-run is maximal cyclically.

## Proof

**Step 1: complete one-spin classification.** For any vertex, flipping a single spin changes the energy by \(-2Js_v\sum_{u\sim v}s_u\). A rim \(A\) has one agreeing neighbor (the hub), so it is stable exactly when both rim neighbors are \(B\). A rim \(B\) has an opposing hub, so it is stable exactly when at least one rim neighbor is \(A\). Consequently the rim word must avoid both \(AA\) and \(BBB\), and these conditions suffice for all rim vertices. They also guarantee the hub is stable: if \(m\) denotes the number of \(A\) vertices, then \(m\le n/2\), so its flip has cost \(2J(n-2m)\ge0\). Every word is uniquely decomposed cyclically into \(m\) blocks \(AB\) or \(ABB\). Let \(j\) be the number of long blocks \(ABB\). Thus \(n=2m+j\), with \(0\le j\le m\).

**Step 2: the complete cooperative flip test.** In a one-spin-stable configuration, divide each single-spin increment by \(J\). The hub increment is \(2j\); an \(A\) has increment \(2\); an isolated \(B\) has increment \(6\); and a \(B\) within a run \(BB\) has increment \(2\). For a simultaneous flip of a set \(S\), counting its internal edges once rather than twice gives the exact identity

\[
\Delta H(S)=\sum_{v\in S}\Delta H(\{v\})+4J\sum_{\{u,v\}\in E[S]}s_us_v.
\]

For two spins the only corrections come from adjacent pairs. Rim pairs \(AB\) have normalized cost \(0\) or \(4\), rim pairs \(BB\) have cost \(8\), hub–\(A\) pairs have cost \(2j+6\), and hub–\(B\) pairs have cost \(2j+2\) (isolated \(B\)) or \(2j-2\) (\(B\) in \(BB\)); the last is nonnegative because such a run forces \(j\ge1\). Nonadjacent pairs have the sum of two nonnegative single costs. Hence every one-spin-stable configuration is two-spin-stable.

For three rim spins, disconnected induced subgraphs do not cause energy decreases, since their components of sizes one or two have nonnegative costs. A connected three-vertex induced path along the rim has, up to reversal, one of the forms \(ABA\), \(BAB\), and \(ABB\) (or \(BBA\)); \(AAA\), \(AAB\), and \(BBB\) are impossible. The normalized costs are respectively \(2\), at least \(-2\), and \(6\). The \(BAB\) cost equals \(-2\) **if and only if both outer \(B\) spins are members of distinct runs \(BB\)**; otherwise it is at least \(2\). This is exactly the five-vertex cyclic motif \(BBABB\).

For a three-spin set containing the hub, the other two rim spins are either adjacent or not. If adjacent, their types are \(AB\) or \(BB\), and the normalized cost is nonnegative (respectively \(2j+(0\text{ or }4)\) and \(2j\)). If nonadjacent, the \(AA\) and \(AB\) cases have positive cost. For \(BB\), both isolated \(B\) spins give cost \(2j+4\); one isolated and one long-run \(B\) give \(2j\); and two long-run \(B\) spins give \(2j-4\). In the final case nonadjacency forces them to belong to distinct long runs, hence \(j\ge2\), so the cost is still nonnegative. This exhausts every three-spin subset for \(n\ge5\). Therefore a one-spin-stable configuration is three-spin-stable precisely when no two cyclically consecutive \(B\)-runs both have length two.

**Step 3: exact labeled enumeration.** Fix the hub sign (two choices). For \(m\) \(A\)-spins and \(j\) long gaps, the number of ordinary ordered cyclic gap strings is \(\binom mj\); rooting a labeled rim at a distinguished \(A\) gives a factor \(n/m\). This yields the baseline polynomial. For three-spin stability, the long gaps form an independent set of size \(j\) on the cycle of \(m\) gap positions. For \(m\ge2\), the number of such cyclic selections is \(\frac{m}{m-j}\binom{m-j}{j}\), nonzero only for \(2j\le m\). Multiplying by \(n/m\) and by two hub signs gives the boxed polynomial.

For completeness, set \(a=yz^2\) and \(b=yz^3\). Ordinary ordered gap words have scalar transfer \(a+b\), giving determinant \(1-a-b\). For the three-spin exclusion, a previous-short/previous-long two-state transfer matrix is

\[
T(z,y)=\begin{pmatrix}a&b\\a&0\end{pmatrix},
\qquad \det(I-T)=1-a-ab=1-yz^2-y^2z^5.
\]

The familiar trace–log identity \(-\log\det(I-T)=\sum_{m\ge1}\operatorname{tr}(T^m)/m\), followed by \(z\partial_z\), supplies the labeled length factor. Together with hub reversal this proves both rational length-generating expressions for every \(n\ge5\).

**Step 4: asymptotic entropy.** At \(y=1\), the singularities of the ordinary count are the roots of \(1-z^2-z^3\) and of the three-spin count the roots of \(1-z^2-z^5\). In each case the nonnegative-coefficient rational series has a unique dominant positive pole: the step lengths are coprime, respectively \(\gcd(2,3)=1\) and \(\gcd(2,5)=1\), and aperiodicity excludes same-modulus competing poles. Their positive reciprocals \(\alpha\) and \(\beta\) solve the displayed equations and are simple. Coefficient asymptotics give positive constants times the corresponding powers, and hence the stated entropy limits and exponential survivor fraction. The total number of spins is \(n+1\); normalizing by that instead of \(n\) gives the same limits.

## Verification

The self-contained accompanying `verify.py` evaluates the original spin Hamiltonian directly, not just a recoded word count. It enumerates **every** spin assignment for \(5\le n\le12\), tests **every** nonempty flip subset of at most three spins, and compares the results against both motif classifications and both energy-graded binomial expressions. It also compares both binomial polynomials to coefficients of independent rational-series recurrences for every \(5\le n\le150\), and checks numerical values of the positive algebraic roots. Its last run completed without assertion failures and reported 49,252 direct configuration-or-coefficient assertions. The finite computation supports the all-size proof; it is not an infinite proof or a claim of exhaustive bibliographic novelty.

Representative totals for one-/two-spin versus three-spin stability are \(10/4\) for \(n=6\), \(20/4\) for \(n=8\), \(34/14\) for \(n=10\), and \(58/28\) for \(n=12\).

## Relationship to prior work

The literature on one-spin Ising minima includes Bray and Moore's metastable-energy formalism and Wacław and Burda's methods on graphs. Newman and Stein formulated multi-spin-flip stable states in disordered lattices, particularly connected lattice animals, and investigated their large-volume properties. The one-spin Perrin cyclic-word baseline is already available by an equivalent staggered-field chain coding; it is explicitly not presented as new. In contrast, the present claimed contribution is the complete **three-spin cooperative obstruction on the uniform antiferromagnetic wheel**, with all-site (including hub) flip testing, exact energy grading, and the distinct fifth-degree entropy root. General M-spin frameworks, stochastic quench results, and the cyclic one-spin census do not themselves imply that wheel-specific obstruction or counting formula without additional analysis.

## Limitations

The result concerns **weak** energetic stability (zero-cost moves are allowed) rather than strict absorbing states of dynamics that execute neutral flips. It gives neither the likelihood of reaching a stable configuration after a quench nor transition times. The graph is a wheel with equal antiferromagnetic bonds; none of the formulas is claimed for ferromagnetic, disordered, field-driven, or general planar graphs. The coefficient arrays are obtained from elementary cyclic independent-set enumeration, which may appear in combinatorial tables under different terminology; the physical cooperative-flip identification is the substantive claim. An equivalent niche wheel-graph metastability classification not found in the inspected literature remains possible. Independent validation has not been performed.

## References

1. C. M. Newman and D. L. Stein, *Metastable States in Spin Glasses and Disordered Ferromagnets*, Physical Review E **60** (1999), 5244–5260, DOI: 10.1103/PhysRevE.60.5244; preprint arXiv:cond-mat/9908455v1 (public 1999-08-30).
2. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, Physical Review E **77** (2008), 041114, DOI: 10.1103/PhysRevE.77.041114; preprint arXiv:0801.1224v1 (public 2008-01-08).
3. A. J. Bray and M. A. Moore, *Metastable states in spin glasses with short-ranged interactions*, Journal of Physics C: Solid State Physics **14** (1981), 1313–1329, DOI: 10.1088/0022-3719/14/9/016.
