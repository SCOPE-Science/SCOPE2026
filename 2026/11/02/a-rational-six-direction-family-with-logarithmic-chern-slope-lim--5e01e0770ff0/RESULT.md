# A rational six-direction family with logarithmic Chern-slope limit \(43/18\)

## Finding
Let \(V=((1,0),(0,1),(1,1),(1,-1),(1,2),(2,1))\). For every positive integer \(n\) divisible by \(6\), let \(\mathcal A_n\) be the arrangement of the \(12n+6\) distinct rational lines
\[
 aX+bY-tZ=0,\qquad (a,b)\in V,\quad t\in\{-n,-n+1,\ldots,n\}
\]
in \(\mathbb P^2_{\mathbb Q}\). For \(n\ge6\), write \(u=n(n+1)\). The entire projective intersection-multiplicity census is
\[
 t_2=14u,\quad t_3=5u,\quad t_4=u,\quad t_5=u,\quad
 t_6=u+1,\quad t_{2n+1}=6,
\]
with all other \(t_m\) zero. Its logarithmic Chern numbers are exactly
\[
 \overline c_1^{\,2}(\mathcal A_n)=86n^2+62n-13,
 \qquad \overline c_2(\mathcal A_n)=36n^2+24n-4.
\]
Consequently, the logarithmic Chern slope tends to \(43/18\), exceeding the rational value \(19/8\) exhibited in the motivating 2018 literature by \(1/72\). Using the previously established density lemma for rational line arrangements, every number in \([2,43/18]\) is an accumulation point of logarithmic Chern slopes of arrangements defined over \(\mathbb Q\). The claim is about an explicit infinite family and its resulting interval, not the optimal possible endpoint.

## Assumptions and scope
The base field is \(\mathbb Q\), with geometric intersections counted in its algebraic closure (all intersections here are rational). We take \(n\in6\mathbb Z_{>0}\), so the infinity multiplicity \(2n+1\) does not coincide with any finite multiplicity, which is at most six. An \(m\)-point means a projective point incident to exactly \(m\) distinct arrangement lines. The logarithmic Chern numbers are those of the reduced total transform of the arrangement on the blow-up of its intersection points of multiplicity at least three. The standard combinatorial formula for these invariants is recalled in the proof.

## Proof
**Distinct lines and points at infinity.** Each pair of distinct vectors in \(V\) has nonzero determinant, so the six directions are distinct. Lines of a fixed direction have distinct offsets. Exactly \(2n+1\) lines meet in the unique point of that direction on \(Z=0\), giving six points with multiplicity \(2n+1\). No finite point can lie on two different members of the same parallel family, so its multiplicity is between two and six.

**Counting all finite intersections by rational polygons.** For every subset \(S\subseteq V\) of size \(j\ge2\), set
\[
 \Lambda_S=\{(x,y)\in\mathbb Q^2: ax+by\in\mathbb Z\text{ for all }(a,b)\in S\},
\qquad
 P_S=\{(x,y)\in\mathbb R^2:|ax+by|\le1\text{ for all }(a,b)\in S\}.
\]
A finite point lies on one line from each family in \(S\) exactly when it lies in \(nP_S\cap\Lambda_S\). Denote this count by \(N_S(n)\). Each \(P_S\) is a centrally symmetric convex polygon. Its vertices are among the intersections of the finitely many pairs of boundary lines \(ax+by=\pm1\). The nonzero determinants of the six primitive directions have absolute value at most three and divide six. Thus every vertex of \(6P_S\) has integral coordinates, hence lies in \(\Lambda_S\). Pick's theorem, or the lattice-polygon Ehrhart formula, therefore applies whenever \(6\mid n\):
\[
 N_S(n)=g_S\operatorname{area}(P_S)n^2+\frac{B_S}{12}n+1,
 \qquad
 g_S=\gcd\{|\det(v,w)|:v,w\in S,\ v\ne w\},
\]
where \(B_S\) is the number of boundary lattice steps of \(6P_S\) relative to \(\Lambda_S\). Indeed the covolume of \(\Lambda_S\) in ordinary Euclidean coordinates is \(1/g_S\). For an edge \(p\!\to\!q\) of \(6P_S\), the step count is precisely
\[
 \gcd\{|v\cdot(q-p)|:v\in S\},
\]
since a rational multiple of the edge difference belongs to \(\Lambda_S\) exactly when each scalar product is integral. This gives a finite, exact, reproducible algorithm for all the necessary Ehrhart coefficients.

Summing these expressions over all subsets of each cardinality gives the following **complete exact arithmetic certificate**, where \(M_j(n)=\sum_{|S|=j}N_S(n)\):
\[
\begin{array}{c|c}
 j&M_j(n)\\\hline
2&60n(n+1)+15\\
3&39n(n+1)+20\\
4&21n(n+1)+15\\
5&7n(n+1)+6\\
6&n(n+1)+1
\end{array}
\]
The stand-alone `verify_ehrhart.py` computes the polygons, signed areas, edge lattice lengths, and all \(57\) subset coefficients with exact rational arithmetic and checks precisely these five polynomial identities. Its convexity and integral-vertex assertions are also performed with exact arithmetic. Hence the displayed identities are finite, exhaustive, and not inferred from a numerical pattern.

A finite point of multiplicity \(m\) appears exactly \(\binom mj\) times in \(M_j\), so \(M_j(n)=\sum_{m=j}^{6}\binom mj t_m^{\rm finite}(n)\). Descending binomial inversion from \(j=6\) to \(j=2\) gives
\[
 (t_2^{\rm finite},t_3^{\rm finite},t_4^{\rm finite},t_5^{\rm finite},t_6^{\rm finite})
 =(14u,5u,u,u,u+1).
\]
Adding the six infinity points gives the claimed projective census. The independent incidence checker `verify_intersections.py` directly constructs all \(\binom{12n+6}{2}\) line-pair intersections in primitive integer projective coordinates and reproduces the complete census for \(n=6,12,18,24\), without using the polygon computations. The general theorem rests on the preceding exact Ehrhart argument, not on these four finite experiments.

**Chern numbers and accumulation.** For any nontrivial arrangement of \(d\) lines, the standard formulas are
\[
 \overline c_1^{\,2}=9-5d+\sum_{m\ge2}(3m-4)t_m,
 \qquad
 \overline c_2=3-2d+\sum_{m\ge2}(m-1)t_m.
\]
Substituting \(d=12n+6\), the five finite multiplicities, and the six points of multiplicity \(2n+1\), gives \(\overline c_1^{\,2}=86n^2+62n-13\) and \(\overline c_2=36n^2+24n-4\). In particular, their ratio tends to \(43/18>19/8\). Since the line count tends to infinity and \(\overline c_1^{\,2}/d^2\) tends to \(86/144>0\), the hypotheses of Eterović–Figueroa–Urzúa, Lemma 4.2, hold with exponent two and base field \(\mathbb Q\). That published lemma establishes density throughout \([2,43/18]\), including the endpoints as accumulation points.

## Verification
Run `python3 verify_ehrhart.py` and `python3 verify_intersections.py` from this directory, using only the Python standard library. The exact-polygon run prints `EXACT_EHRHART_CERTIFICATE_OK`; the independently constructed projective incidence run prints `INDEPENDENT_PROJECTIVE_CENSUS_OK`. Both were executed successfully. The polygon checker also verifies the projective pair identity \(\sum_m\binom m2t_m=\binom d2\) at four sample widths. No external computer algebra, downloadable data, or non-embedded artifacts are required.

## Relationship to prior work
Eterović, Figueroa, and Urzúa (2018/2019), Example 4.5, produce a **four-direction rational** family whose limit is \(19/8\); their Lemma 4.2 already gives density below any independently established endpoint. Urzúa (2022), Question 2.2, records \([2,19/8]\) as the known rational density interval and asks whether the full real interval \([2,5/2]\) occurs. The present result extends the **verified explicit endpoint** to \(43/18\), not to \(5/2\).

There is an important classical equivalence: the unimodular substitution \((a,b)\mapsto(a+b,b)\) sends the six normal directions to the six positive-root directions of type \(G_2\). Hence the affine construction is an extended \(G_2\) Catalan arrangement. Athanasiadis (2004), Theorem 1.2, already computes characteristic polynomials for this root-system arrangement, and in rank two this determines the weighted sum \(\sum_m(m-1)t_m^{\rm finite}\); it does **not** by itself determine the individual intersection multiplicities or the unweighted number of finite intersection points necessary for \(\overline c_1^{\,2}\). The contribution claimed here is the explicit all-multiplicity census and its *logarithmic Chern-slope geography*, not discovery of the classical root-system arrangement or its characteristic polynomial. The prior theorem's stronger algebraic nature is acknowledged without attributing to it a Chern-slope calculation that it does not state.

## Limitations
The census and formulas are asserted only for positive \(n\) divisible by six. The resulting accumulation statement is a **lower inclusion** for the rational slope accumulation set, not an optimality or maximality theorem. The exact Ehrhart checker is a transparent exhaustive finite verification of the \(57\) subset computations, justified by an algebraic lattice-polygon argument; the independent enumerations at four widths alone would not prove the infinite family. Classic \(G_2\) arrangement literature is extensive, and an earlier unindexed calculation of the complete incidence census or a stronger rational Chern-slope result may exist. No independent external mathematical audit has been performed.

## References
1. S. Eterović, F. Figueroa, G. Urzúa, *On the geography of line arrangements*, arXiv:1805.00990, first public May 2, 2018; revised 2019. Especially Definition 3.1, Lemma 4.2, Example 4.5. https://arxiv.org/abs/1805.00990
2. G. Urzúa, *Some open questions about line arrangements in the projective plane*, Proyecciones 41 (2022), 517–536, DOI:10.22199/issn.0717-6279-5277, especially Question 2.2. https://www.scielo.cl/pdf/proy/v41n2/0716-0917-proy-41-02-517.pdf
3. C. A. Athanasiadis, *Generalized Catalan Numbers, Weyl Groups and Arrangements of Hyperplanes*, Bull. Lond. Math. Soc. 36 (2004), 294–302, DOI:10.1112/S0024609303002856, especially Theorem 1.2. https://sites.math.washington.edu/~billey/classes/lie/bulletins/athanasiadis.04.pdf
4. B. Naskręcki, P. Pokora, *On the geography of log-surfaces*, arXiv:2412.14635 (first public December 19, 2024), overview of logarithmic Chern geography. https://arxiv.org/abs/2412.14635
