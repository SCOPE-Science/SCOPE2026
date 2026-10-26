# Review: Exact radius-two successive adjacent-swap balls

## Correctness (C): PASS

The changed-support partition in `RESULT.md` gives all mutually disjoint classes and proves \(1+b+\binom b2-s+h+d\) for every alphabet and length. Linearity of expectation gives the exact rational mean; the three-count upper bound plus explicit words characterizes nonbinary maximizers; the binary boundary-bit deficit identity and all small cases establish the binary maximum. The embedded program exhausts \(19{,}394\) centers and confirms direct balls, rational averages, maxima and extremizers; these checks supplement, rather than replace, the proof.

## Originality (O): PASS, with limitations

The nearest primary source is Kovačević--Goyal--Kiah, arXiv:2509.06692, which defines the successive model, bounds the two-stage \(\bar B\) ball (Proposition 5), and computes average one-stage disjoint balls (Proposition 6), but does not yield this radius-two equality or extremal classification. Cicirello, arXiv:1905.02752, defines the repeated-letter swap distance and develops distance algorithms, not sphere volumes. Indexed searches for alternative formulations, general bounds, exact tables, and stronger implications found nearby unrelated finite coding and mixed-error inverse-degree statements, not an implication covering this theorem. As always, unindexed overlap remains possible; source access and search do not prove global uniqueness.

## Value (V): PASS

This establishes an exact general-alphabet radius-two neighborhood invariant for a coding-motivated error model and determines average and worst-case ball sizes together with every maximizer, including sharp binary small-length transitions. The structural distinction between three-letter cycling and binary alternation supplies usable finite-radius geometry, beyond routine normalization or a small arbitrary example.

## Independent validation and scope

The derivation and checker are packaged for reproduction. Higher-radius behavior and optimal code-cardinality consequences are not asserted.

Self-review: passed. Independent audit: not yet performed.
