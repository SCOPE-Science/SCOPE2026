# Same-model review

## Correctness
PASS. The proof reduces the summatory occurrence count to a finite sum of positional tail-residue counting functions. For each position, the floor-plus-tail expression is derived directly from the binary residue class defining an occurrence of \(1^r\). A complete three-case comparison of the two residues proves superadditivity for arbitrary nonnegative arguments. The equality strip is a separate binary-prefix argument: below the stated threshold, prefixing the leading \(1\) creates no new boundary occurrence.

The bundled verifier independently reconstructs occurrences from binary strings, compares them with the positional formula, checks more than a million finite input pairs, probes complete residue periods and boundary cases, and exhaustively checks the equality strip through moderate dyadic scales. These checks support the proof but are not used to infer the infinite theorem.

## Originality
PASS. The closest direct recent source explicitly asks whether summatory digit inequalities have block-counting analogues and names binary \(11\) as its example. The closest older full-text source gives exact formulas for general subblock summatory functions, but its inspected theorem statements and proofs do not state the two-addend inequality or the sharp equality strip. published-finding corpus and public-web searches covered native notation, the classical \(B(N,w)\) notation, superadditivity aliases, and the cited historical sources.

The main residual risk is that the broad older exact formula could have generated an unindexed or unstated corollary elsewhere. The 1983 Kirschenhofer full text was not openly available through the checked routes, so that source was assessed from its abstract and later descriptions rather than a complete full-text read.

## Value
PASS. The \(r=2\) case is exactly the concrete block-counting example posed in the anchor paper, while the proof yields the full all-one family \(r\ge2\). The result also identifies an infinite dyadic equality region, showing that the positive correction term present in Graham's digit-sum inequality has no analogue depending only on the smaller addend here. This is a structural answer to a stated research direction, not a routine finite computation.

Same-model review: passed. Independent audit: not yet performed.
