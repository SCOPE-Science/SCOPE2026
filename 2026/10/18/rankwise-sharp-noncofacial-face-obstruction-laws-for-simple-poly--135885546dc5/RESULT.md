# Rankwise sharp noncofacial-face obstruction laws for simple polytopes with one extra facet

## Finding

Let \(d\ge2\). A **noncofacial obstruction of rank \(k\)** in a \(d\)-polytope \(P\) is an **ordered** pair \((F,G)\) of nonempty proper faces satisfying \(\dim F\le k-1\) and \(\dim G\le d-k-1\) such that no proper face of \(P\) contains both. Put \(N_k(P)\) equal to their number, for \(1\le k\le d-1\).

**Theorem.** Let \(P\) be a simple \(d\)-polytope with exactly \(d+2\) facets. The standard combinatorial classification writes \(P\cong\Delta_p\times\Delta_q\), with \(p,q\ge1\) and \(p+q=d\). Put
\[
G_m(z)=(1+z)^m-1-z^m.
\]
Then the complete rank profile is
\[
N_k(\Delta_p\times\Delta_q)=[z^{k+1}]G_{p+1}(z)G_{q+1}(z)
=\sum_{\substack{1\le a\le p\\1\le k+1-a\le q}}\binom{p+1}{a}\binom{q+1}{k+1-a}.
\]
Every obstruction has \(\dim F=k-1\) and \(\dim G=d-k-1\) exactly. If \(1\le p\le q-2\), then
\[
N_k(\Delta_{p+1}\times\Delta_{q-1})>N_k(\Delta_p\times\Delta_q)
\qquad (1\le k\le d-1).
\]
Thus all ranks simultaneously attain their unique minimum (up to factor swapping) at the simplex prism \(\Delta_1\times\Delta_{d-1}\), where \(N_k=2\binom d k\), and their unique maximum at the balanced product \(\Delta_{\lfloor d/2\rfloor}\times\Delta_{\lceil d/2\rceil}\). The exact total is
\[
\sum_{k=1}^{d-1}N_k=4(2^p-1)(2^q-1).
\]
In particular, it has the sharp lower value \(4(2^{d-1}-1)\), and the sharp upper value \(4(2^{\lfloor d/2\rfloor}-1)(2^{\lceil d/2\rceil}-1)\).

## Assumptions and scope

A simple polytope has exactly \(d\) facets incident with each vertex. The theorem concerns only \(d\ge2\), exactly \(d+2\) facets, and the **face lattice** of the polytope. For \(d=2\) the unique type is a quadrilateral, and both extremal classes coincide. Faces must be nonempty and proper; a face may have either product factor full. An ordered pair is counted once with its specified first and second components, even when \(k=d-k\).

The source of the obstruction definition is the complementary face-dimension criterion in Fryš–Kotrbatý–Mouamine–Wang, Theorem 1.4. The criterion itself, in the polyhedral setting, dates at least to Develin's 2004 disjoint-faces theorem. The new claim is the simultaneous exact rank-count and its strict product-balance order at the first possible facet excess, not a new qualitative characterization of simplices.

## Proof

**1. Reduction to two simplex factors.** By the classical one-dimensional Gale-diagram classification of simplicial \(d\)-polytopes with \(d+2\) vertices, the polar of a simple \(d\)-polytope with \(d+2\) facets has two nonempty Gale sign classes, each of size at least two. Dualizing identifies its face lattice with \(\Delta_p\times\Delta_q\), where the class sizes are \(p+1\) and \(q+1\). The restriction that the polar is simplicial excludes zero Gale entries (which would give a non-simplex base facet of a pyramid). The factor pair is unique up to interchange. This standard classification is also a special case of the familiar structural theory of products of simplices [3].

**2. Classification and enumeration of obstructions.** Write the vertex sets of the two factors as \(I,J\), with \(|I|=p+1\), \(|J|=q+1\). Every nonempty face is uniquely \(\operatorname{conv}(A)\times\operatorname{conv}(B)\), where \(\emptyset\ne A\subseteq I\) and \(\emptyset\ne B\subseteq J\); its dimension is \(|A|+|B|-2\). For faces corresponding to \((A,B)\) and \((C,D)\), their smallest containing face is
\[
\operatorname{conv}(A\cup C)\times\operatorname{conv}(B\cup D).
\]
Hence they fail to have a common proper face exactly if \(A\cup C=I\) and \(B\cup D=J\).

Their dimension bounds give
\[
(|A|+|B|)+(|C|+|D|)\le (k+1)+(d-k+1)=d+2=|I|+|J|.
\]
The covering conditions give the reverse inequality. Equality follows throughout, forcing \(A,C\) to be disjoint complementary nonempty subsets of \(I\), and likewise \(B,D\) to be disjoint complementary nonempty subsets of \(J\). Both face dimensions are therefore exactly their respective upper bounds. For \(a=|A|\), \(b=|B|\), one has \(1\le a\le p\), \(1\le b\le q\), and \(a+b=k+1\). There are \(\binom{p+1}{a}\binom{q+1}{b}\) ordered choices. This proves the generating polynomial and coefficient formula.

**3. Strict coefficientwise balancing.** Write \(m=p+1\), \(\ell=q+1\), assume \(\ell\ge m+2\), and use the identity
\[
G_{j+1}=(1+z)G_j+z+z^j.
\]
The difference between the more balanced and the original profiles is
\[
G_{m+1}G_{\ell-1}-G_mG_\ell
=z(G_{\ell-1}-G_m)+z^mG_{\ell-1}-z^{\ell-1}G_m.
\]
The first summand has strictly positive coefficients at degrees \(2,\ldots,\ell-1\) and none outside. In the last two summands there is no negative coefficient below degree \(\ell\). At every degree \(j=\ell,\ldots,m+\ell-2\), put \(r=j-\ell+1\), so \(1\le r\le m-1\). Their combined coefficient equals
\[
\binom{\ell-1}{j-m}-\binom{m}{j-\ell+1}
=\binom{\ell-1}{m-r}-\binom{m}{m-r}>0,
\]
because \(\ell-1>m\) and \(1\le m-r\le m-1\). Thus the whole polynomial difference has strictly positive coefficients in each degree \(2,\ldots,m+\ell-2=d\). This proves simultaneous strict improvement at every rank.

**4. Sharp extrema.** Repeated balancing takes any unordered pair \((p,q)\) toward the unique balanced pair and strictly raises all rank counts unless already balanced. Reversing this chain takes it to \((1,d-1)\), strictly lowering all ranks. For the prism,
\[
G_2(z)G_d(z)=2z\big((1+z)^d-1-z^d\big),
\]
whose degree-\(k+1\) coefficient is \(2\binom dk\). Finally, evaluating the generating polynomial at \(z=1\) gives the total and its sharp endpoint values.

## Verification

The standalone `checker.py` enumerates all nonempty proper product faces and tests each ordered pair's smallest containing face, without using the proposed generating formula. It compares this enumeration with the exact binomial expression for all factor pairs up to dimension seven (91 rank-and-factor checks). Independent exact-integer assertions test coefficientwise balancing and the prism minimum through dimension 49. It prints a PASS summary when all tests succeed. The displayed universal statements follow from the preceding argument, not from finite enumeration.

## Relationship to prior work

Fryš, Kotrbatý, Mouamine, and Wang [1], Theorem 1.4, characterize simplices through the **absence** of every such obstruction for any fixed rank. Their article explicitly credits Develin [2] for the earlier polyhedral criterion. Neither theorem gives the polynomial distribution of obstruction counts or simultaneous rankwise extremality across the simple polytopes with one more facet than a simplex. Yu and Masuda [3] provide structural theory for combinatorial products of simplices, which is a classification input but does not supply the rankwise incidence count. The resulting exact profile is different from opposite-body mixed-volume deficits or facet-assignment questions: no metric or numerical mixed volume enters the definition.

## Limitations

The classification and strict balance order hold only for simple polytopes with exactly \(d+2\) facets. No claim is made that the prism minimizes this count over polytopes with more facets, nor that these integer counts quantitatively control the Godbersen mixed-volume difference. Prior independent discovery of the same count or coefficientwise order in unindexed polytope-combinatorics literature has not been excluded. The finite checker is a reproducibility supplement and does not certify all dimensions by exhaustive computation.

## References

1. F. Fryš, J. Kotrbatý, M. A. Mouamine, S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806, first submitted 2026-10-05, Theorem 1.4.
2. M. Develin, *Disjoint Faces of Complementary Dimension*, Beiträge zur Algebra und Geometrie 45 (2004), 463–464.
3. L. Yu, M. Masuda, *On Descriptions of Products of Simplices*, Chinese Annals of Mathematics, Series B (2021), structural criteria for simple products of simplices.
