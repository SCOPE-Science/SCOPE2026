# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For the cyclic Thomas flow \(\dot x_i=\sin(x_{i+1})-b x_i\), the origin is globally asymptotically stable exactly for \(b\ge1\); at \(b=1\) the sharp worst-case decay is \(t^{-1/2}\) with sup-norm constant \(\sqrt3\), and for \(0<b<1\) the origin is unstable with nonzero synchronized equilibria.

## C — PASS

The quadratic Lyapunov function gives \(\dot V\le-(b-1)\sum_i x_i^2-\tfrac12\sum_i(|x_i|-|x_{i+1}|)^2\). At \(b=1\), any nonzero equality candidate still makes \(|\sin u|<|u|\) strict, so the derivative is negative definite and global asymptotic stability follows. For the rate, after convergence the Dini derivative of \(M=\|x\|_\infty\) is bounded by \(\sin M-M\); the scalar comparison has \(d(q^{-2})/dt\to1/3\), giving the sharp \(\sqrt3\) envelope, attained on the synchronized line. The subcritical instability and equilibria follow from the invariant scalar equation \(\dot u=\sin u-bu\).

## O — PASS

The closest pre-existing Thomas literature located in this audit treats the strict \(b>1\) stable regime, the pitchfork at \(b=1\), and subsequent bifurcations, but does not close the nonhyperbolic endpoint or give the sharp critical decay. Sorin–Tulchinsky (2024) explicitly labels its Lyapunov argument as the case \(b>1\); its proof uses the strict inequality \(-b\|x\|^2<-\|x\|^2\), which disappears at \(b=1\). A stronger published SCOPE theorem dated 2026-09-21 contains logarithmically refined endpoint asymptotics, but it postdates this 2026-09-20 record and therefore is not priority evidence against this record.

### Equivalent formulations

**Searches:** Thomas cyclic sine system b=1 global stability algebraic decay; Sorin–Tulchinsky 2024 arXiv:2408.09525, section 2.1; Chlouverakis–Sprott 2007 DOI 10.1063/1.2721237

**Evidence:** Sorin–Tulchinsky’s section is explicitly titled the case \(b>1\) and proves global stability using the strict factor \(b>1\); it does not state global attraction at \(b=1\) or a \(t^{-1/2}\) law. The 2007 hyperlabyrinth paper studies high-dimensional routes to chaos and stability changes, not the critical endpoint decay theorem.

**Reasoning:** The located pre-existing statements are adjacent but not equivalent to the audited closed-threshold theorem.
### Broader coverage

**Searches:** Published SCOPE search: Thomas critical damping logarithmic relaxation; SCOPE-20260921-2bd40880d8a8

**Evidence:** A 2026-09-21 SCOPE theorem gives the same closed threshold and a stronger reciprocal-square expansion with a logarithmic correction.

**Reasoning:** This is stronger coverage at audit time but it was published after the audited 2026-09-20 record, so it cannot establish that the earlier record lacked originality when published. It is retained as a subsequent refinement, not priority evidence.
### Exact database or table

**Searches:** Published SCOPE semantic search for Thomas \(b=1\) endpoint stability and critical rate; Web exact-phrase searches for Thomas \(b=1\) global stability and algebraic decay

**Evidence:** No pre-2026-09-20 exact theorem with the endpoint \(b=1\) closure and sharp \(\sqrt3\) envelope was located.

**Reasoning:** The result is an analytic dynamical theorem rather than a table value; searches identify the strict regime and later refinement but no earlier exact endpoint statement.
### Claim versus prior implication

**Searches:** Implication comparison with arXiv:2408.09525 strict-\(b>1\) Lyapunov proof; Implication comparison with pitchfork/stability results in the Thomas literature

**Evidence:** The strict \(b>1\) estimate loses coercivity at \(b=1\), and knowing that a zero eigenvalue occurs at a pitchfork does not imply global attraction at the bifurcation value or its decay rate.

**Reasoning:** The audited endpoint theorem is not mechanically implied by the located prior strict-regime statements.

## V — PASS

Closing a stability threshold at a nonhyperbolic bifurcation parameter and determining the sharp global algebraic envelope are natural dynamical questions. The endpoint requires a strict equality-case analysis and a scalar critical comparison beyond the known \(b>1\) Lyapunov estimate, so the contribution is not a routine restatement of the pitchfork location.

## Source inspections

- **Infinite Bifurcations in Thomas system** — arXiv:2408.09525. Trigger: Recent primary analysis cited for global stability and the first pitchfork Material read: Accessible full-text extract covering the Thomas equations, fixed points, section 2.1 for \(b>1\), its Lyapunov argument, and section 2.2 for \(b<1\). Method: Public full-text web extract Assessment: PARTIAL_COVERAGE. Evidence: The paper proves global stability only for \(b>1\) and then analyzes the subcritical bifurcation; it does not prove the endpoint \(b=1\) global theorem or critical decay.
- **Hyperlabyrinth chaos: From chaotic walks to spatiotemporal chaos** — https://doi.org/10.1063/1.2721237. Trigger: Primary high-dimensional cyclic-ring source Material read: Abstract and accessible introductory/stability description for the \(N\)-dimensional ring. Method: Public abstract/full-text search material Assessment: BACKGROUND_ONLY. Evidence: It studies scaling laws and stability changes with \(N\) and \(b\), not the sharp endpoint relaxation law.
- **Critical damping rigidity and logarithmic relaxation in the Thomas cyclic sine ring** — Published SCOPE record 2026/09/21/thomas-critical-damping-and-logarithmic-relaxation--2bd40880d8a8. Trigger: Highly relevant stronger theorem found in current published SCOPE Material read: Complete RESULT.md at the audited repository snapshot. Method: Repository full-text inspection Assessment: SUBSEQUENT_STRONGER_RESULT. Evidence: It strictly strengthens the critical asymptotics but is dated one day after the audited record, so it is not prior-art evidence against the 2026-09-20 claim.

## Residual risks

- Thomas (1999) and older bifurcation literature were not exhaustively available at theorem level; an earlier endpoint theorem under different language remains a residual priority risk, but the closest inspected 2024 primary treatment still uses only the strict \(b>1\) regime.

## Limitations

- The sharp rate theorem is specific to the unforced cyclic sine ring at the exact threshold \(b=1\).
- No uniform crossover asymptotics as \(b\to1\) are claimed.
- Older Thomas-system literature remains a residual priority risk; the stronger 2026-09-21 SCOPE theorem is subsequent rather than prior art.
