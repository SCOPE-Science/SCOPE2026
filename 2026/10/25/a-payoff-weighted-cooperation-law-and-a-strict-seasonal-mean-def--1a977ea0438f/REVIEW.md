# Scientific review of the payoff-weighted cooperation law

## Correctness: PASS

The differentiation of the explicitly defined observable \(H\) from the two evolution equations gives the exact identity \(\dot H=[\theta-(1+\theta)x]P_D\). The integration boundary terms vanish on every interior periodic orbit, and \(P_D>0\) makes its payoff-weighted mean well defined. For pairwise groups, the defector payoff is exactly proportional to \(x\) at every synergy value, giving \(\operatorname{Var}(x)=\bar x[\theta/(1+\theta)-\bar x]\); strict sign requires and receives the nonconstancy hypothesis. The source-consistent exact example has Jacobian trace \(-3/20\), determinant \(7/120\), and an attracting equilibrium; the implicit-function theorem yields a nearby periodic branch for sufficiently weak sinusoidal forcing. Direct reasoning excludes constant-cooperation forced periodic branches. The coefficient \(625/52372\) is reconstructed from the exact frequency response. Tests in `verify.py` corroborate each computational step. No global attraction or arbitrary-force existence claim is made.

## Originality: PASS (subject to bibliographic limitations)

Jiang et al. (arXiv:2212.06497, first posted 2022-12-13; DOI 10.1371/journal.pcbi.1011269) establish the payoffs, environmental feedback, and oscillatory phenomena. Shao, Wang, and Fu (arXiv:1904.11081) establish the earlier constant-synergy model and the interior equilibrium coordinate. The time-integrated payoff-weighting invariant, exact seasonal pairwise mean deficit, and explicit weak-forcing existence/response were not identified in their inspected main results or analytical appendix. Targeted records and literature searches did not expose a covering claim. Since the supplement to the 2023 article was not fully readable and no search exhausts all mathematical literature, equivalent derivations remain a nonzero risk.

## Value: PASS

The motivating work demonstrates feedback-driven seasonal cooperation cycles but does not quantify whether the average cooperation level equals the stationary reference. This result addresses that precise dynamical question nonperturbatively: an exact payoff-weighted law holds for all group sizes and a strict ordinary-time penalty holds for the natural pairwise boundary, independent of seasonality waveform and time scale. A rigorous constructive parameter example prevents the sign theorem from being merely vacuous, and its exact small-forcing coefficient quantifies the magnitude. The difference between payoff weighting for general groups and ordinary time weighting for pairwise groups is a meaningful structural effect of interaction order, not a cosmetic parameter substitution.

## Closest literature and residual limits

Primary sources: Jiang et al., PLOS Comput. Biol. 2023, DOI 10.1371/journal.pcbi.1011269 and arXiv:2212.06497 (model, oscillations, appendix on equilibrium stability); Shao et al., EPL 2019, DOI 10.1209/0295-5075/126/40005 and arXiv:1904.11081 (underlying feedback mechanism, stationary reference). The 2023 article's supplementary group-size sensitivity file was located but not inspected in full. Other environmental-feedback games use related replicator methods but lack a demonstrated implication to this particular seasonally forced payoff law. Local forcing existence does not imply arbitrary forcing recurrence; empirical simulations do not independently certify mathematical uniqueness or novelty.

Self-review: passed. Independent audit: not yet performed.
