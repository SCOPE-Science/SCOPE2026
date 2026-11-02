# Dissociation polynomials and extremal configurations of circular ladders

## Finding
For every integer \(n\ge3\), the circular ladder \(Y_n=C_n\square K_2\) has dissociation-set polynomial
\[
D_n(z)=\sum_{S\subseteq V(Y_n):\;\Delta(Y_n[S])\le1}z^{|S|}
=[u^n]\left(-u\frac{\partial}{\partial u}\log Q(u,z)\right),
\]
where
\[
Q(u,z)=(1+zu+z^2u^2)\bigl(1-(1+z)u-(z+2z^2)u^2+(z^3-z^2)u^3+z^4u^4\bigr).
\]
Here \(\log Q\) is the formal power-series logarithm, since \(Q(0,z)=1\). Equivalently,
\[
\begin{aligned}
Q(u,z)={}&1-u-(2z+2z^2)u^2-(3z^2+2z^3)u^3-2z^3u^4\\
&+(2z^5-z^4)u^5+z^6u^6.
\end{aligned}
\]
For every \(n\ge9\),
\[
\begin{aligned}
D_n={}&D_{n-1}+(2z+2z^2)D_{n-2}+(3z^2+2z^3)D_{n-3}
+2z^3D_{n-4}\\
&+(z^4-2z^5)D_{n-5}-z^6D_{n-6}.
\end{aligned}
\]
The initial polynomials, for \(n=3,\ldots,8\), are respectively
\[
\begin{aligned}
D_3={}&1+6z+15z^2+6z^3,\\
D_4={}&1+8z+28z^2+32z^3+8z^4,\\
D_5={}&1+10z+45z^2+90z^3+75z^4+10z^5,\\
D_6={}&1+12z+66z^2+184z^3+261z^4+144z^5+22z^6,\\
D_7={}&1+14z+91z^2+322z^3+644z^4+658z^5+287z^6+28z^7,\\
D_8={}&1+16z+120z^2+512z^3+1316z^4+1968z^5+1568z^6+528z^7+48z^8.
\end{aligned}
\]
The largest possible dissociation set has \(n\) vertices. Exactly
\[
M_n=L_n+3\mathbf 1_{3\mid n}-1+2\mathbf1_{2\mid n}
\]
sets have size \(n\), where the Lucas numbers satisfy \(L_0=2\), \(L_1=1\), and \(L_n=L_{n-1}+L_{n-2}\).

## Assumptions and scope
The graph has vertex set \(\{(i,r):i\in\mathbb Z/n\mathbb Z,\ r\in\{0,1\}\}\). Two vertices are adjacent if their indices agree and layers differ (a rung), or their layers agree and cycle indices differ by one. All vertices and rung positions are labeled; the polynomial counts subsets, not unlabeled orbits. A dissociation set induces maximum degree at most one. The proof applies for every integer \(n\ge3\); no asymptotic inference or unverified finite extrapolation is used.

## Proof
**1. Exact cyclic transfer description.** Encode the selected vertices in rung \(i\) by a two-bit mask \(b_i\in\{0,1,2,3\}\), where the two bits indicate selection from the two layers. For neighboring masks \(a,b,c\), call the triple admissible when, for each layer \(r\) whose bit is selected in \(b\),
\[
\mathbf1_{\{r\in a\}}+\mathbf1_{\{1-r\in b\}}+\mathbf1_{\{r\in c\}}\le1.
\]
This is exactly the degree-at-most-one condition for the selected vertex in the middle rung: its three potential neighbors are the two horizontal neighbors and its vertical partner. All selected vertices of \(Y_n\) meet the condition precisely when every cyclic triple \((b_{i-1},b_i,b_{i+1})\) is admissible.

Index a \(16\)-by-\(16\) matrix \(T(z)\) by ordered pairs \((a,b)\) of masks and define
\[
T(z)_{(a,b),(b',c)}=
\begin{cases}
z^{\operatorname{popcount}(b)},&b=b'\text{ and }(a,b,c)\text{ admissible},\\
0,&\text{otherwise}.
\end{cases}
\]
For \(n\ge3\), there is a weight-preserving bijection between indexed cyclic rung-mask sequences and closed length-\(n\) walks in this pair-state matrix. Consequently \(D_n(z)=\operatorname{tr}T(z)^n\). This remains true for \(n=3\): its two horizontal neighboring rungs are distinct.

**2. Exact characteristic identity.** The finite, explicit matrix has
\[
\det(I-uT(z))=Q(u,z).
\]
This identity is independently reproducible by the attached standard-library verifier. Its check is **algebraically exhaustive**, not numerical interpolation alone: for every \(k\le16\), the coefficient of \(u^k\) in \(\det(I-uT(z))\) is a polynomial in \(z\) of degree at most \(2k\le32\), because each matrix entry has degree at most two. The verifier obtains all sixteen coefficients by integer Newton identities and exact integer matrix multiplication at each of the 33 distinct arguments \(z=0,1,\ldots,32\). At each argument they coincide with the claimed \(Q\), including its ten identically zero high-degree coefficients. Two polynomials of degree at most 32 agreeing at 33 arguments are identical; hence the determinant identity holds in \(\mathbb Z[u,z]\).

The formal trace–determinant identity
\[
-u\frac{\partial}{\partial u}\log\det(I-uT(z))
=\sum_{n\ge1}\operatorname{tr}(T(z)^n)u^n
\]
then establishes the displayed formula for every \(n\ge3\). Multiplying by \(Q\) and equating coefficients of \(u^n\) for \(n\ge9\) gives the six-step recurrence (the derivative numerator has degree at most six). The initial polynomials follow from the same identity.

**3. Maximum size and classification.** Classify each rung as empty, singleton, or double according to whether its mask contains zero, one, or two selected vertices. A double rung forces both adjacent rungs to be empty, since each vertex in the double rung already has its partner as a selected neighbor. Mapping every double rung to its right neighboring empty rung is injective. Thus the number of double rungs is no larger than the number of empty rungs. As
\[
|S|=n+(\#\text{double rungs})-(\#\text{empty rungs}),
\]
we obtain \(|S|\le n\). The alternating singleton assignment using two layers shows the bound is attained.

For equality, there must be equal numbers of empty and double rungs. If there are no double rungs then there are no empty rungs: all rungs are singleton. Write each selected layer as a binary symbol. The selected vertex in a singleton rung has two selected neighbors precisely when the symbols in that rung and its two cyclic neighbors coincide. Hence these optimum configurations are exactly cyclic binary strings avoiding triples of identical consecutive symbols.

If a double rung occurs, equality and the injection imply that every empty rung has a double rung immediately to its left. But each double rung also requires an empty rung immediately to its left; that latter empty rung must itself have a double rung to its left. Repeatedly traversing the cycle forces alternating double and empty rungs. This is possible only for even \(n\), and produces exactly two labeled assignments, each valid.

The first family is counted by the previously known cyclic binary-word sequence OEIS A007040: for \(n\ge3\), its count is \(L_n+2\) if \(3\mid n\), and \(L_n-1\) otherwise. Adding the exactly two even-order alternating configurations proves \(M_n=L_n+3\mathbf1_{3\mid n}-1+2\mathbf1_{2\mid n}\). Thus the maximum size is exactly \(n\), with the claimed complete structural classification.

## Verification
Run `python3 verify.py` under Python 3.9 or later using only the standard library. The verifier constructs the transfer matrix from the defining vertex-neighborhood predicate; establishes the determinant identity by 33 exact specializations and the polynomial-degree bound; exhaustively inspects all \(2^{2n}\) vertex subsets for \(3\le n\le10\), independently computing each entire dissociation polynomial; and compares the closed maximum-size count against transfer coefficients for \(3\le n\le35\). Its four terminal statuses are `EXACT_DETERMINANT_IDENTITY_OK`, `EXHAUSTIVE_SUBSETS_n3_TO_n10_OK`, `EXTREMAL_SEQUENCE_n3_TO_n35_OK`, and `VERIFY_OK`. The determinant interpolation argument and the structural proof, rather than the finitely many subset enumerations, establish the infinite claim.

## Relationship to prior work
Tu, Xiao, and Lang (published 23 February 2023) developed the dissociation polynomial for cubic graphs and established a sharp universal \(K_4\)-based upper bound for positive weights up to one. Their inspected paper does not give this specialized exact all-cardinality enumeration of prisms. The general algorithmic literature on dissociation and minimum three-path vertex covers addresses a broader class of graphs but does not yield the displayed polynomial or optimum-set multiplicity without additional analysis.

OEIS A007040 already records the cyclic binary-word count \(L_n+2\cos(2\pi n/3)\) and notes its separate interpretation using maximal independent sets of prisms. These facts are **credited, not claimed as new**. The present statement concerns all dissociation sets (selected subgraphs of maximum degree one), their full polynomial, and the two additional maximum configurations arising from double/empty rung alternation. Maximal independent sets and maximum dissociation sets are not the same invariant. Searches of the inspected sources and relevant scientific records did not identify a dominating earlier complete prism dissociation polynomial; this absence is not proof of publication priority.

## Limitations
The theorem concerns labeled circular ladders with \(n\ge3\); it neither enumerates isomorphism classes under dihedral symmetry nor covers arbitrary cubic graphs. The equivalent cyclic binary enumeration is prior art. Finite verification is not a substitute for the general proof; exact determinant certification is described separately from finite subset tests. Earlier unindexed or otherwise inaccessible work could contain equivalent results. No independent mathematical audit has been performed.

## References
1. J. Tu, J. Xiao, and R. Lang, “Counting the number of dissociation sets in cubic graphs,” *AIMS Mathematics* 8 (2023), 10021–10032, DOI: 10.3934/math.2023507; published 2023-02-23. https://www.aimspress.com/article/doi/10.3934/math.2023507
2. OEIS Foundation, sequence A007040, cyclic binary strings with no run of length three; includes 2017 prism maximal-independent-set interpretation. https://oeis.org/A007040
3. F. Kardoš, J. Katrenič, and I. Schiermeyer, “On computing the minimum 3-path vertex cover and dissociation number of graphs,” *Theoretical Computer Science* (2011), DOI: 10.1016/j.tcs.2011.09.009. https://doi.org/10.1016/j.tcs.2011.09.009
