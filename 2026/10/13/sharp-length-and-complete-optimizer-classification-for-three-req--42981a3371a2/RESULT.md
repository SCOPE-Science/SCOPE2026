# Sharp length and complete optimizer classification for three-request asynchronous binary batch codes

## Finding

For binary linear encoders with three named message coordinates and three simultaneously active recovery processes, the minimum number of stored coordinates permitting asynchronous recovery is exactly \(8\). Here asynchronous recovery means an adaptive algorithm can serve any requested message coordinate whenever fewer than three recovery processes remain active, despite arbitrary completions of earlier processes.

At length \(8\), with zero generator columns omitted and generator-column permutations identified, exactly **79** column multisets permit such recovery. All \(79\) admit a selection of minimal recovery sets making the encoder **three-strongly online** (and hence strongly asynchronous). Under the additional equivalence of permuting the three message coordinates, the \(79\) column multisets form exactly **17** classes: ten orbits of size \(6\), six of size \(3\), and one of size \(1\). This statement classifies generator matrices with the three named message coordinates, not abstract row spaces modulo arbitrary changes of information basis.

The multiplicity signatures of the \(79\) column multisets are: \(48\) instances of \((1,1,1,1,2,2)\), \(24\) instances of \((1,1,2,2,2)\), and \(7\) instances of \((1,1,1,1,1,1,2)\). An explicit optimal encoder has columns \((1,1,2,2,4,5,6,7)\), with integer column labels understood as binary vectors.

The following table gives all \(17\) orbit representatives; ``orbit size'' counts distinct column multisets after permuting named message coordinates:

| Orbit size | Generator-column labels |
| ---: | --- |
| 3 | 1, 1, 2, 2, 4, 5, 6, 7 |
| 6 | 1, 1, 2, 2, 5, 5, 6, 7 |
| 3 | 1, 1, 2, 2, 5, 6, 7, 7 |
| 3 | 1, 1, 2, 3, 4, 5, 6, 7 |
| 6 | 1, 1, 2, 3, 4, 6, 6, 7 |
| 6 | 1, 1, 2, 3, 4, 6, 7, 7 |
| 6 | 1, 1, 2, 3, 5, 5, 6, 7 |
| 6 | 1, 1, 2, 3, 5, 6, 6, 7 |
| 6 | 1, 1, 2, 3, 5, 6, 7, 7 |
| 6 | 1, 1, 2, 5, 5, 6, 6, 7 |
| 6 | 1, 1, 2, 5, 5, 6, 7, 7 |
| 3 | 1, 2, 3, 3, 4, 5, 5, 7 |
| 3 | 1, 2, 3, 3, 4, 5, 6, 7 |
| 6 | 1, 2, 3, 3, 4, 5, 7, 7 |
| 1 | 1, 2, 3, 4, 5, 6, 7, 7 |
| 6 | 1, 2, 3, 5, 5, 6, 7, 7 |
| 3 | 1, 2, 5, 5, 6, 6, 7, 7 |

The accompanying `witnesses.json` contains all \(79\) column multisets and a checked strongly-online recovery-set selection for each.

## Assumptions and scope

Work over \(\mathbb F_2\), with messages \((u_1,u_2,u_3)\) and a full-row-rank \(3\times n\) generator matrix \(G\). Encode its columns by integers \(1,\ldots,7\) using their three binary bits, so that labels \(1\), \(2\), and \(4\) denote the three unit vectors. A recovery set for request \(i\) is a set of storage positions whose column span contains the corresponding unit vector. Every recovery set is taken inclusion-minimal, as in the cited recovery model.

For the asynchronous property, an algorithm chooses a minimal recovery set disjoint from those still active for any arriving request, at all times with fewer than \(3\) active processes. A strongly-online selection is one nonempty family \(\mathcal R\) of minimal recovery sets whose entire set of pairwise-disjoint histories of at most two members can be extended by a member of \(\mathcal R\) for each of the three request labels. The theorem concerns **all** full-rank binary generator matrices, not solely systematic matrices or constructions from graphs.

Zero columns cannot occur in an inclusion-minimal recovery set. Removing zero columns therefore preserves every relevant recovery model. It suffices to enumerate matrices without zero columns for the sharp length and classification. The classification of length-eight matrices with redundant zero columns is excluded by the no-shorter-code result.

## Proof

**Minimal-recovery lemma.** If \(R\) is minimal for a unit vector in a three-dimensional binary column space, the columns in \(R\) are linearly independent: a dependence would permit dropping a participating column without changing their span. Thus \(|R|\le3\). In an independent binary family, the unique expression for the target unit vector uses every column, since otherwise a proper subset would recover it. Hence \(R\) is minimal for request \(i\) exactly when its column-label XOR is \(2^{i-1}\) and no proper subset has the same XOR. The verifier enumerates precisely these subsets using position masks and all proper submasks; no rank heuristic or random sampling is involved.

**Exchange-core lemma.** Let \(\mathcal T\) be the set of all triples of pairwise-disjoint minimal recovery sets, each member retaining its unique request label. For any subfamily \(\mathcal U\subseteq\mathcal T\), remove every triple for which some two-member face has no completion within \(\mathcal U\) of one of the three request labels. Repeat until the family stabilizes. Each removal is forced in any exchange-closed subfamily: if the face has no valid completion of a required label inside the current family, no smaller subfamily containing that triple has the exchange property. By induction, the fixed point contains every exchange-closed subfamily. Conversely a nonempty fixed point has the exchange property by construction. The exchange characterization of asynchronous histories (Düzgün and collaborators, Theorem IV.11 and Corollary IV.12) therefore makes nonemptiness of this fixed point **equivalent**, not merely sufficient, to asynchronous recovery. This is also immediate from the subset-closed-history extension characterization (their Theorem IV.10).

**Finite, exhaustive classification.** Column reordering does not alter any property, so every nonzero-column matrix of length \(n\) has a unique nondecreasing column sequence drawn from seven possible labels. There are \(\binom{13}{6}=1716\) sequences for \(n=7\) and \(\binom{14}{6}=3003\) for \(n=8\). For each sequence the verifier constructs all minimal recovery subsets, enumerates all disjoint complete histories, and computes the greatest exchange-closed core by the preceding lemma. The complete length-seven enumeration yields zero nonempty cores; the complete length-eight enumeration yields precisely \(79\). Since appending an unused column preserves the asynchronous property, no shorter length can support a code if none does at length seven.

**Strongness and classification certificates.** For each of the \(79\) surviving length-eight sequences, `witnesses.json` supplies a nonempty set \(\mathcal R\) of selected position masks. The verifier independently checks that each selected set is an inclusion-minimal recovery set, that all three request labels occur, and that every disjoint chosen history of size zero, one or two extends to a chosen disjoint recovery set for every label. Thus all \(79\) are three-strongly online; Theorem IV.17 of the cited model identifies their strong asynchronous property. The verifier then performs all six possible permutations of the three message bits and obtains \(17\) orbits, with orbit sizes \(6\) (ten times), \(3\) (six times), and \(1\) (once), and tallies the three multiplicity signatures above. The program and 79 explicit witnesses together constitute a reproducible finite proof of every asserted count.

## Verification

Place `verify.py` and `witnesses.json` in the same directory and run `python3 verify.py` using Python 3.10 or newer; only the standard library is used. The output is:

`VERIFY_OK: n=7 none; n=8 exactly 79 in 17 message-permutation classes; all 79 strong witnesses; profiles 48+24+7`

All \(1716+3003=4719\) nonzero-column multisets are enumerated, with no asymptotic extrapolation or partial search. The stated lower bound uses the exact finite exhaustion plus monotonicity, rather than treating a failed optimizer call as nonexistence.

## Relationship to prior work

Düzgün, Hollmann, Riet, Skachek and Taranchuk (2026) formalize online, asynchronous and strongly-online recovery, including the complete-history exchange criterion used here. Their Example IV.22 already provides a three-strongly-online eight-column generator, with column-label multiset \((1,2,3,4,5,6,7,7)\); **the existence of an eight-column example is not new**. The present additional results are the sharp lower bound against all seven-column matrices, full enumeration of every eight-column asynchronous encoder, the orbit structure, and the fact that each optimum admits a strongly-online selection.

Riet, Skachek and Thomas (2018/2022) establish the foundational asynchronous batch-code model and study constructions and general redundancy bounds. Their concluding questions expressly include the shortest asynchronous lengths at specific small dimensions; their discussed special exact bounds predominantly concern two requests. Neither inspected work provides this full eight-column classification. An earlier publicly indexed result concerning four-request all-symbol batch capacity in dimension three instead addresses a different recovery condition, so its bound does not determine three-request asynchronous feasibility.

## Limitations

These conclusions concern the binary field, exactly three message coordinates, exactly three active recovery processes, and **labeled generator matrices** up to stored-coordinate permutation (and, for the orbit count only, message-coordinate permutations). They do not classify code row spaces under arbitrary nonsingular changes of the information basis, and do not establish an equivalence between asynchronous and strongly-online recovery for longer codes or larger parameters. The computational verification is exhaustive only over the precisely stated finite ranges. Unindexed historical classifications remain a possible prior-art risk; independent scientific review has not been performed.

## References

1. B. Düzgün, H. D. L. Hollmann, A.-E. Riet, V. Skachek, V. Taranchuk, "Recovery Models for Linear Batch Codes," arXiv:2605.09748, first submitted 10 May 2026. https://arxiv.org/html/2605.09748v2 ; https://arxiv.org/abs/2605.09748
2. A.-E. Riet, V. Skachek, E. K. Thomas, "Batch Codes for Asynchronous Recovery of Data," arXiv:1806.00592, https://arxiv.org/html/1806.00592v3
