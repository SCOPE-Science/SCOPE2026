# Exact quaternary four-letter deletion covering and its half-integral relaxation

## Finding

For the ordered four-symbol alphabet \(\Sigma=\{0,1,2,3\}\), let \(\Delta(w)\) be the **set of distinct** length-three subsequences obtained by deleting exactly one position from a word \(w\in\Sigma^4\). A single-deletion covering code is a set \(C\subseteq\Sigma^4\) satisfying \(\bigcup_{w\in C}\Delta(w)=\Sigma^3\). The minimum possible size is exactly
\[
\boxed{D(4,4,1)=19.}
\]
Furthermore, the fractional set-cover relaxation of this same incidence problem has optimum exactly \(37/2\). Thus the integer optimum is the ceiling of a tight half-integral fractional bound.

## Assumptions and scope

Symbols are labeled, positions are ordered, and only **exactly one deletion** is permitted. The output consists of every ordered length-three word over \(\Sigma\). Repeated deletions yielding the same output are counted only once. The quantity \(D(4,4,1)\) is the minimum number of length-four codewords required to cover all \(4^3=64\) outputs. No claim is made for other alphabet sizes, lengths, or multiple deletions.

## Proof

**1. A rational dual certificate.** Assign to every received word \(u=(a,b,c)\in\Sigma^3\) the nonnegative weight
\[
y(u)=\begin{cases}
1/2,&a=b=c,\\
1/8,&a=c\ne b,\\
3/8,&a=b\ne c\text{ or }a\ne b=c,\\
1/4,&a,b,c\text{ pairwise distinct.}
\end{cases}
\]
The four classes contain respectively \(4,12,24,24\) output words. Their total weight is
\[
4(1/2)+12(1/8)+24(3/8)+24(1/4)=37/2.
\]
For every four-letter word \(w\), \(\sum_{u\in\Delta(w)}y(u)\le1\). To check this for all 256 possibilities without relying on empirical sampling, note that the weights and incidence relation are invariant under **every permutation of the four symbols**. Two words are in the same orbit exactly when they have the same equality pattern, encoded by a restricted-growth string. The complete list of all fifteen length-four equality patterns and their exact rational sums is:

| Canonical pattern | Total dual weight of distinct descendants |
|---|---:|
| `0000` | \(1/2\) |
| `0001` | \(7/8\) |
| `0010` | \(1\) |
| `0011` | \(3/4\) |
| `0012` | \(1\) |
| `0100` | \(1\) |
| `0101` | \(1\) |
| `0102` | \(1\) |
| `0110` | \(7/8\) |
| `0111` | \(7/8\) |
| `0112` | \(1\) |
| `0120` | \(3/4\) |
| `0121` | \(1\) |
| `0122` | \(1\) |
| `0123` | \(1\) |

Every entry is at most one. Therefore any covering code \(C\) obeys
\[
37/2=\sum_{u\in\Sigma^3}y(u)\le\sum_{w\in C}\sum_{u\in\Delta(w)}y(u)\le |C|.
\]
Integrality yields \(|C|\ge19\).

**2. Fractional optimality, not just a lower bound.** For each length-four word \(w\), let \(r(w)\) be the restricted-growth encoding of its equality pattern (for example `3132` has pattern `0102`). Define nonnegative fractional codeword weights by
\[
x_w=\begin{cases}
1/6,&r(w)=\texttt{0012},\\
1/3,&r(w)=\texttt{0100},\\
1/3,&r(w)=\texttt{0101},\\
1/12,&r(w)=\texttt{0122},\\
3/16,&r(w)=\texttt{0123},\\
0,&\text{otherwise.}
\end{cases}
\]
The orbit sizes are \(24,12,12,24,24\), so the objective is \(24/6+12/3+12/3+24/12+24(3/16)=37/2\). Every received word has fractional coverage exactly one. The five equality-pattern orbit representatives of three-letter outputs and the numbers of four-letter supersets of each positively weighted type are:

| Received type | `0012` | `0100` | `0101` | `0122` | `0123` |
|---|---:|---:|---:|---:|---:|
| `000` | 0 | 3 | 0 | 0 | 0 |
| `001` | 4 | 0 | 1 | 0 | 0 |
| `010` | 0 | 1 | 2 | 0 | 0 |
| `011` | 0 | 1 | 1 | 4 | 0 |
| `012` | 1 | 0 | 0 | 1 | 4 |

Multiplication by the stated weights gives one in every row. Every three-letter output belongs to one of these orbits, hence the fractional covering constraints hold exactly. Dual and primal match at \(37/2\).

**3. Integral construction.** The following nineteen words constitute a covering code:

- `0010`
- `0032`
- `0213`
- `1010`
- `1012`
- `1033`
- `1131`
- `1230`
- `2020`
- `2031`
- `2121`
- `2122`
- `2323`
- `3011`
- `3022`
- `3030`
- `3132`
- `3210`
- `3313`

Taking the set of distinct one-deletion descendants of these nineteen words gives all 64 length-three words over \(\Sigma\); the embedded standalone checker verifies the complete equality. Hence \(D(4,4,1)\le19\), matching the dual lower bound.

## Verification

The standalone `artifacts/verify.py` uses only Python's standard library and exact rational arithmetic. It independently generates all 256 length-four words, all 64 length-three words and their distinct one-deletion incidences; checks the 19-word witness against all 64 outputs; verifies the dual inequality on all 256 words; enumerates all fifteen equality-pattern classes; and checks the fractional primal constraints for all 64 outputs with exact `fractions.Fraction` arithmetic. The recorded output appears in `artifacts/check_output.txt`. Run `python3 artifacts/verify.py` from any working directory after extracting the three standalone artifact files under their stated paths.

This finite exhaustive check supplements the complete orbit reduction and rational certificates. It makes no claim about alphabet sizes or word lengths outside the stated finite domain.

## Relationship to prior work

Xie, Sun and Ge (2026) formulate deletion covering as a hypergraph cover, establish general bounds and asymptotically tight behavior for growing alphabets, and give constructive methods. Their results motivate the exact small-parameter question, but do not state the quaternary length-four invariant or this fractional primal-dual certificate. Lenz, Rashtchian, Siegel and Yaakobi (2019/2020) establish broader existence and asymptotic bounds for insertion and deletion covering rather than this exact optimum. Chee, Ge and Ling (2010) study the spectrum of perfect **deletion-correcting** codes and directed packings, which are packing conditions, not the covering minimum in this theorem. The primary and indexed comparisons located no exact claim implying this result, but an unindexed earlier computation cannot be excluded.

## Limitations

The result is an exact finite statement for four labeled symbols, four transmitted positions, and one deletion. The symmetric certificates establish no all-parameter formula for deletion-covering numbers. The integer witness is one optimum, not a classification of all optima. Publication priority has not been independently certified.

## References

1. C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first publicly posted 2026-06-13. https://arxiv.org/abs/2606.15379
2. A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944, first publicly posted 2019-11-22. https://arxiv.org/abs/1911.09944
3. Y. M. Chee, G. Ge, A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, arXiv:1008.1343. https://arxiv.org/abs/1008.1343
