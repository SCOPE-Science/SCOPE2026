# Unbounded stable impulse locking at fixed winding with identical circular limit cycles

## Finding
For every integer \(m\geq1\), there are two globally smooth planar autonomous oscillators with exactly the **same parameterized hyperbolically attracting unit-circle orbit** \(\gamma(t)=(\cos t,\sin t)\), period \(2\pi\), and transverse Floquet multiplier \(e^{-2\pi}\), coupled by the **same two fixed nonzero reciprocal Cartesian translation directions and the same fixed positive impulse-strength ratio**, such that for all sufficiently small common impulse strengths the full state-triggered impulsive system has at least \(4m-1\) distinct orbitally attracting one-to-one locked periodic motions and at least \(4m-1\) further locked motions unstable in relative phase. In the winding criterion of Buescu and Oliveira, the effective field has winding zero, the tangent field winding one, and their relative winding is \(-1\) for every \(m\). Thus a fixed, nonzero winding lower bound of one can underestimate stable locking multiplicity by an arbitrarily large factor even when all uncoupled on-cycle trajectories, on-cycle velocities, Floquet contraction factors, impulse directions and impulse ratios are identical.

## Assumptions and scope
Let \(m\geq1\), \(k=4m-1\), and let \(U_j\) denote the Chebyshev polynomial of the second kind, determined by \(U_0=1\), \(U_1(z)=2z\), and \(U_{j+1}(z)=2zU_j(z)-U_{j-1}(z)\). On a sufficiently narrow annulus about the unit circle, use polar coordinates \(r=1+s>0\), \(\theta\in\mathbb R/(2\pi\mathbb Z)\), and set
\[
 g_m(\theta)=4\sin\theta\,U_{m-1}(\cos2\theta)\cos((2m-1)\theta).
\]
Oscillator 1 obeys \(\dot s=-s\), \(\dot\theta=1\). Oscillator 2 obeys
\[
 \dot s=-s,\qquad \dot\theta=\frac{1+s g_m(\theta)}{1+s g_m'(\theta)}.
\]
Choose the annular width small enough that both numerator and denominator stay strictly positive. Extend these annular equations smoothly to the whole Cartesian plane by a radial cutoff, without altering the vector fields on a smaller closed annulus. The impulse received by oscillator 2 when oscillator 1 crosses the positive horizontal radial section is \((x,y)\mapsto(x+\varepsilon,y)\); the impulse received by oscillator 1 when oscillator 2 crosses its positive horizontal radial section is \((x,y)\mapsto(x,y+\varepsilon/2)\). Each section is a sufficiently short radial segment through \((1,0)\), crossed in the positive angular direction. The statement concerns locally continued locked motions for sufficiently small \(\varepsilon>0\), not all global recurrent motions or all emission-convention choices near simultaneous crossings.

## Proof
**1. Shared cycles and exact phases.** Both radial equations satisfy \(\dot s=-s\), hence the circle \(s=0\) is attracting, has period \(2\pi\), and has transverse Floquet multiplier \(e^{-2\pi}\). Both angular equations restrict to \(\dot\theta=1\) on that circle, giving exactly the same on-cycle positions and velocities. Define on the annulus
\[
 \Theta_1(s,\theta)=\theta,\qquad \Theta_2(s,\theta)=\theta+s g_m(\theta)\pmod {2\pi}.
\]
The angular vector field for oscillator 2 was chosen so that
\[
 \dot\Theta_2=(1+s g_m')\frac{1+s g_m}{1+s g_m'}+g_m(-s)=1.
\]
As \(s(t)\to0\), these functions are the genuine asymptotic phases, normalized to \(\theta\) on the cycle. At \(r=1\), using \(e_r=(\cos\theta,\sin\theta)\) and \(e_\theta=(-\sin\theta,\cos\theta)\), their gradients are \(Z_1=e_\theta\) and \(Z_2=e_\theta+g_m e_r\). These equations hold exactly, not only to first order.

**2. Arbitrarily many simple phase-balance zeros with fixed kicks.** The elementary Chebyshev identity \(\sin(2m\theta)=2\sin\theta\cos\theta\,U_{m-1}(\cos2\theta)\), followed by sine addition, yields
\[
 g_m(\theta)\cos\theta=\sin((4m-1)\theta)+\sin\theta.
\]
Therefore, for the fixed kick vectors \(d_2=(1,0)\), \(d_1=(0,1)\) and the fixed ratio \(\eta=1/2\), the on-cycle phase responses are
\[
 h_2(\theta)=Z_2(\theta)\cdot d_2=\sin(k\theta),\qquad
 h_1(\theta)=\eta Z_1(\theta)\cdot d_1=\tfrac12\cos\theta.
\]
The phase balance, using the emission-phase convention of Buescu and Oliveira, is
\[
 H_m(\psi)=h_2(\psi)-h_1(-\psi)
          =\sin(k\psi)-\tfrac12\cos\psi.
\]
In particular \(H_m(0)=-1/2\), so no zero is at simultaneous emission. At the \(2k\) cyclically ordered points \(\psi_j=(j+1/2)\pi/k\), \(j=0,\ldots,2k-1\), the values \(H_m(\psi_j)=(-1)^j-\tfrac12\cos\psi_j\) have strictly alternating signs. Each consecutive open arc, including the wraparound arc, therefore contains a zero. A nonzero trigonometric polynomial of degree \(k\) has at most \(2k\) zeros on a circle counting multiplicities (multiply by \(e^{ik\psi}\) and regard the result as a polynomial in \(e^{i\psi}\) of degree at most \(2k\)). It follows that there is exactly one zero in each arc, all \(2k\) are simple, and exactly \(k\) are downward crossings and \(k\) are upward crossings.

**3. Genuine full-system periodic locking.** The assumptions of Theorem A of Buescu and Oliveira apply: the annular vector fields are smooth, both circles are hyperbolically attracting with transverse multiplier in \((0,1)\), both natural periods equal \(2\pi\), the short radial emission sections are transverse, and the nonzero translations are smooth. Every one of the finitely many simple zeros is strictly inside \((0,2\pi)\), away from simultaneous emission. The theorem therefore continues each to a distinct one-to-one locked periodic motion of the *full state-dependent impulsive system* when \(\varepsilon>0\) is small enough for all \(2k\) continuations simultaneously. At each downward zero the three transverse return multipliers approach \(e^{-2\pi}\), \(e^{-2\pi}\), and \(1+\varepsilon H_m'(\psi_*)+o(\varepsilon)<1\); the resulting periodic orbit is orbitally asymptotically stable. At each upward zero the relative-phase multiplier exceeds one, hence the corresponding locked orbit is unstable in that direction. This establishes at least \(k=4m-1\) of each stability type. We do not infer absence of additional distant periodic motions.

**4. Fixed winding.** On the unit circle, oscillator 2 has \(F_2=e_\theta\). The effective vector field from the winding criterion is
\[
 W_m(\psi)=d_2-\tfrac12\cos\psi\,F_2(\gamma(\psi))
            =(1,0)-\tfrac12\cos\psi\,e_\theta(\psi).
\]
The straight-line homotopy from the constant vector \((1,0)\) to \(W_m\) is everywhere nonvanishing because its deviation from \((1,0)\) has norm at most \(1/2\). Thus \(\operatorname{wind}(W_m)=0\). The tangent \(F_2\) winds once, so the relative winding is \(0-1=-1\), independent of \(m\). The winding lower bound guarantees one attracting lock, whereas the realized number grows without bound.

## Verification
The formulae for \(\Theta_1,\Theta_2\), the explicit phase responses, the root count, the nonvanishing homotopy, and the hypotheses of the full impulsive local-locking theorem constitute the analytic verification. The accompanying standalone checker tests the Chebyshev identity at several angles, brackets all \(2k\) roots for several integer parameters, and confirms their alternating signs and slope types. These finite tests are not a replacement for the all-\(m\) proof, and the theorem invoked for full-impulse continuation is explicitly cited rather than recreated.

## Relationship to prior work
Buescu and Oliveira's 2026 theorem supplies the local continuation and Floquet classification at simple zeros and a lower bound from relative winding, but their full text does not construct a family realizing unbounded multiplicity at one fixed winding under fixed nonzero Cartesian translations and identical circular uncoupled cycles. A previously indexed phase-identifiability result constructs variable *constant* radial phase-gradient components on a fixed cycle; it does not imply the arbitrarily high phase-response harmonics, their trigonometric zero count, or multiple reciprocal locked states. General pulse-coupled phase-response literature studies phase-locking and multistability; the new assertion is specifically the exact realizability of unbounded multiplicity with fixed ratio/directions/on-cycle data and winding in the genuine planar state-triggered system.

## Limitations
The smallness threshold for \(\varepsilon\) may depend on \(m\); there is no claim of a common positive coupling threshold uniform in harmonic order. Only locally continued one-to-one locked states near the product of cycles are counted. No global classification across near-simultaneous emissions is claimed, since the paired-event transition can be discontinuous. The source's local continuation theorem is assumed; its complete independent reproof is outside this result. A general smooth-isochron realization theorem under alternate terminology could establish a broader existence principle, so priority requires further independent checking.

## References
1. Jorge Buescu and Henrique M. Oliveira, *Winding number forces universal synchronisation*, arXiv:2610.15686v1, first public October 11, 2026. In particular Theorems A–C and §§2–4, 7.
2. *Limit-cycle-only phase data do not identify the full phase response curve*, publicly indexed mathematical finding, October 11, 2026, a publicly accessible 2026 result (identification suffix 6ed1f7d91395) (comparison concerning radial asymptotic-phase gradients).
3. C. S. Peskin and other phase-response models are discussed and cited in Reference 1, §1.1; see also *Pulse Coupled Oscillators and the Phase Resetting Curve*, 2010, PMCID: PMC3022482 (earlier phase-response locking criteria).
