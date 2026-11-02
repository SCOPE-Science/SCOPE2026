# The rational discriminant boundary of Kawakita's sextics in characteristic three

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\), let \(a,b\in k\), and define the plane sextic
\[
S_{a,b}:\quad X^6+Y^6+Z^6+a(X^4Y^2+Y^4Z^2+Z^4X^2)+b(X^2Y^4+Y^2Z^4+Z^2X^4)=0.
\]
Assume precisely
\[
 a+b\ne0,\qquad a-b\ne0,\qquad D(a,b):=(ab)^2-(a+b)^3=0.
\]
Then \(S_{a,b}\) is geometrically integral and has exactly **ten** geometric singular points: four unibranch ordinary cusps at \([1:\pm1:\pm1]\) and six ordinary nodes, two on each coordinate axis. Its normalization is \(\mathbf P^1_k\). More explicitly, putting \(q_0=b/a\) and choosing \(r\in k\) with \(r^2=q_0\), its nodes are
\[
 [0:\pm r:1],\quad [1:0:\pm r],\quad [\pm r:1:0].
\]
Every singularity has \(\delta=1\), so \(4+6=10\) equals the plane-sextic arithmetic genus. This boundary is nonempty over an algebraic closure of \(\mathbf F_3\).

## Assumptions and scope
The family is the characteristic-three specialization of Kawakita's published two-parameter family with integral coefficient \(c=-3(a+b+1)\); the three displayed open/boundary assumptions are all essential to this statement. The result concerns geometric singularities and the smooth projective normalization over an algebraically closed field, not a claim about intrinsic positive-characteristic sextactic points, finite-field rational-point counts, or the excluded loci \(a+b=0\) and \(a=b\). The principal classification is algebraic geometry of singular plane curves (MSC 14H20).

## Proof
**1. The cubic quotient and its unique cusp.** Let \(\pi:\mathbf P^2\to\mathbf P^2\) be \([X:Y:Z]\mapsto[X^2:Y^2:Z^2]\), and let \(U,V,W\) denote the coordinates of its target. The sextic is the inverse image of
\[
 C_{a,b}:\quad U^3+V^3+W^3+a(U^2V+V^2W+W^2U)+b(UV^2+VW^2+WU^2)=0.
\]
Set \(A=a+b\), \(B=b-a\) and use the invertible linear coordinates \(s=U-W\), \(t=U+V+W\), \(w=W\), where characteristic \(3\) is understood. Exact polynomial expansion gives
\[
 C_{a,b}=Awt^2+Bs^3+As^2t+bst^2+t^3.
\]
The right side is primitive and linear in \(w\): \(\gcd(t^2,Bs^3+As^2t+bst^2+t^3)=1\) because \(B\ne0\). Thus the cubic is geometrically irreducible. The \(w\)-derivative is \(At^2\); if a point is singular, \(t=0\), and the \(t\)-derivative then forces \(s=0\). Therefore the unique singularity is \(P=[U:V:W]=[1:1:1]\). In the chart \(w=1\), the initial form is \(At^2\) and the tangent line \(t=0\) has local intersection order \(3\), since its restriction is \(Bs^3\). It is a unibranch ordinary cusp with \(\delta_P=1\); equivalently, the irreducible cubic has arithmetic genus one and this cusp exhausts its genus defect. Its normalization \(E\) is \(\mathbf P^1_k\).

**2. The axis discriminant and its exact multiplicities.** Each coordinate axis meets the cubic in the same cyclic binary cubic. For example, on \(U=0\), in the chart \(W=1\) put \(q=V/W\) and obtain
\[
 f(q)=q^3+aq^2+bq+1,\qquad f'(q)=b-aq.
\]
If \(a=0\) or \(b=0\), then \(D=0\) forces \(a=b=0\), contradicting \(A\ne0\); thus \(ab\ne0\). The sole possible multiple root is \(q_0=b/a\), and
\[
 a^3f(q_0)=a^3+b^3-a^2b^2=-D=0.
\]
The coefficient of \((q-q_0)^2\) is \(a\ne0\), so \(q_0\) is exactly double, and the third root \(q_1=q_0-a\) is distinct and nonzero (the constant coefficient of \(f\) is one). Consequently each coordinate axis has exactly one tangency of order two and one transverse intersection with the smooth cubic; no coordinate vertex belongs to the cubic.

**3. The six axis singularities are precisely ordinary nodes.** At \((U,V,W)=(0,q_0,1)\), the derivative transverse to the axis is
\[
 \frac{\partial C}{\partial U}=a+bq_0^2=\frac{a^3+b^3}{a^2}=\frac{(a+b)^3}{a^2}\ne0.
\]
Take \(Z=1\), \(Y_0^2=q_0\), and local coordinates \(X\) and \(v=Y-Y_0\). As \(q-q_0=2Y_0v+v^2\), the quadratic tangent cone of the pulled-back sextic at \((X,v)=(0,0)\) is
\[
 \frac{(a+b)^3}{a^2}X^2+bv^2.
\]
Both coefficients are nonzero and the characteristic is not two, so this is the product of two distinct linear forms over \(k\): an ordinary node. There are two square roots \(Y_0=\pm r\) and hence two such nodes on \(X=0\). Cyclic symmetry gives the six nodes displayed in the finding. At the simple axis intersections, \(\pi^*C\) is smooth: locally the cubic equation has a nonzero derivative along the axis.

**4. Four cusp preimages and exhaustiveness.** The point \(P\) has all coordinates nonzero. The squaring map is finite étale on the coordinate torus because \(2\) is invertible, and the inverse image of \(P\) consists of exactly four distinct points \([1:\pm1:\pm1]\). Hence all four have the same ordinary-cusp local analytic germ as \(P\). Outside the coordinate axes the map is étale, so no other singularities are introduced. On the axes, Step 3 treats every intersection; the coordinate vertices are not on \(S_{a,b}\). This proves exhaustiveness.

**5. Geometric irreducibility and rational normalization.** Let \(K=k(E)\) be the function field of the normalized cubic, and consider the two squareclasses represented by \(U/W\) and \(V/W\). The unique simple intersection on \(U=0\) has valuation parity \((1,0)\), and the one on \(V=0\) has parity \((0,1)\). Consequently these classes are independent in \(K^*/K^{*2}\), so the compositum \(K(\sqrt{U/W},\sqrt{V/W})\) is a field of degree four and is the function field of a geometrically integral \(S_{a,b}\). It is a tame Klein-four Galois extension of \(K\).

On \(E\), each coordinate axis contributes precisely one simple intersection and one double tangent intersection. The simple intersections are the only ramification points of the Klein-four cover: the double contacts give even valuations, while at \(W=0\) both functions have odd poles and yield a single order-two inertia subgroup. Thus the cover has exactly three branch points, each of ramification index two and each contributing \(2\) to the degree-four Riemann--Hurwitz different. Therefore
\[
 2g-2=4(-2)+3\cdot2=-2,\qquad g=0.
\]
An independent genus check is \(p_a(S_{a,b})=(6-1)(6-2)/2=10=4\delta_{\mathrm{cusp}}+6\delta_{\mathrm{node}}\). Over \(k\), a smooth genus-zero curve is \(\mathbf P^1_k\).

**6. Nonempty parameter boundary.** Set \(a=1\) and take \(b\) to be a root of \(T(z)=z^3-z^2+1\) in \(\overline{\mathbf F}_3\). This cubic has no root in \(\mathbf F_3\) and hence is irreducible of degree three. It satisfies \(D(1,b)=-(b^3-b^2+1)=0\), while \(b\notin\{0,1,-1\}\); thus the assumptions hold.

## Verification
Run `python3 verify_boundary.py` from the directory containing the script (requires `sympy`). It checks the full characteristic-three coordinate-change identity, the axis restriction and derivative, the double-root/discriminant equality, the nonzero transverse derivative identity, and a nonempty boundary witness by exact polynomial arithmetic modulo three. The actual execution returned `KAWAKITA_CHAR3_BOUNDARY_SYMBOLIC_IDENTITIES_AND_NONEMPTY_WITNESS_PASS`. The symbolic computations support, but do not replace, the separate irreducibility, local-singularity and Riemann–Hurwitz arguments given above. No finite enumeration is asserted as a proof for all fields.

## Relationship to prior work
Kawakita introduced this two-parameter sextic and the specialization \(c=-3(a+b+1)\) in *Certain sextics with many rational points* (2017), Section 2, under the stated working restriction \(p\ge5\). Iezzi–Kawakita–Timpanella, arXiv:2306.01928 (first posted 2023-06-02), Section 4, revisit the genus-six family and its Jacobian decompositions, again for \(p\ge5\). Giulietti–Kawakita–Lia–Montanucci, arXiv:1805.06317, Remark 3.1, establish reducibility of the special *symmetric* Wiman sextic at \(p=3\), which is not the present \(a\ne b\) boundary.

The open region \(D\ne0\) in characteristic three has a known four-cusp genus-six normalization classification; it is excluded explicitly here. The characteristic-at-least-five discriminant degeneration has a different geometric singularity structure and does not imply this characteristic-three boundary theorem. The novelty claim is only the complete \(D=0\), \(A B\ne0\) boundary classification with six nodes, four cusps and rational normalization. Exhaustive historical priority is not established.

## Limitations
There is no claim about parameters with \(a+b=0\) or \(a=b\), the intrinsic moduli of sextics, the arithmetic field of definition of all singular points, or rational-point bounds. The discriminant boundary is classified only for the specified equation in characteristic three. Earlier historical literature may contain an unindexed equivalent statement. No independent audit or independent validation has been performed.

## References
1. M. Q. Kawakita, *Certain sextics with many rational points*, Advances in Mathematics of Communications **11** (2017), 289–292, DOI 10.3934/amc.2017020; freely readable full text: https://www.researchgate.net/publication/316820130_Certain_sextics_with_many_rational_points.
2. A. Iezzi, M. Q. Kawakita, M. Timpanella, *New sextics of genus 6 and 10 attaining the Serre bound*, arXiv:2306.01928 (first posted 2023-06-02), https://arxiv.org/abs/2306.01928.
3. M. Giulietti, M. Q. Kawakita, S. Lia, M. Montanucci, *An \(\mathbf F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (first posted 2018-05-15), https://arxiv.org/abs/1805.06317.
