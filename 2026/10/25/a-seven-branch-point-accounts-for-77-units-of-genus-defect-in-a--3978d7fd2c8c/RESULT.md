# A seven-branch point accounts for \(77\) units of genus defect in a degree-\(17\) radical plane curve

## Finding
For the degree-\(17\) rational plane curve of Sendra-Arranz, J. R. Sendra and J. Sendra, Example 38, the projective point \(P=[0:1:0]\) has exactly seven branches: six smooth branches and one unibranch cusp of type \((2,5)\). All seven have tangent \(Z=0\). The six smooth branches split into two groups of three. Every pair in one group has intersection multiplicity \(4\); every cross-group pair has intersection multiplicity \(3\); each smooth branch meets the cusp with multiplicity \(4\). Consequently the local delta invariant is exactly \(\delta_P=77\), the point multiplicity is \(8\), and all other singular points together have total delta invariant \(43\). The last assertion does not classify those other points.

## Assumptions and scope
All varieties and branches are over \(\mathbb C\). Put \(A(h)=h^6-1\), \(F(h)=h^9-h^6-h^3+2\) and \(G(h)=h^5(h^{12}+h^7-2h^6-2h+1)\). Let \(C\subset\mathbb P^2\) be the reduced image of the morphism \(\nu:\mathbb P^1\to\mathbb P^2\) represented in the affine parameter \(h\) by
\[
\nu(h)=[F(h)A(h):G(h):A(h)^2].
\]
The three polynomials are homogenized to common degree \(17\). This is the projective closure of the source's Example 38 rational parametrization, with projective coordinates \([X:Y:Z]\). The proof includes birationality and hence justifies using \(\mathbb P^1\) as the normalization.

## Proof
First the parameterization has no base point. If \(A(h)\ne0\), then \(Z\ne0\); at any sixth root \(\zeta\) of unity, \(F(\zeta)=1\) and \(G(\zeta)=-1\); and at \(h=\infty\) the degree-\(17\) leading term of \(G\) is nonzero. Consequently \(\nu\) is a morphism with pullback of a line of degree \(17\). The image is not a line: the homogeneous coordinate polynomials have pairwise different degrees \(15,17,12\), hence no constant-coefficient linear relation. Since \(17\) is prime and \(\deg\nu\cdot\deg C=17\), the map has generic degree one and \(C\) has degree \(17\). A finite birational morphism from the smooth projective curve \(\mathbb P^1\) gives its normalization.

The inverse image of \(P=[0:1:0]\) is exactly the set of six sixth roots \(\zeta\) of unity and the point \(h=\infty\). Near \(P\) work in affine coordinates \(u=X/Y\), \(v=Z/Y\). At each finite preimage \(\zeta\), \(u\) vanishes to order one and \(v\) to order two; hence this is a smooth branch tangent to \(v=0\). At \(h=\infty\), putting \(s=1/h\) yields \(u=s^2(1+O(s))\), \(v=s^5(1+O(s))\), a cusp with characteristic pair \((2,5)\) and delta invariant \(2\).

For the intersections among the six smooth branches, introduce \(a=A(h)\), \(t=h^3\) and \(q=h^5\). Direct polynomial identities give
\[
F=t^3-t^2-t+2,\qquad G=-1+(1+q)a^2,\qquad t^2=1+a.
\]
At \(h=\zeta\), write \(\varepsilon=\zeta^3\in\{1,-1\}\). For fixed \(\varepsilon\), the local analytic branch of \(t=\varepsilon\sqrt{1+a}\) is independent of the choice of the three corresponding roots, and \(q(0)=\zeta^5\) distinguishes them. The local functions satisfy \(u=Fa/G\), \(v=a^2/G\) and therefore \(v/u^2=G/F^2\). Since \(u=-a+O(a^2)\), the coefficient of \(u^3\) in \(v(u)\) is \(0\) for \(\varepsilon=1\) and \(4\) for \(\varepsilon=-1\): indeed \(F'(0)=0\) and \(-2\), respectively, as a function of \(a\). Opposite-type branches thus have intersection multiplicity exactly \(3\).

For two branches of the same type, \(F\) is identical as a function of \(a\), whereas the first difference in \(G\) is \((\zeta^5-\eta^5)a^2\), which is nonzero. At fixed \(u\), implicit differentiation of \(u=Fa/G\), \(v=a^2/G\) shows that the first induced difference in \(v(u)\) is \((\zeta^5-\eta^5)u^4\) (up to a common nonzero sign convention); hence their intersection multiplicity is exactly \(4\). There are \(2\binom32=6\) same-type pairs and \(3\cdot3=9\) opposite-type pairs.

For any smooth branch \(v=-u^2+O(u^3)\). On the infinite branch, \(u=s^2(1+O(s))\) and \(v=s^5(1+O(s))\). Substitution therefore gives intersection multiplicity \(4\) for each of the six smooth-cusp pairs. The additivity of the delta invariant for reduced plane branches yields
\[
\delta_P=2+6\cdot4+9\cdot3+6\cdot4=77.
\]
The multiplicity of the whole germ is \(6\cdot1+2=8\). Finally the arithmetic genus of a degree-\(17\) plane curve is \(\frac{(17-1)(17-2)}2=120\), while its normalization has genus zero. Thus the sum of the delta invariants away from \(P\) is \(120-77=43\).

## Verification
The accompanying `CHECK.py` reproduces the identities for \(F,G\), verifies their values at the six preimages, checks the two cubic-jet coefficients, and recomputes the exact pairwise intersection and delta arithmetic. The proof, rather than finitely many coefficient tests, establishes the universal analytic branch comparisons. The source's parametrization is quoted only to define the object; the local intersection computation is new work.

## Relationship to prior work
Sendra-Arranz, J. R. Sendra and J. Sendra, *On the Structure of Radical Towers and their Parametrizations*, Example 38, provide the radical construction, explicit rational parametrization, degree \(17\), and normalization genus zero. Their inspected Example 38 does not calculate the projective singularity at \([0:1:0]\), its seven branches, branch-contact multiplicities, or local delta invariant. The standard plane-curve delta formula and Puiseux intersection theory are prior methods, not claimed as new. A targeted search of available mathematical records did not yield the same exact local calculation; historical priority remains open to further archival review.

## Limitations
Only the germ at \(P\) is classified. The residual total delta invariant \(43\) does not locate or classify any remaining singularities. The normalization and local contacts are over \(\mathbb C\); no claim about real branches is made. There has been no independent mathematical audit.

## References
1. J. Sendra-Arranz, J. R. Sendra, J. Sendra, *On the Structure of Radical Towers and their Parametrizations*, arXiv:2610.20404v1 (2026-10-14), Section 5.2, Example 38; https://arxiv.org/html/2610.20404v1.
2. C. T. C. Wall, *Singular Points of Plane Curves*, London Mathematical Society Student Texts 63, Cambridge University Press, 2004 (standard delta and branch-intersection formulas).
