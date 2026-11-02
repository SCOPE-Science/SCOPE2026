# Sharp three-attractor bound at the smallest quorum-protection group

## Finding

**Theorem.** In the infinite well-mixed, three-strategy quorum-protection public-goods replicator model of Li–Li–He–Shi–Szolnoki, at the smallest admissible group size \(N=3\) and quorum \(M=2\), for *every* admissible parameter choice, the following statements hold:

1. No fully mixed equilibrium with positive frequencies of ordinary cooperators, defectors, and protective cooperators is locally asymptotically stable. Every such equilibrium has either a negative Jacobian determinant or a strictly positive Jacobian trace.
2. There are at most **three** locally asymptotically stable equilibrium points on the closed strategy simplex: at most the all-defector vertex, the all-ordinary-cooperator vertex, and one equilibrium mixing defectors with protective cooperators.
3. This bound is attained with strictly interior efficacy \(0<\omega<1\). In particular, with
   \[
   (r,c,L,\rho,k,\omega)=\left(\frac{33}{20},1,2,\frac12,\frac3{25},\frac34\right),
   \]
   exactly three locally asymptotically stable equilibria occur: all defection, all ordinary cooperation, and the protective–defector mixture of protective frequency \(z=4/5\). The second nontrivial protective–defector mixture, at \(z=1/5\), is a saddle.

Thus the source model permits **three locally stable equilibrium outcomes already at its smallest legally defined interaction group**, but no locally stable coexistence equilibrium containing all three strategies at that group size.

## Assumptions and scope

The strategy frequencies are \(x\) (ordinary cooperator \(C\)), \(y\) (defector \(D\)), and \(z\) (protective cooperator \(S\)), with \(x,y,z\ge0\) and \(x+y+z=1\). Groups have three participants sampled independently from an infinite well-mixed population, and protection activates if at least two group members are protective cooperators. Both \(C\) and \(S\) pay \(c>0\) into the public good, multiplied by \(r\in(1,3)\) and shared equally; \(S\) additionally pays \(k>0\). A group with \(d\) defectors has failure probability \(1-\rho^d\), where \(\rho\in(0,1)\), with loss \(L>0\) per participant. When protection activates, it reduces this failure probability by the factor \(1-\omega\), where \(\omega\in[0,1]\), and benefits all strategies.

We discuss **locally asymptotically stable equilibrium points** of the deterministic continuous-time replicator flow, relative to the closed two-dimensional simplex. We make no claim that all trajectories converge to equilibria, or that periodic orbits are absent. Write
\[
 y=1-x-z,\quad h=1-\rho,\quad C_0=Lh,\quad a=\frac{rc}{3}-c<0,\quad q=1-hy=\rho+h(x+z).
\]
Here \(C_0\) is a positive risk scale, not the ordinary-cooperator strategy \(C\).

## Proof

**1. Exact selection gradients.** Let \(P_C,P_D,P_S\) be the expected payoffs and set \(A=P_C-P_D\), \(B=P_S-P_D\). The two independently sampled co-players yield
\[
 A=a+C_0(q^2-\omega z^2),\qquad B=A-k+2C_0\omega zy. \tag{1}
\]
Indeed, the difference in baseline failure probabilities of a focal defector versus a focal contributor is \(h q^2\). The survival-weighted protection event affecting their difference requires both co-players to be \(S\), of probability \(z^2\). The focal protective cooperator is pivotal for quorum activation precisely if exactly one co-player is \(S\) and the other is \(D\), of probability \(2zy\) and failure probability \(h\). This proves (1) directly, without a mean-field or independence approximation beyond the stipulated random matching.

The reduced replicator equations are
\[
 \dot x=x[(1-x)A-zB],\qquad \dot z=z[(1-z)B-xA]. \tag{2}
\]
All later derivatives are taken with \(y=1-x-z\) imposed.

**2. Strict interior instability.** Suppose \(x,y,z>0\) is an equilibrium. Then \(A=B=0\). The four gradient derivatives are
\[
 A_x=2C_0hq,\quad A_z=2C_0(hq-\omega z),\quad
 B_x=A_x-2C_0\omega z,\quad B_z=A_z+2C_0\omega(y-z).
\]
Differentiating (2) at \(A=B=0\) and simplifying gives the *exact* Jacobian trace and determinant
\[
 \operatorname{tr}J=2C_0 y\,[hq(x+z)+\omega z(1-3z)], \tag{3}
\]
\[
 \det J=4C_0^2\omega xyz\,(hq y-\omega z^2). \tag{4}
\]
For \(\omega=0\), the identity \(B-A=-k<0\) excludes any interior equilibrium, so assume \(\omega>0\). If \(\det J<0\), the equilibrium is a saddle. If \(\det J\ge0\), (4) gives \(\omega z^2\le hqy\). For \(z\le1/3\), the bracket in (3) is strictly positive. For \(z>1/3\), the same bracket satisfies
\[
 \begin{aligned}
 hq(x+z)+\omega z(1-3z)
 &\ge hq\left(x+z-\frac{y(3z-1)}z\right)\\
 &=\frac{hq}{z}\left[(2z-1)^2+x(4z-1)\right]>0.
 \end{aligned}
\]
The last inequality uses \(x>0\) and \(z>1/3\). Therefore when the determinant is nonnegative the trace is strictly positive, giving at least one eigenvalue with positive real part, including in the zero-determinant case. Every interior equilibrium is unstable; no hyperbolicity assumption is needed.

**3. Sharp upper bound on stable equilibria.** At full defection, the invasion eigenvalues are \(a+C_0\rho^2\) and \(a+C_0\rho^2-k\); at full ordinary cooperation they are \(-a-C_0\) and \(-k\). Each vertex can contribute at most one locally stable equilibrium. Full protective cooperation is unstable because a rare ordinary cooperator has growth rate \(+k\).

On the \(C\)–\(D\) edge, \(A(x,0)=a+C_0(\rho+hx)^2\) is strictly increasing, so every nonvertex equilibrium has positive tangential derivative. On the \(C\)–\(S\) edge, \(P_S-P_C=-k\), so no nonvertex equilibrium exists. On the \(D\)–\(S\) edge (\(x=0\)), the selection gradient is the quadratic
\[
 B_0(z)=a-k+C_0\left[\rho^2+2(\rho h+\omega)z+(h^2-3\omega)z^2\right],\qquad
 B_0'(0)=2C_0(\rho h+\omega)>0. \tag{5}
\]
The restricted flow is \(\dot z=z(1-z)B_0(z)\). A locally asymptotically stable nonvertex equilibrium must attract from *both* directions along this invariant edge. A quadratic with positive initial slope has at most one such root (only a decreasing simple root can be attracting; a double root, if present, repels from its lower-frequency side). This leaves at most one locally stable \(D\)–\(S\) equilibrium. Together with Step 2, the entire simplex has at most three locally asymptotically stable equilibria.

**4. Exact sharpness witness.** Set \((r,c,L,\rho,k,\omega)=(33/20,1,2,1/2,3/25,3/4)\), all strictly satisfying the relevant positive bounds and with \(\omega\in(0,1)\). Then \(a=-9/20\), \(C_0=1\), and
\[
 A(0,0)=-\frac15,\qquad A(1,0)=\frac{11}{20},\qquad
 B_0(z)=-2\left(z-\frac15\right)\left(z-\frac45\right).
\]
Hence the pure \(D\) and pure \(C\) vertices are locally asymptotically stable, while two \(D\)–\(S\) edge equilibria lie at \(z=1/5\) and \(z=4/5\). The transverse eigenvalue at both is \(-3/25\), and their tangential eigenvalues are respectively \(+24/125\) and \(-24/125\). Thus the former is a saddle and the latter is a locally asymptotically stable node. Step 2 excludes any additional locally stable interior equilibrium; Step 3 excludes any other boundary one. The sharp total is exactly three. The condition \(2\le M\le N-1\) in the model rules out smaller \(N\), establishing minimum group size.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently enumerates the nine ordered co-player pairs for each focal strategy, tests the exact payoff identities against the closed formula, separately constructs the Jacobian entries at payoff equality, and tests identities (3)–(4) using rational arithmetic. It also confirms every polynomial factorization and all four nonzero edge eigenvalues in the exact sharpness witness. In one run, the checker completed 1,344 rational payoff/Jacobian checks and 101 polynomial identity checks, all passing. These finite tests are **not** substituted for the algebraic proof above.

## Relationship to prior work

Li, Li, He, Shi and Szolnoki introduced precisely this quorum-protection mechanism and derived its general selection gradients and boundary stability conditions (arXiv:2609.28132, Sections 2.1–2.7 and Appendices A–C). Their numerical studies concern the baseline group size \(N=5\), and report coexistence of three stable outcomes and the nonattraction of *sampled* interior equilibria. Their general formulas do not assert the universal absence of interior attractors when \(N=3\), a sharp bound for all permissible parameters at that size, or the exact smallest-group rational realization above. The present result does not claim novelty for the replicator model, the quorum pivotality formula, or the general Jacobian factorization; its contribution is the special-size sign obstruction and sharp minimal-size classification.

Related replicator-mutator public-goods work with institutional incentives, including Balabanova, Duong and Han (2026), concerns a different mutation-and-incentive mechanism, and its abstract cannot establish coverage of the specific quorum-protection theorem. Earlier exact treatment not indexed by the searches remains a possible priority risk.

## Limitations

The theorem is confined to \(N=3\), \(M=2\), an infinite well-mixed deterministic replicator model with the stated risk and protection rules and strictly positive costs. It counts locally asymptotically stable **equilibria**, not invariant sets generally, global basins, or transient dynamics. It does not preclude stable cycles or establish convergence of every initial state. No assertion is made for larger group sizes, alternate quorum rules, or stochastic finite populations. Independent mathematical assessment remains outstanding.

## References

- S. Li, X. Li, J. He, L. Shi and A. Szolnoki, *Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection*, arXiv:2609.28132, first publicly posted 2026-09-23. https://arxiv.org/abs/2609.28132
- N. Balabanova, M. H. Duong and T. A. Han, *Replicator-mutator dynamics for public goods games with institutional incentives*, Mathematical Biosciences **395** (2026), 109644. https://doi.org/10.1016/j.mbs.2026.109644
