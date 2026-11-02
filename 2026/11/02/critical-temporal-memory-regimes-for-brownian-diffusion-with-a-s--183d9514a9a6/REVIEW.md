# Self-review

## Correctness — PASS

Under a stationary independently Poisson-refreshed intensity environment and a conditional Cox reset process, conditioning on the first intensity redraw gives the exact renewal equation for the no-reset survival function. Its Laplace transform is a resolvent with denominator strictly positive for every fixed positive refresh rate. A two-sided Brownian construction conditional on the reset history yields the exact stationary covariance \(C_\mu(t)=2D\int_t^\infty S_\mu(u)\,du\), and differentiating the resolvent gives the integrated normalized covariance. The two singular indices follow by beta-integral asymptotics of \(g\) and \(h\). The gamma profile is proved by convergence of Laplace transforms of the survival-weighted law; the logarithmic profile follows by a two-sided stochastic-intensity sandwich and explicit integration. All parameter boundary cases \(\alpha=1,2\) are addressed separately.

Finite verification: the standalone `verify.py` executed successfully, testing two-rate killed generators, exact Stieltjes transforms and derivatives for gamma intensity laws, asymptotic constants, deterministic-rate reduction, and numerical inversion of both scaling profiles. It yielded 271 deterministic assertions. The universal statements rely on the mathematical proof, not finite observations.

## Originality — PASS, qualified best-knowledge

The motivating Arutkin–Reuveni paper (arXiv:2509.25365v1) already proves the exact spatial characteristic transform in this Cox resetting model. Its general survival functional and stationary formula are acknowledged, and the new result does **not** reassert their spatial transform. In particular, their formula implicitly determines the same killed-survival resolvent; that implication is explicitly included in the comparison rather than hidden. The assessed claim combines the temporal covariance identity with a full weak-refresh transition analysis: two distinct critical low-rate indices, an incomplete-gamma correlation profile, and a separate logarithmic-observation-time profile. These are not stated as such in the inspected source.

Stojkoski et al. (arXiv:2107.11686) derive the exponential steady correlation for constant-rate Poisson resets and give a general last-reset-time framework, which recovers the fixed-rate boundary here but does not by itself state the nonrenewed random-intensity scaling theorem. Taźbierski (2025 dissertation) studies Cox and mixed-Poisson reset models through distributions and mean-square displacement; the examined relevant sections do not establish the present stationary two-time scaling results. Published mathematical record searches and accessible previous claims revealed no statement with the same two indices and full profiles, but this is a best-knowledge assessment, not proof of uniqueness. Known general Tauberian and Laplace-continuity theorems supply ingredients, so implicit coverage remains a genuine residual risk.

## Value — PASS

The statement resolves a mathematically motivated distinction between finite instantaneous fluctuations and persistent temporal correlations in an established stochastic-reset model. The open interval \(1<\alpha\le2\) has a finite limiting stationary position variance yet a diverging integrated correlation time, a regime not detected from the variance alone. The exact incomplete-gamma profile and critical logarithmic-time law provide observable, quantitative signatures of slow environmental refreshes across all eligible intensity densities, not an arbitrary numerical slice.

## Closest literature and limitations

The reference model and stationary spatial transform are prior results of Arutkin–Reuveni, 2025. The fixed-rate temporal correlation comes from Stojkoski et al., 2021; general Cox reset and mixed-Poisson displacement studies appear in Taźbierski, 2025. The theorem assumes an independent Poisson environmental refresh clock, complete positional reset, and a positive intensity density regularly varying as a pure power at zero. It does not assert finite-rate uniform-in-time bounds, arbitrary renewal environmental refresh, stochastic clock dependence on position, or first-passage behavior. The general stochastic-process literature could still implicitly subsume part of the result.

Self-review: passed. Independent audit: not yet performed.
