# Exact fastest-mixing probabilities on Möbius ladders

## Finding
For every integer \(m\ge3\), let the Möbius ladder \(M_{2m}\) have vertex set \(\mathbb Z/(2m)\mathbb Z\), rim edges \(\{i,i+1\}\), and \(m\) antipodal rungs \(\{i,i+m\}\). Among **all** symmetric, entrywise-nonnegative stochastic matrices \(P\) whose off-diagonal support is contained in these edges, the minimum second-largest eigenvalue modulus (SLEM)
\[
\mu(P)=\max_{j=2,\ldots,2m}|\lambda_j(P)|
       =\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{2m}\right\|_2
\]
is the following exact value. Put
\[
u=2\left(1-\cos\frac{\pi}{m}\right),\qquad
v=2\left(1-\cos\frac{2\pi}{m}\right),\qquad
\Delta=v-u>0.
\]
Then
\[
\boxed{\quad
\mu_m^*=\begin{cases}
1-\dfrac{v}{2+\Delta},&m\text{ even},\\[5pt]
1-\dfrac{2v}{4+\Delta+v},&m\text{ odd}.
\end{cases}\quad}
\]
One optimal matrix assigns a common rim probability \(a_m\) and a common rung probability \(b_m\), with
\[
\boxed{\quad
(a_m,b_m)=\begin{cases}
\left(\dfrac1{2+\Delta},\dfrac{\Delta}{2(2+\Delta)}\right),&m\text{ even},\\[5pt]
\left(\dfrac2{4+\Delta+v},\dfrac{\Delta}{4+\Delta+v}\right),&m\text{ odd}.
\end{cases}\quad}
\]
The remaining probability \(1-2a_m-b_m\) is a **strictly positive holding probability**. The displayed pair is the unique optimum among rotation-invariant matrices. No uniqueness claim is made for arbitrary nonsymmetric allocations of edge probabilities.

Moreover,
\[
 b_m=\frac{3\pi^2}{4m^2}+O(m^{-4}),\qquad
 1-\mu_m^*=\frac{2\pi^2}{m^2}+O(m^{-4}),
\]
with parity-dependent sharper expansions
\[
1-\mu_m^*=\begin{cases}
\dfrac{2\pi^2}{m^2}-\dfrac{11\pi^4}{3m^4}+O(m^{-6}),&m\text{ even},\\[5pt]
\dfrac{2\pi^2}{m^2}-\dfrac{25\pi^4}{6m^4}+O(m^{-6}),&m\text{ odd}.
\end{cases}
\]
The fastest chain on the bare \(2m\)-cycle has SLEM \(\mu_{\mathrm{cycle}}^*=(4-u)/(4+u)\); hence
\[
\boxed{\displaystyle\lim_{m\to\infty}
\frac{1-\mu_m^*}{1-\mu_{\mathrm{cycle}}^*}=4.}
\]
Thus optimally weighted antipodal shortcuts quadruple the leading-order spectral gap even though each optimal rung probability vanishes quadratically with graph size.

## Assumptions and scope
Vertices are indexed modulo \(2m\); repeated edges do not occur when \(m\ge3\). Transition matrices are real symmetric; entrywise nonnegativity, unit row sums, and allowed support are the only feasibility restrictions. All rim and rung weights are independently adjustable in the original optimization. A diagonal hold is allowed. The spectral gap refers to \(1-\mu(P)\), with \(\mu(P)\) the absolute nontrivial spectral radius, not merely \(1-\lambda_2(P)\). The comparison cycle permits arbitrary symmetric edge probabilities and holds.

## Proof
**1. Reduce without restricting the problem.** Let \(J=\mathbf1\mathbf1^{\mathsf T}/(2m)\). The map \(P\mapsto\|P-J\|_2\) is convex and invariant under conjugation by rotations of \(\mathbb Z/(2m)\mathbb Z\). Averaging any feasible \(P\) over all \(2m\) rotations gives a feasible circulant matrix with no larger SLEM. Such a matrix has equal probability \(a\ge0\) on every rim edge, equal probability \(b\ge0\) on every antipodal rung, and diagonal \(1-2a-b\ge0\). The two edge classes are distinct for \(m\ge3\).

**2. Fourier spectrum.** With \(k=0,1,\ldots,2m-1\), the discrete Fourier eigenvalues are
\[
\lambda_k=1-a t_k-b\bigl(1-(-1)^k\bigr),\qquad
 t_k=2\left(1-\cos\frac{\pi k}{m}\right).
\]
The trivial eigenvalue is \(\lambda_0=1\). For nontrivial odd modes, \(u\le t_k\le\eta\), where \(\eta=4-u\) when \(m\) is even (maximum at \(k=m\pm1\)), and \(\eta=4\) when \(m\) is odd (maximum at \(k=m\)). Even nonzero modes satisfy \(v\le t_k\le4\).

**3. Three-mode global lower bound.** Every rotation-invariant feasible matrix obeys
\[
\mu\ge\max\{g_1,g_2,g_3\},\quad
 g_1=1-ua-2b,\quad g_2=1-va,\quad g_3=-1+\eta a+2b.
\]
Set
\[
\rho=\frac{v}{2v+\eta-u},\qquad
\sigma=\frac{\eta-u}{2v+\eta-u}.
\]
Because \(m\ge3\), \(v>0\) and \(\eta>u\); thus \(\rho,\sigma>0\) and \(2\rho+\sigma=1\). Direct cancellation gives
\[
\rho g_1+\sigma g_2+\rho g_3=\sigma.
\]
Consequently every feasible invariant matrix has \(\mu\ge\sigma\), with equality possible only if all three inequalities are equalities. Solving \(g_1=g_2=g_3\) yields
\[
a=\frac2{\eta+\Delta+v},\qquad
b=\frac{\Delta}{\eta+\Delta+v}=\frac{a\Delta}{2},\qquad
\mu=1-av=\sigma.
\]
All three positive multipliers make this the **unique** minimizing pair within the invariant class. Substituting the two parity formulas for \(\eta\) gives the stated expressions.

**4. Verify feasibility and every mode.** Here \(a,b>0\), and
\[
2a+b=\frac{4+\Delta}{\eta+\Delta+v}<1,
\]
since \(\eta+v>4\): for odd \(m\), \(\eta=4\) and \(v>0\); for even \(m\), \(\eta=4-u\) and \(v>u\). The odd Fourier eigenvalues lie between \(g_1=\mu\) and \(-g_3=-\mu\). Every even nonzero eigenvalue lies between \(1-4a\) and \(1-va=\mu\). The remaining needed bound \(1-4a\ge-\mu\) is equivalent to \(2\ge a(4+v)\). For odd \(m\), this follows from \(\Delta>0\). For even \(m\), it is equivalent to \(v\ge2u\), which follows from
\[
\frac vu=4\cos^2\frac{\pi}{2m}\ge3>2.
\]
Therefore the proposed matrix attains the lower bound \(\sigma\) and is a global optimum, including against all nonsymmetric feasible matrices by step 1.

**5. Cycle baseline and asymptotics.** For the bare \(2m\)-cycle, Fourier extremes are \(1-ux\) and \(1-4x\) for edge probability \(0\le x\le1/2\). Balancing them gives \(x=2/(4+u)\) and \(\mu_{\mathrm{cycle}}^*=(4-u)/(4+u)\); the balancing point is feasible, and the extremes imply global optimality after rotational averaging. Taylor expansion of \(u=2(1-\cos(\pi/m))\), \(v=2(1-\cos(2\pi/m))\), and the explicit expressions yields the displayed \(m^{-2}\), \(m^{-4}\), and gap-ratio conclusions.

## Verification
The standalone `verify.py` constructs the transition matrices, independently diagonalizes them, checks all Fourier modes and the positive three-mode dual certificate, and solves the full two-variable Fourier linear program with SciPy. With fixed seed it also compares 1,200 edge-asymmetric feasible allocations directly against the derived optimum. The reproducible structured output is in `verification_output.json`. These finite checks are corroboration, not a substitute for the analytic all-\(m\) proof.

## Relationship to prior work
Boyd, Diaconis, and Xiao established the general convex/semidefinite formulation of fastest-mixing symmetric chains [1]. Boyd, Diaconis, Parrilo, and Xiao derived graph-symmetry reductions and explicit solutions for edge-transitive graphs, cycles, wheels, and several other families [2]. Their wheel Fourier analysis motivates the technique, but the Möbius ladder has antipodal matching rather than a universal hub. For \(m\ge4\), its two non-equivalent edge orbits and the competing odd/even Fourier extremizers require the displayed parity-dependent solution; the special case \(m=3\) is the previously understood edge-transitive \(K_{3,3}\). Jakobson and Rivin identify the eight-vertex Möbius ladder in a different spanning-tree extremal context [3]; that does not determine the optimal stochastic edge probabilities. The explicit formulas, unique invariant optimizer, and fourfold gap gain are the claim assessed here, not the general Fourier diagonalization or abstract solvability of the SDP.

## Limitations
Uniqueness is proved only in the rotation-invariant subspace. The chain is reversible with uniform stationary measure; arbitrary nonuniform stationary measures, directed transitions, mixing-time prefactors, and worst-case finite-time total variation are outside the claim. Broad optimization frameworks might allow this family to be solved algorithmically and publication priority is not certified. Asymptotic statements use fixed topology family with \(m\to\infty\). The inverse spectral radius alone does not bound the finite-time mixing time without its usual constants.

## References
[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264. Public full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first public arXiv submission 2007-09-06), SIAM J. Optimization 20 (2009), 792–819. Public full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .

[3] D. Jakobson, I. Rivin, *On Some Extremal Problems in Graph Theory*, arXiv:math/9907050v1 (1999-07-08), especially Sections 2.4 and 5. Public text: https://arxiv.org/html/math/9907050v1 .
