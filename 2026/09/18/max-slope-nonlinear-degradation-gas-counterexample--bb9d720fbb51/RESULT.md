# A counterexample to the max-slope nonlinear-degradation GAS conjecture

## Result

Consider the scalar delay differential equation studied by Adimy, Crauste, Ivanov, and Pujo-Menjouet,
\[
x'(t)=-h(x(t))+f(x(t))g(x(t-\tau)),
\]
under their standing assumptions: \(f,g>0\), \(f\) and \(g\) strictly decreasing, \(h(0)=0\), \(h\) strictly increasing and unbounded, and \(f,g,h\in C^1(\mathbb R_+)\).

For the linear degradation law \(h(x)=\mu x\), their Theorem 3.6 gives the sufficient GAS condition
\[
\frac{1-e^{-\mu\tau}}{\mu}\,f(x_*)L_g<1,
\qquad
L_g=\max_{x\in[m,M]}|g'(x)|.
\]
Immediately after the theorem, the paper conjectures that the same statement extends to nonlinear monotone \(h\) after replacing \(\mu\) by
\[
\mu_{\max}:=\max_{x\in[m,M]}h'(x).
\]

That conjecture is false. In fact, there is a one-parameter family satisfying all of the paper's standing assumptions for which the conjectured left-hand side can be made arbitrarily small for every delay, while the positive equilibrium has a fixed finite delay-instability threshold.

## Explicit family

Set
\[
\varepsilon=10^{-2},\qquad
c=e^\varepsilon-1,
\]
and define
\[
f(x)=e^{-\varepsilon x},
\qquad
g(x)=c+\frac{2}{1+e^{4(x-1)}}.
\]
Let
\[
q(u)=
\begin{cases}
(1-u^2)^2,& |u|\le 1,\\
0,& |u|\ge 1,
\end{cases}
\]
and for any \(A\ge100\) put
\[
\delta_A=\frac{1}{10A},
\qquad
h_A(x)=x+A\int_0^x q\!\left(\frac{s-\frac32}{\delta_A}\right)\,ds.
\]
Then \(q\in C^1(\mathbb R)\), so \(h_A\in C^2(\mathbb R_+)\), and
\[
h_A'(x)=1+Aq\!\left(\frac{x-\frac32}{\delta_A}\right)\ge1.
\]
Hence \(h_A\) is strictly increasing, \(h_A(0)=0\), and \(h_A(x)\to\infty\). The functions \(f\) and \(g\) are positive and strictly decreasing.

Because
\[
\int_{-1}^{1}(1-u^2)^2\,du=\frac{16}{15},
\]
the added bump has total area
\[
A\delta_A\frac{16}{15}=\frac{8}{75},
\]
independent of \(A\). Therefore
\[
h_A(x)=x\quad\text{for }x\le\frac32-\delta_A,
\qquad
h_A(x)=x+\frac{8}{75}\quad\text{for }x\ge\frac32+\delta_A.
\]

## The equilibrium and the invariant interval

At \(x=1\),
\[
h_A(1)=1,\qquad
f(1)g(1)=e^{-\varepsilon}e^\varepsilon=1,
\]
so \(x_*=1\). The monotonicity assumptions make this positive equilibrium unique.

Write
\[
F_A(x)=\frac{h_A(x)}{f(x)}=h_A(x)e^{\varepsilon x}.
\]
The source paper defines
\[
M=F_A^{-1}(g(0)),
\qquad
m=F_A^{-1}(g(M)).
\]
For every \(A\ge100\), the bump ends no later than \(1.501\), and
\[
F_A(1.501)
=
\left(1.501+\frac{8}{75}\right)e^{0.01501}
\approx1.6319797566
<
g(0)
\approx1.9740777472.
\]
Thus \(M>1.501\). Since \(M>1\) and \(g\) is strictly decreasing,
\[
g(M)<g(1)=F_A(1),
\]
and since \(F_A\) is strictly increasing, \(m<1\). Consequently \(1\) and the entire narrow bump lie inside \([m,M]\).

The derivative of \(g\) is
\[
g'(x)
=
-\frac{8e^{4(x-1)}}{(1+e^{4(x-1)})^2},
\]
so its global maximum magnitude is attained at \(x=1\):
\[
L_g=2.
\]
Also, because the bump center \(3/2\) belongs to \([m,M]\),
\[
\mu_{\max}
=
\max_{x\in[m,M]}h_A'(x)
=
1+A.
\]

## The conjectured criterion holds for every delay

The proposed nonlinear extension of Theorem 3.6 would test
\[
K_A(\tau)
=
\frac{1-e^{-(1+A)\tau}}{1+A}\,
e^{-\varepsilon}\,2.
\]
For every \(\tau>0\),
\[
K_A(\tau)
<
\frac{2e^{-\varepsilon}}{1+A}.
\]
At \(A=100\), this gives
\[
K_{100}(\tau)<0.0196049473<1
\]
for every positive delay. Moreover,
\[
\sup_{\tau>0}K_A(\tau)\longrightarrow0
\qquad(A\to\infty).
\]
Thus the conjectured sufficient condition can be made arbitrarily strongly satisfied.

## Nevertheless the equilibrium becomes unstable

The source paper linearizes its equation at \(x_*\) as
\[
y'(t)+\mathcal A\,y(t)+\mathcal B\,y(t-\tau)=0,
\]
where
\[
\mathcal A=h'(x_*)-f'(x_*)g(x_*),
\qquad
\mathcal B=-f(x_*)g'(x_*).
\]
For the family above, the bump is disjoint from \(x_*=1\), so these coefficients are independent of \(A\):
\[
\mathcal A=1+\varepsilon=1.01,
\qquad
\mathcal B=2e^{-\varepsilon}\approx1.9800996675.
\]
Hence \(\mathcal B>\mathcal A\). By the exact local-stability criterion stated as Proposition 2.3 in the source paper, the critical delay is
\[
\tau_*=
\frac{\arccos(-\mathcal A/\mathcal B)}
{\sqrt{\mathcal B^2-\mathcal A^2}}
\approx1.2365780223,
\]
and the equilibrium is unstable whenever \(\tau>\tau_*\). In particular, at \(\tau=2\) the equilibrium is linearly unstable, although the conjectured nonlinear-GAS inequality is satisfied with a margin exceeding a factor of fifty.

Linear instability is incompatible with global asymptotic stability. Therefore the proposed replacement
\[
\mu=\max_{[m,M]}h'(x)
\]
does not extend Theorem 3.6 to nonlinear monotone degradation.

## Structural obstruction

The failure is not an isolated numerical accident. The family \(h_A\) leaves \(h_A\) and \(h_A'\) unchanged near the equilibrium and leaves the linearized stability threshold unchanged, while a progressively narrower remote bump makes \(\max h_A'\) arbitrarily large. Because the conjectured quantity places this maximum in the denominator and in \(1-e^{-\mu\tau}\), the remote steepening makes the proposed criterion look increasingly favorable without adding local damping at the equilibrium.

This identifies the obstruction: a maximum slope of \(h\) is not a lower damping rate. Any valid nonlinear analogue based on variational or comparison estimates must control a lower effective damping along the relevant trajectories, rather than treating a remote upper bound on \(h'\) as uniform dissipation. No optimal replacement criterion is claimed here.

## Limitations

This result refutes the literal nonlinear extension proposed immediately after Theorem 3.6. It does not rule out other nonlinear extensions of that theorem under additional hypotheses, nor does it characterize the sharp global-stability region for general \(h\). The construction uses a smooth localized steepening of the degradation law; the instability conclusion is purely analytical and follows already from the source paper's local criterion.

## References

1. M. Adimy, F. Crauste, A. Ivanov, L. Pujo-Menjouet, *Global stability and periodicity in a delay differential model*, Journal of Mathematical Analysis and Applications 561(1), 130555 (2026). https://doi.org/10.1016/j.jmaa.2026.130555
2. A. F. Ivanov, H. Matsunaga, *Global attractivity and periodicity in a delay differential equation of population dynamics*, Journal of Mathematical Analysis and Applications 566(1), 131043 (2027 issue). https://doi.org/10.1016/j.jmaa.2026.131043
