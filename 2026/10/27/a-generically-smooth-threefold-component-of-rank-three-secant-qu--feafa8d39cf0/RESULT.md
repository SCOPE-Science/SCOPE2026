# A generically smooth threefold component of rank-three secant Quot loci for plane curves

## Finding

For any integer \(m\ge4\) and any smooth plane curve \(C\subset\mathbb P^2_{\mathbb C}\) of degree \(m\), put \(L=\mathcal O_C(2)\) and \(V=H^0(C,L^{\oplus2})\). The determinantal locus
\[
Q_m^3=\{[L^{\oplus2}\twoheadrightarrow T]\in\operatorname{Quot}^{0,m}(L^{\oplus2}):\operatorname{rank}(V\to H^0(T))\le3\}
\]
has a generically smooth irreducible component of dimension exactly \(3\). It is the closed image of
\[
(\mathbb P^2)^\vee\times\mathbb P^1\longrightarrow Q_m^3,\qquad
(\ell,[u])\longmapsto[L^{\oplus2}\xrightarrow{u}L|_{C\cap\ell}],
\]
where \(u\) is a nonzero constant linear functional on the two summands, taken modulo scalar. For a transverse line \(\ell\), the Zariski tangent space of \(Q_m^3\) at the corresponding point has dimension \(3\).

The same family consists of \(\pi\)-nondefective length-\(m\) subschemes \((C\cap\ell)\times\{[u]\}\subset C\times\mathbb P^1\), and thus gives a corresponding generically smooth component of the nondefective Hilbert secant locus on the scroll.

## Assumptions and scope

The ground field is \(\mathbb C\). The curve is smooth, irreducible and plane of any degree \(m\ge4\); no genericity hypothesis on the curve is used. The line is generic only when asserting the tangent-space and smoothness statements: it is required to meet the curve in \(m\) distinct points. The rank condition defining the determinantal scheme is imposed on the full \(12\)-dimensional section space. In Hitching's notation this is \(Q_m^{m-f}\) with \(m-f=3\), i.e. \(f=m-3\), for \(E=L^{-1}\oplus L^{-1}\) and \(M=\mathcal O_C\).

The scroll is \(\mathbb P E\simeq C\times\mathbb P^1\), embedded by \(\mathcal O_{\mathbb P E}(1)\simeq L\boxtimes\mathcal O_{\mathbb P^1}(1)\). This bundle is very ample because \(L=\mathcal O_C(2)\) is very ample.

## Proof

**1. Global sections and the rank-three family.** The restriction sequence
\[
0\longrightarrow\mathcal O_{\mathbb P^2}(2-m)\longrightarrow\mathcal O_{\mathbb P^2}(2)\longrightarrow L\longrightarrow0
\]
and \(H^1(\mathbb P^2,\mathcal O(j))=0\) imply \(H^0(C,L)=H^0(\mathbb P^2,\mathcal O(2))\), of dimension \(6\). Let \(D_\ell=C\cap\ell\), a Cartier divisor of length \(m\). Quadrics on the plane restrict to quadratic polynomials on \(\ell\), a space of dimension \(3\). The resulting map into \(H^0(L|_{D_\ell})\) is injective on this three-dimensional space: a nonzero degree-two polynomial on \(\ell\simeq\mathbb P^1\) cannot vanish on the effective length-\(m\) divisor when \(m\ge4\). Thus \(H^0(L^{\oplus2})\to H^0(L|_{D_\ell})\) has rank exactly \(3\) for any nonzero \(u\), so the displayed family lies in \(Q_m^3\).

The family is a morphism from a projective irreducible threefold; its image is closed. It is injective on geometric points: the quotient's support recovers \(D_\ell\), and the unique line cutting out that divisor is \(\ell\), since two distinct linear forms cannot have identical zero divisors on \(C\); the quotient's kernel then recovers its constant fiber direction \([u]\). Consequently its closed image is irreducible of dimension \(3\).

**2. Quot tangent space.** Choose a line \(\ell\) meeting \(C\) transversely, and a basis making \(u=(1,0)\). Put \(D=D_\ell\) and \(T=L|_D\). The kernel of the quotient is
\[
F=L(-D)\oplus L\simeq\mathcal O_C(1)\oplus\mathcal O_C(2).
\]
The tangent space of the ambient smooth torsion Quot scheme is
\[
\operatorname{Hom}_C(F,T)=H^0(\mathcal O_D(D))\oplus H^0(\mathcal O_D),
\]
of dimension \(2m\). The kernel of the global-section evaluation is \(H^0(F)\), with summands of dimension \(3\) and \(6\). Since the evaluation has rank \(3\), linearizing its rank-at-most-three minors gives the condition that the induced deformation from \(H^0(F)\) to the quotient \(H^0(T)/R\) vanish, where \(R\) is the original three-dimensional image.

Choose an affine coordinate \(t\) on \(\ell\) avoiding all points of \(D\), and use the corresponding nonvanishing local trivializations. For the monic separable polynomial \(P(t)\) whose zeros are the points of \(D\), set
\[
A=\mathbb C[t]/(P(t)),\qquad R=\langle1,t,t^2\rangle\subset A,
\qquad R_1=\langle1,t\rangle\subset A.
\]
Then the Quot tangent pair corresponds to \((a,b)\in A^2\). The linearized determinantal condition is exactly
\[
aR_1\subseteq R,\qquad bR\subseteq R.
\]
Indeed, it is the vanishing modulo \(R\) of the products of the deformation pair with the restrictions of sections in the two summands \(H^0(\mathcal O_C(1))\) and \(H^0(\mathcal O_C(2))\) of \(H^0(F)\). There are no additional first-order conditions at a rank-exactly-three point.

**3. Exact multiplier calculation.** Representatives in \(A\) are chosen of degree at most \(m-1\). Because \(1\in R_1\), the first containment implies \(a\in R\); write \(a=a_0+a_1t+a_2t^2\). Then \(ta\in R\), and \(\deg(ta)\le3<m\) makes reduction modulo \(P\) irrelevant. Therefore \(a_2=0\) and \(a\in R_1\), a two-dimensional space.

Likewise \(1\in R\) implies \(b=b_0+b_1t+b_2t^2\). The condition \(tb\in R\), with degree at most \(3<m\), first forces \(b_2=0\). The condition \(t^2b\in R\), now also of degree at most \(3<m\), then forces \(b_1=0\). Therefore \(b\) is constant, a one-dimensional space. Thus
\[
\dim T_{[L^{\oplus2}\twoheadrightarrow T]}Q_m^3=2+1=3.
\]
Since the image of the parameter threefold is closed and three-dimensional, the local dimension of \(Q_m^3\) at any such generic image point is at least \(3\). It cannot exceed tangent dimension \(3\). Hence its local ring is regular of dimension \(3\). The image is an irreducible component, generically smooth and reduced. This proves the main claim.

**4. Hilbert interpretation and boundary.** For transverse \(D\), the length-\(m\) subscheme \(D\times\{[u]\}\) has \(m\) distinct projections to \(C\), so is \(\pi\)-nondefective; the Hilbert-to-Quot correspondence is bijective here by Hitching, Propositions 2.9 and 2.12, and is locally an isomorphism: over disjoint support points, both functors identify with unordered tuples of points of \(C\) and their one-dimensional quotient directions. For \(m=3\), the rank restriction is automatic since every length-three quotient has at most three-dimensional target section space; the ambient rank-two Quot scheme has dimension \(6\), so the three-dimensional family is not a component. Thus the lower bound \(m\ge4\) is sharp for this component statement.

## Verification

A standalone pure-Python checker `verify.py` forms the exact linear map \((a,b)\mapsto(aR_1\bmod R,bR\bmod R)\) over \(A=\mathbb Q[t]/(t^m+1)\) and computes its kernel dimension by rational Gaussian elimination for \(3\le m\le14\). It obtains dimension \(6\) at \(m=3\) and dimension \(3\) at each \(4\le m\le14\), ending with `VERIFY_OK`. This is a finite reproducibility check of the linearization; the preceding multiplier argument proves the statement for every \(m\ge4\) and every transverse divisor without relying on the computation.

## Relationship to prior work

Hitching, *Secant loci of scrolls over curves*, arXiv:2302.04328v1, defines the generalized secant Quot and Hilbert schemes (§2.3–2.5), gives split-bundle examples (Example 2.4), develops the tangent-space criterion (§5), and proposes a Martens-type dimension bound (Conjecture 2.13). The present result specializes that framework to complete quadratic sections on smooth plane curves and proves an explicit all-degree irreducible-component and smoothness statement, including the exact tangent calculation, not stated in those inspected sections.

For \(m\in\{6,7,8\}\), the plane curve is nonhyperelliptic with \(g=(m-1)(m-2)/2\ge9\); the bundle \(E=\mathcal O_C(-2)^{\oplus2}\) has slope \(-2m\le g-2\) and very ample tautological bundle. Also \(m\le h^0(C,E^*)-2r=8\). The found dimension \(3\) exceeds the numerical value \(e-f-r=1\). **Notation caveat:** The public version of Conjecture 2.13 prints \(e\le h^0(C,E)-2r\), not \(e\le h^0(C,E^*)-2r\). Here \(h^0(C,E)=0\), so its *literal* premise is never met. The dimension comparison consequently concerns only the natural dual-section normalization; no literal refutation of that printed conjecture is claimed.

## Limitations

The claim identifies one irreducible component, not every component or the full scheme structure away from transverse divisors. Its generic smoothness assertion does not extend automatically to tangency/repeated-point boundary divisors. The field and rank-two, quadratic, plane-curve hypotheses are essential to the proof as written. The originality comparison cannot exclude an implicit or unindexed equivalent description of this special component, and the all-degree claim has not received independent audit.

## References

- George H. Hitching, *Secant loci of scrolls over curves*, arXiv:2302.04328v1 (8 February 2023), §§2.3–2.5, 5; https://arxiv.org/html/2302.04328v1 .
- Abel Castorena and George H. Hitching, *Geometry of linearly stable coherent systems over curves*, arXiv:2509.11244 (2025), abstract checked for topical comparison, https://arxiv.org/abs/2509.11244 .
