# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For symmetric Lorenz-84 with \(G=0\), the eddy phase satisfies the exact phase-amplitude law \(\theta(t)-\theta(0)=bt+(b/2)\log(R(t)/R(0))\). In the autonomous case \(F>1\) this yields explicit global isochrons on \(R>0\); at the critical value \(F=1\), every off-axis orbit has \(tR(t)\to a/2\), \(t(x(t)-1)\to-1/2\), and a logarithmic phase lag with the stated coefficient.

## C — PASS

Writing \(w=y+iz\) gives \(\dot w=((x-1)+ibx)w\), hence \(\dot R=2(x-1)R\) and the phase-amplitude identity by direct integration. For constant \(F>1\), the reduced system in \(s=x-1\) and \(R\) has a coercive relative-entropy Lyapunov function whose derivative is \(-as^2\), so on \(R>0\) LaSalle gives global convergence to \((0,a(F-1))\); subtracting the logarithmic amplitude term produces the exact phase coordinate. At \(F=1\), \(W=(s^2+R)/2\) has derivative \(-as^2\); after setting \(h=-s\), the ratio \(p=h/R\) satisfies \(p' +(a-2h)p=1\), giving \(p\to1/a\), then \((1/R)'\to2/a\) and the stated sharp amplitude and phase asymptotics. The invariant axis \(R=0\) is correctly excluded from phase claims.

Residual risk: The theorem is confined to \(G=0\); it does not assert global phase coordinates for asymmetric forcing.

## O — PASS

The full Broer–Simó–Vitolo primary paper was inspected at the reduced-system and reconstruction pages. It defines \(r=y^2+z^2\), proves the autonomous \(F>1\) reduced global attractor, and prints a reconstruction of \(y,z\) in its equation (10); it does not state the audited logarithmic phase-amplitude invariant, global isochrons, or the \(F=1\) sharp algebraic/logarithmic asymptotics. A Resultary search found a distinct earlier Lorenz-84 stationary eddy-memory result, not this phase theorem.

Residual risk: Older Lorenz-84 theses and early papers were not exhaustively inspected, so priority risk remains.

### Equivalent formulations

**Searches:** Resultary: Lorenz-84 symmetric exact phase amplitude isochrons critical F=1 logarithmic spiral; Broer–Simó–Vitolo, Nonlinearity 15 (2002), DOI 10.1088/0951-7715/15/4/312

**Evidence:** Broer et al. reduce \(G=0\) to \(\dot u=-au-r-a+aFf(t)\), \(\dot r=2ur\) with \(r=y^2+z^2\). Their equation (10) gives a direct \(y,z\) reconstruction for a periodic setting, not the exact amplitude-corrected phase invariant or isochron foliation.

**Reasoning:** The primary source contains the same reduced amplitude dynamics but not an equivalent final phase/asymptotic theorem.

### Broader coverage

**Searches:** Broer–Simó–Vitolo full paper, sections 2.3 and autonomous dynamics; Resultary: Lorenz84 eddy memory and small forcing convergence

**Evidence:** Broer et al. prove the reduced equilibrium is the unique global attractor for autonomous \(F>1\). The earlier SCOPE stationary-memory theorem treats a different balance and \(F<1\) small-forcing convergence.

**Reasoning:** Reduced global attraction alone does not supply the global isochrons or threshold asymptotic constants.

### Exact database or table

**Searches:** Resultary semantic search over Lorenz-84 phase/isochron aliases; Primary-paper exact equation inspection

**Evidence:** No exact database/table is relevant; the issue is theorem-level phase geometry.

**Reasoning:** This check is inapplicable as a tabular search; exact equation comparison was performed instead.

### Claim versus prior implication

**Searches:** Broer et al. Proposition 2.4 and equation (10); Earlier stationary eddy-memory result

**Evidence:** The known reduced attraction does not determine the full angular phase because \(\dot\theta=bx\) must be coupled to amplitude. The critical \(F=1\) limit lies outside the prior \(F>1\) attractor statement.

**Reasoning:** The audited theorem requires the extra exact complex-coordinate integration and critical asymptotic analysis; it is not mechanically implied by the inspected prior results.

### Source inspections

- **The Lorenz-84 climate model** (https://doi.org/10.1088/0951-7715/15/4/312): PARTIAL_COVERAGE. Trigger: Closest primary treatment of the same \(G=0\) reduction. Material read: Full PDF pages containing section 2.3, reduced equation (9), reconstruction equation (10), and Proposition 2.4 global attractor proof. Method: Full PDF text plus page-image inspection. Evidence: It supplies the reduced radial system and \(F>1\) global attraction, but not the audited logarithmic phase-amplitude invariant, isochrons, or critical \(F=1\) asymptotics.
- **Stationary eddy-energy law and a small-forcing convergence criterion for Lorenz-84** (published Resultary record dated 2026-09-20): NOT_COVERING. Trigger: Closest earlier published SCOPE hit for Lorenz-84. Material read: Resultary title and summary. Method: Semantic database inspection. Evidence: It concerns stationary eddy-energy memory and a small-forcing \(F<1\) convergence criterion, not phase geometry.

### Residual risks

- Older theses and early Lorenz-84 literature may contain an equivalent phase formula under different notation.

## V — PASS

The exact phase coordinate and critical logarithmic spiral sharpen the qualitative Hopf/reduced-attractor picture of a classic atmospheric model. The result gives explicit global isochrons and leading critical constants rather than a routine local calculation.

Residual risk: The contribution is special to the symmetric \(G=0\) reduction and does not address the generic forced model.

## Overall disposition

**PASSED**
