# The eleven-vertex Radau positivity frontier for complete bipartite diffusion

## Finding

Let \(p,q\geq1\) be integers, \(N=p+q\), and let \(L\) be the unweighted combinatorial Laplacian of the complete bipartite graph \(K_{p,q}\). Apply the two-stage, third-order Radau IIA method to the continuous-time diffusion equation \(u'(t)=-Lu(t)\). Its completed-step matrix is
\[
T_h=\left(I-\frac h3 L\right)
\left(I+\frac{2h}{3}L+\frac{h^2}{6}L^2\right)^{-1},
\qquad h\geq0.
\]

**Theorem (sharp order-only frontier).** The matrix \(T_h\) is entrywise nonnegative for **every** timestep \(h\geq0\) if and only if \(N\leq11\). Moreover, whenever \(N\geq12\), put \(a=\min(p,q)\), \(b=\max(p,q)\), and \(h_*=8/b\). At \(h=h_*\), the diagonal entry of \(T_h\) at **every vertex in the part of size \(a\)** is strictly negative. Nonetheless, for each fixed \(K_{p,q}\), the completed step is entrywise strictly positive at all sufficiently small positive timesteps and at all sufficiently large timesteps. Thus, for every complete bipartite graph of order at least twelve, positivity is lost at an intermediate step and recovered for large steps.

In particular, the threshold is independent of the bipartition. For the balanced twelve-vertex graph \(K_{6,6}\), the diagonal entry at \(h=4/3\) is exactly \(-125/24939\).

## Assumptions and scope

The graph is finite, simple, undirected, unweighted, and complete bipartite; singleton parts are permitted. The Laplacian is \(L=D-A\) without normalized scaling. All real steps \(h\geq0\) are considered. Entrywise nonnegativity of \(T_h\) is equivalent to preservation of every nonnegative input vector by **one completed step**. Stage vectors are not asserted to be nonnegative. Conservation holds at all steps because \(T_h\mathbf1=\mathbf1\), but conservation alone does not imply positivity. No claim is made for arbitrary graphs, weighted bipartite graphs, or nonlinear diffusion.

## Proof

Write
\[
F(x)=\frac{6-2x}{x^2+4x+6},\qquad
D(x)=x^2+4x+6.
\]
These satisfy \(T_h=F(hL)\) by the Radau IIA stability function, and \(D(x)>0\) for \(x\geq0\). The eigenvalues of \(L\) are \(0\) once, \(q\) with multiplicity \(p-1\), \(p\) with multiplicity \(q-1\), and \(N\) once. The corresponding orthogonal projectors are the constant projector, the two within-part zero-sum projectors, and the one-dimensional between-part contrast projector. Consequently, with \(f_s=F(sh)\), entries of \(T_h\) have the following forms:

\[
\begin{aligned}
\text{across parts:}\quad &\frac{1-f_N}{N}=\frac{h(Nh+6)}{D(Nh)},\\[2pt]
\text{off-diagonal within the part of size }p:\quad
&\frac{p+qf_N-Nf_q}{pN}
=\frac{h^2q\{Nqh^2+(6p+12q)h+18\}}{D(qh)D(Nh)},\\[2pt]
\text{off-diagonal within the part of size }q:\quad
&\frac{q+pf_N-Nf_p}{qN}
=\frac{h^2p\{Nph^2+(12p+6q)h+18\}}{D(ph)D(Nh)},\\[2pt]
\text{diagonal in the part of size }p:\quad
&\delta_p=\frac1N+\frac{q}{pN}f_N+\left(1-\frac1p\right)f_q,\\[2pt]
\text{diagonal in the part of size }q:\quad
&\delta_q=\frac1N+\frac{p}{qN}f_N+\left(1-\frac1q\right)f_p.
\end{aligned}
\]

The within-part off-diagonal formulas apply only where distinct vertices in that part exist. Every off-diagonal entry is strictly positive for every \(h>0\); the only possible loss of positivity occurs on the diagonal.

Differentiation gives
\[
F'(x)=\frac{2(x^2-6x-18)}{D(x)^2}.
\]
Its unique positive minimum is at \(x_0=3+3\sqrt3\), with value
\[
F(x)\geq m_0=\frac{5-3\sqrt3}{2}\qquad(x\geq0).
\]
For any vertex, the diagonal entries of the orthogonal spectral projectors are nonnegative, sum to one, and give the constant projector coefficient \(1/N\). Therefore
\[
(T_h)_{vv}\geq\frac{1+(N-1)m_0}{N}.
\]
For \(N\leq11\), this is at least \((26-15\sqrt3)/11>0\). Together with the off-diagonal formulas and \(T_0=I\), this proves positivity for all steps in the first regime.

For the converse, relabel the parts so \(a\leq b\) and put \(w=a/b\in(0,1]\). At \(h_*=8/b\), \(F(8)=-5/51\) and
\[
F(8(1+w))=-\frac{8w+5}{32w^2+80w+51}.
\]
Substitution into the displayed diagonal formula yields
\[
\delta_a(h_*)=-\frac5{51}+\frac{C(w)}{N},\qquad
C(w)=\frac{32(w+1)(56w+89)}{51(32w^2+80w+51)}.
\]
The essential sharp inequality is the **strict** identity
\[
\frac{20}{17}-C(w)
=\frac{4(32w^2+40w+53)}{51(32w^2+80w+51)}>0
\qquad(0<w\leq1).
\]
Hence, whenever \(N\geq12\),
\[
\delta_a(h_*)< -\frac5{51}+\frac{20}{17N}\leq0.
\]
This gives an explicit negative matrix entry for **every** partition at every order at least twelve; the inequality is strict even at the boundary order.

Finally, \(T_0=I\), its diagonal entries are continuous and equal to one at zero, and its off-diagonal entries are strictly positive for every positive step. Thus every sufficiently small positive \(h\) has a strictly positive update. Since \(F(x)\to0\) as \(x\to\infty\), the spectral formula also shows \(T_h\to\mathbf1\mathbf1^\mathsf{T}/N\) entrywise as \(h\to\infty\), so every sufficiently large step is strictly positive. The intermediate negative witness establishes the asserted loss and recovery. \(\square\)

## Verification

The supplied `verify.py` checks seven universal rational-function identities symbolically, including the exact negative-witness identity and its strict positivity polynomial. It also independently constructs the full completed-step matrix from \(L\) and computes 228 exact-rational matrix comparisons over bipartitions and positive rational steps. All 228 comparisons passed. This finite sample is only a reproduction check; the preceding spectral and algebraic proof establishes the universal quantifiers. Run `python verify.py` with Python 3 and SymPy installed.

For a boundary example, \(K_{1,11}\) at \(h=8/11\) has a negative leaf-hub-side diagonal \(-5/787\), while \(K_{6,6}\) at \(h=4/3\) has diagonal \(-125/24939\). Each smaller complete bipartite graph remains nonnegative at all steps by the analytic bound.

## Relationship to prior work

The completed third-order Radau IIA stability function and A-/L-stability background are classical; Hairer and Wanner (1999, Section 3) explicitly supply its rational stability function. Bolley and Crouzeix (1978, Lemmas 1–2 and Theorem 1) exclude higher-order unconditional positivity for **all** positivity-preserving generators, which does not preclude unconditional positivity on a sharply restricted graph class. Horváth (2005, available online 27 October 2004, Sections 2–4) studies general positivity thresholds, test classes and invariant cones. Those results are not a classification of complete bipartite Radau steps by vertex count.

Earlier computations establish a twelve-vertex cutoff for the **star subfamily** \(K_{1,m}\), with an exact description of its timestep intervals. The present theorem does **not** re-claim the star interval classification: it establishes a new order-only equivalence simultaneously for **every** bipartition \(K_{p,q}\), including balanced graphs, and supplies the explicit witness \(8/\max(p,q)\). A complete-multipartite positivity theorem for the **even-stage diagonal Padé/Gauss** family concerns a different rational integrator and does not imply the third-order Radau criterion. Bibliographic and semantic searches found no same-statement result; unindexed equivalence remains possible.

## Limitations

The exact boundaries and number of positive-timestep intervals for each individual graph of order at least twelve are not classified here. The theorem proves the existence of at least one negative intermediate interval and strict positive regions near zero and infinity, not their maximal extents. The global threshold does not extend to arbitrary Laplacians or directed generators.

## References

1. E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, Journal of Computational and Applied Mathematics **111** (1999), 93–111; doi:10.1016/S0377-0427(99)00134-X. Author full text: https://www.unige.ch/~hairer/preprints/coimbra.pdf.
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356; doi:10.1016/j.apnum.2004.08.026; available online 27 October 2004.
3. C. Bolley and M. Crouzeix, *Conservation de la positivité lors de la discrétisation des problèmes d'évolution paraboliques*, RAIRO Analyse numérique **12** (1978), 237–245; https://www.numdam.org/article/M2AN_1978__12_3_237_0.pdf.
4. J. F. B. M. Kraaijevanger and J. A. van de Griend, *Absolute monotonicity of rational functions occurring in the numerical solution of initial value problems*, Numerische Mathematik **49** (1986), 413–424.
