# Three rational hyperflexes characterize one projective orbit of binary plane quartics

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_2}\) be a geometrically smooth plane quartic. A *rational hyperflex* is a point \(P\in C(\mathbf F_2)\) for which the scheme-theoretic intersection of the tangent line with \(C\) is \(4P\). Then \(C\) has at most **three** rational hyperflexes. Exactly **28** smooth quartic equations attain this bound: one for each noncollinear unordered triple in \(\mathbf P^2(\mathbf F_2)\). They form one orbit under \(\operatorname{PGL}_3(\mathbf F_2)\), of size \(28\), with stabilizer isomorphic to \(S_3\).

The unique quartic having the three coordinate vertices as hyperflexes is
\[
F_0=XY(X^2+XY+Y^2)+XZ(X^2+XZ+Z^2)+YZ(Y^2+YZ+Z^2).
\]
Its entire rational-point set comprises those same three vertices. Thus the maximal hyperflex triple determines both the curve and its complete rational-point set.

## Assumptions and scope
All polynomials are homogeneous of degree four over \(\mathbf F_2\). Smooth means geometrically nonsingular over an algebraic closure, not merely nonsingular at rational points. Tangent intersection multiplicity is defined over that algebraic closure. Quartic equations are counted in the fixed ternary coordinate space; over \(\mathbf F_2\) there is only one nonzero scalar, so equation and hypersurface counts coincide. The equivalence group is \(\operatorname{PGL}_3(\mathbf F_2)\), not the group of abstract curve isomorphisms. The claim is a sharp extremal classification, not a claim about the full Weierstrass divisor.

## Proof
**1. A hyperflex triple cannot be collinear.** A smooth plane quartic cannot contain a line. Suppose that three distinct rational hyperflexes lie on one rational line \(L\). Restrict its quartic equation to \(L\cong\mathbf P^1_{\mathbf F_2}\). The nonzero degree-four binary form vanishes at the three rational points of \(L\); hence it is divisible by the three distinct rational linear factors corresponding to those points. The remaining degree-one factor is rational and therefore repeats one of them. At that point the intersection multiplicity of \(L\) and \(C\) is at least two, so \(L\) is its tangent line. But \(L\) also contains the two other points of \(C\), contradicting the defining divisor \(4P\) of a hyperflex tangent. Therefore every triple of distinct rational hyperflexes is noncollinear.

**2. Normalize the triple and its three tangents.** Three noncollinear rational points form a projective coordinate frame over \(\mathbf F_2\); send them to \(e_X=(1:0:0)\), \(e_Y=(0:1:0)\), and \(e_Z=(0:0:1)\). A hyperflex tangent at one of these points cannot pass through either of the other two points. In the Fano plane there are exactly three rational lines through each point, so the respective tangent lines are necessarily
\[
L_X:\ Y+Z=0,\qquad L_Y:\ X+Z=0,\qquad L_Z:\ X+Y=0.
\]
On \(L_X\), the restriction of the defining quartic has its unique zero of multiplicity four at \(e_X\). In homogeneous coordinates \((X,Y,Z)=(u,v,v)\), this restriction is therefore \(v^4\); its coefficient is \(1\), since a coefficient \(0\) would make the whole line a component of a smooth quartic. Analogously, the restrictions on \(L_Y\) and \(L_Z\) are the fourth powers of their parameters vanishing at the corresponding vertices.

**3. The three restrictions identify one smooth candidate.** The displayed \(F_0\) has exactly those three line restrictions. Thus any candidate \(F\) differs from \(F_0\) by a quartic vanishing on three distinct rational lines. In the polynomial ring this difference is divisible by their product, yielding
\[
F=F_0+(X+Y)(X+Z)(Y+Z)(aX+bY+cZ),\quad a,b,c\in\mathbf F_2.
\]
At \(e_X\), both \(\nabla F_0\) and \(\nabla[(X+Y)(X+Z)(Y+Z)]\) equal \((0,1,1)\). Consequently \(\nabla F(e_X)=(0,1+a,1+a)\). Smoothness at this point forces \(a=0\). The same argument at \(e_Y,e_Z\) forces \(b=c=0\). Hence \(F=F_0\): there is at most one smooth quartic realizing the normalized triple.

**4. \(F_0\) is geometrically smooth.** Put \(s=X+Y+Z\), \(q=XY+XZ+YZ\), and \(r=XYZ\). Direct expansion in characteristic two gives \(F_0=s^2q+sr+q^2\) and
\[
(F_{0,X},F_{0,Y},F_{0,Z})=((Y+Z)(s^2+YZ),\ (X+Z)(s^2+XZ),\ (X+Y)(s^2+XY)).
\]
At any common zero of the derivatives with \(s=0\), each derivative equals \(r\), hence \(r=0\). Up to permutation and scaling, the point is \((1:1:0)\), where \(q=1\) and \(F_0=q^2=1\), so this is not a singular point of the curve.

If \(s\ne0\), scale to \(s=1\). If one coordinate equals \(1\), say \(X=1\), then \(Y=Z\), and \(F_{0,Y}=(1+Y)^2=0\) forces \(Y=Z=1\). Otherwise none of \(X,Y,Z\) equals \(1\), so \(X+Y=1+Z\), \(X+Z=1+Y\), and \(Y+Z=1+X\) are all nonzero. The derivative equations therefore yield \(XY=XZ=YZ=1\), which forces \(X=Y=Z=1\), again a contradiction to that case. The only remaining common derivative zero with \(s\ne0\) is \((1:1:1)\), where \(F_0=1\). Thus \(F_0\) and its partial derivatives have **no common projective zero over the algebraic closure**, proving geometric smoothness.

**5. Rational points, existence, and the sharp count.** On the three coordinate vertices, \(F_0=0\), and the restrictions from step 2 show that these points are hyperflexes. On a rational point with exactly two nonzero coordinates, precisely one of the three displayed pairwise terms is \(1\), so \(F_0=1\); at \((1:1:1)\), the three pairwise terms sum to \(1\). There are therefore no other rational points. In particular, \(F_0\) has exactly three rational hyperflexes. Every noncollinear triple is carried to the coordinate triple by an element of \(\operatorname{PGL}_3(\mathbf F_2)\), and steps 2–4 show it determines precisely one smooth quartic. A fourth rational hyperflex on any smooth quartic would yield a noncollinear triple; by uniqueness it would force a coordinate transform of \(F_0\), whose rational-point set has only three points. Therefore the maximum is three.

Finally, the seven nonzero vectors of \(\mathbf F_2^3\) represent its seven projective points. An ordered noncollinear triple is exactly an ordered vector-space basis, of which there are \((2^3-1)(2^3-2)(2^3-2^2)=168\). After dividing by the six permutations, there are \(28\) unordered triples. The projective stabilizer of each triple is exactly its six coordinate permutations, a copy of \(S_3\). By the uniqueness theorem, this is also the full projective stabilizer of its associated quartic.

## Verification
The independent `verify_three_hyperflex.py` verifier enumerates all \(2^{15}-1=32767\) nonzero homogeneous ternary quartic forms. Using exact polynomial restrictions to the rational tangent line, it identifies exactly \(28\) forms having three rational hyperflexes and verifies a bijection with all \(28\) noncollinear rational triples. It checks the representative's geometric smoothness by exact Gröbner bases on each affine chart, and independently computes all \(168\) projective linear substitutions, obtaining an orbit of size \(28\) and stabilizer order \(6\). Run `python verify_three_hyperflex.py` with SymPy available; the script regenerates `three_hyperflex_certificate.json` and prints `three_hyperflex_verification.txt`'s recorded checks. The exhaustive computation corroborates rather than replaces the non-computational proof above.

## Relationship to prior work
Asgarli and Ghioca (first publicly posted 2023-02-26, arXiv:2302.13420) study rational tangent-line configurations of finite-field plane curves; the present sharp hyperflex configuration question is distinct from tangent-filling. Nart and Ritzenthaler (arXiv:math/0312366) classified nonhyperelliptic genus-three curves over even finite fields up to isomorphism, providing normal forms and geometric bitangent structure; this classification is not being claimed anew. The present statement classifies a particular rational *contact-four* incidence configuration and uniquely determines its fixed-coordinate quartic for each maximal rational triple, rather than merely counting bitangent lines or abstract curves. Hilario and Stöhr (arXiv:2306.08579) discuss special singular quartic fibrations, which do not impose geometric smoothness on individual quartics in this theorem.

## Limitations
The result concerns only rational hyperflex points and only the field \(\mathbf F_2\); it does not classify all ordinary rational flexes, all bitangents, or higher-field phenomena. A complete earlier or unindexed calculation of these rational hyperflex triples, potentially obtainable from historical normal-form classifications or Weierstrass-point studies, has not been ruled out definitively. The article by Viana and Paz La Torre on genus-three curves in characteristic two (DOI:10.1080/00927870500288036) was located by abstract, but its complete text could not be inspected during this investigation. No independent external audit has been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first public version, 2023-02-26), https://arxiv.org/abs/2302.13420.
2. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2003), https://arxiv.org/abs/math/0312366.
3. R. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579 (2023), https://arxiv.org/abs/2306.08579.
4. M. Viana and M. C. Paz La Torre, *Curves of genus three in characteristic two*, Communications in Algebra (2005), DOI:10.1080/00927870500288036 (abstract accessed; full text not inspected).
