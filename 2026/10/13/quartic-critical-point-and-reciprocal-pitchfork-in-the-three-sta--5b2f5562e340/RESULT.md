# Quartic critical point and reciprocal pitchfork in the three-state Potts tree maximizer

## Finding

For the three-state ferromagnetic Potts model on a Cayley tree, Bogachev and Rozikov introduce, for every integer \(k\ge2\), the functions
\[
p_k(v)=v+v^2+\cdots+v^{k-1},
\]
\[
L_1(v;\theta)=(\theta-1)p_k(v)-v^k-1,
\]
and
\[
K_1(v;\theta)=
\frac{(p_k(v)+1)^kL_1(v;\theta)}{(p_k(v)+L_1(v;\theta))^k}.
\]
They show the reciprocal symmetry \(K_1(v;\theta)=K_1(v^-1;\theta)\), identify
\[
\widetilde\theta_1(k)=
\frac{5-k+\sqrt{49k^2+62k+49}}{6(k-1)},
\]
and prove that \(v=1\) changes from a local maximum to a local minimum there.

The critical point is in fact nondegenerate at quartic order for every \(k\ge2\). Put
\[
x=\frac12\log v,
\qquad
t=\theta-1,
\qquad
s=(k-1)t,
\]
and let
\[
s_k^*=\frac{11-7k+\sqrt{49k^2+62k+49}}6,
\qquad
\widetilde\theta_1(k)=1+\frac{s_k^*}{k-1}.
\]
For
\[
F_k(x,t)=\log K_1(e^{2x};1+t),
\]
one has near \(x=0\)
\[
F_k(x,t)=F_k(0,t)+c_2(t)x^2+c_4(t)x^4+O(x^6),
\]
with
\[
c_2(t)=
\frac{k(k-1)Q_k(s)}{6(s-2)(s+k-3)},
\qquad
Q_k(s)=3s^2+(7k-11)s-18k+6.
\]
At \(s=s_k^*\), \(Q_k(s_k^*)=0\), and the quartic coefficient is
\[
c_{4,k}^*=
-\frac{2k(k-1)(k+1)^2R_k(s_k^*)}
{1215(s_k^*-2)^2(s_k^*+k-3)^2},
\]
where
\[
R_k(s)=14k^3s-36k^3-21k^2s+183k^2-21ks+69k+14s-42.
\]
For every \(k\ge2\),
\[
c_{4,k}^*<0.
\]
Hence \(v=1\) is a strict quartic local maximum exactly at \(\theta=\widetilde\theta_1(k)\).

Moreover, define
\[
A_k=
\frac{k(k-1)^2(6s_k^*+7k-11)}
{6(s_k^*-2)(s_k^*+k-3)}>0
\]
and
\[
C_k=
\frac{405(k-1)(s_k^*-2)(s_k^*+k-3)(7k+6s_k^*-11)}
{8(k+1)^2R_k(s_k^*)}>0.
\]
Then there is \(\varepsilon_k>0\) such that, for every
\[
0<\delta=\theta-\widetilde\theta_1(k)<\varepsilon_k,
\]
there are exactly two noncentral critical points of \(K_1(\cdot;\theta)\) in a fixed neighborhood of \(v=1\). They are reciprocal strict local maxima \(v_-(\theta)=v_+(\theta)^{-1}\), the point \(v=1\) is a strict local minimum, and
\[
\log v_+(\theta)=2\sqrt{C_k}\,\sqrt{\delta}+O(\delta^{3/2}).
\]
The logarithmic height gain of either side maximum over the center is
\[
\log\frac{K_1(v_+(\theta);\theta)}{K_1(1;\theta)}
=\frac{A_kC_k}2\,\delta^2+O(\delta^3).
\]
Thus the source's distinguished value \(\widetilde\theta_1(k)\) is a supercritical reciprocal pitchfork of the local maximization geometry for every tree order \(k\ge2\).

## Assumptions and scope

The statement uses the source's three-state case \(q=3\), its \(m=1\) auxiliary function \(K_1\), and integer tree order \(k\ge2\). It is local in \(v\) and local in \(\theta\) about \(\widetilde\theta_1(k)\). The positivity domain is automatic near the critical point because \(s_k^*>18/7>2\), so \(L_1(1;\widetilde\theta_1)>0\).

No claim is made that the two local side maxima are global maximizers when \(k\ge5\). In particular, this result does not prove Conjecture 2.1 of Bogachev--Rozikov, does not determine the complete number of completely homogeneous splitting Gibbs measures for arbitrary \(k\), and does not classify thermodynamic order/disorder transitions.

## Proof

Write \(v=e^{2x}\). The finite geometric sums give
\[
p_k(e^{2x})=e^{kx}\frac{\sinh((k-1)x)}{\sinh x},
\]
\[
p_k(e^{2x})+1=e^{(k-1)x}\frac{\sinh(kx)}{\sinh x},
\]
and
\[
e^{2kx}+1=2e^{kx}\cosh(kx).
\]
Therefore all exponential factors cancel from \(K_1\), and, with
\[
U_m(x)=\frac{\sinh(mx)}{\sinh x},
\]
we obtain
\[
K_1(e^{2x};1+t)=
\frac{U_k(x)^k\left(tU_{k-1}(x)-2\cosh(kx)\right)}
{\left((t+1)U_{k-1}(x)-2\cosh(kx)\right)^k}.
\]
This expression is even in \(x\), which is the reciprocal symmetry in logarithmic coordinates.

The elementary expansion
\[
U_m(x)=m+\frac{m(m^2-1)}6x^2
+\frac{m(3m^4-10m^2+7)}{360}x^4+O(x^6)
\]
inserted into the preceding formula gives the displayed expansion of \(F_k\). Direct collection of the quadratic coefficient yields
\[
c_2(t)=
\frac{k(k-1)\left(3s^2+(7k-11)s-18k+6\right)}
{6(s-2)(s+k-3)}.
\]
The unique positive zero of the numerator is \(s_k^*\), reproducing the source's critical value.

For the quartic term, exact collection gives a rational function whose numerator is a quartic polynomial \(P_k(t)\). The following exact polynomial reduction is useful:
\[
27P_k(t)-8(k+1)^2R_k((k-1)t)
=Q_k((k-1)t)H_k(t),
\]
where \(H_k(t)\) is a polynomial. Hence, at \(t=s_k^*/(k-1)\), the \(Q_k\) term vanishes and the displayed formula for \(c_{4,k}^*\) follows.

It remains to prove the sign without numerical root estimates. Since
\[
Q_k(18/7)=-\frac{120}{49}<0,
\]
and \(Q_k\) has one positive root, \(s_k^*>18/7\). Also
\[
R_k(18/7)=3(43k^2+5k-2)>0
\]
and
\[
\frac{\partial R_k}{\partial s}
=7(k-2)(k+1)(2k-1)\ge0.
\]
Thus \(R_k(s_k^*)>0\) for every \(k\ge2\), proving \(c_{4,k}^*<0\).

Differentiating \(c_2\) at the simple zero gives \(c_2'(t_k^*)=A_k>0\). Because \(F_k\) is even and analytic, divide \(\partial_xF_k\) by \(2x\) and write it as an analytic function of \(y=x^2\) and \(\delta=t-t_k^*\). Its derivative with respect to \(y\) at \((y,\delta)=(0,0)\) is \(2c_{4,k}^*\neq0\). The analytic implicit-function theorem therefore gives a unique nearby branch
\[
y(\delta)=C_k\delta+O(\delta^2),
\qquad
C_k=-\frac{A_k}{2c_{4,k}^*}>0.
\]
For \(\delta>0\), the roots \(x=\pm\sqrt{y(\delta)}\) are the only nonzero nearby critical points. The sign of the second derivative shows they are strict local maxima while \(x=0\) is a strict local minimum. Taking \(v=e^{2x}\) gives the square-root law. Substitution into the normal form gives the stated positive height gain.

## Verification

The accompanying `verify.py` reconstructs the Taylor coefficients symbolically from the hyperbolic formula, verifies the exact identity for \(c_2\), verifies the polynomial reduction used for \(c_4\), factors the two sign certificates
\[
Q_k(18/7)=-120/49,
\qquad
\partial_sR_k=7(k-2)(k+1)(2k-1),
\]
and checks representative numerical values of the critical coefficients for \(2\le k\le40\). A successful replay prints `VERIFY_OK symbolic=1 k_range=2..40`.

The finite numerical loop is only a consistency check. The all-
\(k\) conclusions come from the displayed symbolic identities and sign argument.

## Relationship to prior work

Bogachev and Rozikov define \(L_m\) and \(K_m\), identify \(\widetilde\theta_1(k)\), and calculate the second derivative at \(v=1\). Their Appendix B proves that \(v=1\) becomes a local minimum for \(\theta>\widetilde\theta_1(k)\). For the harder global assertion below the threshold they propose a reciprocal-polynomial monotonicity scheme and carry it out only for \(k=2,3,4\). The inspected manuscript does not compute the fourth-order normal form at the threshold, the all-
\(k\) sign of that coefficient, or the square-root onset amplitude of the reciprocal side extrema.

Lin and Taylor classify symmetry-breaking schemes for the ferromagnetic Potts model on a Bethe lattice without an external field; that zero-field classification does not imply the present local external-field \(K_1\) normal form. Gandolfo, Rahmatullaev, and Rozikov study translation-invariant Gibbs measures and boundary conditions in the zero-field order-two case; it likewise does not contain this threshold expansion.

Targeted searches for the source identifier, the exact critical radical, reciprocal \(K_1\) aliases, fourth-derivative/quartic formulations, and square-root onset formulations did not locate a published statement implying the result. A residual risk remains that an equivalent local bifurcation calculation appears in older Bethe-lattice literature under different coordinates.

## Limitations

This is a local bifurcation theorem for the auxiliary maximization function \(K_1\), not a global phase-diagram theorem. For \(k\ge5\), distant critical points or larger maxima are not excluded. The result therefore cannot be substituted for the source's unresolved global uniqueness statement.

The term “pitchfork” describes the reciprocal local critical-point geometry in \(x=\tfrac12\log v\); it is not a claim about a dynamical-system flow.

## References

1. L. V. Bogachev and U. A. Rozikov, “On the uniqueness of Gibbs measure in the Potts model on a Cayley tree with external field,” arXiv:1903.11440, first public 27 March 2019; *Journal of Statistical Mechanics: Theory and Experiment* 2019, 073205, DOI: 10.1088/1742-5468/ab270b.
2. D. Gandolfo, M. M. Rahmatullaev, and U. A. Rozikov, “Boundary conditions for translation-invariant Gibbs measures of the Potts model on Cayley trees,” arXiv:1504.01265; *Journal of Statistical Physics* 167 (2017), 1164–1179, DOI: 10.1007/s10955-017-1771-5.
3. J.-C. Lin and P. L. Taylor, “Symmetry-breaking schemes for the Potts model on a Bethe lattice,” *Physical Review B* 48 (1993), 7216–7220, DOI: 10.1103/PhysRevB.48.7216.
