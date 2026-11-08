# A four-phase constrained fastest-mixing law for wheel networks

## Finding

Let \(m\ge4\) be an integer, and let \(W_{m+1}=K_1\vee C_m\) be the wheel with one hub and \(m\) cyclically ordered rim vertices. Let \(0\le\tau\le1/2\). Among **all** symmetric, entrywise nonnegative, row-stochastic matrices \(P\) supported on the vertices, loops and edges of this wheel and satisfying the **individual edge lower bounds** \(P_{i,i+1}=P_{i+1,i}\ge\tau\) on every rim edge (cyclic indices), minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-\mathbf1\mathbf1^{\mathsf T}/(m+1)\|_2\).

Put
\[
 a_m=4\sin^2(\pi/m),\qquad b_m=4\sin^2(\pi\lfloor m/2\rfloor/m),\qquad
 \vartheta_m=\frac{b_m-a_m}{b_m+a_m},
\]
\[
 \tau_1=\frac{2(m-1)}{m(a_m+b_m)},\qquad
 \tau_2=\frac{2m}{(m+2)a_m+mb_m},\qquad
 \tau_3=\frac{m}{2(m+2)-b_m}.
\]
Then \(0<\tau_1<\tau_2<\tau_3\le1/2\), with \(\tau_3=1/2\) exactly when \(m\) is even. The exact optimal SLEM is the following **continuous four-piece law** (the fourth piece has positive length exactly for odd \(m\)):
\[
 \mu_m^*(\tau)=
 \begin{cases}
 (1-1/m)\vartheta_m,&0\le\tau\le\tau_1,\\
 \frac12(b_m-a_m)\tau,&\tau_1\le\tau\le\tau_2,\\
 \frac{(m+1)b_m\tau-m}{m+2},&\tau_2\le\tau\le\tau_3,\\
 2(m+1)\tau-m,&\tau_3\le\tau\le1/2.
 \end{cases}
\]

An optimal chain has one probability \(p\) on each hub--rim edge and one probability \(q\) on each rim edge; it is uniquely optimal **within this automorphism-invariant two-parameter family**. Its exact probabilities are
\[
 (p,q)=\begin{cases}
 (1/m,\tau_1),&0\le\tau\le\tau_1,\\
 (1-\frac12(a_m+b_m)\tau,\tau),&\tau_1\le\tau\le\tau_2,\\
 ((2-b_m\tau)/(m+2),\tau),&\tau_2\le\tau\le\tau_3,\\
 (1-2\tau,\tau),&\tau_3\le\tau\le1/2.
 \end{cases}
\]
All unspecified off-diagonal entries vanish. The hub holding probability is \(1-mp\), and each rim holding probability is \(1-p-2q\). These probabilities are nonnegative in every displayed regime. The formulas do **not** claim that every optimal non-invariant matrix must equal this chain.

This solves the minimum-rim-exploration-constrained problem, not the previously solved unconstrained wheel problem: the plateau at \(\tau\le\tau_1\) is already known, while the other pieces quantify the sharp price of forcing more local rim transitions. The last regime, involving zero rim holding, occurs only for odd rim lengths.

## Assumptions and scope

The wheel is finite, simple and undirected, with \(m\ge4\) distinct rim vertices; loops are allowed **as holding probabilities**, not as original graph edges. Probabilities are real, symmetric, nonnegative and row-stochastic; stationary distribution is uniform. The lower bound applies separately to every undirected rim edge, not merely to the average. The entire closed range \(0\le\tau\le1/2\) is considered, including reducible boundary chains at \(\tau=1/2\). Feasibility fails for \(\tau>1/2\). The objective is asymptotic eigenvalue-modulus contraction, not total-variation mixing time at a specified finite horizon.

## Proof

**1. Symmetry reduction.** The cyclic and reflection automorphisms of the wheel preserve the nonnegativity, row-sum, support and edge-floor constraints. Since the spectral norm \(\|P-J\|_2\), where \(J=\mathbf1\mathbf1^{\mathsf T}/(m+1)\), is convex and invariant under vertex permutation, group averaging never raises the objective. Therefore a global optimizer exists among invariant chains. Write \(p\) for hub--rim transition, \(q\) for rim--rim transition. Feasibility is exactly \(0\le p\le1/m\), \(q\ge\tau\), and \(p+2q\le1\).

**2. All eigenvalues.** The hub/constant-rim subspace gives eigenvalues \(1\) and \(1-(m+1)p\). Discrete Fourier modes around the rim give \(1-p-4q\sin^2(\pi k/m)\), for \(k=1,\ldots,m-1\). Hence, setting \(a=a_m\), \(b=b_m\),
\[
 \mu(p,q)=\max\left\{|1-(m+1)p|,\;|1-p-aq|,\;|1-p-bq|\right\}.
\]
The Fourier endpoint indices suffice because the eigenvalue depends monotonically on \(\sin^2(\pi k/m)\), and the absolute value of an affine expression is convex.

**3. Rim minimax.** For \(m\ge4\), \(a+b>4\). This is immediate when \(m\) is even (\(b=4\)); for odd \(m\), write \(b=4\cos^2(\pi/(2m))\) and observe \(\sin^2(\pi/m)>\sin^2(\pi/(2m))\). For fixed \(p\), the balanced rim probability \(q_0=2(1-p)/(a+b)\) obeys \(q_0\le(1-p)/2\) and equioscillates the two extreme Fourier values. The optimal rim norm with \(q\ge\tau\) is therefore
\[
 g_\tau(p)=\begin{cases}
 \vartheta_m(1-p),&p\le 1-\frac12(a+b)\tau,\\
 p+b\tau-1,&p\ge 1-\frac12(a+b)\tau,
 \end{cases}
\]
attained by \(q=\max\{\tau,q_0\}\). The left branch is strictly decreasing in \(p\) and the right is strictly increasing.

**4. Suppressing the negative radial mode.** For every \(0\le p\le1/m\), \(g_\tau(p)\ge\vartheta_m(1-p)\ge(1-1/m)\vartheta_m\ge1/m\). The final inequality is equivalent to \((m-2)b\ge ma\). It is an equality at \(m=4\); at \(m=5\) it follows directly from \(a=(5-\sqrt5)/2\), \(b=(5+\sqrt5)/2\); for \(m\ge6\), \(a\le1\), \(b\ge3\), hence \((m-2)b\ge3(m-2)\ge m\). The negative part \((m+1)p-1\), when positive, is at most \(1/m\). Thus only the decreasing radial branch \(1-(m+1)p\) can affect the optimum: minimize \(\max\{1-(m+1)p,g_\tau(p)\}\) over \(0\le p\le p_{\max}=\min\{1/m,1-2\tau\}\).

**5. Three exact switching points.** The rim V-shaped minimum occurs at \(p_{\rm bal}=1-\tfrac12(a+b)\tau\). On its increasing branch, equality with the decreasing radial bound occurs at \(p_{\rm cross}=(2-b\tau)/(m+2)\). Consequently the unique invariant minimizer is
\[
 p_*=\min\{p_{\max},\;\max\{p_{\rm bal},p_{\rm cross}\}\},
\]
where the max/min expression also handles boundary values, because \(p_{\rm cross}\ge0\) on the admissible range. The first switch \(p_{\rm bal}=1/m\) gives \(\tau_1\). The second \(p_{\rm bal}=p_{\rm cross}\) gives \(\tau_2\). The last \(p_{\rm cross}=1-2\tau\) gives \(\tau_3\). Their order follows from \(b\ge a>0\) and \(a+b>4\); specifically \(\tau_1<\tau_2\) reduces to \(mb>(m-2)a\), while \(\tau_2<\tau_3\) reduces to \(a+b>4\). Finally \(\tau_3\le1/2\) is equivalent to \(b\le4\), with equality only for even \(m\). Substitution into \(\mu(p_*,q_*)\) yields the four formulas above. All holding probabilities and boundary coincidences are nonnegative, finishing global optimality and invariant-family uniqueness.

## Verification

`python3 verify_wheel_frontier.py` enumerates independently every vertex of the defining three-variable linear program and compares its optimum with the analytical formula. It also reconstructs the complete Fourier spectrum for each candidate. The standalone verification passed 1,833 numerical LP/spectral comparisons for all integer rim lengths from \(4\) through \(50\), across grid and transition-point thresholds, plus 48 exact-rational linear-program checks for rim lengths \(4\) and \(6\). This finite testing supports, but does not replace, the proof for all integers and all real floors.

For \(m=6\), the three thresholds are \(1/3\), \(3/8\), and \(1/2\); for odd \(m=5\), the terminal fourth regime has a strictly positive interval. These cases check both the familiar unconstrained plateau and the new constraint-induced changes.

## Relationship to prior work

Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, section 5.3.3, pages 28–29) explicitly derive the entire two-parameter Fourier spectrum of the wheel and solve its **unconstrained** fastest-mixing problem; their optimal point is exactly this result's first phase. That spectrum and symmetry reduction are credited, not asserted as new. The additional result here is the exact response to a separate individual-rim-edge **lower-bound** constraint: an explicit four-piece optimal-value law, three switching points, invariant optimal transitions, and a parity-dependent terminal phase.

Boyd, Diaconis and Xiao (SIAM Review 2004) give the general convex/semidefinite formulation, which allows numerical treatment of additional linear constraints but does not state this parametric wheel frontier. Jafarizadeh (arXiv:2501.02117, 2025) studies edge-probability tradeoffs for a **friendship graph**, a different topology and a different edge-objective orientation; that analysis does not imply the wheel thresholds. The constrained wheel result is an explicit specialized resolution, not a claim to invent the general FMMC model, wheel Fourier decomposition, or convex reduction.

## Limitations

The conclusion concerns symmetric Markov kernels with uniform stationary distribution. It does not extend without change to directed, nonreversible or nonuniform-stationary chains. Existence of an invariant optimum is proved; uniqueness is proved **only within the invariant family**, not among all feasible edgewise-asymmetric kernels. At \(\tau=1/2\) the hub is isolated and \(\mu^*=1\), so convergence to the global uniform distribution does not occur. The formula optimizes spectral contraction rather than finite-horizon mixing. The closest earlier paper already contains the full wheel spectrum, making the novelty a constrained sharp Pareto/phase calculation rather than a new spectral decomposition; independent literature priority examination remains useful.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first public version 2007-09-06, section 5.3.3. https://arxiv.org/abs/0709.0955 . DOI: 10.1137/070689413.
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://doi.org/10.1137/S0036144503423264 . Author-hosted text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain on Friendship Graph: Trade-Off between Transition Probabilities among Friends and Convergence Rate*, arXiv:2501.02117, first public 2025-01-03. https://arxiv.org/abs/2501.02117 .
