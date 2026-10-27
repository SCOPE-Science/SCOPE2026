# Scientific review

## Correctness — PASS

The full four-ranking definition fixes every allowed preference. The Condorcet criterion reduces to the two extreme-peak majority inequalities; the IRV failure event then requires the center to be the unique lowest first-preference candidate. Exact endpoint-counting gives the two ranges in the finite sum. The normalized counting polytope has volume \(7/864\), while all nonnegative four-histograms have leading count \(n^3/6\); hence the precise ratio is \(7/144\). Independent full-ballot enumeration and exact integer calculations are described in VERIFICATION.md and implemented in verify.py. No finite test is offered as a proof of the asymptotic theorem.

## Originality — PASS, with residual priority risk

Walsh (arXiv:1503.02766, 2015) gives the four single-peaked orders, not the stated IAC Condorcet-failure probability. Miller (2012) analyzes the known center-elimination mechanism, not the exact uniform-histogram law. Lackner and Lackner (2017) analyze probabilities of single-peaked domains within broader preference models; their examined sections do not supply this conditional fixed-axis IRV error. Kamwa, Merlin and Top (2023) analyze abstention/participation paradoxes under single-peaked IAC rather than the Condorcet-failure event; only their abstract was accessible. The same deterministic event has an independently weighted ballot law, whose exponential asymptotic behavior does not entail the uniform anonymous-histogram coefficient. The contrast is substantive, not relabeling of identical measures. Residual risk: restricted-domain Condorcet-efficiency studies and inaccessible specialized full texts could already give or imply the result. Exact historical priority is not independently established.

## Mathematical value — PASS

An IAC model explicitly treats anonymous electorate compositions as equally likely; unlike a uniform independent-ballot model, that places non-vanishing mass on imbalanced political blocs. The result quantifies an important gap between two standard social-choice benchmarks: the three-candidate single-peaked domain eliminates majority cycles, yet a meaningful constant fraction of IAC histograms yield an IRV Condorcet failure. The exact finite census, rational limiting constant and order \(O(1/n)\) give reproducible benchmarks for restricted-domain voting calculations; they do not merely recount a known tabulation. Its interpretation is limited to the stated culture rather than observed voting behavior.

## Closest sources and limitations

Relevant sources: Walsh (2015), Miller (2012), Lackner and Lackner (2017), Kamwa, Merlin and Top (2023), and works studying IAC Condorcet efficiency for other rules. Deterministic center-squeeze criteria and generic Ehrhart/Riemann counting methods are not new. Earlier inaccessible restricted-domain work is a remaining novelty risk. No independent review has been performed.

Self-review: passed. Independent audit: not yet performed.
