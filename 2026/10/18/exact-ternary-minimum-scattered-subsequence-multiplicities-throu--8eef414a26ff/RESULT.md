# Exact ternary minimum scattered-subsequence multiplicities through length 16

## Finding
For a finite word \(w\), define \(\operatorname{occ}(w,u)\) to be the number of strictly increasing position sequences spelling the scattered subsequence \(u\), including \(\operatorname{occ}(w,\varepsilon)=1\). For \(n\ge1\), put
\[
F_3(n)=\min_{w\in\{0,1,2\}^n}\max_{u\in\{0,1,2\}^*}\operatorname{occ}(w,u).
\]
The exact initial values and *all* minimizing words modulo alphabet relabeling are determined for \(1\le n\le 16\). The complete canonical word lists are in `data/census.json`.

| Length | Minimum maximal multiplicity | Canonical optimizers | Representative |
|---:|---:|---:|---|
| 1 | 1 | 1 | `0` |
| 2 | 1 | 1 | `01` |
| 3 | 1 | 1 | `012` |
| 4 | 2 | 7 | `0012` |
| 5 | 2 | 5 | `01102` |
| 6 | 2 | 1 | `012210` |
| 7 | 3 | 2 | `0122201` |
| 8 | 5 | 10 | `01102201` |
| 9 | 6 | 26 | `011022201` |
| 10 | 8 | 12 | `0121020021` |
| 11 | 9 | 1 | `01222100012` |
| 12 | 15 | 9 | `012102021012` |
| 13 | 18 | 10 | `0122111200012` |
| 14 | 24 | 1 | `01221000021120` |
| 15 | 33 | 1 | `012221000211120` |
| 16 | 46 | 4 | `0122100102021120` |

In particular, \(F_3(16)=46\); there are exactly 4 canonical minimizers at this length. The optimization allows words that use fewer than three symbols; this is included in the exhaustive count.

## Assumptions and scope
The alphabet is the fixed three-letter set \(\{0,1,2\}\), words are linear (not cyclic), subsequence occurrences are indexed by increasing position tuples, and empty subsequences are allowed with multiplicity one. No equivalence under word reversal is imposed; only bijective alphabet relabeling is used to report minimizers. The result concerns the complete contiguous length range \(1\le n\le 16\), and nothing beyond that range.

## Proof
For any word \(v\), final letter \(a\), and nonempty pattern \(u\), decompose an occurrence in \(va\) by whether it uses its final position. The resulting exact recurrence is
\[
\operatorname{occ}(va,u)=\operatorname{occ}(v,u)+\mathbf{1}_{u=u'a}\operatorname{occ}(v,u'),
\]
where the second term exists precisely when \(u\) ends in \(a\). The empty pattern has multiplicity one. Starting from the empty word, this recurrence computes **all** positive-multiplicity patterns and their exact integer multiplicities by induction on the word length. Thus their largest value is exactly \(\max_u\operatorname{occ}(w,u)\), without any restriction on pattern length other than the automatic bound \(|u|\le|w|\).

Any ternary word admits a unique restricted-growth encoding under alphabet bijections: label the first new symbol \(0\), the next unseen symbol \(1\), and the third unseen symbol \(2\). Consequently a canonical prefix can be extended only by an already introduced symbol or the next unused symbol (if fewer than three have appeared). The depth-first enumeration in `census.cpp` follows **every** such extension. The normalization preserves the multiplicity of each subsequence under the corresponding symbol bijection, so optimizing over canonical words is equivalent to optimizing over all \(3^n\) ternary words.

Patterns are encoded without collisions as strings of digits \(1,2,3\) in base four, with a 64-bit key, and the multiplicity arrays are merged in increasing key order when a letter is appended. Up to \(n=16\), the key uses at most \(32\) bits, and the largest possible subsequence count is at most \(\binom{16}{\lfloor 16/2\rfloor}\), within the implementation's unsigned integer capacity. Each canonical word contributes exactly once to the minimum and optimizer count; the program explicitly compares the resulting values, canonical totals and optimizer numbers with the table. The exact source file and full data are part of the result.

## Verification
Compile the standalone exhaustive enumerator with `g++ -O3 -std=c++17 census.cpp -o census` and execute `./census`. Its exact integer output includes all optimum canonical words and a final `CENSUS_VERIFY_OK` indicator; a mismatch makes it return nonzero. The separately implemented `verify_independent.py` enumerates position subsets directly for **every** canonical word through length nine and directly checks every displayed minimizing word at longer lengths. This independent implementation does not call the primary recurrence, and its checked values agree with the table. Counts of canonical words also equal \(\sum_{j=1}^3 S(n,j)\), with \(S\) the Stirling numbers of the second kind; the exact counts are recorded in `data/census.json`.

## Relationship to prior work
W. Fang, *Maximal number of subword occurrences in a word* (arXiv:2406.02971, first submitted June 5, 2024), defines this minimax quantity for arbitrary alphabet sizes and proves general bounds and limit existence, but reports its exhaustive minimizing-word table for the **binary** alphabet, not the ternary alphabet. The present result is the full first nonbinary length range through \(16\), including the optimizer sets; it does not claim novelty for the underlying recurrence, the definition, or the binary data. General expectation lower bounds in Fang's work are strict for several values in this table and do not determine the new exact minima. Other investigations of scattered-subsequence counting concern different statistics or individual fixed patterns rather than this ternary minimax profile.

## Limitations
The values above are finite, exact results; they do not imply a closed expression for \(F_3(n)\) for arbitrary \(n\), asymptotic rate, eventual optimizer structure, or computational tractability in large length. Literature searches reduce but do not eliminate the possibility of earlier equivalent finite tables, especially in unindexed program outputs.

## References
1. W. Fang, *Maximal number of subword occurrences in a word*, arXiv:2406.02971v1 (June 5, 2024); updated version v3 (May 14, 2025), Sections 2, 3, 5 and Tables 1–2. https://arxiv.org/abs/2406.02971
2. W. Fang, *Maximal Number of Subword Occurrences in a Word*, AofA 2024, LIPIcs 302, 3:1–3:12 (July 18, 2024). https://doi.org/10.4230/LIPIcs.AofA.2024.3
