# Complete dimension and singularity census of toric Richardson varieties in the seven-step flag variety

## Finding

Let \(\mathrm{Fl}(7)\) denote the complete flag variety of \(\mathbb C^7\). For each comparable pair \(v\le w\) in the strong Bruhat order of \(S_7\), let \(\overline R_{v,w}\) denote the standard **embedded closed Richardson variety**. Two different endpoint pairs give different embedded subvarieties; we do **not** quotient by abstract isomorphism. Write \(d=\ell(w)-\ell(v)\) for their complex dimension.

The following is the **complete** stratification of toric Richardson varieties by dimension and smoothness:

| \(d\) | Toric | Smooth toric | Singular toric |
| ---: | ---: | ---: | ---: |
| 0 | 5,040 | 5,040 | 0 |
| 1 | 33,984 | 33,984 | 0 |
| 2 | 111,910 | 111,910 | 0 |
| 3 | 229,848 | 223,704 | 6,144 |
| 4 | 312,552 | 286,108 | 26,444 |
| 5 | 276,604 | 231,484 | 45,120 |
| 6 | 146,138 | 111,064 | 35,074 |
| 7 | 37,852 | 27,484 | 10,368 |
| 8 | 3,448 | 2,736 | 712 |
| 9 | 64 | 64 | 0 |

Therefore there are exactly **1,157,440** toric Richardson varieties, exactly **123,862** of them singular, in \(\mathrm{Fl}(7)\). Their greatest dimension is \(9\), achieved by exactly **64** embedded varieties, **all smooth**. The greatest dimension of a singular toric Richardson is \(8\), with exactly **712** singular representatives in dimension \(8\). In the unexpected range \(d>6\), there are \(41,364\) toric varieties, of which \(11,080\) are singular.

The smooth toric counts in the third column agree with previously published counts of Boolean Bruhat intervals; they are included to identify the **new singular complement** and are not asserted to be novel by themselves.

## Assumptions and scope

All varieties and toric actions are over \(\mathbb C\). The word *toric* permits a nonstandard dense algebraic torus of dimension \(d\): it does **not** require a torus action extending the diagonal torus of \(\mathrm{GL}_7\). The Schubert and opposite-Schubert flags are fixed, and all \(7!\) permutations occur as labeled endpoints. The zero-dimensional cases \(v=w\) count as toric points.

## Proof

**1. The geometric classification.** Theorem 1.2 of Gorsky–Kim–Sherman-Bennett, arXiv:2603.29260, gives
\[\overline R_{v,w}\text{ toric}\quad\Longleftrightarrow\quad [v,w]\text{ contains no rank-three interval isomorphic to }S_3.\]
For such a toric Richardson, smoothness holds precisely when \([v,w]\) is a Boolean interval (ibid., Introduction, and Lee–Masuda–Park, arXiv:1904.10187). The flag variety has a distinct Richardson closure for each comparable pair; its dimension is \(\ell(w)-\ell(v)\).

**2. An exact first characterization suitable for exhaustive enumeration.** Represent every permutation as a word in \(\{1,\ldots,7\}\), ordered lexicographically. For any \(a,b\), the standard rank-matrix criterion says that \(a\le b\) in strong Bruhat order exactly when, for every \(1\le k\le6\) and \(1\le t\le7\),
\[\#\{i\le k:a(i)\le t\}\ \ge\ \#\{i\le k:b(i)\le t\}.\]
The two supplied executables independently generate all \(5040\) permutations and apply this exact criterion. Since the set of pairs is finite, this is exhaustive, not statistical sampling.

**3. A direct forbidden-subinterval recurrence.** A rank-three Bruhat interval is an \(S_3\) interval exactly when it has six elements, equivalently two immediate upper covers of its bottom endpoint (the rank-two subintervals are diamonds). For a comparable pair \((a,b)\) of length difference at least four, its interval contains such a rank-three obstruction if and only if either there is an immediate upper cover \(a\lessdot c\le b\) with a bad interval \([c,b]\), or an immediate lower cover \(a\le c\lessdot b\) with a bad interval \([a,c]\). The converse is immediate. For necessity, any embedded bad subinterval with bottom strictly above \(a\) can be reached by an upper cover of \(a\), and one with bottom equal to \(a\) and top strictly below \(b\) can be reached by a lower cover of \(b\). Induction on length difference proves the recurrence exactly. Transposition-cover generation and a rank-bitset intersection compute the sizes of all good intervals. This yields the full toric and Boolean columns in `VERIFY_CROWN.cpp`.

**4. Independent \(R\)-polynomial route.** The Kazhdan–Lusztig \(R\)-polynomials satisfy the usual right-descent recurrence (for a right descent \(s\) of \(w\)):
\[R_{v,w}(q)=\begin{cases}R_{vs,ws}(q),&vs<v,\\qR_{vs,ws}(q)+(q-1)R_{v,ws}(q),&vs>v,\end{cases}\]
with \(R_{v,v}=1\) and \(R_{v,w}=0\) when \(v\not\le w\). Deodhar's decomposition expresses \(R_{v,w}(q)\) as a positive sum of terms \((q-1)^a q^b\) with one distinguished open-torus cell contributing \((q-1)^d\). By Gorsky–Kim–Sherman-Bennett, Lemma 3.1, the open Richardson variety is a torus exactly when no other such cells occur. Consequently,
\[\overline R_{v,w}\text{ toric}\quad\Longleftrightarrow\quad R_{v,w}(2)=1.\]
Every additional Deodhar cell contributes a strictly positive integer at \(q=2\). Thus the second executable needs only \(\min\{2,R_{v,w}(2)\}\) and evaluates the recurrence with saturation at \(2\); no floating-point operations occur. This route evaluates all comparable pairs independently of the forbidden-subinterval recurrence.

**5. Exhaustive output and reconciliation.** Both algorithms return the toric column displayed above, including \(64\) pairs of dimension \(9\) and none of dimension \(10\) or more. The forbidden-subinterval algorithm also computes the exact cardinality of each good Bruhat interval with bitset intersections; it returns the Boolean column above. Its independent Boolean counts for dimensions \(3\) through \(9\) reproduce Table 1 of Ellenberg–Libedinsky–Plaza–Simental–Williamson. Subtracting the smooth toric column from the toric column gives the singular column, hence all assertions. Both implementations include explicit array-by-array assertions for dimension \(0\) through \(9\) and the excluded higher dimensions.

## Verification

`VERIFY_RPOLY.cpp` and `VERIFY_CROWN.cpp` are self-contained ISO C++17 sources, compiled and executed by `VERIFY_ALL.sh`; they use only the standard library. Exact integer results are also supplied as `COUNTS.tsv`. The independently implemented algorithms each return `VERIFY_OK` for \(n=7\). The crown checker verifies every length-three interval against its actual element count and checks all toric and Boolean counts. The \(R\)-polynomial checker separately verifies the complete toric distribution, its top rank, and the \(64\) top pairs with their interval sizes and rank profiles. Since the claimed theorem is a finite complete \(S_7\) census, exhaustive computation is a valid proof when coupled with the cited structural characterizations and independently reviewed code.

## Relationship to prior work

Ellenberg–Libedinsky–Plaza–Simental–Williamson, arXiv:2601.01235 (first public 2026-01-03), Table 1, enumerate **Boolean** rank-\(3\) through rank-\(12\) intervals in \(S_7\); the \(64\) dimension-nine smooth cases were already known. The paper does not classify all lattice intervals, all toric Richardson varieties, or the non-Boolean/singular complement. Gorsky–Kim–Sherman-Bennett, arXiv:2603.29260 (first public 2026-03-31), Theorem 1.2, establishes the toric/lattice/crown equivalence and its examples, but does not provide the present full dimension census. Lee–Masuda–Park, arXiv:1904.10187, treats standard-torus toric Bruhat interval polytopes, smoothness and Boolean criteria, not the present nonstandard-torus census. Gao–Gui, arXiv:2610.17798 (first public 2026-10-13), treats polytopal realizations and intersection cohomology of lattice Bruhat intervals; only its abstract and bibliographic record were accessible in this check, so a remaining priority risk is explicitly acknowledged.

## Limitations

The claim is about **labeled embedded** Richardson varieties in \(\mathrm{Fl}(7)\), not abstract isomorphism types or all ranks \(n\). This is a complete finite classification, not a claimed new general toricity theorem. The already-published Boolean counts are reused as a cross-check and smoothness comparison. Historical priority is provisional; full comparison with every earlier enumeration or inaccessible source and independent external mathematical review are outstanding.

## References

1. J. Ellenberg, N. Libedinsky, D. Plaza, J. Simental, G. Williamson, *Bruhat intervals that are large hypercubes*, arXiv:2601.01235v1 (2026-01-03), especially Table 1.
2. E. Gorsky, S. Kim, M. Sherman-Bennett, *Unexpected toric Richardson varieties*, arXiv:2603.29260v1 (2026-03-31), Theorem 1.2 and Lemma 3.1.
3. E. Lee, M. Masuda, S. Park, *Toric Bruhat Interval Polytopes*, arXiv:1904.10187v2 (originally 2019-04-23), especially Theorems 1.1 and 1.3.
4. Y. Gao, T. Gui, *Lattice Bruhat intervals are polytopal*, arXiv:2610.17798v1 (2026-10-13); only abstract and record checked.
