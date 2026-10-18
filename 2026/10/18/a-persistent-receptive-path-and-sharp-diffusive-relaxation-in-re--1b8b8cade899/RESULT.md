# A persistent receptive path and sharp diffusive relaxation in repulsive opinion dynamics

## Finding

In the discrete repulsive bounded-confidence model of Kann and Feng [1], a complete antagonistic network can have a **permanently active receptive path**, despite every opinion converging to an equilibrium at which no distinct agents remain receptive. The phenomenon holds on a nonempty open set of initial states for every population size, has a closed finite-dimensional linear description, and has a sharp quadratic-in-population relaxation law.

**Theorem.** Fix an integer \(n\ge3\) and confidence radius \(c>0\). Put all off-diagonal interaction signs equal to \(-1\) and all diagonal signs equal to \(+1\). Start from strictly increasing real opinions satisfying
\[
0<\delta_i(0):=c-[x_{i+1}(0)-x_i(0)]\le c/2,
\qquad 1\le i<n.
\]
Then for every finite integer \(t\ge0\):

1. Precisely the adjacent pairs \(\{i,i+1\}\) are receptive; in particular the receptive graph is the same path for all finite times.
2. The positive gap-deficit vector \(\delta(t)\in\mathbb R^{n-1}\) obeys \(\delta(t+1)=Q_{n-1}\delta(t)\), where, for \(m=n-1\),
\[
(Q_m)_{ij}=\begin{cases}
1/6,&i=j\in\{1,m\},\\
1/3,&i=j\notin\{1,m\}\ \text{or}\ |i-j|=1,\\
0,&\text{otherwise}.
\end{cases}
\]
3. There are constants \(0<\sigma_n<\rho_n<1\), with \(\rho_n\) the simple Perron eigenvalue of \(Q_{n-1}\), and a strictly positive unit Perron vector \(w_n\), such that
\[
\delta(t)=(w_n^\top\delta(0))w_n\rho_n^t+O(\sigma_n^t).
\]
Here the positive leading coefficient is automatic for every permitted initial condition.
4. The opinions converge to a translated equally spaced lattice. If \(d_1=d_n=2\), \(d_i=3\) for \(2\le i\le n-1\), and
\[
\mu=\frac{\sum_{i=1}^{n}d_i[x_i(0)-(i-1)c]}{3n-2},
\]
then \(x_i(t)\to\mu+(i-1)c\). At the limit **every off-diagonal pair is nonreceptive**, since confidence uses a *strict* inequality.
5. The sharp leading large-population rate satisfies
\[
\frac{1+2\cos(\pi/n)}3-\frac{2\sin^2(\pi/n)}{3n}
\le\rho_n\le\frac{1+2\cos(\pi/n)}3,
\qquad
1-\rho_n=\frac{\pi^2}{3n^2}+O(n^{-3}).
\]
In particular, the slowest relaxation time has leading scale \(3n^2/\pi^2\) synchronous updates.

**Fully connected initial-confidence corollary.** For \(n=3\) or \(4\), start from *any strictly ordered configuration* with \(x_n(0)-x_1(0)<c\). The first synchronous step yields
\[
x_i(1)=\bar x(0)+\frac{c}{n}(2i-n-1),\qquad
\bar x(0)=\frac1n\sum_{j=1}^n x_j(0).
\]
The subsequent trajectory lies in the theorem's invariant path chamber, with equal deficits \(c/3\) for \(n=3\) and \(c/2\) for \(n=4\). Its exact limiting configuration is \(\bar x(0)+c(i-(n+1)/2)\). For three agents, the entire path-phase trajectory is
\[
x_i(t)=\bar x(0)+c(i-2)[1-2^{-(t-1)}/3],\qquad t\ge1,
\]
so adjacent pairs remain receptive at **every** finite time and become nonreceptive only in the limit. The spectral radius is exactly \(\rho_3=1/2\) and \(\rho_4=(3+\sqrt{33})/12\).

## Assumptions and scope

Agent labels coincide with strict increasing opinion order. Opinions are real, the underlying signed graph is complete, and all distinct agents repel. The self-loop has sign \(+1\). The bounded-confidence test is \(|x_j-x_i|<c\), not a weak inequality. At every nonnegative integer time, the model updates **synchronously** by
\[
x_i(t+1)=\frac{x_i(t)+\sum_{j\ne i:\,|x_j(t)-x_i(t)|<c}T_{ij}(t)}{1+\#\{j\ne i:|x_j(t)-x_i(t)|<c\}},
\]
where the repulsive target is
\[
T_{ij}(t)=\begin{cases}x_j(t)+c,&j<i,\\x_j(t)-c,&j>i.\end{cases}
\]
These are equations (3)–(4) of [1], after their algebraic rearrangement in Lemma 4.2, restricted to strictly ordered states. The displayed hypotheses keep that order strict throughout. No statement is made about arbitrary sign patterns, asynchronous models, ties, or attraction.

## Proof

**1. Candidate neighborhood and linearization.** Every adjacent gap initially lies in \([c/2,c)\). Consequently any pair at index separation at least two has distance at least \(c\), whereas all adjacent pairs have distance strictly less than \(c\): the initial receptive graph is precisely the path. In this graph the endpoint updates are
\[
x_1^+=\tfrac12(x_1+x_2-c),\qquad
x_n^+=\tfrac12(x_{n-1}+c+x_n),
\]
and for \(1<i<n\) the opposite repulsive shifts cancel, giving
\[
x_i^+=\tfrac13(x_{i-1}+x_i+x_{i+1}).
\]
Define \(e_i=x_i-(i-1)c\). The transformed state satisfies \(e^+=P_ne\), where the stochastic lazy-path matrix has \((P_n)_{ij}=1/d_i\) for \(|i-j|\le1\) and zero otherwise. In particular \(\delta_i=e_i-e_{i+1}\). Taking adjacent differences in this recurrence, including the two endpoints, yields exactly the matrix \(Q_{n-1}\) displayed above.

**2. Global-in-time chamber invariance.** The matrix \(Q_m\) is nonnegative and irreducible, its row sums are \(1/2\) at the two endpoints and \(1\) at every interior row; for \(m=2\), both row sums are \(1/2\). Thus if every deficit satisfies \(0<\delta_i\le c/2\), then every component of \(Q_m\delta\) remains strictly positive and at most \(c/2\). Repeating the argument inductively validates the assumed receptive path for every finite integer time. In particular the opinions remain strictly ordered, consecutive gaps never equal \(c\) in finite time, and nonadjacent gaps never fall below \(c\).

**3. Convergence and asymptotic profile.** The matrix \(Q_m\) has a strictly positive diagonal, so irreducibility implies primitivity. Its two boundary rows have sum \(1/2<1\). If \(Q_m w=\rho w\) with \(w>0\), then \(\rho<1\): otherwise, the maximal component of \(w\) and irreducibility force all components maximal, contradicting a deficient boundary row. The Perron–Frobenius theorem gives a simple dominant positive eigenvalue \(0<\rho<1\), and since \(Q_m\) is symmetric all other eigenvalues have smaller modulus. Orthogonal spectral expansion proves the claimed profile with strictly positive coefficient \(w^\top\delta(0)\).

The matrix \(P_n\) is an irreducible aperiodic stochastic matrix and is reversible with respect to \(\pi_i=d_i/(3n-2)\), because \(d_i(P_n)_{i,i+1}=d_{i+1}(P_n)_{i+1,i}=1\). Hence \(e_i(t)\to\sum_j\pi_je_j(0)=\mu\). The limiting consecutive gaps equal \(c\), and all other pairs are farther apart, proving the discrepancy between finite-time receptivity and limit-state receptivity.

**4. Spectral estimate.** For \(m=n-1\), introduce the symmetric tridiagonal Toeplitz matrix \(B_m\) with diagonal \(1/3\) and immediate off-diagonals \(1/3\). Then
\[
Q_m=B_m-\tfrac16(e_1e_1^\top+e_me_m^\top).
\]
Its maximal Toeplitz eigenvalue is \((1+2\cos(\pi/n))/3\). The Rayleigh–Ritz principle gives the upper bound. Test the positive vector \(v_j=\sin(\pi j/n)\), whose squared norm equals \(n/2\) and which is a top eigenvector of \(B_m\). The boundary penalty has numerator \(2\sin^2(\pi/n)/6\), yielding the asserted lower bound. The gap between the two bounds is \(O(n^{-3})\); expanding \(\cos(\pi/n)\) gives \(1-\rho_n=\pi^2/(3n^2)+O(n^{-3})\). This is a theorem for every integer \(n\ge3\), not an extrapolation from finite numerics.

**5. All-receptive starts for three and four agents.** If initially all distinct opinions are separated by less than \(c\), every pair interacts. Each agent averages its own opinion and every translated repulsive target, giving \(n x_i(1)=\sum_jx_j(0)+c[(i-1)-(n-i)]\). Thus first-step adjacent spacing is exactly \(2c/n\). For \(n=3,4\) these spacings lie in \([c/2,c)\), and the invariant theorem applies at time one. Reflection about the mean plus preservation of the degree-weighted offset mean identifies the limiting lattice. When \(n=3\), the equal deficit vector is an eigenvector of \(Q_2\) of eigenvalue \(1/2\), giving the displayed full time formula. The three-by-three characteristic polynomial of \(Q_3\) gives its largest root \((3+\sqrt{33})/12\), while \(Q_2\) has top eigenvalue \(1/2\).

## Verification

Run `python3 verify.py` with Python 3 (standard library only). The bundled program independently implements the original sign-based synchronous update and checks the path recurrence with exact fractions for \(n=3,\ldots,12\) and eight rational initial conditions per size across 12 time steps (960 exact transitions). It checks 80 additional rational first-step complete-confidence examples for three and four agents. It also computes the largest eigenvalues of tridiagonal matrices numerically for eight network sizes and checks the derived spectral brackets. Its successful output begins `VERIFY_OK rational_state_transitions 1040 spectral_brackets 8`.

These computations test the algebra and examples. The infinite-time assertions follow instead from the positivity induction, matrix spectral theorem, and reversible Markov-chain argument in the proof.

## Relationship to prior work

Kann and Feng [1, Sections 3–4, especially Lemma 4.9 and Theorem 4.10] introduce this discrete-time repulsive rule and derive the asymptotic maximal width \((n-1)c\) when all off-diagonal edges are repulsive. Their qualitative discussion does **not** supply the invariant receptive-path chamber, its exact deficit transition matrix, a non-finite-separation proof on an open set, the explicit stationary weighted center, or sharp population-size relaxation scaling. The current claim pertains to these additional quantitative statements, **not** to rediscovery of the limiting width.

Altafini and Ceragioli [2] analyze sign-preserving bounded-confidence dynamics using continuous-time state-dependent signed interactions; their sign and time-evolution mechanisms differ, and their results do not give this synchronous exact path-deficit recurrence. Published work on a seven-agent nonfreezing *attractive* bounded-confidence system [3] studies switching counts for heterogeneous confidence radii, not an all-repulsive complete network. Published work on repulsive discrete sine-coupled phase oscillators [4] treats angular variables and the Kuramoto sine law, not the confidence-cutoff opinion map. Neither theorem entails the matrix and sharp rate above.

## Limitations

The invariant chamber is explicit and open when all inequalities are strict, but the result does not classify all possible initial opinions, sign patterns, or transient receptive graphs. The fully connected initial-confidence corollary is only proved for three and four agents. Spectral estimates supply the sharp leading \(n^{-2}\) relaxation law but not the exact eigenvalue as an elementary function for every size. The limiting graph change is a discontinuity of the *strict* receptivity criterion evaluated at the limiting opinions, not an actual finite-time topology switch. Priority over additional uninspected specialist work is not established; independent external audit has not been performed.

## References

[1] C. Kann and M. Feng, *A Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1 (first public version 2023-01-05), Sections 3–4, https://arxiv.org/html/2301.02210v1.

[2] C. Altafini and F. Ceragioli, *Signed bounded confidence models for opinion dynamics*, Automatica 93 (2018), 114–125, doi:10.1016/j.automatica.2018.03.064; lawful open postprint https://www.diva-portal.org/smash/get/diva2:1235308/FULLTEXT01.pdf.

[3] *Exact logarithmic switching lifetime near a nonfreezing seven-agent confidence system*, publicly indexed research note (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-logarithmic-switching-lifetime-near-a-nonfreezing-seven-ag--3aa033f36f32.

[4] *Odd-even relaxation dichotomy for discrete repulsive all-to-all phase networks*, publicly indexed research note (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-odd-even-relaxation-dichotomy-for-discrete-repulsive-all-to-all--d8909b4a83b3.
