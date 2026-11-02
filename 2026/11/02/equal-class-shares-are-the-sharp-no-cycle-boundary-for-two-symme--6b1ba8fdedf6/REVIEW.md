# Scientific review

## Correctness — PASS

The exact half-share comparison follows from the odd strictly increasing function \(G(z)=F(z)-1/2\): the sign of \(G(a)+G(b)\) equals the sign of \(a+b\), including ties. At unequal shares, choosing \(d\) between half and all of the positive inverse-link cutoff forces the reverse-edge probability above one half for every positive \(K\), while sufficiently large finite \(K\) makes the other two majority directions strict. Logistic subcase inequalities and the exact three-alternative witness have been reconstructed. The standalone rational checker passed 25,215 assertions. It does not replace the infinite analytical proof.

## Originality — PASS within inspected evidence; historical priority provisional

Regenwetter, Dana and Davis-Stober (2010, https://doi.org/10.3389/fpsyg.2010.00148) place binary majority relations and mixtures of strict latent rankings in a general convex framework, but their broad class does not identify this two-score common-link share boundary. Zhao, Piech and Xia (2016, https://arxiv.org/abs/1603.07323) address Plackett–Luce mixture identifiability rather than pairwise majority weak ordering. Makhijani and Ugander (2019, https://doi.org/10.1145/3308558.3313717) construct cycles with a nonlinear majority of three independent dimensions, an operator not implied by, nor implying, this convex two-class blend. Generic two-component BTL identifiability was also compared at abstract level (https://arxiv.org/abs/2201.13132). Searches for two-class mixture aliases, geometric-mean score ranking, equal mixing and three-cycle constructions did not locate a dominating published claim. Earlier equivalent descriptions and unavailable detailed sections of later mixture literature remain priority risks.

## Value — PASS

A precise structural question about population aggregation of individually transitive random-utility responses has a complete all-links answer. It is useful to know that exactly equal mixing shares guarantee a globally weakly transitive majority ranking even with large between-class disagreements, whereas arbitrarily small imbalance permits a three-alternative Condorcet cycle with carefully chosen scores. This distinguishes a universal guarantee from a mere existence example and supplies exact rational validation for logistic mixture implementations. There is no asserted empirical effect, statistical significance or claim of a broader preference-inference theorem.

## Scientific limitations

The two classes must share one strictly increasing, symmetric comparison link; the theorem addresses population-majority signs, not strong stochastic transitivity, rankings from finite samples, or arbitrary group-specific links. Cyclicity outside the boundary is attainable, not unavoidable for every utility profile. Reproduction uses `python3 checker.py`; mathematical implications beyond the tested finite grid are proved in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
