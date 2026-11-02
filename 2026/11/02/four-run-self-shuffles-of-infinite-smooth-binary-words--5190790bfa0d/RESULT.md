# Four-run self-shuffles of infinite smooth binary words

## Finding

Let the alphabet be \(\{1,2\}\). A finite word is *smooth* if repeated finite run-length differentiation (with singleton boundary runs removed at each step) reaches the empty word without any run of length greater than two. A *self-shuffle coloring* assigns every position one of the colors \(U,D\) so that the two induced subsequences are the same word. Its *color-run bound* is the maximum number of consecutive positions of one color.

**Theorem.** Every right-infinite smooth binary word with infinitely many prefixes in which each letter has even multiplicity has a self-shuffle coloring of its entire set of positions whose two infinite color subsequences agree, and whose color-run bound is at most \(4\). In particular, the classical Kolakoski word starting \(122112122\cdots\) has such a coloring. This strengthens the explicit bound \(48\) obtained for that word in [1, Corollary 6.2].

The finite theorem underlying the construction is sharp for its prescribed window: *every* smooth even-Parikh word of length \(38\), \(40\), \(42\), or \(44\) has a self-shuffle coloring with color-run bound at most \(4\); moreover, \(38\) is the least positive even \(T\) for which every smooth even-Parikh word at the four lengths \(T,T+2,T+4,T+6\) has such a coloring. There is a smooth even-Parikh word of length \(38\) with no color-run-three self-shuffle coloring. The last two finite assertions do **not** assert that the infinite bound \(4\) is optimal.

## Assumptions and scope

A word \(w\) is *even-Parikh* when \(|w|_1\) and \(|w|_2\) are both even. Each nonempty even-Parikh word decomposes uniquely into *parity atoms* by cutting after every prefix whose two counts are even. For an infinite smooth word, the hypothesis is that such cut positions occur infinitely often. A right-infinite word is smooth when all its finite factors are smooth. An infinite self-shuffle coloring must produce two identical right-infinite words, not just equal finite prefixes at some selected cut positions.

For a nonempty word \(w\), its run-length list \(r_1\cdots r_h\) records the lengths of maximal runs of identical letters. Its finite derivative \(D(w)\) is undefined if any \(r_i>2\). Otherwise delete \(r_1\) if it equals \(1\), then delete the final surviving entry if it equals \(1\). In particular, \(D(w)\) is a word over \(\{1,2\}\) or empty.

## Proof

**1. Uniform parity-atom bound.** The ten smooth parity atoms are

`11`, `22`, `1212`, `1221`, `2112`, `2121`, `121121`, `212212`, `12112212`, `21221121`.

For a parity atom starting with \(1\), an initial `11` immediately ends the atom. Otherwise its first two letters are `12` and its remaining even-length blocks, until first parity return, must be an alternating sequence of double-letter blocks `11`, `22`, followed by a final `12` or `21`. The run-length-three prohibition fixes the first internal block and forces alternation. Zero, one, and two internal blocks give precisely `1212`, `1221`, `121121`, `12112212`. With at least three internal double blocks, the first derivative contains a `222` factor and so the atom is not smooth. Complementing letters supplies the remaining possibilities. Hence each atom has even length at most \(8\). This is also the atom lemma of [1, Section 3], here with its substantive argument made explicit.

Smoothness is inherited by factors: the derivative of a factor is a factor of the derivative of its parent, after possible boundary trimming, so induction on derivative height proves factoriality; see [1, Lemmas 2.1–2.2].

**2. Exact finite four-run certificate.** The file `four_run_witnesses.tsv` gives one coloring for every smooth even-Parikh word of each length \(38,40,42,44\). The respective counts are \(538,674,682,870\), totaling \(2764\). The verifier `verify_four_run.py` independently reconstructs all \(22194\) nonempty smooth words through length \(44\) by (i) prefix extension and direct repeated differentiation, and (ii) complete inversion of the finite derivative. It checks equality of these sets and equality of the target sets with the certificate's word column, then directly checks that each coloring's two subsequences agree and every monochromatic run has length at most \(4\). All finite operations are exhaustive; no sampling or extrapolation is used.

Completeness of inverse differentiation follows because every nonempty smooth word either has empty derivative (then it is one of `1`, `2`, `12`, `21`) or has a shorter nonempty smooth derivative. For a prescribed nonempty derivative \(u\), the entire preimage consists of alternating runs with lengths `u`, with an optional leading `1` run precisely if \(u\) begins with `2` (otherwise required), and similarly for the trailing `1` run; either initial letter is allowed. This is exactly the generator implemented in the verifier. Prefix-extension completeness follows from factoriality. The independent agreement serves as a further implementation check.

**3. Constructing an infinite coloring.** Begin at prefix position zero. Because the even-Parikh prefix cuts continue infinitely, take the first later cut whose distance from the current cut is at least \(38\). The previous cut was at even distance at most \(36\), and the last parity atom has length at most \(8\). Thus the chosen block length is one of \(38,40,42,44\). Each block is smooth by factoriality and even-Parikh by subtraction of even count vectors. By Step 2 it has a coloring with run bound at most \(4\). Independently swapping the colors in any block does not alter the common self-shuffle root. Orient each successive block so that its first color differs from the previous block's last color. The resulting infinite coloring has no color run crossing a block boundary, hence its global run bound is at most \(4\). Both induced infinite subsequences are the concatenation of the blocks' common roots in the same order, and each block contributes a nonempty root, so they are equal right-infinite words.

The classical Kolakoski sequence is smooth and has infinitely many even-Parikh prefixes by [1, Section 6]. For completeness, the latter fact also follows by grouping its letters into aligned pairs: every second mixed pair forces a return to even parity. If only finitely many mixed pairs existed, eventually all pairs would be homogeneous `11`/`22`. The run-length restriction would force alternating homogeneous pairs, giving eventual run lengths all \(2\), contradicting its self-run-length definition.

**4. Sharpness of the finite window.** The `four_run_lower_bound.tsv` file supplies one exact obstruction at each of lengths \(4,8,10,12,14,16,18,20,24,28,36\) for color-run bound \(4\). Every four-consecutive-even-length window beginning at a positive even \(T<38\) contains at least one of these obstructed lengths. The same file supplies a length-\(38\) smooth even-Parikh word obstructing color-run bound \(3\). For each obstruction, `verify_four_run.py` enumerates *all* prefix-comparable partial two-stream assignments with the indicated run bound; the state consists of the leading stream color, its unmatched suffix, the last color, and the current run length. A word has a valid coloring exactly when an empty residual state remains after its last letter. The exhaustive check establishes the negative claims; finite search failure without exhaustive state closure would not suffice.

## Verification

From the folder containing the embedded files, run `python3 verify_four_run.py`. It prints:

```
independent smooth-word generators agree: 22194
witnesses verified: 2764 {38: 538, 40: 674, 42: 682, 44: 870}
obstruction witnesses verified: 12 and all shorter four-length windows are obstructed
PASS
```

The supplied positive colorings are independently replayed against the original words; the full verifier needs Python 3.10 or later, standard library only. `verification_output.txt` records the actual execution. No finite computation is used as a substitute for the infinite parity-atom/concatenation proof.

## Relationship to prior work

Kilpatrick [1] proves the eventual shuffle-square property of smooth even-Parikh words, the parity-atom bound \(8\), and a color-run bound \(48\) for the infinite Kolakoski word. Zwierzyński [2] independently proves the even-Parikh shuffle-square classification and its generalization to finite differentiability levels; his exact residual-state test (Section 2.1) does not impose color-run bounds. Henshall, Rampersad and Shallit [3] introduced shuffle squares. The present finite controlled-color certificate and orientation argument establish the stronger uniform bound \(4\), as well as the sharp finite-window threshold \(38\). No new claim is made about the established parity-atom classification, original shuffle-square existence theorem, or Kolakoski prefix criterion.

## Limitations

The bound \(4\) is an upper bound for the infinite Kolakoski coloring, not a proven optimal infinite bound. The threshold \(38\) is optimal only for the specified method of requiring *every* smooth even-Parikh word in four consecutive even lengths to have a four-run coloring. The theorem does not apply to arbitrary binary words, arbitrary finitely differentiable words, or smooth infinite words without the infinitely many even-Parikh cut condition. Publication priority may be affected by unindexed work on bounded-run shuffles. The computation was reproduced and checked within the supplied artifacts; independent external mathematical audit has not been performed.

## References

[1] Kory Kilpatrick, *Shuffle squares in smooth binary words and the Kolakoski sequence*, arXiv:2610.02262, first submitted 2026-10-01, https://arxiv.org/abs/2610.02262. In particular, Sections 2–6 and Corollary 6.2.

[2] Michał Zwierzyński, *Shuffle Squares in Differentiable Words*, arXiv:2610.07828, first submitted 2026-10-06, https://arxiv.org/abs/2610.07828. In particular, Sections 1–2 and the finite-differentiability results.

[3] David Henshall, Narad Rampersad and Jeffrey Shallit, *Shuffling and unshuffling*, Bulletin of the European Association for Theoretical Computer Science 107 (2012), 131–142.
