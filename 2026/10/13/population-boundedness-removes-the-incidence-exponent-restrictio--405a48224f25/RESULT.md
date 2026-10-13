# Population boundedness removes the incidence-exponent restriction in a spatial influenza model

## Finding

Consider the spatial epidemic system of Magal, Noussair, Webb, and Wu on a bounded smooth domain \(\Omega\), with
\[
h(u)=\frac{u^p}{1+\kappa u^q},
\qquad
p\ge1,\quad q\ge1,\quad \kappa>0,
\]
and
\[
b(t,\cdot)=(I-\varepsilon\Delta_N)^{-1}i(t,\cdot),
\]
where \(\Delta_N\) denotes the Laplacian with homogeneous Neumann boundary condition.

Their Theorem 3.3 assumes
\[
1\le p\le q+1
\]
and concludes extinction of infection, convergence of the susceptible and recovered populations, and strict positivity of the limiting susceptible density wherever the initial susceptible density is positive.

The upper restriction is unnecessary. Under the hypotheses of the source's global well-posedness theorem, the same complete conclusion holds for every
\[
p\ge1,\qquad q\ge1.
\]

More precisely,
\[
i(t,x)\to0
\]
for every \(x\in\overline\Omega\),
\[
i(t,\cdot)\to0
\quad\text{in }L^1(\Omega),
\]
and there are nonnegative limits \(s_\infty,r_\infty\) such that
\[
s(t,x)\to s_\infty(x),\qquad
r(t,x)\to r_\infty(x)
\]
pointwise and in \(L^1(\Omega)\). Moreover,
\[
s_\infty(x)>0
\]
for almost every \(x\) with \(s_0(0,x)>0\).

The key observation is that the model itself bounds the argument of \(h\). Let
\[
N=\|n\|_\infty,
\]
where the source's conservation law is
\[
s(t,x)+e(t,x)+i(t,x)+r(t,x)=n(x).
\]
Then
\[
0\le i(t,x)\le N.
\]
The Neumann resolvent is positive and fixes constants:
\[
(I-\varepsilon\Delta_N)^{-1}1=1.
\]
Hence order preservation gives
\[
0\le b(t,x)\le N.
\]
Consequently,
\[
h(b)
=
\frac{b^p}{1+\kappa b^q}
\le b^p
\le C_Nb,
\qquad
C_N=\max\{1,N^{p-1}\}.
\]
This bound is valid for every \(p\ge1\), independently of \(q\).

## Assumptions and scope

The domain \(\Omega\subset\mathbb R^2\) is bounded with smooth boundary, as in the source. The transmission and recovery rates are strictly positive continuous functions, the initial history is nonnegative and continuous, and
\[
\varepsilon>0,\qquad \kappa>0,\qquad p\ge1,\qquad q\ge1.
\]
These are within the source's model and global-existence framework.

The claim removes only the upper relation between the two incidence exponents. It does not treat \(p<1\), does not assert a quantitative decay rate, and does not alter the numerical calibration used in the Puerto Rico application.

## Proof

The source introduces the exposed density \(e\) and obtains the pointwise conservation law
\[
s+e+i+r=n(x).
\]
All four terms are nonnegative, so
\[
0\le i(t,x)\le n(x)\le N.
\]

Let
\[
L=(I-\varepsilon\Delta_N)^{-1}.
\]
The source already uses positivity of \(L\). Since the constant function \(1\) satisfies
\[
(I-\varepsilon\Delta_N)1=1,
\]
we have
\[
L1=1.
\]
By positivity and order preservation,
\[
0\le b=Li\le L(N)=N.
\]

For \(0\le u\le N\) and \(p\ge1\),
\[
\frac{u^p}{1+\kappa u^q}
\le u^p.
\]
If \(N\le1\), then \(u^p\le u\). If \(N>1\), then
\[
u^p=u\,u^{p-1}\le N^{p-1}u.
\]
Thus in all cases
\[
h(u)\le C_Nu,
\qquad
C_N=\max\{1,N^{p-1}\}.
\]

The source's balance identity gives
\[
\int_0^\infty\!\!\int_\Omega i(t,x)\,dx\,dt<\infty.
\]
Integrating
\[
b-\varepsilon\Delta b=i
\]
over \(\Omega\) and using the Neumann boundary condition yields
\[
\int_\Omega b(t,x)\,dx
=
\int_\Omega i(t,x)\,dx.
\]
Therefore
\[
\int_0^\infty\!\!\int_\Omega
\beta(x)h(b(t,x))\,dx\,dt
\le
\|\beta\|_\infty C_N
\int_0^\infty\!\!\int_\Omega i(t,x)\,dx\,dt
<\infty.
\]

Fubini's theorem implies, for almost every \(x\),
\[
\int_0^\infty\beta(x)h(b(t,x))\,dt<\infty.
\]
The susceptible equation integrates exactly to
\[
s(t,x)
=
s_0(0,x)
\exp\!\left(
-\int_0^t\beta(x)h(b(\delta,x))\,d\delta
\right).
\]
Hence
\[
s_\infty(x)
=
s_0(0,x)
\exp\!\left(
-\int_0^\infty\beta(x)h(b(\delta,x))\,d\delta
\right)>0
\]
for almost every \(x\) with \(s_0(0,x)>0\).

The remaining conclusions do not need the exponent relation. The source's population balance gives
\[
\int_0^\infty i(t,x)\,dt<\infty
\]
for every \(x\). All state variables and \(b\) are bounded, so the infected equation has bounded time derivative. A nonnegative integrable function with bounded derivative must tend to zero, giving
\[
i(t,x)\to0.
\]
Dominated convergence gives \(L^1\) convergence of \(i\). The susceptible component is nonincreasing and bounded below, while the recovered component is nondecreasing and bounded above; their pointwise limits and \(L^1\) convergence follow by monotonicity and dominated convergence.

Thus no step requires
\[
p\le q+1.
\]

## Verification

The proof is analytic and does not rely on a finite experiment.

The critical checks are:

1. The source's exact conservation law bounds \(i\) by \(N=\|n\|_\infty\).
2. Positivity of the Neumann resolvent together with \(L1=1\) bounds \(b\) by the same \(N\).
3. On the actually reachable interval \(0\le b\le N\),
\[
h(b)\le\max\{1,N^{p-1}\}b
\]
for every \(p\ge1\), regardless of \(q\).
4. The source's identity
\[
\int_\Omega b=\int_\Omega i
\]
then converts infected-population integrability into incidence integrability.
5. The exact susceptible formula turns that finite incidence integral into strict positivity of \(s_\infty\).

These checks establish the infinite-time statement directly.

## Relationship to prior work

The motivating source states the incidence law for the model with
\[
p\ge1,\qquad q\ge1,
\]
but its Theorem 3.3 assumes the narrower condition
\[
p\le q+1.
\]
Inspection of the proof shows that this relation is used only to obtain the global inequality
\[
h(u)\le \max\{1,1/\kappa\}u.
\]
The conservation law and elliptic equation already present in the same model give a sharper state-restricted route that does not compare the two exponents.

Targeted searches using the article title, DOI, theorem number, the phrase \(p\le q+1\), and equivalent extinction/positive-susceptible formulations did not locate a published correction or a result that removes this source-specific exponent restriction. Closest epidemic-threshold and spatial-population results found in the comparison search concern different systems and do not imply the bounded-resolvent estimate above.

## Limitations

No claim is made for \(p<1\). No convergence rate is derived.

The result is about the mathematical theorem for the printed model. It does not refit the Puerto Rico data or assert that parameter estimates would change.

The proof uses bounded total population and the order-preserving Neumann elliptic resolvent. Models without those structural properties require separate analysis.

An unindexed note or correction outside the searched literature could contain the same extension.

## References

1. P. Magal, A. Noussair, G. Webb, Y. Wu, “Modeling epidemic outbreaks in geographical regions: Seasonal influenza in Puerto Rico,” Discrete and Continuous Dynamical Systems - S 13 (2020), 3535–3550. DOI: 10.3934/dcdss.2020237.
