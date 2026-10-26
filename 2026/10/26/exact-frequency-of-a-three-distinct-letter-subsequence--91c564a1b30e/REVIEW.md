# Review

## Correctness

The claim is the generating function for literal subsequences of a fixed three-symbol pattern with pairwise distinct symbols. For the ternary alphabet, the occurrence count is \(\sum_{j:w_j=1} Z_jT_j\). A total of two is exhausted by one contribution of two or two contributions of one. The associated word forms are disjoint and unique; their generating functions sum to \(x^4(3-x)/((1-2x)^2(1-x)^3)\). Inserting neutral symbols into the \(t+1\) gaps of a ternary core gives the stated formula for every \(m\ge3\). Enumeration through length eight for \(m=3,4\) agrees with the formula.

## Originality

The closest primary work treats binary literal subsequences (Menon–Singh) or order-isomorphic patterns (Mansour–Rastegar–Roitershtein and Mansour–Rastegar). Bruda's accessible binary theorem and discussion of an \(m\)-ary extension do not state this exact generating function. The accessible published-finding corpus search and owned-ledger claim/ID scans returned no same-claim record. A mentioned in-preparation automaton paper remains a specific residual overlap risk; no claim of exhaustive literature coverage is made.

## Value

This gives a closed exact count for the first nonbinary, three-distinct-symbol literal-subsequence case with two occurrences, a concrete test case for the broader \(m\)-ary frequency problem. It supplies an all-length formula rather than only a finite census or asymptotic growth statement.

## Closest literature and limitations

- Menon–Singh, arXiv:2306.07870v1: exact binary subsequence frequencies; larger alphabets are a stated direction.
- Bruda, arXiv:2607.02578v1: exact binary frequency structure and an \(m\)-ary conjecture; an in-preparation treatment is mentioned but not publicly inspectable here.
- Mansour–Rastegar–Roitershtein, arXiv:1905.05646: order-isomorphic pattern occurrences, not literal equality of subsequence symbols.

Self-review: passed. Independent audit: not yet performed.
