# Exact four-mode heat transport on cliques with two distinct pendant attachments

## Finding
Let \(p\ge3\) be an integer. Start from a clique \(K_p\), distinguish two different clique vertices \(A,B\), attach a new leaf \(x\) only to \(A\), and another leaf \(y\) only to \(B\). On the resulting unit-edge graph \(G_p\), use the combinatorial Laplacian \(L\), heat semigroup \(H_t=e^{-tL}\), graph distance \(d\), and graph-metric Wasserstein distance \(W_1\). For every \(t\ge0\), the heat-row transport distance across the pendant edge \(xA\) has the following **exact closed formula**, with four exponential rates:
\[
W_1(H_t(x,\cdot),H_t(A,\cdot))
=U_p(t)+\tfrac12\bigl(V_p(t)+V_{p-2}(t)\bigr).
\]
For \(c\in\{p,p-2\}\) put
\[
\Delta_c=\sqrt{(p-2)^2+4c},\quad
\alpha_c=\frac{p+2-\Delta_c}{2},\quad
\beta_c=\frac{p+2+\Delta_c}{2},
\]
\[
U_c(t)=\frac{(\beta_c-2)e^{-\alpha_ct}+(2-\alpha_c)e^{-\beta_ct}}{\Delta_c},\qquad
V_c(t)=\frac{c(e^{-\alpha_ct}-e^{-\beta_ct})}{\Delta_c}.
\]
For every \(t>0\), one and the same optimal Kantorovich potential, unique up to constants, is
\[
f(x)=2,\quad f(A)=1,\quad f(B)=0,\quad f(y)=-1,\quad f(C)=0
\]
for every other clique vertex \(C\). In particular,
\[
W_1(H_t(x,\cdot),H_t(A,\cdot))
=1+(p-3)t+\tfrac12(6-p^2)t^2+O_p(t^3).
\]
Thus the transported adjacent heat rows separate beyond their initial distance \(1\) at all sufficiently small positive times precisely for \(p\ge4\). Further, with \(t_p=(\log p)/p\),
\[
\lim_{p\to\infty}W_1(H_{t_p}(x,\cdot),H_{t_p}(A,\cdot))=2.
\]
This is a statement about the specified **pair** of heat rows, not an assertion of the global graph-Lipschitz norm of \(H_t\).

## Assumptions and scope
All vertices have counting measure; every graph edge has unit length and unit conductance. The continuous-time heat operator uses \(L=D-\mathsf A\), without degree normalization. The Wasserstein cost uses unweighted shortest-path distance. Set \(C_1,\ldots,C_{p-2}\) for the other clique vertices. The first heat row is started at \(x\), and the second at \(A\). The exact formula includes \(t=0\), while the unique-potential conclusion requires \(t>0\). Real-valued \(1\)-Lipschitz functions represent transport dual potentials.

## Proof
Set \(\delta_t=H_t(e_x-e_A)\), viewed as a signed column vector. Symmetry of \(H_t\) identifies this with the difference of the two heat rows. Permutations of \(C_1,\ldots,C_{p-2}\) fix \(\delta_t\). Define
\[
u=\delta_x,\qquad v=-\delta_y,\qquad
w=\delta_x+\delta_A,\qquad z=-(\delta_y+\delta_B).
\]
Then \(\delta_A=w-u\), \(\delta_B=v-z\), \(\delta_y=-v\), and conservation of total signed mass gives
\[
\delta_{C_i}=-\frac{w-z}{p-2}.
\]
Applying \(\delta_t'=-L\delta_t\) at the pendant vertices and their two attachment vertices gives the exact four-dimensional system
\[
\frac d{dt}\begin{pmatrix}u\\v\\w\\z\end{pmatrix}
=\begin{pmatrix}-2&0&1&0\\0&-2&0&1\\p-1&1&-p&0\\1&p-1&0&-p\end{pmatrix}
\begin{pmatrix}u\\v\\w\\z\end{pmatrix},\qquad
(u,v,w,z)(0)=(1,0,0,0).
\]
The displayed matrix is irreducible and Metzler; its exponential sends this nonzero nonnegative initial vector to a strictly positive vector at every \(t>0\). Moreover \(d=u-v\) and \(s=w-z\) solve
\[
(d,s)'=(-2d+s,(p-2)d-ps),\qquad(d,s)(0)=(1,0).
\]
A second irreducible Metzler argument proves \(d(t),s(t)>0\) for \(t>0\). Consequently the signed heat-row difference has \(\delta_x>0\) and \(\delta_y<0\), while after deleting the two leaf edges and pushing those leaf masses to the clique, its clique residuals have **one positive source** at \(A\) of mass \(w\), and strictly negative masses \(-z\) at \(B\) and \(-s/(p-2)\) at each \(C_i\). The identity \(w=z+s\) balances these masses.

Any transport plan must move \(u\) units across bridge \(xA\) and \(v\) across bridge \(yB\). Within the clique it must move exactly \(w\) units from \(A\) to the other clique vertices, each at graph distance one. This constructs a plan of cost \(u+v+w\). Conversely, the graph-Lipschitz potential in the statement gives dual pairing
\[
\langle f,\delta_t\rangle
=2u+\delta_A-\delta_y=u+v+w.
\]
Primal and dual coincide, so \(W_1=u+v+w\). Because the optimal plan transports strictly positive mass along every edge \(xA\), \(AB\), \(AC_i\) and \(By\), every optimal potential must saturate all their oriented Lipschitz constraints. These edges span the whole vertex set, forcing the stated potential up to an additive constant. (At \(t=0\), this uniqueness need not hold.)

To solve the system, form \(U_+=u+v\), \(U_-=u-v\), \(V_+=w+z\), \(V_-=w-z\). Each pair solves
\[
U_c'=-2U_c+V_c,\qquad V_c'=cU_c-pV_c,\qquad(U_c,V_c)(0)=(1,0),
\]
with \(c=p\) for the plus pair and \(c=p-2\) for the minus pair. The characteristic roots are \(-\alpha_c,-\beta_c\), yielding exactly the exponentials displayed in the finding. Since \(u+v=U_p\) and \(w=(V_p+V_{p-2})/2\), the closed transport formula follows.

Differentiating this finite system at \(t=0\) gives the first derivative \(p-3\) and second derivative \(6-p^2\) of the transport distance. For \(p=3\), the first derivative vanishes and the second is negative; for \(p\ge4\), the first derivative is positive. All four exponential decay rates are strictly positive, so the distance tends to zero as \(t\to\infty\). In particular for each \(p\ge4\) it has at least one positive-time global maximum strictly above one. Finally, as \(p\to\infty\), each \(\alpha_c\to1\), each \(\beta_c/p\to1\), and each \(\Delta_c/p\to1\) for \(c=p,p-2\). At \(t_p=(\log p)/p\) the slow exponentials tend to one while the fast exponentials tend to zero. Hence \(U_p(t_p)\to1\), \(V_p(t_p)\to1\), \(V_{p-2}(t_p)\to1\), giving the limit two.

## Verification
The standalone Python checker independently evaluates the full graph heat kernel by Poisson uniformization, computes transport by exact bridge decomposition and by finite extreme-potential enumeration, and compares both to the four-mode expression for \(3\le p\le9\) at three positive times. It additionally tests the small-time derivative and large-order sample values. Run `python3 verify_two_pendants.py`; expected output begins `CHECK_OK`. These numerical checks are finite stress tests, not substitutes for the analytic proof for every integer \(p\ge3\).

## Relationship to prior work
Ollivier's 2007 theory identifies Wasserstein transport of Markov kernels as the natural metric measure of heat-row contraction. The later graph heat-gradient and curvature framework of Münch–Wojciechowski gives general bounds and equivalences, not this fixed-potential, four-exponential law. Previously described one-attachment clique bouquets admit a different two-rate heat-transport calculation. The present family has two **distinct** attachment vertices, so its four-mode transport and the dimension-dependent short-time amplification do not follow by relabeling a one-hub bouquet. Curvature-distortion calculations on pineapple graphs concern a distinct, degree-normalized and weighted optimization problem.

## Limitations
Only the pendant-edge pair \((x,A)\) is optimized. The result does not identify the maximum over **all** adjacent heat-row pairs, nor the full graph-Lipschitz operator norm. It concerns unweighted clique cores, unit-length unweighted pendant edges and the combinatorial heat generator; degree-normalized or independently weighted variants are not covered. The literature comparison cannot exclude unindexed equivalent calculations.

## References
Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first public version 2007-01-30), https://arxiv.org/abs/math/0701886.

F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first public version 2017-12-04), https://arxiv.org/abs/1712.00875.
