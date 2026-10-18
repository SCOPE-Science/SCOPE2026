# Self-review

## Correctness — PASS

The claim quantifies over all finite chain dimensions, all bounded measurable controls, all horizons, and all initial states. The exact first-variation and weighted quadratic storage identity is reconstructed in the proof rather than inferred from numerical data. Conservation adds the required linear inventory storage, yielding the unaveraged identity (1). Strict curvature of the quadratic vacancy law and a compact-ratio argument give a positive dissipation coefficient uniform over all horizon-mean rate vectors in the stated rate box. Integrating proves the finite-horizon estimate, and the one-site solution proves the necessity of an order-inverse-horizon transient allowance. `verify.py` passed 3,170 exact-rational pointwise algebra and sampled positivity assertions; these are not a proof of the universal statement.

## Originality — PASS, with priority risk

Zhou, arXiv:2610.10602v1, Theorems 3.2/3.5, explicitly treats jointly periodic forcing and its periodic orbit; §7 asks about non-common-period and more general recurrent inputs. The new statement concerns arbitrary measurable inputs, arbitrary initial states, the same horizon's means, a uniform quadratic-state deviation penalty, and a sharp transient allowance. The exact nonlinear edge dissipation and the weighted quadratic energy already appear in that article and are not represented as inventions here. The nonperiodic inventory-storage combination, control-uniform coercivity, and quantified performance theorem are not stated in the inspected source. The complete main proof of Massas and Margaliot, arXiv:2607.25435v1, concerns the *linear* hindrance law and periodic solutions. Al-Radhawi, Margaliot, and Sontag (2021) treat periodic optimal control; their relevant open-access full text does not state this law. Broader control-dissipativity principles are a potential earlier route to an equivalent result, so independent priority review is needed.

## Mathematical value — PASS

The estimate answers a concrete, expressly posed dynamical extension: it removes recurrence entirely while controlling performance and squared state occupancy errors for every positive time horizon. The rate-box constants make the conclusion robust under switching and quasi-periodic modulation, and the exact one-site transient proves the boundary correction has the best possible horizon order. This is a structural transport theorem, not a numerical increment or an arbitrary parameter slice. Its value is limited to the curvature-rigid quadratic hindrance class, not to all generalized RFMs.

## Closest literature and residual limits

Primary comparison: H. Zhou (2026), arXiv:2610.10602v1, §§2–3 and 7, fully inspected. Secondary main-paper comparison: R. Massas and M. Margaliot (2026), arXiv:2607.25435v1, theorem/proof and discussion, inspected using its public full-text representation. Earlier full-text control context: M. Ali Al-Radhawi, M. Margaliot and E. D. Sontag (2021), Royal Society Open Science 8:210878. Related nonlinear cascade preprint arXiv:2608.15214v1 inspected at abstract level only; it has a different feedforward object, but overlapping methods cannot be excluded. The lower-dissipation constant is existential, and general nonlinear hindrance is not covered. No independent audit or external certification has been performed.

Self-review: passed. Independent audit: not yet performed.
