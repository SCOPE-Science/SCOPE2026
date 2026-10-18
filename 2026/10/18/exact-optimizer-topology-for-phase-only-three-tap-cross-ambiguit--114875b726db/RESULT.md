# Exact optimizer topology for phase-only three-tap cross-ambiguity on prime cycles

## Finding
Fix any prime \(p\ge7\). Take \(f,g:\mathbb Z_p\to\mathbb C\) with exact common support \(\{0,1,2\}\) and \(|f_j|=|g_j|=1\) on those three points. Define
\[V_gf(t,k)=\sum_{x\in\mathbb Z_p}f(x)\overline{g(x-t)}\exp(-2\pi i kx/p).\]
Then the **entire attainable support-size spectrum** is
\[\boxed{\{|\operatorname{supp}V_gf|\}=\{5p,5p-1,5p-2\}.}\]
In particular, the sharp phase-only lower bound is \(5p-2\), whereas unconstrained complex amplitudes allow \(5p-4\).

The complete sharp-minimizer set also has explicit topology. Quotient by the two independent global phases and put \(a=f_1/f_0\), \(b=f_2/f_1\), \(c=g_1/g_0\), \(d=g_2/g_1\), all in the unit circle \(\mathbb T\). Set \(\mu_p=\{\exp(2\pi i j/p):0\le j<p\}\) and \(\omega_3=\exp(2\pi i/3)\). The entire minimizer locus in \(\mathbb T^4\) is the disjoint union of exactly
\[\boxed{p^2\text{ copies of }\mathbb T^2\quad\text{and}\quad4p^2\text{ copies of }\mathbb T.}\]
The two-torus family satisfies \(-d/a=\xi\), \(-c/b=\eta\) for arbitrarily prescribed \(\xi,\eta\in\mu_p\), leaving \(a,b\in\mathbb T\) free. Every circle in the second family is obtained by choosing \(z_0,\xi\in\mu_p\), \(\epsilon\in\{1,-1\}\), and which of the two side roots is prescribed \(\xi\), then imposing
\[\frac ac=\frac bd=\frac{\omega_3^\epsilon}{z_0},\qquad\text{either }-\frac da=\xi\text{ or }-\frac cb=\xi.\]
Exactly one side-root condition holds in the circle family. Every parameter choice is realized, and there are no other sharp minimizers.

## Assumptions and scope
Both supports are the same consecutive triple. Nonzero complex coefficients have equal modulus within each signal/window; by separate nonzero scalar normalization take all six coefficient moduli to be one. The quotient removes only the two independent global phases, not translations, modulations or reflections. Arithmetic-progression supports with any invertible common step are equivalent by coordinate relabeling. No claim is made for arbitrary three-point supports, unequal amplitudes or composite cyclic orders.

## Proof
Every nonzero translation row arises from the difference set \(\{-2,-1,0,1,2\}\), with intersection cardinalities \(1,2,3,2,1\). Thus there are five potentially nonzero rows of length \(p\), with no zeros in the two singleton rows. For \(z=\exp(-2\pi ik/p)\), the other three Fourier factors are
\[U_-(z)=f_0\overline{g_1}+f_1\overline{g_2}z,\quad H(z)=f_0\overline{g_0}+f_1\overline{g_1}z+f_2\overline{g_2}z^2,\quad U_+(z)=f_1\overline{g_0}+f_2\overline{g_1}z.\]
Set \(r_-=-d/a\), \(r_+=-c/b\), \(u=a/c\), \(v=b/d\). After dividing by a unimodular scalar, \(H(z)=1+uz+uvz^2\), and its two (complex) roots have modulus one if either lies on \(\mathbb T\), because \(|1/(uv)|=1\). Both cannot belong to \(\mu_p\): two distinct sampled roots \(z_1,z_2\) would require \(|z_1+z_2|=1\), forcing \(z_1/z_2\) to be a primitive third root, impossible in \(\mu_p\) for prime \(p\ge7\). A repeated root would force the middle coefficient to have modulus two, also impossible. Thus the central row has at most one Fourier zero.

If \(H(z_0)=0\) at a sampled root \(z_0\in\mu_p\), the three unit phasors \(1,uz_0,uvz_0^2\) form an equilateral triangle. Hence for exactly one \(\epsilon\in\{1,-1\}\),
\[u=v=\omega_3^\epsilon/z_0.\]
Conversely these identities force a central zero at \(z_0\); it is the unique sampled zero. The two linear rows have one sampled zero each precisely when \(r_-\in\mu_p\) and \(r_+\in\mu_p\), respectively. But \(r_-r_+=1/(uv)=z_0^2/\omega_3^{2\epsilon}\notin\mu_p\) whenever the central row vanishes, so at most one side row can then vanish. Without a central zero, at most the two side rows can vanish. Hence no phase-only pair has more than two Fourier zeros among the five nonzero time rows, proving \(s\ge5p-2\).

Equality occurs in precisely two and only two mutually exclusive cases. **Side-side type:** both \(r_-,r_+\in\mu_p\) (then automatically the central row has no sampled zero). Prescribing \(r_-=\xi\), \(r_+=\eta\) forces \(d=-a\xi\), \(c=-b\eta\), leaving arbitrary \((a,b)\in\mathbb T^2\). The discrete choices \((\xi,\eta)\in\mu_p^2\) give exactly \(p^2\) disjoint two-tori. **Center-side type:** one central and exactly one side zero. Prescribe \(z_0\in\mu_p\), \(\epsilon\in\{\pm1\}\), the side sign and a root \(\xi\in\mu_p\); then \(u=v=\omega_3^\epsilon/z_0\) and the chosen side-root equation constrain three independent phase ratios, leaving exactly one free circle. The other side root is automatically outside \(\mu_p\). Each combination determines a different component, giving \(p\cdot2\cdot2\cdot p=4p^2\) circles. Distinct components cannot meet: their sampled-zero labels are discrete and the central and side-side cases are disjoint closed sets. All coefficient phases are recovered uniquely from their four relative ratios, so the parametrization has no redundant identifications.

Finally all three support sizes occur. With triples \(f=g=(1,1,1)\), the central polynomial \(1+z+z^2\) has no \(p\)-th-root zero and both side roots are \(-1\notin\mu_p\), giving \(5p\). With \(f=(1,1,1)\), \(g=(1,1,-1)\), only one side root lies in \(\mu_p\); the central polynomial \(1+z-z^2\) has no \(p\)-th-root zero (its degree is two, and its value at \(1\) is nonzero), giving \(5p-1\). With \(f=(1,1,1)\), \(g=(1,-1,1)\), both side roots equal \(1\) and the central polynomial \(1-z+z^2\) has roots of order six, not \(p\), giving \(5p-2\). This completes the full classification.

## Verification
Every key phase identity follows by multiplication in the unit circle. The product of side roots is exactly \(1/(uv)\). The central sampled-root criterion comes from the elementary rigidity of three unit complex numbers summing to zero. The component count uses a bijective parameterization with independent global phases removed, not a finite numerical census. Explicit phase choices are checked algebraically; no computational evidence is required for the proof.

## Relationship to prior work
The prime-cyclic STFT uncertainty work of Krahmer, Pfander and Rashkov gives support bounds, while Nicola's work classifies absolute global minimum support. The known unrestricted common-three-point theorem gives minimum \(5p-4\) and four-zero patterns when amplitudes may vary; it does not provide the constrained phase-only sharp value or the full component topology. The three-tap self-ambiguity theorem assumes identical signal and window; here their phases vary independently. This phase-only restriction is natural for constant-envelope radar and Gabor coding, and the two different dimensional families describe all optimal designs.

## Limitations
Only the stated unit-modulus, common-progression, independent-pair class is classified. In particular, the result does not classify arbitrary unequal-amplitude 3+3 pairs, other spatial supports, or quantitative noise stability. An unindexed equivalent phase-only cross-ambiguity theorem remains possible; independent literature review has not been performed.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, first posted 29 April 2022. https://arxiv.org/abs/2204.14176
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first posted 16 November 2006. https://arxiv.org/abs/math/0611493
3. Published finding, *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-rigid-ambiguity-support-spectra-for-primitive-three-tap-c--4fe8e5c0fab7
