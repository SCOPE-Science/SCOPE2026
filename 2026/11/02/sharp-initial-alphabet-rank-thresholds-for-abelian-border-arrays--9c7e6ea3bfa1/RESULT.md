# Sharp initial alphabet-rank thresholds for Abelian border arrays

## Finding

Let \(\pi(w)\) be the length-\(n\) array recording, for each nonempty prefix of a finite word \(w\) of length \(n\), the length of its longest *proper Abelian border*: a prefix and a suffix of equal length and equal Parikh vector. The value is zero if there is no such nonempty border. Define the **alphabet rank** \(\rho(\pi)\) of a realizable array as the least number of distinct letters in any word realizing it, and let \(R(n)\) be the greatest alphabet rank of an array of length \(n\).

The complete initial rank thresholds are
\[
R(n)=\begin{cases}
1,&n=1,\\
2,&2\le n\le3,\\
3,&4\le n\le7,\\
4,&8\le n\le10,\\
5,&n=11.
\end{cases}
\]
Thus the first arrays requiring respectively three, four, and five letters occur **exactly at lengths 4, 8, and 11**. There are exactly one, three, and four such first-appearance arrays, respectively. Furthermore, for every \(n\ge11\), at least one length-\(n\) array has alphabet rank exactly five (the maximal rank beyond length 11 is not determined here).

The complete rank distribution through length 11 is as follows. Entry \(a_{n,r}\) is the number of realizable length-\(n\) arrays of minimal alphabet size exactly \(r\).

| \(n\) | \(a_{n,1}\) | \(a_{n,2}\) | \(a_{n,3}\) | \(a_{n,4}\) | \(a_{n,5}\) | Total |
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

Words are finite, *linear*, indexed strings over any finite alphabet; positions are counted from one and all prefixes are included. Letters are distinguishable, but the array is invariant under consistent relabeling. A border must be nonempty and shorter than the word whose border is measured. Abelian equivalence means equality of symbol-count (Parikh) vectors, not equality of the ordered substrings. The claim covers every realizable array at each length \(1\le n\le11\), including arrays produced over alphabets of arbitrarily large declared size, since at most \(n\) distinct letters can actually occur.

## Proof

**1. Exhaustive canonicalization.** Associate with each word the set partition of its positions determined by equal letters. Consistently relabel the blocks in order of their first appearance, yielding a unique *restricted-growth word* \(u=(u_1,\ldots,u_n)\) with \(u_1=0\) and \(0\le u_i\le1+\max(u_1,\ldots,u_{i-1})\) for \(i>1\). Conversely, every such word determines one set partition. Equality of Parikh vectors is invariant under bijective relabeling, so the Abelian border array of any word equals that of its unique restricted-growth representative. The number of letters used is likewise preserved. Therefore **all arrays, together with their minimum realizing alphabet sizes, are determined exactly** by enumerating each restricted-growth word once and taking the minimum letter count for each array. No assumption about an a priori alphabet cutoff is needed.

**2. Exact computation for each representative.** For every \(1\le i\le n\), define
\[
\pi(u)_i=\max\Bigl(\{0\}\cup
\{\ell:1\le\ell<i,\ 
\operatorname{Parikh}(u_1\cdots u_\ell)
=\operatorname{Parikh}(u_{i-\ell+1}\cdots u_i)\}\Bigr).
\]
The direct verifier checks each candidate \(\ell\) by accumulating one count per symbol in the two substrings. A second, separately written implementation grows both the candidate prefix and candidate suffix one symbol at a time, updating their Parikh vectors and checking equality. Both produce the same array for every canonical representative. The recursion begins with \(u_1=0\) and, after a prefix whose greatest label is \(m\), tries every next letter in \(\{0,1,\ldots,m+1\}\). By induction this is a bijective enumeration of all set partitions of \(\{1,\ldots,n\}\).

**3. Complete finite determination.** The verifier visits respectively \(1,2,5,15,52,203,877,4140,21147,115975,678570\) canonical representatives at lengths 1 through 11, agreeing with the Bell-number counts. For each distinct computed array, it retains the smallest number of used letters among representatives. Its complete output is the rank table in the Finding section; a standalone independent Python implementation performs the same complete enumeration using its own Parikh-vector procedure and reproduces the table. The executable source and recorded counts are supplied in `verify.cpp`, `verify_independent.py`, and `CENSUS.csv`. Thus the table is an exact, exhaustive finite certificate, not a statistical extrapolation.

**4. Sharpness and witnesses.** The table shows that no rank-three array occurs before length four, no rank-four array before length eight, and no rank-five array before length eleven. Explicit first-appearance witnesses, written as canonical words followed by their arrays, are:

- Length 4, rank 3: `0102` gives `(0,0,2,0)`.
- Length 8, rank 4: `01203102`, `01202103`, and `01020103` give respectively `(0,0,0,3,0,0,6,5)`, `(0,0,0,3,0,3,6,0)`, and `(0,0,2,0,4,4,6,0)`.
- Length 11, rank 5: `01234024103`, `01234031024`, `01232031024`, and `01203102104` give respectively `(0,0,0,0,0,5,0,0,0,9,6)`, `(0,0,0,0,0,5,0,0,8,7,6)`, `(0,0,0,0,0,5,0,4,8,7,0)`, and `(0,0,0,3,0,0,6,5,6,9,0)`.

The verifier checks each witness and proves the absence of any lower-rank realization by exhaustive comparison against *all* representatives of that length. Each stated count is the full number of newly appearing rank-\(r\) arrays at its corresponding shortest length, not merely a number of constructed examples.

**5. Persistence at longer lengths.** Fix any length-eleven rank-five witness and append copies of an existing letter to reach an arbitrary length \(n\ge11\). The resulting longer array has the original length-eleven array as its first eleven entries, so no word on four or fewer distinct letters can realize it. The displayed extension itself uses five letters, so its rank is exactly five. This proves the claimed existence for all longer lengths.

## Verification

Compile with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify` and run `./verify`, requiring the terminal output marker `VERIFY_OK`. Independently run `python3 verify_independent.py`, requiring `INDEPENDENT_VERIFY_OK`. The C++ implementation executes two distinct border-computation routines on every canonical representative, checks all eleven Bell-number totals, checks every rank distribution, and validates stored witnesses. The Python program independently enumerates all canonical representatives and reproduces every rank count. Both completed successfully on the supplied, unmodified source. No third-party packages are required.

## Relationship to prior work

Habib, Shamil and Rahman (2021), arXiv:2111.00259, prove that the number of binary Abelian border arrays of length \(n\) is \(2^{n-1}\). Their Section 4 identifies larger alphabets as difficult and gives partition-based upper bounds, but does **not** determine the minimum alphabet needed to realize each distinct array or the sharp four- and five-letter first-appearance thresholds. The first two columns of the present table agree with their binary count, while the other columns quantify a new higher-alphabet distinction. Blanchet-Sadri, Chen and Hawes (2017) enumerate Abelian borders of binary/partial words using lattice paths; this concerns border occurrences in words rather than alphabet ranks of entire prefix-border arrays. Prior work on single-word Abelian-border frequencies does not imply the computed distinct-array rank distribution.

## Limitations

The exhaustive maximal-rank classification is restricted to \(n\le11\). The persistent existence of rank-five arrays for all \(n\ge11\) is proved, but their maximal possible ranks and total array counts beyond eleven are not determined. The result concerns complete longest-Abelian-border arrays only, not shortest-border arrays, unordered collections of borders, or approximate Parikh comparisons. Originality is assessed against the inspected sources and available indexed literature; an unindexed equivalent finite census cannot be logically excluded. The independently checked enumeration certifies the stated finite range, not a formula for arbitrary length or alphabet size.

## References

1. M. Habib, Md. S. Shamil, M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, arXiv:2111.00259v1, first public 2021-10-30. https://arxiv.org/abs/2111.00259
2. F. Blanchet-Sadri, K. Chen, K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, EPTCS 252 (2017), 56–70; arXiv:1708.06461. https://arxiv.org/abs/1708.06461
3. M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146. https://doi.org/10.1016/j.dam.2014.02.012
