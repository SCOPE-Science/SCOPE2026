# Sharp initial alphabet-rank thresholds for Abelian border arrays

## Finding

For a finite word \(w\), the array \(\pi(w)\) records the length of the longest proper Abelian border of each nonempty prefix, with zero for a prefix having none. An Abelian border is a proper nonempty prefix and suffix of equal length and equal symbol counts. An array has **alphabet rank** \(r\) if the least number of distinct symbols in a word realizing it is \(r\).

**Four and five letters.** The first arrays of rank four occur at length **8**, with exactly **three** such arrays there. The first arrays of rank five occur at length **11**, with exactly **four** such arrays there. No array of length at most eleven has rank greater than five. At every length \(n\ge 11\) there is a rank-five array; the maximal rank beyond eleven is not determined here.

The exact census is given below. The rank-one through rank-three columns are included as context and consistency checks, not as new results: they follow from the prior binary and ternary cumulative censuses. In particular, the first occurrence of rank three at length four, with one array there, is already implied by those censuses.

| Length | Rank 1 | Rank 2 | Rank 3 | Rank 4 | Rank 5 | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 3 | 1 | 3 | 0 | 0 | 0 | 4 |
| 4 | 1 | 7 | 1 | 0 | 0 | 9 |
| 5 | 1 | 15 | 4 | 0 | 0 | 20 |
| 6 | 1 | 31 | 17 | 0 | 0 | 49 |
| 7 | 1 | 63 | 55 | 0 | 0 | 119 |
| 8 | 1 | 127 | 180 | 3 | 0 | 311 |
| 9 | 1 | 255 | 539 | 23 | 0 | 818 |
| 10 | 1 | 511 | 1658 | 134 | 0 | 2304 |
| 11 | 1 | 1023 | 4880 | 608 | 4 | 6516 |

## Assumptions and scope

The words are finite linear strings over any finite alphabet, and the array includes every prefix. Parikh vectors record the count of each symbol, not the ordering of the symbols. The census imposes no alphabet cutoff: a length-\(n\) word has at most \(n\) distinct letters even if its declared alphabet is larger.

## Proof

**Complete enumeration.** The equal-letter classes of any length-\(n\) word partition its positions. Relabel the classes by \(0,1,2,\ldots\) in order of first occurrence. A resulting canonical word has \(u_1=0\) and \(0\le u_i\le 1+\max_{j<i}u_j\) thereafter, and each such word represents exactly one partition. Relabeling preserves both borders and the number of letters. Thus visiting every canonical word and updating a minimum for every array includes every possible realization up to relabeling, not merely words of alphabet size at most five.

For a prefix of length \(i\), test each \(1\le\ell<i\) by comparing the Parikh vectors of positions \(1,\ldots,\ell\) and \(i-\ell+1,\ldots,i\). Record the largest successful \(\ell\) or zero. Applying this rule to each canonical word and taking the minimum letter count for its array gives the displayed census (also `CENSUS.csv`). The numbers of canonical words inspected for lengths 1 through 11 are \(1,2,5,15,52,203,877,4140,21147,115975,678570\), the corresponding Bell numbers. The supplied implementations compute the candidate Parikh vectors directly or accumulate their differences incrementally; each evaluates the entire finite domain.

**Shortest witnesses.** The positive entries in the rank-four and rank-five columns, and the absence of those ranks at earlier lengths, give both sharp cutoffs. The following words give the entire sets of first-appearance arrays. The all-alphabet minima from the census certify that none has a smaller-alphabet realization.

| Rank | Word | Array |
|---:|:---|:---|
| 4 | `01203102` | \((0,0,0,3,0,0,6,5)\) |
| 4 | `01202103` | \((0,0,0,3,0,3,6,0)\) |
| 4 | `01020103` | \((0,0,2,0,4,4,6,0)\) |
| 5 | `01234024103` | \((0,0,0,0,0,5,0,0,0,9,6)\) |
| 5 | `01234031024` | \((0,0,0,0,0,5,0,0,8,7,6)\) |
| 5 | `01232031024` | \((0,0,0,0,0,5,0,4,8,7,0)\) |
| 5 | `01203102104` | \((0,0,0,3,0,0,6,5,6,9,0)\) |

**Persistence.** Append copies of one of the existing symbols to a rank-five witness of length eleven. The new array still starts with the old array, so any realization restricts to a length-eleven realization requiring at least five letters. The extended witness still uses five, proving equality at the prescribed longer length.

## Verification

Run `python3 verify_independent.py` or compile `verify.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify` and run `./verify`. The respective terminal markers are `INDEPENDENT_VERIFY_OK` and `VERIFY_OK`. The C++ implementation compares two Parikh procedures for each input and checks stored witness realizations; both implementations check the whole census. The finite computation certifies lengths through eleven only. Persistence is proved separately by the prefix argument.

## Relationship to prior work

Write \(T_s(n)\) for the number of arrays realizable over a fixed alphabet of size \(s\), allowing some letters not to occur. This is a cumulative rank count. Habib, Shamil and Rahman prove \(T_2(n)=2^{n-1}\) (Proposition 3.1) and give larger-alphabet upper bounds (§4). The earlier ternary censuses [2, 3] use the same complete prefix-array map and give \(T_3(n)\) through the range in this table. Since \(T_1(n)=1\), the first three columns are exactly \(1,T_2(n)-1,T_3(n)-T_2(n)\). In particular \(T_3(4)-T_2(4)=9-8=1\), with zero difference for all shorter lengths. That lower-rank threshold is prior coverage, even though it can be read off the present computation as well.

The higher-rank columns identify arrays not covered by the ternary census and distinguish the rank-four and rank-five parts. Counting individual Abelian-border incidences in binary or partial words, as in [4], is a different invariant. The finite results do not give a general higher-alphabet counting formula.

## References

1. M. Habib, Md. S. Shamil, M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, [arXiv:2111.00259](https://arxiv.org/abs/2111.00259), 2021.
2. [*Ternary Abelian border array census and sharp leading fiber classification*](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-ternary-abelian-border-array-census-and-sharp-leading-fiber-clas--8e797a662627), 2026-10-26, Finding and assumptions.
3. [*Exact ternary Abelian border array census and reconstruction ambiguity*](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-ternary-abelian-border-array-census-and-reconstruction-amb--05628a83255c), 2026-10-18, Finding.
4. F. Blanchet-Sadri, K. Chen, K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, EPTCS **252** (2017), 56–70, [arXiv:1708.06461](https://arxiv.org/abs/1708.06461).
