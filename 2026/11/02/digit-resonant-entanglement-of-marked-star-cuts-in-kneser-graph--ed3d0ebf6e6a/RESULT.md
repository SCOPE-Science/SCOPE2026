# Digit-resonant entanglement of marked-star cuts in Kneser graph states

## Finding

Let \(k\ge 2\), \(1\le s\le k\), and \(n\ge 2k+s-1\) be integers. In the Kneser graph \(KG(n,k)\), vertices are the \(k\)-subsets of \([n]\), adjacent exactly when disjoint. Fix an \(s\)-element ground-set subset \(U\). Let \(A\) consist of all graph vertices meeting \(U\), and let \(B\) be the other graph vertices. Put one prime-dimensional qudit at each graph vertex, and use unit-weight controlled-phase gates along all edges to prepare the pure graph state.

Write \(m=n-s\), \(\ell=m-k\), \(\mu_i=\binom mi-\binom m{i-1}\), with \(\binom m{-1}=0\). The exact base-\(p\) entropy across \(A\mid B\) is

\[
R_p(n,k,s)=\sum_{i=0}^{k-1}\mu_i\,\mathbf 1\!\left\{\exists j\in\{1,\ldots,\min(s,k-i)\}:\binom{\ell-i}{k-j-i}\not\equiv0\pmod p\right\}.
\]

The complete nonzero spectrum of the reduced state is \(p^{R_p}\) repetitions of \(p^{-R_p}\). Every positive-order Rényi entropy, and the von Neumann entropy, therefore equals \(R_p\) in base-\(p\) units.

The maximum rank permitted by the common subset-incidence row space is \(\binom m{k-1}\). If \(s=k\), that rank is attained for every prime. If \(1\le s<k\), put \(i_*=k-s-1\), \(q=p^a\), where \(a\) is the smallest positive integer with \(p^a>s\), and define the deficiency \(\Delta=\binom m{k-1}-R_p\). With \(b=\binom m{i_*-1}\) (zero when \(i_*=0\)) and \(\mu_{i_*}=\binom m{i_*}-b\), the following **sharp leading resonance** holds for every allowed \(n\):

\[
\begin{aligned}
q\mid(n-2k+1)&\quad\Longrightarrow\quad \mu_{i_*}\le\Delta\le\mu_{i_*}+b,\\
q\nmid(n-2k+1)&\quad\Longrightarrow\quad 0\le\Delta\le b.
\end{aligned}
\]

For fixed \(k,s,p\) with \(s\le k-2\), the resonant deficiency has degree \(k-s-1\) in \(n\), with leading coefficient \(1/(k-s-1)!\), whereas off-resonance its order is at most \(n^{k-s-2}\). For \(s=k-1\), the deficiency is exactly one on the resonant residue class and zero otherwise. The resonant circumferences have natural density \(1/q\).

For the odd graph \(KG(7,3)\), a one-point star cut has entropies \(10,14,15\) in base-\(p\) units at primes \(p=2,3,5\), respectively, while the cut given by the union of two marked-point stars has entropy \(10\) and a maximally mixed ten-qudit smaller subsystem for every prime.

## Assumptions and scope

The graph is simple, its edges all have phase weight one, the local Hilbert-space dimension \(p\) is prime, and the global state is pure. The marked set \(U\) is any fixed subset of the indicated cardinality. The theorem treats the indicated \(A\mid B\) cuts, not arbitrary cuts. Under \(n\ge2k+s-1\), the common incidence basis and binomial factors in the formula are defined without negative upper arguments; \(|B|=\binom m k\) and \(|A|=\binom nk-\binom m k\). Entropies are dimensionless base-\(p\) logarithms and convert to bits by multiplying by \(\log_2p\).

## Proof

**1. Exact quantum rank reduction.** For \(N=\binom nk\), let \(x\in\mathbb F_p^N\) be a configuration and \(\omega=\exp(2\pi i/p)\). The normalized graph-state amplitudes are \(p^{-N/2}\omega^{\sum_{vw\in E}x_vx_w}\). Internal edges on either side of a bipartition induce local diagonal unitaries, so they do not alter the entanglement spectrum. If \(C\) is the cross-adjacency matrix over \(\mathbb F_p\), tracing over \(B\) gives, up to a local diagonal conjugation,

\[
(\rho_A)_{x,x'}=p^{-|A|}\mathbf 1\{C^{\mathsf T}(x-x')=0\}.
\]

Writing \(r=\operatorname{rank}_{\mathbb F_p}C\), each coset of \(\ker C^{\mathsf T}\) supplies one rank-one constant block of size \(p^{|A|-r}\). The nonzero eigenvalues are therefore exactly \(p^{-r}\), each with multiplicity \(p^r\).

**2. Reduction to a stack of subset-incidence matrices.** A \(k\)-set in \(A\) uses \(j\) marked elements for some \(1\le j\le\min(s,k)\), leaving a \((k-j)\)-subset \(S\) of the unmarked \(m\)-set. A vertex in \(B\) is a \(k\)-subset \(T\) of the same unmarked set. The two Kneser vertices are adjacent precisely when \(S\cap T=\varnothing\). Complementing each column index \(T\) within the unmarked set turns this into \(S\subseteq T^c\), with \(|T^c|=\ell\). For each \(j\) there are \(\binom sj\) identical blocks, which do not affect row rank. Hence \(C\) has the same row space as the vertically stacked inclusion matrices \(W_{k-j,\ell}(m)\) over all eligible \(j\).

**3. Simultaneous integral chain decomposition.** The rank-chain basis in Ghorbani--Khosrovshahi--Maysoori--Mohammad-Noori, equations (5)--(8) and Theorem 1, gives row-independent \(\mu_i\)-element groups \(\mathcal R_{i,\ell}\) for \(0\le i\le k-1\). All their rows together are independent over *every* field because the corresponding integer matrix has a full-size unimodular minor whenever \(k-1\le\ell\le m-(k-1)\). This inequality follows from the stated parameter range. For each level \(t\le k-1\), integer-unimodular row operations transform \(W_{t,\ell}(m)\) into the stack of \(\binom{\ell-i}{t-i}\mathcal R_{i,\ell}\) for \(0\le i\le t\). Consequently, the span of all levels \(t=k-j\) contains the entire independent block \(\mathcal R_{i,\ell}\) if and only if at least one of the displayed binomial multipliers is nonzero modulo \(p\). Summing the corresponding block sizes proves the formula for \(R_p\). This step uses a published integral incidence-matrix theorem; its diagonal form is not claimed as new here.

**4. Exact resonance boundary.** If \(i\ge k-s\), the level \(j=k-i\) occurs and has coefficient \(\binom{\ell-i}{0}=1\), so the corresponding \(\mu_i\) block can never disappear. Thus the highest potentially missing block is \(i_*=k-s-1\) when \(s<k\). For that block, the coefficients are precisely \(\binom{n-2k+1}{u}\), \(u=1,\ldots,s\). By Lucas' theorem, all these binomial coefficients vanish modulo \(p\) if and only if the lowest \(a\) base-\(p\) digits of \(n-2k+1\) vanish, where \(a\) is minimal with \(p^a>s\). Indeed, coefficients with \(u=p^h\le s\) detect each of those digits; conversely, if all are zero then every \(1\le u\le s<p^a\) has a nonzero low digit and yields a zero Lucas factor. This proves the congruence criterion.

**5. Exact finite bounds and asymptotics.** The total multiplicity of all still-lower groups is \(\sum_{i=0}^{i_*-1}\mu_i=\binom m{i_*-1}=b\), so the status of the single highest susceptible block yields the two displayed inequalities. For fixed parameters, \(\mu_{i_*}=m^{i_*}/i_*!+O(m^{i_*-1})\) when \(i_*\ge1\), giving the asserted sharp order distinction. If \(i_*=0\), no lower groups exist and the deficiency is exactly zero or one. If \(s=k\), the coefficient \(\binom{\ell-i}{0}=1\) is present at each \(0\le i\le k-1\), so there is no deficiency. Exactly one residue class modulo \(q\) satisfies the resonance, giving density \(1/q\).

## Verification

Run `python check.py` with NumPy installed. The standalone checker constructs *actual disjointness cut matrices*, computes finite-field ranks by independent elimination, and compares with the incidence-block formula for 135 parameter/prime instances. It also constructs the full pure quantum amplitudes for \(KG(5,2)\) at two marked-set sizes and local dimensions two and three, obtaining the predicted flat reduced-state spectra in four direct tests. It checks the odd-graph universal two-star corollary for 52 additional instances and emits `VERIFY_OK`. These finite computations are corroboration, not an infinite proof; the infinite statements use Steps 1--5.

## Relationship to prior work

Hein--Eisert--Briegel (2003) provide the qubit graph-state cut-rank identity. Looi--Yu--Gheorghiu--Griffiths (2007) define the qudit graph-state controlled-phase formalism. Wilson's inclusion-matrix diagonalization (1990) and its explicit chain-basis derivation by Ghorbani et al. (2007) supply the critical established integer-linear-algebra ingredient. The present specialization combines these ingredients to determine a physically defined family of Kneser cuts and a sharp periodic, prime-characteristic hierarchy of entanglement deficiencies. The existence of general incidence-rank theory is acknowledged; novelty is not asserted for Wilson's rank formula, Lucas' theorem or the graph-state character-sum reduction.

Claudet--Perdrix (first preprint 2024) study generalized local equivalence on a *different* point-versus-subset incidence graph, with binomial divisibility playing a role. Their graphical equivalence hierarchy is not a classification of Kneser marked-star cut spectra or of the leading deficiency resonance above.

## Limitations

No result is claimed for composite local dimensions, weighted graph-state edges, noisy states, cuts unrelated to a marked ground-set subset, or the part of parameter space outside \(n\ge2k+s-1\). The proof does not establish that this application is historically the first use of subset-incidence ranks to study Kneser-state entanglement; specialized earlier work could affect priority. It does not treat a joint thermodynamic scaling where \(k\) or \(s\) grows with \(n\).

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, first public arXiv posting 2003-07-18, https://arxiv.org/abs/quant-ph/0307130 .
2. S. Y. Looi, L. Yu, V. Gheorghiu, R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, first public arXiv posting 2007-12-12, https://arxiv.org/abs/0712.1979 .
3. R. M. Wilson, *A diagonal form for the incidence matrices of t-subsets vs. k-subsets*, European Journal of Combinatorics 11 (1990), 609--615, https://doi.org/10.1016/S0195-6698(13)80046-7 .
4. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, first public arXiv posting 2007-09-20, https://arxiv.org/abs/0709.3144 .
5. N. Claudet, S. Perdrix, *Local equivalence of stabilizer states: a graphical characterisation*, first public arXiv posting 2024-09-30, https://arxiv.org/abs/2409.20183 .
