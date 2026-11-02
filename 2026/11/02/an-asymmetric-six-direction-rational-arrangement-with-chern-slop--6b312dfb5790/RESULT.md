# An asymmetric six-direction rational arrangement with Chern-slope limit \(197/81\)

## Finding
Let the ordered primitive normal vectors and associated widths be
\[
(v_1,\ldots,v_6)=((1,0),(0,1),(1,1),(1,-1),(1,2),(2,1)),\qquad
(w_1,\ldots,w_6)=(2,2,2,1,1,1).
\]
For every positive integer \(n\) divisible by \(6\), let \(\mathcal A_n\) be the reduced arrangement of all projective lines
\[
v_i\cdot(X,Y)=tZ,\quad -w_i n\le t\le w_i n,\quad t\in\mathbb Z,\quad 1\le i\le6.
\]
The arrangement has \(d=18n+6\) distinct rational lines. Its finite intersection points, indexed by the exact multiplicity \(r\), have counts
\[
(e_2,e_3,e_4,e_5,e_6)=(23n^2+17n,\,14n^2+8n,\,7n^2+4n,\,n^2+n,\,n^2+n+1).
\]
There are no other finite multiple points. At infinity there are exactly three points of multiplicity \(4n+1\) and three points of multiplicity \(2n+1\). Consequently
\[
\bar c_1^{\,2}(\mathcal A_n)=197n^2+95n-13,\qquad
\bar c_2(\mathcal A_n)=81n^2+36n-4,
\]
and the slopes tend to \(197/81\). By the rational-field density lemma of Eterović--Figueroa--Urzúa, **every real number in** \([2,197/81]\) **is an accumulation point of logarithmic Chern slopes of rational projective line arrangements**.

## Assumptions and scope
All arrangements live in \(\mathbb P^2_{\mathbb Q}\). Only positive multiples of six are required; they form an unbounded sequence. The logarithmic Chern numbers are the incidence-theoretic ones of the cited source:
\[
\bar c_1^{\,2}=9-5d+\sum_{r\ge2}(3r-4)t_r,\qquad
\bar c_2=3-2d+\sum_{r\ge2}(r-1)t_r.
\]
The six primitive normal vectors are distinct up to scalar; hence the stated lines are distinct. The slope claim concerns accumulation points, not realization of every number as the slope of one finite arrangement.

## Proof
**1. Exact lattice counting.** For each subset \(S\subset\{1,\ldots,6\}\) of cardinality at least two, define
\[
P_S=\{(x,y)\in\mathbb R^2:|v_i\cdot(x,y)|\le w_i\ (i\in S)\},\quad
\Lambda_S=\{q\in\mathbb Q^2:v_i\cdot q\in\mathbb Z\ (i\in S)\}.
\]
Every pair of normals is independent, so \(P_S\) is a bounded polygon. The lattice \(\Lambda_S\) has covolume \(1/g_S\), where \(g_S\) is the greatest common divisor of the absolute pairwise determinants \(|\det(v_i,v_j)|\), for \(i,j\in S\). Indeed the normals span a sublattice of index \(g_S\) in \(\mathbb Z^2\), and \(\Lambda_S\) is its dual. The simultaneous intersections supported by all direction families in \(S\) are in bijection with \(nP_S\cap\Lambda_S\); write their number as \(F_S(n)\).

Every vertex of \(P_S\) is an intersection of two boundary lines \(v_i\cdot q=\pm w_i\); its coordinate denominator divides \(|\det(v_i,v_j)|\in\{1,2,3\}\). Thus every vertex of \(6P_S\) has integer coordinates, and hence belongs to \(\Lambda_S\). Ehrhart's theorem applied to the integral lattice polygon \(6P_S\) proves, for all \(n\in6\mathbb Z_{\ge0}\),
\[
F_S(n)=g_S\,\operatorname{area}(P_S)n^2+b_Sn+1,
\]
with a rational constant \(b_S\). No interpolation of an unproved nonpolynomial sequence is used.

**2. Exact 57-polygon area certificate.** The supplied standalone rational-arithmetic verifier enumerates each of the \(\sum_{s=2}^{6}\binom6s=57\) subsets, solves every pair of signed supporting-boundary equations, keeps precisely the feasible vertices, constructs their convex hull, and applies the shoelace formula. It proves the five exact sums
\[
\sum_{|S|=s}g_S\operatorname{area}(P_S)=
\begin{cases}132&s=2,\\72&s=3,\\27&s=4,\\7&s=5,\\1&s=6.\end{cases}
\]
The verifier checks that all vertices of all \(6P_S\) are integral. Every loop runs over an explicitly bounded finite set, with no numerical approximation.

**3. Fixing the linear coefficients exhaustively.** A second standalone verifier constructs all \(114\) lines of \(\mathcal A_6\), checks all \(\binom{114}{2}\) unordered pairs, and uses primitive integer homogeneous coordinates to identify equal projective intersection points. Every finite point on two or more lines appears in this complete pair enumeration. Its exact multiplicity census is
\[
(e_2(6),e_3(6),e_4(6),e_5(6),e_6(6))=(930,552,276,42,43).
\]
Write \(G_s(n)=\sum_{|S|=s}F_S(n)\). A point of multiplicity \(r\) contributes \(\binom rs\) to \(G_s(n)\). Using the census at \(n=6\), the area coefficients from step 2, and the constant term \(G_s(0)=\binom6s\) gives exactly
\[
\begin{aligned}
G_2(n)&=132n^2+90n+15,&G_3(n)&=72n^2+54n+20,\\
G_4(n)&=27n^2+24n+15,&G_5(n)&=7n^2+7n+6,\\
G_6(n)&=n^2+n+1.
\end{aligned}
\]
For every positive multiple of six, \(G_s(n)=\sum_{r=s}^6\binom rs e_r(n)\). Descending binomial inversion gives exactly the five displayed formulas for \(e_2,\ldots,e_6\). In particular, these formulas are valid for **all** admissible \(n\), not merely those enumerated.

**4. Infinity and Chern classes.** For each normal direction, all lines meet in one point on \(Z=0\). The six normals are pairwise nonparallel, so there are precisely six such points: three have \(2(2n)+1=4n+1\) incident lines and three have \(2n+1\). Substituting the five finite multiplicity polynomials and these six points into the defining Chern formulas yields
\[
\bar c_1^{\,2}=197n^2+95n-13,\quad \bar c_2=81n^2+36n-4.
\]
As a consistency identity, \(\sum_{r\ge2}\binom r2t_r=\binom{18n+6}{2}\). The checker verifies this identity independently for \(n=6,12\).

**5. Accumulation interval.** Along \(6\mid n\), \(d(n)=18n+6\to\infty\), the slope tends to \(c=197/81>2\), and
\[
\lim_{6\mid n,\ n\to\infty}\bar c_1^{\,2}(\mathcal A_n)/d(n)^2=197/324>0.
\]
Apply Eterović--Figueroa--Urzúa [1, Lemma 4.2] over the infinite field \(\mathbb Q\), with exponent \(h=2\), to conclude that the accumulation set contains the full interval \([2,197/81]\).

## Verification
Run `python3 verify_areas.py` to reproduce all \(57\) exact rational polygon areas and the five aggregate coefficients. Run `python3 verify_incidence.py` to independently enumerate all intersection pairs at \(n=6,12\), check the exact Chern values, and verify the complete pair-count identity including points at infinity. Both scripts use only the Python standard library. The finite tests at \(n=6\) are an exhaustive finite certificate used **together with** the unrestricted Ehrhart proof, not a claimed infinite experimental induction.

## Relationship to prior work
Eterović--Figueroa--Urzúa [1, Example 4.5] gave a rational construction of asymptotic slope \(19/8\), and [1, Lemma 4.2] proved the density mechanism used in step 5. A previously established equal-width version of these six normal directions has limiting slope \(43/18\). The present asymmetric width vector produces the strictly larger endpoint \(197/81\), improving it by \(7/162\). Root-system and deformed-Catalan characteristic-polynomial literature studies related normal arrangements; no originality is claimed for the list of six directions, nor for the general Ehrhart or density tools. The contribution assessed here is the **specific complete asymmetric-width projective multiplicity census and its strict rational Chern-slope extension**.

## Limitations
This establishes a lower interval of accumulation points, not the optimal rational endpoint or a classification of all rational arrangements. The full projective census is asserted only for positive multiples of six. No assertion about characteristic-positive reductions is made. Unindexed prior calculations of deformed root-arrangement incidence multiplicities remain a possible originality risk. No independent external scientific validation is claimed.

## References
[1] S. Eterović, F. Figueroa, G. Urzúa, *On the geography of line arrangements*, arXiv:1805.00990 (first posted 2018-05-02), especially Section 3 and Section 4, Lemma 4.2, Example 4.5. https://arxiv.org/abs/1805.00990

[2] The standard Ehrhart lattice-polygon theorem, used only after verifying integrality of each dilated polygon.
