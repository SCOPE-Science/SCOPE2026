# Self-review

## Correctness — PASS
The proof uses only the printed autonomous flow, logit differentiations, a global upper barrier on cooperation when the pivotal kernel vanishes at full cooperation, and a risk persistence lemma. The exact identity \(\dot w-k\dot v=(\alpha-\beta)(\theta_3+\theta_4)r+\gamma\) yields an exponential cost boundary law because \(r(t)\) cannot approach zero. The additional strict inequality \(bK_{\max}<\alpha\) then makes cooperation's logit uniformly decrease and risk's logit eventually increase. Both witness equilibrium and stability certificates were checked symbolically with `verification/check.py`. Remaining limit: equality and boundary initial data are excluded.

## Originality — PASS, with residual risk
The main primary paper (2026, DOI 10.1371/journal.pcbi.1013512) gives local equilibrium stability and numerical multistability, not a proof of global upper-cost selection from every interior initial point. The 2023 two-variable adaptive risk model (DOI 10.7554/eLife.82954) lacks cost dynamics. A related preexisting mathematical result about interior invariant measures supplies nonrecurrence criteria but does not imply convergence to the specific defector equilibrium or exponential convergence of all three coordinates. Search-based novelty is not conclusive; a large PDF supplement could not be completely inspected.

## Mathematical value — PASS
This result separates existence of cooperation equilibria from **accessibility** under adaptive feedback, provides a quantitative global basin result and convergence rates, and isolates a sharp benefit obstruction by an exact stable cooperative counterexample beyond the threshold. These are dynamical questions not settled by the published local census and are relevant to whether initial-condition changes could sustain collective action.

Self-review: passed. Independent audit: not yet performed.
