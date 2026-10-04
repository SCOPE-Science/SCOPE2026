# A rigorous finite-horizon fear threshold for prey extinction

## Finding

Consider
\[
u'
=
\frac{au}{1+kv}
-bu^2
-cu^pv^m,
\qquad
v'
=
-dv+eu^pv^m,
\]
where all parameters are positive,
\[
0<p<1,
\qquad
0<m<1,
\]
and
\[
u(0)=u_0>0,
\qquad
v(0)=v_0>0.
\]

A finite-horizon sufficient condition for prey extinction can be written explicitly.

Define
\[
R_T
=
\frac{(1-p)cv_0^m(1-e^{-mdT})}
{md\,u_0^{1-p}}.
\]
If
\[
R_T>1,
\]
then every fear strength satisfying
\[
k>
K(T)
:=
\frac{(1-p)a(e^{dT}-1)}
{dv_0\log R_T}
\]
forces the prey variable to reach zero at some time
\[
t_*<T.
\]

Equivalently, there is at least one horizon for which this explicit certificate is available exactly when
\[
R_\infty
:=
\frac{(1-p)cv_0^m}
{md\,u_0^{1-p}}
>1.
\]

For the initial data and parameters used in Figure 6 of the motivating paper,
\[
u_0=4.8,\qquad
v_0=8.3,
\]
\[
a=2.5,\quad
b=0.3,\quad
c=2.5,\quad
d=2,\quad
e=2.5,\quad
p=0.2,\quad
m=0.4,
\]
one obtains
\[
R_\infty
\approx
1.661798090950775.
\]
Taking
\[
T=1.5
\]
gives
\[
R_T
\approx
1.161274124589654
\]
and
\[
K(T)
\approx
15.37918897486502.
\]
Thus
\[
k=16
\]
is a rigorous certificate that the prey becomes extinct before time \(1.5\) for those initial data.

This is a quantitative sufficient result. It does not establish the full theorem claimed in the source for every parameter set and initial condition covered by that theorem, and it does not certify the source's plotted value
\[
k=0.03.
\]

## Assumptions and scope

The result is for classical positive solutions up to their first prey-extinction time. The argument uses only
\[
a,c,d,k,u_0,v_0,p,m;
\]
the logistic coefficient \(b\) and conversion coefficient \(e\) can only make the estimates used here more favorable and therefore do not appear in the certificate.

The sublinear condition
\[
0<p<1
\]
is essential for the transformation
\[
w=u^{1-p}
\]
and for finite-time extinction under a sufficiently strong negative sublinear term.

The certificate is sufficient, not necessary. Failure of
\[
R_\infty>1
\]
does not imply that fear-driven extinction is impossible; it only means that this particular comparison estimate cannot certify it.

The source's Figure 6 uses
\[
k=0.03.
\]
The present estimate is intentionally not used to validate that numerical value. Its purpose is to give a rigorous finite-horizon threshold in a regime where the comparison can be closed analytically.

## Proof

Before the first time at which \(u\) reaches zero,
\[
v'
=
-dv+eu^pv^m
\ge
-dv.
\]
Therefore
\[
v(t)\ge v_0e^{-dt}.
\]

Since
\[
1+kv\ge kv,
\]
the prey equation satisfies
\[
u'
\le
\frac{a}{kv}u
-cu^pv^m.
\]
Using the lower bound for \(v\),
\[
u'
\le
\frac{ae^{dt}}{kv_0}u
-cv_0^me^{-mdt}u^p.
\]

For positive \(u\), let
\[
w=u^{1-p}.
\]
Then
\[
w'
=
(1-p)u^{-p}u'
\]
and hence
\[
w'
\le
(1-p)\frac{ae^{dt}}{kv_0}w
-(1-p)cv_0^me^{-mdt}.
\]

Define
\[
\Phi_k(t)
=
\frac{(1-p)a}{kdv_0}(e^{dt}-1).
\]
Because
\[
\Phi_k'(t)
=
(1-p)\frac{ae^{dt}}{kv_0},
\]
multiplication by the integrating factor
\[
e^{-\Phi_k(t)}
\]
gives
\[
\frac{d}{dt}
\left(
e^{-\Phi_k(t)}w(t)
\right)
\le
-(1-p)cv_0^m
e^{-mdt-\Phi_k(t)}.
\]
After integration,
\[
w(t)
\le
e^{\Phi_k(t)}
\left[
u_0^{1-p}
-
(1-p)cv_0^m
\int_0^t
e^{-mds-\Phi_k(s)}\,ds
\right].
\]

Suppose the prey remained positive through a time \(T\). Then \(w(T)>0\). Therefore a contradiction is obtained whenever
\[
(1-p)cv_0^m
\int_0^T
e^{-mds-\Phi_k(s)}\,ds
>
u_0^{1-p}.
\]
This proves the sharper integral certificate.

For a closed-form bound, note that
\[
0\le s\le T
\quad\Longrightarrow\quad
\Phi_k(s)\le\Phi_k(T).
\]
Hence
\[
\int_0^T
e^{-mds-\Phi_k(s)}\,ds
\ge
e^{-\Phi_k(T)}
\int_0^T e^{-mds}\,ds
\]
and therefore
\[
\int_0^T
e^{-mds-\Phi_k(s)}\,ds
\ge
e^{-\Phi_k(T)}
\frac{1-e^{-mdT}}{md}.
\]

The contradiction condition follows if
\[
R_Te^{-\Phi_k(T)}>1,
\]
where
\[
R_T
=
\frac{(1-p)cv_0^m(1-e^{-mdT})}
{md\,u_0^{1-p}}.
\]
When
\[
R_T>1,
\]
taking logarithms shows that this is exactly
\[
k>
\frac{(1-p)a(e^{dT}-1)}
{dv_0\log R_T}.
\]

Finally,
\[
R_T
\uparrow
R_\infty
=
\frac{(1-p)cv_0^m}
{md\,u_0^{1-p}}
\]
as
\[
T\to\infty.
\]
Thus a horizon with
\[
R_T>1
\]
exists if and only if
\[
R_\infty>1.
\]

## Verification

The bundled script `verify.py` independently evaluates the Figure 6 parameter set at high precision.

It checks
\[
R_\infty
\approx
1.661798090950775,
\]
\[
R_{1.5}
\approx
1.161274124589654,
\]
and
\[
K(1.5)
\approx
15.37918897486502.
\]

At
\[
k=16,
\]
the closed-form sufficient inequality has normalized margin
\[
R_{1.5}e^{-\Phi_{16}(1.5)}
\approx
1.005818253780147
>
1.
\]
Direct numerical quadrature of the sharper integral gives the larger normalized margin
\[
\frac{(1-p)cv_0^m}{u_0^{1-p}}
\int_0^{1.5}
e^{-mds-\Phi_{16}(s)}\,ds
\approx
1.128993918149717
>
1.
\]

The numerical calculations only replay the explicit certificate for the source parameter set. The finite-time implication itself is proved analytically above.

## Relationship to prior work

Antwi-Fordjour, Parshad, Thompson, and Westaway introduce the fear-driven herd-behavior model and make finite-time prey extinction a central result. Their Theorem 5.1 argues that sufficiently strong fear can move initial data that coexist when
\[
k=0
\]
into finite-time prey extinction. The published proof obtains an upper comparison for the prey and later a strictly positive upper bound. A positive upper bound alone does not establish that the prey reaches zero in finite time. The same section notes that a necessary condition on the size of the fear parameter remains unproved.

Antwi-Fordjour, Parshad, and Beauregard previously studied finite-time extinction in a different predator-prey system without the present fear term. That work develops comparison methods for sublinear predation and supplies sufficient conditions based on initial data, but it does not give the present \(k\)-dependent finite-horizon threshold.

Later work by Antwi-Fordjour and Takyi gives explicit extinction-time estimates in a different susceptible-infectious-predator system with fear and an Allee effect. This confirms that quantitative extinction bounds are a natural object in related models, but its equations and comparison structure are different from the two-dimensional model considered here.

Bearden and Antwi-Fordjour study finite-time extinction in another square-root predator-prey model. Only abstract-level material was available for inspection, so it remains a residual literature risk rather than evidence of coverage.

The contribution here is therefore narrow: it gives an explicit sufficient
\[
k
\]
versus
\[
T
\]
certificate for the exact two-dimensional fear-driven model and evaluates it on the motivating paper's own Figure 6 initial data.

## Limitations

The certificate is conservative. In particular, it does not certify the source's displayed simulation at
\[
k=0.03,
\]
and no claim is made that
\[
15.37918897486502
\]
is a sharp threshold.

The sufficient regime
\[
R_\infty>1
\]
is a property of the comparison argument, not a claimed necessary condition for extinction in the original nonlinear system.

The analysis proves finite-time loss of the prey variable. After that event, the classical positive-state formulation with fractional power
\[
u^p
\]
must be interpreted with care at and beyond the boundary; the result does not prescribe an extension to negative prey values.

No claim is made that the full generality of the motivating paper's Theorem 5.1 has been repaired. The proven statement is the explicit finite-horizon certificate above.

## References

1. K. Antwi-Fordjour, R. D. Parshad, H. E. Thompson, S. B. Westaway, “Fear-driven extinction and (de)stabilization in a predator-prey model incorporating prey herd behavior and mutual interference,” AIMS Mathematics 8 (2023), 3353–3377. DOI: 10.3934/math.2023173. Preprint: arXiv:2108.00546.
2. K. Antwi-Fordjour, R. D. Parshad, M. A. Beauregard, “Dynamics of a predator-prey model with generalized functional response and mutual interference,” Mathematical Biosciences 326 (2020), 108407. DOI: 10.1016/j.mbs.2020.108407. Preprint: arXiv:2003.02712.
3. A. Bearden, K. Antwi-Fordjour, “On a Predator-Prey Model with Square Root Functional Response,” Journal of Applied Nonlinear Dynamics 15 (2026). DOI: 10.5890/JAND.2026.06.011.
4. K. Antwi-Fordjour, E. M. Takyi, “Finite-time extinction in a susceptible-infectious-predator model with dual fear, Allee effect, and sublinear predator aggregation,” Mathematical Biosciences and Engineering 23 (2026). DOI: 10.3934/mbe.2026104.
