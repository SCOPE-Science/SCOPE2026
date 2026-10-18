# A sharp universal logit-slope barrier for epidemic oscillations, with periodic SIS witnesses

## Finding

Consider the homogeneous susceptible–infected–susceptible (SIS) epidemic coupled to continuous-time binary logit learning introduced by Maitra, Paarporn, and Eksin [1]. Define the most negative slope of the payoff difference with respect to cooperation by \(m=\max\{0,b_1-a_1,b_0-a_0\}\), with payoff differences \(a_j=T_j-R_j\), \(b_j=P_j-S_j\). The **universal slope-four threshold** is sharp:

1. For every admissible payoff matrix and all \(\beta,\gamma>0\), finite \(\sigma\geq0\), if \(\sigma m\leq4\), the model has **no nonconstant periodic orbit** in the physical open square.
2. For every \(0<\eta<1\), an explicit admissible parameter family with \(\sigma m=4+\eta\) has exactly one interior endemic equilibrium, a repelling focus, and exactly one disease-free equilibrium, a saddle. Every strictly interior initial state other than the focus has a **nonconstant periodic orbit as its complete \(\omega\)-limit set**. Hence for every positive \(\varepsilon\), periodic SIS–behavior dynamics occur at some \(4<\sigma m<4+\varepsilon\).

The quantitative sharpness concerns the universal bound: a particular model may remain nonoscillatory even if \(\sigma m>4\).

## Assumptions and scope

The state \((x,I)\in[0,1]^2\) consists of the cooperating population fraction \(x\) and infected fraction \(I\). Parameters \(\beta,\gamma>0\), \(0\leq\sigma<\infty\) are transmission, recovery and logit-rationality rates. The two payoff matrices at infection states \(j=1,0\) contain entries \(R_j,S_j,T_j,P_j\) in the convention of [1], with the source's standing assumption \(a_1=T_1-R_1>0\), \(b_1=P_1-S_1>0\), and no imposed sign on \(a_0,b_0\). Let

\[
\Delta(x,I)=(1-I)[b_1+(a_1-b_1)x]+I[b_0+(a_0-b_0)x],
\qquad L(x,I)={1\over 1+\exp(\sigma\Delta(x,I))}.
\]

The ordinary differential equations are

\[
\dot x=L(x,I)-x,\qquad
\dot I=I\,[\beta(1-x)(1-I)-\gamma].
\]

The square is forward invariant: at \(x=0,1\), the behavioral vector field points strictly inward; at \(I=0\) it is tangent, and at \(I=1\) infection strictly decreases. The statement concerns deterministic planar solutions with finite rationality; it neither describes all boundary histories nor finite-population stochastic epidemics.

## Proof

**Part I: exclusion.** As \(\Delta_x=(1-I)(a_1-b_1)+I(a_0-b_0)\geq-m\) and the logistic sensitivity obeys \(0<L(1-L)\leq1/4\), differentiation gives

\[
L_x=-\sigma L(1-L)\Delta_x\leq\sigma m/4.
\]

For the positive Dulac multiplier \(D(x,I)=1/I\) on the simply connected region \((0,1)^2\), its weighted vector-field divergence is

\[
\frac{\partial}{\partial x}\left(\frac{\dot x}{I}\right)
+\frac{\partial}{\partial I}\left(\frac{\dot I}{I}\right)
=-\frac{1+\sigma L(1-L)\Delta_x}{I}-\beta(1-x).
\]

If \(\sigma m\leq4\), the first numerator is nonnegative, while the last summand is strictly negative. Bendixson–Dulac therefore excludes all nonconstant interior cycles, including at equality \(\sigma m=4\).

**Part II: an admissible sharp family.** Fix any \(0<\eta<1\) and take

\[
\sigma=1,\quad m=4+\eta,\quad
\beta=\eta,\quad\gamma=3\eta/8,
\]
\[
a_1=m/2,\quad b_1=3m/2,\quad
 a_0=-7m/2,\quad b_0=-5m/2.
\]

These differences arise, for instance, from \(R_j=S_j=0\), \(T_j=a_j\), \(P_j=b_j\), and satisfy \(a_1,b_1>0\). They yield the simple exact payoff

\[
\Delta(x,I)=m(3/2-x-4I),\quad
\dot I=\eta I[(1-x)(1-I)-3/8].
\]

On the disease-free edge \(I=0\), a stationary \(x\) is a fixed point of \(f(x)=[1+\exp(m(3/2-x))]^{-1}\). For \(0\leq x\leq1\), \(0<f(x)<1/8\) and \(0<f'(x)=mf(x)[1-f(x)]<5/8\). Hence \(f\) has exactly one fixed point \(x_d\in(0,1/8)\) (by continuity and strict contraction). The associated boundary equilibrium \((x_d,0)\) has negative tangential eigenvalue \(f'(x_d)-1\) and positive infection eigenvalue \(\eta(1-x_d-3/8)>\eta/2\), so it is a saddle; its forward stable manifold in the physical square lies on \(I=0\).

Any endemic equilibrium has \(0<x<5/8\) and

\[
I=1-\frac{3}{8(1-x)}.
\]

Substituting into the logit equation gives the strictly decreasing left side and strictly increasing right side of

\[
\log\frac{1-x}{x}
=m\left(-\frac52-x+\frac{3}{2(1-x)}\right),
\qquad 0<x<5/8.
\]

Indeed the right derivative is \(m[-1+3/(2(1-x)^2)]>0\), and \(x=1/2\) solves the equality. Thus there is **exactly one endemic equilibrium**, \(E=(1/2,1/4)\). Direct differentiation at \(E\) gives

\[
J_E=
\begin{pmatrix}
\eta/4 & 4+\eta\\
-3\eta/16 & -\eta/8
\end{pmatrix},\quad
\operatorname{tr}J_E=\eta/8>0,\quad
\det J_E=\frac{\eta(24+5\eta)}{32}>0,
\]
\[
(\operatorname{tr}J_E)^2-4\det J_E
=-\frac{\eta(192+39\eta)}{64}<0.
\]

Therefore \(E\) is a hyperbolic repelling focus.

**Part III: interior persistence and oscillations.** Boundedness of \(\Delta\) on the square gives \(0<\ell\leq L(x,I)\leq u<1\) with constants \(\ell,u\) depending on \(\eta\). The linear comparison \(\dot x=L-x\) places every forward \(\omega\)-limit set strictly between \(x=0\) and \(x=1\). Infection satisfies \(\dot I\leq\eta I(5/8-I)\), hence \(\limsup_{t\to\infty} I(t)\leq5/8\).

For a uniform lower infection bound, put \(h=1/16\). Whenever \(I\leq h\),

\[
\Delta=m(3/2-x-4I)\geq m/4>1,
\quad L<1/3.
\]

Consequently, while \(I\leq h\) and \(x\geq1/2\), \(\dot x\leq-1/6\): in at most three time units, either \(I\) exits above \(h\), or \(x\) crosses below \(1/2\). On the remaining strip \(I\leq h\), \(x\leq1/2\),

\[
\frac{\dot I}{I}=\eta[(1-x)(1-I)-3/8]
\geq 3\eta/32>0,
\]

and the vector field at \(x=1/2\) still points toward smaller \(x\). During any excursion below \(I=h\), infection may therefore decrease only during an initial interval of length at most three. As \(\dot I/I\geq-\gamma\) always, every strictly interior solution satisfies

\[
I(t)\geq \min\{I(0),1/16\}\exp(-3\gamma)>0
\quad\text{for every }t\geq0.
\]

Thus each strictly interior trajectory has its \(\omega\)-limit set compactly contained in \((0,1)^2\). The sole interior equilibrium is a hyperbolic repeller: the local linearization admits a positive definite quadratic Lyapunov form whose derivative is strictly positive near \(E\). Accordingly \(E\) cannot belong to the \(\omega\)-limit set of any other trajectory. The planar Poincaré–Bendixson theorem then forces every such \(\omega\)-limit set to be a nonconstant periodic orbit. This establishes existence of periodic epidemics for every \(0<\eta<1\) and the exact sharpness of the constant four. \(\square\)

## Verification

The dependency-free accompanying `verify.py` rechecks rational identities for the explicit family, Jacobian trace, determinant, discriminant, equilibrium constraints, exact barrier inequalities, and finite numerical samples of the vector field. Its assertions are supplementary to the proof above; sampling cannot certify absence or existence of infinite-time periodic orbits. Reproduce using `python3 verify.py` in a standard Python 3 interpreter. No external data are needed.

## Relationship to prior work

Maitra, Paarporn, and Eksin [1, Eqs. (1)–(5), Secs. IV–VII] introduced precisely this finite-rationality SIS–logit model and analyzed equilibria and local stability with numerical convergence examples; the sharp model-wide periodic-orbit barrier and above periodic witness are not consequences of their stated results. The general Bendixson–Dulac and Poincaré–Bendixson theorems used here are classical and not claimed as new. Achterberg and Sensi [2, Theorem 4] show absence of cycles in a *different* adaptive SIS contact-density model for all its allowed response functions, using another Dulac multiplier. Their theorem does not cover the current logit payoff-feedback equations or imply a universal slope-four dichotomy. Brett et al. [3] also exclude cycles in particular behavioral-contagion SIS systems, but their behavioral response is not the bilinear payoff-dependent logit choice used here. Other epidemic–behavior models can have periodic solutions, including the independent transmission-modulation system described in [4]; the mere existence of SIS–behavior oscillations is therefore not claimed as novel. Hommes and Ochea [5] treat logit-generated cycles in other evolutionary games, not this exact epidemiological exclusion/witness theorem.

## Limitations

The inequality \(\sigma m\leq4\) is **sufficient**, not necessary, for excluding periodic orbits of an individual model. Above threshold, periodic orbits are proved only for the explicit admissible family, not every parameter set. Nothing establishes uniqueness, orbital stability, precise periods, phase amplitudes, or global attraction by a single cycle; the theorem states periodic \(\omega\)-limits individually. The result is restricted to a homogeneous deterministic two-dimensional SIS–logit system, not networked, delayed, stochastic, or empirical epidemics. Some equivalences in unindexed literature may have escaped the search; independent scientific validation has not been performed.

## References

[1] U. Maitra, K. Paarporn, C. Eksin, *SIS Epidemic Containment under Game-theoretic Rational Learning*, arXiv:2610.03173v1, publicly posted 2026-10-02. https://arxiv.org/html/2610.03173v1.

[2] M. A. Achterberg, M. Sensi, *A minimal model for adaptive SIS epidemics*, Nonlinear Dynamics 111 (2023), doi:10.1007/s11071-023-08498-4; full open text https://pmc.ncbi.nlm.nih.gov/articles/PMC10163586/.

[3] T. Brett et al., *Complex contagion leads to complex dynamics in models coupling behaviour and disease*, Journal of Biological Dynamics (2019), doi:10.1080/17513758.2018.1549278. https://www.tandfonline.com/doi/full/10.1080/17513758.2018.1549278.

[4] Plank et al., *transmission-modulated SIS epidemic–behavior model*, arXiv:2604.10995v1 (model comparison; different equations).

[5] C. H. Hommes, M. Ochea, *Multiple equilibria and limit cycles in evolutionary games with Logit Dynamics* (2012), University of Amsterdam repository https://dare.uva.nl/id/cd8acbba-c53c-4b06-942b-c3762f027692.
