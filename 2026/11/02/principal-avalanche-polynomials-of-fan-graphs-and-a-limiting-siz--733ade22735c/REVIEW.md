# Scientific review

## Correctness — PASS

The claim fixes \(n\ge2\), the sink and the exact degree thresholds. The recurrent-word criterion follows from the sink-burning algorithm, the saturated-run lemma proves that stabilization cannot topple sites more than once, and a fully specified finite-state weighted transfer system counts maximal runs with multiplicity exactly equal to possible trigger vertices. The rational transfer identity is verified symbolically over \(\mathbb Q(z,t)\), and an independent burning/stabilization implementation exhaustively tests every recurrent configuration and trigger vertex for \(2\le n\le9\). Pole asymptotics yield the stated normalized limiting distribution. The computations do not purport to prove an infinite theorem without the combinatorial transfer argument.

## Originality — PASS, qualified

Austin et al. (arXiv:1605.02713, full text inspected) already give the fan recurrent-state characterization and Fibonacci count in Proposition 43, and compute avalanche polynomials for wheels. Those claims are credited, not submitted as new. Our precise fan polynomial and limiting size-biased geometric law are not stated by the inspected wheel theorem or that fan counting proposition. The available full text on complete bipartite graphs is about a different adjacency structure; its formula does not automatically entail the fan result. Targeted searches for fan avalanche polynomials, saturated runs, wheel-to-fan equivalences, and mathematical-record matches found no covering statement. The original Cori–Dartois–Rossin chapter was not fully accessible; this leaves a real residual bibliographic risk and makes the originality conclusion best-knowledge rather than a uniqueness certification.

## Value — PASS

Avalanche polynomials capture the full distribution of local cascades rather than only recurrent state counts; the fan is a canonical one-dimensional graph joined to a sink, and the neighboring wheel computation makes it a mathematically motivated comparison family. The formula determines every coefficient at every graph order and yields a nontrivial thermodynamic limit with explicit zero mass and size-biased geometric positive tail. These are coherent natural distributional invariants, not arbitrary small numerical slices or a renaming of a published recurrent count.

## Limits and nearest literature

The primary nearest source is Austin et al., *The Avalanche Polynomial of a Graph*, arXiv:1605.02713v1 (full text), especially its Proposition 43. The 2004 paper *Avalanche Polynomials of Some Families of Graphs* (DOI:10.1007/978-3-0348-7915-6_10) could not be examined in full; the 2016 literature review describes its families as trees, cycles, complete graphs and lollipops. This remaining access limitation is not represented as a negative full-document inspection. The result has not been independently reviewed.

Self-review: passed. Independent audit: not yet performed.
