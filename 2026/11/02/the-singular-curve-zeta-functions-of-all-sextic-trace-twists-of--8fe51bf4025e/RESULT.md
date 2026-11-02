# The singular-curve zeta functions of all sextic trace twists of the Igusa quartic

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\ge 7\), and let \(E/k\) be any degree-six finite étale algebra. On \(\mathbb P_k(\ker\operatorname{Tr}_{E/k})\), define the trace Igusa quartic
\[
I_E:\qquad \operatorname{Tr}_{E/k}(z^2)^2-4\operatorname{Tr}_{E/k}(z^4)=0.
\]
Let \(\Sigma_E=(\operatorname{Sing}I_E)_{\mathrm{red}}\). Over an algebraic closure, \(\Sigma_E\) is the union of fifteen distinct projective lines, with exactly fifteen intersection points; exactly three lines pass through each such point, and all other pairs of lines are disjoint. These are the **Cremona–Richmond singular-curve components** of the Igusa quartic.

Write \(\lambda\vdash6\) for the multiset of field-extension degrees of the factors of \(E\). For each integer \(d\ge1\), let \(\ell_d(\lambda)\), \(p_d(\lambda)\), and \(b_d(\lambda)\) count the length-\(d\) Frobenius orbits, respectively, on the fifteen lines, the fifteen triple intersection points, and the forty-five point–line branches above those points. Then the complete zeta function of the **reduced singular curve** is
\[
\boxed{Z(\Sigma_E,T)=\prod_{d\ge1}(1-T^d)^{b_d-\ell_d-p_d}(1-q^dT^d)^{-\ell_d}.}
\]
Equivalently, for every integer \(n\ge1\),
\[
\boxed{\#\Sigma_E(\mathbb F_{q^n})=(q^n+1)\sum_{d\mid n}d\ell_d-\sum_{d\mid n}db_d+\sum_{d\mid n}dp_d.}
\]
All eleven possibilities are given in the following exact table. In a spectrum such as \(1^3 2^6\), the exponent counts cycles of that length. The final column gives \(\#\Sigma_E(k)\).

| \(\lambda\) | Triple-point spectrum \(p\) | Line spectrum \(\ell\) | Branch spectrum \(b\) | \(\#\Sigma_E(k)\) |
| --- | --- | --- | --- | --- |
| \((1,1,1,1,1,1)\) | \(1^{15}\) | \(1^{15}\) | \(1^{45}\) | \(15q-15\) |
| \((2,1,1,1,1)\) | \(1^7 2^4\) | \(1^3 2^6\) | \(1^9 2^{18}\) | \(3q+1\) |
| \((2,2,1,1)\) | \(1^3 2^6\) | \(1^3 2^6\) | \(1^5 2^{20}\) | \(3q+1\) |
| \((2,2,2)\) | \(1^3 2^6\) | \(1^7 2^4\) | \(1^9 2^{18}\) | \(7q+1\) |
| \((3,1,1,1)\) | \(1^3 3^4\) | \(3^5\) | \(3^{15}\) | \(3\) |
| \((3,2,1)\) | \(1^1 2^1 3^2 6^1\) | \(3^1 6^2\) | \(3^3 6^6\) | \(1\) |
| \((3,3)\) | \(3^5\) | \(1^3 3^4\) | \(3^{15}\) | \(3q+3\) |
| \((4,1,1)\) | \(1^1 2^1 4^3\) | \(1^1 2^1 4^3\) | \(1^1 2^2 4^{10}\) | \(q+1\) |
| \((4,2)\) | \(1^1 2^1 4^3\) | \(1^1 2^1 4^3\) | \(1^1 2^2 4^{10}\) | \(q+1\) |
| \((5,1)\) | \(5^3\) | \(5^3\) | \(5^9\) | \(0\) |
| \((6)\) | \(3^1 6^2\) | \(1^1 2^1 3^2 6^1\) | \(3^3 6^6\) | \(q+1\) |

In particular, when \(\lambda=(3,1,1,1)\), the reduced singular curve has **three rational points but no rational irreducible component**. For \(\lambda=(5,1)\) it has no rational points at all. Every geometric component and every triple point becomes rational over \(\mathbb F_{q^{\operatorname{lcm}(\lambda)}}\), and no smaller extension works simultaneously for all of them.

## Assumptions and scope
Here \(\operatorname{Tr}_{E/k}\) is the ordinary field-algebra trace; after extending scalars to \(\bar k\), the algebra \(E\) splits into six factors and Frobenius permutes those factors with cycle lengths \(\lambda\). The reduced geometric singular curve is the object being counted; the theorem makes no assertion about the scheme-theoretic multiplicities of the singular subscheme or the zeta function of the ambient threefold. Characteristic at least seven ensures that \(2\), \(3\), and \(6\) are invertible and the reduced configuration has the stated incidence.

## Proof
**1. Exhaustion of the geometric singular locus.** Over \(\bar k\), identify \(E\otimes_k\bar k\simeq\bar k^6\), with coordinates \(x_0,\dots,x_5\). Set \(s_j=\sum_i x_i^j\). Then \(I_E\) is \(s_1=0\), \(F=s_2^2-4s_4=0\). Its gradient in the ambient six-space has components \(4x_i(s_2-4x_i^2)\). A projective point of the hyperplane \(s_1=0\) is singular precisely when all six gradient components agree; Euler's identity shows this condition already forces \(F=0\). Thus all six coordinates are roots of one cubic
\[
G(t)=t^3-\frac{s_2}{4}t+c.
\]
If \(G\) has three distinct roots \(u,v,w\), their sum is zero. Writing \(m_u,m_v,m_w\) for the numbers of occurrences among the six coordinates, the relations \(s_1=0\), the coefficient of \(t\) in \(G\), and \(\sum_i m_i=6\) give
\[
\sum_{r\in\{u,v,w\}}(m_r-2)r^j=0\qquad(j=0,1,2).
\]
The Vandermonde matrix is invertible, so every \(m_r\equiv2\pmod p\). Since \(0\le m_r\le6\) and \(p\ge7\), each multiplicity is two. Hence the point lies on the line associated to a partition of the six indices into three pairs, with pair values \(u,v,w\) satisfying \(u+v+w=0\).

If \(G\) has a repeated root, its roots are \(u,u,-2u\). The root \(u=0\) gives no projective point. Otherwise, if \(m\) coordinates equal \(-2u\), the equation \(s_1=0\) gives \(3(m-2)u=0\), so \(m=2\). These are precisely the fifteen points with two entries \(-2u\) and four entries \(u\). Conversely, every point on each displayed pairing line satisfies the singularity equations. Thus the reduced singular locus is exactly the union of the fifteen lines.

**2. Intersections and descent.** Two different pairings either share exactly one pair or share none. In the first case the associated lines meet uniquely at the point whose coordinates on that common pair are \(-2\), and on the four remaining indices are \(1\). In the second case their combined equality constraints force all six coordinates equal, impossible in \(s_1=0\) for \(p\ge7\). Each of the fifteen two-element subsets belongs to three pairings; therefore the fifteen special points are exactly the triple intersections. The preimage of these points under normalization consists of forty-five branches, naturally indexed by flags \((\text{duad},\text{pairing containing it})\).

The coordinates and all incidence maps are equivariant for permutations of the six indices. For a general degree-six étale algebra, the Frobenius permutation has cycle partition \(\lambda\). Therefore the spectra of points, lines, and branches are just the corresponding permutation-orbit spectra of this finite \(S_6\)-set. Exhausting all \(720\) permutations gives the eleven rows in the table; the standalone exact verifier enumerates the permutations and independently confirms the spectra by fixed-point counts under all powers through twelve. Every partition is realized by \(E=\prod_i\mathbb F_{q^{\lambda_i}}\). The action on duads is faithful, proving the minimal common splitting degree is \(\operatorname{lcm}(\lambda)\).

**3. Zeta function.** Let \(N\to\Sigma_E\) be normalization, \(P\) the reduced fifteen-point triple-intersection subscheme, and \(B=N\times_{\Sigma_E}P\) the reduced forty-five-point branch scheme. Away from \(P\), normalization is an isomorphism; hence for every \(n\ge1\),
\[
\#\Sigma_E(\mathbb F_{q^n})=\#N(\mathbb F_{q^n})-\#B(\mathbb F_{q^n})+\#P(\mathbb F_{q^n}).
\]
For a Frobenius orbit of \(d\) geometric line components, the corresponding normalization component over \(k\) is a genus-zero curve over \(\mathbb F_{q^d}\); all genus-zero curves over finite fields have rational points, so it is \(\mathbb P^1\) over \(\mathbb F_{q^d}\). Its zeta factor over \(k\) is \((1-T^d)^{-1}(1-q^dT^d)^{-1}\). The finite étale schemes \(P\) and \(B\) contribute \(\prod_d(1-T^d)^{-p_d}\) and \(\prod_d(1-T^d)^{-b_d}\), respectively. Multiplying \(Z(N,T)Z(P,T)/Z(B,T)\) proves both displayed formulas.

## Verification
The bundled `verify.py` uses Python's standard library alone. It enumerates all \(720\) permutations, checks all \(11\) conjugacy classes, compares orbit decomposition with an independent fixed-point calculation for extension degrees \(1\) through \(12\), checks the minimal splitting degree, and counts the singular points of the split quartic directly over \(\mathbb F_7\) and \(\mathbb F_{11}\) using its defining polynomial and gradient. The latter tests recover exactly \(90\) and \(150\) rational singular points, and verify that they coincide with the explicit fifteen-line union. Its recorded execution ends `VERIFY_OK`. The all-field result rests on the preceding algebraic proof plus finite exhaustive group enumeration, not on extrapolation from the two sample fields.

## Relationship to prior work
The Igusa quartic, its duality with the Segre cubic, and its fifteen singular lines are classical. Hulek and Sankaran describe this geometry and the modular compactification, including the \(S_6\)-action. Rito uses the fifteen singular lines in a separate construction of a quintic with cuspidal lines. Bruin and Kulkarni describe the coordinate model and arbitrary twisted Igusa quartics in the context of genus-four Jacobians. In each case the geometric input is already available; no novelty is claimed for the equations, fifteen-line incidence configuration, or the general possibility of twisting. The new assertion assessed here is the **explicit complete eleven-case zeta classification of the reduced singular curve**, including the normalization–branch correction and arithmetic exceptional cases. A related Segre-cubic node–plane Frobenius classification concerns a different sixty-flag finite scheme and does not state these singular-curve zeta factors.

## Limitations
The claim is restricted to characteristic at least seven and the precisely defined sextic trace twists. It does not evaluate the zeta function of the entire quartic threefold or of its nonreduced singular scheme, nor does it claim a general formula for all possible algebraic forms outside this construction. The underlying \(S_6\)-sets are classical, so an older unlocated treatment or an implicit derivation from a broader result remains a historical-priority risk. No independent scientific audit is asserted.

## References
1. K. Hulek and G. K. Sankaran, *The geometry of Siegel modular varieties*, arXiv:math/9810153, first submitted 1998-10-27; §IV.1 treats the Segre cubic, Igusa quartic, and fifteen singular lines. https://arxiv.org/abs/math/9810153
2. C. Rito, *Cuspidal quintics and surfaces with \(p_g=0\), \(K^2=3\) and 5-torsion*, arXiv:1310.4071, first submitted 2013-10-15; §5 and Appendix discuss the Igusa singular lines. https://arxiv.org/abs/1310.4071
3. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, *Canadian Journal of Mathematics* (published online 2025-09-12); §2.5 describes the \(S_6\)-equivariant Igusa equation, synthemes, and twisted models. https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-22decomposable-genus-4-jacobians/651E1FC3F6A593EB7B03A0642E81C7F0
4. I. Dolgachev and D. Ortland, *Point sets in projective spaces and theta functions*, Astérisque 165 (1988). Bibliographically checked as historical background; the complete monograph was not inspected. https://www.numdam.org/item/AST_1988__165__1_0/
