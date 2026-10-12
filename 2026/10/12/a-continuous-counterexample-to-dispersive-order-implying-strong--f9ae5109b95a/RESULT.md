# A continuous counterexample to dispersive order implying strong expectile-dispersive order
## Finding
Define \(X\) and \(Y\) by their quantile functions. At the probability knots
\[
0,\frac15,\frac25,\frac35,\frac45,1
\]
let
\[
Q_X=
\left(
0,\frac{13}{5},\frac{56}{5},\frac{58}{5},\frac{59}{5},\frac{64}{5}
\right)
\]
and
\[
Q_Y=
\left(
0,\frac{13}{5},\frac{56}{5},\frac{66}{5},\frac{67}{5},\frac{72}{5}
\right),
\]
with linear interpolation between consecutive knots.

Then
\[
X\le_{\mathrm{disp}}Y
\]
in the classical dispersive order, but
\[
X\not\le_{e\text{-}\mathrm{disp}}Y
\]
for the strong expectile-dispersive order of Eberl and Klar.

More explicitly, put
\[
u=\frac{24}{25},
\qquad
v=\frac{159}{164}.
\]
Then \(u<v\) and
\[
e_Y(u)-e_X(u)=\frac{174}{115},
\]
while
\[
e_Y(v)-e_X(v)
=
\frac{1411-\sqrt{62841}}{770}
<
\frac{174}{115}.
\]
Therefore
\[
e_Y(v)-e_Y(u)
<
e_X(v)-e_X(u),
\]
which is the reverse of the required strong expectile-dispersive inequality.

This gives a negative answer to the explicit open question asking whether dispersive order implies strong expectile-dispersive order.

## Assumptions and scope
The distributions are atomless and have compact interval supports. Their quantile functions are continuous and strictly increasing; equivalently, their cdfs are strictly increasing and continuous on their supports. Each density is positive and piecewise constant.

The strong expectile-dispersive order is the all-level order
\[
e_X(v)-e_X(u)\le e_Y(v)-e_Y(u)
\qquad
\text{for every }0<u<v<1.
\]
This is stronger than the weak expectile-dispersive order, whose defining level pairs straddle \(1/2\). The counterexample does not contradict the known implication from dispersive order to the weak expectile-dispersive order.

## Proof
The slopes of \(Q_X\) on the five probability intervals are
\[
13,\ 43,\ 2,\ 1,\ 5,
\]
and those of \(Q_Y\) are
\[
13,\ 43,\ 10,\ 1,\ 5.
\]
All slopes are positive, so both quantile functions define atomless distributions with strictly increasing continuous cdfs.

Let
\[
H(p)=Q_Y(p)-Q_X(p).
\]
Directly from the knots,
\[
H(p)=0
\quad\text{for }0\le p\le\frac25,
\]
\[
H(p)=8\left(p-\frac25\right)
\quad\text{for }\frac25\le p\le\frac35,
\]
and
\[
H(p)=\frac85
\quad\text{for }\frac35\le p\le1.
\]
Hence \(H\) is nondecreasing. For every \(0<a<b<1\),
\[
\bigl(Q_Y(b)-Q_Y(a)\bigr)
-
\bigl(Q_X(b)-Q_X(a)\bigr)
=
H(b)-H(a)\ge0.
\]
Thus \(X\le_{\mathrm{disp}}Y\).

It remains to disprove the strong expectile-dispersive order. For a continuous law with quantile \(Q\), if an expectile equals \(Q(p)\), its level is
\[
\tau_Q(p)
=
\frac{A_-(p)}{A_-(p)+A_+(p)},
\]
where
\[
A_-(p)=pQ(p)-\int_0^p Q(s)\,ds
\]
and
\[
A_+(p)=\int_p^1Q(s)\,ds-(1-p)Q(p).
\]
This is exactly the expectile balance equation
\[
\tau E[(X-e)_+]=(1-\tau)E[(e-X)_+].
\]

On the interval
\[
\frac35\le p\le\frac45,
\]
one has
\[
Q_X(p)=p+11,
\qquad
Q_Y(p)=p+\frac{63}{5}.
\]
Exact integration of the preceding quantile pieces gives
\[
A_{-,X}(p)=\frac{25p^2+143}{50},
\qquad
A_{+,X}(p)=\frac{25p^2-50p+29}{50},
\]
and
\[
A_{-,Y}(p)=\frac{25p^2+183}{50},
\qquad
A_{+,Y}(p)=\frac{25p^2-50p+29}{50}.
\]
Consequently
\[
\tau_X(p)
=
\frac{25p^2+143}
{2(25p^2-25p+86)}
\]
and
\[
\tau_Y(p)
=
\frac{25p^2+183}
{2(25p^2-25p+106)}.
\tag{1}
\]

For
\[
u=\frac{24}{25},
\]
equation (1) gives
\[
\tau_Y\!\left(\frac35\right)=u
\]
and
\[
\tau_X\!\left(\frac{79}{115}\right)=u.
\]
Thus
\[
e_Y(u)=\frac{66}{5},
\qquad
e_X(u)=11+\frac{79}{115}=\frac{1344}{115},
\]
so
\[
e_Y(u)-e_X(u)=\frac{174}{115}.
\tag{2}
\]

Next let
\[
v=\frac{159}{164}.
\]
Equation (1) gives
\[
\tau_X\!\left(\frac45\right)=v,
\]
hence
\[
e_X(v)=\frac{59}{5}.
\]
The equation \(\tau_Y(p)=v\) reduces to
\[
-1925p^2+3975p-1848=0.
\]
Its unique root in \([3/5,4/5]\) is
\[
p_v
=
\frac{159}{154}
-
\frac{\sqrt{62841}}{770}.
\]
Therefore
\[
e_Y(v)-e_X(v)
=
p_v+\frac45
=
\frac{1411-\sqrt{62841}}{770}.
\tag{3}
\]

Subtracting (3) from (2) gives
\[
\frac{23\sqrt{62841}-5657}{17710}.
\]
Both terms in the numerator are positive, and
\[
62841\cdot23^2-5657^2=1241240>0.
\]
Hence the numerator is positive. Thus
\[
e_Y(v)-e_X(v)
<
e_Y(u)-e_X(u),
\]
which is equivalent to
\[
e_Y(v)-e_Y(u)
<
e_X(v)-e_X(u).
\]
The strong expectile-dispersive order therefore fails.

## Verification
The bundled `verify.py` checks the five quantile slopes, the monotonicity of the quantile difference at every linear piece, the exact rational expectile-level identities, the quadratic equation for the irrational expectile quantile, and the final square certificate
\[
62841\cdot23^2-5657^2=1241240.
\]

A successful run ends with
`VERIFY_OK u=24/25 v=159/164 square_margin=1241240`.

The verifier is not used to replace any universal step: the dispersive ordering is proved analytically from a monotone piecewise-linear difference, and one explicit pair of expectile levels is enough to disprove the strong order.

## Relationship to prior work
Eberl and Klar define the classical dispersive order and the strong expectile-dispersive order by requiring, respectively, all quantile spacings and all expectile spacings to be ordered. Their Corollary 11 proves that dispersive order implies only the weak expectile-dispersive order. Immediately afterward they state as an open question whether dispersive order implies the strong expectile-dispersive order. Their Example 12 proves the opposite non-implication: strong expectile-dispersive order does not imply dispersive order.

Zeng, Zhuang, and Hu later use the name “ex-dispersive order” for the weak, median-straddling expectile-spacing order and prove it equivalent to dilation order. Their Remark 5.2 explicitly shows that dilation order does not control all expectile spacings when both levels are allowed on the same side of \(1/2\). That result does not settle the present implication because classical dispersive order is strictly stronger than dilation order; their counterexample is not asserted to satisfy the dispersive premise.

The construction above supplies the missing stronger premise directly: \(Q_Y-Q_X\) is nondecreasing, so classical dispersive order holds, yet two upper-tail expectile levels violate the strong spacing order.

## Limitations
This is a counterexample, not a classification of when dispersive order does imply strong expectile-dispersive order. It uses piecewise-constant positive densities; no smooth-density version is claimed here.

The terminology “expectile-dispersive order” is not uniform across the literature. Here “strong expectile-dispersive order” always means Definition 7(iii) of Eberl and Klar, with all \(0<u<v<1\).

Targeted searches and inspection of the closest later expectile-dispersion paper did not reveal a prior resolution of the exact open implication. Independent appearance under different terminology remains a residual bibliographic risk.

## References
1. A. Eberl and B. Klar, “Stochastic orders and measures of skewness and dispersion based on expectiles,” arXiv:2108.06138v1, 13 August 2021; *Statistical Papers* 64 (2023), 509–527. DOI: 10.1007/s00362-022-01331-x.
2. K. Zeng, W. Zhuang, and T. Hu, “Dispersive orderings induced by differences of inter risk measures,” *Journal of Applied Probability* 60 (2023), 358–365. DOI: 10.1017/jpr.2022.49.
