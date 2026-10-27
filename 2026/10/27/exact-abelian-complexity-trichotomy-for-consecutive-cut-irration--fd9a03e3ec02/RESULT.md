# Exact Abelian-complexity trichotomy for consecutive-cut irrational rotation codings

## Finding
Fix an integer \(m\ge 3\) and an irrational real number \(0<\alpha<1/m\). Partition the circle \(\mathbb T=\mathbb R/\mathbb Z\) into \(m+1\) half-open intervals
\[
I_j=[j\alpha,(j+1)\alpha),\quad 0\le j<m,\qquad I_m=[m\alpha,1).
\]
Let \(w\) code any orbit of rotation \(x\mapsto x+\alpha\pmod 1\) by these intervals. Write \(p_w(n)\) for the number of distinct length-\(n\) factors and \(\rho_w(n)\) for the number of their distinct Parikh vectors (letter-multiplicity vectors). For all integers \(n\ge1\),
\[
p_w(n)=n+m,\qquad
\rho_w(n)=\begin{cases}
m+n,&1\le n<m,\\
2m,&n\ge m\text{ and }\alpha<\{n\alpha\}<1-\alpha,\\
m+1,&n\ge m\text{ and }\{n\alpha\}\in(0,\alpha)\cup(1-\alpha,1).
\end{cases}
\]
For \(n\ge m\), the middle case has natural density \(1-2\alpha\), and the last case has natural density \(2\alpha\). In particular the Abelian complexity oscillates between the two distinct values \(m+1\) and \(2m\) infinitely often, even though ordinary factor complexity is always \(n+m\).

## Assumptions and scope
The alphabet is precisely \(\{0,1,\dots,m\}\); interval endpoints are taken with the specified half-open convention. Irrationality guarantees minimality of the rotation and hence independence of the language from the orbit's initial phase (including phases on partition boundaries). No claim is made for rational angles or nonconsecutive cut patterns. The frequencies of symbols \(0,\dots,m-1\) are all \(\alpha\), and the last symbol has frequency \(1-m\alpha\); in particular the frequency vector has rational dependencies.

## Proof
**1. Letter counts reduce to a moving arc.** Fix \(j<m\), a phase \(x\in\mathbb T\), and put \(p_j=(j+1)\alpha\pmod1\). Since \(I_j\) is a translate of \([0,\alpha)\), a telescoping floor identity gives its number \(N_j(x,n)\) of visits during the first \(n\) iterates:
\[
N_j(x,n)=\lfloor x+(n-1-j)\alpha\rfloor-\lfloor x-(j+1)\alpha\rfloor.
\]
Writing \(n\alpha=L+t\) with \(L\in\mathbb Z_{\ge0}\), \(t=\{n\alpha\}\in(0,1)\), we obtain away from endpoints
\[
N_j(x,n)=L+\mathbf1_{(p_j-t,p_j]}(x).
\]
The count of the remaining symbol is \(n-\sum_{j<m}N_j(x,n)\), so two factors have the same Parikh vector exactly when their phase arcs of length \(t\) capture the same subset of the \(m\) marked points \(p_0,p_1,\ldots,p_{m-1}\). Those points have \(m-1\) successive gaps of length \(\alpha\) and one gap of length \(G=1-(m-1)\alpha>\alpha\).

**2. Count the captured subsets.** As the moving arc travels once around the circle, its start and end pass the \(m\) marks. If no endpoints coincide, this makes \(2m\) phase chambers. Distinct chambers produce distinct captured sets, with only the possible exception of a repeated empty set or a repeated full set: for any nonempty proper consecutive block of marked points, its beginning and ending must lie in the two uniquely determined neighboring gaps, at least one of which has length \(\alpha\); the possible starting phases therefore form one connected interval. Because only the long gap has length exceeding \(\alpha\), empty-set chambers can repeat only when \(t<\alpha\), in which case all \(m\) gaps permit an empty arc and there are \(m\) chambers with the empty set. Likewise full-set chambers repeat only when \(1-t<\alpha\), in which case the same \(m\) gaps accommodate the complementary arc. In either case the \(m\) identical chambers reduce the count by \(m-1\), giving \(m+1\) distinct subsets; otherwise all \(2m\) subsets are different. Since \(m\ge3\), \(\alpha<1/3\), so the two repeated-chamber regimes are disjoint.

For an integer \(1\le n<m\), the arc length equals \(t=n\alpha\); then the endpoint for mark \(p_j\) at one end agrees with the endpoint for \(p_{j-n}\) at the other end, for each \(j\ge n\). There are exactly \(m-n\) such coincidences, hence \(m+n\) chambers. These chambers have different captured subsets: the same one-interval argument eliminates repeat nonempty proper subsets, and the short-gap geometry yields at most one empty or full chamber at these lengths. For \(n\ge m\), irrationality rules out \(\{n\alpha\}=k\alpha\) or \(1-k\alpha\) for any \(1\le k<m\), so the generic \(2m\)-endpoint count applies. This proves the stated Abelian complexity profile.

**3. Ordinary factor complexity.** The discontinuity points of the length-\(n\) coding are precisely the \(n+m\) distinct orbit points \(\{-k\alpha:0\le k<n\}\) together with \(\{j\alpha:1\le j\le m\}\), equivalently one consecutive run of orbit points indexed from \(-(n-1)\) through \(m\). They partition \(\mathbb T\) into \(n+m\) nonempty phase intervals. Each distinct length-\(n\) coding cylinder is one such interval: if its word contains a special symbol \(j<m\), the phase lies in a shifted interval of length \(\alpha<1/3\), and intersections of the remaining translated short intervals (or their complementary connected long intervals) cannot create two separated components within it; if the word is composed entirely of the symbol \(m\), the consecutive excluded short strips combine into one contiguous circular arc, so its complement is connected. Thus different chambers carry different words. Minimality makes them all appear in every coding \(w\). Therefore \(p_w(n)=n+m\).

**4. Density of the regimes.** Weyl's equidistribution theorem for irrational rotations gives that \(\{n\alpha\}\) visits \((\alpha,1-\alpha)\) with natural density \(1-2\alpha\) and its complementary open arcs with density \(2\alpha\). The finitely many \(n<m\) do not affect the densities; there are no endpoint equalities for \(n\ge m\).

## Verification
The attached standalone `verify.py` uses exact integer phase arithmetic with a prime-period rational proxy. It independently enumerates full factor words and Parikh vectors in every phase chamber for \(2\le m\le11\), all selected slopes \(p/10007\) with \(1\le p<70\) satisfying \(mp<10007\), and \(1\le n\le31\). It checks both formulas and terminates with `VERIFY_OK`. These are finite examples, not a substitute for the preceding irrational-angle argument.

## Relationship to prior work
Bédaride–Berthé–Julien (arXiv:2502.18211, publicly available 2025-02-25) investigate symbol balance and discrepancy for hypercubic billiard codings, not this explicit single-circle, \(m+1\)-symbol Abelian complexity profile. Andrieu–Vivion (arXiv:2605.01577, 2026-05-02) prove nonexistence of constant minimal Abelian complexity with rationally independent frequency vectors; the strongly dependent frequencies here fall outside those hypotheses. Karhumäki–Puzynina–Whiteland (arXiv:2012.14701, Section 4) investigate Abelian closures for nonbinary minimal-complexity words and the related ternary two-cut rotation model; their ternary heavy/light pattern result is credited. The finding concerns the complete many-cut profile for every \(m\ge3\) and its exact length-frequency law, neither explicitly supplied by these sources.

## Limitations
The construction is a constrained, highly dependent-frequency family, not a classification of all \(m+1\)-symbol rotation codings. The result does not settle any rationally independent alphabet-frequency problem. Historical priority under minimal-complexity substitutions or multidimensional Parikh-vector language remains a risk. Independent verification has not been performed.

## References
1. N. Bédaride, V. Berthé, A. Julien, *On balance properties of hypercubic billiard words*, arXiv:2502.18211v1, 2025-02-25, https://arxiv.org/abs/2502.18211 .
2. M. Andrieu, L. Vivion, *A proof of Rauzy’s conjecture on abelian complexity*, arXiv:2605.01577v1, 2026-05-02, https://arxiv.org/abs/2605.01577 .
3. J. Karhumäki, S. Puzynina, M. A. Whiteland, *On Abelian Closures of Infinite Non-binary Words*, arXiv:2012.14701v1, 2020-12-29, https://arxiv.org/abs/2012.14701 .
