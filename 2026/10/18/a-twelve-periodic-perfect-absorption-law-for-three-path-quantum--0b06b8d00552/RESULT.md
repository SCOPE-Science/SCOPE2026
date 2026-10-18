# A twelve-periodic perfect-absorption law for three-path quantum theta networks

## Finding

**Theorem (arithmetic terminal trapping).** Let \(m\ge3\) be any integer. Consider the simple graph \(G_m\) with two distinct degree-three terminals \(a,b\), connected by three internally vertex-disjoint paths of edge lengths \(3,3,m\). Let \(A_m\) be its real symmetric adjacency matrix, let \(h\in\mathbb R\setminus\{0\}\), and fix a sink rate \(\kappa>0\). From a localized source state \(\lvert b\rangle\), define the unnormalized no-capture state

\[
\psi(t)=\exp\!\left[-it\left(hA_m-\frac{i\kappa}{2}\lvert a\rangle\langle a\rvert\right)\right]\lvert b\rangle.
\]

Its limiting survival probability exists and is

\[
\boxed{S_m:=\lim_{t\to\infty}\|\psi(t)\|^2=\begin{cases}
\dfrac{2}{2m+1},&m\equiv7\pmod{12},\\[2mm]
0,&m\not\equiv7\pmod{12}.
\end{cases}}
\]

Equivalently, total eventual capture is certain for all lengths except the stated residue class, in which the trapped fraction is exactly \(2/(2m+1)\). This classification is unchanged by varying either nonzero uniform hopping or positive absorber strength. The first exceptional graph has \(m=7\) and trapped fraction \(2/15\); \(m=19\) gives \(2/39\).

## Assumptions and scope

All paths are undirected, simple, and have no internal vertices in common. Their common endpoints are \(a\) and \(b\); an edge length counts edges, not vertices. The graph has \(m+5\) vertices. Each edge receives the same real hopping amplitude \(h\); there are no site energies, magnetic phases, other losses, dephasing, or interactions. The sink is modeled by a single loss term at \(a\) with population removal rate \(\kappa\). The initial state is exactly \(\lvert b\rangle\). The calculated survival is the total unabsorbed population, rather than the probability of remaining at \(b\).

Write \(G=-ihA_m-(\kappa/2)P_a\), where \(P_a=\lvert a\rangle\langle a\rvert\). The conditional state obeys \(\dot\psi=G\psi\), and \(d\|\psi\|^2/dt=-\kappa|\psi_a|^2\). This fixes the otherwise potentially ambiguous factor of two in the absorber normalization. In a Markovian sink extension, \(1-\|\psi(t)\|^2\) is the accumulated absorption probability.

## Proof

**1. Only sink-orthogonal adjacency eigenspaces survive.** Set

\[
\mathcal D=\bigoplus_{\lambda\in\operatorname{spec}(A_m)}\bigl(\ker(A_m-\lambda I)\cap\ker P_a\bigr).
\]

It is a reducing subspace for \(A_m\) and \(G\): for every vector in \(\mathcal D\), both \(P_a\) and its interaction with the sink vanish. The restriction of \(G\) to \(\mathcal D\) is skew-Hermitian. On the orthogonal complement \(\mathcal D^\perp\), every eigenvalue of \(G\) has strictly negative real part. Indeed, an eigenvector \(Gw=zw\) with \(\operatorname{Re}z=0\) would satisfy

\[
0=2\operatorname{Re}\langle w,Gw\rangle=-\kappa\|P_aw\|^2,
\]

so \(P_aw=0\) and then \(A_mw\) is proportional to \(w\), contradicting the definition of \(\mathcal D^\perp\). Finite-dimensional spectral stability, including any Jordan blocks, gives exponential decay on the complement. Consequently,

\[
S_m=\|P_{\mathcal D}\lvert b\rangle\|^2.
\]

**2. A dark eigenvector visible from the source has only two possible eigenvalues.** Rescale away \(h\) and solve \(A_mw=\lambda w\), imposing \(w_a=0\) and denoting \(w_b=z\ne0\). Orient each of the three routes from \(a\) to \(b\). On either short route, write its two internal amplitudes \(u_1,u_2\). The eigenvector recurrence yields

\[
\lambda u_1=u_2,\qquad \lambda u_2=u_1+z.
\]

If \(\lambda^2=1\), these equations force \(z=0\), impossible. Otherwise

\[
u_1=\frac{z}{\lambda^2-1},\qquad
u_2=\frac{\lambda z}{\lambda^2-1}.
\]

On the long route let \(x_j\) be the amplitude at distance \(j\) from \(a\), so \(x_0=0\), \(x_m=z\), and \(x_{j+1}=\lambda x_j-x_{j-1}\). In terms of second-kind Chebyshev polynomials (with \(U_{-1}=0,U_0=1\)),

\[
x_j=x_1U_{j-1}(\lambda/2),\quad
U_{j+1}(\lambda/2)=\lambda U_j(\lambda/2)-U_{j-1}(\lambda/2).
\]

Introduce \(U=U_{m-1}(\lambda/2)\) and \(V=U_{m-2}(\lambda/2)\). Since \(z=x_1U\ne0\), the denominator \(U\) cannot vanish. The eigenvector equation at the absorbing terminal \(a\) is \(2u_1+x_1=0\), and the equation at the source terminal \(b\) is \(\lambda z=2u_2+x_{m-1}\). Substituting gives two necessary equations,

\[
2U=-(\lambda^2-1),\qquad 2V=-\lambda(\lambda^2-3).
\tag{1}
\]

The exact Chebyshev identity

\[
U_{k}(\lambda/2)^2+U_{k-1}(\lambda/2)^2
-\lambda U_k(\lambda/2)U_{k-1}(\lambda/2)=1
\]

follows immediately by induction from the recurrence, starting with \(k=0\). Inserting (1) into that identity and simplifying yields

\[
-(\lambda^2-1)(\lambda^2-3)=0.
\]

The two roots \(\lambda=\pm1\) were excluded by the short-route recurrence. Therefore any dark eigenvector with nonzero source amplitude has \(\lambda=\pm\sqrt3\). This is exhaustive: no numerically inferred spectral cutoff is used.

**3. The exact length residue.** At \(\lambda=\sqrt3=2\cos(\pi/6)\), the identity \(U_{k}(\cos\theta)=\sin((k+1)\theta)/\sin\theta\) turns (1) into

\[
2\sin(m\pi/6)=-1,\qquad
2\sin((m-1)\pi/6)=0.
\]

The second equation forces \(m\equiv1\pmod6\); the first selects exactly \(m\equiv7\pmod{12}\). At \(\lambda=-\sqrt3\), the parity law \(U_k(-y)=(-1)^kU_k(y)\), together with the vanishing of \(U_{m-2}\), gives precisely the same residue. Thus when \(m\not\equiv7\pmod{12}\), every dark eigenvector is orthogonal to \(\lvert b\rangle\), and therefore \(S_m=0\), even if additional sink-dark states with zero source overlap exist.

**4. Exact trapped weight at the exceptional lengths.** Suppose \(m\equiv7\pmod{12}\). For each eigenvalue \(\lambda_\pm=\pm\sqrt3\), set \(z=1\), put \(u_1=1/2\), \(u_2=\lambda_\pm/2\) on both short routes, and put on the long route

\[
x_j=-2(\pm1)^{j-1}\sin(j\pi/6),\qquad 1\le j\le m-1.
\]

The endpoint and interior eigenvector equations just proved are satisfied, giving a sink-dark eigenvector \(w_\pm\) with \((w_\pm)_b=1\). Because \(m-1\) is divisible by six, \(\sum_{j=1}^{m-1}\sin^2(j\pi/6)=(m-1)/2\). Hence

\[
\|w_\pm\|^2=1+2\left(\frac14+\frac34\right)+4\frac{m-1}{2}=2m+1.
\]

For either eigenvalue, the equations above also show that a dark eigenvector with \(w_b=0\) must vanish on both short routes and then on the long route (because \(U=-1\ne0\)). Thus each of these dark eigenspaces is one-dimensional. The normalized eigenvectors at \(\lambda_+\) and \(\lambda_-\) are orthogonal because their eigenvalues differ. They each contribute exactly \(1/(2m+1)\) to the source's squared dark projection. All remaining dark modes have zero source amplitude by step 2. Therefore \(S_m=2/(2m+1)\), proving the theorem. \(\square\)

## Verification

The accompanying `verification/check_theta.py` evaluates an exact Chebyshev polynomial identity and its two endpoint conditions over 81 integer lengths, constructs adjacency matrices directly, and compares the theorem with numerical spectral projectors for every length from \(3\) through \(65\). It also checks explicitly constructed dark eigenvectors at five exceptional lengths and computes sample long-time dynamics from the non-Hermitian loss Hamiltonian at two choices of hopping and sink strength. On the specified dependency versions the run reports `VERIFY_OK exact_length_cases=81 spectral_projectors=63 dark_eigenvectors=10 finite_time_dynamics=8 max_projector_error=2.91e-16`. Run from the package root with `python verification/check_theta.py` after installing `verification/requirements.txt`.

These checks are finite corroboration. The all-integer classification and the strict long-time limit follow from the preceding analytic proof, not from finite enumeration or a time-cutoff test. Matrix exponentials at finite times approximate, rather than equal, the infinite-time limit.

## Relationship to prior work

The sink-invisible invariant-subspace mechanism is established in Caruso, Chin, Datta, Huelga and Plenio (2009), principally for fully connected excitonic networks. Agliari (2011) studies quantum trapping on random graphs. Wang, Huang, Belardo and Li Marzi (2009) examine the **same theta graph class**, but their objective is adjacency cospectrality, not source-to-sink absorption or rooted dark-state overlap. In that paper's notation the present \(G_m\) is \(\theta_{2,2,m-1}\), since its parameters count path vertices differently. Razzoli, Paris and Bordone (2020/2021) give general trapped-subspace and transport-efficiency methods, with explicit calculations for complete bipartite, strongly regular, joined-complete and simplex-of-complete graphs. Their general structural method is consistent with step 1 but does not state the twelve-periodic terminal classification and rational trapped fraction for \(G_m\).

The contribution asserted here is **only** the explicit infinite-length arithmetic classification for this adjacency theta family and the exact source-specific absorption probability, not a new general theory of dark subspaces or Chebyshev recurrences. General projector methods may provide alternate derivations. Literature search cannot establish exhaustive global publication priority.

## Limitations

This theorem assumes a symmetric real adjacency Hamiltonian, a localized initial state at the terminal opposite the absorber, no other environmental mechanisms, and infinite time. A graph-Laplacian Hamiltonian differs at the degree-three terminals and is not covered; neither are asymmetric branch hoppings, phase disorder, finite-time capture bounds or multipartite excitation dynamics. Source-invisible dark eigenstates can exist even when the source is perfectly absorbed; the theorem does not assert that the entire graph has no dark eigenstates. The limiting fraction is independent of positive sink strength, but convergence speed need not be. The exact novelty comparison against all published and unpublished results is not independently certified.

## References

1. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, M. B. Plenio, “Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport,” arXiv:0901.4454, first public 2009-01-28, https://arxiv.org/abs/0901.4454 .
2. J. Wang, Q. Huang, F. Belardo, E. M. Li Marzi, “On the spectral characterization of theta graphs,” MATCH Communications in Mathematical and in Computer Chemistry 62 (2009), 581–598, https://match.pmf.kg.ac.rs/electronic_versions/Match62/n3/match62n3_581-598.pdf .
3. E. Agliari, “Trapping of Continuous-Time Quantum Walks on Erdős–Rényi Graphs,” arXiv:1102.3994, https://arxiv.org/abs/1102.3994 .
4. L. Razzoli, M. G. A. Paris, P. Bordone, “Transport efficiency of continuous-time quantum walks on graphs,” arXiv:2011.13794 (2020), Entropy 23 (2021), 85, https://arxiv.org/abs/2011.13794 .
