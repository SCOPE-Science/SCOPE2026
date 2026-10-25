# Bitangent-contact arithmetic of two exceptional ternary double planes

## Finding
Let \(k=\overline{\mathbb F}_3\). Consider the smooth plane quartics
\[
B_1:\;(x^2+y^2)^2+y^3z-yz^3=0,\qquad
B_2:\;x^4+y^3z-yz^3=0.
\]
They are the branch curves of the two exceptional degree-two del Pezzo surfaces over \(\mathbb F_3\) studied in the work cited below. In each case there are exactly 28 distinct geometric bitangent lines, where a hyperflex tangent (intersection multiplicity four at one point) counts as a bitangent.

For \(B_1\), exactly one bitangent is a hyperflex, namely \(y=0\). The other 27 each have two distinct simple tangencies (multiplicity two each). Their 54 contact points are pairwise distinct, so the support of the full bitangent-contact locus has exactly 55 points. Its geometric Frobenius cycle lengths are
\[
1^1 2^9 6^6.
\]
Thus its entire contact support becomes rational over \(\mathbb F_{3^6}\), and not over any proper subfield of this extension containing \(\mathbb F_3\).

For \(B_2\), all 28 bitangents are hyperflexes. There are exactly 28 distinct contact points, with Frobenius cycle lengths
\[
1^4 4^6.
\]
The full contact support first becomes rational over \(\mathbb F_{3^4}\).

All bitangents besides \(y=0\) have a unique form \(z=sx+ty\). Their complete parameter sets are
\[
\begin{aligned}
B_1:&\quad s^9+s^3+s=0,\qquad t^3-t=s^4-s^6;\\
B_2:&\quad s^9+s=0,\qquad t^3-t=s^4.
\end{aligned}
\]
For \(B_1\), the bitangent-line Frobenius cycles are \(1^{10}3^6\); for \(B_2\), they are \(1^4 4^6\). In particular, the distinct geometric bitangent-contact **points**, not just the bitangent lines or abstract exceptional-curve Galois representations, have the stated exact arithmetic distributions.

## Assumptions and scope
All statements refer to the specified coefficientwise quartics in characteristic three, their geometric lines, and geometric contact points. A geometric bitangent means a line whose intersection divisor with a smooth plane quartic is even, including a fourfold contact. Frobenius cycles are for \(a\mapsto a^3\). The classification is not asserted for arbitrary plane quartics or other del Pezzo surfaces. The pair of double covers is defined by \(-w^2=F_i(x,y,z)\) in \(\mathbb P(1,1,1,2)\), where \(F_i\) defines \(B_i\).

The quartics are smooth: for \(F_1\), partial derivatives modulo three are \(x(x^2+y^2),\;y(x^2+y^2)-z^3,\;y^3\); for \(F_2\), they are \(x^3,-z^3,y^3\). Neither gradient vanishes at a projective point.

## Proof
**Completeness of the line chart.** A projective line not expressible as \(z=sx+ty\) projects to a point in the \((x:y)\)-line, so has equation \(y=cx\) or \(x=0\). Except for \(y=0\), the restricted quartic has a nonzero term cubic in \(z\) but no \(z^4\) term. This is impossible for a square of a binary quadratic, because the vanishing of its \(z^4\) coefficient forces its \(z^2\) coefficient to vanish as well. The line \(y=0\) restricts each quartic to \(x^4\), hence is a hyperflex.

**Square restrictions.** For \(z=sx+ty\), the coefficients of \((x^4,x^3y,x^2y^2,xy^3,y^4)\) are, respectively,
\[
(1,-s^3,-1,s,1+t-t^3)\quad\text{and}\quad(1,-s^3,0,s,t-t^3)
\]
for \(F_1\) and \(F_2\), with all arithmetic in characteristic three. A monic binary quartic is a square exactly when it equals \((x^2+vxy+uy^2)^2\) for some \(u,v\). Comparing the \(x^3y\) and \(x^2y^2\) coefficients gives
\[
(v,u)=(s^3,1+s^6)\quad\text{or}\quad(s^3,s^6).
\]
The remaining two coefficient comparisons reduce, respectively, to the two systems in the Finding. When those systems hold, the restrictions are exactly
\[
F_1|_{z=sx+ty}=(x^2+s^3xy+(1+s^6)y^2)^2,
\]
\[
F_2|_{z=sx+ty}=(x-s^3y)^4.
\]
The first contact quadratic has discriminant \(s^6-4(1+s^6)=-1\), which is nonzero, while the second is the square of a linear polynomial. Consequently the 27 nonvertical \(B_1\) bitangents are ordinary and every \(B_2\) bitangent is hyperflex. No distinct tangent lines can share a contact point because a smooth plane curve has a unique tangent at every point.

**Counting fields and Frobenius cycles.** In \(\mathbb F_3[s]\),
\[
s^9+s^3+s=s(s-1)(s+1)(s^3-s+1)(s^3-s-1).
\]
Both cubic factors are irreducible. The three roots \(s\in\mathbb F_3\) each admit three values \(t\in\mathbb F_3\). For each of the six roots of the cubics, \(s\in\mathbb F_{27}\) and \(s^3=s+\varepsilon\) for some \(\varepsilon\in\{1,-1\}\). The equation for \(t\) then has right-hand side \(s^4-s^6=-\varepsilon s-1\), of trace zero from \(\mathbb F_{27}\) to \(\mathbb F_3\) because \(s+s^3+s^9=0\). Thus there are exactly three solutions \(t\in\mathbb F_{27}\), and all 18 corresponding lines have degree exactly three. Adding \(y=0\), the line-cycle profile is \(1^{10}3^6\).

Similarly,
\[
s^9+s=s(s^4+s^2-1)(s^4-s^2-1),
\]
with both quartic factors irreducible over \(\mathbb F_3\). The root \(s=0\) gives three values \(t\in\mathbb F_3\). Each of the eight other roots lies in \(\mathbb F_{81}\) and satisfies \(s^9=-s\), so \(\operatorname{Tr}_{\mathbb F_{81}/\mathbb F_3}(s^4)=s^4-s^4+s^4-s^4=0\). Therefore the equation for \(t\) has three solutions in \(\mathbb F_{81}\), producing 24 lines of degree exactly four. Adding \(y=0\), the line-cycle profile is \(1^4 4^6\).

For \(B_1\), the 27 ordinary bitangents have contact quadratics of discriminant \(-1\). This element is nonsquare in both \(\mathbb F_3\) and \(\mathbb F_{27}\); over each line's definition field, Frobenius of that field exchanges the two contact points. The nine rational ordinary lines contribute nine two-cycles of contact points, and the six degree-three orbits of ordinary lines contribute six six-cycles of contact points. The \(y=0\) contact point \([0:0:1]\) is rational. For \(B_2\), each hyperflex point is uniquely determined by its bitangent line and defined over the same field; distinctness gives the contact-point cycles \(1^4 4^6\). The least common fields follow from the longest cycle lengths.

For context, the 56 exceptional curves on the respective degree-two del Pezzo double covers have splitting fields \(\mathbb F_{3^6}\) and \(\mathbb F_{3^4}\): over a bitangent with the displayed monic square restriction, the two components are given by \(w=\pm i q(x,y)\), where \(i^2=-1\). The scalar \(-1\) is nonsquare in odd-degree extensions of \(\mathbb F_3\), and is square in even-degree extensions. Their Frobenius cycle profiles are \(2^{10}6^6\) and \(2^4 4^{12}\), respectively. These curve-orbit statements are ancillary and are not asserted to supersede prior Weyl-group Galois computations.

## Verification
The standalone script `verify.py` implements \(\mathbb F_{27}\) and \(\mathbb F_{81}\) by irreducible polynomial quotient rings and enumerates all \(q^2\) pairs \((s,t)\) in each field. It separately checks square-form coefficients by exhaustive quadratic matching and computes the full line Frobenius cycle decomposition and hyperflex counts; it prints `VERIFY_OK`. The computations verify the finite enumerations. Completeness over the algebraic closure, contact fields, and lack of other lines are proved above rather than inferred from finite searches.

## Relationship to prior work
Salgado–Testa–Várilly-Alvarado (arXiv:1304.6798, 2013) identified the two exceptional degree-two del Pezzo surfaces, explained bitangent/exceptional-curve correspondence (Lemma 4), and computed Galois cohomology and distinguished Weyl-group Galois actions (Remark 29). Festi–van Luijk (arXiv:1408.0269, 2014), Section 3, supplied their explicit branch equations and proved their unirationality. Thus neither the surface equations, general bitangent correspondence, nor the abstract exceptional-curve Galois data are new here. The specific contribution is the explicit complete *contact-divisor* analysis, including the ordinary-versus-hyperflex dichotomy and the contact-point fields and orbit decomposition; these are not supplied by the cited Galois cohomology alone. The hyperflex geometry of the second, Hermitian-type branch quartic is classical; its inclusion serves as a sharp contrast to the first branch curve. Banwait–Fité–Loughran (arXiv:1606.00300, first submitted 2016), Section 4, studies possible Frobenius traces of degree-two del Pezzo surfaces, not these contact multiplicities.

## Limitations
This does not classify the incidence graph of all bitangents or all geometrically rational points on the surfaces, nor establish a general theorem about degree-two del Pezzo surfaces. The exceptional-curve orbit counts themselves may be inferred from preexisting Weyl-action computations and are included only as context, not as a freestanding originality claim. Specialized historical classifications of bitangent contact profiles may contain an equivalent result; the searches described in the accompanying audit do not establish absolute uniqueness. The package's finite-field experiments complement, and do not replace, the algebraic completeness proof. Independent external validation has not been performed.

## References
1. C. Salgado, D. Testa, A. Várilly-Alvarado, *On the Unirationality of del Pezzo surfaces of degree two*, arXiv:1304.6798 (first submitted 2013-04-25), especially Lemma 4, Remark 2, Section 4, and Remark 29. https://arxiv.org/abs/1304.6798
2. D. Festi, R. van Luijk, *Unirationality of del Pezzo surfaces of degree two over finite fields (extended version)*, arXiv:1408.0269 (first submitted 2014-08-01), Sections 2–3 and Remark 3.4. https://arxiv.org/abs/1408.0269
3. B. Banwait, F. Fité, D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300 (first submitted 2016-06-01), Section 4. https://arxiv.org/abs/1606.00300
4. R. Oyono, C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, arXiv:1006.0873 (2010), for broader arithmetic context. https://arxiv.org/abs/1006.0873
