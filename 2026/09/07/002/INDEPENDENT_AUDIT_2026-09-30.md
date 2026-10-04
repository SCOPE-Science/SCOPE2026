# Independent audit — 2026-09-30

## Final claim assessed

For lazy simple random walk on the balanced spider S(k,L), the stated two-stage faithful coalescing coupling has mean at most 3L squared; consequently it has the stated geometric restart tail, mixing-time upper bounds, and centered exponential tail.

## Correctness — PASS

The radial distance process and stationary distribution are correct. Folding lazy walk on the cycle of length 2L gives the radial chain. Under alternating updates, each lifted marginal has the correct lazy-cycle law while the difference performs a simple nearest-neighbor walk until meeting, with mean at most L squared. After the radial distances agree, synchronous radial moves preserve equality and reach the center in mean at most 2L squared. Strong Markov plus Markov's inequality gives the 12L-squared quarter-tail; the advertised 32kL-squared scale is a looser valid corollary, and iteration gives the geometric and exponential tails. The L=1 endpoint convention is consistent.

Evidence inspected:
- RESULT.md
- standard gambler's-ruin hitting-time formula
- stationary detailed-balance check for the spider walk

Residual risks:
- The constants are deliberately loose and no matching lower bound or cutoff statement is established; simulations are only supporting evidence.

## Originality — PASS

Searches found literature on spectral analysis of birth-death chains on infinite spiders and exact cover times of spider trees, but not this finite balanced-spider coalescing construction or these explicit coupling-tail/mixing bounds. The related papers cited in the record concern infinite-spider excursions, nonreversible cycle speedups, and binary-tree cover behavior, not this statement. Published-record search found no duplicate.

Sources inspected:
- de la Iglesia and Juarez, arXiv:2111.10450, Birth-death chains on a spider
- Higuchi-Owa-Shirai, Journal of Math-for-Industry 2 (2010), exact cover times of certain trees
- Csaki-Csorgo-Foldes-Revesz, arXiv:1501.00466

Residual risks:
- A textbook or lecture-note treatment may contain essentially the same coupling without indexing it as a balanced-spider theorem.

## Scientific value — PASS

The balanced spider is a natural finite family, and the cycle-fold coupling isolates the diffusive L-squared scale independently of the number of legs before the deliberately looser stated corollary. The result gives a clean structural coupling lemma and explicit concentration, not merely a simulation.

Context checked:
- RESULT.md
- spider random-walk literature

Residual risks:
- The proof uses elementary ingredients and the public headline scale 32kL squared is weaker than the sharper 12L squared bound already proved in the same record.

## Outcome

All three acceptance axes pass for the final claim as stated. Conjectures, heuristic search observations, and explicitly excluded broader regimes remain outside the accepted claim.
