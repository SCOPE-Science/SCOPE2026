# The minimum ternary perfect code for two adjacent deletions at length five

## Finding

For the ternary alphabet \(\Sigma=\{0,1,2\}\), the smallest perfect length-five code correcting a burst of exactly two adjacent deletions has precisely \(8\) codewords. In the standard burst-deletion spectrum notation, the minimum element of \(\mathrm{Spec}_B(3,5,2)\) is \(8\).

One optimal code is

```text
02200 01001 10021 11002 21012 22120 21111 20122
```

## Assumptions and scope

A received word consists of the three symbols remaining after deletion of exactly two consecutive positions from a length-five word. For a word \(x=x_1x_2x_3x_4x_5\), define its *burst shadow* as the set
\[
B(x)=\{x_3x_4x_5,\ x_1x_4x_5,\ x_1x_2x_5,\ x_1x_2x_3\}.
\]
Repeated received words within one shadow are counted only once. A perfect code means that the shadows of distinct codewords are disjoint and their union is all \(27\) ternary length-three words. The claim is specific to alphabet size \(3\), length \(5\), and adjacent two-symbol deletions; it does not concern nonadjacent deletions.

## Proof

**Upper bound.** The eight displayed codewords have burst shadows of cardinalities \(4,3,4,4,3,3,2,4\) in the displayed order. Their shadows are pairwise disjoint and the sum of these cardinalities is \(27\), the full number of ternary length-three words. A direct set comparison is implemented in `verify.py` and is independently enumerated by its shadow construction. Thus the perfect-code minimum is at most \(8\).

**Lower bound.** Every length-five word produces at most four received words, so any covering code contains at least seven codewords. To eliminate the only remaining smaller possibility, enumerate all \(3^5=243\) potential codewords and their \(27\)-bit burst-shadow masks, and exhaustively search for a cover of the \(27\) received triples using at most seven masks. The exact search starts with all bits uncovered and recursively chooses an uncovered bit with the fewest eligible masks containing it. At state with \(u\) uncovered bits and \(r\) remaining codewords, reject if \(u>4r\); any first chosen mask must cover at least \(\max\{1,u-4(r-1)\}\) currently uncovered bits. Branch over *all* masks containing the chosen bit that meet this necessary bound. Memoize the pair (uncovered-mask, remaining-word-budget). If no branch covers all bits, no cover with at most seven words exists, because any proposed cover must include a mask covering the chosen bit and meeting the necessary bound. There are no heuristic pruning rules. The complete search reaches \(649\) distinct states (\(735\) recursive calls in the C++ implementation) and finds no seven-word cover. The complete executable enumeration is in `verify.py` and the independent implementation `exhaustive_lower.cpp`.

Combining the lower and upper bounds proves the stated exact optimum \(8\).

## Verification

From the supplied files, run `python3 verify.py`, which uses only the Python standard library and prints `VERIFY_OK` with a complete independent perfect-code shadow check and the exhaustive seven-word-cover rejection. An independently coded integer-bitset verifier can be compiled and run with `g++ -std=c++17 -O3 exhaustive_lower.cpp -o exhaustive_lower && ./exhaustive_lower`; it prints `SEVEN_WORD_COVER_EXISTS? 0` and reports \(735\) calls and \(649\) memoized states. No numerical optimization or solver logs enter the proof.

## Relationship to prior work

Chee–Li–Zhang (2015) introduced the spectrum of sizes of perfect burst-deletion-correcting codes. In its length-five, two-burst construction from perfect length-three single-deletion codes, the ternary case produces sizes \(9,12,15\), but this construction does not imply an eight-word code or rule out seven words. Its stated general optimal-family result establishes \(q^3/4\) for even alphabets, not an exact ternary minimum. Xie–Sun–Ge (2026) study covering codes under insertions and deletions, including general nonbinary burst-deletion covering constructions; those bounds do not provide the specific optimum and perfect eight-word partition given here. A perfect code is simultaneously a covering code and a uniquely decodable burst-deletion code.

## Limitations

This is an exact finite result only for \(q=3\), \(n=5\), and a burst of two deletions. No complete spectrum of *all* perfect-code sizes is claimed, and no infinite family follows from this finite calculation. The correctness certificate consists of exhaustive finite enumeration of the complete search space, not a symbolic classification of all optimal codebooks. Earlier unindexed finite classifications remain a possible novelty risk.

## References

1. C. Xie, Y. Sun, and G. Ge, “New bounds for covering codes under insertions or deletions,” arXiv:2606.15379v1, first public 2026-06-13. https://arxiv.org/abs/2606.15379
2. Y. M. Chee, Y. Li, and X. Zhang, “Spectrum of sizes for perfect burst deletion-correcting codes,” ISIT 2015, pp. 1931–1935, DOI:10.1109/ISIT.2015.7282792. https://doi.org/10.1109/ISIT.2015.7282792
