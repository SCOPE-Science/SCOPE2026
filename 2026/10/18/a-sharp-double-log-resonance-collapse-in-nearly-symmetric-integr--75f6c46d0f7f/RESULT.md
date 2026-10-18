# A sharp double-log resonance collapse in nearly symmetric integrable ABC vortices

## Finding

Consider the three-torus ABC vector field
\[
\dot x=A\sin z+C\cos y,\qquad
\dot y=B\sin x+A\cos z,\qquad
\dot z=C\sin y+B\cos x.
\]
On its integrable slice \(A=0\), choose \(C=1\) and \(B=1+\delta\), with \(\delta>0\). The transverse Hamiltonian has invariant closed ovals at every energy \(E\in(\delta,2+\delta)\). Let \(T_\delta(E)\) denote their **physical-time** minimal periods, and put \(\rho_\delta(E)=E T_\delta(E)/(2\pi)\), the axial winding per transverse revolution. Then the global minimum \(\rho_{\min}(\delta)\) over this family is attained in the interior for all sufficiently small \(\delta>0\), and has the sharp *two-scale* singular law
\[
\boxed{\rho_{\min}(\delta)=\frac{\delta}{\pi}\left[2\log\frac1\delta+\log\log\frac1\delta+O(1)\right],\quad \delta\downarrow0.}
\]
The coefficient of the secondary log–log term is exact. The minimizing energies lie asymptotically at the separatrix edge: if \(E_\delta\) is any minimizer, then \(E_\delta/\delta\to1\). Moreover, for every sufficiently small fixed \(\delta>0\), every rational winding number strictly between \(\rho_{\min}(\delta)\) and the central winding \((2+\delta)/\sqrt{1+\delta}\) is attained on at least two distinct invariant tori, each foliated by periodic orbits. The theorem does not claim uniqueness of the minimizing torus.

## Assumptions and scope

All phase coordinates are angles modulo \(2\pi\), and time is the original ABC-flow time. The normalization \(C=1\) loses no essential information because common positive rescaling of the ABC strengths rescales time and leaves \(\rho\) unchanged. We fix \(A=0\), \(B/C=1+\delta\), \(0<\delta\ll1\), and follow only the contractible transverse vortex ovals surrounding the elliptic point. Distinct energy levels give distinct invariant two-tori. No perturbative claim for \(A\ne0\) is made.

## Proof

**1. Exact reduction.** Put \(v=y-\pi/2\). The equations reduce to
\[
\dot x=-\sin v,\quad \dot v=(1+\delta)\sin x,\quad \dot z=H(x,v),\quad H=(1+\delta)\cos x+\cos v.
\]
Thus \(E=H\) is constant, and the energy interval \((\delta,2+\delta)\) describes the regular closed ovals about \((0,0)\). The axial angle advances by exactly \(E T_\delta(E)\) during one oval revolution. For \(u=(2+\delta-E)/(2+2\delta)\) and \(w=(E-\delta)/(2+2\delta)\), separation of the Hamiltonian equations gives the exact complete period quadrature
\[
T_\delta(E)=\frac4{1+\delta}\int_0^{\pi/2}
\frac{d\phi}{\sqrt{(1-u\sin^2\phi)(w+u\sin^2\phi)}}.
\]
At the center, linearization has angular frequency \(\sqrt{1+\delta}\), hence \(\rho_\delta(2+\delta)=(2+\delta)/\sqrt{1+\delta}\). At the lower separatrix edge, \(T_\delta(E)\to\infty\), while \(E\to\delta>0\), so \(\rho_\delta(E)\to\infty\).

**2. Uniform two-end logarithm.** Set \(s=E-\delta\), \(\alpha=1-u=(2\delta+s)/(2+2\delta)\), \(\beta=w=s/(2+2\delta)\). Uniformly as \(\delta\downarrow0\) and \(\delta^3\le s\le s_0\) for a sufficiently small *fixed* \(s_0>0\), the integral has the estimate
\[
T_\delta(\delta+s)=\frac2{1+\delta}
\log\frac{4(1+\delta)^2}{s(s+2\delta)}+O(1).
\tag{1}
\]
Here the remainder is absolute and independent of \(\delta,s\) **on the stated range**. For smaller \(s\), the endpoint logarithm has an anisotropy-dependent coefficient, so the bounded-error estimate is not asserted there. For completeness, split the quadrature at \(\phi=\pi/4\). In the lower half the only singular endpoint is \(\phi=0\): replacing its integrand by \((\phi^2+\beta)^{-1/2}\) leaves a difference whose integral is uniformly bounded for \(s\ge\delta^3\) by standard \(\sin\phi/\phi=1+O(\phi^2)\) and \(\cos\phi=1+O(\phi^2)\) estimates, with coefficients bounded away from zero on this half. Its integral is \(\frac12\log(1/\beta)+O(1)\). The upper half, reflected about \(\pi/2\), similarly contributes \(\frac12\log(1/\alpha)+O(1)\). Multiplication by \(4/(1+\delta)\) yields (1). For \(s_0\) fixed but small, the same bounds hold uniformly by continuity and compactness away from the endpoints. This estimate does not silently replace either of the *two* singular corners by one.

**3. Optimization.** Write \(L=\log(1/\delta)\). For \(s=\delta t\), \(\delta^2\le t\le1\), (1) implies, uniformly,
\[
\frac{(1+\delta)\pi}{\delta}\rho_\delta(\delta+\delta t)
=(1+t)\left[2L-\log(t(t+2))+O(1)\right].
\tag{2}
\]
Since \(t+2\in[2,3]\), the right side is bounded below by
\[
2L+2Lt-\log t-O(1)\ge2L+\log L-O(1),
\]
where the final inequality minimizes \(2Lt-\log t\) on \(t>0\). Conversely \(t=1/(2L)\) in (2) gives the upper bound \(2L+\log L+O(1)\). If \(0<s<\delta^3\), the lower endpoint alone, on a fixed small angular subinterval, bounds the integral below by \(\frac12\log(1/s)-O(1)\) after harmless parameter-uniform coefficients (indeed those coefficients are bounded below by one). Therefore \(E T_\delta(E)\ge(2\delta/(1+\delta))[3L-O(1)]\), strictly larger than the trial \( (2\delta/(1+\delta))[2L+\log L+O(1)]\). Hence the asserted minimum law holds when restricted to \(\delta<E\le2\delta\).

We next exclude energies outside this near-separatrix window. If \(2\delta\le E\le E_0\), where \(E_0>0\) is a fixed sufficiently small constant, (1) with \(s=E-\delta\) gives
\[
E T_\delta(E)\ge \frac{2E}{1+\delta}
\log\frac{4(1+\delta)^2}{E^2-\delta^2}-O(E).
\]
The comparison expression on the right is strictly increasing in \(E\in[2\delta,E_0]\) for small enough \(E_0\), since its derivative equals \(\frac2{1+\delta}[\log(4(1+\delta)^2/(E^2-\delta^2))-2E^2/(E^2-\delta^2)]+O(1)\), whose leading logarithm is uniformly large at such \(E_0\). Its value at \(E=2\delta\) is \(\frac{8\delta}{1+\delta}L+O(\delta)\), whereas the near-separatrix trial has \(E T_\delta(E)=\frac{4\delta}{1+\delta}L+O(\delta\log L)\). On \([E_0,2+\delta)\), \(E T_\delta(E)\) is uniformly bounded below by a fixed positive constant because positive periods have a uniform nonzero bound; again this exceeds the shrinking near-separatrix trial. Thus the infimum is the one found in (2).

Finally, (2) shows that any sequence of minimizers with \(t\ge\varepsilon>0\) would increase its leading term from \(2L\) to at least \(2(1+\varepsilon)L\), contradicting the trial. Hence \(t\to0\) and \(E_\delta/\delta\to1\). The minimizer exists by the divergences at the lower endpoint, continuity, and the higher central value. On either side of any chosen minimizing energy, the continuous winding function runs to \(+\infty\) at the separatrix and to the higher central value at the center. Hence every rational in the stated interval is attained at two distinct energies; rational axial winding makes every orbit on each corresponding torus periodic.

## Verification

The proof uses the *exact* Hamiltonian quadrature, a uniform two-corner integral estimate and a controlled variational bound, not a finite enumeration. For numerical diagnostics, execute `python3 verify_abc.py`. It independently evaluates the separated period by quadrature, verifies the existence of distinct resonant energy levels for a fixed anisotropy, and compares finite-\(\delta\) values to the proven asymptotic scales. The diagnostic does not purport to certify the limit or to exclude unobserved minimizers.

## Relationship to prior work

The classical ABC-flow study by Dombre et al. (1986) derives an exact elliptic-integral formula for the winding of integrable ABC vortices (Appendix A) and discusses rational resonances; neither the formula nor the underlying periodic-torus criterion is new here. Szumiński and Llibre (2026) study periodic orbits and regularity obstructions, particularly perturbations near other integrable parameter regimes. The present narrowly scoped result optimizes the **known** winding function in a **joint singular limit** when the two transverse strengths coalesce, obtaining the explicit sharp two-term logarithm–logarithm law for the *minimum*, rather than another expression for the winding function itself. Derivation from an earlier exact formula is acknowledged; the absence of an earlier matched-asymptotic optimization in the inspected sources is not a uniqueness certificate.

## Limitations

Only \(A=0\) and \(B/C\downarrow1\) are covered; no perturbation persistence or uniqueness/nondegeneracy of a shearless torus is asserted. The theorem concerns the global minimum in one vortex annulus and winding *of the flow*, not Floquet instability. The remainder inside the brackets is bounded but its limiting constant is not computed. Earlier analytic work may contain an implicit or explicit version of the singular optimization, so independent priority review is needed. Independent scientific audit has not been performed.

## References

1. T. Dombre, U. Frisch, J. M. Greene, M. Hénon, A. Mehr and A. M. Soward, *Chaotic streamlines in the ABC flows*, Journal of Fluid Mechanics **167** (1986), 353–391, Appendix A. DOI: 10.1017/S0022112086002859. Accessible full scientific text: https://www.researchgate.net/publication/231891929_Chaotic_streamlines_in_the_ABC_flows
2. W. Szumiński and J. Llibre, *Dynamics, periodic orbits and C^1 non-integrability of the ABC flow*, 2026, arXiv:2609.17449v1, first publicly posted 2026-09-15. https://arxiv.org/abs/2609.17449
