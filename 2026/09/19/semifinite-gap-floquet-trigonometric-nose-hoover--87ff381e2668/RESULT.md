# Semifinite-gap Floquet selection in the trigonometric Nosé–Hoover orbit

## Statement

Consider the trigonometric Nosé–Hoover system
\[
\dot x=\sin y,\qquad
\dot y=-\sin x-a\sin y\sin z,\qquad
\dot z=b(1-2\cos y),
\]
with \(b\neq0\), and its exact periodic orbit
\[
\Gamma(t)=(0,0,z_0-bt)\pmod{2\pi}.
\]
The source paper arXiv:2609.19958v1 writes the normal variational equation along \(\Gamma\) as
\[
\ddot X+a\sin(z_0-bt)\dot X+X=0.
\]
This equation has a hidden spectral form that determines the transverse Floquet stability of \(\Gamma\) exactly.

Set
\[
\tau=\frac{z_0-bt}{2},\qquad \alpha=\frac{a}{2b},\qquad \nu=\frac4{b^2}.
\]
Then \(X\) satisfies
\[
X_{\tau\tau}-4\alpha\sin(2\tau)X_\tau+\nu X=0,
\]
or equivalently the weighted Sturm–Liouville equation
\[
-\frac1{w_\alpha}(w_\alpha X_\tau)_\tau=\nu X,
\qquad
w_\alpha(\tau)=e^{2\alpha\cos2\tau}.
\]
After the periodic gauge
\[
\psi=e^{\alpha\cos2\tau}X,
\]
this becomes the \(s=1\) Whittaker–Hill equation
\[
-\psi''-\left(4\alpha\cos2\tau+2\alpha^2\cos4\tau\right)\psi
=\lambda\psi,
\qquad
\lambda=\frac4{b^2}-2\alpha^2.
\]
Because the gauge is \(\pi\)-periodic, it preserves the Floquet classification. Hence the exact transverse stability criterion is
\[
\boxed{\Gamma\text{ is linearly elliptic iff }\lambda\text{ lies in a spectral band of the }s=1\text{ Whittaker–Hill operator},}
\]
and \(\Gamma\) is transversely hyperbolic iff \(\lambda\) lies in a spectral gap.

The two transverse multipliers \(\mu_\pm\) also obey the exact reciprocity law
\[
\boxed{\mu_+\mu_-=1.}
\]
Indeed, Abel's identity gives
\[
\mu_+\mu_-
=\exp\!\left[-a\int_0^{2\pi/|b|}\sin(z_0-bt)\,dt\right]=1.
\]
Thus the exact central orbit can never be a hyperbolic attracting or repelling periodic orbit: away from parabolic boundaries it is either elliptic or saddle-type hyperbolic.

## Semifinite-gap selection rule

The classical Whittaker–Hill theorem states that for integer \(s=2m+1\), all even spectral gaps except the first \(m\) are closed. Here \(s=1\), so \(m=0\):
\[
\boxed{\text{every even (periodic) spectral gap is closed for all real }\alpha.}
\]
Consequently, weak-coupling instability tongues of \(\Gamma\) cannot emanate from the periodic resonances
\[
\frac{2}{|b|}=2j
\quad\Longleftrightarrow\quad
|b|=\frac1j,
\qquad j=1,2,\dots.
\]
Only anti-periodic resonances
\[
\frac{2}{|b|}=2j+1
\quad\Longleftrightarrow\quad
|b|=\frac{2}{2j+1}
\]
can open local instability tongues. This is an exact parity selection rule inherited from the special \(s=1\) Whittaker–Hill structure, not a generic property of parametrically damped oscillators.

In particular, the source paper's frequently studied value \(b=1/2\) is the fourth-harmonic periodic resonance at \(a=0\). The corresponding even Whittaker–Hill gap is identically closed, so no linear instability tongue emanates from \((a,b)=(0,1/2)\). The \(1{:}4\) island chain observed numerically near this parameter is therefore not the opening of a transverse Floquet gap of the central orbit.

## Principal instability tongue near \(|b|=2\)

For definiteness take \(a\ge0\), \(b>0\); the spectrum is unchanged by the sign symmetries. Put
\[
r=\frac{a}{b},\qquad
A=\frac4{b^2}-\frac{r^2}{2}.
\]
The Hill equation is
\[
\psi''+\left[A+2r\cos2\tau+\frac{r^2}{2}\cos4\tau\right]\psi=0.
\]
Degenerate perturbation theory at the first anti-periodic level gives the two characteristic values
\[
A_\pm=1\pm r-\frac{r^2}{8}+O(r^3).
\]
Solving \(A=A_\pm\) for the physical parameter gives the two boundaries of the principal instability tongue:
\[
\boxed{
b_\pm(a)=2\pm\frac a2-\frac{a^2}{32}+O(a^3).
}
\]
Inside this wedge the orbit is hyperbolic. For detuning \(b-2=O(a)\), its positive transverse Floquet exponent is
\[
\boxed{
\chi(a,b)=\frac14\sqrt{a^2-4(b-2)^2}+O(a^2)
}
\]
within the tongue. At exact resonance \(b=2\), \(\chi=a/4+O(a^2)\).

## The observed \(b=1/2\) transition

Although no instability tongue emanates from \((0,1/2)\), the fixed spectral level can enter an anti-periodic gap at finite coupling. Direct integration of the exact normal variational equation gives the first anti-periodic crossing at
\[
\boxed{a_c=1.590316803016\ldots\qquad (b=1/2),}
\]
where the transverse monodromy trace equals \(-2\). Numerically,
\[
\operatorname{tr}M(1.5,1/2)=-1.3758288953,
\qquad
\operatorname{tr}M(1.6,1/2)=-2.0645532050.
\]
Thus the central orbit changes from elliptic to hyperbolic at a flip-type Floquet boundary very close to the source paper's reported reorganization near \(a\simeq1.6\). This supplies a local linear mechanism for that numerical threshold, but it does not by itself prove that the global onset of chaos is caused solely by this crossing.

## Relation to prior work

The source paper derives the same normal variational equation but converts it to a double-confluent Heun equation for differential-Galois analysis. It does not formulate a Floquet stability problem or identify the real-periodic \(s=1\) Whittaker–Hill structure.

The Whittaker–Hill equation and its semifinite-gap theorem are classical. In particular, Hemery and Veselov summarize the result that for \(s=2m+1\), all even gaps except the first \(m\) are closed, citing Magnus–Winkler and Djakov–Mityagin. Those spectral theorems are prior art and are not claimed here. The contribution is their source-specific identification with the central orbit of arXiv:2609.19958v1 and the resulting exact Floquet criterion, multiplier reciprocity, resonance selection rule, principal-tongue asymptotics, and quantitative explanation of the reported \(a\simeq1.6\) transition.

## Limitations

The exact spectral equivalence concerns the central orbit \(\Gamma=(0,0,z_0-bt)\), not all periodic orbits of the three-dimensional system. Spectral-band membership determines linear transverse stability; it does not establish nonlinear KAM stability, attraction, global basin structure, or chaos. The value \(a_c\) above is a numerical root of the exact monodromy problem rather than a closed-form constant. The small-\(a\) tongue expansion is local near \(|b|=2\). The semifinite-gap theorem closes the even spectral gaps, but it does not prevent the physical parameter curve at finite coupling from entering an open anti-periodic gap, as the \(b=1/2\) example demonstrates.

## Reproducibility

`artifacts/verify_floquet.py` checks the exact Whittaker–Hill parameter identities, derives the principal-tongue coefficients symbolically, integrates the exact transverse variational equation, and locates the \(b=1/2\) anti-periodic crossing. `artifacts/verification_output.txt` records the resulting checks.

## References

1. W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability*, arXiv:2609.19958v1 (2026). https://arxiv.org/abs/2609.19958
2. A. D. Hemery and A. P. Veselov, *Whittaker-Hill equation and semifinite-gap Schrödinger operators*, J. Math. Phys. 51, 072108 (2010); arXiv:0906.1697. https://arxiv.org/abs/0906.1697
3. P. Djakov and B. Mityagin, *Asymptotics of instability zones of the Hill operator with a two term potential*, J. Funct. Anal. 242 (2007), 157–194.
4. W. Magnus and S. Winkler, *Hill's Equation*, Interscience, 1966/1969 editions.
