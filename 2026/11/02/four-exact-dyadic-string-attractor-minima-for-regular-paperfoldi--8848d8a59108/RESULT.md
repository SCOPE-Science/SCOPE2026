# Four exact dyadic string-attractor minima for regular paperfolding

## Finding

For the regular paperfolding word \(P\), let \(P_n=P[1..n]\) be its prefix of length \(n\), and write \(\gamma(T)\) for the minimum cardinality of a string attractor of a finite word \(T\). Then the exact new dyadic values are

\[
\boxed{\gamma(P_{128})=5,\quad\gamma(P_{256})=6,\quad\gamma(P_{512})=6,\quad\gamma(P_{1024})=7.}
\]

In particular, the smallest attractor size is unchanged on doubling the length from \(256\) to \(512\), then increases at \(1024\). All four conclusions are exact and are witnessed by two kinds of compact, independently checkable finite certificates: explicit attractor positions for upper bounds, and rational factor-packings for lower bounds.

## Assumptions and scope

For each one-based index \(i\ge 1\), write \(i=2^v q\) with \(q\) odd. Define \(P[i]=0\) when \(q\equiv1\pmod4\), and \(P[i]=1\) when \(q\equiv3\pmod4\). For a binary finite word \(T\), a *factor* is a nonempty contiguous substring, and a position set \(\Gamma\subseteq\{1,\ldots,|T|\}\) is a *string attractor* if every distinct factor has some occurrence crossing at least one position of \(\Gamma\). Here crossing means that the position lies inside the inclusive interval of that occurrence. The statement concerns exactly the four specified finite dyadic prefixes. Reversing or complementing the binary alphabet would not affect their minimum sizes, but the position witnesses use the convention above.

## Proof

For each distinct nonempty factor \(u\) of \(T\), define \(S_T(u)\) as the union, over **all** occurrences of \(u\) in \(T\), of the position intervals occupied by those occurrences. Thus \(\Gamma\) is an attractor precisely when \(\Gamma\cap S_T(u)\ne\varnothing\) for every \(u\).

**Lower-bound lemma (fractional factor packing).** Let \(w_u\ge0\) be nonnegative rational weights on finitely many distinct factors, and suppose \(\sum_{u:p\in S_T(u)}w_u\le1\) for every position \(p\) of \(T\). For any attractor \(\Gamma\), summing the covering inequalities \(1\le\sum_{p\in\Gamma\cap S_T(u)}1\) against the nonnegative weights yields

\[
\sum_u w_u\ \le\ \sum_{p\in\Gamma}\sum_{u:p\in S_T(u)}w_u\ \le\ |\Gamma|.
\]

In particular \(\gamma(T)\ge\lceil\sum_uw_u\rceil\). This is a direct finite combinatorial bound; no optimization solver or unproved asymptotic assertion is used in the verification.

The embedded file `pf_cert.json` gives, for each length, explicit **one-based** upper-attractor positions and lower-packed factors specified by their first occurrence's start coordinate, length, and positive integer weight units. The common denominator is \(16\). Factors are interpreted as the actual substrings of the above \(P_n\); their support sets are recomputed from every exact occurrence in that prefix. The upper witnesses and lower total weights are:

| Prefix length | Explicit attractor positions (one-based) | Lower packing total | Implied integer minimum |
|---:|---|---:|---:|
| \(128\) | \(\{20,40,56,77,96\}\) | \(80/16=5\) | \(5\) |
| \(256\) | \(\{40,96,124,144,180,206\}\) | \(92/16=23/4\) | \(6\) |
| \(512\) | \(\{120,142,192,296,352,404\}\) | \(96/16=6\) | \(6\) |
| \(1024\) | \(\{128,348,435,458,558,743,788\}\) | \(102/16=51/8\) | \(7\) |

For each row, `verify.py` independently reconstructs every distinct factor of the finite prefix and checks it has an occurrence crossing at least one listed attractor position. The same verifier reconstructs the factor represented by each packing row, locates *every* occurrence of that factor, and accumulates integer weights at *every* prefix position. In all four cases the maximum total load at a position is at most \(16\) units, and the sums are exactly the numerators above. The lower-bound lemma gives the required lower bounds, matching the listed upper bounds. Hence the four displayed minima follow.

## Verification

Run `python3 verify.py` in the directory containing `pf_cert.json`; it requires only Python's standard library. It prints `PAPERFOLDING_ATTRACTORS_VERIFY_OK` after proving both certificate inequalities at all four lengths. Its exhaustive distinct-factor counts at the four lengths are respectively \(6479,25775,102767,410351\), matching the earlier independently published factor totals. The verifier examines every substring and, for lower-packed factors, every exact occurrence. The arithmetic proving the lower bounds is integer-only. The optimization used to discover the certificates is not a dependency of their verification. The exact input, output, and all certificate entries are embedded in this package.

## Relationship to prior work

Banbara, Bannai, Guo, Köppl, Mieno and Okamoto's 2026 research on smallest attractors of Fibonacci and period-doubling words motivates the study of exact natural automatic-word families but does not state paperfolding minima. Its 2026 extended version adds Thue–Morse rather than paperfolding. An accessible earlier study of paperfolding and Rudin–Shapiro dyadic prefixes [2] **already determines the regular-paperfolding minima through length \(64\)** and reports valid **upper bounds** of \(7,8,10,9\) and lower bounds \(4\) for lengths \(128,256,512,1024\); it explicitly labels these larger values nonexact. The present four exact minima, all below those reported upper bounds, and their fractional-packing lower certificates are not implications of the recorded bounds. Schaeffer and Shallit's automatic-sequence framework [3] supplies general context but does not provide these four explicit finite values in the material inspected.

## Limitations

Only the four stated finite prefixes are classified here. The argument does not determine \(\gamma(P_n)\) at other lengths and does not decide whether the paperfolding prefix-attractor sequence is bounded or grows logarithmically. The finite proof relies on replayable enumeration and rational factor packings rather than a closed symbolic all-length formula. Search coverage cannot rule out every unpublished, nonindexed, or differently named calculation, and no independent mathematical audit of this new result has been performed.

## References

1. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152, first publicly submitted 2026-02-18; CPM 2026, DOI https://doi.org/10.4230/LIPIcs.CPM.2026.33. Accessible HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.33/LIPIcs.CPM.2026.33.html.
2. *Exact minimal string attractors for Rudin–Shapiro and regular-paperfolding dyadic prefixes (n ≤ 64), with certified bounds to n = 1024*, public research result, https://github.com/Resultary/2026/blob/main/2026/9/8/SCOPE079/RESULT.md (accessed 2026-10-31).
3. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840.
