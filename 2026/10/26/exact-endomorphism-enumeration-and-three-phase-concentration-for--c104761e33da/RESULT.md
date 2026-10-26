# Exact endomorphism enumeration and three-phase concentration for outward-star Hecke–Kiselman monoids

## Finding

For each integer \(r\ge1\), let \(\Theta_r\) be the oriented star with vertices \(c,u_1,\ldots,u_r\) and precisely the arrows \(c\to u_i\). Let \(H_r\) be the associated Hecke–Kiselman monoid, presented by
\[
 c^2=c,\quad u_i^2=u_i,\quad u_i u_j=u_j u_i\ (i\ne j),\quad
 c u_i c=u_i c u_i=c u_i.
\]
The exact number \(E_r=|\operatorname{End}(H_r)|\) of unit-preserving monoid endomorphisms is
\[
 \boxed{E_r=\sum_{s=0}^r\binom rs\left[
 2^r(2^s+2^{r-s}-1)^r+(2^{s+1}+2^{r-s}-1)^r\right].}
\]
It satisfies the sharper asymptotic law
\[
 \boxed{\frac{E_r}{2^{r(r+1)}}
 =3+(3r+1)2^{-r}+O(r^2 4^{-r})\qquad(r\to\infty).}
\]
In particular, \(E_r\sim3\cdot2^{r(r+1)}\).

A uniform random endomorphism concentrates in three disjoint regimes, each with limiting probability \(1/3\): (I) the center and all leaves map to idempotents containing \(c\); (II) the center maps to an idempotent containing \(c\), while no leaf does; (III) neither center nor any leaf maps to an idempotent containing \(c\). Each regime contains exactly \(2^{r(r+1)}\) endomorphisms for every \(r\).

For illustration, \(E_1=15\), \(E_2=339\), \(E_3=22{,}233\), and \(E_4=4{,}780{,}047\).

## Assumptions and scope

The presentation uses the convention that for an arrow \(x\to y\), the defining relations are \(xyx=yxy=xy\). There is one outward-pointing center and \(r\) pairwise nonadjacent sinks; the theorem does not assert the same formula for inward stars, arbitrary directed trees, or all graphs. An endomorphism must preserve the identity.

For \(X\subseteq[r]\), write \(u_X=\prod_{i\in X}u_i\), independent of order, and put \(u_\varnothing=1\). An idempotent is said to contain \(c\) when its support (the set of generators present in any word representing it) contains \(c\).

## Proof

**1. The idempotents and their products.** The acyclic-idempotent classification for Hecke–Kiselman monoids gives precisely one idempotent of every possible content. For this star these are
\[
 e_{0,X}=u_X,\qquad e_{1,X}=c u_X\qquad(X\subseteq[r]).
\]
They are distinct because content is an invariant of the defining relations. The equality \(c u_X c=c u_X\) is the source-vertex deletion identity of Wiertel (2024, Lemma 4.1), applied with source \(c\), and also shows directly that \(c u_X\) is idempotent. The other displayed elements are idempotent because the leaves commute.

The following four product rules are immediate from the presentation and source deletion:
\[
 \begin{aligned}
 e_{0,X}e_{0,Y}&=u_{X\cup Y},\\
 e_{1,X}e_{0,Y}&=c u_{X\cup Y},\\
 e_{1,X}e_{1,Y}&=c u_{X\cup Y},\\
 e_{0,X}e_{1,Y}&=u_X c u_Y.
 \end{aligned}
\]
In the final case the product is idempotent exactly when \(X\subseteq Y\). If \(X\subseteq Y\), use \(u_i c u_i=c u_i\), commuting leaves, and induction through the elements of \(X\) to obtain \(u_X c u_Y=c u_Y\). Conversely, if \(i\in X\setminus Y\), send all leaves other than \(u_i\) to \(1\). The product maps to \(u_i c\), which is not idempotent in the five-element two-generator Hecke–Kiselman monoid \(\{1,c,u_i,cu_i,u_ic\}\), since \((u_ic)^2=cu_i\ne u_ic\). Thus
\[
 e_{b,X}e_{d,Y}\text{ is idempotent}\iff
 b=1\ \text{or}\ d=0\ \text{or}\ X\subseteq Y.
\]
The corresponding commutativity test is: two idempotents with the same \(b\)-bit commute; if the bits differ, the leaf set of the \(b=0\) idempotent must be contained in that of the \(b=1\) idempotent. In that case both products equal the unique idempotent of the union content.

**2. Allowed generator images.** By Andrenšek's presentation criterion for Hecke–Kiselman endomorphisms (2026, Theorem 3.1), a choice of idempotent images for all generators extends uniquely to an endomorphism if and only if images of distinct leaves commute and the product of the center image followed by each leaf image is idempotent. This also follows directly from the presentation and the preceding product rules; idempotence of the ordered product of two idempotents forces both sandwich relations in this acyclic setting.

For a fixed pattern of types of leaf images, let \(s\) leaves have type \(0\) and \(t=r-s\) have type \(1\). Commutativity says that every type-\(0\) leaf support is a subset of every type-\(1\) leaf support. For each individual vertex coordinate, the number of allowed Boolean membership patterns is
\[
 A(s,t)=2^s+2^t-1:
\]
either all \(s\) lower-type membership bits are zero or all \(t\) upper-type membership bits are one, with the overlapping pattern counted once.

If the image of \(c\) has type \(1\), its leaf support is arbitrary (\(2^r\) choices), and there are \(A(s,t)^r\) choices of leaf-image supports. If the image of \(c\) has type \(0\), its membership in each coordinate must additionally be bounded above by all type-\(1\) bits. Treating its bit as one more lower-type bit yields
\[
 B(s,t)=2^{s+1}+2^t-1
\]
patterns per coordinate and hence \(B(s,t)^r\) choices. There are \(\binom rs\) ways to choose the type-\(0\) leaf generators. Summation proves the exact formula.

**3. Precise asymptotic and three regimes.** Dividing the exact formula by \(2^{r(r+1)}\) gives the sum of
\[
 \sum_{s=0}^r\binom rs\left(\frac{2^s+2^{r-s}-1}{2^r}\right)^r
\]
and
\[
 \sum_{s=0}^r\binom rs\left(\frac{2^{s+1}+2^{r-s}-1}{2^{r+1}}\right)^r.
\]
The first sum has exactly two unit terms (\(s=0,r\)); the second has exactly one unit term (\(s=r\)). The two adjacent first-sum terms, \(s=1,r-1\), total
\(2r\,2^{-r}(1+2^{1-r})^r\).
The adjacent second-sum term \(s=r-1\) and the opposite endpoint \(s=0\) total
\((r+1)2^{-r}(1+2^{-r})^r\).
These terms contribute \((3r+1)2^{-r}+O(r^2 4^{-r})\).

All remaining terms total \(O(r^2 4^{-r})\): for either sum, write the relevant numerator as \(2^a+2^{m-a}-1\), with \(m=r\) or \(m=r+1\), and let \(k=\min(a,m-a)\ge2\). Its normalized value is at most \(2^{-k}(1+2^{2k-m})\). When \(k\le m/4\), raising to the \(r\)-th power gives at most \(2^{-kr}\exp(r2^{-m/2})\). Summation with \(\binom rs\le\binom{r+1}k\), over the at most two indices per \(k\), is \(O(r^2 4^{-r})\) by the binomial theorem. For \(k>m/4\), the normalized value is at most \(2^{1-m/4}\), so the total over at most \(2^r\) patterns is at most \(2^{2r-rm/4}=o(r^2 4^{-r})\). This proves the asymptotic.

Finally, each of the three displayed regimes imposes a fixed pattern of type bits, for which every one of the \(r+1\) generator images has independently any of \(2^r\) leaf supports. Thus each regime contains exactly \(2^{r(r+1)}\) endomorphisms. Their total asymptotic proportion is one, so their individual limiting proportions are each \(1/3\).

## Verification

Run the standard-library Python program `verify.py`. It constructs the five-element one-edge monoid from the defining relations, independently checks all idempotent product and commutativity conditions, exhaustively enumerates all possible generator-image assignments for \(r=1,2,3\), and compares these totals to the closed formula. It also tests selected larger exact formula values and the asymptotic trend. The expected success marker is `VERIFY_OK`.

The finite checks are illustrative. The proof above establishes the exact enumeration and asymptotic for all integers \(r\ge1\).

## Relationship to prior work

Andrenšek (2026, arXiv:2604.15497v1) gives a general Boolean-matrix description of the endomorphism monoid of an arbitrary Hecke–Kiselman monoid and works out the directed-path/Catalan case. The present result uses that general characterization as an acknowledged premise and adds the nontrivial closed outward-star enumeration, sharp asymptotic correction, and the three equal-mass limiting regimes. It is **not** a new general classification of all endomorphisms, and the fact that the star-case count is in principle computable from the earlier general algorithm is explicitly acknowledged.

Wiertel (2024) supplies the source-vertex deletion identity used in the product calculus. Aragona and D'Andrea (2019/2020) study general normal forms. Forsberg (2012/2017) treats representations and certain other star-like type-A shapes, not this endomorphism count. The currently inspectable April 2026 manuscript did not state the closed formula or the limiting concentration law; later versions could contain additional comparisons not resolved here.

## Limitations

The statistic concerns endomorphism *counts*, not the internal composition structure or image-size distribution of the endomorphism monoid. It covers outward stars only. The asymptotic regime statement is a uniform counting statement, not a distributional statement about evaluation on individual monoid elements. Published equivalent formulas in unindexed sources or later manuscript versions remain a priority risk; independent external verification has not been performed.

## References

1. L. Andrenšek, *Endomorphisms of Hecke–Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497v1 (first public 2026-04-16), https://arxiv.org/abs/2604.15497 .
2. M. Wiertel, *Identities of Hecke–Kiselman monoids*, Semigroup Forum **109** (2024), 457–466, Lemma 4.1, https://doi.org/10.1007/s00233-024-10451-9 .
3. R. Aragona and A. D'Andrea, *Normal form in Hecke–Kiselman monoids associated with simple oriented graphs*, arXiv:1904.10745 (2019), https://arxiv.org/abs/1904.10745 .
4. L. Forsberg, *Effective representations of Hecke–Kiselman monoids of type A*, arXiv:1205.0676 (2012), https://arxiv.org/abs/1205.0676 .
5. O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316 (2010), https://arxiv.org/abs/1006.0316 .
