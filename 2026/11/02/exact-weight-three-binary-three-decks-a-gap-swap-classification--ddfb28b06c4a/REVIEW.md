# Scientific review

## Correctness — PASS

The three-deck equivalence criterion is proved by direct pattern counts: all eight coordinates are equivalent to the three positional invariants \((L,T,Q)\). A quadratic equation in the first one-position has at most two solutions; its second root is the precise gap swap. A unique orientation by larger first gap gives a bijection between unordered collisions and the integer parameters \((b,h,p)\) with \(b,h\ge1\), \(p\ge0\), \(p+2b+4h\le n-1\). Coefficient extraction yields the claimed rational generating function for every length. A standalone checker reconstructs every equivalence class through length 22, independently computes scattered-subsequence pattern counts through length 15 and returns `VERIFY_OK`. The formal proof does not depend on finite experiment.

## Originality — PASS, with residual risks

The 2013 work of Rigo and Salimov introduces the binomial-equivalence setting; it does not give the fixed-weight-three three-deck classification. The directly pertinent full text by Chrisnata and collaborators states the exact same rational generating function as **Conjecture 1**, not a theorem, after proving only a cubic-order growth bound and checking the first twenty coefficients. This work supplies the missing all-length proof and classifies every collision pair. Later broad work on total deck counts has an abstract that does not imply this fixed-content formula; its full text was unavailable through the attempted access route. Search coverage and historical priority are therefore qualified, as documented in `AUDIT.json`.

## Mathematical value — PASS

The counting identity resolves an explicitly stated literature problem and determines the exact number of distinguishable fixed-weight-three binary sequences under a complete three-subsequence readout. The two-word fiber rigidity also yields an explicit classification of all ambiguity and a natural optimal code size. It is not just an additional finite table entry.

## Closest literature and limitations

Chrisnata et al., *On the number of distinct k-decks*, section 5.3 and Conjecture 1 (early access 2021), is the closest source; see the paper's full text linked in `RESULT.md`. Earlier related work is Rigo and Salimov (2013). Nilforoushan and Parvaresh (2026) study total deck growth but not this exact subclass in their accessible abstract. These are same mathematical model literature and proof assessments. The theorem is restricted to binary linear words with exactly three ones and perfect length-three subsequence multiplicities.

Self-review: passed. Independent audit: not yet performed.
