# Review of exact metastable consensus lifetime

## Correctness — PASS

The two specified strict coordination payoff matrices give the two opposed best-response thresholds. Explicit conditioning on the selected player and layer gives a finite birth–death chain, including a doubled inward jump probability at the first state outside each one-way consensus corridor. Reflection at the central count supplies the exact boundary condition, the binomial detailed-balance identity solves the first-step recursion, and the harmonic sum accounts for the remaining corridor time. The exact recurrence is checked independently through 13,814 rational assertions, including microstate enumeration for small populations. The strict entropy gap follows from matching binomial upper and lower bounds and Stirling asymptotics, not from finite extrapolation.

## Originality — PASS (provisional priority)

Raducha and San Miguel (arXiv:2212.08877) study two opposing games on overlapping graph layers, chiefly finite-simulation phase diagrams for random regular layers. The examined manuscript does not state the exact complete-graph expected absorption time or parameterized entropy exponent. Auletta and collaborators (arXiv:1107.4537, Section 6) investigate a related almost-Ehrenfest chain arising from an OR game under logit dynamics, but its exceptional transition structure and model differ and its statements do not imply this exact threshold-dependent time identity. Krapivsky and Redner (arXiv:2103.04248) analyze exponential consensus times for a two-class majority-rule process, not the alternating coordination payoff family. Classical Ehrenfest identities are acknowledged as tools, not purported discoveries. Broader general birth–death formulations or unpublished specializations remain priority risks; a negative search alone does not certify global novelty.

## Value — PASS

A mixed population under opposed, alternately sampled strategic environments appears persistent in simulations, yet the finite game has almost-sure consensus. The result precisely quantifies the size-dependent lifetime, supplies a closed calculation at every allowable even population, and identifies how the conflict threshold alters the exponential barrier. This is a useful interpretable benchmark for finite-size effects in multilayer coordination games, not an arbitrary isolated numerical example.

## Closest literature and limitations

References: arXiv:2212.08877 (full main manuscript reviewed); arXiv:1107.4537 (full available text, with Section 6 examined); arXiv:2103.04248 (paper and relevant derivations read). Historical priority and uninspected external supplements remain a risk. The theorem excludes sparse random-regular layers, partial node overlap, nonuniform update rules, tie conventions, and full consensus-time distribution claims. Independent scientific evaluation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
