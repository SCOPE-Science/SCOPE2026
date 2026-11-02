# Four-phase fastest reversible mixing on three communities with unequal stationary masses

## Finding

Let \(m,r\ge2\) be integers, and let \(G=K_{m,m,r}\), whose three independent vertex classes are \(A,B,C\). Prescribe the positive stationary distribution that assigns total probability \(a\) to each of \(A\) and \(B\), and \(g=1-2a\) to \(C\), uniformly within each class, for \(0<a<1/2\). Over **all** reversible, nonnegative row-stochastic transition matrices supported on the edges of \(G\) and on self-loops, the minimum second-largest eigenvalue modulus is

\[
\mu_*(a)=\begin{cases}
\dfrac{1-4a}{1-2a},&0<a\le1/6,\\[3pt]
\dfrac{1-2a}{1+2a},&1/6\le a\le1/3,\\[3pt]
\dfrac{a}{2-a},&1/3\le a\le2/5,\\[3pt]
\dfrac{4a-1}{6a},&2/5\le a<1/2.
\end{cases}
\]

An explicit globally optimal transition matrix is constructed from the interclass **stationary flow totals** \(x\) from \(A\) to \(B\) and \(y\) from each of \(A,B\) to \(C\), as follows:

\[
(x,y)=\begin{cases}
(0,a),&0<a\le1/6,\\[3pt]
\left(\dfrac{2a(6a-1)}{3(1+2a)},\dfrac{2ag}{1+2a}\right),&1/6\le a\le1/3,\\[3pt]
\left(\dfrac{2a^2}{2-a},\dfrac{2ag}{2-a}\right),&1/3\le a\le2/5,\\[3pt]
\left(\dfrac{4a-1}{3},\dfrac g2\right),&2/5\le a<1/2.
\end{cases}
\]

The optimal value and these canonical flows do **not depend on the class cardinalities** \(m,r\), as long as each class contains at least two vertices. Four different eigenvalue/constraint regimes occur. There is also a sharp distinction between **optional** and **unavoidable** edges: for \(a\le1/6\), every unrestricted optimal chain omits all \(A\)-to-\(B\) transitions; for \(1/6<a\le1/4\), optimal chains exist both with and without these transitions; for \(a>1/4\), every unrestricted optimal chain has positive total \(A\)-to-\(B\) flow. For \(a\ge2/5\), every unrestricted optimum has zero holding probability at every vertex of \(C\).

## Assumptions and scope

A reversible chain \(P\) obeys \(P\mathbf1=\mathbf1\), \(P_{ij}\ge0\), detailed balance \(\pi_iP_{ij}=\pi_jP_{ji}\), and \(P_{ij}=0\) for distinct vertices in the same class. Self-loops are permitted. Its mixing criterion is the operator norm of \(\Pi^{1/2}P\Pi^{-1/2}-ss^{\mathsf T}\), with \(\Pi=\operatorname{diag}(\pi)\) and \(s_i=\sqrt{\pi_i}\); equivalently it is the maximum modulus of all eigenvalues other than the stationary eigenvalue one. This is the usual reversible-chain spectral criterion, not the exact finite-time total-variation mixing time.

For an invariant chain, the stationary edge flow is \(x/m^2\) on each \(A\)-to-\(B\) edge, and \(y/(mr)\) on each \(A\)-to-\(C\) or \(B\)-to-\(C\) edge. Consequently, a vertex in \(A\) sends probability \(x/(am)\) to each vertex of \(B\), probability \(y/(ar)\) to each vertex of \(C\), and holds with probability \(1-(x+y)/a\). A vertex of \(C\) sends \(y/(gm)\) to each vertex in either of \(A,B\), holding with probability \(1-2y/g\). The same description holds for \(B\). Feasibility is exactly

\[
x\ge0,\qquad y\ge0,\qquad x+y\le a,\qquad 2y\le g.
\]

## Proof

**Reduction without restricting the optimum.** The objective is a convex spectral norm in the symmetrized transition matrix. Permuting vertices within each class and interchanging \(A,B\) preserves the prescribed stationary distribution. Averaging any feasible \(P\) over this finite symmetry group remains feasible and does not increase the norm. Thus the minimum over unrestricted matrices equals the minimum over the two-flow family above. This does not assert uniqueness of unrestricted optimizers.

**Complete spectrum.** Each of the \(A\)- and \(B\)-internal zero-sum subspaces has eigenvalue \(u=1-(x+y)/a\) with multiplicity \(m-1\); the \(C\)-internal zero-sum subspace has eigenvalue \(v=1-2y/g\) with multiplicity \(r-1\). On vectors constant within each class, the three-state quotient is

\[
T=\begin{pmatrix}
1-(x+y)/a &x/a&y/a\\
x/a&1-(x+y)/a&y/a\\
y/g&y/g&1-2y/g
\end{pmatrix}.
\]

It has eigenvalues \(1\), \(w=1-(2x+y)/a\), and \(z=1-y/(ag)\). Since \(m,r\ge2\), every listed nonstationary eigenvalue occurs; hence

\[
\mu(x,y)=\max\{u,v,|w|,|z|\},\qquad u,v\ge0.
\]

**Minimization over the first flow.** For fixed feasible \(y\), \(u\) decreases linearly with \(x\) and \(-w\) increases linearly with \(x\). Their intersection occurs at

\[
x_0(y)=\frac{2(a-y)}3,
\quad u(x_0,y)=-w(x_0,y)=\frac{a-y}{3a}.
\]

Moreover, \(\max\{u,|w|\}\ge(a-y)/(3a)\) for every feasible \(x\), with equality at \(x_0(y)\). Therefore the **exact** global minimization becomes

\[
\min_{0\le y\le\min(a,g/2)}
\max\left\{\frac{a-y}{3a},\ 1-\frac{2y}g,\ \left|1-\frac{y}{ag}\right|\right\}.
\]

Set \(t=y/(ag)\). The upper endpoint is \(T_{\max}=\min\{1/g,1/(2a)\}\), and the three functions are

\[
f(t)=\frac{1-gt}3,\qquad k(t)=1-2at,\qquad |1-t|.
\]

For \(t\le1\), the last function is dominated by \(k(t)\), and the other two are decreasing. For \(t\ge1\), \(t-1\) increases while \(f,k\) decrease. Their crossings occur respectively at \(t_f=2/(2-a)\) and \(t_k=2/(1+2a)\). Hence the unique optimal \(t\) is

\[
t_* =\min\left\{T_{\max},\max\left(\frac2{2-a},\frac2{1+2a}\right)\right\}.
\]

Comparing these rational expressions shows that the controlling upper bound and crossing change at \(a=1/6,1/3,2/5\). Substitution yields the displayed four branches, and \(x=x_0(ag t_*)\) yields the canonical flows. These scalar monotonicity and intersection arguments prove global optimality for **every real** \(a\in(0,1/2)\), not merely for tested rational values.

**Exactly which symmetric solutions are optimal.** The scalar optimizer \(y_*=ag t_*\) is unique. At that fixed value \(y_*\), all invariant optimal \(x\) form the closed interval

\[
\max\{0,a(1-\mu_*)-y_*\}\ \le x\le\
\min\left\{a-y_*,\frac{a(1+\mu_*)-y_*}2\right\}.
\]

For \(1/6\le a\le1/4\), this is exactly \([0,a(6a-1)/(1+2a)]\). For \(1/4\le a\le1/3\), it is \([2a(4a-1)/(1+2a),2a^2/(1+2a)]\). Outside \([1/6,1/3]\), the interval collapses to the canonical \(x\). These statements follow by imposing the four exact eigenvalue inequalities \(|u|,|v|,|w|,|z|\le\mu_*\).

**Support consequences for all optimal matrices.** Every unrestricted optimum averages to an invariant optimum. If \(a\le1/6\), every invariant optimum has zero \(A\)-to-\(B\) aggregate flow, and nonnegativity of individual edge flows forces every unrestricted optimum to have all these edges zero. For \(1/6<a\le1/4\), the preceding interval contains zero and a positive number, giving both support patterns. If \(a>1/4\), that interval has strictly positive lower endpoint (or is a strictly positive singleton); every unrestricted optimum must therefore have positive aggregate \(A\)-to-\(B\) flow. Finally, for \(a\ge2/5\), every invariant optimum has \(2y=g\), hence zero average holding probability on \(C\); individual holding probabilities are nonnegative, so all of them vanish in any unrestricted optimum.

## Verification

Run `python3 verify.py` with the Python 3 standard library. It checks the piecewise rational formulas, feasibility, exact spectra, endpoint intervals, and exact detailed balance using `fractions.Fraction` on hundreds of rational parameter values. It additionally constructs full matrices for multiple unequal class sizes and checks six eigenvector types by exact matrix multiplication. This is a finite reproducibility check, **not** the proof for all real parameters; the proof above is algebraic.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) formulate the fixed-stationary-distribution reversible fastest-mixing problem as a convex semidefinite program and explicitly solve the uniform-stationary complete-bipartite case. Its bipartite restriction explains the first branch, where the \(A\)-to-\(B\) flow vanishes. Boyd, Diaconis, Parrilo and Xiao (2009), Section 5.4.2, give a spectral block reduction for arbitrary complete multipartite graphs with symmetric transitions and explain that the blocks can be inserted into an SDP; they explicitly solve the bipartite case, but do not give the above four-phase tripartite optimal-value formula, the interval of optimizers, or the optional-versus-unavoidable edge threshold. Here the prescribed class masses need not follow their cardinalities. The general symmetry and semidefinite methods are established prior work; the claim is the exact solved mass-dependent three-community classification and its support implications.

## Limitations

No claim of a unique unrestricted optimum is made. Indeed, within \(1/6<a<1/3\), even invariant optimal matrices are nonunique. The theorem requires three independent classes with the first two having equal prescribed total stationary mass, uniform mass within each class, and at least two vertices per class. It does not characterize all nonsymmetric optimal matrices, allow arbitrary within-class edges, or optimize finite-time total-variation distance. The literature comparison may miss specialized earlier work providing the same exact class-mass phase diagram. Independent external validation has not been performed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. Public version dated 2004-10-29. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf . Relevant material: Sections 6 and 7.1, especially pages 683–685.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optim. 20 (2009), 792–819; preprint arXiv:0709.0955, first posted 2007-09-06. https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf . Relevant material: Section 5.4.2, pages 812–813.
