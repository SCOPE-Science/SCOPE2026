# Exact dephasing optimum for local capture on complete bipartite quantum networks

## Finding

For every pair of integers \(m,n\geq 2\), consider the complete bipartite graph \(K_{m,n}\), with uniform edge hopping \(J>0\) and one absorbing vertex \(s\) in its part of size \(m\). Every vertex undergoes site-local Markovian pure dephasing at off-diagonal decay rate \(\gamma>0\), while the absorber removes population at rate \(\kappa>0\). Set \(N=m+n\), \(a=m-1\), \(b=n\), and choose the initial single-excitation state

\[
\rho_0=p\lvert s\rangle\langle s\rvert+\frac{1-p}{N-1}\bigl(I-\lvert s\rangle\langle s\rvert\bigr),\qquad 0\leq p\leq1.
\]

Every excitation is eventually absorbed. The unconditional mean absorption time \(T_p=\int_0^\infty\operatorname{tr}\rho(t)\,dt\) has the **exact all-size formula**

\[
\boxed{T_p=\frac{N}{\kappa}+c\left(\frac{\kappa(N-1)^2}{4J^2b}+A\gamma+\frac B\gamma+\frac C{2\gamma+\kappa}\right)},\quad c=\frac{1-p}{N-1},
\]

where

\[
A=\frac{(N-1)^2+a}{2J^2b},\qquad B=a(a-1)+b(b-1),\qquad C=a(N-2)^2.
\]

For every \(p<1\), the unique optimal positive dephasing rate at each fixed \(\kappa\) is the solution of

\[
\boxed{A=\frac{B}{\gamma_*^2}+\frac{2C}{(2\gamma_*+\kappa)^2}}.
\]

It is independent of \(p\), **strictly decreases** as the trapping rate \(\kappa\) increases, and obeys the sharp endpoints

\[
\lim_{\kappa\downarrow0}\gamma_*(\kappa)=\sqrt{\frac{B+C/2}{A}},\qquad
\lim_{\kappa\to\infty}\gamma_*(\kappa)=\sqrt{\frac BA}.
\]

In addition, for every \(p<1\), the objective is jointly strictly convex in \((\gamma,\kappa)\) and has exactly one global minimizer in the positive quadrant. At \(p=1\), \(T_1=N/\kappa\) is independent of dephasing, so uniqueness in \(\gamma\) is deliberately not asserted.

For a concrete example, on \(K_{3,3}\) with \(J=\kappa=1\) and the initial excitation uniformly mixed over non-absorbing sites \((p=0)\), \(\gamma_*\approx2.0149718805\). The lifetime decreases from \(T_0(1)=11.05\) to \(T_0(\gamma_*)\approx10.2965771365\), then increases under excessive dephasing.

## Assumptions and scope

The single-excitation space is \(\mathbb C^N\), and the Hamiltonian \(H\) is \(J\) times the ordinary adjacency matrix of \(K_{m,n}\), with no onsite detuning. Let \(P_j=\lvert j\rangle\langle j\rvert\). The trace-decreasing generator is exactly

\[
\mathcal L(\rho)=-i[H,\rho]-\frac\kappa2\{P_s,\rho\}+\gamma\sum_{j=1}^N\left(P_j\rho P_j-\frac12\{P_j,\rho\}\right).
\]

Thus each off-diagonal density-matrix entry is damped by \(\gamma\), **not** by \(2\gamma\), in the absence of other effects. The local trap has population-loss rate \(\kappa\). There is no other recombination, source, driving, or inter-particle interaction. The objective is the integral of the surviving one-excitation probability, equivalent to the first moment of absorption because all population is eventually captured. The initial family includes the uniform non-trap mixture at \(p=0\), the completely mixed state at \(p=1/N\), and the absorber-localized state at \(p=1\).

## Proof

**1. Exponential absorption.** For any operator \(X\), Hilbert--Schmidt dissipation gives

\[
\operatorname{Re}\langle X,\mathcal L X\rangle_{HS}=
-\frac\kappa2\bigl(\lVert P_sX\rVert_{HS}^2+\lVert XP_s\rVert_{HS}^2\bigr)
-\gamma\sum_{i\ne j}\lvert X_{ij}\rvert^2.
\]

Every generator eigenvalue therefore has nonpositive real part. If an eigenoperator had an eigenvalue with zero real part, the displayed identity would make it diagonal with its \(s\)-entry zero. Its eigenvalue equation forces \(H_{ij}(X_{jj}-X_{ii})=0\) for every edge. Connectivity makes all diagonal entries equal, hence zero. Therefore no nonzero eigenoperator has zero real part, all eigenvalues have strictly negative real part, and \(\rho(t)\to0\) exponentially. In particular, the integrated density exists, and trace loss gives \(\kappa\int_0^\infty\rho_{ss}(t)\,dt=1\).

**2. Symmetry reduction.** Write \(a=m-1\), \(b=n\), and call the remaining left vertices \(L\) and the right vertices \(R\). Permutation invariance within each class and preservation of the real-same-part/imaginary-cross-part subspace give eight real amplitudes: diagonal entries \(p_s,q,r\) for \(s,L,R\), the real coherence \(x=\rho_{s,L}\), imaginary coherences \(iy=\rho_{s,R}\) and \(iz=\rho_{L,R}\), and the real distinct-site coherences \(u=\rho_{L,L'}\), \(v=\rho_{R,R'}\). When \(a=1\), the nonexistent \(u\) entry and its equation may be omitted: it always appears multiplied by \(a-1\) in the physical equations. In this paragraph \(p_s\) is a time-dependent site population, distinct from the initial mixture parameter \(p\).

Directly taking entries of the Lindblad equation yields

\[
\begin{aligned}
\dot p_s&=-\kappa p_s-2Jby, &\dot q&=-2Jbz, &\dot r&=2J(y+az),\\
\dot x&=-Jb(y+z)-(\gamma+\kappa/2)x,\\
\dot y&=J[p_s+ax-r-(b-1)v]-(\gamma+\kappa/2)y,\\
\dot z&=J[q+(a-1)u+x-r-(b-1)v]-\gamma z,\\
\dot u&=-2Jbz-\gamma u, &\dot v&=2J(y+az)-\gamma v.
\end{aligned}
\]

Initially \(p_s(0)=p\), \(q(0)=r(0)=c=(1-p)/(N-1)\), and all five coherences vanish. Integrate each differential equation over nonnegative time. Using capital letters for integrals of the corresponding lower-case quantities and the fact that each amplitude tends to zero, the first three and last two equations immediately give

\[
P=\frac1\kappa,\qquad
Y=-\frac{(N-1)c}{2Jb},\quad Z=\frac c{2Jb},\quad U=V=-\frac c\gamma.
\]

The coherence equations then yield, in order,

\[
X=\frac{(N-2)c}{2\gamma+\kappa},
\]

\[
R=P+aX-(b-1)V-\frac{\gamma+\kappa/2}{J}Y,
\]

\[
Q=R-(a-1)U-X+(b-1)V+\frac\gamma J Z.
\]

Substitution into \(T_p=P+aQ+bR\) gives exactly the formula in the Finding. These equations reconstruct the integral without guessing an invariant-state ansatz and hold for all stated dimensions, rates and initial mixtures.

**3. Optimality and sensitivity.** For \(p<1\), \(c>0\), and all three coefficients \(A,B,C\) are strictly positive for \(m,n\ge2\). Differentiating the exact formula gives

\[
\frac{\partial T_p}{\partial\gamma}=c\left(A-\frac{B}{\gamma^2}-\frac{2C}{(2\gamma+\kappa)^2}\right),\quad
\frac{\partial^2T_p}{\partial\gamma^2}=c\left(\frac{2B}{\gamma^3}+\frac{8C}{(2\gamma+\kappa)^3}\right)>0.
\]

The first derivative runs from negative infinity to \(cA>0\), so its sole root is the global dephasing optimum. Implicit differentiation of that root gives \(d\gamma_*/d\kappa<0\), since the defining expression has positive partial derivatives with respect to both \(\gamma\) and \(\kappa\). Sending \(\kappa\) to zero or infinity inside the strictly monotone root relation gives the stated limits.

Finally \(N/\kappa\) and \(cB/\gamma\) are strictly convex in their respective positive variables; \(cC/(2\gamma+\kappa)\) is convex in both jointly; all other terms are linear in one of the rates. The Hessian is positive definite. The positive reciprocal terms blow up at the respective zero boundaries, while the positive linear terms grow at infinity. Therefore exactly one joint positive-rate minimum exists.

## Verification

The self-contained `proof_check.py` checks all eight time-integrated amplitude equations symbolically for the general parameter \(p\), the closed-form identity, and the first two dephasing derivatives; its exact symbolic certificate passed all 11 identities. It independently builds the **full** \(N^2\)-dimensional Lindblad superoperator, not the reduced eight-variable system, for nine bipartition sizes, three nontrivial rate triples, and four initial mixture weights: 108 direct solves. All matched the predicted lifetime with maximum relative error \(1.35\times10^{-14}\) and maximum linear-system residual \(9.22\times10^{-15}\). Thirty additional numerical checks bracketed the unique optimum and verified its strict decrease with trap strength. Running `python proof_check.py` after installing `requirements.txt` reproduces these tests. Finite tests support but do not replace the above all-parameter algebraic proof.

## Relationship to prior work

Kassal and Aspuru-Guzik (arXiv:1201.5202, first public 2012-01-25) analyze environment-assisted quantum transport on finite ordered paths and cycles with site dephasing, loss and trapping. Their general finite-matrix solution method is relevant, but their evaluated families and merit functions do not state the two-sided complete-bipartite lifetime formula or the strictly decreasing dephasing optimum at every trap rate.

Novo and collaborators (arXiv:1412.7209, first public 2014-12-22) analyze continuous-time **spatial search** on complete bipartite graphs and use invariant subspaces for coherent transport without dephasing. Their three-dimensional coherent search reduction is not a reduced dissipative density-matrix generator and does not imply the formula above by a parameter identification.

Alterman, Berman and Strauch (arXiv:2309.00164, first public 2023-08-31) obtain exact analytic noise-assisted transport laws for a **fully connected complete graph**, including dephasing, trapping and background decay. Complete graphs are not the specified \(K_{m,n}\) for \(m,n\ge2\); their five-variable density reduction has different connectivity, and its stated results do not directly provide this bipartite formula or optimal-rate monotonicity. The exact algebraic methods themselves are established and are not asserted to be new.

## Limitations

The theorem covers a uniform-edge, zero-detuning, finite single-excitation complete bipartite network, all-site equal pure-dephasing rates, one strictly positive local sink, no other loss, and only the explicit permutation-symmetric diagonal initial-state family. The finite-dimension exact formula does not claim results for localized initial excitations outside that family, nonuniform dephasing, disorder, coherent driving, many excitations, non-Markovian baths, or the complete distribution of capture time. The discovery-priority comparison is based on accessible primary sources and a scientific-claim search; an uncatalogued earlier formula or a stronger unpublished Haken--Strobl reduction could affect originality. No independent audit is claimed.

## References

1. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (initial submission 2012-01-25), https://arxiv.org/html/1201.5202v2 .
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven, Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (initial submission 2014-12-22), https://arxiv.org/html/1412.7209v2 .
3. S. Alterman, J. Berman, F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network*, arXiv:2309.00164 (initial submission 2023-08-31), https://arxiv.org/abs/2309.00164 .
