# The exact fastest symmetric Markov chain on every sunlet graph

## Finding

Let \(G_m=C_m\circ K_1\) be the **sunlet graph** with \(m\ge3\): the rim vertices \(u_0,\ldots,u_{m-1}\) form a cycle, and each \(u_j\) has exactly one pendant neighbor \(v_j\). Self-loops are allowed as holding probabilities. Among **all** nonnegative symmetric stochastic matrices \(P\) supported on the edges and diagonal of \(G_m\), minimize the second-largest eigenvalue modulus
\[
\mu(P)=\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{2m}\right\|_2.
\]
Write
\[
\delta_m=1-\cos\!\left(\frac{2\pi}{m}\right),\qquad
\alpha_m=\frac{4-(2-\delta_m)\sqrt{\delta_m}}{2(4+\delta_m^2)},\qquad
\beta_m=\frac{\delta_m^2+(2-\delta_m)\sqrt{\delta_m}}{4+\delta_m^2}.
\]
Then the **global optimum** is
\[
\boxed{\mu_m^*=\frac{2(2-\delta_m+\delta_m^{3/2})}{4+\delta_m^2}}.
\]
It is attained by assigning transition probability \(\alpha_m\) to every rim edge in **both** directions, probability \(\beta_m\) to every spoke in both directions, holding probability zero at each rim vertex, and holding probability \(1-\beta_m\) at each pendant vertex. These parameters satisfy \(2\alpha_m+\beta_m=1\) and are strictly positive. This is the **unique optimizer invariant under all dihedral symmetries** of the rim. The result does **not** assert that every (possibly asymmetric) global optimizer is identical.

For increasing rim size,
\[
\beta_m=\frac{\pi}{\sqrt2\,m}+O(m^{-3}),\qquad
\alpha_m=\frac12-\frac{\pi}{2\sqrt2\,m}+O(m^{-3}),
\]
\[
\boxed{1-\mu_m^*=\frac{\pi^2}{m^2}-\frac{\sqrt2\pi^3}{m^3}+O(m^{-4}).}
\]
The spoke probability is therefore of order \(m^{-1}\), while the optimal spectral gap is of order \(m^{-2}\). On the eight-vertex sunlet \(G_4\), the exact optimal values are \(\alpha_4=3/10\), \(\beta_4=2/5\), and \(\mu_4^*=4/5\).

## Assumptions and scope

Every \(m\) is an integer at least three. All edge probabilities may vary independently in the original optimization. The admissible \(P\) is a real \(2m\)-by-\(2m\) matrix with \(P=P^{\mathsf T}\), \(P\mathbf1=\mathbf1\), all entries nonnegative, and zero off-diagonal entries on nonedges. Diagonal holding probabilities are unconstrained except by nonnegativity and row sums. This is symmetric fastest mixing to the uniform equilibrium measure. The spectral norm is the Euclidean operator norm, and \(\mu(P)\) is the maximum absolute eigenvalue other than the trivial stationary eigenvalue, counted with multiplicity; disconnected choices have \(\mu(P)=1\).

## Proof

**1. Reduction is globally legitimate.** Put \(J=\mathbf1\mathbf1^{\mathsf T}/(2m)\). Because \(PJ=JP=J\) for any admissible symmetric stochastic \(P\), one has \(\mu(P)=\|P-J\|_2\), a convex function of \(P\). The dihedral automorphism group \(D_m\) permutes the \(m\) rim-spoke pairs. For any feasible \(P\), its conjugate by each automorphism is feasible and has the same objective. Averaging these conjugates preserves feasibility and cannot increase the objective by convexity of the norm. Thus at least one **global** optimum is dihedrally invariant; the edge orbits are exactly the rim edges and spokes.

Let \(\alpha\) be the common rim-edge probability and \(\beta\) the common spoke probability. Feasibility is exactly
\[
0\le\alpha\le\frac12,\qquad0\le\beta\le1-2\alpha.
\]
The rim holding probability is \(1-2\alpha-\beta\) and the leaf holding probability is \(1-\beta\).

**2. Exact Fourier blocks.** With rim coordinates followed by leaves, the invariant matrix is
\[
P=\begin{pmatrix}
(1-\beta-2\alpha)I+\alpha A(C_m)&\beta I\\
\beta I&(1-\beta)I
\end{pmatrix}.
\]
The Fourier character of order \(j\) on the rim has adjacency eigenvalue \(2\cos(2\pi j/m)\). Put \(d_j=1-\cos(2\pi j/m)\). On that Fourier sector the real symmetric \(2\)-by-\(2\) block is
\[
B_j=\begin{pmatrix}
1-\beta-2\alpha d_j&\beta\\
\beta&1-\beta
\end{pmatrix},
\]
with eigenvalues
\[
\lambda_\pm(d_j)=1-\beta-\alpha d_j\pm\sqrt{\beta^2+\alpha^2d_j^2}.
\]
For \(j=0\) these are \(1\) and \(1-2\beta\). The smallest nonzero \(d_j\) is \(\delta=\delta_m\), where \(0<\delta\le3/2\); every \(d_j\) belongs to \([\delta,2]\). Hence \(\mu(P)\ge\lambda_+(\delta)\ge0\), regardless of whether other eigenvalues are larger in modulus.

**3. Saturating rim capacity optimizes the lower bound.** For fixed \(\alpha>0\), the expression
\[
\lambda_+(\delta)=1-\beta-\alpha\delta+\sqrt{\beta^2+\alpha^2\delta^2}
\]
is strictly decreasing in \(\beta\ge0\), because its derivative is \(-1+\beta/\sqrt{\beta^2+\alpha^2\delta^2}<0\). At \(\alpha=0\) the expression equals one, so it cannot be a strict global optimum. Thus the best lower bound for fixed \(\alpha\) occurs at \(\beta=1-2\alpha\).

In fact the lower bound becomes the **exact** SLEM everywhere on that boundary. With \(\beta=1-2\alpha\), the eigenvalues become
\[
\lambda_\pm(d)=\alpha(2-d)\pm\sqrt{\beta^2+\alpha^2d^2}.
\]
The function \(\lambda_+(d)\) is nonincreasing on \([0,2]\); thus its largest nonstationary member is \(\lambda_+(\delta)\). Also, since \(d\le2\),
\[
-\lambda_-(d)\le\sqrt{\beta^2+4\alpha^2}=\lambda_+(2)\le\lambda_+(\delta).
\]
For \(\lambda_-(d)\ge0\), plainly \(\lambda_-(d)\le\lambda_+(d)\le\lambda_+(\delta)\). Finally,
\[
|1-2\beta|=|4\alpha-1|\le\sqrt{\beta^2+4\alpha^2}\le\lambda_+(\delta),
\]
because \((\beta^2+4\alpha^2)-(4\alpha-1)^2=4\alpha(1-2\alpha)\ge0\). Consequently, for every \(\alpha\in[0,1/2]\) with \(\beta=1-2\alpha\),
\[
\mu(P)=f_\delta(\alpha):=(2-\delta)\alpha+\sqrt{(1-2\alpha)^2+\delta^2\alpha^2}.
\]
For an arbitrary feasible pair, its SLEM is at least \(f_\delta(\alpha)\). Minimizing this scalar function therefore solves the original unrestricted-matrix problem, by Step 1.

**4. Unique exact minimum.** The square root is the Euclidean norm of the affine vector \((1-2\alpha,\delta\alpha)\). It is strictly convex in \(\alpha\), as its second derivative is \(\delta^2/[(1-2\alpha)^2+\delta^2\alpha^2]^{3/2}>0\). Therefore \(f_\delta\) is strictly convex. Its derivatives at the endpoints are \(f_\delta'(0)=-\delta<0\) and \(f_\delta'(1/2)=2>0\). Thus there is a unique stationary point in \((0,1/2)\), which is the unique invariant minimizer.

Differentiation gives
\[
0=2-\delta+\frac{(4+\delta^2)\alpha-2}{\sqrt{(1-2\alpha)^2+\delta^2\alpha^2}}.
\]
Direct substitution of the claimed \(\alpha_m\) shows both this identity and
\[
\sqrt{(1-2\alpha_m)^2+\delta^2\alpha_m^2}=\frac{\sqrt\delta}{2}.
\]
Since \(0<\delta\le3/2\), the displayed \(\alpha_m\) lies strictly between \(0\) and \(1/2\). Inserting it into \(f_\delta\) yields the stated \(\mu_m^*\). The corresponding \(\beta_m=1-2\alpha_m\) gives the listed holding probabilities. Uniqueness among invariant matrices follows from strict convexity and the strict decrease in \(\beta\) for \(\alpha>0\).

**5. Asymptotic expansion.** Put \(\delta=2\sin^2(\pi/m)=2\pi^2m^{-2}+O(m^{-4})\). The exact formulas yield
\[
\alpha_m=\frac12-\frac{\sqrt\delta}{4}+O(\delta^{3/2}),\quad
\beta_m=\frac{\sqrt\delta}{2}+O(\delta^{3/2}),\quad
\mu_m^*=1-\frac\delta2+\frac{\delta^{3/2}}2+O(\delta^2).
\]
Substitution proves all stated expansions, including the order of the remainder.

## Verification

The accompanying `verify.py` builds the full \(2m\)-state transition matrices and independently diagonalizes them, comparing against the Fourier eigenvalues and exact optimum. It also evaluates feasible nonsymmetric edge assignments and compares sample values with the global analytic lower bound; this **does not** constitute a finite proof of global optimality. It checks the stationary equation and algebraic radical formulas over many sizes, plus the exact \(m=4\) rational example. Run `OPENBLAS_NUM_THREADS=1 python verify.py` with NumPy. The accompanying `verification_output.txt` is the recorded output of that command. Mathematical correctness rests on Steps 1–5 rather than the finite tests.

## Relationship to prior work

Boyd, Diaconis, and Xiao formulate symmetric fastest mixing as a convex spectral-norm or semidefinite optimization problem [1]. Boyd, Diaconis, Parrilo, and Xiao establish general symmetry averaging and block diagonalization, and give explicit solutions for cycles and wheels [2, Sections 2, 3.1.1, 5.3.3]. The graph here is neither a cycle nor a wheel: it has \(2m\) vertices, \(m\) distinct degree-one leaves, and two edge orbits. The present exact closed form and the \(m^{-1}\) spoke-probability law are not stated in those inspected examples. Jafarizadeh develops formulas for clique lifts and families of tree-like subgraphs [3]; the cycle with one pendant at each rim vertex is not a clique lift of the rim cycle, and the inspected topology lists do not cover this exact family. Unlike a numerical SDP solution for each size, the claim gives a closed formula for **every** integer \(m\ge3\).

## Limitations

The result assumes equal stationary probabilities and symmetric transition matrices, holding probabilities permitted, and precisely one leaf attached to every rim vertex. It does not classify **all nonsymmetric-in-the-graph** optimizers (i.e. transition matrices that break dihedral spatial symmetry), nor does it cover nonuniform equilibrium measures or two or more leaves per rim vertex. The available literature comparison cannot establish absolute priority; unindexed graph-family variants or implicit specializations of broader theorems remain possible. No independent mathematical validation has been performed.

## References

[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264. Accessible text: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/SIREV042326-1.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first posted 2007-09-06), later SIAM Journal on Optimization 20 (2009), 792–819. https://arxiv.org/abs/0709.0955.

[3] S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI 10.1109/TSIPN.2020.2964211. Accessible author-provided full text: https://www.researchgate.net/publication/387767555_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_and_Subgraphs.
