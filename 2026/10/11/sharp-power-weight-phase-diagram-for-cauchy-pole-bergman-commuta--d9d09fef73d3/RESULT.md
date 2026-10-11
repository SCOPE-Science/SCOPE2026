# Sharp power-weight phase diagram for Cauchy-pole Bergman commutators

## Finding

Let
\[
\mathbb H=\{z=x+iy:y>0\},
\qquad
\alpha>-1,
\]
with weighted area measure
\[
dA_\alpha(z)=c_\alpha y^\alpha\,dx\,dy,
\]
where the harmless constant \(c_\alpha>0\) is fixed.

For real parameters \(u,v\) satisfying
\[
|u|<\alpha+1,
\qquad
|v|<\alpha+1,
\]
set
\[
\mu_u(z)=y^u,
\qquad
\lambda_v(z)=y^v,
\qquad
s=\frac{u-v}{2}.
\]
For any pole
\[
\zeta\in\{w:\operatorname{Im}w<0\}
\]
and exponent
\[
r>0,
\]
define
\[
b_{r,\zeta}(z)=(z-\zeta)^{-r}
\]
with the holomorphic logarithm whose argument lies in \((0,\pi)\).

Then the two commutators
\[
[b_{r,\zeta},P_\alpha]
\quad\text{and}\quad
[b_{r,\zeta},P_\alpha^+]
\]
are bounded
\[
L_\alpha^2(\mu_u)\longrightarrow L_\alpha^2(\lambda_v)
\]
if and only if
\[
-r\le s\le1.
\]
Equivalently, boundedness holds exactly in the closed strip
\[
-2r\le u-v\le2.
\]

The same commutators are compact exactly in the open strip
\[
-r<s<1,
\]
equivalently
\[
-2r<u-v<2.
\]
Hence every admissible boundary point of the boundedness strip is bounded but not compact.

The two boundaries have different geometric origins. The upper boundary
\[
s=1
\]
is forced by shrinking Carleson boxes and the nonzero first derivative of the symbol at the boundary. The lower boundary
\[
s=-r
\]
is forced by Carleson boxes escaping to infinity and the exact decay order
\[
|b_{r,\zeta}(z)|\asymp |z|^{-r}.
\]

## Assumptions and scope

For an interval
\[
I\subset\mathbb R
\]
of length
\[
L=|I|,
\]
write
\[
Q_I=I\times(0,L).
\]
The weighted BMO seminorm used here is
\[
\sup_I
\frac{1}{\nu(Q_I)}
\int_{Q_I}|b-b_{Q_I}|\,dA_\alpha,
\]
where
\[
\nu=\mu_u^{1/2}\lambda_v^{-1/2}=y^s
\]
and
\[
b_{Q_I}
\]
denotes the \(dA_\alpha\)-average of \(b\) on \(Q_I\).

The source theorem characterizes boundedness and compactness of the analytic-symbol Bergman commutators by membership in the corresponding weighted spaces
\[
\operatorname{BMOA}_\nu
\quad\text{and}\quad
\operatorname{VMOA}_\nu.
\]
The present result evaluates those abstract conditions exactly for the canonical scale-homogeneous power weights and a Cauchy-pole symbol.

The hypotheses
\[
|u|<\alpha+1,
\qquad
|v|<\alpha+1
\]
are exactly the power-weight Békolle--Bonami conditions. They also imply
\[
|s|<\alpha+1,
\]
so
\[
\nu=y^s
\]
belongs to the same weight class.

The pole is required to remain strictly below the real axis. The theorem does not address boundary poles, interior singularities, nonanalytic symbols, or symbols with a different decay profile.

## Proof

First note that for every real \(q\),
\[
y^q\in\mathcal B_2
\]
if and only if
\[
|q|<\alpha+1.
\]
Indeed,
\[
A_\alpha(Q_I)\asymp L^{\alpha+2},
\]
and, provided the relevant integral is finite,
\[
\frac{1}{A_\alpha(Q_I)}
\int_{Q_I}y^q\,dA_\alpha
\asymp L^q.
\]
The reciprocal average is correspondingly comparable to
\[
L^{-q}.
\]
Both local integrals are finite precisely when
\[
-\alpha-1<q<\alpha+1.
\]

Horizontal translation and positive dilation reduce the symbol to
\[
b(z)=(z+i)^{-r}.
\]
Indeed, if
\[
\zeta=a-ih,
\qquad h>0,
\]
then the change of variables
\[
z=a+hw
\]
takes Carleson boxes to Carleson boxes, while the numerator and denominator of the weighted oscillation quotient acquire fixed powers of \(h\). This changes the seminorm only by a finite nonzero factor and does not change either vanishing condition.

For a box \(Q_I\), define
\[
\mathcal O_s(I)
=
\frac{\displaystyle\int_{Q_I}|b-b_{Q_I}|\,dA_\alpha}
{\displaystyle\int_{Q_I}y^s\,dA_\alpha}.
\]
Its denominator is exactly comparable to
\[
L^{\alpha+s+2}.
\]

Let
\[
R=1+\operatorname{dist}(I,0).
\]
Suppose first that
\[
L\le \frac{R}{4}.
\]
On \(Q_I\), the distance to the pole is comparable to \(R\), and
\[
|b'(z)|
=
r|z+i|^{-r-1}
\lesssim
R^{-r-1}.
\]
Using the mean oscillation bound obtained from pairs of points in the box gives
\[
\int_{Q_I}|b-b_{Q_I}|\,dA_\alpha
\lesssim
L^{\alpha+3}R^{-r-1}.
\]
Consequently
\[
\mathcal O_s(I)
\lesssim
L^{1-s}R^{-r-1}.
\]
If
\[
s\le1
\quad\text{and}\quad
r+s\ge0,
\]
then
\[
L^{1-s}R^{-r-1}
\lesssim
R^{-r-s},
\]
so this contribution is uniformly bounded.

Now suppose
\[
L>\frac{R}{4}.
\]
Then the horizontal location of the box is controlled by a constant multiple of \(L\), and
\[
L\gtrsim1.
\]
The elementary estimate
\[
\int_{Q_I}|b-b_{Q_I}|\,dA_\alpha
\le
2\int_{Q_I}|b|\,dA_\alpha
\]
reduces the problem to the decay of
\[
(z+i)^{-r}.
\]
A scaling estimate gives
\[
\int_{Q_I}|z+i|^{-r}\,dA_\alpha(z)
\lesssim
\begin{cases}
L^{\alpha+2-r},&r<\alpha+2,\\
\log(2+L),&r=\alpha+2,\\
1,&r>\alpha+2.
\end{cases}
\]
After division by
\[
L^{\alpha+s+2},
\]
the quotient is uniformly bounded whenever
\[
r+s\ge0.
\]
For
\[
r<\alpha+2
\]
the leading bound is
\[
L^{-r-s}.
\]
For
\[
r\ge\alpha+2,
\]
boundedness follows automatically from
\[
\alpha+s+2>1.
\]

These two cases prove
\[
b\in\operatorname{BMOA}_{y^s}
\]
whenever
\[
-r\le s\le1.
\]

Both inequalities are necessary. For the upper boundary, take
\[
I_L=[0,L]
\]
and let
\[
L\downarrow0.
\]
The Taylor expansion
\[
(z+i)^{-r}
=
i^{-r}
-r i^{-r-1}z
+
O(|z|^2)
\]
shows, after scaling
\[
z=Lw,
\]
that
\[
\int_{Q_{I_L}}|b-b_{Q_{I_L}}|\,dA_\alpha
=
c_0L^{\alpha+3}
+
o(L^{\alpha+3})
\]
for a constant
\[
c_0>0.
\]
Therefore
\[
\mathcal O_s(I_L)
\sim
c_1L^{1-s},
\qquad
c_1>0.
\]
Thus
\[
s>1
\]
is impossible.

For the lower boundary, take
\[
I_L=[L,2L]
\]
and let
\[
L\to\infty.
\]
After writing
\[
z=Lw,
\]
one has
\[
b(Lw)
=
L^{-r}(w+i/L)^{-r}.
\]
The rescaled function converges uniformly on the fixed box to the nonconstant function
\[
w^{-r}.
\]
Hence
\[
\int_{Q_{I_L}}|b-b_{Q_{I_L}}|\,dA_\alpha
=
c_2L^{\alpha+2-r}
+
o(L^{\alpha+2-r})
\]
with
\[
c_2>0.
\]
It follows that
\[
\mathcal O_s(I_L)
\sim
c_3L^{-r-s},
\qquad
c_3>0.
\]
Thus
\[
s<-r
\]
is impossible.

We have proved the exact equivalence
\[
b\in\operatorname{BMOA}_{y^s}
\quad\Longleftrightarrow\quad
-r\le s\le1.
\]

For vanishing mean oscillation, the same estimates are quantitative. If
\[
s<1,
\]
then the small-box estimate tends to zero uniformly as
\[
L\downarrow0.
\]
If
\[
r+s>0,
\]
then boxes whose Euclidean centers escape to infinity have oscillation quotient tending to zero: in the far-box case this follows from
\[
R^{-r-s},
\]
and in the comparable-box case it follows from
\[
L^{-r-s}
\]
or the stronger decay when
\[
r\ge\alpha+2.
\]
Conversely, the two asymptotic tests above show that vanishing fails at
\[
s=1
\]
and
\[
s=-r.
\]
Therefore
\[
b\in\operatorname{VMOA}_{y^s}
\quad\Longleftrightarrow\quad
-r<s<1.
\]

The source boundedness and compactness theorems now give the claimed operator phase diagram.

## Verification

The proof was checked at the level of the defining weighted oscillation quotient, rather than by numerical testing of operator norms.

The power-weight condition was reconstructed directly from the two integrals
\[
\int_0^L y^{\alpha+q}\,dy
\quad\text{and}\quad
\int_0^L y^{\alpha-q}\,dy.
\]

The upper phase boundary is certified by a first-order Taylor expansion on a fixed rescaled Carleson box. Its leading oscillation constant is strictly positive because the affine function
\[
w\mapsto w
\]
is nonconstant on that box.

The lower phase boundary is certified by a scaling limit on boxes
\[
[L,2L]\times(0,L).
\]
The limiting profile
\[
w\mapsto w^{-r}
\]
is nonconstant, so its weighted mean absolute deviation is strictly positive.

No finite experiment is used to infer any infinite statement. The only asymptotics used in the proof come from uniform convergence on fixed compact rescaled boxes or from explicit integrals.

## Relationship to prior work

Hu, Li, and Wagner characterize two-weight boundedness and compactness of analytic-symbol Bergman projection commutators on the upper half-plane by the weighted spaces
\[
\operatorname{BMOA}_\nu
\quad\text{and}\quad
\operatorname{VMOA}_\nu.
\]
Their paper provides the abstract criterion and emphasizes that the holomorphic-symbol case admits a complete two-weight characterization. It does not state an explicit power-weight/Cauchy-pole phase diagram.

Earlier Bergman Hankel-operator theory identifies BMO, VMO, and Bloch-type conditions in unweighted or differently weighted settings. In particular, Si studies BMO and Hankel operators on the Siegel upper half-space and relates holomorphic symbols to Bloch behavior. Those results supply nearby structural context but do not imply the two independent weight-imbalance thresholds
\[
s=1
\quad\text{and}\quad
s=-r
\]
for the two-weight commutators considered here.

The present calculation makes the abstract two-weight theorem completely explicit on a natural homogeneous model. It also separates the two failure mechanisms: excessive target/source weight imbalance is detected locally at shrinking boundary boxes on one side and globally at spatial infinity on the other.

## Limitations

The classification concerns power weights and a single Cauchy-pole decay law. More general regularly varying weights or sums of poles can have additional interactions not addressed here.

The pole remains a positive distance below the boundary. A boundary pole changes the local scaling and is outside the claim.

The result uses the analytic-symbol theorem. It makes no assertion for arbitrary measurable symbols, where the source shows that additional weight regularity issues arise.

The originality comparison was targeted to the source theorem, its weighted BMO/VMO formulations, power-weight specializations, Cauchy-pole symbols, and classical upper-half-plane Hankel/Bloch literature. Related estimates under a substantially different normalization remain a residual literature risk.

## References

1. B. Hu, J. Li, and N. A. Wagner, *Boundedness and compactness of Bergman projection commutators in two-weight setting*, arXiv:2504.11312v1, first posted 15 April 2025; *Journal of Fourier Analysis and Applications* 32 (2026), Article 15, DOI: 10.1007/s00041-025-10231-1.
2. J. Si, *BMO and Hankel operators on Bergman space of the Siegel upper half-space*, arXiv:2109.01320; *Complex Analysis and Operator Theory* 16 (2022), Article 24, DOI: 10.1007/s11785-022-01198-8.
