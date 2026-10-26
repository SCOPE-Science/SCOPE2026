# A semicubical cusp in the zero geometry of a four-atom Cauchy wavelet

## Finding
Let \(0<r<1\), \(t>0\), and consider the positive, symmetric four-atom measure
\[
\mu_{r,t}=\delta_{-1}+\delta_1+t\delta_{-r}+t\delta_r.
\]
Its order-one analytic Cauchy-wavelet extension, up to a fixed nonzero scalar factor, is
\[
W_{r,t}(z)=\frac1{(z-1)^2}+\frac1{(z+1)^2}
+t\left(\frac1{(z-r)^2}+\frac1{(z+r)^2}\right),\qquad \operatorname{Im}z>0.
\]
There are always exactly three zeros in the open upper half-plane, counted with analytic multiplicity. Their geometry has a sharp two-parameter phase diagram. Put \(q=r^2\),
\[
B(q)=q^4+76q^3-282q^2+76q+1,\qquad q_c=17-12\sqrt2,\quad r_c=3-2\sqrt2.
\]
If \(0<q<q_c\), set
\[
t_\pm(q)=\frac{B(q)\pm(1-q)(q^2-34q+1)^{3/2}}{16(1+q)^3}.
\]
These are distinct positive numbers. For \(t_-(q)<t<t_+(q)\), all three upper-half-plane zeros are simple and lie on the positive imaginary axis. At either boundary \(t=t_\pm(q)\), there is one simple and one double positive-imaginary-axis zero. Everywhere outside the closed interval, precisely one upper zero is positive imaginary and the other two are simple, off-axis and related by reflection across the imaginary axis.

For \(q>q_c\), the latter one-on-axis/two-off-axis pattern holds for every \(t>0\). At \(q=q_c\), the same holds except at the unique parameter \(t=r_c\), where all three upper zeros coalesce into the unique triple zero
\[
z=i\sqrt{r_c}.
\]
No zero of multiplicity four or more is possible in this family. The exactly determined width of the three-imaginary-zero chamber is
\[
t_+(q)-t_-(q)=\frac{(1-q)(q^2-34q+1)^{3/2}}{8(1+q)^3}
\asymp (q_c-q)^{3/2}\quad(q\uparrow q_c),
\]
so the merger is a semicubical cusp; its radius threshold is exactly \(r_c\).

## Assumptions and scope
The four support locations are the two distinct symmetric pairs \(\{-1,1\}\) and \(\{-r,r\}\). The two outer atoms have equal positive mass, and the two inner atoms have equal positive mass in the ratio \(t\) to either outer mass. Overall positive normalization does not change zeros. The upper half-plane coordinate \(z=x+iy\) has \(y>0\); the kernel above is, up to a nonzero convention-dependent multiplicative factor, the order-one Cauchy wavelet convolution of the atomic measure at location \(x\) and scale \(y\). Only zeros in \(y>0\) are counted. Multiplicity is the local holomorphic order in \(z\), not the order of a real-valued modulus.

## Proof
Write \(w=z^2\) and \(q=r^2\). Pairing the two outer and two inner terms gives the exact rational identity
\[
W_{r,t}(z)=\frac{2P_{q,t}(z^2)}{(z^2-1)^2(z^2-q)^2},\qquad
P_{q,t}(w)=(w+1)(w-q)^2+t(w+q)(w-1)^2.
\]
The nominal poles at \(z=\pm1,\pm r\) do not cancel: \(P_{q,t}(1)=2(1-q)^2>0\) and \(P_{q,t}(q)=2tq(1-q)^2>0\). Also \(P_{q,t}(w)>0\) for every real \(w\ge0\). In particular the rational wavelet has no real zeros and no zero at the origin. Because its numerator is an even degree-six polynomial with real coefficients and no real roots, it has exactly three roots in the open upper half-plane, including multiplicity. Every real root \(w\) of its cubic \(P\) is negative; a negative \(w\) corresponds to one positive-imaginary-axis zero, while a nonreal conjugate pair of \(w\)-roots corresponds to two off-axis upper zeros reflected across the imaginary axis.

Direct expansion of the cubic discriminant yields
\[
\operatorname{Disc}_{w}P_{q,t}=t(1-q)^2H(q,t),\quad
H(q,t)=-8(1+q)^3t^2+B(q)t-8q(1+q)^3.
\]
The discriminant of this *quadratic* in \(t\) is
\[
\operatorname{Disc}_{t}H=(1-q)^2(q^2-34q+1)^3.
\]
The unique zero of \(q^2-34q+1\) in \((0,1)\) is \(q_c=17-12\sqrt2\). For \(0<q<q_c\), the identity
\[
B(q)=(1+q)^4+72q(q^2-4q+1)
\]
shows \(B(q)>0\): indeed \(q<q_c<2-\sqrt3\), so \(q^2-4q+1>0\). Hence the two roots of \(H(q,\cdot)\) are exactly the displayed positive numbers \(t_-<t_+\); the leading quadratic coefficient is negative and \(H\) is positive exactly between them. For \(q>q_c\), the quadratic discriminant is negative, and \(H(q,t)<0\) everywhere. The sign of the real cubic discriminant is positive for three distinct real roots, negative for a real root and a nonreal conjugate pair, and zero for repeated roots. Since all real roots are negative, these signs give every asserted open phase.

On \(0<q<q_c\), \(t=t_\pm\) is a *simple* zero of \(\operatorname{Disc}_wP\) as a function of \(t\). A cubic with a triple root has zero differential of its discriminant with respect to every coefficient, so such a simple crossing cannot have a triple root. Its repeated root therefore has order exactly two and is negative; the remaining simple real root is also negative. At \(q=q_c\), the only quadratic-discriminant boundary parameter is \(t=r_c\). Here the exact identity
\[
P_{q_c,r_c}(w)=(1+r_c)(w+r_c)^3
\]
proves the triple root. The map \(z\mapsto z^2\) has nonzero derivative at \(z=i\sqrt{r_c}\), so this is a genuine order-three zero in \(z\). The degree bound excludes higher multiplicity. At all other parameters the discriminant is nonzero and all three upper zeros are simple.

Finally, subtraction of the two explicit roots of \(H\) gives the width formula. As \(q\uparrow q_c\),
\[
q^2-34q+1=(24\sqrt2)(q_c-q)+O((q_c-q)^2),
\]
whence
\[
t_+(q)-t_-(q)\sim
\frac{(1-q_c)(24\sqrt2)^{3/2}}{8(1+q_c)^3}(q_c-q)^{3/2}.
\]
The cusp is nondegenerate: the Jacobian of \((P,P_w)\) with respect to \((q,t)\) at the triple point \((q_c,r_c,w=-r_c)\) is exactly \(12672-8960\sqrt2>0\), while \(P_{www}=6(1+r_c)>0\). Thus the two physical parameters locally unfold the triple root in both independent directions.

## Verification
The standalone checker `check.py` uses exact symbolic polynomial arithmetic to recompute the cubic discriminant, the discriminant of its coefficient quadratic, the cusp factorization, the nonzero transversality Jacobian, and the multiplicity-three derivative test. It verifies the rational wavelet identity at two exact parameter choices; numerical root diagnostics at four representative interior/exterior settings supplement the analytical sign classification. The checker confirms a double, but not triple, cubic root at both boundaries for the exact rational test \(q=1/100\). Run `python check.py` with Python 3, SymPy and NumPy. The reproduced expected console output is in `check_output.txt`.

## Relationship to prior work
The analytic Cauchy-wavelet framework and its connection to upper-half-plane holomorphic transforms are classical. Mallat and Waldspurger (2014), especially Section 2, study phase retrieval and stability for Cauchy wavelets; their statements do not classify zeros or a two-parameter symmetric four-atom cusp. Bauer (2003), Sections 2–3, gives general representation and univalence results for reciprocal Cauchy transforms, including a finite-variance univalence region; this is not an exact classification of critical-point multiplicities for four symmetric atoms. Abakumov, Baranov and Belov (2013), Introduction and principal localization theorems, study zeros in spaces of Cauchy transforms associated with infinite discrete supports; that does not supply the finite four-atom squared-pole discriminant. These are comparisons of their actual statements and objects, not assertions that keyword search alone proves novelty. Earlier finite rational-function classifications may exist and remain a priority risk.

## Limitations
The phase diagram uses positive weights symmetric within each shell and two strictly separated symmetric pairs. It is not a classification of arbitrary four-atom configurations or higher-order Cauchy wavelets. The global count here is finite and purely holomorphic, not a phase-retrieval uniqueness statement for general signals. The 3/2 cusp is an exact local parameter-width law, not a claim about robustness to noisy data. No independent external validation has been performed.

## References
1. R. O. Bauer, *Chordal Loewner families and univalent Cauchy transforms*, arXiv:math/0306130 (first posted 2003-06-07), Sections 2–3.
2. S. Mallat and I. Waldspurger, *Phase retrieval for the Cauchy wavelet transform*, arXiv:1404.1183 (first posted 2014-04-04), Section 2.
3. E. Abakumov, A. Baranov and Y. Belov, *Localization of zeros for Cauchy transforms*, arXiv:1312.6706 (first posted 2013-12-23), Introduction and main results.
