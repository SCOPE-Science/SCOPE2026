# Review

## Correctness
**PASS (self-review).** The explicit inverse is a finite XOR sum because each active edge decreases a nonnegative rank. Fixed-control data maps are compact-group automorphisms, hence preserve fair product data. The optimal fixed-window error follows from a conditional fair unseen bit on any continuing rank chain; direct disjoint rank-cylinder summation yields the general law and the exact geometric tail. The proof addresses all nonnegative ranks and all radius-\(R\) decoders. Exact finite checks test inversion, tail sums, and Bayesian optimality, but are not used in place of the infinite proof.

## Originality
**PASS under checked evidence, with residual priority risk.** Yang's 2026 source already proves the underlying pointwise inverse and nonreversibility; those are not claimed as novel. The new claim is the exact optimal finite-window prediction risk under iid ranks, including the quadratic-logarithm geometric law. Direct inspection of Yang's Section 4 and the older nilpotent-block construction found no equivalent probabilistic error theorem. Finitary-coding and discrete-alphabet shift-morphism abstracts were checked, with their uninspected full texts identified as a risk. No search is treated as global novelty certification.

## Mathematical value
**PASS.** The sharp decoder and matching lower bound quantify the otherwise qualitative distinction between unrestricted inverse memory and average-case locality. The natural geometric-rank law leads to a strictly positive error at every finite radius but a superexponential optimal decay, with an exact almost-sure spatial error-frequency interpretation. These are quantitative structural properties of a motivated class of noncompact symbolic inverses, not a numerical curiosity.

## Closest literature and limitations
Closest: Jiang Yang, arXiv:2606.29958, Section 4; Ceccherini-Silberstein and Coornaert, arXiv:0910.0863, Section 5; Campos–Romero–Vivas (2022) on discrete-alphabet inverse continuity; Harvey–Holroyd–Peres–Romik (2007) on finitary-code tails. The theorem does not handle biased/correlated data, optimize \(\bar d\) over arbitrary joinings, or certify independent priority. The supporting exact enumerations cover bounded finite instances only.

Self-review: passed. Independent audit: not yet performed.
