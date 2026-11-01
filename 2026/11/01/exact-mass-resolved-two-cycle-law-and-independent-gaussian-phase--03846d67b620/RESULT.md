# Exact mass-resolved two-cycle law and independent Gaussian phase fluctuations on complete graphs

## Finding
For every integer \(n\ge2\), synchronous ordinary chip-firing on the labelled simple complete graph \(K_n\), **without self-loops**, has the following polynomial enumerating primitive period-two *orbits*, counted once per unordered pair of alternating states and weighted by conserved chip mass:
\[
P_n(z)=\frac12\sum_{a=1}^{n-1}\binom na z^{n(n-1)-a(n-a)}[n-a]_z^a[a]_z^{n-a},\qquad [k]_z=\sum_{j=0}^{k-1}z^j.
\tag{1}
\]
In particular,
\[
N_n=P_n(1)=\frac12\sum_{a=1}^{n-1}\binom na (n-a)^a a^{n-a}\sim\frac{n^n}{4},
\tag{2}
\]
and \(P_n(z)=z^{n(2n-3)}P_n(z^{-1})\). For a uniformly random primitive orbit and an independent uniform phase, denote its firing-set cardinality by \(A_n\) and its conserved chip mass by \(M_n\). Then
\[
\left(\frac{A_n-n/2}{\sqrt n},\frac{M_n-(n^2-3n/2)}{n^{3/2}}\right)
\xrightarrow{\mathrm{law}}(G_1,G_2),\qquad
G_1\sim\mathcal N(0,1/16),\quad G_2\sim\mathcal N(0,1/48),
\tag{3}
\]
where the two limits are independent; exactly \(\mathbb E M_n=n^2-3n/2\) for every \(n\ge2\).

## Assumptions and scope
The finite vertex set is labelled \(\{1,\dots,n\}\), with an edge between each distinct pair and no loops. A state is a vector \(\sigma\in\mathbb Z_{\ge0}^{n}\). Set \(d=n-1\) and \(F_\sigma(v)=\mathbf1_{\{\sigma(v)\ge d\}}\); the deterministic synchronous update is
\[
(U\sigma)(v)=\sigma(v)-dF_\sigma(v)+\sum_{w\ne v}F_\sigma(w).
\]
Mass \(M(\sigma)=\sum_v\sigma(v)\) is invariant. A primitive two-cycle is an unordered pair of **distinct** states \(\{\sigma,U\sigma\}\) with \(U^2\sigma=\sigma\). In (3), a temporal phase is chosen uniformly independently after an orbit is chosen uniformly; this is equivalent to choosing a uniformly random primitive period-two state. Neither (1) nor (3) counts transient states or their attraction basins.

## Proof
**Complementary firing phases.** We first establish the standard phase-cut parametrization, included as a proof ingredient and not a novel general theorem. On any finite connected loopless graph, let \(\sigma'=U\sigma\ne\sigma\), \(U\sigma'=\sigma\), and write their binary firing vectors as \(f,g\). Summing the two update equations yields \(L(f+g)=0\), where \(L\) is the graph Laplacian. Connectivity makes \(f+g\) constant, and a nonfixed orbit rules out the constants zero and two. Thus \(g=\mathbf1-f\), and the first-phase firing set \(S=\{v:f(v)=1\}\) is nonempty and proper. Write \(c_v=|\{w\sim v:\mathbf1_S(w)\ne\mathbf1_S(v)\}|\). Then the update decreases the chips of each \(v\in S\) by \(c_v\) and increases the chips of each \(v\notin S\) by \(c_v\). The two threshold requirements are **equivalent** to the independent integer intervals
\[
\sigma(v)\in[d_v,d_v+c_v-1]\quad(v\in S),\qquad
\sigma(v)\in[d_v-c_v,d_v-1]\quad(v\notin S).
\tag{4}
\]
Each interval has length \(c_v\); its endpoints are nonnegative because \(c_v\le d_v\). Conversely, (4) makes the second firing vector exactly \(\mathbf1-f\), and the second update returns the state. Therefore (4) is necessary and sufficient, and it excludes any cut with an isolated monochromatic vertex \(c_v=0\). Each period-two orbit is represented by precisely two first-phase states, with firing sets \(S\) and \(V\setminus S\).

**Exact complete-graph count.** In \(K_n\), if \(|S|=a\), then \(c_v=n-a\) for \(v\in S\) and \(c_v=a\) for \(v\notin S\). The minimum total mass from (4) is
\[
a(n-1)+(n-a)(n-1-a)=n(n-1)-a(n-a).
\]
Independent choices within the intervals contribute the factors \([n-a]_z^a[a]_z^{n-a}\); there are \(\binom na\) labelled choices of \(S\). Dividing by two for temporal phase proves (1). Setting \(z=1\) proves the finite sum in (2). Every factor \([k]_z\) is reciprocal of degree \(k-1\); the exponent of reciprocity for each summand is
\[
2\big(n(n-1)-a(n-a)\big)+a(n-a-1)+(n-a)(a-1)=n(2n-3),
\]
independent of \(a\). Thus (1) is palindromic and its mass mean equals \(n(2n-3)/2\) exactly.

**Firing-phase fluctuations and total population.** Let \(w_{n,a}=\binom na(n-a)^a a^{n-a}\); the probability of \(A_n=a\) under a uniform primitive state is \(w_{n,a}/\sum_{j=1}^{n-1}w_{n,j}\). With \(u=a/n\), the exact entropy identity and Stirling's formula, locally uniformly for \(u\) in compact subsets of \((0,1)\), give
\[
w_{n,a}=\frac{n^n}{\sqrt{2\pi n u(1-u)}}\exp\big(nh(u)\big)\big(1+O(n^{-1})\big),\quad
h(u)=(1-2u)\log\frac{u}{1-u}.
\]
The strictly nonpositive function \(h\) has its unique maximum at \(u=1/2\); near that point \(h(1/2+\varepsilon)=-8\varepsilon^2+O(\varepsilon^4)\). To justify ignoring the endpoints, observe that for every \(u\in(0,1)\), \((1-2u)\log(u/(1-u))\le0\), with a strictly negative maximum on each closed set excluding \(1/2\); the elementary entropy bound \(\binom na\le e^{nH(u)}\) and the exact defining formula for \(w_{n,a}\) give a uniform \(n^ne^{nh(u)}\) bound. Thus the lattice Laplace method applies, yielding
\[
\sum_{a=1}^{n-1}w_{n,a}\sim\frac{n^n}{2},\qquad
\frac{A_n-n/2}{\sqrt n}\xrightarrow{\mathrm{law}}\mathcal N(0,1/16).
\]
The orbit count is half of the total first-phase state count, proving the asymptotic in (2).

**Conditional mass fluctuations and asymptotic independence.** Conditional on \(A_n=a\), the individual chip counts in (4) are independent discrete uniforms: \(a\) have interval length \(n-a\), and \(n-a\) have length \(a\). Therefore
\[
\mathbb E[M_n\mid A_n=a]=n^2-\frac{3n}{2},\qquad
\operatorname{Var}(M_n\mid A_n=a)=\frac{n\big(a(n-a)-1\big)}{12}.
\tag{5}
\]
For every sequence \(a=n/2+O(\sqrt n)\), this conditional variance divided by \(n^3\) tends uniformly to \(1/48\), and every centered independent summand has absolute value at most \(n\). Its maximum divided by the overall standard-deviation scale \(n^{3/2}\) therefore tends to zero. The elementary Lindeberg or characteristic-function proof of the triangular-array central limit theorem gives the same centered normal limit for mass, uniformly across any fixed central window \(|a-n/2|\le C\sqrt n\). Combining the uniform conditional convergence with the tight Gaussian limit for \(A_n\), and finally letting \(C\to\infty\), makes the joint characteristic function factor into the two Gaussian characteristic functions. This proves (3), including independence.

## Verification
The included standalone standard-library script `verify_cut_cycle.py` performs direct synchronous iteration and compares every periodic mass coefficient against (4) for all connected labelled simple graphs with two to four vertices. It separately enumerates all states in finite guaranteed containing boxes for complete graphs of sizes two through six (including one million initial configurations at size six), and for paths and cycles of sizes three through eight. It checks the closed complete-graph polynomial, exact palindromicity and means, and computes finite-size asymptotic diagnostics at sizes \(40\), \(160\), and \(640\). The saved output is `verification_output.txt`. The final success line is `GRAPH_CUT_TWO_CYCLE_VERIFY_OK`. This computational testing is supplementary: the all-size formulas and joint limit are proved above, not inferred from the tests.

## Relationship to prior work
Levine's complete-graph study [1] develops period/activity windows and the devil's staircase, but the checked paper's main period-two theorem does not supply the mass-resolved population polynomial (1) or the joint phase–mass limit (3). **Conventions differ**: Levine uses the looped complete graph with firing threshold \(n\), whereas this theorem uses a loopless complete graph with threshold \(n-1\); translating all vertex chips by one conjugates the corresponding update maps and shifts total mass by \(n\). Scully–Jiang–Zhang [2] analyze firing sequences and constraints, rather than this microcanonical enumeration. Wang–Lannan [3] establish eventual period-two behavior throughout a middle mass window on general graphs; eventual-period assertions do not determine the number of states already lying on a primitive two-cycle at each mass. The complementary phase-cut/interval characterization is a standard ingredient also used in other graph families; **it is not asserted here as new**. The specific finite \(K_n\) mass polynomial and the asymptotically independent joint Gaussian law are the claims assessed for novelty.

## Limitations
The claimed classification concerns **only states already on primitive period-two orbits** on labelled loopless complete graphs; not all initial states become period two, and no claim is made about transient basins, general orbit periods, or arbitrary-graph central limit laws. The Gaussian theorem holds as \(n\to\infty\), not exactly at finite \(n\). Earlier phase-cut descriptions and other graph-family mass censuses are acknowledged rather than treated as novelties. Some historical full texts were inaccessible; an earlier equivalent complete-graph mass formula or limit law cannot be categorically excluded by the literature search. The verification program is a finite exact check, not a standalone proof of the asymptotic statement.

## References
[1] L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, initial preprint 2008-11-17, arXiv:0811.2800v1, https://arxiv.org/abs/0811.2800 . The openly available full paper at https://lionellevine.github.io/staircase-completegraph.pdf was examined, including the period-two discussion and Theorem 23.

[2] Z. Scully, T.-Y. Jiang, Y. Zhang, *Firing Patterns in the Parallel Chip-Firing Game*, FPSAC proceedings (2014), HAL:hal-01207550, https://ziv.codes/pdf/dmtcs2014-scully.pdf . Examined abstract and the portions on firing patterns.

[3] D. Wang, N. Lannan, *All parallel chip-firing games with \(2|E|-|V|<|\sigma|<2|E|\) have period \(2\)*, arXiv:2608.04153v1 (2026-08-04), https://arxiv.org/abs/2608.04153 . Examined the open full-text theorem statements and proofs on arXiv.

[4] J. Bitar, E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science (1992), DOI:10.1016/0304-3975(92)90316-8 . Bibliographic metadata and abstract were consulted; full text was not accessible for direct comparison.
