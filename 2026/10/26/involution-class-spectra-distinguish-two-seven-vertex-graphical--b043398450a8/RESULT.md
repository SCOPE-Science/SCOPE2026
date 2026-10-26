# Involution-class spectra distinguish two seven-vertex graphical groups with identical ordinary class-size spectra

## Finding
Let \(q=2^f\) for any integer \(f\ge1\). For a finite simple graph \(\Gamma=(V,E)\), let \(G_\Gamma(q)=1+J_\Gamma\), where \(J_\Gamma\) is the associative \(\mathbb F_q\)-algebra with basis \(x_v\) for \(v\in V\) and \(z_{uv}\) for edges \(\{u,v\}\in E\), using the order \(u<v\), with \(x_ux_v=z_{uv}\) on edges \(u<v\) and every other product of basis elements zero. This realizes the usual graphical group. Put \(e=|E|\).

For every independent set \(S\subseteq V\), write \(N(S)\) for its *external open neighborhood*, namely all vertices outside \(S\) adjacent to a vertex in \(S\). The conjugacy-class-size enumerator on elements whose order divides two (including the identity) is
\[
H_\Gamma(q,T)=\sum_{\substack{S\subseteq V\\S\text{ independent}}}(q-1)^{|S|}q^{e-|N(S)|}T^{|N(S)|}.
\]
Here \([T^r]H_\Gamma(q,T)\) is the number of conjugacy classes *contained in the order-at-most-two locus* having cardinality \(q^r\). To count classes of elements of order exactly two, subtract one from the coefficient of \(T^0\) (the identity class).

Consider the following distinct graphs on \(V=\{0,1,2,3,4,5,6\}\), each with eight edges:
\[
\begin{aligned}
E_A&=\{01,03,04,13,14,16,24,25\},\\
E_B&=\{01,02,04,05,12,23,45,56\}.
\end{aligned}
\]
Each two-digit symbol represents an unordered pair of the listed vertices. These graphs have **the same number of ordinary conjugacy classes of every possible size** for every prime power \(q\), and, for every even \(q\), the **same number of elements of order at most two**. Nevertheless, their order-at-most-two conjugacy-class spectra differ by the nonzero identity
\[
\boxed{H_A(q,T)-H_B(q,T)=q^3(q-1)^2T^2(T-q)^3.}
\]
Therefore \(G_A(q)\) and \(G_B(q)\) are nonisomorphic for every even \(q\), despite sharing their complete ordinary conjugacy-class-size spectra and their involution counts.

For example, over \(\mathbb F_2\), the coefficients of \(T^0,T^1,T^2,T^3,T^4,T^5\) in \(H_A\) are \(256,256,256,416,112,16\), whereas those in \(H_B\) are \(256,256,320,320,160,8\). Both groups have \(7424\) elements of order at most two and group order \(32768\).

## Assumptions and scope
All graphs are finite, simple and undirected; loops and multiple edges are excluded. The universal involution formula holds for any finite graph, including disconnected graphs and isolates, over every finite field of characteristic two. The two-graph separation uses exactly the labeled edge sets above. The assertion about equal *ordinary* class-size spectra remains true for every prime power, whereas the involution refinements are asserted only in characteristic two. We distinguish ordinary conjugacy classes from conjugacy classes meeting the order-two locus; conjugacy preserves order, so each such class is entirely contained in it.

## Proof
Write \(a=\sum_{v\in V}a_vx_v+\sum_{u<v}c_{uv}z_{uv}\in J_\Gamma\). Every element of \(G_\Gamma(q)\) has the unique form \(1+a\), and \(J_\Gamma^3=0\). In characteristic two, \((1+a)^2=1+a^2\), with
\[
a^2=\sum_{\{u,v\}\in E,\ u<v}a_ua_vz_{uv}.
\]
The \(z_{uv}\) are linearly independent, so \((1+a)^2=1\) if and only if the support \(S=\{v:a_v\ne0\}\) is independent. Every such support occurs with exactly \((q-1)^{|S|}\) vertex-coordinate assignments and \(q^e\) unrestricted central-coordinate assignments.

For fixed \(a\) and another group element with vertex coordinates \(b_v\), commutation is equivalent to
\[
a_ub_v-a_vb_u=0 \qquad(\{u,v\}\in E,\ u<v).
\]
If \(S\) is independent, every nonzero equation has precisely one nonzero coefficient \(a_u\) or \(a_v\), and hence forces the coordinate \(b_w=0\) for a vertex \(w\in N(S)\). Conversely these vanishing coordinates satisfy all equations. Thus the centralizer has order \(q^{|V|+e-|N(S)|}\) and the conjugacy class has cardinality \(q^{|N(S)|}\). Dividing the number of elements of each support by their common orbit size establishes the formula for \(H_\Gamma\) with no restriction on the graph's size.

To prove the finite distinction rigorously, for every one of the \(128\) subsets \(S\subseteq V\) compute \(s=|S|\) and
\[
\rho_\Gamma(S)=|S\cup N(S)|-c(\Gamma[S]),
\]
where \(c(\Gamma[S])\) is the number of connected components of the induced graph, with \(c(\varnothing)=0\). The complete exhaustive table in `CERTIFICATE.json` gives identical histograms \(h_\Gamma(s,r)=\#\{S:|S|=s,\rho_\Gamma(S)=r\}\) for \(A\) and \(B\). In particular Rossmann's ordinary graphical-group class formula, or directly its standard centralizer proof, gives for both graphs exactly the same polynomial
\[
F_\Gamma(q,T)=\sum_{S\subseteq V}(q-1)^{|S|}q^{8-\rho_\Gamma(S)}T^{\rho_\Gamma(S)}.
\]
The same exhaustive table shows that independent-set sizes in both graphs have counts \(1,7,13,7,1\) for sizes \(0,1,2,3,4\), so the order-at-most-two element counts both equal
\[
q^8\bigl(1+7(q-1)+13(q-1)^2+7(q-1)^3+(q-1)^4\bigr).
\]
Finally, the independent-support histograms in `CERTIFICATE.json`, substituted into the already-proved expression for \(H\), differ by \(q^3(q-1)^2T^2(T-q)^3\). The certificate records every histogram entry, and `verify.py` enumerates all masks \(0\) through \(127\) and performs the identity in the integer polynomial ring, not by sampling values of \(q\). Hence the equality of the ordinary polynomials and the difference of the involution polynomials both hold for all stated fields. Since the difference is nonzero whenever \(q\ge2\), group isomorphism is impossible in even characteristic.

## Verification
Run `python3 verify.py` in the directory containing the standalone verifier. It independently computes all support-component histograms for the two graphs, checks the two complete ordinary class polynomials for exact identity, and verifies the involution-polynomial factorization as a formal polynomial in two indeterminates. It also computes actual group multiplication over \(\mathbb F_2\) and \(\mathbb F_4\), tests square-one elements and centralizers directly in the indicated small graphs, and checks the full seven-vertex examples over \(\mathbb F_2\). Each seven-vertex graph has exactly \(128\) vertex supports and its subset census is exhaustive, rather than a nonexhaustive sample. The program additionally checks a sharp neighborhood bound for path graphs through sixteen vertices; those auxiliary finite checks are not part of the accepted claim.

## Relationship to prior work
Finite class-two nilpotent groups associated with graphs have a substantial earlier literature (Mishchenko–Treyer; Mainkar). Rossmann's 2022 theorem already determines the **unrestricted** class-size polynomial \(F_\Gamma\) for *every* graph, including these two; that general theorem is background, not a newly claimed enumeration. The new assertion is a joint element-order/conjugacy refinement: the two selected groups share exactly the full unrestricted data quantified by Rossmann's theorem (and the entire count of square-one elements) but differ under the restriction to conjugacy classes of square-one elements. The defining identity for \(H_\Gamma\) records this order-sensitive refinement. The polynomial certificates establish the explicit separation; no claim is made that unrestricted graphical-group class polynomials were previously unknown.

## Limitations
Only characteristic-two finite fields are covered by the involution-class formula and separation. The formula says nothing about higher element orders or arbitrary nilpotent groups. The underlying unrestricted class enumeration is pre-existing. The distinction is proved by finite exact subset enumeration for a fixed pair, not by a classification of all such twin pairs or a minimality theorem. The earliest graph-group reference in the list was inspected at the abstract level, not as a full Russian text; unidentified priority under alternative terminology is a residual risk. No independent mathematical audit has been performed.

## References
1. A. A. Mishchenko and A. V. Treyer, *Commuting graphs for partially commutative nilpotent \(\mathbb Q\)-groups of class \(2\)*, Siberian Electronic Mathematical Reports 4 (2007), 460–481, https://www.mathnet.ru/eng/semr168 (published 26 November 2007; contextual graph-group predecessor).
2. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, Groups Geometry and Dynamics 9 (2015), 55–65, https://arxiv.org/abs/1310.3414 (preprint publicly submitted 12 October 2013; graph-Lie-algebra background).
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. Lond. Math. Soc. 54 (2022), 1923–1943, https://doi.org/10.1112/blms.12665 (full-text Theorem A and Section 2 inspected; known unrestricted class formula).
