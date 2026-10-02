# Independent audit review — 2026-10-01

## Final claim

For the cyclic Thomas flow \(\dot x_i=\sin(x_{i+1})-b x_i\), the origin is globally asymptotically stable exactly for \(b\ge1\); at \(b=1\) the sharp worst-case decay is \(t^{-1/2}\) with sup-norm constant \(\sqrt3\), and for \(0<b<1\) the origin is unstable with nonzero synchronized equilibria.

## Correctness — PASS

The quadratic Lyapunov function gives \(\dot V\le-(b-1)\sum_i x_i^2-\tfrac12\sum_i(|x_i|-|x_{i+1}|)^2\). At \(b=1\), any nonzero equality candidate still makes \(|\sin u|<|u|\) strict, so the derivative is negative definite and global asymptotic stability follows. For the rate, after convergence the Dini derivative of \(M=\|x\|_\infty\) is bounded by \(\sin M-M\); the scalar comparison has \(d(q^{-2})/dt\to1/3\), giving the sharp \(\sqrt3\) envelope, attained on the synchronized line. The subcritical instability and equilibria follow from the invariant scalar equation \(\dot u=\sin u-bu\).

## Originality — PASS

The closest pre-existing Thomas literature located in this audit treats the strict \(b>1\) stable regime, the pitchfork at \(b=1\), and subsequent bifurcations, but does not close the nonhyperbolic endpoint or give the sharp critical decay. Sorin–Tulchinsky (2024) explicitly labels its Lyapunov argument as the case \(b>1\); its proof uses the strict inequality \(-b\|x\|^2<-\|x\|^2\), which disappears at \(b=1\). A stronger published SCOPE theorem dated 2026-09-21 contains logarithmically refined endpoint asymptotics, but it postdates this 2026-09-20 record and therefore is not priority evidence against this record.

## Value — PASS

Closing a stability threshold at a nonhyperbolic bifurcation parameter and determining the sharp global algebraic envelope are natural dynamical questions. The endpoint requires a strict equality-case analysis and a scalar critical comparison beyond the known \(b>1\) Lyapunov estimate, so the contribution is not a routine restatement of the pitchfork location.

## Source inspections

- **Infinite Bifurcations in Thomas system** (arXiv:2408.09525): PARTIAL_COVERAGE. The paper proves global stability only for \(b>1\) and then analyzes the subcritical bifurcation; it does not prove the endpoint \(b=1\) global theorem or critical decay.
- **Hyperlabyrinth chaos: From chaotic walks to spatiotemporal chaos** (https://doi.org/10.1063/1.2721237): BACKGROUND_ONLY. It studies scaling laws and stability changes with \(N\) and \(b\), not the sharp endpoint relaxation law.
- **Critical damping rigidity and logarithmic relaxation in the Thomas cyclic sine ring** (Published SCOPE record 2026/09/21/thomas-critical-damping-and-logarithmic-relaxation--2bd40880d8a8): SUBSEQUENT_STRONGER_RESULT. It strictly strengthens the critical asymptotics but is dated one day after the audited record, so it is not prior-art evidence against the 2026-09-20 claim.

## Residual risks

- Thomas (1999) and older bifurcation literature were not exhaustively available at theorem level; an earlier endpoint theorem under different language remains a residual priority risk, but the closest inspected 2024 primary treatment still uses only the strict \(b>1\) regime.
