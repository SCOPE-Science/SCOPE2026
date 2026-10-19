# Exact four-survivor ternary multiset deletion-code profile

## Finding

For every integer \(n\ge5\), the maximum number \(S_3(n,n-4)\) of ternary multisets of cardinality \(n\) that can be distinguished after as many as \(n-4\) deletions is
\[
S_3(n,n-4)=
\begin{cases}
7,&n=5,\\
6,&n=6,\\
4,&7\le n\le9,\\
3,&n\ge10.
\end{cases}
\]
Thus the all-constant three-word code first becomes optimal at \(n=10\), while the small-length exceptions and both intermediate plateaux are exact. The first value, \(S_3(5,1)=7\), was previously established by the known ternary single-deletion formula. The contribution here is the complete four-survivor profile, in particular every \(n\ge6\).

## Assumptions and scope

Use the fixed alphabet \(\{0,1,2\}\). A cardinality-\(n\) multiset is a vector \(x=(x_0,x_1,x_2)\in\mathbb Z_{\ge0}^3\) satisfying \(x_0+x_1+x_2=n\). Define its intersection with another vector by
\[
I(x,y)=\sum_{i=0}^2\min(x_i,y_i).
\]
The pair \(x\ne y\) can share a received multiset of size four precisely when \(I(x,y)\ge4\). Hence correction of up to \(n-4\) deletions is equivalent, for all pairs of distinct codewords, to \(I(x,y)\le3\). A common received multiset of cardinality greater than four could itself be truncated to a common four-element multiset, so this criterion also covers fewer than \(n-4\) deletions. There are no positional or ordering assumptions.

## Proof

**Heavy-coordinate bound.** Call a vector heavy when at least one coordinate is at least four, and light when all three coordinates are at most three. For each heavy codeword choose any coordinate attaining four or more. Two codewords cannot be assigned the same coordinate, since then their intersection would have size at least four. Therefore any valid code has at most three heavy words.

**Lengths \(n\ge10\).** A light vector has total size at most nine. Hence every codeword is heavy and there are at most three. The three pure vectors \((n,0,0)\), \((0,n,0)\), and \((0,0,n)\) have zero pairwise intersection and attain the bound.

**Lengths \(7\le n\le9\).** Any two distinct light vectors \(x,y\) satisfy
\[
I(x,y)=2n-\sum_{i=0}^2\max(x_i,y_i)\ge2n-9\ge5.
\]
They are therefore incompatible. Together with the heavy-coordinate bound, this gives at most four codewords. The three pure vectors together with \((n-6,3,3)\) form a four-word code: the fourth vector is light in precisely the stated range and meets each pure vector in at most three symbols.

**Length \(n=6\).** Every light vector has two coordinates at least two; otherwise its total size would be at most \(3+1+1=5\). Accordingly it contains at least one of the three four-element submultisets \((2,2,0)\), \((2,0,2)\), and \((0,2,2)\). Two light codewords containing the same one of these three submultisets cannot coexist, as their intersection would be at least four. Assigning one such certificate to each light codeword shows that a valid code has at most three light words. Thus at most six words are possible in total. Equality holds for
\[
\{(6,0,0),(0,6,0),(0,0,6),(0,3,3),(3,0,3),(3,3,0)\}.
\]
Distinct nonconstant words in this code meet in exactly three symbols, and each meets each pure word in at most three.

**Length \(n=5\).** There are twelve light vectors. The following nine triples are cliques in the incompatibility graph on these vectors, meaning every pair within a displayed triple has intersection at least four:

| Certificate | Three incompatible light vectors |
| --- | --- |
| 1 | \((1,3,1),(2,2,1),(2,3,0)\) |
| 2 | \((2,2,1),(2,3,0),(3,2,0)\) |
| 3 | \((0,2,3),(1,1,3),(1,2,2)\) |
| 4 | \((0,3,2),(1,2,2),(1,3,1)\) |
| 5 | \((0,2,3),(0,3,2),(1,2,2)\) |
| 6 | \((2,0,3),(2,1,2),(3,0,2)\) |
| 7 | \((2,1,2),(3,0,2),(3,1,1)\) |
| 8 | \((1,1,3),(2,0,3),(2,1,2)\) |
| 9 | \((2,2,1),(3,1,1),(3,2,0)\) |

Every one of the twelve light vectors occurs in at least two of these nine triples (a directly checkable finite incidence statement). A code may choose at most one word from each triple. Counting incidences between selected light words and certificate triples therefore gives \(2L\le9\) for the number \(L\) of selected light words, hence \(L\le4\). Combined with the three-heavy bound, this yields at most seven codewords. The seven-word code
\[
\{(0,0,5),(0,2,3),(0,5,0),(1,3,1),(3,0,2),(3,2,0),(5,0,0)\}
\]
has pairwise intersection at most three, attaining the bound. These arguments cover every integer \(n\ge5\). \(\square\)

## Verification

The standalone standard-library script `check.py` independently enumerates all size-\(n\) ternary multiplicity vectors for \(5\le n\le10\), constructs incompatibility from the exact intersection formula, and uses a complete bitset clique search to exclude any code larger than the displayed witnesses. It separately checks the nine incidence certificates, the three size-four receiver certificates, and the exact witnesses. For \(n=11,12,17,32\) it additionally performs finite consistency checks on the heavy-coordinate reasoning. The accompanying `check_output.txt` records its completed execution ending in `VERIFICATION_OK`.

To reproduce, place both files in the same directory and run `python3 check.py`. The infinite range \(n\ge10\) is proved by the heavy-coordinate argument, not by the finite search. Both the algebraic proof and computational verification use exact integer arithmetic.

## Relationship to prior work

Kreindel, Essayag, and Zabokritskiy [1] establish the multiset-deletion model and its intersection criterion. Their Section 4.4 gives a general certificate bound for **three** surviving multiset elements; their Section 5.3 provides an exact ternary **single-deletion** formula and therefore already implies the displayed \(n=5\) value. Neither establishes the four-survivor values at \(n\ge6\). A separately published ternary three-survivor exact profile gives \(4,4,3,\ldots\), but that is a different permitted intersection threshold and does not imply the present profile. The later work [2] studies multiset deletion-ball geometry and related code bounds, without an exact four-survivor ternary profile in its inspected statements. Kovačević and Tan [3] develop the general discrete-simplex code framework; their general bounds do not imply the displayed finite-length optima. These statement-level distinctions were checked against source text, rather than inferred from titles alone.

## Limitations

The result concerns three alphabet symbols and exactly four surviving symbols, not arbitrary alphabet size or survivor count. It determines the maximum code size, not the number or isomorphism classes of all optimum codes. It includes one previously known endpoint (\(n=5\)). The finite certificates are elementary and reproducible, but independent external mathematical validation has not been performed. Prior discoveries under other discrete-simplex or lattice-packing notation cannot be categorically excluded solely by targeted searches.

## References

1. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy (Yohananov), “Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results,” arXiv:2601.05636, first posted January 9, 2026, updated July 13, 2026. https://arxiv.org/html/2601.05636v2
2. “Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes,” arXiv:2603.18322, first posted March 2026. https://arxiv.org/abs/2603.18322
3. M. Kovačević and V. Y. F. Tan, “Codes in the Space of Multisets—Coding for Permutation Channels with Impairments,” arXiv:1612.08837, 2016. https://arxiv.org/abs/1612.08837
