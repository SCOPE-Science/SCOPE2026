# Polynomial stabilization of fixed low Bruhat up-degree layers

## Finding
For a permutation \(\pi=(\pi_1,\ldots,\pi_n)\), let \(b(\pi)\) be the number of pairs \((i,j)\) satisfying
\[
1\le i<j\le n,\qquad \pi_i<\pi_j,\qquad
\nexists\ i<t<j\text{ with }\pi_i<\pi_t<\pi_j.
\]
These pairs are upward covers in the strong Bruhat order and occurrences of the boxed mesh pattern \(12\) in the terminology of Kitaev--Qiu--Xu. Define
\[
D_n(q)=\sum_{\pi\in S_n}q^{b(\pi)},\qquad
 a_{n,r}=[q^r]D_n(q),\qquad A_r(x)=\sum_{n\ge0}a_{n,r}x^n.
\]
For **every fixed integer \(r\ge1\)**,
\[
\boxed{A_r(x)=\frac{P_r(x)}{(1-x)^{r+1}},\quad
P_r(x)\in\mathbb Z[x],\quad\deg P_r\le 2r,\quad P_r(1)=1.}
\]
Thus \(a_{n,r}\) is **exactly a polynomial in \(n\) for all \(n\ge2r\)**, of degree \(r\) and leading coefficient \(1/r!\). For every \(r\ge2\),
\[
a_{n,r}=\frac{n^r}{r!}+\frac{r(3r-5)}{2r!}n^{r-1}+O_r(n^{r-2}).
\]
For \(r=1\), \(a_{n,1}=n-1\) for \(n\ge1\). As a consequence, for any fixed \(R\), \(a_{n,0}<a_{n,1}<\cdots<a_{n,R}\) for all sufficiently large \(n\).

The first exact cases are
\[
 A_1(x)=\frac{x^2}{(1-x)^2},\qquad
 A_2(x)=\frac{3x^3-2x^4}{(1-x)^3},\qquad
 A_3(x)=\frac{11x^4-16x^5+6x^6}{(1-x)^4}.
\]
In particular, \(a_{n,2}=(n-2)(n+3)/2\) for \(n\ge3\), and \(a_{n,3}=(n^3+6n^2-13n-42)/6\) for \(n\ge4\).

## Assumptions and scope
All permutations are of \(\{1,\ldots,n\}\), with \(S_0\) consisting of the empty permutation. A skew sum is a concatenation of two nonempty permutations for which every entry in the first part exceeds every entry in the second. A skew-indecomposable permutation admits no such split. The assertions apply to arbitrary finite permutations; no pattern avoidance restriction is imposed. The index \(r\) is fixed while \(n\) varies, and the formulas use ordinary generating functions as formal power series.

## Proof
**1. The connected-block lemma.** Form the graph on positions \(1,\ldots,n\) with an edge between \(i<j\) whenever \(\pi_i<\pi_j\). If \(i<k<j\) and \(\pi_i<\pi_j\), then either \(\pi_i<\pi_k\), making \((i,k)\) an ascent, or \(\pi_k<\pi_i<\pi_j\), making \((k,j)\) an ascent. Hence every position strictly between the endpoints of any graph edge belongs to the same connected component as its endpoints. Taking an edge path shows that every component is an interval of positions. There are no ascents between distinct components; therefore the entries of an earlier component all exceed those of a later one. The components are precisely the unique skew-indecomposable factors of \(\pi\).

Replace the ascent graph by the graph of the cover pairs defining \(b(\pi)\). Each ascent \((i,j)\) is either a cover pair or admits a position \(t\) strictly between with \(\pi_i<\pi_t<\pi_j\). Repeatedly splitting such an ascent expresses its endpoints as a path of cover edges, and terminates because the position intervals shorten. Thus the cover graph has **exactly the same connected components** as the ascent graph. A skew-indecomposable factor of size \(s\ge2\) therefore has a connected cover graph and at least \(s-1\) cover edges. No cover or ascent can cross between skew factors. In particular \(b\) is additive under skew sum. Connectivity of the analogous permutation graph was recognized in the earlier work of Adin--Roichman; only its enumerative application here is asserted as new.

**2. Formal-series decomposition.** Define \(C_s(q)=\sum_{\sigma\in S_s\text{ skew-indecomposable}}q^{b(\sigma)}\), for \(s\ge2\). A singleton factor has weight \(x\). By uniqueness of the skew-factor decomposition and additivity,
\[
\sum_{n\ge0}D_n(q)x^n=
\frac{1}{1-x-\sum_{s\ge2}x^sC_s(q)}.
\]
Every monomial in \(C_s\) has \(q\)-degree at least \(s-1\). Therefore to extract \(q^r\) we need only factors of size at most \(r+1\), and at most \(r\) nonsingleton factors. Let
\[
R_r(x,q)=\sum_{s=2}^{r+1}x^s C_s(q)\pmod{q^{r+1}}.
\]
Geometric expansion at fixed positive \(q\)-degree yields
\[
\boxed{A_r(x)=\sum_{k=1}^{r}
\frac{[q^r]R_r(x,q)^k}{(1-x)^{k+1}},\quad
P_r(x)=[q^r]\sum_{k=1}^r(1-x)^{r-k}R_r(x,q)^k.}
\]
These formulas compute \(P_r\) by enumerating only finitely many skew-indecomposable permutations, all of lengths at most \(r+1\).

**3. Degree and normalization.** A monomial of total \(q\)-degree \(r\) in \(R_r^k\) combines \(k\) nonsingleton factors of sizes \(s_1,\ldots,s_k\). Because each factor contributes at least \(s_i-1\), their combined length obeys \(\sum_i s_i\le r+k\). After multiplication by \((1-x)^{r-k}\), every contribution to \(P_r\) has degree at most \(2r\). All coefficients of \(P_r\) are integers.

At \(x=1\) every term with \(k<r\) vanishes. For \(k=r\), achieving \(q\)-degree exactly \(r\) requires every nonsingleton factor to have \(q\)-degree exactly one. The only possibility is a size-two skew-indecomposable factor, and \(C_2(q)=q\). Hence \(P_r(1)=1\).

**4. Polynomial and asymptotic conclusions.** Expanding \((1-x)^{-r-1}\) gives, for every \(n\ge2r\),
\[
 a_{n,r}=\sum_{j=0}^{2r}[x^j]P_r(x)\binom{n-j+r}{r}.
\]
This is an exact degree-\(r\) polynomial in \(n\); its leading coefficient is \(P_r(1)/r!=1/r!\). To extract the next coefficient, the unique term with \(k=r\) in the preceding expansion is \(x^{2r}/(1-x)^{r+1}\). The only term with \(k=r-1\) and \(q\)-degree \(r\) uses one size-three factor and \(r-2\) size-two factors. The explicit identity \(C_3(q)=3q^2\) yields \(3(r-1)x^{2r-1}/(1-x)^r\). Terms with \(k\le r-2\) have poles of order at most \(r-1\). Consequently,
\[
 a_{n,r}=\binom{n-r}{r}+3(r-1)\binom{n-r}{r-1}+O_r(n^{r-2}),
\]
which simplifies to the displayed second coefficient. For \(r=1\), only \(x^2/(1-x)^2\) remains and gives \(n-1\). Since for each fixed \(r\) the leading term is positive and grows as \(n^r/r!\), adjacent fixed-degree coefficients are eventually strictly increasing. The zero-degree coefficient is one: the unique decreasing permutation has no ascents.

## Verification
The accompanying standard-library `verify.py` directly enumerates all permutations of lengths one through nine (409,113 total). It compares a record-minimum algorithm for the cover statistic with its literal three-index definition on every permutation through length seven, and compares the skew-indecomposable criterion with connectivity of the cover graph through length seven. It independently computes all coefficients up to \(q^5\) from the block series and compares them against the direct permutation distribution through length nine. It checks both stated low-degree formulas. Run `python3 verify.py`; the expected terminal line is `VERIFY_OK`. Finite checks corroborate, but do not replace, the all-\(r\), all-\(n\) proof above.

## Relationship to prior work
Kitaev--Qiu--Xu (2026, arXiv:2609.13764) identify boxed \(12\) with the strong Bruhat up-degree, calculate extrema and first moments, provide an exact insertion identity, and conjecture unimodality of full distribution polynomials. The present theorem answers a **different fixed-coefficient question**: all fixed small-degree layers stabilize polynomially, with exact generating functions and an eventual increasing initial segment. It does not prove full unimodality. Bousquet-Mélou--Butler (2006, arXiv:math/0603617) study the same permutation/Hasse graph under forest-like and tree-like restrictions, including the diagonal regime of edge number comparable to graph size; their results do not imply the universal fixed-edge formula. Adin--Roichman (2005, arXiv:math/0505020) previously studied the strong Bruhat cover graph and its connectivity, extrema, and expected degree; those facts are used with attribution. The length-two mesh-pattern classification of Su--Kitaev--Zhang (2026, arXiv:2605.19429) is related, but only its abstract was accessible in the available inspection, so a hidden equivalent formulation remains a historical-priority risk.

## Limitations
The result concerns one statistic on ordinary permutations with \(r\) fixed. It does not settle the global distribution-polynomial unimodality conjecture, compute modes, or give a uniform estimate when \(r\) grows with \(n\). The originality assessment is based on accessible primary literature and research-record searches, not a proof that no earlier equivalent statement exists. Independent mathematical audit has not been performed.

## References
1. Sergey Kitaev, Dun Qiu, Chao Xu, *Coincidences and Growth of Boxed Mesh Patterns*, arXiv:2609.13764, first posted 2026-09-12; Section 8.
2. Mireille Bousquet-Mélou, Steven Butler, *Forest-like permutations*, arXiv:math/0603617, 2006; Theorem 8 and Section 4.2.
3. Ron M. Adin, Yuval Roichman, *On Degrees in the Hasse Diagram of the Strong Bruhat Order*, arXiv:math/0505020, 2005.
4. Xinyu Su, Sergey Kitaev, Jiahao Zhang, *Equidistribution of mesh patterns of short length*, arXiv:2605.19429, 2026.
