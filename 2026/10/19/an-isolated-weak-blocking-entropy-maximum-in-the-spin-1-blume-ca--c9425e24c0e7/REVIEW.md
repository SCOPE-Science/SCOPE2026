# Mathematical review

## Correctness — PASS
The local objective \(f_{a,c}(u)=\delta u^2-(a+c)u\) exhausts all possible one-site energy changes and yields exactly the transition points \(\delta=1,2\) for positive field. For the nine-state overlapping-pair transfer matrix, every labelled stable cyclic word corresponds to one closed walk, and conversely. Its four exact characteristic polynomials are checked symbolically with `verify.py`. The domain–zero-run classification independently derives the two Perron growth equations; their uniqueness and strict separation follow from monotone positive renewal kernels. For \(\delta>1\), any nonzero site propagates a monochromatic configuration, proving the finite exact counts. The square-gradient identity proves the ground-state contrast. The package also performs 30 exhaustive finite-volume comparisons; these are corroboration rather than a substitute for the analytic proof.

## Originality — PASS within inspected comparisons
The closest physical literature concerns spin-1 Blume–Capel metastability but different objects: Fiig et al. (1994) use long-range metastable free-energy branches; Yamamoto–Park (2013) study two-dimensional nucleation lifetimes; Chen–Shen (2015) study three-state network nucleation. Waclaw–Burda (2008) count one-spin-stable binary disordered spin glasses, not three-spin-value chains with a crystal field. Published positive-temperature transfer-matrix partition functions count Boltzmann-weighted configurations, not weak one-step minima. Direct claim and equivalent-formulation searches did not identify the exact 9-state blocked-word trace, the quartic Perron root, or the three-ground-state/exponential-local-minimum contrast. This is not a claim of exhaustive novelty: full 1994 text was inaccessible and separately indexed work could contain an equivalent result.

## Mathematical value — PASS
The result is a complete exact positive-field classification of the one-site energy-landscape complexity of a standard three-state magnetic chain. It separates true ground-state coexistence from the extensive proliferation of weak local minima at the same coupling and quantifies a sharp isolated entropy spike. The strict contrast between an extensive low-field density, an enhanced marginal density, and exactly three or one stable configurations at larger fields is structural, not a small finite census or a reparametrized known table. The distinction can matter when neutral moves are suppressed versus accepted.

## Limits
This concerns labelled cycles, uniform nearest-neighbour exchange, strictly positive crystal field, and all single-site recolourings. No finite-time kinetic, neutral-move absorption, or higher-dimensional statement is claimed. An independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
