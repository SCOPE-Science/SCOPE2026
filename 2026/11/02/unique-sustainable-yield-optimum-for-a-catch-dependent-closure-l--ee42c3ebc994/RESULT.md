# Unique sustainable-yield optimum for a catch-dependent-closure logistic fishery

## Finding

For logistic growth with proportional pulse harvesting and the linear, post-harvest-biomass-dependent closure rule of Córdova-Lepe, del Valle and Robledo, the sustainable catch per unit physical time has **exactly one global maximizer** over the entire persistent-effort interval. Its effort and yield are determined by one scalar equation with a strictly decreasing left side and a strictly increasing right side. Moreover, the optimal yield strictly decreases with the dimensionless closure-slope parameter, remains strictly below the continuous-harvest benchmark, and approaches that benchmark with an exact quadratic deficit:

\[
\frac{Y_{\max}(A)}{rK}=\frac14-\frac{A^2}{768}+O(A^3)\qquad(A\downarrow0).
\]

The result concerns the *state-dependent* closure policy, not an externally fixed harvesting period.

## Assumptions and scope

Let the unharvested population biomass \(X\) obey

\[
\dot X=rX(1-X/K),\qquad r>0,\ K>0.
\]

At every harvest, a constant fraction \(F\) of pre-harvest biomass is removed. Put \(u=1-F\), so the post-harvest biomass is \(uX^-\). The ensuing closed season lasts

\[
\tau=a(uK-uX^-),\qquad a>0,
\]

where \(a\) has units of time per biomass. Define \(A=raK\), and assume throughout \(0<A<4\), a sufficient parameter range for monotonicity of the harvest-to-harvest map. This is the linear closure rule studied in the motivating fishery model. If effort is expressed through Schaefer catchability \(q>0\), then \(F=qE\).

Every positive persistent orbit has a constant pre-harvest biomass \(X^*\). Define its average sustainable yield \(Y=F X^*/\tau\). Write \(W(A)\) for the unique positive solution of \(W e^W=A\), and for \(0<s<W(A)\), set

\[
C=A-se^s,\qquad B=A-s(e^s-1)=C+s.
\]

Then the entire persistent-effort interval is parameterized, bijectively, by

\[
u=1-\frac{s(e^s-1)}A,\qquad
\frac{X^*}{K}=\frac CB,\qquad
s=r\tau.
\]

The normalized sustainable yield is exactly

\[
y_A(s):=\frac{Y}{rK}=\frac{(e^s-1)C}{AB}.
\]

The unique optimizer \(s_*(A)\in(0,W(A))\) is characterized by

\[
\boxed{\frac{(A-se^s)\bigl(A-s(e^s-1)\bigr)}{A+s^2e^s}=1-e^{-s}.}
\]

The optimal removal fraction and fishing effort are

\[
F_*(A)=\frac{s_*(A)(e^{s_*(A)}-1)}A,\qquad E_*(A)=F_*(A)/q.
\]

At the lower and upper persistent-effort boundaries the sustainable catch tends to zero. Exactly one interior optimum exists; there is no optimization over alternative closure laws, size-selective fishing, stochastic recruitment, or spatially structured populations.

## Proof

**1. Persistent periodic state and exact parameterization.** Normalize biomass by \(K\), and denote a pre-harvest state by \(x\in(0,1)\). Starting the logistic flow at \(ux\) for the dimensionless duration \(s=Au(1-x)\) gives

\[
\Phi_s(ux)=\frac{ux}{ux+(1-ux)e^{-s}}.
\]

A positive fixed point \(x=\Phi_s(ux)\) is equivalent to

\[
1-u=\frac{s}{A}(e^s-1),\qquad
x=\frac{A-se^s}{A-s(e^s-1)}.
\]

Positivity of \(x\) is exactly \(0<s<W(A)\). On this interval, \(F(s)=s(e^s-1)/A\) increases strictly from \(0\) to \(1-e^{-W(A)}\). This proves the bijective parameterization and the displayed yield formula.

For completeness, the nonzero fixed point is the long-run attracting state in the stated range. The one-step map \(f_u(x)=\Phi_{Au(1-x)}(ux)\) is strictly increasing, since

\[
\frac{d}{dx}\log\frac{f_u(x)}{1-f_u(x)}
=\frac{1-Aux(1-ux)}{x(1-ux)}>0,
\]

using \(ux(1-ux)\le1/4\) and \(A<4\). Set \(t=1-x\). The sign of \(f_u(x)-x\) equals that of

\[
h_u(t)=Aut-\log\left(1+\frac{1-u}{ut}\right),
\]

which is strictly increasing in \(t>0\), tends to negative infinity as \(t\downarrow0\), and satisfies \(h_u(1)=Au+\log u\). Thus the unique positive fixed point exists precisely when \(ue^{Au}>1\); the increasing map and its single sign crossing imply convergence to it from every positive starting biomass. At equality and below, the population converges to zero.

**2. One and only one optimum.** Since \(C>0\) and \(B=C+s>0\), logarithmic differentiation gives

\[
\frac{y_A'(s)}{y_A(s)}
=\frac{e^s}{e^s-1}-\frac{A+s^2e^s}{CB}.
\]

The sign of this derivative is the sign of

\[
L_A(s)-(1-e^{-s}),\qquad L_A(s)=\frac{CB}{A+s^2e^s}.
\]

Both \(C\) and \(B\) are positive and strictly decreasing, while the denominator of \(L_A\) strictly increases. Hence \(L_A\) strictly decreases from \(A\) to \(0\) as \(s\) goes from \(0\) to \(W(A)\). The function \(1-e^{-s}\) strictly increases from \(0\) to a positive value. The two sides cross exactly once. The derivative is positive before and negative after that crossing; also \(y_A\) tends to zero at both endpoints. Therefore the crossing is the unique global maximum.

**3. Strict decrease of the maximum with \(A\).** The crossing is transverse, so \(s_*(A)\) is differentiable. At fixed \(s\), differentiation gives

\[
\partial_A y_A(s)=-\frac{(e^s-1)(C^2-s^2e^s)}{A^2B^2}.
\]

At the optimum let \(C=A-se^s\). Its first-order equation, after replacing \(A\) by \(C+se^s\), is

\[
G_s(C):=C(C+s)-(1-e^{-s})[C+se^s(1+s)]=0.
\]

For \(C\ge0\), \(G_s\) is strictly increasing because \(G_s'(C)=2C+s-(1-e^{-s})>0\). Setting \(v=e^{s/2}\), direct algebra yields

\[
G_s(sv)=\frac{s(v+1)}v\,[sv-v^2+1]<0,
\]

as \(v^2-1-sv=v[2\sinh(s/2)-s]>0\) for \(s>0\). Hence the unique root satisfies \(C>se^{s/2}\), making \(\partial_A y_A(s_*(A))<0\). The envelope identity \(d[y_A(s_*(A))]/dA=\partial_A y_A(s_*(A))\) proves strict decrease of the maximum.

**4. Continuous-harvest ceiling and small-closure limit.** On every nonconstant periodic logistic flight, the harvested biomass equals total biomass growth. Therefore

\[
\frac{Y}{rK}=\frac1\tau\int_0^\tau\left[\frac{X(t)}K\left(1-\frac{X(t)}K\right)\right]dt<\frac14.
\]

The inequality is strict because the flight is nonconstant and the integrand is \(1/4-(X/K-1/2)^2\). Choosing \(s=A/2\) for small \(A\) gives \(y_A(s)\to1/4\), so \(Y_{\max}(A)/(rK)\to1/4\). For the sharper coefficient, the stationarity equation has the analytic solution

\[
s_*(A)=\frac A2-\frac{3A^2}{16}+\frac{19A^3}{192}+O(A^4),
\]

obtained by substituting a power series into its exact derivative numerator. Substitution into \(y_A(s)\) gives the quadratic yield deficit stated above. The nondegenerate leading stationary equation after \(s=Az\) is \(1-2z=0\), which justifies the analytic expansion near \(A=0\).

## Verification

`verify.py` reproduces the derivative identities and series coefficients using exact symbolic algebra. It also evaluates rigorously bounded rational Taylor intervals for the exponential function, certifying that for \(A=1\),

\[
\frac38<s_*(1)<\frac{3751}{10000}.
\]

The certificate is finite arithmetic and supplements, rather than replaces, the preceding proofs for the full continuum of parameters. Run `python3 verify.py` with SymPy installed. The physical-scale yield is \(rK\) times the normalized output.

## Relationship to prior work

Córdova-Lepe, del Valle and Robledo (arXiv:1110.6413v1, 13 October 2011) introduce harvest-dependent closures, prove persistence/extinction conditions, and explicitly identify maximum sustainable yield under their policy as an open direction in Section 6. Their Section 5 supplies the particular linear closure law treated here, but not an optimal effort or its strict comparative statics.

Bai and Wang (2003) optimize a proportional pulse harvest at **fixed, externally prescribed** periods; their optimal-effort formula does not apply when the period changes with the harvest decision and equilibrium biomass. Braverman and Mamdani (2008) give a general pulse-versus-continuous-harvest ceiling, which is compatible with the ceiling here but does not identify this feedback-policy optimum. Bohner and Streipert (2016) analyze a discrete Beverton–Holt policy with periodic coefficients, rather than this continuous-logistic, biomass-dependent harvest clock. These sources motivated comparison by implication, not merely by title.

## Limitations

The existence and global-attraction statements rely on \(0<A<4\); this note does not claim stable realized annual yield for larger feedback slopes, where nonmonotone return maps can arise. The conclusion optimizes one fixed functional form of closure and one constant harvest fraction; it is not an optimal-control theorem over arbitrary harvest schedules. The result is deterministic and assumes exact homogeneous logistic growth and perfect biomass measurement. Historical-priority comparison is limited to the identified sources and accessible material; an exhaustive novelty guarantee or independent validation is not claimed.

## References

1. F. Córdova-Lepe, R. del Valle and G. Robledo, *A Pulse Fishery Model with Closures as Function of the Catch: Conditions for Sustainability*, arXiv:1110.6413v1 (13 October 2011), https://arxiv.org/pdf/1110.6413 ; later published in *Mathematical Biosciences* **239** (2012), 169–177, https://doi.org/10.1016/j.mbs.2012.04.004.
2. L. Bai and K. Wang, *Optimal Impulsive Harvest Policy for Time-Dependent Logistic Equation with Periodic Coefficients*, *Electronic Journal of Differential Equations* **2003**(121), 1–9 (9 December 2003), https://ejde.math.txstate.edu/Volumes/2003/121/bai.pdf.
3. E. Braverman and R. Mamdani, *Continuous versus Pulse Harvesting for Population Models in Constant and Variable Environment*, *Journal of Mathematical Biology* **57** (2008), 413–434, https://doi.org/10.1007/s00285-008-0169-z.
4. M. Bohner and S. Streipert, *Optimal Harvesting Policy for the Beverton–Holt Model*, *Mathematical Biosciences and Engineering* **13** (2016), 673–695, https://doi.org/10.3934/mbe.2016014.
