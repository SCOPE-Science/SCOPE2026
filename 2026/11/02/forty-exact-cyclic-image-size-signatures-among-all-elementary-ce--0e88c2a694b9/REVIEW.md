# Scientific review

## Correctness (PASS)

The proof equates same-period predecessor existence to a nonzero diagonal entry in a Boolean de Bruijn relation product. Deterministic relation products yield exact integer vector recurrences for \(A_r(n)\). Cayley–Hamilton then turns equality through dimension \(d_r+d_s-1\) into a theorem for every \(n\). The bundled verifier regenerated 88 conventional symmetry classes, 40 image-count classes, their full 8/26/4/2 size distribution, 48 exact all-length equality checks (largest degree bound 4,750), and maximum separation length six. It also directly enumerated every input configuration for all 256 rules at lengths 1 through 11. The actual checker completed with `VERIFY_OK`. The method does not mistake those finite enumerations for a proof of an infinite assertion: the exact block-diagonal matrix argument supplies that bridge.

## Originality (PASS; remaining priority risk)

The most proximate primary source is Krawczyk, arXiv:1304.5771 (2013), whose full manuscript's classification counts compressed equivalence classes of states in global transition networks, denoted \(\#(N)\), not one-step reachable outputs \(A_r(N)\). It establishes the conventional 88 symmetry classes, but neither the precise 40-way image-count partition nor the sharp six-cell separation. Fukś, arXiv:1305.6533 (2013), analyzes preimage multiplicities of particular blocks under iterates; the current invariant counts **distinct complete cyclic outputs** after one step and compares **all** rules. Martínez, arXiv:1306.5577 (2013), surveys dynamical and classification invariants without a complete image-count partition. Salo, arXiv:1804.03913 (2018), covers von Neumann regularity and split epimorphisms, a different question. A finite interactive Garden-of-Eden census tabulates selected lengths, not an all-length proof. Literature comparison found no dominating classification. Absence from search is not proof of priority; unidentified earlier catalogs of one-step image counts remain a residual risk.

## Value (PASS)

A complete all-rule, all-ring-length classification gives a natural and reusable numerical equivalence invariant for finite cellular automata, with an unexpectedly substantial collapse from 88 conventional symmetry classes to 40 image-count signatures. Six-way collisions and the sharp length-six separation illuminate both the coarseness and finite detectability of the invariant. This is not merely a particular finite table: it settles the infinite comparison problem for all 256 elementary rules, useful in inverse reachability, finite-state information loss and algorithmic comparisons.

## Scope and evidence

The contribution does not classify image languages, multistep behavior, automaton conjugacy or number of individual predecessors. Its exact counts and formal all-length derivation are within the package. Historical priority and independent validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
