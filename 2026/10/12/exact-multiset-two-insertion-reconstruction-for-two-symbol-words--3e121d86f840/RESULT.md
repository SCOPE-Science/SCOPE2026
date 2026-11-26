# Exact multiset two-insertion reconstruction for two-symbol words

## Finding

For an alphabet of size \(q\ge2\), the largest intersection of the exact-two-insertion multiset spheres of distinct length-two words is \(N_q^{\mathrm m}(2,2)=8q-5\). The binary maximum \(11\) is already reported in [2, Table II]. The formula here holds for all alphabets, and the unordered maximizers are exactly \(\{aa,ab\}\) and \(\{aa,ba\}\), for distinct \(a,b\). There are exactly \(2q(q-1)\) such labeled unordered pairs. In the exact-two-insertion model with distinct insertion vectors across channels, the sharp universal reconstruction threshold from the multiset of outputs is \(8q-4\).

## Assumptions and scope

Let \(\Sigma\) be an alphabet with \(|\Sigma|=q\ge2\); no field structure is assumed. A source word \(x=(x_1,x_2)\) receives exactly two letters, placed in the three gaps before, between, and after its original letters. Different gap words of total length two count as different insertion vectors even if they produce the same four-letter output. The original characters are retained in order. Deleting the inserted positions gives the multiplicity of an output \(y\):
\[
e_x(y)=\sum_{1\le i<j\le4}\mathbf 1\{(y_i,y_j)=(x_1,x_2)\}.
\]
Writing \(M_2(x)\) for this multiset sphere, the intersection size is
\[
I_q(x,z)=\lvert M_2(x)\cap M_2(z)\rvert=\sum_{y\in\Sigma^4}\min(e_x(y),e_z(y)).
\]
This is not the intersection of ordinary sets of insertion outputs, nor the corresponding model with a mixture of insertion counts or the non-multiset reconstruction model.

## Proof

Renaming alphabet symbols does not affect subsequence embeddings. Thus \(I_q(x,z)\) depends only on the equality pattern of the four positions \((x_1,x_2,z_1,z_2)\). Encode each pattern as a restricted-growth tuple \(p\), starting with \(p_1=0\) and giving each new symbol the smallest unused index. Of the 15 set partitions of four positions, exactly two encode identical centers, leaving 13 patterns.

Fix a pattern using \(s\) symbols, with support \(S=\{0,\ldots,s-1\}\). Let \(C_p\) be the sum of minimum multiplicities over \(y\in S^4\); let \(E_p\) be the corresponding sum over \(y\in(S\cup\{s\})^4\) with exactly one occurrence of \(s\), a fixed outsider. If \(y\) has at least two positions outside \(S\), at most two positions remain for an embedding of either center. Both embeddings would then use the same two positions, which would force identical centers. So such outputs contribute zero. With renaming symmetry for the choice of the single outsider, for every \(q\ge s\) we have \(I_q=C_p+(q-s)E_p\).

For each pattern the coefficients are calculated by summing the above embedding multiplicities over the indicated finite sets. The full enumeration is:

| Restricted-growth pattern | \(s\) | \(C_p\) | \(E_p\) | \(I_q\) |
|:--|--:|--:|--:|:--|
| `0001`, `0010`, `0100`, `0111` | 2 | 11 | 8 | \(8q-5\) |
| `0110` | 2 | 10 | 8 | \(8q-6\) |
| `0011` | 2 | 6 | 0 | \(6\) |
| `0102`, `0121` | 3 | 18 | 8 | \(8q-6\) |
| `0112`, `0120` | 3 | 12 | 4 | \(4q\) |
| `0012`, `0122` | 3 | 6 | 0 | \(6\) |
| `0123` | 4 | 6 | 0 | \(6\) |

The largest entry is \(8q-5\) for every \(q\ge2\), strictly above every other admissible expression. Its patterns are exactly the pairs consisting of a constant word \(aa\) and a word containing a single \(a\) and one different \(b\). Choosing \(a,b\) in order and choosing the order of the nonconstant word gives \(2q(q-1)\) different unordered pairs, because the constant word is unique in each pair.

Any two distinct centers realize a common output multiset of size precisely their intersection size, by choosing for each output the minimum common multiplicity. For each center separately, its distinct insertion vectors producing a given output suffice for the selected multiplicity, and each vector produces only one output. No larger multiset can be common. A maximizing pair therefore witnesses ambiguity at \(8q-5\) observations, and none can do so at \(8q-4\).

## Verification

The standard-library `verify.py` enumerates the complete set of 13 patterns, evaluates \(C_p,E_p\), checks the affine relation on four alphabet sizes per pattern, and directly checks all unordered center pairs for \(q=2,3,4,5,6\). The proof for arbitrary \(q\) uses the support reduction and the complete finite pattern table, not extrapolation from those alphabet sizes.

## Relationship to prior work

Junnila et al. [2, §II-A, equations (3)–(4)] define the multiplicity-sensitive intersection and extremal size in this model. Example 4 gives \(I_2(01,11)=11\), and Table II separately gives the exact computer-searched binary maximum \(N_2^{\mathrm m}(2,2)=11\). The binary maximum and its consequent threshold are not new. Theorem 27 assumes \(n\ge3\); Theorem 28 gives a recursive upper bound applicable to \(n=2,t=2\), but it does not determine the maximum at these parameters or classify ties. The distinct contributions here are the exact dependence on the alphabet size and the full equality classification. The related ISIT article [3] concerns insertion-error diversity; overlap could not be resolved from its full text, which was not available for inspection. No claim about the non-multiset threshold or ordinary set intersections is made.

## References

1. V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *On Levenshtein's Reconstruction Problem for Channels with Unique Insertion Error Patterns*, IEEE ITW (2025), DOI `10.1109/ITW62417.2025.11240278`.
2. V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *Unique Insertion Error Patterns in Levenshtein's Reconstruction Problem*, arXiv:`2607.06181`, especially §II-A, Example 4, Table II and Theorems 27–28.
3. V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *Number of Channels with Different Insertion Errors Required for the Levenshtein's Reconstruction Problem*, IEEE ISIT (2026), DOI `10.1109/ISIT62367.2026.11653882`.
