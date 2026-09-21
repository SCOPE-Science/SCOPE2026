# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** With \(w=y+iz\),
\[
\dot w=((x-1)+ibx)w,
\]
so \(\dot R/R=2(x-1)\) and \(\dot\theta=bx\) on \(R>0\). Subtracting \(b/2\) times the logarithmic radial equation from the phase equation gives the claimed phase-amplitude invariant exactly.

For autonomous \(F>1\), direct differentiation of
\[
L=\frac12s^2+\frac12(R-c-c\log(R/c))
\]
gives \(\dot L=-as^2\). Properness on \(R>0\) and LaSalle's principle reduce the largest invariant zero-dissipation set to \((s,R)=(0,c)\). The phase function then satisfies \(\dot\Phi=b\) everywhere in the basin, so the isochron formula follows from global attraction to the cycle.

At \(F=1\), \(W=(s^2+R)/2\) satisfies \(\dot W=-as^2\) and its largest invariant zero-dissipation set is the origin of the reduced system. Every off-axis trajectory has \(s<0\) eventually. Writing \(h=-s\), \(p=h/R\) gives
\[
\dot p+(a-2h)p=1.
\]
Since \(h\to0\), comparison and variation of constants give \(p\to1/a\). The identity \((1/R)'=2p\) then yields \(tR\to a/2\), and \(t(x-1)\to-1/2\). Substitution into the exact phase law gives the logarithmic phase limit.

The edge cases were checked explicitly: \(b=0\) makes the phase law trivial and removes the nonzero-frequency cycle interpretation; \(R=0\) keeps phase undefined and is treated separately; the cycle radius tends to zero consistently as \(F\downarrow1\).

## Originality

**PASS, to the best of our knowledge.** Lorenz (1984) introduced the model. Shil'nikov--Nicolis--Nicolis (1995) studies its global bifurcation organization. Broer--Simó--Vitolo (2002) is the closest primary source: it explicitly introduces \(u=x-1\), \(r=y^2+z^2\), derives the two-dimensional \(G=0\) reduction, and proves the autonomous \(F>1\) reduced equilibrium is globally attracting.

The 2002 paper then prints, in its equation (10), a full-state reconstruction using \(r(t)\) itself as Cartesian amplitude together with a constant angular law. Read with its immediately preceding definition \(r=y^2+z^2\), that printed formula is not an identity for the stated Lorenz-84 ODE. Direct complex-coordinate reconstruction gives the logarithmic amplitude correction in RESULT.md. The corrected formula still yields parameter-independent phase advance of a periodic reduced orbit.

Searches through later Lorenz-84 stability, nonautonomous-attractor, bifurcation, isochron, asymptotic-phase and critical-slowing literature did not locate the exact global phase law, the closed-form global isochrons, or the sharp \(F=1\) amplitude and logarithmic phase asymptotic.

Residual priority risk is nonzero because the phase identity is short once \(y+iz\) is introduced. K. Homan's 1998 master's thesis and the 1992 paper of Masoller--Sicardi Schifino--Romanelli were not fully inspected. The 1995 Shil'nikov--Nicolis--Nicolis article was inspected at the model and bifurcation level, but the scan is not fully text-searchable. The originality claim is therefore deliberately limited to the exact theorem package and stated as to the best of our knowledge.

## Value

**PASS.** The result upgrades a known symmetry reduction into full-state phase geometry. It gives a closed global isochron coordinate on the entire off-axis basin of the symmetric supercritical cycle, corrects the printed reconstruction attached to a standard Lorenz-84 reference, and resolves the threshold approach with exact leading constants. The phase reconstruction also applies to arbitrary time-dependent symmetric forcing.

## Scientific limitations

The results require \(G=0\). The global isochron foliation is stated only for constant \(F>1\); the critical asymptotic only for constant \(F=1\). The invariant axis has no eddy phase and is treated separately. No conclusion is drawn for the \(G\ne0\) chaotic regimes. The literature search is not exhaustive, and older theses or less-indexed studies may contain an equivalent phase identity or part of the critical asymptotics.
