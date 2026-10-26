# Arithmetic near-perfect transport through three weakly connected quantum-walk communities

## Finding
Let three nontrivial connected simple graphs be joined in a chain by weak edges of weight \(\varepsilon>0\). Their respective numbers of internal directed arcs are \(M_1,M_2,M_3>0\), and the numbers of weak undirected edges between successive communities are positive integers \(k_1,k_2\). The source's weak-edge Grover walk has an effective symmetric Laplacian
\[
L=\begin{pmatrix}
 k_1/M_1&-k_1/\sqrt{M_1M_2}&0\\
 -k_1/\sqrt{M_1M_2}&(k_1+k_2)/M_2&-k_2/\sqrt{M_2M_3}\\
 0&-k_2/\sqrt{M_2M_3}&k_2/M_3
\end{pmatrix}.
\]
Define the **optimal leading-order end-to-end transfer** by
\[
Q=\sup_{\tau\geq0}\left|\left[\cos(\tau\sqrt L)\right]_{31}\right|^2.
\]
Then \(Q=1\) **if and only if** \(M_1=M_3=M\), \(k_1=k_2=k\), and the frequency ratio
\[
\rho=\sqrt{1+\frac{2M}{M_2}}
\]
is either irrational or a rational \(p/q\) in lowest terms with \(p\) even and \(q\) odd. If \(\rho\) is irrational, unit transfer is approached but not attained at any finite reduced time; if \(\rho=p/q\) has the specified parity, unit transfer is attained at \(\tau=q\pi\sqrt{M/k}\). All other reduced three-community paths satisfy \(Q<1\).

For balanced communities \(M_1=M_2=M_3=M\), with equal bridge multiplicity \(k\), put
\[
x_j+q_j\sqrt3=(2+\sqrt3)^{2j+1},\qquad j=0,1,2,\ldots.
\]
These are positive integers with \(x_j\) even, \(q_j\) odd, and \(x_j^2-3q_j^2=1\). At \(\tau_j=\pi q_j\sqrt{M/k}\), the limiting transfer probability \(P_j\) obeys the explicit quantitative witness
\[
1-P_j<\frac{\pi^2}{72q_j^2}.
\]
For example, the successive denominators \(1,15,209\) give nearly perfect pulses, despite the impossibility of exactly perfect reduced-time transfer at any finite time when the masses are balanced.

## Assumptions and scope
The three original communities are finite, connected, simple, and each contains at least one internal edge. Weak edges form a reduced path: there are no direct weak edges between the first and third communities. Internal edges have weight one and weak edges have common positive weight \(\varepsilon\). We use the precise arc-space weighted Grover operator and initial normalized uniform state on internal arcs of the first community in Hosaka and Segawa, arXiv:2610.07768v1, Sections 2–3. The reduced quantity \(Q\) optimizes the **leading-order wave dynamics**, not the exact finite-\(\varepsilon\) walk across unrestricted observation times. The integers \(M_i\) are even in a simple undirected graph, and only realizable combinations of arc counts and bridge multiplicities are asserted for physical graphs.

For every **fixed** \(\tau>0\), the source proves
\[
\mu_{\lfloor\tau/\sqrt{2\varepsilon}\rfloor}^{(\varepsilon)}(1,3)
=\left|\left[\cos(\tau\sqrt L)\right]_{31}\right|^2+O_\tau(\sqrt\varepsilon).
\]
Thus in all cases with \(Q=1\), for every target infidelity \(\delta>0\) there exists a **fixed** witness \(\tau_\delta>0\) and then sufficiently small \(\varepsilon>0\) for which the original walk has end-community finding probability exceeding \(1-\delta\) at the corresponding rescaled integer time. No order-of-limits interchange is assumed for the cases with \(Q<1\).

## Proof
**1. Necessary symmetry from a hypothetical unit supremum.** Let \(C(\tau)=\cos(\tau\sqrt L)\). This is a real symmetric contraction. Its zero eigenvector is
\[
w=\frac{(\sqrt{M_1},\sqrt{M_2},\sqrt{M_3})^{\mathsf T}}{\sqrt{S}},\qquad S=M_1+M_2+M_3.
\]
If \(Q=1\), take a sequence \(\tau_n\) along which \(|\langle e_3,C(\tau_n)e_1\rangle|\to1\). The contraction property forces \(C(\tau_n)e_1\to\sigma e_3\) along a subsequence for \(\sigma\in\{-1,1\}\). Since \(C(\tau_n)w=w\), projection onto \(w\) yields \(\sqrt{M_1}=\sigma\sqrt{M_3}\). All masses are positive, so \(\sigma=1\) and \(M_1=M_3\).

Let \(E_\lambda\) be the orthogonal spectral projection of \(L\) at eigenvalue \(\lambda\). The convergence \(C(\tau_n)e_1\to e_3\) implies
\[
\|E_\lambda e_3\|\leq\|E_\lambda e_1\|
\]
for every eigenvalue, since \(|\cos(\tau_n\sqrt\lambda)|\leq1\). Summing squared norms over the finite spectral resolution gives equality for every eigenvalue because both endpoint basis vectors have norm one. Therefore their diagonal spectral measures coincide, and in particular
\[
L_{11}=\sum_\lambda\lambda\|E_\lambda e_1\|^2
=\sum_\lambda\lambda\|E_\lambda e_3\|^2=L_{33}.
\]
As \(L_{11}=k_1/M_1\) and \(L_{33}=k_2/M_3\), this and \(M_1=M_3\) force \(k_1=k_2\). Hence all asymmetric cases have \(Q<1\), regardless of time.

For an additional explicit obstruction when the outer masses differ, project the two endpoint vectors onto the zero mode and its orthogonal complement and apply Cauchy–Schwarz, using \(\|C(\tau)\|\leq1\):
\[
\left|C(\tau)_{31}\right|\leq
\frac{\sqrt{M_1M_3}+\sqrt{(M_1+M_2)(M_2+M_3)}}{S}<1
\quad(M_1\ne M_3).
\]

**2. Exact three-mode reduction in the symmetric case.** Put \(M_1=M_3=M\), \(M_2=m\), \(k_1=k_2=k\). The three simple eigenvalues of \(L\) are
\[
0,\qquad \omega_a^2=k/M,\qquad \omega_s^2=k/M+2k/m.
\]
The zero-mode, antisymmetric-mode, and high symmetric-mode contributions to the endpoint entry have respective coefficients \(M/(2M+m)\), \(-1/2\), and \(m/[2(2M+m)]\). Therefore
\[
C(\tau)_{31}=\frac{M}{2M+m}
-\frac12\cos(\omega_a\tau)
+\frac{m}{2(2M+m)}\cos(\omega_s\tau).
\]
The sum of the upper bounds of these three terms is one, and the smallest possible value of this real expression is strictly greater than minus one. Thus \(|C(\tau)_{31}|=1\) can occur only when
\[
\cos(\omega_a\tau)=-1,\qquad \cos(\omega_s\tau)=1.
\]
Both coefficients in front of the cosines are strictly positive, so these conditions are also necessary for any sequence with transfer probability approaching one.

**3. Rational/irrational dichotomy and attainment.** Their frequency ratio is \(\rho=\omega_s/\omega_a=\sqrt{1+2M/m}>1\). If \(\rho\) is irrational, Kronecker's density theorem makes the line \((\omega_a\tau,\omega_s\tau)\bmod2\pi\) dense in the two-torus. The target phases \((\pi,0)\) can be approached arbitrarily closely, but cannot be reached at finite time. Hence \(Q=1\) without attainment. If \(\rho=p/q\) in lowest terms, the line is periodic; attainment of the target phases requires \(\rho=2v/(2u+1)\) for integers \(u,v\), exactly the condition that \(p\) is even and \(q\) odd. It is then attained at \(\tau=q\pi/\omega_a\). If this condition fails, the periodic compact orbit misses the unique unit-transfer phase, so continuity gives a strict maximum below one. This also proves the claimed necessary-and-sufficient classification.

**4. Balanced-community quantitative witnesses.** If \(m=M\), then \(\rho=\sqrt3\), while the Pell sequence satisfies \(x_j^2-3q_j^2=1\), \(x_j\) even and \(q_j\) odd. At \(\tau_j=\pi q_j/\omega_a\),
\[
C(\tau_j)_{31}=\frac56+\frac16\cos\bigl(\pi(q_j\sqrt3-x_j)\bigr).
\]
Since \(x_j-q_j\sqrt3=1/(x_j+q_j\sqrt3)<1/(2\sqrt3 q_j)\), the inequalities \(1-(1-u/6)^2\leq u/3\) for \(u=1-\cos\theta\in[0,2]\), and \(1-\cos\theta\leq\theta^2/2\), give
\[
1-|C(\tau_j)_{31}|^2
\leq\frac{\pi^2}{6}(x_j-q_j\sqrt3)^2
<\frac{\pi^2}{72q_j^2}.
\]
Finally, inserting each fixed \(\tau_j\) into the established source reduction proves the corresponding original-walk asymptotic statement. The fixed-witness requirement is essential: the reduction error is not claimed uniform in \(j\to\infty\).

## Verification
The standalone `verification_three_bridge.py` independently diagonalizes weighted three-mass Laplacians, compares 160 randomized parameter choices against the derived closed formula, checks finite samples of the asymmetric mass ceiling, tests both rational parity regimes, verifies exact Pell identities and inequalities, and constructs a full arc-space weighted Grover operator on explicitly connected finite graphs. It reports 307 passing finite checks. For equal-size three-community paths, the direct arc-space probability at one near-perfect Pell witness converges toward the predicted limiting probability \(0.99939149\) as the weak-edge weight decreases. All infinite, arbitrary-time, and double-limit assertions are proved above; these finite checks are not substituted for proofs.

## Relationship to prior work
Hosaka and Segawa, arXiv:2610.07768v1, prove the entire reduction from the original Grover walk to a cosine of the square root of a weighted reduced-graph Laplacian, including the explicit equal-mass three-path formula; **that reduction and formula are prior results**. The new result is the all-parameter **necessary-and-sufficient classification of near-perfect end-community concentration**, including asymmetry obstructions, rational parity exceptions, generic irrational nonattainment, and explicit Pell-rate witness times. Their Section 6 names identifying conditions for concentration in a chosen component as future work.

Vaia, arXiv:2008.01685, already characterizes **exact** perfect pulse transmission for mirror-symmetric mass-spring chains with appropriately alternating commensurate normal-mode parities; the exact rational parity subcase here is an application of that principle and is not asserted to be a newly discovered general criterion. Chan and Zhan, arXiv:2105.03762, supply general spectral/number-theoretic criteria for pretty-good transfer in fixed discrete-time quantum walks. Their generic framework does not give the present weak-edge reduced three-community mass-and-bridge classification or Pell bounds. The source's previous two-component pulsation result, arXiv:2511.12872, does not address a three-component two-frequency path.

## Limitations
The asymptotic weak-edge reduction is imported from a published preprint and not reproved here. The principal theorem classifies the supremum of **leading-order** three-community wave transport, not the supremum over all times for each fixed nonzero weak-edge weight. In particular, \(Q<1\) does not imply any uniform nontransfer bound for the exact walk at times much larger than \(\varepsilon^{-1/2}\). The result covers a reduced path on exactly three nontrivial components, not general reduced graphs. General state-transfer spectral principles are prior work; the originality claim is specific to their synthesis with the recently derived weak-edge Grover asymptotics and explicit classification. Independent external validation has not been performed.

## References
1. T. Hosaka and E. Segawa, *Pulsation of quantum walk on finite graphs*, arXiv:2610.07768v1 (first submitted 2026-10-06), Sections 2–6, especially Theorem 3.1, Eq. (3.11), the three-component path example, and Eq. (5.22). https://arxiv.org/html/2610.07768v1
2. T. Hosaka and E. Segawa, *Pulsation of quantum walk between two arbitrary graphs with weakly connected bridge*, arXiv:2511.12872v1 (2025). https://arxiv.org/abs/2511.12872
3. R. Vaia, *Dispersionless pulse transport in mass-spring chains: All possible perfect Newton's cradles*, arXiv:2008.01685 (2020), especially Sections II–IV. https://arxiv.org/abs/2008.01685
4. A. Chan and H. Zhan, *Pretty good state transfer in discrete-time quantum walks*, arXiv:2105.03762 (2021), especially Section 4. https://arxiv.org/abs/2105.03762
