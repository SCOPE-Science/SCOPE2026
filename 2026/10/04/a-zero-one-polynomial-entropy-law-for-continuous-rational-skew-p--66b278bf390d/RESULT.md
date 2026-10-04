# A zero-one polynomial entropy law for continuous rational skew products
## Finding
Let \(p\in\mathbb Z\) and \(q\ge 1\) be coprime. For a continuous function \(\phi:\mathbb T\to\mathbb R\), consider
\[
f_{p/q,\phi}(x,y)=\bigl(x+p/q,\,y+\phi(x)\bigr)\quad\text{on }\mathbb T^2,
\]
and define the periodic Birkhoff sum
\[
\Phi_q(x)=\sum_{j=0}^{q-1}\phi(x+jp/q).
\]
Then
\[
h_{\mathrm{pol}}(f_{p/q,\phi})=
\begin{cases}
0,&\Phi_q\text{ is constant},\\
1,&\Phi_q\text{ is nonconstant}.
\end{cases}
\]
Thus, for this entire rational-base family, polynomial entropy is zero exactly when the rotation set is a singleton and is one otherwise. The statement requires only continuity of \(\phi\); no Lipschitz or Hölder hypothesis is needed.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\), the torus is \(\mathbb T^2\), and polynomial entropy is the standard Bowen separated/spanning growth invariant. The fraction \(p/q\) is in lowest terms with \(q\ge1\). The function \(\phi\) is real-valued and continuous, so the displayed formula induces a homeomorphism of \(\mathbb T^2\).

The key upper-bound argument is slightly more general. If \(K\) is any compact metric space and \(\psi:K\to\mathbb R\) is continuous, then the scalar twist
\[
G_\psi(u,v)=\bigl(u,\,v+\psi(u)\bigr)\quad\text{on }K\times\mathbb T
\]
has \(h_{\mathrm{pol}}(G_\psi)\le1\). Only this upper bound is used outside the torus setting.

## Proof
First compute the rational iterate. Because \(qp/q=p\in\mathbb Z\),
\[
f_{p/q,\phi}^{q}(x,y)=\bigl(x,\,y+\Phi_q(x)\bigr)=G_{\Phi_q}(x,y).
\]
Polynomial entropy is invariant under positive iterates on compact metric systems, hence
\[
h_{\mathrm{pol}}(f_{p/q,\phi})=h_{\mathrm{pol}}(G_{\Phi_q}).
\]
For completeness, this iterate invariance follows by comparing Bowen metrics at times \(0,q,2q,\ldots\) for one inequality and using uniform continuity of the finitely many maps \(f^r\), \(0\le r<q\), for the reverse inequality.

It remains to analyze \(G_\psi\) for a continuous scalar velocity \(\psi\). Fix \(0<\varepsilon<1/8\). Cover \(K\) by finitely many sets \(U_1,\ldots,U_J\) of diameter smaller than \(\varepsilon/4\), and choose a finite \(\varepsilon/4\)-net \(Y\subset\mathbb T\). Write
\[
a=\min_K\psi,\qquad b=\max_K\psi.
\]
For each horizon \(n\ge1\), partition \([a,b]\) into at most
\[
1+\frac{4n(b-a)}{\varepsilon}
\]
intervals of length smaller than \(\varepsilon/(4n)\). For every nonempty intersection of the form \(U_j\cap\psi^{-1}(I)\), choose one representative \(u_{j,I}\). Use as candidate spanning points all \((u_{j,I},y)\) with \(y\in Y\).

Given \((u,v)\in K\times\mathbb T\), choose \(j\) and \(I\) so that \(u\in U_j\cap\psi^{-1}(I)\), and choose \(y\in Y\) with \(d_{\mathbb T}(v,y)<\varepsilon/4\). For the chosen representative \(u_{j,I}\),
\[
d_K(u,u_{j,I})<\varepsilon/4,
\qquad
|\psi(u)-\psi(u_{j,I})|<\frac{\varepsilon}{4n}.
\]
Therefore, for every \(0\le k\le n\),
\[
d_{\mathbb T}\bigl(v+k\psi(u),\,y+k\psi(u_{j,I})\bigr)
\le d_{\mathbb T}(v,y)+k|\psi(u)-\psi(u_{j,I})|
<\varepsilon/2.
\]
Hence these representatives form an \((n,\varepsilon)\)-spanning set of cardinality at most
\[
J\,|Y|\left(1+\frac{4n(b-a)}{\varepsilon}\right)=O_\varepsilon(n).
\]
Thus \(h_{\mathrm{pol}}(G_\psi)\le1\). If \(\psi\) is constant, \(G_\psi\) is an isometry for the product metric, so its polynomial entropy is \(0\).

Now suppose that \(\psi:\mathbb T\to\mathbb R\) is nonconstant. A lift of \(G_\psi\) has displacement after \(n\) iterates equal to \((0,n\psi(x))\), so its rotation set is exactly
\[
\{0\}\times\psi(\mathbb T).
\]
Since \(\mathbb T\) is connected and \(\psi\) is nonconstant, this set contains more than one point. Corrêa's 2026 rotation-set theorem therefore gives \(h_{\mathrm{pol}}(G_\psi)\ge1\). Combined with the preceding spanning bound, \(h_{\mathrm{pol}}(G_\psi)=1\).

Taking \(\psi=\Phi_q\) proves the claimed dichotomy. The same iterate computation also gives
\[
\rho(\check f_{p/q,\phi})=\{p/q\}\times\frac1q\Phi_q(\mathbb T),
\]
so the entropy-zero case is exactly the singleton-rotation-set case.

## Verification
The upper bound is a direct covering argument and does not use a modulus of continuity. The only growth-dependent partition is in the scalar velocity range \([a,b]\), which contributes linearly many bins. The base cover and fiber net are fixed once \(\varepsilon\) is fixed.

Boundary checks include the following. If \(q=1\), the statement reduces to the scalar twist itself. If \(\phi\) is nonconstant but \(\Phi_q\) is constant, the entropy is still \(0\); for example, when \(p/q=1/2\), a continuous antisymmetric cocycle may satisfy \(\phi(x+1/2)=-\phi(x)\), giving \(f^2=\mathrm{id}\). Thus the correct criterion is the periodic sum \(\Phi_q\), not pointwise nonconstancy of \(\phi\).

The proof also stress-tests a regularity issue in earlier literature. A 2023 paper on polynomial torsion states, for the scalar angle-action model with \(\omega(r)=|r|^\alpha\) and \(0<\alpha<1\), that the polynomial entropy is \(1/\alpha\). The spanning construction above applies to that displayed compact scalar model and gives the universal bound \(h_{\mathrm{pol}}\le1\), so the two statements are incompatible when \(\alpha<1\). The 2023 paper omits the lower-bound proof for that proposition. No conclusion about its broader torsion theory is needed here.

## Relationship to prior work
Corrêa's 2026 paper introduces exactly the skew products \(f_{\alpha,\phi}\). For rational \(\alpha=p/q\), it computes the \(q\)-th iterate and the rotation set, then proves the lower bound \(h_{\mathrm{pol}}(f_{p/q,\phi})\ge1\) when \(\Phi_q\) is nonconstant. Its Proposition 5.1 proves \(h_{\mathrm{pol}}(f_{0,\phi})\le1\) under the additional assumption that \(\phi\) is Lipschitz. The present argument removes that regularity assumption by partitioning the bounded velocity range rather than the base at a scale controlled by a Lipschitz constant. Iteration then yields the exact rational-base classification.

Correa and Pujals study cylindrical cascades with irrational base rotation and highly nonuniform growth, so their construction does not imply the rational-periodic classification above. Grycan-Gérard and Marco study weak angle-action models and obtain Hölder-dependent upper bounds; their displayed scalar example with entropy \(1/\alpha\) conflicts with the universal scalar-velocity cover proved here rather than covering it.

## Limitations
The theorem is restricted to scalar circle fibers and rational base rotation. It does not classify irrational-base cylindrical cascades, where Birkhoff sums need not collapse to one periodic velocity function. For higher-dimensional torus fibers, the same velocity-range argument gives a dimension-dependent polynomial upper bound rather than the stated zero-one law.

The literature search was broad but cannot prove absolute novelty. The 2023 conflicting proposition is recorded explicitly because it is scientifically material; the present package proves only the stated rational skew-product theorem and the scalar-twist upper bound needed for it, and does not attempt a general repair of polynomial torsion results.

## References
1. H. Corrêa, “Polynomial entropy and rotation sets,” *Archiv der Mathematik* (2026), DOI: 10.1007/s00013-026-02286-3. First verified public date: 2026-09-12.
2. F. Grycan-Gérard and J.-P. Marco, “Polynomial Entropy and Polynomial Torsion for Fibered Systems,” *Regular and Chaotic Dynamics* 28 (2023), 613–627, DOI: 10.1134/S156035472304007X.
3. J. Correa and E. R. Pujals, “Orders of Growth and Generalized Entropy,” *Journal of the Institute of Mathematics of Jussieu* 22 (2023), 1581–1613; arXiv:2003.01257.
