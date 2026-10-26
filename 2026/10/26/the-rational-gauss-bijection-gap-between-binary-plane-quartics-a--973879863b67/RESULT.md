# The rational Gauss-bijection gap between binary plane quartics and sextics

## Finding
Let \(C=V(F)\subset\mathbf P^2_{\mathbf F_2}\) be a geometrically smooth plane curve given by a nonzero homogeneous polynomial of degree \(d\). Suppose \(C(\mathbf F_2)=\mathbf P^2(\mathbf F_2)\), so the curve passes through all seven rational plane points. The restricted rational Gauss map \(\gamma_F\) takes a rational point \(P\) to its tangent line \(T_PC\), viewed as a rational point of the dual plane. Require \(\gamma_F\) to be a bijection of the seven-element rational point and rational line sets.

In degrees \(d=4,5,6\), the respective exact numbers of scalar-normalized homogeneous equations are
\[
24,\qquad 0,\qquad 3048.
\]
Under \(G=\operatorname{PGL}_3(\mathbf F_2)\), the degree-four solutions form one orbit of size \(24\); the degree-six solutions form precisely nineteen orbits, one of size \(24\) and eighteen of size \(168\). In particular, the existence of such smooth curves is not monotone between these three consecutive degrees.

## Assumptions and scope
All coefficients and rational points are over \(\mathbf F_2\); smoothness is **geometric**, meaning no singular points over an algebraic closure. There are no nontrivial scalar multiples of an equation over \(\mathbf F_2\). The Gauss condition requires every rational point to be on the curve and smooth, and the seven corresponding rational tangent lines to be pairwise distinct. No statement about all tangent-filling curves, arbitrary degrees, or abstract isomorphism classes is made.

For reproducible bit encodings, order degree-\(d\) monomials as \(X^iY^jZ^{d-i-j}\), first \(i=0,\ldots,d\) and then \(j=0,\ldots,d-i\); coefficient mask bit \(k\) is the coefficient of the \(k\)-th monomial. The rational point order is lexicographic among nonzero binary triples.

## Proof
**Incidence step.** Every nonzero tangent vector at a rational curve point determines one of the three rational lines through that point. Enumerating the \(3^7\) line assignments and retaining those using all seven rational lines gives exactly **24** incidence bijections. This is an exhaustive finite search over all choices, not a sample.

**First-jet step.** For each point \(P\), choose the first nonzero homogeneous coordinate as its affine chart denominator; record the value of the form and its two affine partial derivatives. This defines a linear map from the \(\binom{d+2}{2}\)-dimensional space of degree-\(d\) forms to \(\mathbf F_2^{21}\). The exact binary ranks for \(d=3,4,5,6\) are \(10,15,21,21\). The rank-\(21\) assertion for quintics has an independent geometric proof: a quintic vanishing to order at least two at all seven Fano points restricts to a polynomial with at least six zeros counted with multiplicity on every rational line, hence contains each of the seven rational lines as a component; degree five forces it to be zero. Since the source and target both have dimension \(21\), fifth-degree first-jet evaluation is an isomorphism. Degree-six surjectivity also follows by multiplying first-jet interpolation basis elements of degree five by suitable linear forms nonzero at the specified point. Its kernel therefore has dimension seven.

**Degree four and five.** Every one of the 24 bijective tangent assignments has exactly one polynomial solution in degree four (because the full jet map has zero kernel), and exactly one in degree five (by isomorphism). For each solution geometric smoothness is decided by the ideals \( (f,\partial_uf,\partial_vf)\) on the three standard affine charts. Exact characteristic-two Gröbner reductions find all 24 degree-four solutions geometrically smooth and all 24 degree-five solutions geometrically singular. One degree-five representative has coefficient mask `0xea11e`; on the \(Z=1\) chart its singularity ideal has reduced Gröbner basis \(\{X^2+Y^4+Y^2+1,\ Y^6+Y^2+1\}\), hence a geometric singular point. The attached finite enumerator checks all 24 cases, not just the representative.

**Degree six.** Each incidence assignment specifies 21 jet bits and lifts to an affine coset of the seven-dimensional kernel; hence exactly \(2^7=128\) sextic equations. For one assignment, an exhaustive scan with exact Gröbner calculations on each affine chart finds **127 smooth sextics and one singular sextic** (singular representative mask `0x7408822`). The full 168-element group \(\operatorname{PGL}_3(\mathbf F_2)\) acts transitively on all 24 incidence assignments (the code's three elementary generators suffice), so the total smooth count is \(24\cdot127=3048\). Exhaustive orbit closure under the same generators yields one orbit of size 24 and eighteen of size 168. Each orbit's nonzero defining forms remain scalar-normalized because the field has two elements.

An explicit geometrically smooth witness has coefficient mask `0x6026b22`, which in ordinary coordinates is
\[
X^5Y+X^5Z+X^2Y^4+X^2YZ^3+X^2Z^4+XY^4Z+XY^2Z^3+XYZ^4+Y^5Z+YZ^5=0.
\]
Its three affine chart Jacobian ideals all contain \(1\), as confirmed in the attached output.

**Completeness of geometric checks.** On each affine chart, an ideal generated by the dehomogenized equation and its two partial derivatives has a common zero over an algebraic closure exactly when its Gröbner basis is not \(\{1\}\). The three standard charts cover projective space. Thus the exact algebraic computations decide geometric, not merely rational, smoothness. All enumerations run over finite explicit lists, and the group computation exhausts the generated group actions.

## Verification
Run `python verify_gauss.py` (Python 3 and SymPy required) and compare with `verification_output.txt`. The code enumerates all 24 point–line incidence bijections, solves binary first-jet systems in degrees three through six, performs Gröbner computations for every relevant quartic/quintic and every sextic lift of one incidence matching, and exhausts orbit closure for sextics. The exact nineteen sextic orbit representatives, coefficient masks, and orbit sizes appear in the output. No random input or floating-point operations are used.

## Relationship to prior work
Asgarli–Ghioca's *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, 2023) studies the rational Gauss map through tangent-line covering and explicitly discusses prescribing points and incident tangents by interpolation. It does not give this seven-point **bijective** Gauss restriction census, its degree-five smoothness gap, or the degree-six orbit classification. Their paper on small-degree plane-filling curves (arXiv:2307.03072, 2023) addresses existence and low-degree plane filling but not this dual incidence refinement. The genus-six census by Huang–Kedlaya–Lau (arXiv:2402.00716, 2024) concerns the quintic/genus-six case, not the degree-six/genus-ten classification; the quartic and quintic counts alone are not offered as separately original discoveries. The finite-geometry and jet-interpolation steps are standard; the new asserted contribution is their sharp combined arithmetic and symmetry classification in the indicated range.

## Limitations
The result concerns **equations up to nonzero field scalar**, not arbitrary abstract-isomorphism classes or all possible finite extensions. It does not classify smooth sextics with repeated rational tangents. The count is a complete finite computation supported by an independent linear-algebra argument and exact algebraic-geometry criterion, but it has not undergone independent external review. An unindexed published census or a specialization of a more general tangent-map classification might precede this calculation; the searched literature did not resolve every such priority risk. Characteristic-two inseparability of the global Gauss map does not affect the stated finite rational-point restriction.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first public 2023-02-26), https://arxiv.org/abs/2302.13420.
2. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (2023), https://arxiv.org/abs/2307.03072.
3. E. Huang, K. Kedlaya, and J. Lau, *A census of genus 6 curves over the field with two elements*, arXiv:2402.00716 (2024), https://arxiv.org/abs/2402.00716.
