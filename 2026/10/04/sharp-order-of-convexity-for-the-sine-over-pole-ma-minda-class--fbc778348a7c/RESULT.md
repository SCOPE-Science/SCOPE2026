# Sharp order of convexity for the sine-over-pole Ma--Minda class

## Finding

Let
\[
\xi(z)=1+\frac{\sin z}{1-z},\qquad z\in\mathbb D,
\]
and let the associated classical Ma--Minda convex class be
\[
\mathcal C_\xi
=
\left\{
 f\in\mathcal A:
 1+\frac{zf''(z)}{f'(z)}\prec\xi(z)
\right\}.
\]
The sharp order of convexity of this class is
\[
\boxed{
\mu_*
=
0.39072298833669261703444293158667137888774859706022\ldots
}.
\]
Thus every \(f\in\mathcal C_\xi\) satisfies
\[
\operatorname{Re}\!\left(1+\frac{zf''(z)}{f'(z)}\right)>\mu_*
\qquad(z\in\mathbb D),
\]
and \(\mu_*\) cannot be increased.

The constant has a canonical one-variable characterization. Put
\[
F(t)=\operatorname{Re}\xi(e^{it}),\qquad 0<t<2\pi.
\]
There is a unique minimizer on \((0,\pi)\), namely
\[
t_*
=
1.808644860488715898679582852398313963676602879316\ldots,
\]
characterized exactly by
\[
F'(t_*)
=
\operatorname{Re}\!\left(i e^{it_*}\xi'(e^{it_*})\right)
=0.
\]
Then
\[
\mu_*=F(t_*).
\]
By conjugation symmetry, the only other boundary minimizer is \(2\pi-t_*\).

## Assumptions and scope

Here \(\mathcal A\) is the usual normalized analytic class
\[
f(0)=0,\qquad f'(0)=1.
\]
The order of convexity of a family is the largest \(\mu\) for which every member satisfies
\[
\operatorname{Re}\!\left(1+\frac{zf''(z)}{f'(z)}\right)>\mu
\]
throughout the unit disk.

The source article introduces the target
\[
\xi(z)=1+\frac{\sin z}{1-z}
\]
as the classical limit of its quantum family and defines \(\mathcal C_\xi\) by the displayed subordination. It proves coefficient and determinant estimates and explicitly lists geometric properties as a future direction. The statement here addresses that geometric direction for the most basic sharp invariant of the classical class.

No assertion is made here about the quantum classes \(\mathcal C_{\xi_q}\), about uniform convexity, or about the exact Euclidean geometry of the full image \(\xi(\mathbb D)\).

## Proof

Set
\[
u(z)=\operatorname{Re}\xi(z).
\]
This is harmonic in \(\mathbb D\). For each \(0<r<1\), the minimum of \(u\) on \(|z|\le r\) is attained on \(|z|=r\). Passing to \(r\uparrow1\), every boundary accumulation point other than \(1\) is governed by
\[
F(t)=\operatorname{Re}\xi(e^{it}).
\]
The singular boundary point \(z=1\) cannot lower the infimum. Indeed,
\[
\frac{\sin z}{1-z}
=
\frac{\sin1}{1-z}-\cos1+O(|1-z|),
\]
and
\[
\operatorname{Re}\frac1{1-z}>\frac12
\qquad(|z|<1).
\]
Hence
\[
\liminf_{z\to1,\ |z|<1}u(z)
\ge
1+\frac{\sin1}2-\cos1
=
0.8804331865\ldots>
\mu_*.
\]
Consequently
\[
\inf_{z\in\mathbb D}u(z)
=
\min_{0<t<2\pi}F(t).
\]

Because \(\xi\) has real Taylor coefficients,
\[
F(2\pi-t)=F(t),
\]
so it suffices to minimize on \((0,\pi)\). Differentiation gives
\[
F'(t)=
\operatorname{Re}\!\left(i e^{it}\xi'(e^{it})\right),
\]
where
\[
\xi'(z)
=
\frac{(1-z)\cos z+\sin z}{(1-z)^2}.
\]
A reproducible interval-arithmetic certificate accompanying this result proves
\[
F'(t)<0
\quad(0.1\le t\le1.8086448),
\]
\[
F'(t)>0
\quad(1.8086449\le t\le\pi-0.1),
\]
and
\[
F''(t)>0
\quad(1.8086448\le t\le1.8086449).
\]
The endpoint arcs are separated from the candidate minimum by elementary bounds. For \(0<t\le0.1\), writing \(c=\cos t\), \(s=\sin t\),
\[
F(t)
=
1+\frac12\left[
\sin c\cosh s
-
\cos c\sinh s\,\frac{1+c}s
\right].
\]
Monotonicity of the elementary factors gives
\[
F(t)
\ge
1+\frac12\left[
\sin(\cos0.1)
-
2\cos(\cos0.1)
\frac{\sinh(\sin0.1)}{\sin0.1}
\right]
>
0.8739.
\]
For \(\pi-0.1\le t\le\pi\), the same formula and
\[
0\le\frac{1+\cos t}{\sin t}
\le
\frac{1-\cos0.1}{\sin0.1}
\]
give the coarse lower bound \(F(t)>0.57\). Both are well above \(\mu_*\).

Thus there is exactly one upper-semicircle critical point capable of being the global minimum. The interval certificate brackets it by
\[
1.8086448<t_*<1.8086449
\]
and evaluates
\[
t_*=1.808644860488715898679582852398313963676602879316\ldots,
\qquad
F(t_*)=0.39072298833669261703444293158667137888774859706022\ldots .
\]
This proves
\[
\inf_{z\in\mathbb D}\operatorname{Re}\xi(z)=\mu_*.
\]

Now take \(f\in\mathcal C_\xi\). Subordination means
\[
1+\frac{zf''(z)}{f'(z)}=\xi(\omega(z))
\]
for a Schwarz function \(\omega\), and therefore
\[
\operatorname{Re}\!\left(1+\frac{zf''(z)}{f'(z)}\right)
\ge
\inf_{w\in\mathbb D}\operatorname{Re}\xi(w)
=
\mu_*.
\]
The inequality is strict inside the disk because the harmonic function \(\operatorname{Re}\xi-\mu_*\) has positive interior values.

Finally, let \(f_*\) be the canonical extremal defined by
\[
1+\frac{zf_*''(z)}{f_*'(z)}=\xi(z),
\qquad
f_*(0)=0,
\qquad
f_*'(0)=1.
\]
This is the classical Ma--Minda extremal already implicit in the source construction. Along \(z=re^{it_*}\) with \(r\uparrow1\),
\[
\operatorname{Re}\!\left(1+\frac{zf_*''(z)}{f_*'(z)}\right)
\longrightarrow
F(t_*)=
\mu_*.
\]
Hence no larger order is valid for the entire class.

## Verification

The primary article was read in full through the definitions of \(\xi_q\) and \(\xi\), the definitions of \(\mathcal C_{\xi_q}\) and \(\mathcal C_\xi\), the extremal construction, the main coefficient theorems, and the concluding statement that geometric properties remain a future direction. Its displayed MSC list begins with \(30C45\), which places the source in geometric function theory.

The accompanying checker uses outward interval arithmetic from `mpmath.iv`. It certifies the sign of \(F'\) on the two central intervals by adaptive subdivision, positivity of \(F''\) on the root bracket, and high-precision evaluation of the uniquely bracketed critical point. The small endpoint arcs are handled analytically in the proof, not by floating-point extrapolation.

The checker output begins with `VERIFY_OK` and records the certified second-derivative interval
\[
0.7302132125\ldots<F''(t)<0.7302151004\ldots
\]
on the root bracket.

## Relationship to prior work

Sakthivel, Srivastava, and Sivasubramanian introduce \(\xi_q\), its classical limit \(\xi\), and the corresponding convex classes. Their paper gives growth, rotation, distortion, coefficient, Fekete--Szegő, Kruskal, and Toeplitz estimates. The concluding section explicitly identifies geometric properties of the new subclass as a direction for further research. It does not state the sharp order of convexity of \(\mathcal C_\xi\), nor does it minimize \(\operatorname{Re}\xi\) on the disk.

The classical Ma--Minda framework explains why minimizing the real part of a target function yields the order of convexity of its subordinate class, but it does not supply the nontrivial minimization for this particular sine-over-pole target.

Searches using the exact target \(1+\sin z/(1-z)\), the class notation, “convex of order,” “order of convexity,” and the source title returned the source paper and general geometric-function literature, but no published statement of the constant \(\mu_*\), its critical-point characterization, or an implication-equivalent result.

## Limitations

The exact constant is specified implicitly by a unique transcendental critical point and numerically evaluated to high precision; no elementary closed form is claimed.

The proof determines only the sharp order of convexity of the classical class. The quantum deformation \(\mathcal C_{\xi_q}\) has a different operator and parameter-dependent geometry and is not covered.

The interval checker is used only to certify a one-variable sign pattern after the analytic reduction. The reduction, endpoint control, subordination argument, and sharpness mechanism are proved symbolically.

## References

1. K. Sakthivel, H. M. Srivastava, and S. Sivasubramanian, *Sharp Estimates for q-Convex Functions and the Associated Classical Family*, Axioms 15 (2026), 605, DOI:10.3390/axioms15080605.
2. W. Ma and D. Minda, classical work introducing the subordinate starlike and convex families generated by admissible target functions, as cited in the source article.
