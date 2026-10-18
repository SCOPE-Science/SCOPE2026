# Spectral-collision spikes and finite-time sinc windows in weighted quantum joins

## Finding

A coherent continuous-time quantum walk can have a discontinuous **infinite-time averaged** return probability at an isolated positive intergraph coupling, despite having a propagator that is analytic in that coupling at every fixed time. The collision positions and spatial jump profiles are determined exactly for arbitrary finite connected regular graph components. The observation-time resolution of each collision is a universal sinc profile. For two equally sized complete graphs the entire finite-time return average admits a closed formula, exhibiting a sharp coupling window of width \(1/(nT)\).

For the precise statements, let \(X\) and \(Y\) be finite connected undirected, unweighted, simple, regular graphs on \(n,m\geq2\) vertices and with degrees \(r,s\), respectively. Form the weighted join with adjacency Hamiltonian
\[
H_\gamma=\begin{pmatrix}A_X&\gamma\mathbf 1_n\mathbf 1_m^{\mathsf T}\\
\gamma\mathbf 1_m\mathbf 1_n^{\mathsf T}&A_Y\end{pmatrix},\qquad\gamma>0.
\]
For vertices \(u,v\in X\), define
\[
F_T^\gamma(u,v)=\frac1T\int_0^T\!\big|\langle v|e^{-itH_\gamma}|u\rangle\big|^2\,dt,
\qquad \overline M_\gamma(u,v)=\lim_{T\to\infty}F_T^\gamma(u,v).
\]
Write \(\overline M_X\) for the corresponding mean mixing matrix of \(A_X\) alone. Put
\[
\Delta_\gamma=\sqrt{(r-s)^2+4\gamma^2nm},\quad
\lambda_\pm(\gamma)=\frac{r+s\pm\Delta_\gamma}{2},\quad
\beta_\gamma=\frac12\left(1-\frac{r-s}{\Delta_\gamma}\right),\quad
\alpha_\gamma=1-\beta_\gamma.
\]
For each real \(\mu\), let \(E^X_\mu\) denote the orthogonal spectral projector of \(A_X\) for \(\mu\), or the zero matrix if \(\mu\notin\operatorname{spec}(A_X)\).

**Exact resonance law.** For every \(\gamma>0\) and all \(u,v\in X\),
\[
\boxed{\overline M_\gamma(u,v)=\overline M_X(u,v)
-\frac{2\alpha_\gamma\beta_\gamma}{n^2}
+\frac{2\beta_\gamma}{n}E^X_{\lambda_-(\gamma)}(u,v).}
\tag{1}
\]
The final term vanishes except at the finite set of couplings
\[
\boxed{\gamma_\mu=\sqrt{\frac{(r-\mu)(s-\mu)}{nm}}\quad
\text{for }\mu\in\operatorname{spec}(A_X)\setminus\{r\},\ \mu<\min\{r,s\}.}
\tag{2}
\]
At such a coupling, the jump of the averaged \(X\)-to-\(X\) block relative to its smooth, nonresonant extension is exactly
\[
\boxed{J_\mu(u,v)=\frac{2\beta_{\gamma_\mu}}{n}E^X_\mu(u,v).}
\tag{3}
\]
Every diagonal jump is nonnegative, and the trace jump is strictly positive:
\[
\sum_{u\in X}J_\mu(u,u)=\frac{2\beta_{\gamma_\mu}}n\operatorname{rank}(E^X_\mu)>0.
\]
In contrast, for any \(w\in Y\) and any \(u\in X\), at **all** positive couplings, including collisions,
\[
\boxed{\overline M_\gamma(u,w)=\frac{2\gamma^2}{\Delta_\gamma^2}.}
\tag{4}
\]
Thus the collision redistributes the time-averaged probability *within* \(X\) without creating an extra jump of the probability entering \(Y\).

**Sharp finite-observation crossover.** Fix one eligible eigenvalue \(\mu\) in (2), put \(\gamma_* =\gamma_\mu\), and consider \(\gamma_T=\gamma_*+c/T>0\), where \(c\in\mathbb R\) is fixed. For every pair \(u,v\in X\),
\[
\boxed{\lim_{T\to\infty}F_T^{\gamma_T}(u,v)=
\overline M_X(u,v)-\frac{2\alpha_*\beta_*}{n^2}
+\frac{2\beta_*}{n}E^X_\mu(u,v)
\operatorname{sinc}\left(\frac{2\gamma_*nm}{\Delta_*}c\right),}
\tag{5}
\]
where the starred quantities are evaluated at \(\gamma_*\) and \(\operatorname{sinc}(z)=\sin z/z\), continuously extended by \(\operatorname{sinc}(0)=1\). The convergence in (5) has error \(O_C(T^{-1})\) uniformly for \(|c|\le C\), for every fixed choice of the two graphs.

**Complete-graph form.** Let \(X=Y=K_n\) with \(n\ge2\), and launch and observe at one vertex of the first clique. For every \(\gamma>0\) and \(T>0\), exactly
\[
\boxed{\begin{aligned}
F_T^\gamma(u,u)
={}&1-\frac2n+\frac{3}{2n^2}
+\frac{n-1}{n^2}\Big[\operatorname{sinc}\big(n(1-\gamma)T\big)
+\operatorname{sinc}\big(n(1+\gamma)T\big)\Big]\\
&+\frac1{2n^2}\operatorname{sinc}(2n\gamma T).
\end{aligned}}
\tag{6}
\]
In particular,
\[
\boxed{\overline M_\gamma(u,u)=
\begin{cases}
1-\dfrac1n+\dfrac1{2n^2},&\gamma=1,\\[3pt]
1-\dfrac2n+\dfrac3{2n^2},&\gamma\ne1,
\end{cases}}
\qquad \gamma>0.
\tag{7}
\]
The jump is \((n-1)/n^2\). For \(\gamma=1+z/(nT)\), the return average equals the nonresonant value in (7) plus \((n-1)n^{-2}\operatorname{sinc}(z)\) and a remainder bounded by \(O(n^{-2}T^{-1})\), uniformly for \(|z|\) bounded, \(n\ge2\), and \(T\) large enough that \(1/2\le\gamma\le3/2\).

## Assumptions and scope

All graphs are finite, connected, simple, regular and undirected; their internal edges have unit hopping, every intercomponent edge has the same strictly positive real hopping \(\gamma\), and there are no onsite energies or losses. Time is continuous, the Hamiltonian is the *adjacency* matrix, and measurement means occupation probability for a localized single-particle initial state. Equations (1)--(5) do not require vertex transitivity or equality of the graph orders. Equation (6) is specifically for two equal complete-graph components. Infinite-time limits always take \(T\to\infty\) with the graphs fixed unless the separate finite-window statement explicitly specifies a joint regime.

## Proof

**Invariant-sector decomposition.** Since each component is connected and regular, its all-ones vector is an eigenvector of its adjacency matrix, with simple eigenvalue its degree. The orthogonal complements of \(\mathbf1_n\) and \(\mathbf1_m\) are invariant under the join Hamiltonian. The restriction to the two normalized uniform vectors is the real symmetric matrix
\[
B_\gamma=\begin{pmatrix}r&\gamma\sqrt{nm}\\
\gamma\sqrt{nm}&s\end{pmatrix}.
\]
Its distinct eigenvalues are \(\lambda_\pm\) above. The squared overlap of the first normalized uniform vector with the \(\lambda_+\) eigenvector equals \(\alpha_\gamma\); the remaining overlap equals \(\beta_\gamma\). Direct evaluation gives \(\alpha_\gamma\beta_\gamma=\gamma^2nm/\Delta_\gamma^2\), with both factors strictly between zero and one.

For \(u,v\in X\), the full transition amplitude decomposes **exactly**, at every time, as
\[
\langle v|e^{-itH_\gamma}|u\rangle=
\sum_{\nu\in\operatorname{spec}(A_X)\setminus\{r\}}
 e^{-it\nu} E^X_\nu(v,u)
+\frac{\alpha_\gamma e^{-it\lambda_+}+\beta_\gamma e^{-it\lambda_-}}n.
\tag{8}
\]
This expression remains valid at degenerate eigenvalues because it is an orthogonal decomposition into fixed invariant subspaces, not a formula obtained by dividing by spectral gaps.

**Infinite-time averaging and collisions.** For real \(a,b\), \(T^{-1}\int_0^T e^{it(a-b)}dt\to0\) if \(a\ne b\), and equals one otherwise. Squaring (8), its transverse-transverse terms give \(\overline M_X(u,v)-1/n^2\); the two uniform modes give \((\alpha^2+\beta^2)/n^2\). The larger uniform-sector eigenvalue satisfies \(\lambda_+>\max\{r,s\}\), so it cannot meet an eigenvalue of \(A_X\). Only \(\lambda_-\), which lies below \(\min\{r,s\}\), can meet a transverse eigenvalue, adding the cross term \(2\beta E^X_{\lambda_-}(u,v)/n\). Since \(\alpha^2+\beta^2-1=-2\alpha\beta\), this proves (1). Solving \(\lambda_-=\mu\) gives (2). Each eligible \(\mu\) is isolated, so approaching its coupling without equality removes the cross term and gives (3). Positivity of the diagonal projector and positivity of its rank establish the trace claim. Every transverse projector annihilates the uniform vector, hence \(E^X_\mu\mathbf 1_n=0\); therefore the jump does not change the sum of each row of the \(X\)-block.

For initial \(u\in X\), target \(w\in Y\), all transverse contributions vanish and the transition amplitude has the form
\[
\langle w|e^{-itH_\gamma}|u\rangle=
\frac{\sqrt{\alpha\beta}}{\sqrt{nm}}
\left(e^{-it\lambda_+}-e^{-it\lambda_-}\right)
\]
up to an overall sign. The two frequencies are different whenever \(\gamma>0\). Its infinite-time squared modulus is \(2\alpha\beta/(nm)=2\gamma^2/\Delta^2\), proving (4), including collision values.

**Observation-time crossover.** For a nonzero gap \(d\), the time average of \(\cos(dt)\) equals \(\operatorname{sinc}(dT)\). Apply this directly to the cross terms in (8). When \(\gamma=\gamma_*+c/T\), every frequency difference other than \(\lambda_-(\gamma)-\mu\) stays uniformly separated from zero for sufficiently large \(T\) and fixed \(|c|\le C\). Its time-averaged contribution is therefore \(O_C(T^{-1})\). The unique vanishing gap satisfies
\[
\lambda_-(\gamma)-\mu=
-\frac{2\gamma_*nm}{\Delta_*}\frac cT+O_C(T^{-2}).
\]
All coefficients are analytic in \(\gamma>0\), so they differ from their resonant values by \(O_C(T^{-1})\). Substituting these facts proves (5) and the stated uniform error. There is no complication if \(\lambda_-\) also equals a transverse eigenvalue of \(Y\), since such vectors have zero amplitude on any vertex of \(X\).

**Two equal cliques.** Their only transverse eigenvalue is \(-1\), with projector \(I_n-\mathbf 1_n\mathbf 1_n^{\mathsf T}/n\), while \(r=s=n-1\), \(\alpha=\beta=1/2\), and \(\lambda_\pm=n-1\pm n\gamma\). Thus the return amplitude is a sum of three phases with positive real coefficients \((n-1)/n\), \(1/(2n)\), \(1/(2n)\). Squaring and averaging pairs of phases yields (6), with spectral gaps \(n(1-\gamma)\), \(n(1+\gamma)\), and \(2n\gamma\). At fixed positive coupling, only the first gap vanishes, precisely at \(\gamma=1\); taking \(T\to\infty\) establishes (7). Substitution of \(\gamma=1+z/(nT)\) gives the claimed window. The two remaining sinc factors have arguments of order \(nT\); using \(|\operatorname{sinc}(a)|\le\min\{1,1/|a|\}\) bounds their sum by \(O(n^{-2}T^{-1})\) uniformly in the stated regime.

## Verification

Run `python verify.py` with Python 3 and NumPy. The program independently diagonalizes complete-graph and cycle joins, integrates every spectral-frequency pair to obtain finite- and infinite-window averages, and compares with (1)--(7). It checks 1,330 configurations; the largest discrepancy in the infinite-time projector checks is below \(2.3\times10^{-14}\). It verifies the specific collision on \(K_3\) joined to \(K_2\), where the time-averaged return is \(17/25\) at coupling one but has a nonresonant one-sided limit of \(113/225\), a jump of \(8/45\). Numerical diagonalization is corroborative; the proof above covers all stated sizes and parameters.

## Relationship to prior work

Lo, Rajaram, Schepens, Sullivan, Tamon and Ward give an explicit time-averaged probability law for joins of circulants, **under a noncollision hypothesis**; their Theorem 5 explicitly excludes coincidence of the lower uniform-sector eigenvalue with transverse spectra. The nonresonant uniform shift in (1) is acknowledged as an extension of that established formula, not as an independent discovery. Coutinho, Godsil, Guo and Zhan give the general spectral-projector representation of average mixing matrices. Kirkland and Monterde derive general transition-amplitude relationships and finite-time bounds for joins, focusing on periodicity and state transfer. The contribution isolated here is the complete exceptional-coupling projector term on arbitrary connected regular components, the nonzero return-trace jump, and the uniform finite-observation sinc law, including its exact \(1/(nT)\) calibration in equal cliques. These statements were not found in the inspected primary texts, but independent priority verification remains outstanding.

## Limitations

The phenomenon requires exact coherent evolution and sufficiently controlled, uniform intercomponent couplings. At finite observation time every probability varies continuously with \(\gamma\); the discontinuity is only in the infinite-time averaging operation. Equation (5) fixes the graph pair before taking the asymptotic limit, whereas the explicit equal-clique remainder in (6) also controls the displayed joint size-time regime. No claims are made about open-system decoherence, robustness to internal disorder, or originality relative to every unexamined publication. Source statements about off-resonance mixing and general projector identities are credited rather than presented as new.

## References

1. P. Lo, S. Rajaram, D. Schepens, D. Sullivan, C. Tamon, J. Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059v1 (8 September 2005), especially Theorem 5 and its noncollision condition. https://arxiv.org/abs/quant-ph/0509059
2. S. Kirkland and H. Monterde, *Quantum walks on join graphs*, arXiv:2312.06906v1 (12 December 2023), especially Section 3 and Section 11. https://arxiv.org/abs/2312.06906
3. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (11 September 2017), especially the projector identity. https://arxiv.org/abs/1709.03591
