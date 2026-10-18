# Six proper rational tritangent planes on a canonical genus-four curve on the binary quadric cone
## Finding
Let \(k=\mathbf F_2\), let \(Q\subset\mathbf P^3_k\) be the quadric cone \(XZ+Y^2=0\), and let \(C=Q\cap V(F)\) be a geometrically smooth cubic section. A **proper rational tritangent plane** means a \(k\)-rational hyperplane \(H\) for which the scheme-theoretic hyperplane divisor on \(C_{\overline k}\) is \(2(P_1+P_2+P_3)\), where the three geometric points are distinct. This definition counts both tangent planes to the cone arising from its ruling and transverse planes; it is not restricted to odd theta-characteristic planes.

**Theorem.** Every such \(C\) has at most six proper rational tritangent planes. Equality occurs for exactly **144** cubic sections in the natural 16-dimensional quotient space of cubic equations modulo multiples of \(Q\), forming exactly **three** projective equivalence classes under \(\operatorname{Aut}_k(Q)\). Every maximizer has precisely three cone-tangent and three transverse proper rational tritangent planes. Two extremal classes have one rational curve point and one has no rational curve points.

The **complete spectrum** for the 12,288 geometrically smooth sections is:

| Proper rational tritangents | Number of smooth cubic sections | Number of projective classes |
| ---: | ---: | ---: |
| 0 | 448 | 10 |
| 1 | 2,392 | 55 |
| 2 | 4,536 | 95 |
| 3 | 3,512 | 81 |
| 4 | 1,016 | 24 |
| 5 | 240 | 6 |
| 6 | **144** | **3** |
| **Total** | **12,288** | **274** |

An extremal equation is
\[
F=X^3+X^2Y+X^2W+XYW+Y^2W+Z^3+W^3=0.
\]
Its six planes are \(X=0\), \(Z=0\), \(X+Z=0\), \(W+Y=0\), \(W+X=0\), and \(W+X+Y=0\). The first three are tangent to \(Q\), and the final three cut smooth conics on \(Q\). This curve has exactly one \(k\)-point.

## Assumptions and scope
All equations and projective equivalences are defined over \(\mathbf F_2\). Smoothness and distinctness of contacts are geometric, i.e. over an algebraic closure, and a contact plane need only be \(\mathbf F_2\)-rational; the points of tangency need not be rational. The quadric cone has vertex \([0:0:0:1]\). A smooth section cannot contain this vertex, and therefore its cubic defining equation must have a nonzero coefficient of \(W^3\), which equals one over \(\mathbf F_2\). As \(Q\) is fixed, two cubic equations defining the same scheme-theoretic section are identified modulo \(Q\) times a linear form. The resulting quotient has dimension 16. We choose the 16 degree-three monomials not divisible by \(XZ\) as its ordered basis, because the relation \(XZ=Y^2\) gives a unique reduction. The smooth sections are canonical nonhyperelliptic curves of genus four by adjunction for complete intersections of degrees two and three.

The full joint distribution by number of rational curve points, cone-tangent proper tritangents, and transverse proper tritangents is supplied in `cone_results.json`. That data also lists one explicit binary coefficient-mask representative and orbit cardinality for each of the 274 projective classes. The three extremal masks, in the monomial order specified in that file, are **37143, 37945, 45079**, each with orbit size 48. The first two have one rational point and the last has no rational points.

## Proof
**1. Exhaustive parameter domain.** Among the \(2^{16}-1\) nonzero cubic section classes, smoothness forces the coefficient of \(W^3\) to equal one. Thus there are exactly \(2^{15}=32,768\) possible smooth candidates. Every eligible class appears exactly once in this canonical binary-mask representation. A section containing the vertex cannot be smooth because all partial derivatives of \(Q\) vanish at the vertex, so the projective complete-intersection Jacobian has rank at most one there.

**2. Exact geometric smoothness criterion.** On the chart \(X\ne0\), the cone is parametrized by \((X,Y,Z,W)=(1,t,t^2,w)\); on \(Z\ne0\), use \((t^2,t,1,w)\). Together these charts cover the cone outside the vertex. In either chart the cubic section is
\[
f(t,w)=w^3+a(t)w^2+b(t)w+c(t),\quad \deg a\le2,\ \deg b\le4,\ \deg c\le6.
\]
In characteristic two \(f_w=w^2+b(t)\). At a simultaneous zero of \(f\) and \(f_w\), the relation \(w^2=b(t)\) reduces \(f=0\) to \(D(t)=a(t)b(t)+c(t)=0\). The remaining partial derivative is \(f_t=a'(t)b(t)+b'(t)w+c'(t)\), whose square, after substituting \(w^2=b(t)\), is
\[
E(t)=(a'(t)b(t)+c'(t))^2+b'(t)^2b(t).
\]
Every element of the algebraic closure has a unique square root, so the section has a geometric singularity on the chart **if and only if** \(D\) and \(E\) have a common geometric zero. Equivalently, the polynomial gcd of \(D\) and \(E\) over \(\mathbf F_2\) is not one. The two-chart criterion is exact, with no bounded-point sampling. Running it over the 32,768 candidates yields exactly 12,288 smooth sections.

**3. Exact geometric tritangency criterion.** There are exactly 15 rational hyperplanes in \(\mathbf P^3_k\). Seven contain the cone vertex. Of these, exactly three are tangent to the cone: \(X=0\), \(Z=0\), \(X+Z=0\). Their intersections with \(Q\) are doubled ruling lines. Each is a proper tritangent precisely when the binary cubic obtained by restricting \(F\) to the corresponding ruling line has three distinct geometric zeros. The remaining four vertex-containing planes cut two distinct geometric ruling lines; because a smooth section misses the vertex, each component contributes a divisor of odd degree three, so their total cannot be twice a divisor. Hence none of the remaining four planes is tritangent.

The other eight rational planes have equations \(W+uX+vY+zZ=0\) with \((u,v,z)\in k^3\). Their sections on \(Q\) are smooth conics parametrized by
\[
(X,Y,Z,W)=(s^2,st,t^2,us^2+vst+zt^2).
\]
The hyperplane divisor on \(C\) is the zero divisor of the homogeneous binary sextic obtained by substituting this parametrization into \(F\). It is twice three distinct geometric points exactly when the sextic is the square of a squarefree binary cubic. Over \(k=\mathbf F_2\), a binary cubic \(As^3+Bs^2t+Cst^2+Dt^3\) is squarefree if and only if \(AD+BC=1\). Squaring the cubic produces only even exponent terms. Thus the eight tests are exact binary coefficient comparisons plus the stated discriminant condition.

**4. Distribution and orbits.** Directly applying these finite exact tests to every smooth class produces the seven-row distribution stated above, as well as the full joint distribution in `cone_results.json`. Every automorphism of \(Q\) fixes its unique vertex and induces a projectivity on its base conic. There are six such base projectivities (\(\operatorname{PGL}_2(\mathbf F_2)\)), and the vertex coordinate can additionally be shifted by any linear form in \(X,Y,Z\), giving eight choices. Thus \(\lvert\operatorname{Aut}_k(Q)\rvert=48\). Its 48 matrices, applied to each cubic and reduced modulo \(XZ+Y^2\), partition the candidate space into 752 orbits. Exactly 274 are smooth; their sizes sum to 12,288. Each orbit is constant in the rational-point and tritangent invariants, and the three six-tritangent orbits have size 48 apiece. There are no seven-tritangent examples, since all smooth candidates have been checked.

**5. Witness.** For the displayed extremal equation, the restrictions to the three rational ruling lines are, in the homogeneous ruling parameter \((\lambda:\mu)\), the cubics with coefficient lists \((1,1,0,1)\), \((1,0,0,1)\), \((1,1,0,1)\), respectively. The three transverse planes displayed above each pull back to the sextic with coefficient bits \((1,0,1,0,0,0,1)\), which is the square of the cubic with coefficients \((1,1,0,1)\). All these cubics satisfy \(AD+BC=1\), so the six contact divisors are proper. Exact substitution verifies smoothness and one rational point.

## Verification
`cone_census.py` independently enumerates all 32,768 vertex-avoiding cubic masks, uses exact polynomial gcds for geometric smoothness, tests all 15 rational planes, and calculates all 48 automorphisms and their orbit partitions. Its output is the accompanying `cone_results.json`.

`verify_extension.cpp` implements an independently coded smoothness check by evaluating the affine Jacobian equations over the six fields \(\mathbf F_{2^m}\), \(1\le m\le6\), using explicit irreducible polynomials. This is exhaustive for this application: unless \(D\equiv0\), every possible singular chart parameter is a zero of \(D\) of degree at most six; when \(D\equiv0\), the factorization \(f=(w+a)(w^2+b)\) makes all possible singular parameters roots of \(b'\) or \(a^2+b\), of degrees at most four. The verifier also reconstructs every hyperplane contact test independently using direct binary-form multiplication and square testing. It reproduces the full joint distribution, not only the maximum.

A third method checks geometric smoothness on one representative from **every one of the 752 automorphism orbits** via Gröbner bases of \((f,f_t,f_w)\) over \(\mathbf F_2\) on both affine charts; it agrees with the polynomial-gcd method on all 752 representative decisions. The fixed-data trace `groebner_agreement.txt` summarizes this check. Finally, the total of 274 cone-section classes combines with the separately known smooth-quadric class counts to recover the published overall genus-four nonhyperelliptic census of 780 classes; that numerical agreement is supporting evidence, not a substitute for the independent algebraic checks.

To reproduce the two exhaustive enumerations, run `python3 cone_census.py cone_results.json` and `g++ -O3 -std=c++17 verify_extension.cpp -o verify_extension && ./verify_extension` in the directory containing the package files. Check the joint entries of `cone_results.json` against standard output from the compiled verifier. No nonstandard Python packages are needed for these two core enumerations. For the Gröbner cross-check, install SymPy and follow `verify_groebner.py`.

## Relationship to prior work
Xarles (2020) classifies genus-four curves over \(\mathbf F_2\), including their quadric models, abstract isomorphism classes and low-degree point statistics. The 274 rank-three-quadric classes agree with the corresponding portion of that census; neither the proper tritangent distribution nor its sharp six-plane obstruction is presented there.

Kulkarni, Ren, Sayyary Namin and Sturmfels (2017) explain why a genus-four canonical curve on a singular quadric has infinitely many geometric tritangent planes, and distinguish the 120 odd-theta planes from the cone's tangent-plane family. The present theorem counts **rational planes whose contacts are three distinct geometric double points**, which includes the three rational ruling-tangent planes. The cited general construction implies that the ruling planes are tangential, but it gives neither the exact proper-contact conditions nor the finite-field spectrum or exceptional projective classes.

Bouchet (2023) treats invariant-theoretic classification of genus-four curves over algebraically closed fields of characteristic zero, not the rational hyperplane incidence classification in characteristic two. Hanselman, Pieper and Schiavone (2024) reconstruct generic genus-four curves from theta constants in characteristic zero or sufficiently large positive characteristic. It does not determine the characteristic-two contact spectrum.

## Limitations
The theorem is restricted to the fixed rank-three quadric cone over \(\mathbf F_2\), not to all genus-four curves or larger fields. The word *tritangent* in this result includes cone-ruling contact planes, unlike conventions restricting the term to the 120 odd-theta planes; counts must not be interchanged without this distinction. The exhaustive programs constitute reproducible computational proof for a finite domain, not an independent mathematical audit. Literature searches are not a proof of publication priority. A previous unindexed classification or unpublished computation may have determined an equivalent spectrum.

## References
1. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822, first public 2020-07-15. https://arxiv.org/pdf/2007.07822
2. A. Kulkarni, Y. Ren, M. Sayyary Namin, B. Sturmfels, *Real Space Sextics and their Tritangents*, arXiv:1712.06274, first public 2017-12-18. https://arxiv.org/pdf/1712.06274
3. T. Bouchet, *Invariants of genus 4 curves*, arXiv:2310.01158, first public 2023-10-02. https://arxiv.org/pdf/2310.01158
4. J. Hanselman, A. Pieper, S. Schiavone, *Equations of genus 4 curves from their theta constants*, arXiv:2402.03160, first public 2024-02. https://arxiv.org/html/2402.03160v2
