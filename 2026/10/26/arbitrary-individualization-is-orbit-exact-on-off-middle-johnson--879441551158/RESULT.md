# Arbitrary individualization is orbit-exact on off-middle Johnson graphs

## Finding

**Theorem.** For integers \(n>2k\ge 2\), let \(J(n,k)\) have as vertices the \(k\)-element subsets of \([n]\), adjacent when one element can be exchanged for another. Let \(A_1,\ldots,A_r\) be any ordered collection of distinct vertices, with \(0\le r\le\binom nk\). Give each \(A_i\) its own initial colour and all other vertices one common colour. Ordinary simultaneous one-dimensional counting colour refinement reaches **exactly the orbits of the pointwise stabilizer** of \(A_1,\ldots,A_r\) after at most \(k+1\) refinement rounds. Consequently every nonmiddle Johnson graph \(J(n,k)\), with \(1\le k<n\) and \(n\ne2k\), has this property (apply complementation when \(k>n/2\)); its bound is then \(\min(k,n-k)+1\).

For each subset \(T\subseteq[r]\), form the ground-set atom
\[
B_T=\{u\in[n]:\{i\in[r]:u\in A_i\}=T\},\qquad b_T=|B_T|.
\]
A vertex \(X\) has profile \(h_T(X)=|X\cap B_T|\). Stable colours are in one-to-one correspondence with vectors \((h_T)_{T\subseteq[r]}\) satisfying \(0\le h_T\le b_T\) and \(\sum_T h_T=k\). The colour of a profile has size \(\prod_T\binom{b_T}{h_T}\), and the number of colours is exactly
\[
[z^k]\prod_{T\subseteq[r]}(1+z+\cdots+z^{b_T}).
\]
These conclusions also include the empty distinguished set, when the graph remains monochromatic.

## Assumptions and scope

Refinement is the synchronous update \(c_{t+1}(X)=(c_t(X),\{\!\{c_t(Y):Y\sim X\}\!\})\), with colours understood up to relabelling. The initial colour of each marked vertex is unique. The theorem concerns the stable vertex partition on a single graph; it does not assert graph identification against every nonisomorphic graph, exact minimal rounds, or the same bound when \(n=2k\). The primary argument treats \(n>2k\), using the natural ground-set permutation subgroup only; no classification of exceptional automorphisms is assumed.

## Proof

**1. Orbit profiles.** Every permutation of \([n]\) preserving each \(A_i\) independently permutes the atoms \(B_T\), and every collection of independent permutations within the atoms gives such a permutation. Two \(k\)-subsets \(X,Y\) lie in the same orbit of this subgroup if and only if their profiles \((h_T(X))\) and \((h_T(Y))\) are equal. Since this subgroup acts by colour-preserving graph automorphisms, colour refinement never separates vertices within one such orbit.

**2. Landmark overlaps are visible by round \(k\).** For every marked vertex \(A_i\), its initial singleton colour and graph-neighbour counting distinguish successive distance spheres: inductively, vertices of distance \(t+1\) are precisely those outside the previously recognized spheres having a neighbour in the sphere at distance \(t\). The diameter of \(J(n,k)\) is \(k\) when \(n\ge2k\), and graph distance is \(k-|X\cap A_i|\). Thus after \(k\) rounds the colour of \(X\) determines every overlap \(m_{\{i\}}(X)=|X\cap A_i|\). Let \(m_U(X)=|X\cap\bigcap_{i\in U}A_i|\) and \(m_{\varnothing}(X)=k\).

**3. Odd neighbour-displacement moments.** For a neighbour obtained from \(X\) by exchanging \(a\in X\) with \(b\notin X\), set \(\delta_i={\bf1}_{b\in A_i}-{\bf1}_{a\in A_i}\). If \(P(-\delta)=-P(\delta)\), define
\[
F_P(X)=\sum_{Y\sim X}P\bigl(m_{\{i\}}(Y)-m_{\{i\}}(X):i\in[r]\bigr).
\]
The entire vector of landmark overlaps is a function of the round-\(k\) colour. Therefore \(F_P(X)\) is determined by the round-\((k+1)\) colour, for every fixed odd polynomial \(P\). Because \(P\) is odd, the sum of \(P(\delta)\) over ordered pairs \((a,b)\in X\times X\) is zero by antisymmetry. Hence
\[
F_P(X)=\sum_{a\in X}\sum_{b\in[n]}P\bigl({\bf1}_{b\in A_i}-{\bf1}_{a\in A_i}:i\in[r]\bigr).\tag{1}
\]

**4. Multilinear recovery of all intersections.** We prove inductively on \(|U|\) that the round-\((k+1)\) colour determines \(m_U(X)\). The empty and one-element cases were already covered. For any nonempty \(U\subseteq[r]\), choose the following odd polynomial:
\[
P_U(\delta)=\begin{cases}
\prod_{i\in U}\delta_i,& |U|\text{ odd},\\
\delta_j^2\prod_{i\in U\setminus\{j\}}\delta_i,& |U|\text{ even},\quad j\in U\text{ fixed}.
\end{cases}
\]
Write \(s_i={\bf1}_{a\in A_i}\) and \(t_i={\bf1}_{b\in A_i}\). On Boolean inputs \(s_i,t_i\in\{0,1\}\), the identity \((t_j-s_j)^2=t_j+s_j-2t_js_j\) implies that the inner sum in (1) is a multilinear polynomial in the variables \((s_i)_{i\in U}\). Its coefficient of \(\prod_{i\in U}s_i\) is \(-n\) when \(|U|\) is odd, and is
\[
(-1)^{|U|-1}\sum_{b\in[n]}(1-2{\bf1}_{b\in A_j})=-(n-2k)
\]
when \(|U|\) is even. Every other monomial uses a proper subset of \(U\). Summing the polynomial over \(a\in X\) therefore gives
\[
F_{P_U}(X)=\begin{cases}-n\,m_U(X)+\sum_{W\subsetneq U}c_{U,W}m_W(X),& |U|\text{ odd},\\
-(n-2k)m_U(X)+\sum_{W\subsetneq U}c_{U,W}m_W(X),& |U|\text{ even},\end{cases}\tag{2}
\]
where the integer coefficients \(c_{U,W}\) depend only on the marked vertices and the ground set. Both displayed leading coefficients are nonzero under \(n>2k\). Using (2) and the already recovered \(m_W(X)\), induction recovers \(m_U(X)\) for every subset \(U\subseteq[r]\).

**5. Recover the atoms and conclude.** Boolean inclusion-exclusion yields
\[
h_T(X)=\sum_{U\supseteq T}(-1)^{|U|-|T|}m_U(X).
\]
Thus equal colours after round \(k+1\) imply equal atom profiles. Step 1 proves the converse: equal profiles are carried into each other by automorphisms fixing all marks, so they have equal colours at every round. The orbit partition is therefore reached by round \(k+1\) and is stable. Profile feasibility, the size formula and the coefficient-extraction formula follow by independently choosing \(h_T\) elements from each atom. For \(k>n/2\), graph complementation identifies \(J(n,k)\) with \(J(n,n-k)\) and transports arbitrary individualizations. This proves all statements.

## Verification

Two standard-library Python checkers accompany this proof. `check_refinement.py` independently builds finite Johnson graphs, performs colour refinement, computes ground-atom profiles, compares both partitions and every class size, and tests the round bound. Its recorded execution passed \(864\) marked configurations in seven families up to \(J(11,5)\), with zero- and up-to-ten-mark cases. `check_moments.py` independently evaluates the odd displacement polynomials, verifies \(1080\) exact leading coefficients and \(32400\) swap-moment identities across \(54\) marked sets, with all checks passing. Run `python3 check_refinement.py` and `python3 check_moments.py` in an environment with Python 3 and no external packages. The programs provide finite corroboration; the universally quantified theorem is justified by Steps 1–5, not by extrapolation from these tests.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015), Section 0.A.2 and Theorem 0.A.7, establish the Tinhofer property for rank-two Johnson graphs \(J(n,2)\). Their proof does not state the property for general higher rank. The present result proves it for every rank away from the middle layer, every number of individually distinguished vertices and an explicit refinement-round bound, by a different odd-moment mechanism. The 2016 work of Arvind et al. studies the general complexity of individualization, not this Johnson-family classification. Bhattacharjee, Panse and Sarma (2026) develop a general hierarchy of partial Tinhofer properties, but do not state the present Johnson-family result in the examined manuscript. Della-Giustina (2023) studies fixing numbers of \(J(n,2)\) and \(J(n,3)\), a different invariant, without proving the colour-refinement statement.

## Limitations

The middle layer \(n=2k\) is not covered: the even-order leading coefficient in (2) vanishes, and a separate argument would be required. No claim is made that the bound \(k+1\) is sharp for any specified configuration. The published-literature comparison cannot establish complete publication priority; specialized unlocated results may exist. Independent validation of the theorem and source coverage remains outstanding.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04), especially Section 0.A.2, Theorem 0.A.7. https://arxiv.org/html/1502.01255v3
2. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert and G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, MFCS 2016, DOI:10.4230/LIPIcs.MFCS.2016.13. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.13
3. S. Bhattacharjee, A. Panse and J. Sarma, *A Hierarchy of Tinhofer Graphs: Separations and Membership Testing*, arXiv:2605.19702 (2026). https://arxiv.org/html/2605.19702
4. J. Della-Giustina, *Finding the Fixing Number of Johnson Graphs \(J(n,k)\) for \(k\in\{2,3\}\)*, American Journal of Undergraduate Research 20 (2023), DOI:10.33697/ajur.2023.097. https://doi.org/10.33697/ajur.2023.097
