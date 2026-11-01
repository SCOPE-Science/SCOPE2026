# Sharp projective phase packing for three-point normal spectra with two equal weaker moduli

## Finding
For \(0<r\leq 1\) and real phases \(\phi,\psi\), let
\[
T_{r,\phi,\psi}=\operatorname{diag}(1,r e^{i\phi},r e^{i\psi})\quad\text{on }\mathbb C^3.
\]
For a Hilbert-space operator \(T=H+iK\), write
\[
\omega_{\mathrm{Cart},2}(T)^2=\frac1{2\pi}\int_0^{2\pi}\|H\cos t+K\sin t\|^2\,dt.
\]
Set \(a_r=\arcsin(r/2)\) and \(\theta_r=\pi/2-a_r=\arccos(r/2)\). Then the following is the **exact global maximum**, with no symmetry condition on the two variable phases:
\[
\boxed{\max_{\phi,\psi\in\mathbb R}\omega_{\mathrm{Cart},2}(T_{r,\phi,\psi})^2
=\frac12+\frac{2(r^2-1)a_r+r\sqrt{1-r^2/4}(1+r^2/2)}{\pi}.}
\]
Equality holds precisely when the unordered pair of projective phases satisfies
\[
\boxed{\{\phi\bmod\pi,\psi\bmod\pi\}=\{\theta_r\bmod\pi,-\theta_r\bmod\pi\}.}
\]
Thus the optimal phases of the two equal weaker modes lie symmetrically about the dominant mode, but their angle depends sharply on their modulus. At \(r=1\), the three projective eigenphases are equally spaced; as \(r\downarrow0\), the weaker pair converges to the perpendicular projective direction. The gain above the single-mode benchmark has the exact asymptotic expansion
\[
\boxed{\max_{\phi,\psi}\omega_{\mathrm{Cart},2}(T_{r,\phi,\psi})^2-\frac12
=\frac{4r^3}{3\pi}-\frac{r^5}{30\pi}+O(r^7).}
\]
The same formula applies to a bounded normal operator whose set of nonzero spectral values is precisely \(\{c,c r e^{i\phi},c r e^{i\psi}\}\), after division of the squared radius by \(|c|^2\), regardless of spectral multiplicities; an additional zero spectral value is immaterial.

## Assumptions and scope
All Hilbert spaces and operators are complex. The parameter satisfies \(0<r\le 1\); there are exactly three specified nonzero spectral entries, with moduli \(1,r,r\), before optional direct sums and unitary equivalence. The high-modulus spectral phase is fixed to zero by unimodular homogeneity. Phases are projective because the integrand contains squared absolute values of real projections: changing any individual eigenvalue's sign does not affect this radius. The result optimizes over **both independent phase parameters**; it does not optimize arbitrary spectral moduli, four-point configurations, or nonnormal operators. For \(r=1\), the labels of the three equal-modulus eigenvalues may be permuted.

## Proof
**Step 1: Spectral and projective-circle reduction.** The real part of \(e^{-it}T_{r,\phi,\psi}\) is diagonal with entries \(\cos t\), \(r\cos(t-\phi)\), and \(r\cos(t-\psi)\). Since each squared entry is \(\pi\)-periodic,
\[
\omega_{\mathrm{Cart},2}(T_{r,\phi,\psi})^2=\frac1\pi\int_0^\pi\max\{\cos^2t,r^2\cos^2(t-\phi),r^2\cos^2(t-\psi)\}\,dt. \tag{1}
\]

**Step 2: Sharp one-arc integral lemma.** For every measurable set \(E\) on the circle \(\mathbb R/\pi\mathbb Z\), of length \(0\le\ell\le\pi\), and every phase \(\alpha\),
\[
\int_E\cos^2(t-\alpha)\,dt\le \int_{-\ell/2}^{\ell/2}\cos^2t\,dt=\frac{\ell+\sin\ell}{2}.\tag{2}
\]
To prove (2), measure projective distance from \(\alpha\) in \([0,\pi/2]\). The profile \(\cos^2\) decreases strictly with that distance; moving any portion of \(E\) outside the centered arc of length \(\ell\) into an equal-measure unused portion inside cannot decrease the integral. This gives (2) by a measure-preserving layer-cake argument. When \(0<\ell<\pi\), equality forces \(E\), up to null sets, to be that centered arc.

**Step 3: Global upper bound and its unique optimal cell lengths.** Break ties arbitrarily in the maximum in (1) to obtain measurable winner sets \(E_0,E_1,E_2\), with lengths \(\ell_0,\ell_1,\ell_2\) summing to \(\pi\). Applying (2) separately yields
\[
\pi\omega_{\mathrm{Cart},2}(T_{r,\phi,\psi})^2\le\frac12\{\ell_0+\sin\ell_0+r^2(\ell_1+\sin\ell_1+\ell_2+\sin\ell_2)\}.\tag{3}
\]
The function \(\sin x\) is strictly concave on \((0,\pi)\). At fixed \(\ell_0=L\), the right side is maximized uniquely by \(\ell_1=\ell_2=(\pi-L)/2\), whenever \(0<L<\pi\). Consequently the global upper envelope is
\[
G_r(L)=\frac{L+\sin L+r^2\big(\pi-L+2\sin((\pi-L)/2)\big)}{2\pi},\qquad0\le L\le\pi.\tag{4}
\]
Direct differentiation gives
\[
2\pi G_r'(L)=1+\cos L-r^2\big(1+\cos((\pi-L)/2)\big),
\]
\[
2\pi G_r''(L)=-\sin L-\frac{r^2}{2}\sin((\pi-L)/2)<0\quad(0<L<\pi).\tag{5}
\]
Also \(G_r'(0)>0\), \(G_r'(\pi)<0\), so there is a unique maximizing length \(L=L_r\). Put \(s=\sin(L_r/2)\). The critical equation simplifies to \(2(1-s^2)=r^2(1+s)\), hence \(s=1-r^2/2\). With \(a_r=\arcsin(r/2)\), the unique solution is
\[
L_r=\pi-4a_r,\qquad \ell_1=\ell_2=2a_r.\tag{6}
\]
Substitution in (4) gives the stated exact formula, since \(\sin(2a_r)=r\sqrt{1-r^2/4}\) and \(\sin(4a_r)=2r\sqrt{1-r^2/4}(1-r^2/2)\).

**Step 4: Realization of every sharp rearrangement equality.** Choose \(\phi=\theta_r=\pi/2-a_r\) and \(\psi=-\theta_r\), and put \(t_r=\pi/2-2a_r\). Partition the projective circle into the dominant arc \(E_0=[0,t_r]\cup[\pi-t_r,\pi)\), the first weak arc \(E_1=[t_r,\pi/2]\), and the second weak arc \(E_2=[\pi/2,\pi-t_r]\). Their lengths are exactly \(L_r,2a_r,2a_r\); each is centered at its associated spectral phase (modulo \(\pi\)). For \(0\le t\le\pi/2\), the identity
\[
\cos^2(t-\theta_r)-\cos^2(t+\theta_r)=\sin(2t)\sin(2\theta_r)\ge0
\]
shows that the first weak mode dominates the second. Moreover \(\cos t=r\cos(t-\theta_r)\) has its unique solution on this half circle at \(t=t_r\), because \(\tan t=(1-r\cos\theta_r)/(r\sin\theta_r)\) is strictly increasing; the dominant mode wins before that crossing and the weak mode after. The identity \(\cos t_r=\sin(2a_r)=r\cos a_r=r\cos(t_r-\theta_r)\) locates the crossing exactly. Reflection \(t\mapsto\pi-t\) proves the stated winner assignment on the other half. Every inequality in Steps 2 and 3 is therefore attained.

**Step 5: Uniqueness.** Suppose an arbitrary phase pair attains the upper bound. By strict concavity in (5) and of \(\sin\) in (3), the winner-set lengths must be those in (6), all strictly between zero and \(\pi\). Equality in (2) then forces all three winning sets to be single centered arcs. As they partition the projective circle, the strong arc is the unique arc of length \(L_r\) centered at phase \(0\), and the remaining two equal arcs are necessarily its two neighbors. Their centers are \(\pm(L_r+2a_r)/2=\pm(\pi/2-a_r)\), modulo \(\pi\). Interchanging the two weak entries is the only further freedom. This proves the complete equality characterization, including at \(r=1\).

**Step 6: Endpoint expansion.** Taylor series \(\arcsin(r/2)=r/2+r^3/48+3r^5/1280+O(r^7)\) and \(\sqrt{1-r^2/4}=1-r^2/8-r^4/128+O(r^6)\), substituted in the exact formula, yield \(4r^3/(3\pi)-r^5/(30\pi)+O(r^7)\). At \(r=1\), the exact formula reduces to \(1/2+3\sqrt3/(4\pi)\). This completes the proof.

## Verification
The complete all-parameter argument is Steps 1–6. The accompanying standalone `check.py` numerically integrates independent three-point phase configurations, compares the exact predicted optimum to a projective-circle quadrature at the asserted phases, tests the sharp scalar envelope over many cell lengths, and verifies the weak-mode cubic limit. It executes deterministically and contains no external dependencies beyond the Python standard library. Finite checks are supplemental rather than an infinite proof.

## Relationship to prior work
Audeh, Kittaneh, Moradi, and Sahoo introduced this integral numerical radius and proved general norm inequalities; their accessible full text does not provide the fixed-three-modulus global phase optimization or its equality configurations. Earlier quantitative work on two-point normal spectra determines an independent single phase-separation profile; it does not imply the interaction of the two weaker modes or the global three-phase optimizer. The previously established optimal angular placement of equal-modulus unitary eigenvalues gives the special endpoint \(r=1\) only. The new contribution is the full \(0<r<1\) unequal-modulus sharp value, global phase uniqueness, and the cubic onset law.

## Limitations
Publication priority has not been independently established. The statement is only for three nonzero spectral values with two equal smaller moduli (plus optional zero), and for the \(L^2\)-Cartesian radius. No classification for three independently prescribed unequal moduli, larger spectra, nonnormal operators, or other averaging powers is claimed. An earlier general weighted-circle rearrangement theorem could imply this special application even if it does not use the numerical-radius name; this remains a literature priority risk.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radii of Hilbert Space Operators*, arXiv:2610.04844, first submitted 2026-10-04, version 2 dated 2026-10-23, https://arxiv.org/abs/2610.04844; relevant definition (1.1), Theorem 4 and Remark 19.
2. Standard symmetric decreasing rearrangement (bathtub) principle on a circle, proved directly for the needed cosine profile in Step 2.
