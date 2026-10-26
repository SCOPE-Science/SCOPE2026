# Review

## Correctness

The proof sums exact path-reachability probabilities and evaluates finite rational sums. The size-biased household law gives \(\mathcal R_*=\beta\sum_m q_m mH_m/\mathbb E[M]\). Both distributions have mean \(2\) and second moment \(5\); their reproduction numbers are \(13\beta/8\) and \(77\beta/48\), so they lie on opposite sides of one throughout \(\beta\in(8/13,48/77)\). At \(\beta=31/50\), the exact values are \(403/400\) and \(2387/2400\). The claim is limited to the stated path-household branching model.

## Originality

The closest inspected household-size formula uses a size-independent attack rate and therefore gives an affine expected household size; another inspected model uses complete mixing within each household. Neither of those displayed formulas implies the exact path-contact witness. Searches also returned a household-epidemic ranking result comparing \(R_*\) with a different reproduction number, but its available summary does not establish this moment-matched threshold comparison. Broader household-network literature remains a residual overlap risk.

## Value

The example is a compact exact counterexample to using only the first two household-size moments to classify invasion when within-household topology affects transmission. Its value is the qualitative threshold flip over a nonempty interval of external-infection means, not the small numerical difference at one chosen point by itself. It identifies a model boundary and does not claim the same conclusion for size-only attack-rate models.

## Closest literature and limitations

Dönges et al. (2023 preprint; 2024 journal publication) derive a moment formula under a size-independent attack-rate assumption. Barlow, Adams, and Penington (2024 preprint) model complete-mixing household contacts with a Markovian within-household process. Ball, Sirl, and Trapman (2008 preprint; 2009 publication) analyze household branching processes and assume equal household sizes for their main exposition. The exact witness here uses path contact graphs and independent edge transmission.

Self-review: passed. Independent audit: not yet performed.
