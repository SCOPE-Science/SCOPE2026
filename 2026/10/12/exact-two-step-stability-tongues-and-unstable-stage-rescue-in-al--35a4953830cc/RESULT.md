# Exact two-step stability tongues and unstable-stage rescue in alternating Verlet

## Finding
For the harmonic oscillator \(q''+\omega^2q=0\), \(\omega>0\), apply the standard kick-drift-kick (velocity) Störmer–Verlet integrator with indefinitely alternating positive steps \(H,h\). Write \(x=\omega H>0\), \(y=\omega h>0\) and let \(F\) be the real two-step phase-space transfer matrix. Its trace and determinant are exactly
\[
\operatorname{tr}F=2+\frac{(x+y)^2(xy-4)}4,
\qquad \operatorname{tr}F+2=\frac{(x^2+xy-4)(y^2+xy-4)}4,\qquad \det F=1.
\]
**Complete classification:** the alternating recurrence is power-bounded for every initial phase-space vector if and only if either
\[
xy<4\quad\text{and}\quad(x(x+y)-4)(y(x+y)-4)>0,
\]
or \(x=y=\sqrt2\). All other positive pairs give an unbounded solution. In particular, unequal individually stable steps can be jointly unstable, whereas an individually unstable step can be made jointly stable by alternation. The parabolic boundary contains exactly one power-bounded point, \((\sqrt2,\sqrt2)\).

## Assumptions and scope
With physical state \((q,p)=(q,q')\), one velocity-Verlet step of length \(s\) consists of \(p_{1/2}=p-\omega^2sq/2\), \(q_{\rm new}=q+sp_{1/2}\), and \(p_{\rm new}=p_{1/2}-\omega^2s q_{\rm new}/2\). Conjugate by the fixed rescaling \((q,p)\mapsto(q,p/\omega)\) to use nondimensional steps \(x=\omega H\), \(y=\omega h\). A two-step cycle means the fixed product of two such updates, repeated indefinitely; switching its starting phase conjugates the products and does not affect their eigenvalues or boundedness. Stability means all homogeneous iterates stay bounded for every starting state, not merely that the one-cycle multipliers have modulus at most one. A nontrivial Jordan block on the unit circle is unstable in this sense.

## Proof
**One-step map.** In the nondimensional coordinates the map is
\[
M(s)=\begin{pmatrix}1-s^2/2&s\\-s(1-s^2/4)&1-s^2/2\end{pmatrix},\qquad \det M(s)=1.
\]
Put \(F=M(y)M(x)\). Direct matrix multiplication and factorization yield
\[
\operatorname{tr}F=\frac{x^3y+2x^2y^2+xy^3-4x^2-8xy-4y^2+8}{4},
\]
\[
\operatorname{tr}F-2=\frac{(x+y)^2(xy-4)}4,
\quad\operatorname{tr}F+2=\frac{(x(x+y)-4)(y(x+y)-4)}4.
\]
Thus \(|\operatorname{tr}F|<2\) holds exactly when \(xy<4\) and the product of the latter two factors is positive. A real two-by-two matrix with determinant one and trace strictly between \(-2\) and \(2\) has distinct complex-conjugate unit multipliers, so its powers are bounded. If \(|\operatorname{tr}F|>2\), one real multiplier has modulus greater than one, giving exponential growth for some initial vector.

**Parabolic boundaries.** If \(\operatorname{tr}F=2\), then \(xy=4\), while the upper-right entry is \(F_{12}=(x+y)(1-xy/2)=-(x+y)\ne0\). Hence \(F\ne I\), its repeated eigenvalue \(1\) has a nontrivial Jordan block, and the powers are unbounded. If \(\operatorname{tr}F=-2\), power-boundedness requires \(F=-I\). Since \(F=-I\) is equivalent to \(M(y)=-M(x)^{-1}\), comparing their upper-right entries forces \(y=x\); then comparing diagonal entries gives \(x^2=2\). Conversely \(x=y=\sqrt2\) gives \(\operatorname{tr}M(x)=0\), \(\det M(x)=1\), so the Cayley–Hamilton identity gives \(F=M(x)^2=-I\). Every other parabolic point has a nontrivial Jordan block and grows linearly. This proves the classification, including its boundaries.

**Two opposite effects.** With \((x,y)=(6/5,8/5)\), both one-step maps satisfy \(0<x,y<2\) and are individually power-bounded, yet \(\operatorname{tr}F=-1298/625<-2\); the alternating product grows exponentially. With \((x,y)=(3,6/5)\), the step of size \(x=3\) is individually hyperbolic, yet \(\operatorname{tr}F=59/250\in(-2,2)\), so the repeated alternating product is bounded. More generally, for any fixed contrast \(r=x/y>1\), writing \(S=x+y\), the parametric-instability tongue inside the individually stable region is characterized by
\[
\frac{4(1+r)}r<S^2<4(1+r),\qquad \frac{rS}{1+r}<2.
\]
This interval is nonempty for every \(r>1\): its lower endpoint lies below both upper bounds. Near equal steps the tongue closes at \(S=2\sqrt2\), explaining why any nonzero contrast creates instability at a suitable oscillator-scaled mean step.

## Verification
The standard-library exact checker `verify.py` independently multiplies the rational two-by-two Verlet matrices, tests the trace and determinant factorization identities on exact rational parameter pairs, checks the parabolic upper-right obstruction, and tests a collection of rational pairs on both sides of the stability tongue. It also tests the two displayed rational witnesses and their exact traces. Run `python3 verify.py`. The universal statements follow from the displayed matrix identities and elementary two-dimensional spectral classification, not from the sampled parameter pairs.

## Relationship to prior work
Skeel's 1993 study established that varying a timestep can destabilize Störmer/leapfrog/Verlet integration; Richardson and Finn (2011, arXiv:1108.0322v1) give a detailed modified-equation explanation of parametric resonances for smooth periodic timestep modulation. The present statement isolates the exact global two-parameter period-two stability classification for *velocity Verlet*, including both parabolic boundaries, the unique bounded parabolic exception, and explicit counterintuitive rescue of an unstable one-step map by an alternating product. A qualitative instability warning is weaker than this complete bidirectional classification. The original Skeel article remained inaccessible in complete text; historical equivalence risk is recorded rather than treating abstracts as proof of noncoverage.

## Limitations
Only the linear scalar harmonic oscillator and strictly alternating prescribed physical timesteps are covered. This theorem does not establish nonlinear long-time stability, energy conservation of varying-step orbits, robustness to perturbing the alternation, convergence for arbitrary adaptive controllers, or stability for higher-dimensional coupled oscillators outside independent normal-mode reduction. An exactly parabolic but nondiagonalizable map is deliberately classified as unstable. Qualitative variable-step resonance is known; the new assessment concerns only the exact two-parameter formula and full boundary/dual-regime classification.

## References
1. A. S. Richardson and J. M. Finn, *Symplectic integrators with adaptive time steps*, arXiv:1108.0322v1, first public 2011-08-01, https://arxiv.org/abs/1108.0322 . See §2 and references.
2. R. D. Skeel, *Variable step size destabilizes the Störmer/leapfrog/Verlet method*, BIT Numerical Mathematics 33 (1993), 172–175, https://doi.org/10.1007/BF01990352 . Full text could not be inspected.
3. R. D. Skeel and C. W. Gear, *Does variable step size ruin a symplectic integrator?*, Physica D 60 (1992), 311–313, https://doi.org/10.1016/0167-2789(92)90247-K .
