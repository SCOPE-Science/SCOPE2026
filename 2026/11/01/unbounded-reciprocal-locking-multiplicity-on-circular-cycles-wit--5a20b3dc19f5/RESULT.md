# Unbounded reciprocal locking multiplicity on circular cycles with fixed translations

## Finding
For every odd integer \(m=2q+1\geq1\), every \(0<a<1\), and every prescribed \(\omega,\lambda_1,\lambda_2>0\), there exist two real-analytic planar vector fields on open annuli about the **same unit circle**, each having that circle as an attracting hyperbolic limit cycle with period \(T=2\pi/\omega\) and transverse multiplier \(e^{-\lambda_iT}\). Each oscillator emits once per cycle. Coupling the two systems with the **fixed Cartesian translations** \(K_1^\varepsilon(z)=z+\varepsilon a(0,1)\) and \(K_2^\varepsilon(z)=z+\varepsilon(1,0)\), with the subscript denoting the receiver, produces, for every sufficiently small \(\varepsilon>0\), at least \(m\) distinct orbitally asymptotically stable one-to-one locked motions and at least \(m\) distinct hyperbolic one-to-one locked motions unstable in relative phase (saddles on a three-dimensional Poincaré section).

The complete leading phase balance has **exactly** \(2m\) simple non-simultaneous roots, of which \(m\) are downward and \(m\) upward. Moreover, the source paper's winding-number difference for the effective impulse field equals \(1\) for **every** \(m\), despite the unbounded number of locked motions. Thus that topological lower bound can underestimate locking multiplicity by an arbitrary factor even for circular cycles and constant translations.

## Assumptions and scope
Take \(q\in\mathbb Z_{\geq0}\), \(m=2q+1\), \(0<a<1\), and \(\omega,\lambda_1,\lambda_2>0\). Let \((r_i,\theta_i)\) denote polar coordinates on separate copies of a sufficiently thin annulus \(1-\delta<r_i<1+\delta\) in the plane. The emission section is \(\Sigma_i=\{\Theta_i\equiv0\pmod{2\pi}\}\) restricted to a short radial transverse arc through \((1,0)\); the outward orientation of angular phase distinguishes the recorded crossings. An emission of oscillator \(i\) applies \(K_j^\varepsilon\) to the *other* oscillator \(j\), using the event convention of Buescu and Oliveira [1]. The conclusion is local to neighborhoods of the finitely many nonsimultaneous locking phases and requires \(\varepsilon>0\) sufficiently small depending on the fixed choices; it does not assert global return continuity, an invariant circle for all phases, or a universal coupling threshold uniform in \(m\).

## Proof
**1. An analytic phase profile.** Let \(U_{2q}\) be the Chebyshev polynomial of the second kind, with \(\sin(m\theta)=\sin\theta\,U_{2q}(\cos\theta)\). Set
\[
 b_m(\theta)=(-1)^{q+1}\sin(m\theta),\qquad
 h_m(\theta)=\frac{b_m(\theta)+\sin\theta}{\cos\theta}.
\]
The latter is well-defined by analytic continuation at both zeros of \(\cos\theta\): \(U_{2q}\) is even and \(U_{2q}(0)=(-1)^q\), so \(1+(-1)^{q+1}U_{2q}(x)\) is divisible by \(x^2\). Thus \(h_m(\theta)=\sin\theta\cos\theta\,P_q(\cos\theta)\) for a genuine integer-coefficient polynomial \(P_q\), and \(h_m\) is a real-analytic \(2\pi\)-periodic function. In particular,
\[
 -\sin\theta+h_m(\theta)\cos\theta=b_m(\theta).
\]

**2. Construct the planar oscillators.** On the first annulus put \(\dot r_1=-\lambda_1(r_1-1)\), \(\dot\theta_1=\omega\), and \(\Theta_1=\theta_1\). On the second define
\[
 \Theta_2(r,\theta)=\theta+(r-1)h_m(\theta),\quad
 \dot r_2=-\lambda_2(r_2-1),\quad
 \dot\theta_2=\frac{\omega+\lambda_2(r_2-1)h_m(\theta_2)}{1+(r_2-1)h'_m(\theta_2)}.
\]
Choose \(\delta>0\) sufficiently small that the denominator is positive everywhere on the annulus. These are real-analytic vector fields in Cartesian coordinates on their annuli. Differentiating gives the *exact* identity \(d\Theta_2/dt=\omega\). The radial equations imply convergence to \(r_i=1\), and \(\theta_2-\Theta_2\to0\); hence \(\Theta_i\) are genuine asymptotic phases. Both unit circles have angular velocity \(\omega\), period \(T\), and transverse multipliers \(e^{-\lambda_iT}\), as claimed. Their chosen isochron sections are smooth and crossed transversely exactly once per unperturbed period.

**3. Obtain the phase balance from constant physical kicks.** On the unit circle write \(e_r=(\cos\theta,\sin\theta)\), \(e_\theta=(-\sin\theta,\cos\theta)\). The phase gradients are \(Z_1=e_\theta\) and \(Z_2=e_\theta+h_m e_r\). Therefore the vertical translation into oscillator 1 has phase response \(h_1(\theta)=a\cos\theta\), and the horizontal translation into oscillator 2 has response \(h_2(\theta)=Z_2\cdot(1,0)=-\sin\theta+h_m\cos\theta=b_m(\theta)\). With \(\psi=\Theta_2-\Theta_1\), the reciprocal balance of [1, Definition 2.6] is
\[
 H_m(\psi)=h_2(\psi)-h_1(-\psi)
 =(-1)^{q+1}\sin(m\psi)-a\cos\psi.
\]
In particular \(H_m(0)=-a\ne0\).

**4. Count all simple phase roots.** At the \(2m\) points \(t_j=(\pi/2+j\pi)/m\), \(j=0,\dots,2m-1\), the values \(H_m(t_j)=(-1)^{q+1+j}-a\cos t_j\) have strictly alternating signs because \(a<1\). The \(2m\) intervening open arcs of the circle each contain a zero. But \(H_m\) is a nonzero real trigonometric polynomial of degree \(m\), so it has at most \(2m\) zeros on the circle counted with multiplicity: multiply its Laurent polynomial by \(z^m\) where \(z=e^{i\psi}\), producing an ordinary nonzero polynomial of degree at most \(2m\). Thus there are exactly \(2m\) distinct **simple** zeros, none at \(\psi=0\), and their derivatives alternate in sign: \(m\) negative and \(m\) positive.

**5. Transfer the result to the full impulsive system.** On compact disjoint phase intervals around these roots, crossing order is fixed and both impulses are received away from the receiver's section. The analytic vector fields, hyperbolic limit cycles, transverse sections, and translation diffeomorphisms satisfy all local hypotheses of [1, Theorem A and Corollary 2.9]. At each root this theorem establishes, for every sufficiently small positive \(\varepsilon\), a locally unique hyperbolic one-to-one locked motion with relative-phase return multiplier \(1+\varepsilon H'_m(t_*)+o(\varepsilon)\) and other two return multipliers approaching \(e^{-\lambda_iT}\). Choosing \(\varepsilon\) below the minimum of the finitely many local thresholds gives simultaneously \(m\) attracting and \(m\) phase-unstable saddle motions. Their distinct limiting phases ensure distinct periodic motions.

**6. Why the topological lower bound remains one.** In [1, equation (2.7)] the effective field along oscillator 2 is \(W=e_x-[h_1(-\psi)/\omega]F_2=e_x-a\cos\psi\,e_\theta\). Since \(\|W-e_x\|\le a<1\), its homotopy to the constant unit field never vanishes, so \(\operatorname{wind}(W)=0\). The unit-circle tangent has winding \(1\). Hence the relative winding number \(1-0=1\) does not increase with \(m\), although the actual stable lock count does.

## Verification
The accompanying dependency-free `verify.py` generates \(U_{2q}\) exactly over the integers, checks the polynomial phase-response identity on a finite angular grid for \(m=1,3,5,7,9,11,13,15\), and checks alternating extrema and \(H_m(0)=-a\) at three positive values of \(a<1\). It passed **4,128** finite diagnostics. The analytic Chebyshev factorization, root upper bound and local return theorem—not the finite tests—establish the universal conclusion. The independent return-map theorem is used with explicit hypotheses and is not claimed as a new proof.

## Relationship to prior work
Buescu and Oliveira [1] derive the local phase-balance theorem and a winding lower bound; their three analytic examples address regularity and two-root balances. They explicitly do not assume two roots, but do not supply this high-harmonic constant-translation realization, its exact \(2m\) balance count, or the fixed-winding/unbounded-multiplicity contrast. Their general locking theorem is an essential cited ingredient, not rediscovered here. Canavier and Achuthan [2] discuss multistable pulse locking for abstract phase-response curves and feedback, which is not a realization by reciprocal *constant Cartesian translations* acting on a pair of planar systems with exactly circular cycles and freely prescribed radial multipliers. Pérez-Cervera, M-Seara and Huguet [3] analyze computation and geometry of phase responses rather than this exact construction.

## Limitations
The theorem constructs analytic vector fields only on annuli near the attracting circles; no global extension to the entire plane is asserted. It establishes at least the specified \(2m\) local locks rather than an exhaustive count of all far-from-cycle impulsive motions. It makes no claim of globally continuous return across simultaneous emissions, even though none of the constructed local locks lies there. The allowable coupling magnitude and annulus width may shrink as \(m\) grows. The review is not independent, and historical priority beyond inspected sources remains uncertain.

## References
[1] J. Buescu and H. M. Oliveira, *Winding number forces universal synchronisation*, arXiv:2610.15686v1 (first public 2026-10-11), https://arxiv.org/html/2610.15686v1. In particular Definition 2.6, Theorem A, Corollary 2.9, Theorem B and Section 7.2.

[2] C. C. Canavier and S. Achuthan, *Pulse Coupled Oscillators and the Phase Resetting Curve*, Mathematical Biosciences **226** (2010), 77–96, https://pmc.ncbi.nlm.nih.gov/articles/PMC3022482/.

[3] A. Pérez-Cervera, T. M. Seara and G. Huguet, *A geometric approach to Phase Response Curves and its numerical computation through the parameterization method*, arXiv:1809.07318 (2018), https://arxiv.org/abs/1809.07318.
