# Directed two-community games: robust mixed-state stability with oscillatory relaxation

## Finding
Consider the action-blind constant-migration specialization of the two-community network replicator with any strictly positive two-strategy matrix game having an interior evolutionarily stable state (ESS). Every irreducible, possibly non-symmetric, strictly positive community interaction matrix yields a **locally exponentially stable** joint balanced equilibrium. There is no local oscillatory *instability* caused solely by directed contact weights, even when migration is asymmetric. Nevertheless the stable linearized action dynamics can have genuinely nonreal eigenvalues: directed contacts permit damped oscillatory relaxation.

More precisely, for every positive off-diagonal contact pair and every pair of positive constant migration rates, the full three-dimensional physical-state Jacobian has strictly negative spectral abscissa. For the concrete admissible game and contacts below, its eigenvalues are
\[
-\frac1{10},\qquad -\frac{209}{80}\pm\frac{\sqrt{6479}}{80}\,\mathrm{i}.
\]
Thus non-reciprocal learning can change the *character* of local relaxation without overturning mixed-strategy stability. The conclusion concerns local behavior; it is not a global convergence theorem.

## Assumptions and scope
Let \(h\in\{1,2\}\) denote communities and \(A,B\) the two actions. A strictly positive payoff matrix \(G=(g_{ij})_{i,j\in\{A,B\}}\) induces rewards \(r_A(y)=g_{AA}y+g_{AB}(1-y)\) and \(r_B(y)=g_{BA}y+g_{BB}(1-y)\), where \(y\) is the population fraction playing \(A\). Assume there exists \(p\in(0,1)\) such that \(r_A(p)=r_B(p)=R>0\), with
\[
K=-\frac{d}{dy}(r_A(y)-r_B(y))>0.
\]
For a two-action matrix game this is precisely a strict interior mixed ESS (the payoff advantage decreases through the crossing).

Let the directed community-contact matrix be \(W=\begin{psmallmatrix}w_{11}&u\\v&w_{22}\end{psmallmatrix}\), with \(w_{11},w_{22},u,v>0\); **no requirement** \(u=v\). Individuals migrate from community 1 to 2 at constant rate \(\alpha>0\), and from 2 to 1 at constant rate \(\beta>0\), independently of action. Total mass is one. Denote community mass by \(\eta_h>0\), mass using action \(A\) there by \(s_h\), and mass using action \(B\) there by \(\eta_h-s_h\), so that \(y=s_1+s_2\). The state satisfies \(\eta_1+\eta_2=1\), \(0\le s_h\le\eta_h\).

The exact dynamics (a two-action instance of the Govaert--Zino--Tegling network replicator) are
\[
\dot\eta_1=-\alpha\eta_1+\beta\eta_2,\qquad
\dot\eta_2=\alpha\eta_1-\beta\eta_2,
\]
\[
\dot s_h=\sum_{k\ne h}(m_{kh}s_k-m_{hk}s_h)
+\sum_{k=1}^2W_{hk}\big[(\eta_h-s_h)s_k r_A(y)-s_h(\eta_k-s_k)r_B(y)\big],
\]
where \(m_{12}=\alpha\) and \(m_{21}=\beta\). Set
\[
e=\frac{\beta}{\alpha+\beta},\qquad f=\frac{\alpha}{\alpha+\beta},\qquad \kappa=p(1-p)K.
\]
The equilibrium under discussion is \((\eta_1,\eta_2)=(e,f)\) and \((s_1,s_2)=(pe,pf)\). Only its local stability and linearized relaxation spectrum are claimed.

## Proof
**Existence.** Migration balances because \(\alpha e=\beta f\). At \(s_h=p\eta_h\), the strategy conversion terms cancel pairwise, since \(r_A(p)=r_B(p)\). The migration terms also cancel. Therefore the stated interior balanced state is an equilibrium.

**Linearization.** Use independent physical coordinates \((\eta_1,s_1,s_2)\). The first equation is independent of action masses, with derivative \(-\alpha-\beta\). Consequently the full Jacobian is block lower triangular, and its remaining two eigenvalues belong to the action block \(L\), obtained by differentiating at fixed community densities \((e,f)\).

Introduce positive numbers
\[
A_0=Rfu+\alpha,\quad B_0=Rev+\beta,\quad X_0=Reu+\beta,\quad Y_0=Rfv+\alpha,
\]
\[
g_1=e(ew_{11}+fu),\qquad g_2=f(ev+fw_{22}).
\]
A direct differentiation of the conversion term shows that a perturbation \(\delta s\) has linearized drift
\[
L\delta s=(C-\kappa g\mathbf 1^{\mathsf T})\delta s,
\qquad
C=\begin{pmatrix}-A_0&X_0\\Y_0&-B_0\end{pmatrix},
\quad g=\begin{pmatrix}g_1\\g_2\end{pmatrix}.
\]
For clarity, at the balanced point each conversion summand differentiates to \(R(\eta_h\delta s_k-\eta_k\delta s_h)-Kp(1-p)\eta_h\eta_k(\delta s_1+\delta s_2)\); this gives the claimed \(C\) and rank-one term after summing over \(k\) and adding migration. Neither contact symmetry nor symmetric migration was used.

**Strict Hurwitz property.** By \(\alpha e=\beta f\), the positive vector \((e,f)^{\mathsf T}\) lies in \(\ker C\), so \(\det C=0\). The trace and determinant of the corrected block are exactly
\[
\operatorname{tr}L=-A_0-B_0-\kappa(g_1+g_2)<0,
\]
\[
\det L=\kappa\big[(B_0+Y_0)g_1+(A_0+X_0)g_2\big]>0.
\]
The determinant follows directly from \(\det(C-\kappa g\mathbf 1^{\mathsf T})\) using the two-by-two adjugate identity; every displayed factor is strictly positive. The elementary two-dimensional Hurwitz criterion now places both eigenvalues of \(L\) in the open left half-plane. The remaining eigenvalue, \(-\alpha-\beta\), is also strictly negative. The physical equilibrium is interior and the vector field is smooth, hence the classical linearization theorem yields local exponential stability.

**Exact oscillatory witness.** Take \(G=\begin{psmallmatrix}1/2&3/2\\3/2&1/2\end{psmallmatrix}\), \(W=\begin{psmallmatrix}10&1\\5&1\end{psmallmatrix}\), and \(\alpha=\beta=1/20\). Then \(p=e=f=1/2\), \(R=1\), \(K=2\), \(\kappa=1/2\), and the equilibrium is \((\eta_1,s_1,s_2)=(1/2,1/4,1/4)\). The **full** Jacobian is exactly
\[
J=\begin{pmatrix}
-1/10&0&0\\
1/2&-77/40&-33/40\\
-5/2&9/5&-33/10
\end{pmatrix}.
\]
The characteristic polynomial factors as
\[
\det(\lambda I-J)=(\lambda+1/10)\left(\lambda^2+\frac{209}{40}\lambda+\frac{627}{80}\right).
\]
Its quadratic discriminant is \(-6479/1600<0\), giving the nonreal pair in the finding. All matrix-game entries and all contact/migration rates are strictly positive; the oscillatory pair is therefore not a zero-contact or negative-reward artifact.

## Verification
Reconstruct the symbolic block and its determinant from the explicitly defined ODE. The included `CHECK.py` performs the general symbolic identities (balanced eigenvector, zero determinant for \(C\), rank-one determinant formula), rebuilds the full three-dimensional Jacobian at the rational witness, and checks the exact characteristic polynomial, negative discriminant and strict stability. It uses symbolic computation for reproducibility; the proof of universal stability is the algebraic positive trace/determinant argument above, **not** extrapolation from sampled parameters.

## Relationship to prior work
Govaert, Zino and Tegling (2022, arXiv:2203.00371, equation (6) and Theorem 2) formulate this action-blind migration and community imitation model. Their mixed-ESS convergence result requires **symmetric** interaction weights; the paper identifies stability under more general network structures as an avenue for investigation. The present local theorem drops contact symmetry in the smallest two-community model, using an exact determinant argument; it neither asserts their global theorem nor covers more than two communities.

Como, Fagnani and Zino (2020, arXiv:2009.10020) examine imitation on fixed communities and give global potential-game convergence assuming an undirected network; that claim does not imply directed-contact local stability in the present migratory system. Pi and collaborators (2020, DOI 10.3390/math8122120) analyze different two-community delayed replicator equations with heterogeneous payoff matrices. Hu and Zhang (2020, DOI 10.1186/s13662-020-02718-6) analyze another delayed two-community imitation model. Neither delayed framework contains the exact constant action-blind migration/weighted-encounter operator examined here as an immediate specialization.

## Limitations
The theorem is **local** and specific to two communities, two actions, constant action-independent migration, positive payoffs, and a strict interior mixed ESS. It does not preclude other attractors or global failures of convergence, nor does it address time-varying or strategy-dependent migration, zero migration rates, multi-community networks, delay equations, or stochastic finite-population variants. The example demonstrates damped linear oscillations near an attracting equilibrium, **not** a Hopf bifurcation or a sustained limit cycle. Broader unpublished, unindexed, or differently formulated linear-systems literature could contain an equivalent special-case theorem; the comparison is necessarily best-knowledge, not an independence certificate.

## References
1. A. Govaert, L. Zino, E. Tegling, *Population games on dynamic community networks*, arXiv:2203.00371 (first public version 2022-03-01), IEEE Control Systems Letters 6 (2022), 2695–2700. https://arxiv.org/html/2203.00371v1
2. G. Como, F. Fagnani, L. Zino, *Imitation dynamics in population games on community networks*, arXiv:2009.10020 (2020); IEEE Transactions on Control of Network Systems 8 (2021), 65–76. https://arxiv.org/pdf/2009.10020
3. J. Pi, H. Yang, Y. Shu, C. Zhong, G. Yang, *The Stability of Two-Community Replicator Dynamics with Discrete Multi-Delays*, Mathematics 8 (2020), 2120. https://doi.org/10.3390/math8122120
4. W. Hu, G. Zhang, *Stability analysis of imitative dynamics in two-community with multiple delays*, Advances in Difference Equations (2020), 263. https://doi.org/10.1186/s13662-020-02718-6
5. Mathematical Reviews, *MSC2020: Evolutionary games*, code 91A22. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=91A22
