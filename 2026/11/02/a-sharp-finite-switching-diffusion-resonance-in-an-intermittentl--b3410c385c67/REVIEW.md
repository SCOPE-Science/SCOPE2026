# Scientific review

## Correctness — PASS

The object is a continuous-time Markov-modulated planar swimmer with state-independent rotational Brownian diffusivity \(D_R>0\), zero propulsion in the resting state, opposite state-dependent angular drifts, and fixed rate ratio \(r\ge1\). The diffusion coefficient is derived by integrating the stationary velocity correlation, identified with the \((+,+)\) entry of an exponentially stable \(2\times2\) complex semigroup. Its inverse gives the displayed rational expression. Direct differentiation factors into a quadratic with strictly positive constant coefficient; its linear and leading coefficients have the stated signs below the explicitly derived threshold. Above the threshold, the negative leading coefficient forces a unique positive critical point and thus a unique global maximum. The expansion at the threshold yields the asserted sharp blow-up prefactor. Symbolic exact checks and independently quadrature-integrated correlations (1,478 total checks) reproduce these steps. None of the finite tests purport to prove the continuum assertions.

## Originality — PASS on examined evidence

Weber, Sokolov and Schimansky-Geier (arXiv:1205.3419, 2012) analyze asymmetric Markov angular forcing with **constant** translational speed; they already obtain nonmonotone diffusivity and resonance, so neither phenomenon in isolation is original here. Their accessible abstract does not supply a motile/resting state that simultaneously flips the angular drift. Nourhani et al. (arXiv:1607.00587, 2016) study chirality reversals with constant speed. Das and Basu (arXiv:2301.11194) again retain constant speed, whereas Jamali (arXiv:2012.14155) switches motile and passive speeds but specifies independent rotational Brownian angular dynamics. The present claim instead fixes the motile fraction while varying both transition rates, links propulsion shutdown exactly to opposite chirality, and proves a sharp rate-ratio boundary with a uniquely finite optimum and inverse-distance critical scaling. The closest examined published-results records concern different stochastic or dynamical objects and do not imply this theorem.

This is a historical-priority assessment, not proof of uniqueness: the complete 2012 Weber et al. study remained inaccessible from the available lawful routes. A fuller bibliographic comparison may reveal broader coverage.

## Mathematical value — PASS

The switching rate changes temporal correlations without changing stationary motile occupancy. Whether increased switching can *reduce* long-time exploration is therefore not settled by mixture weights alone. The exact threshold separates an everywhere-monotone regime from genuine optimal finite switching, with a sharp divergence of the optimizer at onset. The rule is physically motivated and parameter-wide, not a single isolated computation. Its precise dimensionless critical law can guide design of intermittent self-propelled transport.

## Limitations

The theorem is restricted to positive rotational diffusivity, \(\Omega>D_R\), the sector \(r\ge1\), symmetric opposite angular-speed magnitudes and Poisson transitions. It concerns asymptotic scalar diffusion rather than finite-time navigation, arbitrary speed switching, or experimental optimization. A closely related historical full text remains inaccessible. No independent certification is claimed.

Self-review: passed. Independent audit: not yet performed.
