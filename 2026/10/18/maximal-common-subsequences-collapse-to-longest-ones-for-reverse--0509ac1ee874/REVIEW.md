# Scientific review

## Correctness: PASS

For every integer alphabet size \(q\ge2\) and repetition count \(m\ge1\), the greedy-block criterion counts ascents, descents, and equalities exactly. Insertion of a letter between equal neighbors preserves both block-use budgets. The key nonstandard step is the one-sided-extension lemma: failure of an available ascent insertion forces the first letter to be minimum, the last to be maximum, all ascents to be steps of size one, and all descents to be full jumps, contradicting a smaller ascent than descent count. The symmetric case follows by alphabet reversal. This establishes maximality collapse at length \(2m-1\). A transfer-matrix derivation and constant-term calculation give the ternary formula. The packaged checker independently tests the claimed classification by direct maximality and confirms \(15\) finite cells; its dynamic method checks the ternary formula at \(40\) additional parameter values. Computation is corroborative, not a proof for untested integers.

## Originality: PASS within the evidence examined

Buzzega et al. (2025, arXiv:2504.04757), Hirota--Sakai (2023, arXiv:2307.10552), and Conte et al. (ISAAC 2023) study general maximal-common-subsequence algorithms or representations. Greenberg's two 2003 papers give general longest-common-subsequence counting methods and bounds. The examined results do not imply that **all** maximal subsequences become longest for a reversed-periodic permutation pair, or the ternary exact count; the structural inclusion-maximal versus length-maximal distinction matters. OEIS A396530 contains an arithmetically related central-binomial sequence but no inspected common-subsequence interpretation. Published mathematical-record and exact-formula searches found no covering statement. Possible unindexed coverage remains; a 2018 analogies article with a specific analogous pair was visible in a search snippet but not in accessible full text. A snippet is insufficient to rule out prior coverage, so that source is a named residual risk rather than a claim of no overlap.

## Value: PASS

Maximal common subsequences can include shorter objects than longest ones in general, complicating exhaustive output-sensitive enumeration. The theorem proves their equality throughout an infinite, explicitly parameterized family, gives a combinatorial characterization for all \(q\), and converts its ternary enumeration into a closed binomial formula with sharp exponential growth. This supplies a mathematically motivated benchmark for maximal-subsequence enumeration and precise output-size predictions beyond a small finite census.

## Scope and limitations

Only equally repeated, mutually reversed full alphabet permutations are covered. The ternary closed formula is not asserted for larger alphabets, and the self-review is not an independent expert audit. Prior numerical central-binomial identities are credited.

Self-review: passed. Independent audit: not yet performed.
