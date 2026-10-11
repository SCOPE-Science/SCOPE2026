# A Fibonacci entropy staircase and its full scaled accumulation interval

## Finding
Let \(f=010010100100101\ldots\) be the right-infinite fixed point of \(0\mapsto01\) and \(1\mapsto0\). Let \(X\subseteq\{0,1\}^{\mathbb Z}\) be the two-sided subshift having exactly the finite factors of \(f\). For every integer \(n\ge1\), define the shift of finite type
\[
Y_n=\{y\in\{0,1\}^{\mathbb Z}: y_{j}\ldots y_{j+n}\in\mathcal L_{n+1}(X)\text{ for every }j\in\mathbb Z\},
\]
and let \(h_n=h_{\rm top}(Y_n)\) use the natural logarithm. Write \(F_1=F_2=1\), \(F_{m+1}=F_m+F_{m-1}\). **For every \(m\ge3\) and every integer \(n\) with \(F_m-1\le n\le F_{m+1}-2\)**, the entropy \(h_n\) is the unique positive solution of
\[
e^{-F_{m-1}h_n}+e^{-F_mh_n}=1.\tag{1}
\]
In particular, \(h_n\) is a decreasing staircase, constant on the displayed Fibonacci intervals. Put \(\varphi=(1+\sqrt5)/2\), and let \(c\) be the unique positive solution of
\[
e^{-c/\varphi}+e^{-c}=1.\tag{2}
\]
Then the full subsequential accumulation set is
\[
\bigcap_{N\ge1}\overline{\{n h_n:n\ge N\}}=[c,\varphi c].\tag{3}
\]
Numerically, \(c=0.8739139654917809\ldots\) and \(\varphi c=1.4140224994089043\ldots\). In particular, \(n h_n\) does not converge, even though \(h_n\to0\).

## Assumptions and scope
The alphabet is binary, the system is two-sided, entropy is logarithmic to base \(e\), and only the Fibonacci substitution language is considered. The indexing of \(Y_n\) is specified by **permitted factors of length \(n+1\)**; relative to the convention in Coles–Cyr–Kra–Pavlov, in which the \(k\)-th cover admits factors of length \(k\), the present \(Y_n\) is their \((n+1)\)-st cover. In particular, there is no hidden offset in (1)–(3). The source motivating the use of canonical SFT covers was publicly posted on 2026-02-04 [1].

## Proof
**1. Rauzy graphs and the cover.** Let \(G_n\) be the directed graph whose vertices are the length-\(n\) factors of \(f\), with one directed edge for each length-\(n+1\) factor, connecting its prefix to its suffix. Its edge shift presents \(Y_n\), hence
\[
h_n=\log\rho(G_n),
\]
where \(\rho\) is the Perron spectral radius. The Fibonacci language is Sturmian and recurrent; the graph has exactly \(n+1\) vertices and \(n+2\) edges, with exactly one right-special vertex of outdegree two, exactly one left-special vertex of indegree two, and all other degrees equal to one [2,3].

**2. Why the entropy is unchanged at nonbispecial lengths.** For any \(n\), vertices of the directed line graph of \(G_n\) are length-\(n+1\) factors; its edges are pairs of composable length-\(n+1\) factors. Such a pair represents an allowed length-\(n+2\) factor unless the common length-\(n\) middle factor admits both left and right extensions and the combined extension is the missing one. Therefore, if the unique left- and right-special length-\(n\) factors are distinct (\(n\) is not a bispecial length), *every* composable pair is realized, so \(G_{n+1}\) is precisely the directed line graph of \(G_n\). For every finite directed graph the edge and vertex incidence factorizations give adjacency matrices \(RS\) and \(SR\); their nonzero eigenvalues, with multiplicity, agree. Thus \(\rho(G_{n+1})=\rho(G_n)\) whenever \(n\) is not bispecial.

**3. The bispecial endpoints.** The Fibonacci language has bispecial factors precisely at lengths \(F_j-2\), \(j\ge3\). At \(n=F_{m+1}-2\), the left- and right-special vertices of \(G_n\) coincide; the two directed loops meeting at that vertex have lengths \(F_{m-1}\) and \(F_m\). These *specific structural facts* are established for Fibonacci Rauzy graphs in Bruin–Leplaideur [2, §2.1–2.2], including its Proposition 2.2 and the graph discussion, and are not claimed as new here. Equivalently, the graph is a directed bouquet of two circles of these lengths: every other vertex has indegree and outdegree one and strong connectivity leaves no other component. Its first-return generating series at the common vertex is
\[
R(z)=z^{F_{m-1}}+z^{F_m}.
\]
All closed walks through that vertex concatenate these two return circuits. Their exponential growth parameter \(z\in(0,1)\) is determined by \(R(z)=1\), and \(z=e^{-h_{F_{m+1}-2}}\). This gives (1) at the right endpoint. Since consecutive bispecial lengths are \(F_m-2\) and \(F_{m+1}-2\), the lengths \(F_m-1,\ldots,F_{m+1}-3\) are nonbispecial. Step 2 propagates the *same* entropy through that whole interval, proving (1) with its exact boundary indices. For \(m=3\) the interval consists only of \(n=1\) and the same two-loop argument applies directly.

**4. Sharp accumulation set.** Let \(H_m\) denote the common \(h_n\) on the \(m\)-th interval, and define \(c_m=F_mH_m\). Dividing the two exponents in (1) by \(F_m\) gives
\[
e^{-(F_{m-1}/F_m)c_m}+e^{-c_m}=1.
\]
Because \(F_{m-1}/F_m\to1/\varphi\), strict monotonicity and continuity of the left-hand side imply \(c_m\to c\). Every corresponding index satisfies
\[
1-F_m^{-1}\le n/F_m\le F_{m+1}/F_m-2/F_m\to\varphi.
\]
Therefore all accumulation points of \(nH_m=(n/F_m)c_m\) lie in \([c,\varphi c]\). Conversely, for every \(t\in[1,\varphi]\), choose integers \(n_m\) in the specified interval with \(n_m/F_m\to t\) (round \(tF_m\) and clamp to the interval). Then \(n_mh_{n_m}\to tc\). This proves the **entire** interval in (3), not just the two extrema. Finally (1) bounds \(h_n=O(1/F_m)=O(1/n)\).

## Verification
The accompanying standalone standard-library program `verify_fibonacci_cover.py` builds independent finite substitution prefixes and, for every \(1\le n\le200\), checks exact factor counts, graph edges and degrees, and the two first-return circuit lengths. It prints the first eight Fibonacci interval transitions and independently solves the scalar limit equation numerically. These 200 finite diagnostics are *not* an exhaustive proof of the infinite Fibonacci factor assertions; those enter through the cited full-text structural results and the argument above. Reproduce with `python3 verify_fibonacci_cover.py` from the extracted package directory. No external data or installed packages are needed.

## Relationship to prior work
Coles–Cyr–Kra–Pavlov [1] introduce quantitative stabilization questions for the canonical SFT cover of a general subshift, including entropy differences, but do not establish (1)–(3) for the Fibonacci system. Bruin–Leplaideur [2] explicitly determine the Fibonacci bispecial indices and the two loop lengths at bispecial Rauzy graphs. Those graph facts are **prior results** and are used here rather than presented as discoveries. The new statement tracks the entropy of *every* canonical finite-type cover, proves exact constant-entropy index intervals, and determines its sharp rescaled accumulation set. Praveen–Rama [3] analyze Fibonacci Rauzy graph structure and connectivity, not this entropy scaling. De Luca [4] independently details the Fibonacci palindromic-prefix periods underlying the special indices. Classical finite-graph Perron theory and line-graph spectra are also prior facts. No novelty claim is made for those ingredients individually.

## Limitations
The result is specific to the fixed Fibonacci Sturmian language and to this indexing of canonical covers; it is not a rate theorem for arbitrary Sturmian slopes. The entropy equation itself follows transparently once the existing Fibonacci graph structure is supplied. In particular, older statements of equivalent finite-cover entropy asymptotics may exist under different symbolic or continued-fraction terminology. No independent priority audit has been performed. Numerical checks at finite lengths cannot certify the infinite structure independently of the cited mathematics.

## References
[1] Solly Coles, Van Cyr, Bryna Kra, and Ronnie Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1 (first public 2026-02-04), https://arxiv.org/pdf/2602.04097.

[2] Henk Bruin and Renaud Leplaideur, *Renormalization, freezing phase transitions and Fibonacci quasicrystals*, arXiv:1309.7934v1 (2013), especially Section 2.1–2.2, Proposition 2.2 and the bispecial Rauzy-loop discussion; https://arxiv.org/html/1309.7934v1.

[3] Rajavel Praveen M and Rama R, *A Note On \(\ell\)-Rauzy Graphs for the Infinite Fibonacci Word*, arXiv:2210.08629v2 (2022), Sections 2–5; https://arxiv.org/html/2210.08629v2.

[4] Aldo de Luca, *Some extremal properties of the Fibonacci word*, arXiv:1209.3927v1 (2012), Sections 3–4; https://arxiv.org/pdf/1209.3927.
