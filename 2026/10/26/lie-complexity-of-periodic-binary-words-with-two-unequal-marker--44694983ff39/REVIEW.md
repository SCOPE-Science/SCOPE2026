# Self-review

## Correctness — PASS

The word \((01^b01^d)^\omega\) has primitive period \(p=b+d+2\) for \(1\le b<d\), since a period block with two zeros could be a nontrivial power only when the two inter-zero gaps agree. For lengths greater than the primitive period, cyclic completeness of length-\(n\) factors forces each successive rotation's starting phase to advance by one, and closure forces \(p\mid n\). At shorter lengths, complete classification by the number of zeros gives the only five possible classes; interval coverage across short and long return gaps gives the precise threshold \(\min(d,2b+1)\). Direct summation and a two-piece monotone optimization establish the generating function, fixed-period mass, maximum and equality cases. The complete proof appears in RESULT.md. Independent finite brute-force comparison of complete classes has 28,766 passing cases, plus exact finite optimization and transition checks; finite testing is not used as an infinite proof.

## Originality — PASS, with residual risk

Bell–Shallit [1] defines the exact all-conjugates occurrence invariant and obtains general bounds, but the inspected original sections and examples do not imply this specific complete unequal-gap spectrum. De Luca–Fici [2] treats aperiodic Sturmian words, not this periodic word family. Cassaigne and collaborators [3] count conjugacy classes containing any occurring rotation, a different invariant with weaker occurrence requirements. No equivalent or stronger covering result was identified in targeted published-paper and research-record queries. The primary research papers' full available HTML texts were inspected beyond abstracts. An undiscovered reduction or unindexed treatment of a special periodic family remains possible. Absence of a search result does not itself prove novelty.

## Mathematical value — PASS

The two unequal return gaps form the simplest primitive periodic binary family with competing marker spacings. Full cyclic completeness is not equivalent to ordinary cyclic-factor complexity. The exact classes expose a sharp \(d=2b+1\) threshold, a three-class coexistence transition at \(d\ge2b+2\), and explicit first-period mass with sharp all-parameter equality conditions under fixed primitive period length. Counting all transient Lie classes before the permanent primitive-period series is a natural finite invariant for periodic words. This is a complete infinite-family structural and extremal classification, not an arbitrary finite census.

## Related literature and scope

[1] J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821 (2021 preprint).

[2] A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995 (2022 preprint).

[3] J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (2014 preprint).

The classification is limited to primitive unequal two-gap periodic binary words, and independent validation remains to be performed.

Self-review: passed. Independent audit: not yet performed.
