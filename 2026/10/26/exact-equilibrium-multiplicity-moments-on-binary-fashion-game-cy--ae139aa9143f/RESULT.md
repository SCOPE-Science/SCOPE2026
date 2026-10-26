# Exact equilibrium-multiplicity moments on binary fashion-game cycles

## Finding
For every integer \(n\ge3\), assign each vertex of an undirected \(n\)-cycle independently to be a conformist or a rebel with probability \(1/2\) each. Each vertex chooses an action from \(\{0,1\}\); conformists maximize matching neighbors and rebels maximize disagreeing neighbors, with indifference allowed. Let \(N_n\) count **all labeled pure Nash equilibrium action profiles** for the realized types, counting profiles related by global action complementation separately.

Define
\[
\alpha=\frac{5+\sqrt{17}}4,\qquad
\beta=\frac{5-\sqrt{17}}4,\qquad
\gamma=\frac{7+\sqrt{33}}8,\qquad
\delta=\frac{7-\sqrt{33}}8.
\]
Then the exact first and second moments, at every \(n\ge3\), are
\[
\boxed{\mathbb E N_n=
 (3/2)^n+(-1/2)^n+2(\sqrt3/2)^n\cos(n\pi/2)}
\]
and
\[
\boxed{\begin{aligned}
\mathbb E N_n^2={}&\alpha^n+\beta^n+(-1)^n+2+3(-1/2)^n\\
&+4\mathbf1_{\{2\mid n\}}(-1)^{n/2}
 (\gamma^{n/2}+\delta^{n/2}).
\end{aligned}}
\]
Here the parity term is defined to be zero when \(n\) is odd; no half-integer power or alternating-sign interpretation is needed in that case. Consequently,
\[
\boxed{\lim_{n\to\infty}
\frac{\operatorname{Var}(N_n)}{(\mathbb E N_n)^2}
\left(\frac9{5+\sqrt{17}}\right)^n=1.}
\]
In particular, the relative variance diverges exponentially, even though the older existence characterization implies \(\Pr(N_n=0)\to0\). The latter existence statement is cited as prior work, **not** claimed as a new result.

## Assumptions and scope
Let \(C_n\) be the simple undirected cycle with distinct vertices \(1,\ldots,n\), where \(n\ge3\). Type variables \(\tau_i\in\{C,R\}\) are independent, each equally likely; the graph is fixed and not random. The action profile is \(x\in\{0,1\}^n\). A conformist's payoff is the number of its two neighbors with the same action as itself; a rebel's payoff is the number with the opposite action. A pure Nash equilibrium means no vertex can strictly improve its own payoff by switching action. Both actions are counted separately when a vertex is indifferent. The moments average over type assignments only, not over equilibrium selection or graph randomness.

## Proof
**Local constraints and parity.** Put \(y_i=x_i\mathbin{\oplus}x_{i+1}\), with indices cyclic and \(y_i\in\{0,1\}\). Every realizable vector \(y\) has even parity \(\sum_i y_i\equiv0\pmod2\), and each even-parity \(y\) determines exactly two action profiles \(x\), exchanged by global complementation. At vertex \(i\), a conformist violates best response precisely when both adjacent edges disagree with its action (\(y_{i-1}=y_i=1\)), and a rebel violates best response precisely when both edges agree (\(y_{i-1}=y_i=0\)). Both types are indifferent when one adjacent edge agrees and the other disagrees.

Index rows/columns by \(0,1\) and define
\[
C=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
R=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
For a fixed type word \(\tau\), write \(A_i=C\) if \(\tau_i=C\) and \(A_i=R\) otherwise. The cyclic trace expansion of \(A_1\cdots A_n\) sums the admissible edge patterns; inserting \(D\) on the left of each factor weights each pattern by \((-1)^{\sum_i y_i}\). Since \(1+(-1)^{\sum_i y_i}\) is \(2\) on even-parity patterns and zero on odd-parity patterns, it supplies exactly the two action profiles in each realizable edge class. Therefore
\[
N_n(\tau)=\operatorname{tr}(A_1\cdots A_n)
+\operatorname{tr}((DA_1)\cdots(DA_n)). \tag{1}
\]
This also proves the exact finite-instance formula and handles possible zero equilibria without division or limiting arguments.

**First moment.** Set \(T=(C+R)/2\). Multilinearity and independence of the types yield
\[
\mathbb E N_n=\operatorname{tr}(T^n)+\operatorname{tr}((DT)^n).
\]
The eigenvalues of \(T\) are \(3/2,-1/2\), and those of \(DT\) are \(\pm i\sqrt3/2\). Taking power traces proves the first displayed formula for every \(n\ge3\).

**Second moment.** Because \(\operatorname{tr}(M)\operatorname{tr}(L)=\operatorname{tr}(M\otimes L)\), squaring (1) and independently averaging each type yields
\[
\begin{aligned}
\mathbb E N_n^2&=\operatorname{tr}(U^n)+2\operatorname{tr}(V^n)
+\operatorname{tr}(W^n),\\
U&=\tfrac12(C\otimes C+R\otimes R),\\
V&=\tfrac12(C\otimes DC+R\otimes DR),\\
W&=\tfrac12(DC\otimes DC+DR\otimes DR).
\end{aligned} \tag{2}
\]
The mixed tensor product and its reversed counterpart have the same trace, explaining the coefficient \(2\). Direct exact determinant expansion gives the *monic* characteristic polynomials
\[
\begin{aligned}
\det(zI-U)&=\frac{(z+1)(2z+1)(2z^2-5z+1)}4,\\
\det(zI-V)&=z^4+\frac74z^2+\frac14,\\
\det(zI-W)&=\frac{(z-1)^2(2z+1)^2}4.
\end{aligned}
\]
Thus the four eigenvalues of \(U\) are \(\alpha,\beta,-1,-1/2\); those of \(V\) are \(\pm i\sqrt\gamma,\pm i\sqrt\delta\); and those of \(W\) are \(1,1,-1/2,-1/2\), with algebraic multiplicities. Power traces exist for every positive integer even in the presence of repeated eigenvalues. Substituting their power sums in (2) proves the exact second-moment formula.

**Asymptotic comparison.** We have \(\alpha>9/4\); all other spectral magnitudes in the second moment are strictly smaller than \(\alpha\). The first-moment formula similarly gives \(\mathbb E N_n/(3/2)^n\to1\). Hence \(\mathbb E N_n^2/\alpha^n\to1\) and \((\mathbb E N_n)^2/\alpha^n\to0\). Taking their difference and dividing by \((\mathbb E N_n)^2\) proves the claimed relative-variance limit. No unproved concentration assumption is used.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library, integer matrix arithmetic, and rational numbers. Run `python3 verify.py` in the same directory. It independently enumerates all labeled actions and independently enumerates even-parity edge vectors for every type assignment with \(3\le n\le9\), comparing both counts to (1) for \(1016\) type words. For every type assignment with \(3\le n\le12\), it exhaustively sums the counts and their squares and compares the exact averages against the matrices in (2). It also verifies exact characteristic-polynomial annihilations for all three doubled integer tensor matrices. The complete arbitrary-\(n\) assertion follows from the proof; these bounded tests are checks, not exhaustive proofs for all \(n\).

## Relationship to prior work
Cao and Yang (2014), as restated explicitly in Shen and Lin (2020, Theorem 1.3), characterized when a binary fashion game on a fixed cycle has **no** pure equilibrium: precisely the alternating type configurations with half the cycle length odd. In the present independent fair-type experiment, that known theorem implies \(\Pr(N_n=0)=2^{1-n}\) when \(n\equiv2\pmod4\) and zero otherwise. Existence/nonexistence does not determine the number of equilibria among the overwhelmingly prevalent feasible type configurations, much less either moment or the exponential relative-variance law.

Cao, Sánchez and Zhang (2026) analyze existence and evolving strategy frequencies for heterogeneous network games, including random-network nonexistence, but do not present these exact fixed-cycle equilibrium-multiplicity moments. Pei, Cao and Zhang (2026) study multiple player types and strategy-frequency outcomes; their ring theorem explicitly focuses on at least three actions. Shen and Lin (2020) optimize minimum satisfaction on several graph classes, rather than count equilibria averaged over independent types. Guo and Wang (2016) give methods for locating equilibria in general finite fashion games; an algorithm for individual instances is not the closed annealed moment calculation. Sun (2016) applies statistical mechanics to fashion games on random networks. Its complete text could not be assessed, so overlap with a specialized cycle limit cannot be conclusively excluded; its accessible description addresses random-network satisfaction and existence regimes, not the exact two-moment fixed-cycle law. A recent study of directed cycles with unidirectional dependence (Sánchez-Sáez et al., 2026) uses a different information graph and does not directly imply the bidirectional two-neighbor counting formulas above.

## Limitations
The results assume a fixed simple cycle, two binary behavioral types, *independent exactly fair* type probabilities, symmetric pairwise payoffs, and the standard non-strict best-response convention. They do not determine the full probability distribution of \(N_n\), typical logarithmic growth, sampled equilibrium selection dynamics, or the corresponding moments for general random graphs, unequal type probabilities, or networks with stubborn agents. Characteristic-polynomial computations are verified exactly in the packaged program, not by any external formal proof system. The mathematical finding has undergone an internal self-review only; independent scientific audit has not been performed. The inaccessible full text of relevant earlier statistical-mechanics work remains a publication-priority risk.

## References
1. W. Cao, A. Sánchez, and B. Zhang, *Network games with heterogeneous players*, arXiv:2607.05932v1, first public 2026-07-07. https://arxiv.org/html/2607.05932v1
2. S. Pei, W. Cao, and B. Zhang, *Network games with three types of players*, arXiv:2607.10997v1, first public 2026-07-13. https://arxiv.org/html/2607.10997v1
3. Z. Cao and X. Yang, *The fashion game: Network extension of Matching Pennies*, Theoretical Computer Science 540-541 (2014), 169-181.
4. C. Shen and W. Lin, *Fashion game on graphs*, Discrete Optimization 38 (2020), 100606. https://doi.org/10.1016/j.disopt.2020.100606
5. P. Guo and Y. Wang, *The computation of Nash equilibrium in fashion games via semi-tensor product method*, Journal of Systems Science and Complexity 29 (2016), 881-896. https://doi.org/10.1007/s11424-016-5057-9
6. Y.-F. Sun, *Statistical mechanics of the fashion game on random networks*, Journal of Statistical Mechanics: Theory and Experiment (2016), 023203. https://doi.org/10.1088/1742-5468/2016/02/023203
7. J. M. Sánchez-Sáez, N. Odishelidze, and F. Criado-Aldeanueva, *N-Player Binary Games with Unidirectional Dependencies: Cycle Robustness and Induced Indifference*, arXiv:2606.06625v1, 2026. https://arxiv.org/html/2606.06625v1
