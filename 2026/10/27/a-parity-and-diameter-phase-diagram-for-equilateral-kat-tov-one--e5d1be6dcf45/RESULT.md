# A parity and diameter phase diagram for equilateral Katětov one-types

## Finding

Let \(D\ge s\ge1\) be integers. Let \(\mathbb U_D\) denote the countable universal homogeneous metric structure whose nonzero distances are \(1,2,\ldots,D\). Inside it, individually name \(n\ge1\) distinct points \(A=\{a_1,\ldots,a_n\}\) with \(d(a_i,a_j)=s\) for distinct indices. Let \(T_{D,s}(n)\) be the number of complete nonalgebraic one-types over these named parameters. Put \(a=\lceil s/2\rceil\) and define
\[
 U_m=\min(D,m+s)-m+1\quad(a\le m\le D),\qquad
 B_m=\min(D,m+s)-s+m+1\quad(1\le m<a).
\]
Then the following **exact formula** holds, with an empty sum interpreted as zero:
\[
\boxed{
T_{D,s}(n)=\sum_{m=a}^{D}(U_m^n-(U_m-1)^n)
+n\sum_{m=1}^{a-1}B_m^{\,n-1}.}
\]

For fixed \(D,s\), set
\[
 w=\min(s+1,D-a+1),\qquad
 h=\max(1,D-s-a+1).
\]
There is a sharp distinction between the following two regimes as \(n\to\infty\):

* **Singleton-short regime:** if \(s=2k+1\ge3\) and \(s\le D\le3k+1\), then \(w=D-k\) and
  \[
  T_{D,s}(n)=n w^{n-1}+w^n+O_{D,s}\bigl(n(w-1)^{n-1}\bigr).
  \]
  Among the \(T_{D,s}(n)\) types chosen uniformly, the probability that exactly one parameter is at distance \(k\) from the new point, and all other parameter distances are at least \(k+1\), tends to \(1\).
* **Ordinary exponential regime:** for all other \(D\ge s\ge1\),
  \[
  T_{D,s}(n)=h w^n+O_{D,s}\bigl(n(w-1)^{n-1}\bigr).
  \]
  The probability that any parameter distance is strictly less than \(s/2\) tends to \(0\).

For example, the transition with \(s=3\) occurs between ambient diameters \(D=4\) and \(D=5\):
\[
 T_{3,3}(n)=2^n+n2^{n-1},\quad
 T_{4,3}(n)=3^n+n3^{n-1},\quad
 T_{5,3}(n)=4^n+n3^{n-1}.
\]

## Assumptions and scope

The metric is integer-valued with allowed distances \(\{0,1,\ldots,D\}\), and the \(n\) named parameters are pairwise at distance exactly \(s\). Equality types \(x=a_i\) are excluded; including them adds exactly \(n\). The statement concerns complete one-types in the relational language with a distance predicate for each integer distance. It counts labeled distance vectors: the named parameters are fixed individually, not identified under permutations. \(D,s\) are fixed in the asymptotics, with \(n\to\infty\).

## Proof

**One-point extensions.** Finite integer metric spaces with distances at most \(D\) form an amalgamation class. For an amalgam over a common subspace, cross-distances can be taken as capped shortest-path distances, \(\min(D,\min_a(d(x,a)+d(a,y)))\); for an empty common subspace take every cross-distance \(D\). The resulting metric extends the inputs because every alternate path through the common subspace is bounded below by the original distances. Fraïssé homogeneity gives a unique countable universal homogeneous limit. Equivalently, Sauer's restricted Katětov-function criterion applies. Because the language is finite relational and the limit is ultrahomogeneous, complete nonalgebraic one-types over finite named sets are precisely isometry classes of one-point extensions fixing those parameters. Thus a type is a vector \(f=(f_1,\ldots,f_n)\in\{1,\ldots,D\}^n\) satisfying
\[
 |f_i-f_j|\le s\le f_i+f_j\qquad(i\ne j).
\]

**Exact census.** For \(n\ge2\), these inequalities say that the width of the set of coordinates is at most \(s\), and that the sum of the two smallest coordinates is at least \(s\). Partition vectors by their least coordinate \(m\). If \(2m\ge s\), all coordinates may lie in the interval \([m,\min(D,m+s)]\), but at least one must equal \(m\). This contributes exactly \(U_m^n-(U_m-1)^n\). If \(2m<s\), two occurrences of \(m\) would violate the sum inequality. There is exactly one occurrence of \(m\), in any of \(n\) positions, while each other coordinate may independently lie in \([s-m,\min(D,m+s)]\). This interval has \(B_m\) elements and every resulting vector is admissible. Its contribution is \(nB_m^{n-1}\). The same count works when \(n=1\): each possible minimum is simply its sole coordinate, and the formula gives \(T_{D,s}(1)=D\). Summing proves the closed expression.

**Largest exponential bases.** For \(m\ge a\), the interval width \(U_m=\min(s+1,D-m+1)\) is nonincreasing, with maximum \(w=U_a\). Exactly \(h=\max(1,D-s-a+1)\) values of \(m\) attain that maximum: a singleton if the width is truncated by the diameter, and otherwise the full-interval minima \(a,\ldots,D-s\). Every other upper-sum base is at most \(w-1\).

For \(m<a\), the numbers \(B_m=\min(D-s+m+1,2m+1)\) strictly increase with \(m\). If \(s=2\), the lower sum is empty. If \(s=2k\ge4\), its largest possible base is \(\min(D-k,2k-1)\), strictly smaller than \(w=\min(D-k+1,2k+1)\). If \(s=2k+1\ge3\), their largest possible value, at \(m=k\), is \(\min(D-k,2k+1)\), whereas \(w=\min(D-k,2k+2)\). Equality holds exactly when \(D\le3k+1\). The case \(s=1\) has no lower sum. Hence, outside the indicated odd-distance interval, every lower-sum base is at most \(w-1\), yielding \(h w^n+O_{D,s}(n(w-1)^{n-1})\).

In the exceptional odd-distance interval, \(D\le3k+1\), one has \(w=D-k\le s\). The upper sum telescopes exactly to \(w^n\), and the lower term indexed by \(m=k\) is exactly \(nw^{n-1}\). All other lower bases are at most \(w-1\), proving the exceptional formula.

**Concentration.** A vector with a coordinate below \(s/2\) necessarily has exactly one such coordinate. In the exceptional interval, the types having the unique short coordinate \(k\) number exactly \(nw^{n-1}\), which dominates the total. Outside this interval, the total number of vectors with any short coordinate is at most \(O_{D,s}(n(w-1)^{n-1})\), negligible relative to \(hw^n\). This proves both probability limits.

## Verification

The accompanying standalone Python checker uses exhaustive, independently coded pairwise triangle inequalities to enumerate every distance vector for all \(1\le s\le D\le8\), \(1\le n\le5\), plus \(1\le s\le D\le5\), \(n=6,7\). It compares all 210 exact counts to the closed formula. It separately checks asymptotic leading forms at 120 parameter pairs \(1\le s\le D\le15\) with \(n=100\). It terminates with `ALL_TESTS_PASS`. The infinite identities and limits follow from the preceding proof, not from these finite checks.

## Relationship to prior work

Sauer (2011) establishes the foundational restricted Katětov-function framework and existence/uniqueness of metric Fraïssé limits for suitable distance sets. In particular, his Section 2 supplies the necessary-and-sufficient one-point metric inequalities. This characterization is a prerequisite and is not claimed new; the exact equilateral two-parameter census and the sharp parity/diameter transition are the proposed contribution. The published diameter-three type-polynomial analysis *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* describes the \(D=3\) constraint table and counts over graph metrics with only distance-1 and distance-2 parameters. Its main formula does not cover arbitrary \(D\) or equilateral parameter distances \(s\) ranging up to \(D\), and does not give the phase criterion above. Direct use of its local triangle table would, of course, recover individual small cases; these are not offered as separate new results.

The cited diameter-three source also documents #P-completeness of general graph-metric one-type counting, so the completely solvable equilateral family gives a useful reference case inside a difficult counting landscape. The distinction between an arbitrary admissible distance vector and its explicit enumeration matters: general extension principles establish realizability but do not provide the two-parameter growth law, the exceptional singleton-minimum dominance, or its exact boundary. Searches for equilateral Katětov-vector counts, one-point type enumerators in bounded integer Urysohn spaces, parity, and asymptotic regimes did not identify an equivalent formula. This is not a claim of exhaustive literature coverage.

## Limitations

The parameters are equilateral and all distances are consecutive integers. No assertion is made about arbitrary parameter metrics, nonconsecutive distance sets, or growing \(D\) and \(s\) with \(n\). The results require no probabilistic independence assumption: uniformity refers to counting distinct complete types. The possibility of an equivalent enumeration implicit in specialized or unindexed Katětov-function literature is a residual originality risk. No independent scientific audit is claimed.

## References

1. Norbert Sauer, *Distance sets of universal and Urysohn metric spaces*, arXiv:1107.4794, first posted 2011-07-24, especially Definition 2.1, the type-function inequalities in Section 2, and Theorem 1. https://arxiv.org/abs/1107.4794
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, publicly available full result, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989
