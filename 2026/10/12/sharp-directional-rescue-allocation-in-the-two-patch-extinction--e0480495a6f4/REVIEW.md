# Scientific review: sharp directional-rescue allocation

## Correctness — PASS

For the finite continuous-time occupancy model, first-step analysis yields the three exact rational hitting-time formulas in `RESULT.md`. Substituting the fixed directed-rate sum gives a quadratic in the allocation with second derivative \(-2/[ab(a+b+C)]<0\). Its unique constrained maximum is the clipped stationary point, including exact equality and boundary cases. The rational Gauss-Jordan checker independently reproduces all three state-specific absorption times for 576 positive-rate cases, 8,640 initial-weight expectations and 8,640 exact optimum-grid inequalities. The proof is valid for every positive \(a,b,C\), not inferred from those finite checks. No assumptions about metastable limiting distributions enter.

## Originality — PASS, with documented coverage risk

The 2006 Vuilleumier–Possingham article studies directional-colonization viability in 100-patch Monte Carlo landscapes; the available Methods and Results describe common local extinction and finite simulation horizons rather than a two-patch continuous-time hitting-time optimization with prescribed \(x+y=C\). Ross–Pollett's 2009 management rule, read in relevant indexed manuscript sections, optimizes between the aggregate colonization parameter \(c\) and local extinction \(e\), not between two oppositely directed colonization rates. The 2008 Ross–Sirl–Pollett–Possingham study optimizes habitat creation versus protection. The 2001 Etienne–Heesterbeek paper also studies managing extinction/colonization, but only its abstract was available and its possibility of containing a dominating comparison cannot be ruled out. The journal 2010 Ross–Pollett version was not fully accessible. Indexed research searches, model-equivalence queries and prior available results showed no identified statement that entails the full directional and initial-mixture formula; this is evidence for, not proof of, originality. A published but unindexed stronger general allocation theorem remains a substantive risk.

## Value — PASS

The result answers a natural conservation allocation question under fixed total corridor-improvement capacity: how should rescue efforts be split between two directions when patch quality and initial occupancy differ? It yields a globally sharp policy for all positive rates, including explicit interior/boundary thresholds and a surprising occupancy-dependent switch from perfect symmetry to all-one-direction investment. The full quadratic loss identity quantifies the cost of deviation from the optimum. This is a structural decision rule for the smallest genuinely directional patch model, not an arbitrary parameter census or a numerical comparison. The theorem does not validate its assumptions against particular ecosystems, nor does it extend automatically to larger, correlated or density-dependent networks.

## Closest literature and limits

- Vuilleumier and Possingham (2006), DOI `10.1098/rspb.2006.3469`: closely related asymmetric dispersal motivation, different patch count, transition scheme and objective.
- Etienne and Heesterbeek (2001), DOI `10.1086/321986`: especially close stochastic investment setting; full text inaccessible, residual coverage risk retained.
- Ross and Pollett (2009/2010), MODSIM09 and DOI `10.1016/j.ecolmodel.2010.02.016`: aggregate colonization/extinction budget rather than two directed rates; only partial preprint passages and the journal abstract were accessible.
- Ross et al. (2008), DOI `10.1890/07-1094.1`: budget compares habitat protection with habitat creation, not directional rate allocation.

The package does not contain an independent validation, certification, or claim of exhaustive literature uniqueness.

Self-review: passed. Independent audit: not yet performed.
