# Exact Ahmad--Xie--Li \(T_{\perp}\) constant of the real \(\ell_4^2\) plane
## Finding
For the real Banach plane \(X=\ell_4^2\), Ahmad, Xie and Li define
\[
T_{\perp}(X)=
\sup\left\{
\sqrt{\|x+y\|\,\|2x-y\|}:
 x,y\in S_X,\ x\perp_B y
\right\}.
\]
This constant has the following exact algebraic value. Let \(z_*\) be the unique root in
\[
0.8255<z<0.8256
\]
of
\[
\begin{aligned}
Q(z)={}&28561z^{14}-12324932z^{13}+214007730z^{12}-1563667459z^{11}\\
&+6135906104z^{10}-15047504769z^9+25081174393z^8-29615229256z^7\\
&+25081174393z^6-15047504769z^5+6135906104z^4-1563667459z^3\\
&+214007730z^2-12324932z+28561.
\end{aligned}
\]
Put
\[
t_*=z_*^{1/4},
\qquad
r_*=\left(\frac{1+z_*}{1+z_*^3}\right)^{1/4}.
\]
Then
\[
\boxed{
T_{\perp}(\ell_4^2)=
\left(
\frac{
\bigl((t_*+r_*)^4+(1-r_*t_*^3)^4\bigr)
\bigl((2t_*-r_*)^4+(2+r_*t_*^3)^4\bigr)
}{(1+t_*^4)^2}
\right)^{1/8}
}
\]
and numerically
\[
T_{\perp}(\ell_4^2)=2.0703790182255246\ldots.
\]
A maximizing pair is
\[
x=\frac{(t_*,1)}{(1+t_*^4)^{1/4}},
\qquad
y=\frac{(1,-t_*^3)}{(1+t_*^{12})^{1/4}}.
\]
The reduced maximizing parameter is
\[
t_*=0.9532144723643976\ldots.
\]

## Assumptions and scope
All scalars are real. The norm is
\[
\|(a,b)\|_4=(|a|^4+|b|^4)^{1/4}.
\]
Birkhoff orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|_4\ge \|x\|_4
\quad\text{for every }\lambda\in\mathbb R.
\]
Since \(\ell_4^2\) is smooth, for a unit vector \(x=(a,b)\) this is equivalent to
\[
a^3y_1+b^3y_2=0.
\]
Signed coordinate permutations are linear isometries. Hence every unit vector may be reduced to
\[
x(t)=\frac{(t,1)}{(1+t^4)^{1/4}},
\qquad 0\le t\le1.
\]
For such an \(x(t)\), the two unit Birkhoff-orthogonal directions are
\[
y_{\sigma}(t)=
\sigma\frac{(1,-t^3)}{(1+t^{12})^{1/4}},
\qquad \sigma\in\{-1,1\}.
\]
Thus the original two-vector supremum reduces without loss to two one-variable branches.

## Proof
Write
\[
r(t)=\left(\frac{1+t^4}{1+t^{12}}\right)^{1/4}.
\]
For the positive branch \(y_+(t)\), direct substitution gives
\[
\|x+y_+\|_4^4
=
\frac{(t+r)^4+(1-rt^3)^4}{1+t^4}
=:A(t),
\]
and
\[
\|2x-y_+\|_4^4
=
\frac{(2t-r)^4+(2+rt^3)^4}{1+t^4}
=:B(t).
\]
Therefore the eighth power of the objective is
\[
F_+(t)=A(t)B(t).
\tag{1}
\]
The negative branch is obtained by replacing \(r\) by \(-r\) in the numerator before taking the product. If \(P(t,r)\) denotes the numerator product in (1), exact expansion gives
\[
\begin{aligned}
P(t,r)-P(t,-r)
={}&8r^3t(t-1)(t+1)(t^2+1)(t^4+1)^2\\
&\times\bigl(r^4(t^8-t^4+1)-12r^2t^2-14\bigr).
\end{aligned}
\tag{2}
\]
For \(0<t<1\), one has \(r>0\), \(t-1<0\), and
\[
r^4(t^8-t^4+1)-12r^2t^2-14<0,
\]
because \(r^4=(1+t^4)/(1+t^{12})\le2\) and \(t^8-t^4+1\le1\). Hence (2) is positive. The two branches agree at \(t=0,1\), so
\[
F_-(t)\le F_+(t)
\qquad(0\le t\le1).
\tag{3}
\]
It remains to maximize \(F_+\).

Introduce an auxiliary variable \(r\) and the algebraic constraint
\[
G(t,r)=(1+t^{12})r^4-(1+t^4)=0.
\tag{4}
\]
Differentiating \(P(t,r)/(1+t^4)^2\) along the positive solution of (4), clearing positive denominators, and eliminating \(r\) gives the exact resultant
\[
-(1+t^4)^{18}(t^8-t^4+1)^2Q(t^4).
\tag{5}
\]
Consequently every interior stationary point must have \(Q(t^4)=0\).

A Sturm calculation gives exactly two roots of \(Q\) in \((0,1)\): one in
\[
0.0024169<z<0.0024171
\]
and one in
\[
0.8255<z<0.8256.
\]
Substitution into the original stationarity equation before elimination excludes the first interval: on the positive branch its stationarity numerator stays strictly positive there. The second interval contains one compatible root \(z_*\). The same exact-isolation calculation verifies that the derivative of \(F_+\) is positive at \(t=1/2\) and negative at \(t=99/100\). Since there is no other compatible interior stationary point, \(F_+\) increases up to \(t_*\) and decreases afterwards. Thus \(t_*\) is its unique reduced global maximizer.

Equations (1)--(5), together with (3), prove the displayed formula for \(T_{\perp}(\ell_4^2)\). The displayed pair is unit and Birkhoff-orthogonal by construction, so the maximum is attained.

## Verification
The bundled `verify.py` reconstructs the one-variable reduction symbolically. It checks the Birkhoff parametrization, factors the positive-minus-negative branch difference exactly, forms the constrained derivative, computes the resultant in (5), and verifies the displayed degree-fourteen factor coefficient by coefficient.

It then uses exact Sturm root counting to confirm that \(Q\) has precisely two roots in \((0,1)\), isolates them in disjoint rational intervals, evaluates the original pre-elimination stationarity equation on the positive algebraic branch to reject the small resultant root, and isolates the compatible root near \(0.8255863615843957\). High-precision evaluation is used only to print the decimal value after the exact algebraic and root-count checks have fixed the maximizer.

The finite decimal output is not the proof. The proof is the exact reduction, factorization, resultant identity, Sturm count, and sign isolation.

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_{\perp}\) in 2022. They proved the universal bounds
\[
\sqrt2\le T_{\perp}(X)\le\sqrt6,
\]
computed the square endpoint \(T_{\perp}(\ell_\infty^2)=\sqrt6\), and obtained the inner-product value
\[
T_{\perp}(H)=10^{1/4}.
\]
Their conclusion explicitly notes that values on further specific spaces were not obtained and were left for future study.

A public exact computation exists for the real \(\ell_3^2\) plane, but it has a different tangent parametrization and a different algebraic stationary equation. Public exact results for \(\ell_4\) also exist for the generalized rectangular constant and for an unconstrained skew geometric-mean operator norm. Neither statement implies the present Birkhoff-constrained product with the asymmetric pair of coefficients \(x+y\) and \(2x-y\).

Targeted searches under \(T_{\perp}\), Birkhoff-geometric-mean terminology, \(\ell_4\), the defining DOI, and the asymmetric \(2x-y\) objective returned no covering statement.

## Limitations
The theorem is for the two-dimensional real space \(\ell_4^2\). It does not assert the value in higher-dimensional \(\ell_4\), nor does it give a closed expression by radicals for the degree-fourteen algebraic parameter.

The exact value is specified by an isolated algebraic root and an explicit algebraic expression. The decimal expansion is only for orientation.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent computation could exist under a different notation for the Ahmad--Xie--Li constant.

## References
1. A. Ahmad, H. Xie and Y. Li, “Some new geometric constants in Banach spaces,” Advances in Fixed Point Theory 12 (2022), Article 9, doi:10.28919/afpt/7588. Published 25 August 2022. Primary MSC 46B20.
