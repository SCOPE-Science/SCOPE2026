# Six and only six mutual Birkhoff–James directions in real \(\ell_1^3\)

## Finding
Let \(X=(\mathbb R^3,\|\cdot\|_1)\) and let \(\Gamma_{\mathrm{BJ}}(X)\) be the simple graph whose vertices are one-dimensional linear subspaces of \(X\). Two distinct vertices \([x]\) and \([y]\) are adjacent precisely when \(x\perp_B y\) and \(y\perp_B x\), where \(x\perp_B y\) means \(\|x+\lambda y\|_1\ge\|x\|_1\) for every real \(\lambda\).

**The exact clique number is \(\omega(\Gamma_{\mathrm{BJ}}(X))=6\). Moreover the maximum clique is unique, and it is the set of six lines**
\[
\mathcal C_* = \{[e_i+e_j],[e_i-e_j]:1\le i<j\le3\},
\]
where \(e_1,e_2,e_3\) is the canonical basis. The classification applies to every real vector, with no ternary-coordinate or equal-magnitude restriction imposed on competing cliques.

## Assumptions and scope
The field is real; projective lines identify nonzero scalar multiples. For a nonzero vector \(u=(u_1,u_2,u_3)\), let \(S(u)=\{i:u_i\ne0\}\). The dual norming functionals at \(u\) are exactly the vectors \(f\in[-1,1]^3\) whose coordinates satisfy \(f_i=\operatorname{sgn}(u_i)\) on \(S(u)\). Consequently, for all nonzero real \(u,v\),
\[
 u\perp_B v\quad\Longleftrightarrow\quad
\left|\sum_{i\in S(u)}\operatorname{sgn}(u_i)v_i\right|
\le\sum_{i\notin S(u)}|v_i|. \tag{1}
\]
Indeed the remaining coordinates of a norming functional sweep out the whole closed interval whose radius is the right-hand sum, so a norming functional vanishing on \(v\) exists exactly under (1). This equivalence, including zero-coordinate boundaries, is the only analytic lemma used.

## Proof
**Step 1: the lower bound and all six adjacencies.** Within the fixed pair of coordinates \(i<j\), the vectors \(e_i+e_j\) and \(e_i-e_j\) satisfy (1) in both directions because their signed inner contributions cancel and their remaining coordinates vanish. For vectors supported on different two-element coordinate sets, the supports share exactly one coordinate. The magnitude of the signed contribution on this shared coordinate is one, and the sole coordinate of the second vector missing from the first support also has magnitude one. Thus (1) holds with equality in both directions, for every choice of signs. These six different lines form a clique.

**Step 2: cliques containing a coordinate axis.** Suppose \([e_i]\) belongs to a clique. If \(v_i\ne0\), then \(v\not\perp_B e_i\), since every norming functional at \(v\) takes the nonzero value \(\operatorname{sgn}(v_i)\) at \(e_i\). Hence every other line in that clique is supported in the two-coordinate subspace \(\{v_i=0\}\). The mutual Birkhoff–James orthogonality graph of real \(\ell_1^2\) has clique number two: if one line has both coordinates nonzero, its outgoing orthogonality condition restricts all neighbors to one line, while if no such line is present, the two coordinate axes are the only possibilities. Thus any clique containing \([e_i]\) has at most three vertices.

**Step 3: cliques containing a vector of full support.** Suppose the clique contains \([u]\) with \(S(u)=\{1,2,3\}\). Applying a diagonal sign change and a positive scalar multiplication, we may assume \(u=(a,b,c)\) with \(a,b,c>0\). A coordinate-axis line cannot be adjacent to \([u]\), because (1) for \(u\perp_B e_i\) would require a nonzero signed coordinate to vanish.

Every other two-supported neighbor \(v\) of \([u]\) must satisfy \(u\perp_B v\), which reduces (1) to \(v_1+v_2+v_3=0\). For each two-coordinate support this forces opposite signs and equal magnitudes, giving at most one projective line for each of the three possible supports.

For an additional full-support neighbor \([w]\), the reverse condition \(w\perp_B u\) requires
\[
\operatorname{sgn}(w_1)a+\operatorname{sgn}(w_2)b+\operatorname{sgn}(w_3)c=0.
\]
Modulo global sign, a nontrivial sign triple gives one of the three equalities \(a=b+c\), \(b=a+c\), \(c=a+b\). Positive \(a,b,c\) cannot satisfy two of these at once. For any fixed sign triple, two full-support vectors cannot be Birkhoff–James orthogonal in even one direction, because the signed sum in (1) is then strictly positive after projective sign normalization. There is therefore at most one other full-support line. The clique has at most \(1+3+1=5\) vertices.

**Step 4: all remaining cliques and equality rigidity.** By the preceding steps, a clique of size at least six consists solely of vectors with exactly two nonzero coordinates. For each unordered two-coordinate support \(\{i,j\}\), there are exactly two sign types modulo simultaneous negation: equal signs and opposite signs. Two vectors of the same sign type cannot be Birkhoff–James orthogonal in even one direction, because the left side of (1) is strictly positive while the right side vanishes. Thus each of the three supports contributes at most two projective lines and the clique has at most six vertices.

If six vertices occur, each support contributes both sign types. On any fixed support, choose representatives \(v=a e_i+b e_j\) and \(w=c e_i-d e_j\), with \(a,b,c,d>0\). The two directions of (1) respectively give \(c=d\) and \(a=b\). Hence the two lines must be \([e_i+e_j]\) and \([e_i-e_j]\). This is forced for each of the three supports and gives exactly \(\mathcal C_*\). The upper bound, attainment and uniqueness follow.

## Verification
The self-contained standard-library program `CHECK.py` enumerates all thirteen nonzero ternary projective sign-support types, computes every mutual adjacency using (1), finds clique number six and exactly one six-clique among these types, and checks the sign-support inequality against the one-sided derivative criterion for every ordered pair of nonzero integer vectors in \(\{-2,-1,0,1,2\}^3\). Reproduce with `python3 CHECK.py`. The observed output is `VERTICES 13 EDGES 36 OMEGA 6 MAX_CLIQUES 1`, followed by `VERIFY_OK pairwise_integer_tests 15376`.

The computation is **not** an exhaustive search over real vectors. Step 2 through Step 4 establish the unrestricted theorem analytically, and the checker only verifies finite supporting cases and arithmetic.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić and Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces* (2021), introduce the mutual-orthogonality orthograph, prove dimension-dependent finiteness, and exhibit large cliques for the **supremum** norm; those conclusions do not determine the \(\ell_1^3\) clique number. Guterman, Kuzma, Singla and Zhilina (2024) recognize norm properties from directed orthographs and do not give the present exact, undirected mutual-clique classification in their inspected statements. A published result on exponential mutual cliques in real \(\ell_1^n\) supplies a dimension-uniform **lower bound** but explicitly leaves exact values open. Exact results for the dual \(\ell_\infty^n\) graph are not transferable here: Birkhoff–James orthogonality need not be preserved by Banach duality.

The present exact value in the first nonsmooth dimension beyond a plane is accompanied by a rigidity statement: unlike a count-only lower bound, it determines every maximum configuration in the full continuous projective graph.

## Limitations
Only the real three-dimensional \(\ell_1\) norm is treated. No claim is made about complex scalars, exact clique numbers in higher dimensions, or the universal maximum over all three-dimensional norms. A relevant survey chapter could only be inspected at abstract level and may contain equivalent unindexed material. Literature novelty has not been independently audited.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić and S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, Journal of Mathematical Analysis and Applications 502 (2021), 125203, DOI: 10.1016/j.jmaa.2021.125203, especially Section 3 and Example 3.7.
2. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić and S. Zhilina, *What does Birkhoff–James orthogonality know about the norm?*, arXiv:2109.09414v1 (20 September 2021).
3. A. Guterman, B. Kuzma, S. Singla and S. Zhilina, *Birkhoff–James classification of norm’s properties*, Advances in Operator Theory 9 (2024), article 43, DOI: 10.1007/s43036-024-00321-0, arXiv:2402.13416.
4. *Exponential mutual Birkhoff–James cliques in real \(\ell_1^n\)*, public mathematical result record `2026/10/11/SCOPE-exponential-mutual-birkhoff-james-cliques-in-real-ell-1-n--6a12ae18b191`, statement and proof as publicly available.
5. L. Arambašić, A. Guterman, B. Kuzma and S. Zhilina, *Birkhoff–James Orthogonality: Characterizations, Preservers, and Orthogonality Graphs*, Trends in Mathematics (2022), 255–302, DOI: 10.1007/978-3-031-02104-6_8 (only the abstract was accessible).
