# Self-review

## Correctness — PASS
The statement concerns all integer cycle lengths \(n\ge4\), nonadjacent offsets \(2\le k\le n-2\), and nonnegative rates \(a,b\). Its proof uses an exact finite cyclic adjugate identity and a rank-one determinant expansion, then obtains the Kemeny functional from the first two characteristic-polynomial coefficients. The sign and strict-equality statements follow by explicit differentiation and integer inequalities. Exact minor and determinant checks corroborate the coefficients without claiming to prove the unbounded-parameter theorem by enumeration.

## Originality — PASS, with qualification
Catral et al.'s general 2010 stochastic-matrix perturbation theory, Kirkland's 2010 graph-wide discrete-time optimization and Kirkland--Zeng's 2016 directed-forest identity/Braess analysis for undirected trees were compared using primary text. A pre-existing one-shortcut specialization covers \(b=0\); the distinct contribution here is the exact **simultaneous reciprocal-rate law**, fixed-budget orientation and threshold reversal. General matrix-tree and determinant tools themselves are not claimed as original. A specialized unindexed prior solution remains possible.

## Value — PASS
The theorem supplies a complete rate-and-location decision rule in a natural edge-addition problem. It demonstrates that adding a reciprocal connection is globally harmful relative to the unmodified cycle in every dimension above four, yet incrementally increasing one of its rates can become beneficial after an exact threshold. It also gives a closed-form choice of rate orientation and the worst location under symmetric installation.

## Closest sources and limitations
- Catral, Kirkland, Neumann, Sze (2010), https://doi.org/10.1007/s10915-010-9382-1: general perturbations and structure-dependent Kemeny identities.
- Kirkland (2010), https://doi.org/10.1016/j.laa.2010.07.016: discrete-time constrained digraph optimization, not fixed-rate reciprocal CTMC chords.
- Kirkland and Zeng (2016), https://doi.org/10.13001/1081-3810.3222: general forest representation and Braess behavior for undirected trees.
- An existing one-arc directed ring result is a covered boundary case and is not claimed as new.

The result does not treat heterogeneous base rates, multiple chord pairs, or other notions of mixing; historical coverage is not guaranteed. Independent expert validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
