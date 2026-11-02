# Exact Hopf-criticality transition in a logit game with environmental feedback

## Finding

Consider the two-strategy bounded-rationality game–resource differential equations below. Under the parameter assumptions in the next section, the unique interior equilibrium undergoes a transversal Hopf crossing as rationality \(\beta\) increases through \(\beta_h\). Its Hopf criticality is determined **exactly** by the sign of
\[
\mathcal H(\varepsilon)=-\frac{(1+\theta)(R+T+P-s)}{qD}
 +\varepsilon\beta_h n_h(1-n_h)\big[(1-3\theta)(P-s)-(3-\theta)(R+T)\big].
\]
Here \(q=\theta/(1+\theta)^2\), \(D=R+T+\theta(P-s)\), and \(n_h\) is the equilibrium resource level at Hopf. In explicitly specified canonical linear coordinates, the first Lyapunov coefficient is \(\ell_1=\mathcal H(\varepsilon)/16\).

Write \(M=(1-3\theta)(P-s)-(3-\theta)(R+T)\). If \(M\leq 0\), the Hopf bifurcation is **supercritical for every environmental adjustment speed** \(\varepsilon>0\), producing locally attracting small-amplitude periodic orbits on the side \(\beta>\beta_h\). If \(M>0\), there is a unique positive speed
\[
\varepsilon_c=\frac{(1+\theta)(R+T+P-s)}{qD\,\beta_h n_h(1-n_h)M}
\]
such that the Hopf is supercritical for \(0<\varepsilon<\varepsilon_c\) and **subcritical** for \(\varepsilon>\varepsilon_c\), producing locally repelling small periodic orbits on the side \(\beta<\beta_h\). At the equality \(\varepsilon=\varepsilon_c\) the first Lyapunov coefficient vanishes; no assertion about the next coefficient or nearby cycle multiplicities is made.

The condition \(M>0\) is possible **if and only if** \(0<\theta<1/3\) and \(P-s>(3-\theta)(R+T)/(1-3\theta)\). For \(\theta\geq1/3\), all admissible games have supercritical Hopf bifurcations, regardless of \(\varepsilon\).

## Assumptions and scope

The state variables are cooperator fraction \(x\in[0,1]\) and resource fraction \(n\in[0,1]\). The strategy-revision process is logit learning coupled to logistic environmental feedback:
\[
\dot x=\frac{1}{1+\exp[-\beta g(x,n)]}-x,\qquad
\dot n=\varepsilon n(1-n)((1+\theta)x-1),
\]
\[
g(x,n)=a x n+b x+c n-s,
\quad a=P-R-s-T,\quad b=R+s,\quad c=s-P.
\]
Assume \(0<\theta<1\), \(R>s>0\), \(T>0\), \(P>0\), and \(\varepsilon>0\). Here \(R=R_0-T_0\) and \(s=P_0-S_0\) describe the depleted-resource payoff differences, while \(T=T_1-R_1\) and \(P=P_1-S_1\) describe the resource-rich payoff differences. These signs are precisely the game's stated dominant-defection and depleted-resource assumptions. Every rate is deterministic; no demographic noise is included.

Define
\[
q=\frac{\theta}{(1+\theta)^2},\quad K=R-\theta s>0,\quad
D=R+T+\theta(P-s)>K,\quad C=(1+\theta)\log(1/\theta).
\]
The interior equilibrium is \(x_*=1/(1+\theta)\) and \(n_*(\beta)=[K-C/\beta]/D\) for \(\beta>\beta_{\mathrm{int}}=C/K\). The unique trace-zero crossing is
\[
\beta_h=\frac{D(1+\theta)/\theta+(P-R-s-T)\log(1/\theta)}{RP+sT},\qquad
n_h=\frac{K-C/\beta_h}{D}.
\]
All inequalities \(\beta_h>\beta_{\mathrm{int}}>0\) and \(0<n_h<1\) follow from the hypotheses (proved below), so the Hopf crossing is genuinely interior.

## Proof

**1. Existence and transversality.** At \(x_*=1/(1+\theta)\), write \(p=x_*\), \(q=p(1-p)\), and \(B=ap+c=-D/(1+\theta)<0\). Because the equilibrium logit probability equals \(p\), its Jacobian is
\[
J_* =\begin{pmatrix} \beta q(b+a n_*)-1&\beta q B\\
\varepsilon(1+\theta)n_*(1-n_*)&0\end{pmatrix}.
\]
The determinant is positive throughout the interior-equilibrium branch. The trace is affine increasing in \(\beta\) with slope
\[
q\left(b+\frac{aK}{D}\right)=\frac{q(1+\theta)(RP+sT)}{D}>0.
\]
Solving for trace zero gives the displayed \(\beta_h\). At the interior-branch entrance \(\beta_{\mathrm{int}}\), the trace is \(\beta_{\mathrm{int}}qb-1\), which is strictly negative. Indeed \(R>s\) implies
\[
\beta_{\mathrm{int}}qb
=\frac{\theta(R+s)\log(1/\theta)}{(1+\theta)(R-\theta s)}
<\frac{2\theta\log(1/\theta)}{1-\theta^2}<1.
\]
The last inequality follows from \(1-\theta^2>2\theta\log(1/\theta)\) for \(0<\theta<1\), obtained by differentiating the difference and using \(\log\theta<\theta-1\). Since the trace increases and eventually becomes positive, \(\beta_h>\beta_{\mathrm{int}}\). Also \(n_h<n_*(\infty)=K/D<1\). Thus \(J_h\) has simple eigenvalues \(\pm i\omega\), with \(\omega>0\), crossing transversally with positive real-part derivative.

**2. Exact cubic Hopf coefficient.** Put \(h=1-2p\), \(k=1-6p+6p^2\), and \(m=\varepsilon(1+\theta)n_h(1-n_h)>0\). At Hopf, \(\beta_h q(b+a n_h)=1\), and
\[
J_h=\begin{pmatrix}0&j\\m&0\end{pmatrix},\qquad j=\beta_h q B<0,\qquad \omega=\sqrt{-jm}.
\]
Use canonical linear coordinates \(X=x-p\) and \(Y=(-j/\omega)(n-n_h)\), for which the linear terms are \(\dot X=-\omega Y\), \(\dot Y=\omega X\). Set \(\kappa=\omega/(-j)=m/\omega\). Let \(F\) denote the original right-hand side for \(\dot x\). The only derivatives needed for the planar cubic radial coefficient are
\[
F_{xx}=h/q,\quad F_{xn}=\beta_h(hB+qa),\quad
F_{nn}=qh\beta_h^2B^2,\quad
F_{xxx}=k/q^2,\quad
F_{xnn}=\beta_h^2(kB^2+2qhBa).
\]
For the environment right-hand side \(G\), \(G_{xx}=G_{nn}=G_{xxn}=G_{nnn}=0\) at this equilibrium, so the standard planar Hopf formula reduces to
\[
16\ell_1=F_{xxx}+\kappa^2F_{xnn}
 +\frac{\kappa}{\omega}F_{xn}(F_{xx}+\kappa^2F_{nn}).
\]
Using \(k-h^2=-2q\), \(\kappa^2=m/(-\beta_h qB)\), and \(\kappa/\omega=1/(-\beta_h qB)\), simplify to
\[
16\ell_1=-\frac2q-\frac{ah}{qB}+m\beta_h(2B-ha).
\]
Finally, direct substitutions give
\[
\frac2q+\frac{ah}{qB}=\frac{(1+\theta)(R+T+P-s)}{qD},\quad
(1+\theta)(2B-ha)=(1-3\theta)(P-s)-(3-\theta)(R+T),
\]
which proves \(16\ell_1=\mathcal H(\varepsilon)\) exactly.

**3. Sign and direction.** The first term of \(\mathcal H\) is strictly negative, since \(R>s\), \(P,T>0\), and \(D,q>0\). The second term is \(\varepsilon\) times a positive prefactor times \(M\). Hence the asserted exhaustive sign classification and unique \(\varepsilon_c\) when \(M>0\). If \(\theta<1/3\), positivity of \(M\) is equivalent to the stated inequality. If \(\theta\geq1/3\), \(M<0\): this is immediate when \(P\geq s\); when \(P<s\), use \((3\theta-1)(s-P)<(3\theta-1)R<(3-\theta)(R+T)\). Nonzero \(\ell_1\) and positive trace-crossing speed invoke the nondegenerate planar Hopf theorem: positive \(\ell_1\) gives the subcritical (unstable-cycle) side, negative \(\ell_1\) the supercritical (stable-cycle) side.

**4. Fully admissible witness.** Take \(\theta=1/10\), \(R=2\), \(s=1/2\), \(T=1/2\), \(P=50\). These arise from strictly positive matrices
\[
A_0=\begin{pmatrix}3&1\\1&3/2\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&1\\3/2&51\end{pmatrix}.
\]
Then \(D=149/20\), \(a=47\), and \(M=137/5>0\). The Hopf quantities are \(\beta_h\approx1.896972562301\), \(n_h\approx0.082523076904\) and \(\varepsilon_c\approx23.607116993784\). At \(\varepsilon=1\), \(\ell_1\approx-5.560417137554\); at \(\varepsilon=30\), \(\ell_1\approx+1.572385202232\). Thus the same strictly positive payoff matrices and the same rationality threshold support opposite Hopf criticalities solely by varying environmental adjustment speed.

## Verification

Run `python3 verify_hopf_criticality.py` with Python 3's standard library; it recalculates the three stated cases, the critical speed, and 100 deterministic parameter tests. Each case independently contracts the Taylor quadratic and cubic tensors using normalized complex eigenvectors in the Kuznetsov Hopf formula, compares its real cubic coefficient with the closed expression, and checks equilibrium/Jacobian identities. This is a finite computational cross-check, not the proof of the universal statement. The analytical derivation above covers all permitted real parameters.

## Relationship to prior work

Paarporn (2023, arXiv:2311.02745v1) introduced this logit-learning/resource-feedback model, gave interior equilibrium and trace-zero thresholds, and expressly left the first Lyapunov coefficient and periodic-orbit stability as future work (Section IV-A and V). The present theorem supplies a closed sign classification, including a subcritical region not implied by those local linearization statements. Gavin, Cao, and Paarporn (2024, arXiv:2409.05044v1) analyze logit equilibria in *static*, one-dimensional two-strategy games, where this environmental Hopf bifurcation is absent. Gong et al. (2022, arXiv:2205.10734v1) compute a Hopf coefficient for a **different replicator–mutator**, polynomial strategy-update equation, not for the sigmoid logit equation above. Liu et al. (2023, eLife 82954) likewise compute coefficients in a distinct collective-risk strategy/environment model. These methods provide background, but their results do not imply the displayed model-specific formula and sign-change criterion.

## Limitations

The claim is local to the interior Hopf crossing and does not classify all periodic orbits or their global basins, determine the second Lyapunov coefficient at the degenerate equality \(\varepsilon=\varepsilon_c\), prove a Bautin unfolding, or treat asynchronous/stochastic individual learning. The coefficient is tied to the explicitly defined canonical coordinates; its **sign** and criticality are coordinate-independent. Bibliographic coverage cannot rule out an equivalent calculation in unindexed work; no independent scientific audit has been performed.

## References

1. Keith Paarporn, *The madness of people: rational learning in feedback-evolving games*, arXiv:2311.02745v1 (first posted 2023-11-05), https://arxiv.org/html/2311.02745v1 .
2. Lulu Gong, Weijia Yao, Jian Gao, and Ming Cao, *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734v1 (2022), https://arxiv.org/html/2205.10734v1 .
3. Rory Gavin, Ming Cao, and Keith Paarporn, *An Analysis of Logit Learning with the r-Lambert Function*, arXiv:2409.05044v1 (first posted 2024-09-08), https://arxiv.org/abs/2409.05044 .
4. Linjie Liu and collaborators, *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, eLife 12:e82954 (2023), https://elifesciences.org/articles/82954 .
5. Andrew R. Tilman, Joshua B. Plotkin, and Erol Akçay, *Evolutionary games with environmental feedbacks*, Nature Communications 11:915 (2020), https://doi.org/10.1038/s41467-020-14531-6 .
