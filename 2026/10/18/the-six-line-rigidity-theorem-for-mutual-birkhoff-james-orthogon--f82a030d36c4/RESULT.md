# The six-line rigidity theorem for mutual Birkhoff–James orthogonality in real \(\ell_1^3\)

## Finding
In the real normed space \(X=(\mathbb R^3,\|\cdot\|_1)\), form the undirected orthogonality graph whose vertices are one-dimensional linear subspaces \([x]=\mathbb Rx\) for nonzero \(x\), and in which two distinct vertices are adjacent when \(x\perp_B y\) and \(y\perp_B x\). Its clique number is **exactly six**. Moreover, it has **one and only one maximum clique**, namely the six projective lines
\[
\mathcal C_*=\{[e_i+e_j],[e_i-e_j]:1\le i<j\le3\},
\]
where \(e_1,e_2,e_3\) are the coordinate vectors. Thus every six-line pairwise mutually Birkhoff–James orthogonal configuration coincides with this configuration as a set of projective lines. No restrictions to rational or finite-coordinate vectors are imposed.

## Assumptions and scope
All scalars and vectors are real, and \(\|x\|_1=\sum_{i=1}^3|x_i|\). For nonzero \(x,y\), the relation \(x\perp_B y\) means
\[
\|x+t y\|_1\ge\|x\|_1\quad\text{for every }t\in\mathbb R.
\]
This relation is invariant under nonzero scaling of either vector. Its mutual version means both directed relations hold; projective lines, rather than oriented representatives, are counted. The theorem concerns the **mutual** orthogonality clique number, not one-sided Birkhoff orthogonal sets, Roberts orthogonality, or the orthodigraph's ordinary chromatic number.

## Proof
**Coordinate criterion.** For \(x\ne0\), write \(S(x)=\{i:x_i\ne0\}\) and \(s_i=\operatorname{sgn}(x_i)\) on \(S(x)\). The norming functionals of \(x\) for the \(\ell_1\) norm are exactly the vectors \(f\in\ell_\infty^3\) with \(f_i=s_i\) on \(S(x)\) and \(|f_i|\le1\) elsewhere. The subgradient characterization of Birkhoff–James orthogonality states that \(x\perp_B y\) precisely when some such \(f\) annihilates \(y\). Consequently,
\[
 x\perp_B y\ \Longleftrightarrow\
 \left|\sum_{i\in S(x)}s_i y_i\right|\le\sum_{i\notin S(x)}|y_i|.\tag{1}
\]
Indeed the unrestricted coordinates of a norming functional contribute exactly the interval with endpoints \(\pm\sum_{i\notin S(x)}|y_i|\). Formula (1) is valid at all coordinate degeneracies, including zeros.

**One-coordinate supports.** Suppose a clique contains \([e_i]\). For every other line \([y]\), the relation \(y\perp_B e_i\) and (1) force \(y_i=0\): if \(y_i\ne0\), its left side is one while its right side is zero. All remaining lines therefore lie in the other two-coordinate plane. In real \(\ell_1^2\), a mutual clique has at most two lines. To see this, an axis line forces every other line to be the complementary axis. Without an axis, all vectors have two nonzero coordinates; mutual orthogonality for any pair \(u,v\) forces \(\operatorname{sgn}(u_1)v_1+\operatorname{sgn}(u_2)v_2=0\), and conversely with \(u,v\) swapped. This forces their projective directions to be the two diagonals \([(1,1)]\) and \([(1,-1)]\). Thus a clique containing an axis has at most three lines.

**Two-coordinate supports.** Let two distinct projective vectors \([u],[v]\) in a mutual clique have the same support \(\{i,j\}\), with both listed coordinates nonzero. Equation (1) for \(u\perp_B v\) gives \(\operatorname{sgn}(u_i)v_i+\operatorname{sgn}(u_j)v_j=0\), whence \(|v_i|=|v_j|\). The reverse relation similarly gives \(|u_i|=|u_j|\). Their signs must be opposite in one relative coordinate. Hence the **only possible** two lines for support \(\{i,j\}\) are \([e_i+e_j]\) and \([e_i-e_j]\). In particular, at most two clique lines have that support.

**Three-coordinate supports.** A full-support vector \(u\) has a unique norming functional \(s(u)\in\{\pm1\}^3\), and (1) reduces to \(s(u)\cdot v=0\). Suppose three full-support vectors \(u,v,w\) belonged to one mutual clique. The sign vectors \(s(v),s(w)\) cannot be equal or opposite, since either would imply \(s(v)\cdot w=\pm\|w\|_1\ne0\), contradicting \(v\perp_B w\). Thus both sets of coordinates
\[
 I_+=\{i:s(v)_i=s(w)_i\},\qquad I_-=\{i:s(v)_i=-s(w)_i\}
\]
are nonempty. From \(v\perp_B u\) and \(w\perp_B u\) we have \(s(v)\cdot u=s(w)\cdot u=0\). Adding and subtracting yields
\[
\sum_{i\in I_+}s(v)_i u_i=0,\qquad \sum_{i\in I_-}s(v)_i u_i=0.
\]
One of these two nonempty sets is a singleton because there are exactly three coordinates. The corresponding coordinate of \(u\) is zero, contradicting full support. Hence at most two full-support lines can coexist in a clique.

If a clique contains a full-support line \([u]\), it contains no axis by the first step. For each two-element support \(\{i,j\}\), every clique line \([v]\) with that support must satisfy \(s(u)_iv_i+s(u)_jv_j=0\), so it lies in a **single** projective direction. There are only three two-element supports, and at most two full-support lines, giving a total of at most five lines. Consequently every clique with six or more lines consists solely of two-coordinate-supported vectors.

**Sharpness and rigidity.** Without singleton or full supports, the preceding two-coordinate bound gives at most two lines for each of the three two-coordinate supports, hence at most six. The six lines in \(\mathcal C_*\) attain the bound: the two diagonal lines on one support satisfy (1) in both directions with zero left sides; for distinct two-coordinate supports their intersection is one coordinate, so the left and right sides of (1) both equal one for the displayed sign vectors. Therefore all six are mutually orthogonal. Equality in the six-line bound forces exactly two lines in each of the three two-coordinate supports; these must be the two diagonals already identified. This proves both the exact clique number and uniqueness of the maximum clique.

## Verification
The standalone program `CHECK.py` computes Birkhoff–James orthogonality in two logically separate ways: (1) the signed-support inequality and (2) exact minimization of the piecewise-linear function \(t\mapsto\|x+t y\|_1\) over all its rational breakpoints. It exhaustively checks all pair relations among primitive projective integer triples with coordinates in \(\{-2,-1,0,1,2\}\), then determines maximal cliques using an independent graph search. It verifies clique numbers \(1,2,6\) in dimensions one, two, three and, in dimension three, identifies the unique six-line clique. Run with `python3 CHECK.py` (only the Python standard library). These finite computations corroborate, but **do not replace**, the all-real-vector proof above.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić and Zhilina (2021) introduce the symmetrized Birkhoff–James orthogonality graph, prove general finite-dimensional clique bounds and give other normed-space constructions. Their nonexplicit dimension-only bound and the lower-dimensional example do not furnish this exact real \(\ell_1^3\) maximum and rigidity statement. Wang, Ji and Wei (2023, published 17 October 2023) explicitly discuss mutually orthogonal sets in real \(\ell_1^2\) and exhibit an ordinary (one-sided) four-vector Birkhoff orthogonal set in real \(\ell_1^3\); their specific three-dimensional example does not imply the present six-line mutual extremum. Their paper lists primary MSC \(46B20\).

A later online mathematical note, *Exponential mutual Birkhoff–James cliques in real \(\ell_1^n\)* (2026), proves an existential exponential lower bound for general dimensions, explicitly without determining the exact clique number. The general-n lower bound does not imply either the sharp upper bound or the extremizer rigidity proved here. The similarly named ternary construction for \(\ell_\infty^n\) concerns a different norm; duality does not preserve the mutual Birkhoff–James orthograph.

## Limitations
The result is restricted to **real three-dimensional \(\ell_1\)**. It does not determine clique numbers in higher dimensions, describe all submaximal cliques, or give a complex-scalar statement. It is a self-reviewed proof, not independent certification. A 2022 orthogonality-graph survey chapter could not be inspected in full; an equivalent statement in obscure or unindexed literature remains a bibliographic risk.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, Journal of Mathematical Analysis and Applications **502** (2021), 125203. DOI: 10.1016/j.jmaa.2021.125203. https://doi.org/10.1016/j.jmaa.2021.125203.
2. X. Wang, D. Ji, Y. Wei, *Study on Orthogonal Sets for Birkhoff Orthogonality*, Mathematics **11** (2023), 4320; first published 17 October 2023. DOI: 10.3390/math11204320. https://www.mdpi.com/2227-7390/11/20/4320.
3. *Exponential mutual Birkhoff–James cliques in real \(\ell_1^n\)*, online mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exponential-mutual-birkhoff-james-cliques-in-real-ell-1-n--6a12ae18b191.
4. L. Arambašić et al., *Birkhoff–James Orthogonality: Characterizations, Preservers, and Orthogonality Graphs*, 2022, DOI: 10.1007/978-3-031-02104-6_8 (full text not inspected).
