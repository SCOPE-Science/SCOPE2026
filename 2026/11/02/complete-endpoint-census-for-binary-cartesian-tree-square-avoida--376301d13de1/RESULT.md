# Complete endpoint census for binary Cartesian-tree square avoidance

## Finding

Fix the ordered binary alphabet \(\{0<1\}\). A *Cartesian-tree square* is a contiguous factor \(uv\) for which the two equal-length halves \(u\) and \(v\) have the same ordered, unlabeled Cartesian-tree shape, with ties broken by selecting the leftmost minimum. A word is *three-plus Cartesian-tree-square-free* if it has no such factor with \(|u|=|v|\geq 3\).

**Theorem (endpoint classification).** The maximum length of such a binary word is \(29\), and there are exactly \(20\) words of that length, counted as distinct ordered-alphabet words without quotienting by reversal or complement. All \(20\) agree with the length-\(29\) template

```
110--11010--1101010--110101--
```

where the eight dashes are at one-based positions \(4,5,11,12,20,21,28,29\). Write the symbols in those positions, from left to right, as an eight-bit string. The **complete list** of admissible eight-bit strings is described by the following eight disjoint rules:

| First six variable bits | Permitted final two variable bits | Number |
| --- | --- | ---: |
| `000100` | `00`, `01`, `10` | 3 |
| `000111` | `10` | 1 |
| `001100` | `00`, `01`, `10` | 3 |
| `001101` | `10` | 1 |
| `010001` | `00`, `01`, `10` | 3 |
| `010011` | `00`, `01`, `10` | 3 |
| `110001` | `00`, `01`, `10` | 3 |
| `110011` | `00`, `01`, `10` | 3 |
| **Total** | | **20** |

The complete sorted list of the \(20\) words appears in `extremal_words.txt`. The theorem is a classification of **all** maximum-length witnesses, not a new claim that the maximum length is \(29\): the latter appeared in Shibata et al. (2026).

## Assumptions and scope

A word means a finite sequence over the **fixed ordered** alphabet \(\{0<1\}\). For the empty word put \(\operatorname{CT}(\epsilon)=\emptyset\). For nonempty \(w\), find the first position \(i\) where the minimum symbol occurs, and define its ordered Cartesian-tree shape recursively from the left factor, root at \(i\), and right factor. We compare ordered tree **shapes**, ignoring root labels. In particular, reversing or complementing a binary word is **not** presumed to preserve the relation, so both operations are excluded from the census quotient.

For any integer \(m\geq3\), a forbidden factor is a contiguous block \(uv\) of length \(2m\), with \(|u|=|v|=m\) and \(\operatorname{CT}(u)=\operatorname{CT}(v)\). No restriction is placed on factors of shorter half-length. The theorem concerns every word over this binary alphabet, not just a particular morphic family.

## Proof

**Exhaustive recurrence.** Let \(F_0=\{\epsilon\}\). For \(n\geq1\), form \(F_n\) from each word \(x\in F_{n-1}\) by independently appending the two symbols and retaining \(xc\) if and only if, for each \(3\leq m\leq \lfloor n/2\rfloor\), the suffixes \((xc)[n-2m:n-m]\) and \((xc)[n-m:n]\) have different Cartesian-tree shapes. The ranges use zero-based, right-exclusive slice notation.

This recurrence is **exact** by induction on \(n\). If a word is valid, deleting its last letter leaves a valid word and the only newly introduced forbidden factors end at its last position. Conversely, a retained extension has no old forbidden factor (by induction), and the suffix tests eliminate every new one. Therefore \(F_n\) is precisely the set of valid length-\(n\) words. There is no random sampling or heuristic truncation.

**Deciding tree equality.** The function `ct` in `cartesian_enumerate.py` implements the recursive leftmost-minimum rule literally and represents a tree by the triple (root index, left subtree shape, right subtree shape). Because the ordered subtree sizes determine the root index, equality of these triples is exactly ordered-tree-shape equality. Caching changes only runtime, not the recursion.

**Finite counts and structural classification.** Executing the recurrence through \(n=30\) gives the following exact final layers:

\[
|F_{26}|=156,\quad |F_{27}|=107,\quad |F_{28}|=56,\quad |F_{29}|=20,\quad |F_{30}|=0.
\]

The full layer-count vector for \(n=1,\ldots,30\) is in `tree_run.txt`. From \(F_{30}=\varnothing\) and prefix closure, no valid word has length \(30\) or greater. Directly scanning every coordinate of the complete \(F_{29}\) produces exactly the displayed \(21\)-fixed-position template, and projection to the remaining eight positions yields the eight disjoint rules. Each rule reconstructs valid words already in \(F_{29}\), and the rules cover every element of this exhaustively generated set. This proves both sharpness and the claimed census.

**Independent representation and finite rerun.** By Park et al. (2019, Theorem 3.2), two strings Cartesian-tree match if and only if their *parent-distance* sequences match. For a word \(w\), define \(\operatorname{PD}(w)_i=0\) when no earlier position has symbol at most \(w_i\); otherwise let \(j\) be the last preceding position with \(w_j\leq w_i\) and put \(\operatorname{PD}(w)_i=i-j\). The separate program `parent_distance_check.py` computes this sequence by a monotone stack instead of constructing trees. It independently generates all prefix layers and checks all possible long factors inside each of the \(20\) extremizers. Its complete layer counts and sorted endpoint-word digest match the tree-recursion program exactly. Thus the critical equivalence implementation has a representation-independent check.

## Verification

With Python 3, run both standalone files in the same directory:

```
python3 cartesian_enumerate.py
python3 parent_distance_check.py
```

Each prints the full \(30\)-layer count vector and ends in, respectively, `CARTESIAN_ENUMERATION_OK` and `PARENT_DISTANCE_CHECK_OK`. Both report the SHA-256 digest of the sorted list of all \(20\) length-\(29\) words, each word followed by a newline:

```
fa7a68bf7155a80ca632847616541706160392ee2d4492e90c3310f1787da79a
```

The actual recorded outputs appear in `tree_run.txt` and `pd_run.txt`. The complete word list and the compact template classification are also supplied separately; no external packages or inputs are required.

## Relationship to prior work

Shibata, Mieno, Köppl and Inenaga, *Relaxation of Square-Freeness* (arXiv:2607.00674, first posted July 1, 2026), already list \(29\) as the greatest length of a binary three-plus Cartesian-tree-square-free word and print one extremal word. Their Table 1 and Table 2 do **not** give the number of maximum-length words, their shared-position template, or their complete classification. This finding adds precisely that endpoint census and rigidity statement; the prior maximum-length result is background rather than a new discovery.

Park, Amir, Landau and Park, *Cartesian Tree Matching and Indexing* (arXiv:1905.08974), define the stable leftmost-minimum Cartesian-tree relation and prove equivalence with the parent-distance representation (Theorem 3.2). The latter supplies an independent formulation of the matching test, not a census of repetition-avoiding extremizers.

## Limitations

The classification is a finite, computer-assisted exhaustive result. Its proof rests on two included complete algorithms and finite replay, not on a closed-form noncomputational argument for the count \(20\). It does not settle the open three-plus question for larger alphabets, nor the four-plus binary case. It does not classify near-extremal words of every smaller length. An implicit enumeration in code or literature not fully accessible here cannot be ruled out.

## References

1. H. Shibata, T. Mieno, D. Köppl, S. Inenaga, *Relaxation of Square-Freeness*, arXiv:2607.00674 (first public version July 1, 2026), https://arxiv.org/html/2607.00674 . Tables 1 and 2, and the accompanying discussion of generalized squares.
2. S. G. Park, A. Amir, G. M. Landau, K. Park, *Cartesian Tree Matching and Indexing*, arXiv:1905.08974, https://arxiv.org/abs/1905.08974 . Definition of the leftmost-minimum Cartesian tree in §2.2 and parent-distance equivalence in Theorem 3.2.
