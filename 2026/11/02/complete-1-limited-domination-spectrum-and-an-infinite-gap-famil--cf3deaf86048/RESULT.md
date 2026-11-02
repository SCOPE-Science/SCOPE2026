# Complete 1-limited domination spectrum and an infinite gap family of circular prisms

## Finding

For every integer \(n\ge3\), let \(Y_n=C_n\square K_2\) be the labelled circular prism with two \(n\)-cycles and corresponding rungs. Write \(L_n(z)=\sum_D z^{|D|}\), where the sum runs over **all** vertex subsets \(D\subseteq V(Y_n)\) that dominate the graph and satisfy \(|N(v)\setminus D|\le1\) for every \(v\in D\). The coefficients count labelled vertex subsets, without quotienting by rotation or layer exchange.

Define the polynomials
\[
Q(t,z)=1-tz^2-t^2z^3-t^3(2z^4+z^5)-t^4(z^4+z^5+z^6)-t^5z^6,
\]
\[
\Delta(t,z)=(1-tz)(1-tz+t^2z^3)Q(t,z).
\]
Then the **entire cardinality distribution** is given by the rational bivariate identity
\[
\boxed{\displaystyle\sum_{n\ge1}\operatorname{tr}(M(z)^n)t^n
=-t\,\frac{\partial}{\partial t}\log\Delta(t,z),\qquad
L_n(z)=\operatorname{tr}(M(z)^n)\quad(n\ge3),}
\]
where the finite explicit matrix \(M(z)\) is specified below. The formal summands for \(n=1,2\) are transfer-matrix closed-walk counts; they are not interpreted as simple circular prisms.

The three smallest potentially nonzero cardinality layers are **exactly**
\[
\boxed{[z^n]L_n(z)=2+4\mathbf1_{\,4\mid n},}
\]
\[
\boxed{[z^{n+1}]L_n(z)=\begin{cases}n,&n\text{ odd},\\0,&n\text{ even},\end{cases}}
\]
\[
\boxed{[z^{n+2}]L_n(z)=\begin{cases}
\frac n2(3n-6-(-1)^{(n-1)/2}),&n\text{ odd},\\
\frac n4(7n-14+2(-1)^{n/2}),&n\text{ even}.
\end{cases}}
\]
The minimum cardinality is \(\gamma^{\mathrm L}_1(Y_n)=n\). In particular, for **every even \(n\ge4\)**, the polynomial has a genuine *internal coefficient gap*: its coefficients at cardinalities \(n\) and \(n+2\) are positive but the coefficient at \(n+1\) is zero. Hence this whole infinite family has non-interval support and is **not unimodal**.

## Assumptions and scope

Graphs are simple, with labelled positions \((i,r)\in\mathbb Z/n\mathbb Z\times\{0,1\}\), and three edges incident to each vertex: two cycle edges and one rung. A dominating set requires every exterior vertex to have a selected neighbour; selected vertices need not themselves be dominated. A \(1\)-limited dominating set additionally requires every selected vertex to have *at most one exterior neighbour*. On these cubic graphs this is equivalent to \((1,2)\)-domination, meaning every selected vertex has at least two selected neighbours. This is **different** from \([1,2]\)-domination, which bounds the number of selected neighbours *of exterior vertices*.

A column mask \(b\in\{0,1,2,3\}\) records the two selected vertices by its two binary digits; let \(b_r\in\{0,1\}\) be bit \(r\). Define
\[
h(b)=b_0+b_1,\qquad
\Phi(a,b,c)=\prod_{r=0}^1
\mathbf1\{a_r+c_r+b_{1-r}\ge1+b_r\}.
\]
For the sixteen ordered pairs of masks \((a,b)\), define the explicitly reproducible weighted transfer matrix
\[
M(z)_{(a,b),(u,c)}=\mathbf1\{u=b\}\,\Phi(a,b,c)\,z^{h(b)}.
\]

## Proof

**1. Local condition and complete enumeration.** For an interior vertex in a column with mask \(b\), its three neighbours have selection bits \(a_r,c_r,b_{1-r}\). If the vertex is not selected, domination requires at least one of these neighbours to be selected. If it is selected, the \(1\)-limited condition requires at least two of the neighbours selected. These are exactly the two inequalities defining \(\Phi(a,b,c)=1\). A cyclic word of \(n\) masks is therefore admissible if and only if each consecutive triple passes \(\Phi\). The closed walks of length \(n\) in the matrix encode these cyclic words bijectively, and every chosen column contributes \(z^{h(b)}\) once. Consequently \(L_n(z)=\operatorname{tr}M(z)^n\) for every \(n\ge3\), with no rotational or reflection quotient.

**2. Finite exact determinant.** Of the sixteen pair states, precisely the following ten can occur in any directed cycle (including length-one cycles):
\[
(0,0),(0,3),(1,1),(1,3),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3).
\]
States outside this set lie on no closed walk, and their contributions to the characteristic determinant are trivial. Let \(M_{10}(z)\) be the displayed ten-state restriction of the entry formula. The following is an exact, finite, integer-polynomial identity:
\[
\det(I-tM_{10}(z))
=(1-tz)(1-tz+t^2z^3)Q(t,z)=\Delta(t,z).
\]
It follows by ordinary determinant expansion; the accompanying standalone code independently performs a complete signed subset expansion of this determinant and checks every monomial of the product on the right. The identity is a finite polynomial calculation, not extrapolation from numeric specializations. Its logarithmic derivative satisfies
\[
-t\partial_t\log\det(I-tM)=\sum_{n\ge1}t^n\operatorname{tr}(M^n)
\]
as a formal power series, proving the full enumerator formula.

**3. Minimum cardinality and its multiplicity.** Let \(E(D,\bar D)\) count edges joining a selected vertex to an exterior vertex. Domination gives \(E(D,\bar D)\ge|\bar D|\), while the \(1\)-limited condition gives \(E(D,\bar D)\le|D|\). Since there are \(2n\) vertices, \(|D|\ge n\). Selecting an entire layer of \(n\) vertices is feasible, so equality is sharp. At equality, *each* vertex is incident with exactly one edge of the cut, i.e. that edge set is a perfect matching of the prism. If any rung crosses the cut, the incident vertices have no other crossing edges. Applying this at the adjacent columns forces every rung to cross and all vertices within each layer to share a selected status, giving exactly two configurations. Otherwise every rung is monochromatic, the two vertices in each column have identical status, and each vertex must have precisely one crossing cycle edge. Thus the cyclic binary column pattern is \(0011\) repeated, up to four choices of phase, possible exactly when \(4\mid n\). The count is \(2+4\mathbf1_{4\mid n}\).

**4. Two higher coefficients.** The determinant factors show that, after factoring out \(z\) from the nonzero eigenvalues, the normalized eigenvalues comprise the constant root \(w=1\), two roots of \(w^2-w+z=0\), and five roots of
\[
F(w,z)=w^5-w-z(w^4+w^3+2w^2+w+1)-z^2(w^2+w)=0.
\]
At \(z=0\), all roots are simple within each factor. The small roots of the quadratic and quintic vanish at \(z=0\), so their \(n\)-th powers do not affect the first three Taylor coefficients of \(z^{-n}L_n(z)\) for \(n\ge3\). The root of the quadratic near \(1\) has expansion \(1-z-z^2+O(z^3)\); the four nonzero roots of the quintic have expansions
\[
\begin{aligned}
w_{1}(z)&=1+\frac32z-\frac58z^2+O(z^3),\\
w_{-1}(z)&=-1+\frac12z+\frac18z^2+O(z^3),\\
w_{i}(z)&=i+\frac{-1+i}{4}z^2+O(z^3),\\
w_{-i}(z)&=-i+\frac{-1-i}{4}z^2+O(z^3).
\end{aligned}
\]
The expansions follow by equating coefficients in the displayed quadratic and quintic; all denominators are nonzero because the roots are simple. Summing the \(n\)-th powers with the constant root \(1\) gives
\[
[z^0](z^{-n}L_n)=3+(-1)^n+2\cos(\pi n/2),
\qquad [z^1](z^{-n}L_n)=\frac n2(1-(-1)^n),
\]
and the coefficient at \(z^2\) equals
\[
\frac{n(n-1)}8(13+(-1)^n)-\frac n8(13+(-1)^n)
+\frac n2\{\cos(\pi n/2)-\sin(\pi n/2)\}.
\]
Evaluating those expressions by parity yields precisely the three boxed coefficient formulas. The last displayed expression simplifies to the stated piecewise formula after using \(n(n-1)-n=n(n-2)\).

**5. Genuine internal gap.** For even \(n\), the first two formulas give \([z^n]L_n>0\) and \([z^{n+1}]L_n=0\). The third is positive for every even \(n\ge4\) (equivalently, selecting a whole top layer and two adjacent bottom vertices is an explicit valid set of size \(n+2\)). Thus a zero coefficient lies strictly between positive coefficients, contradicting both interval support and unimodality of a nonnegative sequence. Ordinary domination polynomials cannot have this obstruction because supersets of an ordinary dominating set remain dominating; the capacity condition destroys this monotonicity.

## Verification

The supplied Python 3 standard-library program `verify.py` constructs the transfer transitions directly from the defining two inequalities, computes the ten-state determinant through signed subset dynamic programming with exact integer bivariate polynomials, and tests the stated factorization coefficient by coefficient. It also directly examines all \(87{,}360\) labelled vertex subsets across prism sizes \(n=3,4,5,6,7,8\), checking adjacency without using the transfer recurrence. The program compares the full polynomials with transfer counts in those sizes and checks the three lowest layers and all lower-bound instances through \(n=40\). On execution it prints:

`VERIFY_OK determinant_monomials=16 exhaustive_assignments=87360 n=3..8 min_nearmin_profiles=3..40`

These checks verify the crucial finite algebraic identity and small instances; the exact infinite-family statements follow from the preceding general proofs and coefficient extraction. No claims about untested graph families or arbitrary external implementations are made.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević and Tepeh introduced \(k\)-limited domination and its relation to \((1,t)\)-domination [1]. Radić and Tepeh studied the \(1\)-limited problem on cubic graphs, proving NP-completeness and exact Goldberg-snark minima [2]; their primary subject classification is 05C69, and the first public source appeared on 2026-10-01. Tepeh established Cartesian-product bounds and exact values for several other families [3], including prism connections under a different parameter regime and general bounds that imply the present minimum \(n\). No new priority is asserted for the lower bound \(n\) by itself.

Allagan's 2026 prism paper [4] uses cyclic-word methods for the **ordinary** domination number and counts of *ordinary* minimum dominating sets, not for the entire size distribution of \(1\)-limited dominating sets. Its overlapping graph and method do not make the additional local selected-vertex constraint automatic. The present theorem supplies an all-cardinality limited-domination polynomial and the parity-dependent gap mechanism, which are not stated in the inspected sources. An earlier unlocated classification under \((1,2)\)-domination terminology remains a historical-priority risk.

## Limitations

This is a complete formula only for the labelled, two-row **circular** prism family and for the \(1\)-limited condition. It does not enumerate unlabelled orbits, open ladders, arbitrary Cartesian products, or variants in which exterior vertices have bounded numbers of selected neighbours. A finite transfer-matrix proof for bounded width is a standard enumerative technique; the substantive conclusion here is the exact factorization, all-cardinality distribution, and infinite non-unimodal support-gap family. Same mathematical model proof review and finite replay do not constitute independent validation. Comprehensive historical priority is not claimed.

## References

[1] D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422v1 (first public 2026-06-21), https://arxiv.org/abs/2606.22422.

[2] G. Radić, A. Tepeh, *On \(1\)-limited and \((1,2)\)-domination in cubic graphs*, arXiv:2610.01796v1 (first public 2026-10-01), https://arxiv.org/abs/2610.01796.

[3] A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428v2, https://arxiv.org/abs/2606.22428.

[4] J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488v1, https://arxiv.org/abs/2601.03488.
