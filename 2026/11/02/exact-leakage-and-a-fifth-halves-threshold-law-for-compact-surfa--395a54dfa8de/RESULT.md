# Exact leakage and a fifth-halves threshold law for compact surface Fano modes

## Finding

A compact eigenmode of a semi-infinite tight-binding waveguide array becomes a quantitatively controlled resonance when the two equal couplings to its pendant site are detuned together. Fix an integer \(m\ge1\), take the attachment position \(N=3m+1\), the near-surface hopping \(C>0\), the background hopping \(C_b=hC\), and the two pendant couplings \(V=C(1+\varepsilon)\). All on-site energies are zero and \(\varepsilon\) is real and sufficiently small. For each fixed \(h>1/2\), the outgoing resonance energy near the compact state satisfies

\[
\frac{E_m(\varepsilon)}C=-1-\frac{\varepsilon}{m+1}+\frac{6m^2+6m+1}{4(m+1)^3}\varepsilon^2-i\frac{(2m+1)^2\sqrt{4h^2-1}}{4(m+1)^3}\varepsilon^2+O_{m,h}(\varepsilon^3).
\]

In particular, the *resonance linewidth* defined as \(\Gamma_m=-2\operatorname{Im}E_m\) is

\[
\Gamma_m(\varepsilon)=C\frac{(2m+1)^2\sqrt{4h^2-1}}{2(m+1)^3}\varepsilon^2+O_{m,h}(\varepsilon^3).
\]

The leading coefficient has the large-cavity asymptotic \(2C\sqrt{4h^2-1}/m+O_h(m^{-2})\); this is an asymptotic *of coefficients* and does not assert an error bound uniform in the attachment position.

At the critical background hopping \(h=1/2\), the unperturbed eigenenergy lies at the lower continuum edge. For \(\varepsilon=-t<0\), \(t\downarrow0\), the outgoing pole instead obeys the direction-dependent law

\[
-\operatorname{Im}\frac{E_m(-t)}C=\frac{(2m+1)^2\sqrt2}{4(m+1)^{7/2}}t^{5/2}+o_m(t^{5/2}).
\]

For \(h=1/2\) and small \(\varepsilon>0\), the continuation is a real bound eigenvalue strictly below the continuum, with \(E_m/C=-1-\varepsilon/(m+1)+O_m(\varepsilon^2)\); it has no radiative linewidth. These three assertions together give a precise sharp crossover between interior-band quadratic leakage, threshold fifth-halves leakage, and a bound state outside the continuum.

## Assumptions and scope

Let \(\psi_j\), \(j\ge1\), be chain amplitudes on the Hilbert space \(\ell^2(\mathbb N)\), and let \(\psi_F\) be the additional pendant amplitude. Chain hopping is \(C\) on edges \((j,j+1)\) for \(1\le j\le N+1\), and \(C_b=hC\) on all later edges. The pendant amplitude couples with the same positive hopping \(V\) to both chain sites \(N\) and \(N+1\), forming a single triangular attachment. There is no on-site potential and no other coupling. The incoming-free outgoing condition on the infinite tail defines the resonance as the pole of the meromorphically continued resolvent; on the interior of the tail band, take the retarded boundary value. Fix \(m\) and \(h\) before sending \(\varepsilon\to0\).

At \(\varepsilon=0\), the compact eigenvector at \(E=-C\) is proportional to the chain pattern \((1,-1,0,1,-1,0,\ldots,1,-1,0,\ldots)\) through the attachment, with \(\psi_F=-1\). More precisely, for \(N=3m+1\), the entries through \(j=N\) are \(\psi_j=P_j(-1)\), the entry at \(N+1\) and all later entries vanish, and \(\psi_F=-1\); its squared norm is \(2(m+1)\). For \(h>1/2\) its energy lies inside the propagation band \((-2C_b,2C_b)\); for \(h=1/2\) it is at the lower edge.

## Proof

Divide energies and hoppings by \(C\), so the spectral parameter is \(e=E/C\), the pendant coupling is \(v=1+\varepsilon\), and the background hopping is \(h\). Define \(P_0(e)=0\), \(P_1(e)=1\) and \(P_{j+1}(e)=eP_j(e)-P_{j-1}(e)\). In the undecorated surface segment these are the amplitudes arising from \(\psi_1=1\) and the Dirichlet boundary at zero. The outgoing surface self-energy at the first tail site, after eliminating the semi-infinite constant-hopping background, is

\[
\sigma_h(e)=\frac{e-i\sqrt{4h^2-e^2}}{2h^2}.
\]

The square root has the positive real value inside the propagating band and is continued to the outgoing sheet. Eliminating \(\psi_F\), \(\psi_N\), and \(\psi_{N+1}\) by the three attachment equations yields exactly the secular determinant

\[
F_m(e,\varepsilon)=\bigl(e+v^2\bigr)\bigl((e-\sigma_h(e))P_{N+1}(e)-P_N(e)\bigr)-v^2\bigl(e-\sigma_h(e)+1\bigr)\bigl(P_N(e)+P_{N+1}(e)\bigr).
\]

No denominator singular at the reference compact state was divided out. The recurrence gives the following identities at \(e=-1\):

\[
\begin{aligned}
&P_N=1,\quad P_{N+1}=-1,\\
&P_N'=m,\quad P_{N+1}'=m+1,\\
&P_N''=-3m(m+1),\quad P_{N+1}''=3m(m+1).
\end{aligned}
\]

They follow either by induction on \(m\) in blocks of three or by differentiating \(P_j(e)=U_{j-1}(e/2)\). Direct substitution shows \(F_m(-1,0)=0\) and \(\partial_eF_m(-1,0)=2(m+1)\sigma_h(-1)\neq0\). For each fixed \(h>1/2\), the implicit-function theorem therefore gives exactly one outgoing pole in a sufficiently small neighborhood. Substituting \(e=-1+A\varepsilon+B\varepsilon^2+O(\varepsilon^3)\) in \(F_m=0\) and equating coefficients yields

\[
A=-\frac1{m+1},\qquad B=\frac{m}{2(m+1)^2}-\frac{(2m+1)^2}{2(m+1)^3\sigma_h(-1)}.
\]

The derivative of the self-energy cancels out of the quadratic coefficient. Since

\[
\frac1{\sigma_h(-1)}=\frac{-1+i\sqrt{4h^2-1}}2,
\]

the stated real and imaginary coefficients follow. The sign of the imaginary part is negative, as required for the outgoing decaying resonance. The linewidth and coefficient-wise large-\(m\) asymptotic follow by algebra.

At \(h=1/2\) the local square-root variable \(w=\sqrt{e+1}\) is a natural coordinate on the two-sheeted resolvent surface. The secular determinant is analytic in \((w,\varepsilon)\). The nonzero coefficient of \(e+1\) in the secular equation gives \(e+1=-\varepsilon/(m+1)+O(\varepsilon^2)\). Its analytic-in-energy quadratic correction at the edge is \((6m^2+6m+1)\varepsilon^2/[4(m+1)^3]\), obtained by putting \(1/\sigma=-1/2\) in the displayed formula for \(B\). For \(\varepsilon=-t\), one has \(e+1=t/(m+1)+O(t^2)\) and, on the outgoing side,

\[
\frac1{\sigma_{1/2}(e)}=\frac{e+i\sqrt{1-e^2}}2.
\]

The first imaginary contribution arises from the quadratic coupling correction \(-[(2m+1)^2/(2(m+1)^3)]\varepsilon^2/\sigma_{1/2}(e)\). Using \(\sqrt{1-e^2}=\sqrt{2t/(m+1)}+O(t^{3/2})\) gives the stated negative \(t^{5/2}\) coefficient. Higher-order analytic secular terms do not alter it: their first possible square-root contribution is at order \(t^{7/2}\), and the purely analytic contributions are real. If \(\varepsilon>0\), the local energy lies below \(-1\), the physical exterior-band self-energy is real, and the same nondegenerate secular branch gives a real square-summable eigenstate below the tail spectrum. This proves the direction-dependent classification.

## Verification

The attached standalone `check_fano.py` reproduces the recurrence identities, verifies both formal perturbation coefficients symbolically for six attachment distances, and solves the original outgoing secular equation at 60-digit precision for several \(m\), background hopping strengths, and perturbations. It checks the quadratic and fifth-halves linewidth coefficients and a real below-band pole for positive detuning at threshold. Execute `python check_fano.py` with `sympy` and `mpmath` available. Numerical tests are diagnostic only; the general claims above rest on the algebraic recurrence, exact secular determinant, and local analytic continuation.

## Relationship to prior work

Weimann and collaborators, arXiv:1304.4699 (first publicly posted 17 April 2013), construct compact surface Fano states at periodically selected attachment positions, including the relevant \(N=3m+1\) geometries. Their existence and compactness result is the starting point, not the novelty claimed here. Longhi's single-level Fano–Anderson bound states in the continuum and Molina–Miroshnichenko–Kivshar's surface embedded modes provide nearby, but differently coupled, mechanisms. Flach and collaborators' detangling of flat-band lattices develops broader perturbative language for localized interference states. The assessed contribution is the explicit dependence of the outgoing resonance *linewidth on the attachment distance and tail hopping*, together with a threshold \(5/2\) exponent and a direction-dependent zero-width bound state for the same finite-cavity geometry. The inspected primary papers did not state these coefficients or this threshold classification. Algebraically related results elsewhere in the scattering literature remain a priority risk.

## Limitations

The expansion is local in a common real perturbation of both pendant couplings. It does not address unequal perturbations, disorder, absorption, finite-time evolution, finite chains, or arbitrary attachment lengths. The remainder constants can depend on \(m\) and \(h\); no joint limit in cavity size, detuning and distance to the band edge is asserted. The \(h=1/2\) resonance is interpreted on the outgoing continuation, while the \(\varepsilon>0\) eigenvalue is on the physical sheet. Distinct resonances far from \(e=-1\) are not classified. Literature novelty remains conditional on the inspected sources and is not independent certification.

## References

1. S. Weimann et al., *Compact surface Fano states embedded in the continuum of waveguide arrays*, arXiv:1304.4699 (first posted 2013-04-17).
2. S. Longhi, *Bound states in the continuum in a single-level Fano-Anderson model*, arXiv:quant-ph/0612152 (2006).
3. M. I. Molina, A. E. Miroshnichenko and Y. S. Kivshar, *Surface bound states in the continuum*, arXiv:1110.6472 (2011).
4. S. Flach et al., *Detangling Flat Bands into Fano Lattices*, arXiv:1311.5689 (2013).
