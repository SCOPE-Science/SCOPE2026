# A sharp dispersal-mortality paradox in an alternating two-habitat population

## Finding

In a deterministic, density-independent two-habitat population with perfectly alternating habitat qualities, a single survival penalty on migration creates **two different sharp dispersal thresholds**. For any high and low annual multipliers \(a>b>0\), migration survival \(0<s\leq1\), and constant migration fraction \(m\in[0,1]\), the exact asymptotic per-year multiplication factor is
\[
 R(m)=\frac{s(a+b)m+\sqrt{s^2(a-b)^2m^2+4ab(1-m)^2}}2.
\]
It is strictly convex in \(m\) over the entire admissible interval. Thus *no strictly partial dispersal fraction maximizes the asymptotic growth factor*. Complete habitat swapping is the unique optimum if \(s>\sqrt{b/a}\), zero migration is the unique optimum if \(s<\sqrt{b/a}\), and both endpoints (only) are optima at equality.

More subtly, the effect of an infinitesimal amount of migration is negative exactly when \(s<2\sqrt{ab}/(a+b)\). Consequently, in the nonempty interval
\[
\sqrt{b/a}<s<\frac{2\sqrt{ab}}{a+b},
\]
**complete switching is globally optimal, yet every sufficiently small positive migration fraction is worse than none**. There is exactly one interior minimizer, not an interior maximizer.

For the exact parameters \(a=4\), \(b=1/5\), and \(s=3/10\), the completely isolated populations decline at annual factor \(2/\sqrt5<1\). At migration fraction \(m=1/10\), they decline faster at factor \(87/100\), but full swapping grows at factor \(6/5>1\). The unique threshold between extinction and growth is
\[
 m_c=\frac{85+5\sqrt{1745}}{364}\in(0,1).
\]
The population declines for \(0\leq m<m_c\), is neutrally critical at \(m=m_c\), and grows for \(m>m_c\).

## Assumptions and scope

The population is represented by nonnegative vectors \(x_t\in\mathbb R_{\ge0}^2\), with a strictly positive initial vector if the per-year factor is interpreted as total abundance growth. In alternating years local growth matrices are
\[
G_0=\begin{pmatrix}a&0\\0&b\end{pmatrix},\qquad
G_1=\begin{pmatrix}b&0\\0&a\end{pmatrix}.
\]
Every year an unconditional fraction \(m\) leaves each patch for the other, surviving movement with probability \(s\); residents do not suffer movement mortality. Thus
\[
 D_m=\begin{pmatrix}1-m&sm\\sm&1-m\end{pmatrix},\qquad
 x_{t+1}=D_m G_{t\bmod2}x_t.
\]
Here \(a>b>0\), \(s\in(0,1]\), and \(m\in[0,1]\); the model is linear, with period exactly two. “Growth” and “decline” refer to deterministic exponential asymptotics, not to a finite-population extinction probability. At reducible endpoints \(m=0\) and \(m=1\), strictly positive initial populations ensure the stated top exponential factor is attained. No nonlinear carrying capacity or selection dynamics is asserted.

## Proof

Let \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), which interchanges patches. Both \(D_m\) and \(G_1\) obey \(JD_mJ=D_m\) and \(JG_0J=G_1\). Hence the two-year monodromy has the exact square reduction
\[
 M_2=D_mG_1D_mG_0=(JD_mG_0)^2.
\]
The nonnegative one-year transformed matrix \(T=JD_mG_0\) is
\[
 T=\begin{pmatrix}sma&(1-m)b\\(1-m)a&smb\end{pmatrix},
\]
with trace \(sm(a+b)\) and determinant \(ab[s^2m^2-(1-m)^2]\). Its Perron root is precisely \(R(m)\) as printed above. Since \(M_2=T^2\), its spectral radius is \(R(m)^2\), establishing the annual factor, including both endpoints by direct substitution.

Set \(u=s(a-b)>0\), \(v=2\sqrt{ab}>0\), and \(H(m)=\sqrt{u^2m^2+v^2(1-m)^2}\). Direct differentiation gives
\[
 R''(m)=\frac{u^2v^2}{2H(m)^3}>0\qquad(0\leq m\leq1).
\]
Strict convexity proves every nonendpoint is strictly below the maximum of the two endpoints. Those values are \(R(0)=\sqrt{ab}\) and \(R(1)=sa\); comparing gives exactly \(s=\sqrt{b/a}\) as the optimizer switching curve, with the stated uniqueness and tie cases.

The endpoint slopes are
\[
 R'(0)=\frac{s(a+b)}2-\sqrt{ab},\qquad R'(1)=sa>0.
\]
Consequently, for \(s<2\sqrt{ab}/(a+b)\), the strictly increasing derivative has one zero in \((0,1)\), which is a unique minimum. For \(s\geq2\sqrt{ab}/(a+b)\), \(R\) is strictly increasing on \((0,1]\), with possible zero derivative only at \(m=0\). Since \(a>b\), the strict inequality \(\sqrt{b/a}<2\sqrt{ab}/(a+b)\) follows after multiplication from \(a+b<2a\), proving the paradoxical interval is nonempty.

In the concrete example, substitution yields
\[
 R(m)=\frac{63m+\sqrt{11249m^2-16000m+8000}}{100}.
\]
The asserted factors at \(m=0,1/10,1\) follow by exact arithmetic. Solving \(R(m)=1\), requiring a nonnegative square-root side before squaring, gives only the displayed \(m_c\) inside \([0,1]\); the other algebraic root is negative. Strict convexity plus the single interior minimum and endpoint factors implies \(R(m)<1\) exactly below \(m_c\) and \(R(m)>1\) exactly above it. This completes the proof.

## Verification

Run \(\texttt{python verify.py}\) with Python 3 and SymPy installed. The checker reconstructs \(M_2\) and \(T^2\) symbolically, proves trace, determinant, discriminant, curvature and endpoint-slope identities, checks the exact rescue witness, and independently verifies characteristic-polynomial identities at 38 rational parameter points. All checks passed in the attached standalone code. The universal inequalities follow from the displayed analytic proof, not from the finite test grid.

## Relationship to prior work

Schreiber (2010) analyzes autocorrelation, spatial heterogeneity and growth under partially mixing population models, predominantly through approximation and stochastic environments. Schreiber and Li (2011; preprint 2010) derive general selection principles for unconditional dispersal in periodic environments; their migration operator is stochastic and explicitly assumes no movement mortality. Bansaye and Lambert (2013; preprint 2012) derive broad source–sink persistence and ancestral-lineage criteria, including periodic environments, but their inspected periodic examples do not give this survival-penalized, exactly alternating two-patch dispersal optimum or the two distinct cost thresholds. Wu (2016) analyzes travel loss in a continuous-time, density-dependent resident–mutant system at constant patch qualities, addressing an evolutionarily stable strategy rather than the present periodically forced linear Floquet optimum. Katriel (2021) analyzes continuous-time symmetric migration with time-periodic growth; its dynamics do not include complete discrete-time habitat swapping or movement-survival penalties.

The present result is a closed, necessary-and-sufficient parameter classification for this discrete two-patch mechanism, not a claim that dispersal-induced growth, convexity of norms, Perron theory or movement-cost tradeoffs were invented here.

## Limitations

A general older matrix optimization identity or an uninspected equivalent special calculation could precede this statement. Novelty is assessed against accessible literature and mathematical implication rather than certified historical priority. The model presumes exact anticorrelation and annual habitat swaps, fixed per-migrant mortality, equal migration propensities in both directions, deterministic linear growth, and no uncertainty in parameters. The result does not determine optimal dispersal under general seasonality, nonlinear regulation, demographic stochasticity, mutation/competition or real conservation deployments. Exponential decline is a deterministic statement and does not prove almost-sure extinction of an unspecified branching process.

## References

1. Sebastian J. Schreiber, “Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence,” *Proceedings of the Royal Society B* 277 (2010), 1907–1914. First published 2010-02-17. DOI: https://doi.org/10.1098/rspb.2009.2006 . Full text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2019/10/prsb-10.pdf .
2. Sebastian J. Schreiber and Chi-Kwong Li, “Evolution of unconditional dispersal in periodic environments,” *Journal of Biological Dynamics* 5 (2011), 120–134. Preprint https://arxiv.org/abs/1007.5267 (2010-07-29). DOI: https://doi.org/10.1080/17513758.2010.525667 . Full text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2021/04/Evolution-of-unconditional-dispersal-in-periodic-environments.pdf .
3. Vincent Bansaye and Amaury Lambert, “New approaches to source-sink metapopulations decoupling demography and dispersal,” *Theoretical Population Biology* 88 (2013), 31–46. Preprint https://arxiv.org/abs/1210.4641 (2012-10-17). DOI: https://doi.org/10.1016/j.tpb.2013.06.003 .
4. Chang-Hong Wu, “The optimal dispersal strategy: A two-patch model with travel loss,” *Tamkang Journal of Mathematics* 47 (2016), 27–38. DOI: https://doi.org/10.5556/j.tkjm.47.2016.1883 .
5. Guy Katriel, “Dispersal-induced growth in a time-periodic environment,” arXiv https://arxiv.org/abs/2104.01589 (2021-04-04).
