# Optimal snapshot discrimination of coexisting resetting active-gas phases and a spinodal cusp

## Finding

Consider the **two distinct symmetric stationary mean-field branches** of the one-dimensional density-slowed run-and-tumble model with local Poisson resetting, in the parameter window in which a supersaturated, entirely gaseous profile and a central dense droplet coexist. Sample one position from either profile, normalized by the same total mass. With equal prior probabilities, the **unique optimal likelihood-ratio rule, up to null sets**, is to classify the observation as a droplet if and only if its distance from the resetting origin lies *inside the dense droplet's interface*. The resulting total-variation distance is computable exactly from one Lambert-function value.

The distinguishability is not always improved by increasing the reset rate: for each fixed density parameter satisfying an explicit computable endpoint-sign test, it has exactly one interior maximum, despite the strictly increasing dense-phase mass. A concrete rigorously certified regime is \(\rho_m=20\); in contrast \(\rho_m=5\) gives a strictly increasing contrast over the full coexistence interval. At the upper existence fold of the gas-only branch the contrast has a nonzero, explicitly signed **three-halves-power correction**, with divergent second derivative.

Precisely, let \(Q=\rho_m>4\), \(\chi=\sqrt{r(r+\alpha)}/v_0\), \(m=M\chi/2\) and \(s=Q/4\). Work on \(1<m<s\). Put
\[
\Phi_Q(z)=z-z^2/Q,\qquad F_Q(z)=\log z-2z/Q,
\]
and define
\[
q_Q=\frac Q2\bigl(1-\sqrt{1-4/Q}\bigr),\qquad
 a_m=\frac Q2\bigl(1-\sqrt{1-4m/Q}\bigr),\qquad
 b_m=\frac{\log m}{Q}.
\]
There is a unique \(z_m\in(q_Q,a_m)\) satisfying
\[
F_Q(z_m)=F_Q(a_m)-b_m.
\]
For the two mass-normalized laws \(P_{\mathrm{drop}}\) and \(P_{\mathrm{gas}}\) of a sampled position,
\[
\boxed{\mathcal D_Q(m):=d_{\mathrm{TV}}(P_{\mathrm{drop}},P_{\mathrm{gas}})
      =\frac{\Phi_Q(z_m)-1}{m}.}
\]
The equal-prior optimal probability of classification error is exactly \((1-\mathcal D_Q(m))/2\), achieved by the stated radius threshold \(|X|<b_m/\chi\). There is exactly one sign change of the density difference, at that threshold.

The exact derivative is
\[
\boxed{\mathcal D'_Q(m)=\frac{G_Q(m)}{m^2},\qquad
G_Q(m)=1-\frac{z_m(a_m+1-z_m)}{Q}.}
\]
For every \(Q>4\), \(G_Q\) is strictly decreasing throughout \((1,s)\), and \(G_Q(1+)=1/q_Q>0\). Let \(z_*\in(0,Q/2)\) solve
\[
F_Q(z_*)=F_Q(Q/2)-\frac{\log s}{Q},\qquad
G_*=1-\frac{z_*(Q/2+1-z_*)}{Q}.
\]
Thus **if \(G_*\ge0\)**, \(\mathcal D_Q\) is strictly increasing on \((1,s)\); **if \(G_*<0\)**, it has a unique interior maximizer, the unique solution of \(G_Q(m)=0\). This is an exhaustive, exact, parameter-by-parameter classification without assuming uniqueness of a global \(Q\)-threshold.

Finally, with \(\epsilon=\sqrt{1-m/s}\downarrow0\), write \(\mathcal D_*=[\Phi_Q(z_*)-1]/s\) and \(A_*=\mathcal D_*+(z_*/s)(1/Q-1/2)\). Then
\[
\boxed{\mathcal D_Q(m)=\mathcal D_*+A_*\epsilon^2
   -\frac{z_*}{3s}\epsilon^3+O_Q(\epsilon^4).}
\]
The coefficient of \(\epsilon^3\) is strictly negative: the one-sided second derivative of \(\mathcal D_Q\) diverges to \(-\infty\) at the upper gas-only fold. At the lower droplet onset, \(\mathcal D_Q(m)=(m-1)/q_Q+O_Q((m-1)^2)\).

## Assumptions and scope

Fix \(v_0,\alpha,r,M>0\) and a dimensionless crowding parameter \(Q>4\). On the whole real line the mean-field run-and-tumble velocity has magnitude \(v_0(1-\rho/Q)\) in a gas region \(0\le\rho<Q\), and \(v_0/Q\) in the dense region \(\rho\ge Q\). Runs reverse direction with intensity \(\alpha/2\), and independent position resets occur at intensity \(r\), retaining the model's symmetric steady-state closure. The two stationary branches are the explicit **single-gas** and **single-central-droplet-plus-gas** solutions with the low-density gas root; they exist together when \(1<m=M\chi/2<Q/4\). No uniqueness or stability assertion is made outside these prescribed continuum stationary branches.

For a profile \(\rho(x)\) of total mass \(M\), define \(P(dx)=\rho(x)dx/M\). A snapshot is a draw from that *one-particle mass-normalized law*, not an assertion of independent tagged particles in a microscopic interacting system. Equal prior probabilities and equal zero-one misclassification losses are assumed in the decision-theoretic statement. Total variation is \(\sup_B|P_{\mathrm{drop}}(B)-P_{\mathrm{gas}}(B)|=\tfrac12\int|dP_{\mathrm{drop}}-dP_{\mathrm{gas}}|\). Sampling sign as well as distance gives the same total variation because both profiles are symmetric.

## Proof

**1. Branch reduction from the exact stationary equations.** Use dimensionless radius \(y=\chi|x|\) and let \(g(y)\) denote the gas-region density, not yet normalized as a probability. The stationary gas equation derived from the local-reset kinetic balances is
\[
(1-2g/Q)g'(y)=-g(y).
\]
On \(0<g<Q/2\), \(F_Q'(g)=(1-2g/Q)/g>0\), so any lower-branch gas solution starting at \(c\in(0,Q/2]\) obeys \(F_Q(g(y))=F_Q(c)-y\) and tends to zero at infinity. Its tail mass is exactly
\[
\int_y^\infty g(u)\,du=\Phi_Q(g(y)),
\]
because \(d\Phi_Q(g(y))/dy=-g(y)\). In the gas-only profile, normalization \(\int_0^\infty g=m\) gives \(\Phi_Q(a_m)=m\), hence the stated \(a_m\).

In the two-phase profile, the gas begins at dimensionless radius \(b_m\) with density \(q_Q\), where interface flux matching gives \(\Phi_Q(q_Q)=1\). Inside the droplet the exact solution is \(d(y)=Qm e^{-Qy}\) for \(0\le y<b_m\), since \(d(b_m^-)=Q\). Outside, it solves the same gas differential equation from \(q_Q\). Its half-line mass is
\[
\int_0^{b_m}Qm e^{-Qy}\,dy+\int_{b_m}^\infty d(y)\,dy
=m(1-e^{-Qb_m})+1=m.
\]
The original density profiles and their existence ranges are established by Grange (2026); none of those source profile formulas is claimed as new here.

**2. A strict single crossing and the optimal rule.** The gas-only density \(g(y)\) is at most \(a_m<Q/2\). In \(0\le y<b_m\), the droplet density is at least \(Q\), so \(d(y)>g(y)\). Set \(H(m)=F_Q(a_m)-F_Q(q_Q)-b_m\). At \(m=1\), \(a_m=q_Q\) and \(H(1)=0\). As \(\Phi_Q(a_m)=m\), differentiation gives
\[
H'(m)=\frac1{a_m}-\frac1{Qm}>0,
\]
since \(Qm=a_m(Q-a_m)>a_m\) for \(a_m<Q/2\) and \(Q>4\). Hence \(H(m)>0\) whenever \(1<m<s\). Monotonicity of \(F_Q\) gives a unique \(z_m=g(b_m)>q_Q\). At every \(y>b_m\), the gas-only and droplet-gas branches have constant \(F_Q\)-difference \(H(m)>0\), so \(g(y)>d(y)\) there. Thus the density difference switches sign **exactly once**, at the interface, where a jump is permitted.

By the characterization of total variation through the positive part of the signed density difference, the optimal hypothesis region is \(\{|X|<b_m/\chi\}\). The droplet and gas tail probabilities past that radius are \(1/m\) and \(\Phi_Q(z_m)/m\), respectively. Their difference is the claimed \(\mathcal D_Q(m)\). The standard equal-prior Bayes-risk identity yields \(P_{\mathrm{error}}=(1-\mathcal D_Q(m))/2\). In particular \(0<\mathcal D_Q(m)<1-1/m\).

**3. Exact monotonicity and unique maximum criterion.** Parameterize the pure-gas origin density by \(a\in(q_Q,Q/2)\) with \(m=\Phi_Q(a)\), strictly increasing in \(a\). The interface pure-gas value \(z=z(a)\) satisfies \(F_Q(z)=F_Q(a)-Q^{-1}\log\Phi_Q(a)\), and \(0<z<a\). Implicit differentiation gives
\[
\frac{1}{z}\frac{dz}{da}
=\frac{1-2a/Q}{1-2z/Q}
\left(\frac1a-\frac1{Q\Phi_Q(a)}\right).
\]
Because \(0<z<a<Q/2\) and \(Q-a>1\), both factors are positive and the right side is strictly less than \(1/a\). Hence \(0<z_a<z/a\).

Differentiating \(\Phi_Q(z_m)\) with respect to \(m\), using the implicit \(F_Q\) equation, yields
\[
\frac{d}{dm}\Phi_Q(z_m)=\frac{z_m}{a_m}-\frac{z_m}{Qm}.
\]
The quotient rule then gives \(\mathcal D'_Q(m)=m^{-2}[1-z_m(a_m+1-z_m)/Q]\). In the \(a\)-parameterization,
\[
\frac{dG_Q}{da}=-\frac1Q\,[z+(a+1-2z)z_a].
\]
The bracket is positive: if \(a+1-2z\ge0\), both terms have the required sign. Otherwise, since \(z_a<z/a\), the bracket exceeds \(z+z(a+1-2z)/a=z(2a+1-2z)/a>0\). Hence \(G_Q\) is **strictly decreasing**. Its lower limit is \(1-q_Q/Q=1/q_Q>0\); its upper limit is \(G_*\). This proves the exhaustive monotone/unique-interior-maximum dichotomy.

Both cases really occur, without relying on floating-point sign tests. For \(Q=5\), \(z_*(Q/2+1-z_*)\le(7/2)^2/4=49/16<5\), so \(G_*>0\). For \(Q=20\), let \(s=5\). The value \(z_*\) solves \(F_{20}(z_*)=\log10-1-\log5/20\), which lies strictly between \(F_{20}(6)\) and \(F_{20}(7)\); thus \(6<z_*<7\). On this interval \(z_*(11-z_*)\ge28>20\), so \(G_*<0\). Consequently \(\mathcal D_{20}\) has exactly one interior maximum even though \(1-1/m\), the dense mass fraction, increases strictly with \(m\).

**4. Onset and upper-fold asymptotics.** At \(m=1\), the profiles meet, \(z_1=a_1=q_Q\), and the derivative formula gives \(\mathcal D'_Q(1+)=1/q_Q\); smoothness for fixed \(Q>4\) supplies the stated linear onset.

At the upper fold write \(m=s(1-\epsilon^2)\), so \(a_m=Q(1-\epsilon)/2\). Because
\[
F_Q(a_m)=F_Q(Q/2)+\log(1-\epsilon)+\epsilon
=F_Q(Q/2)-\frac{\epsilon^2}{2}-\frac{\epsilon^3}{3}+O(\epsilon^4),
\]
and
\[
\frac{\log m}{Q}=\frac{\log s}{Q}-\frac{\epsilon^2}{Q}+O(\epsilon^4),
\]
the implicit equation at the interface yields
\[
F_Q(z_m)=F_Q(z_*)+(1/Q-1/2)\epsilon^2-\epsilon^3/3+O(\epsilon^4).
\]
Here \(z_*<Q/2\), so \(F_Q'(z_*)>0\), permitting ordinary Taylor inversion. Using \(\Phi_Q'(z_*)/F_Q'(z_*)=z_*\),
\[
\Phi_Q(z_m)=\Phi_Q(z_*)+z_*(1/Q-1/2)\epsilon^2-z_*\epsilon^3/3+O(\epsilon^4).
\]
Dividing by \(m=s(1-\epsilon^2)\) proves the displayed three-halves-power expansion, including its explicit nonzero coefficient. Differentiating that expansion twice in \(m\) gives a negative one-sided curvature divergence proportional to \(-(s-m)^{-1/2}\).

## Verification

A standalone checker, `verify.py`, independently constructs the two profiles from their Lambert-function expressions, integrates their absolute density difference, checks the unique crossing and the exact derivative, and probes the upper-fold coefficient. Executed from the embedded package, it passed 2,180 bounded checks across eight crowding parameters and multiple coexistence values. Selected numerical illustrations: for \(Q=20\), the unique maximizer is at \(m\approx4.883313195\) with \(\mathcal D\approx0.678599108\); the fold value at \(m=5\) is \(\mathcal D_*\approx0.677904506\). These decimals illustrate, rather than establish, the universal statements proved above.

The strict monotonicity proof, one-crossing argument, and spinodal expansion are analytical and do not rely on finite checks. Code uses Python with NumPy/SciPy and does not attempt microscopic finite-particle or time-dependent simulation.

## Relationship to prior work

Grange (arXiv:2610.26149v1/v2, first submitted 19 October 2026) derives the precise mean-field kinetic equations, stationary pure-gas and droplet profiles, interface conditions, their coexistence window, and a nonmonotone *droplet width*. All these facts are used as established input. An earlier analytical result on these profiles establishes radial stochastic ordering of coexisting branches and exact total variation *against exponential reference laws*. Such ordering does not by itself identify the single-crossing likelihood-ratio boundary, the exact **interbranch** total variation, its interior maximum criterion, or the three-halves-fold coefficient. The present theorem concerns those additional quantities, not a newly constructed phase or new stationary density formula.

Thompson–Tailleur–Cates–Blythe (arXiv:1012.0786) establish related density-dependent run-and-tumble lattice dynamics. Pelizzola–Pretti–Zamparo (arXiv:2012.10993) and Miron–Reuveni (arXiv:2011.08241) analyze local resetting with exclusion in different lattice models. Those frameworks support the motivation but do not, in the inspected accessible material, supply this two-branch snapshot-decision frontier. A source with exact generic density laws may entail these observables after new analysis; independent publication-priority assessment remains necessary.

## Limitations

The theorem is conditioned on the two explicit symmetric continuum stationary branches, equal prior phase odds, and a single mass-weighted spatial observation. It does not prove the stationary branches are dynamically stable, estimate the probability of phase switching, or establish a detection theorem for correlated microscopic particle configurations. The exact sign criterion \(G_*\) is a complete classification *for each fixed \(Q\)*; no global uniqueness theorem for a crowding threshold \(Q_*\) is asserted. At \(m=s\) the gas-only branch exists only as a limiting fold solution; the three-halves expansion is one-sided. Prior full-density and radial-quantile formulas are known, so this theorem is a specialized, analytically evaluated observability consequence rather than a new stationary-state solution. Publication priority and independent mathematical verification have not been established.

## References

1. Pascal Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149v2 (2026), https://arxiv.org/html/2610.26149v2 ; original submission https://arxiv.org/abs/2610.26149v1 (19 October 2026).
2. A. G. Thompson, J. Tailleur, M. E. Cates, R. A. Blythe, *Lattice Models of Nonequilibrium Bacterial Dynamics*, arXiv:1012.0786, https://arxiv.org/abs/1012.0786 .
3. A. Pelizzola, M. Pretti, M. Zamparo, *Simple Exclusion Processes with Local Resetting*, arXiv:2012.10993, https://arxiv.org/abs/2012.10993 .
4. A. Miron, S. Reuveni, *Diffusion with Local Resetting and Exclusion*, arXiv:2011.08241, https://arxiv.org/abs/2011.08241 .
