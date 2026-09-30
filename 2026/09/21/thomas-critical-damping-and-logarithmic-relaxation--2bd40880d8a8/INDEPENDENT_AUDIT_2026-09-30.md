# Independent audit — 2026-09-30

**Record:** `2026/09/21/thomas-critical-damping-and-logarithmic-relaxation--2bd40880d8a8`  
**Audited repository:** `SCOPE-Science/SCOPE2026`  
**Audited current commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree SHA:** `dba073fdfd6294080e9dc8438c528a257ec4d427`  
**Disposition:** passed

The assignment snapshot remains current for this record: comparison from the dispatcher's source-tree-checked commit to current `main` showed no changed file under the assigned record path. The dated independent-audit targets were separately verified absent, and the current `VERIFICATION.md` blob guard was verified before staging this change-set.

## Correctness — PASS

PASS. The Lyapunov estimate is valid for every N>=3: V'<=-(b-1)||x||_2^2-(1/2)sum_i(|x_i|-|x_{i+1}|)^2, and at b=1 the sine inequality is strict at every nonzero state, so the origin is globally asymptotically stable. The common-mode eigenvalue 1-b proves instability for b<1. At b=1 the diagonal is an exact one-dimensional center manifold, while all transverse eigenvalues exp(2*pi*i*k/N)-1 have negative real part. The strong-stable foliation therefore gives exponential synchronization off the codimension-one strong-stable set. For the scalar diagonal equation u'=sin(u)-u, setting w=u^-2 gives w'=1/3-1/(60w)+O(w^-2). Since w~t/3, one bootstrap yields w=t/3-(1/20)log t+C+o(1). An independent symbolic expansion reproduced 1/3-u^2/60+u^4/2520-u^6/181440+..., and the exponentially small transverse error changes 1/x_i^2 by o(1), so every coordinate shares the same constant C.

## Originality — PASS

PASS with an explicit inaccessible-source limitation. The accessible 2007 hyperlabyrinth literature treats the higher-dimensional cyclic ring, its pitchfork and later bifurcations. The open 2024 Thomas-system preprint proves the strict b>1 Lyapunov regime and then treats b<1 bifurcation behavior; it does not supply the critical b=1 global endpoint theorem or the reciprocal-square logarithmic relaxation law. Targeted searches did not locate the coefficient -1/20 or an equivalent sharp critical asymptotic. The original Thomas (1999) paper was pursued after open-access routes failed, but authorized institutional retrieval stopped at a human-verification barrier; those pages were not read. This leaves a historical-priority risk, but it is not decisive for the specific all-N endpoint-plus-logarithmic theorem, which is not present in the accessible later literature inspected.

## Scientific value — PASS

PASS. The theorem closes the damping threshold at its nonhyperbolic endpoint and gives a sharp generic-versus-strong-stable relaxation dichotomy, including a universal logarithmic correction. That is analytically stronger than locating the pitchfork or reporting numerical bifurcations, and it supplies a precise benchmark for critical simulations.

## Independent checks

- Re-derived the global Lyapunov inequality and checked strictness at b=1.
- Recomputed the cyclic-shift spectrum and center/transverse splitting for arbitrary N>=3.
- Independently expanded -2(sin u-u)/u^3 symbolically through u^6 and recovered the stated logarithmic coefficient.
- Checked that an O(e^{-eta t}) transverse error produces an o(1) error in reciprocal squares because |u(t)| is asymptotic to sqrt(3/t).
- Attempted authorized retrieval of Thomas (1999) after OA failure; the job required human verification, so the inaccessible paper was not claimed as read.

## Literature evidence

- https://doi.org/10.1142/S0218127499001383 — Thomas (1999), original model; full text remained inaccessible in this run after human-verification barrier.
- https://doi.org/10.1142/S0218127407018245 — Sprott and Chlouverakis (2007), labyrinth-chaos analysis.
- https://doi.org/10.1063/1.2721237 — Chlouverakis and Sprott (2007), higher-dimensional hyperlabyrinth ring.
- https://arxiv.org/abs/2408.09525 — Sorin and Tulchinsky (2024), accessible Thomas-system analysis; strict b>1 Lyapunov regime and b<1 bifurcations.

## Access notes

- Oxford job b217497f3e660cce4b5842bd2c1719e3 reached needs_human; no inaccessible content was treated as read.

## Limitations

- The sharp asymptotic is specific to the unforced sine ring at exactly b=1.
- The global strong-stable-manifold statement uses standard invariant-manifold/foliation theory in addition to the model-specific calculation.
- Thomas (1999) could not be inspected in full because authorized retrieval required human verification; no claim is made about inaccessible pages.

No GitHub write was performed by the audit chat. This file is staged only by the guarded `scope-audit-change-set-v1` publication plan.
