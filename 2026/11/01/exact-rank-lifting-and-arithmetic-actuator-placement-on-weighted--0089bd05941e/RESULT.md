# Exact rank-lifting and arithmetic actuator placement on weighted cyclic combs

## Finding

**Theorem (complete terminal-leaf Kalman rank).** Let \(n\ge3\) and \(\ell\ge1\) be arbitrary integers. Form the undirected weighted cyclic comb \(G_{n,\ell}\) by taking the cycle on \(\mathbb Z/n\mathbb Z\), attaching to every cycle vertex an identical rooted path of \(\ell\) edges, assigning positive common cycle conductance \(a\), and assigning positive conductances \(b_1,\ldots,b_\ell\) at respective depths along every attached path. The total number of vertices is \(N=n(\ell+1)\). Write \(L\) for the symmetric combinatorial conductance Laplacian.

Choose any nonempty set \(S\subseteq\mathbb Z/n\mathbb Z\), and put one independent coordinate actuator at the terminal vertex \((s,\ell)\) for each \(s\in S\). Let \(B_S\) be the resulting \(N\times|S|\) input matrix. Fix \(s_0\in S\) and define
\[
g=\gcd\bigl(n,\{2(s-s_0):s\in S\}\bigr).
\]
This nonnegative greatest common divisor is independent of \(s_0\), and is \(n\) when \(S\) is a singleton. Then, for every admissible choice of all positive conductances,
\[
\boxed{\operatorname{rank}[B_S,LB_S,\ldots,L^{N-1}B_S]
=(\ell+1)\left(n-\left\lfloor\frac{g-1}{2}\right\rfloor\right).}
\]
The unobservable (and uncontrollable) eigenvalues consist precisely of one mode in each of the \(\ell+1\) Jacobi branches for each frequency pair \(k,n-k\) such that \(1\le k<n/2\) and \(n\mid2k(s-s_0)\) for all \(s\in S\).

In particular, **one** terminal-leaf input always fails for \(n\ge3\), while **two** suffice. For distinct roots \(p,q\), the pair of terminal-leaf inputs is controllable exactly when
\[
\gcd\bigl(n,2(q-p)\bigr)\le2.
\]
Equivalently, the separation is coprime to \(n\) when \(n\) is odd and coprime to \(n/2\) when \(n\) is even. The number of unordered successful pairs equals
\[
\begin{cases}
\dfrac n2\varphi(n),&n\text{ odd},\\[3pt]
n\varphi(n/2),&n\text{ even}.
\end{cases}
\]
Thus the exact deficiency is the number of invisible cycle frequency pairs **multiplied by the full length \(\ell+1\) of each rooted path**, without any exceptional positive conductance ratios.

## Assumptions and scope

All edge weights are positive real numbers; each level \(j\) of every attached path has the same conductance \(b_j\), but the \(\ell\) conductances may be mutually different. The cycle-edge conductance \(a\) is common. Actuators have independent scalar inputs, one per selected terminal leaf; the state equation is \(\dot x=-Lx+B_Su\). All rank assertions hold over \(\mathbb R\) (equivalently, over \(\mathbb C\)). No claim is made for arbitrarily independent edge weights, actuator coupling, a non-path decoration, or a uniformly bounded controllability Gramian.

## Proof

**Step 1: exact fiber decomposition.** Write \(V(G_{n,\ell})=\{(s,j):s\in\mathbb Z/n\mathbb Z,0\le j\le\ell\}\). Let \(J\) be the \((\ell+1)\times(\ell+1)\) weighted path Laplacian with conductance \(b_j\) between levels \(j-1\) and \(j\). Denote the depth-zero basis vector by \(e_0\). For \(0\le k<n\), put
\[
\mu_k=2-2\cos(2\pi k/n),\qquad
H(\mu)=J+a\mu e_0e_0^{\mathsf T}.
\]
The unitary discrete Fourier transform in the cyclic variable conjugates \(L\) to \(\bigoplus_{k=0}^{n-1}H(\mu_k)\). Hence every eigenvalue arises in one of the \(\ell+1\) ordered eigenvalue branches of \(H(\mu_k)\).

**Step 2: no hidden interbranch resonance.** Let \(D\) be the principal submatrix of \(J\) obtained by removing its depth-zero row and column. Because every \(b_j>0\), both \(D\) and \(H(\mu)\) are real symmetric irreducible tridiagonal (Jacobi) matrices. Every eigenvector of \(H(\mu)\) has nonzero depth-zero and nonzero terminal coordinates: the eigenvalue equation at either endpoint forces the next coordinate to vanish if the endpoint vanishes, and induction along the path would force the whole eigenvector to vanish. The eigenvalues of \(D\) and \(H(\mu)\) cannot coincide: equality in Cauchy interlacing would produce an eigenvector of \(H(\mu)\) vanishing at depth zero (alternatively use the three-term characteristic-polynomial recurrence and positivity of off-diagonal entries). Thus Cauchy interlacing is strict. Writing the \(\ell\) eigenvalues of \(D\) as \(\delta_1<\cdots<\delta_\ell\), we obtain, for every \(\mu\ge0\),
\[
\lambda_1(\mu)<\delta_1<\lambda_2(\mu)<\cdots<\delta_\ell<\lambda_{\ell+1}(\mu).
\]
In particular distinct branch labels can never have the same eigenvalue, even at different \(\mu\).

Each \(\lambda_j(\mu)\) is simple and differentiable. For a normalized eigenvector \(v_j(\mu)\), Hellmann--Feynman differentiation gives
\[
\lambda_j'(\mu)=a|v_j(\mu)_0|^2>0.
\]
Consequently the only repeated eigenvalues of \(L\) occur in Fourier pairs \(k,n-k\), since \(\mu_k=\mu_{n-k}\) and \(\mu_k\) is strictly increasing for \(0\le k\le\lfloor n/2\rfloor\). Each such eigenvalue has multiplicity exactly two; the modes \(k=0\) and, for even \(n\), \(k=n/2\) are simple.

**Step 3: the leaf observation is a cyclic character matrix.** For every fiber eigenvector \(v_j(\mu_k)\), the global eigenvector takes the separated form
\[
\psi_{k,j}(s,t)=n^{-1/2}e^{2\pi iks/n}v_j(\mu_k)_t.
\]
Every terminal coordinate \(v_j(\mu_k)_\ell\) is nonzero by Step 2. On the double eigenspace generated by \(\psi_{k,j}\) and \(\psi_{n-k,j}\), restriction to the actuated leaves is therefore, after nonzero column scaling, the matrix with rows
\[
\left(e^{2\pi iks/n},e^{-2\pi iks/n}\right),\quad s\in S.
\]
Its two columns are dependent exactly when all ratios of paired entries are equal, i.e. when \(e^{4\pi ik(s-s_0)/n}=1\) for every \(s\in S\), equivalently \(n\mid 2k(s-s_0)\). Each simple eigenspace is observed by any one leaf.

**Step 4: exact count and Kalman rank.** The integers \(2(s-s_0)\) together with \(n\) generate \(g\mathbb Z\). Thus the simultaneous congruences of Step 3 are equivalent to \(n\mid kg\), or \((n/g)\mid k\). For \(1\le k<n/2\), there are exactly \(\lfloor(g-1)/2\rfloor\) such multiples, because \(n/g\) divides \(n\). Each yields precisely one invisible dimension in each of the \(\ell+1\) disjoint eigenvalue branches. For a real symmetric matrix, polynomial spectral interpolation shows that the block Kalman matrix spans exactly the direct sum of projections of \(\operatorname{im}B_S\) to the distinct eigenspaces. Its rank is therefore the total dimension \(n(\ell+1)\) minus \((\ell+1)\lfloor(g-1)/2\rfloor\), proving the formula.

**Step 5: pairs and count.** For \(S=\{p,q\}\), full rank means \(g=1\) or \(2\), equivalently \(\gcd(n,2(q-p))\le2\). When \(n\) is odd this is \(\gcd(n,q-p)=1\); when \(n\) is even it is \(\gcd(n/2,q-p)=1\). Every adjacent pair passes, so two inputs suffice. A singleton gives \(g=n\), so one fails for \(n\ge3\). For odd \(n\), there are \(\varphi(n)\) successful nonzero differences per starting vertex, giving \(n\varphi(n)/2\) unordered pairs. For even \(n\), exactly \(2\varphi(n/2)\) residues modulo \(n\) yield an allowed difference, giving \(n\varphi(n/2)\) unordered pairs. This completes the proof.

## Verification

Run `python verify.py` with Python, NumPy and SymPy installed. The program builds the full weighted graph Laplacian independently of the Jacobi fiber matrices, checks numerical eigenspectra and eigenspace-wise PBH ranks for multiple lengths, weight profiles, cycle sizes and multisensor sets, verifies six characteristic-polynomial factorizations exactly, and verifies forty more controllability ranks by exact integer/rational matrix arithmetic. The bundled run reports **1,126 passed checks**. Finite tests do not establish the all-parameter theorem; Steps 1--5 supply the proof.

## Relationship to prior work

Parlangeli and Notarstefano [1, Section IV-B and Theorem IV.10] establish gcd-based reachability and observability for **plain cycles**, including adjacent-pair sufficiency. Those facts and the Fourier/PBH apparatus are prior art and are not claimed as discoveries here. The new claim concerns the complete rank (not only a controllability decision) of the **rooted product of a cycle with arbitrary-length positive weighted paths**, for every terminal-leaf subset and every positive level-wise weight profile. The noncollision of entire Jacobi bands explains why this is a weight-invariant multiplicative rank law rather than an unverified reuse of the plain-cycle criterion.

Suzuki [2] examines infinite periodic lattices decorated by pendant edges, using a normalized transition operator and spectral-band questions; it does not present this finite-input controllability classification. A published finite-cycle two-sensor frame result [3] concerns unadorned cycles and optimizes demixed low-pass frame bounds, a different operator and objective. Liu and Ji [4] state in their abstract that they also analyze further graph families generated from paths and cycles; the accessible abstract does not identify whether any includes this exact rooted-product family, so source overlap with their inaccessible full text remains a priority risk. No conclusion of noncoverage is drawn from the abstract alone.

## Limitations

The arithmetic law relies on **identical** path decorations and identical weights at corresponding levels, plus independent terminal-leaf actuators. Irregularity among the paths, non-path decorations or general block inputs may create additional eigenspace collisions or change the leaf restrictions. Exact rank is not a robustness, damping, control-energy or uniform numerical conditioning guarantee. The documented overlap search is evidence-based, not an exhaustive uniqueness certificate; the complete Liu--Ji article and potentially undiscovered specialist work remain an originality risk. No independent mathematical audit has been performed.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, publicly submitted 16 September 2011, https://arxiv.org/html/1109.3556v1 .
2. A. Suzuki, *Spectrum of the Laplacian on a covering graph with pendant edges I: The one-dimensional lattice and beyond*, arXiv:1304.4315v1, publicly submitted 16 April 2013, https://arxiv.org/html/1304.4315v1 .
3. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818 .
4. X. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, Int. J. Robust Nonlinear Control 28 (2018), 296--309, first published 30 June 2017, https://doi.org/10.1002/rnc.3870 .
