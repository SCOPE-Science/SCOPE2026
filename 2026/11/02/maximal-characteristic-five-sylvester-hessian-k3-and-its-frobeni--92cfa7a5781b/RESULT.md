# Maximal characteristic-five Sylvester-Hessian K3 and its Frobenius spectrum

## Finding
Let \(k=\mathbb F_5\), let \(H\subset\mathbb P^4_k\) be the hyperplane \(\sum_{i=0}^4 X_i=0\), and let \(Q\subset H\cong\mathbb P^3_k\) be the quartic defined by \(\sigma_4(X_0,\ldots,X_4)=0\), with \(\sigma_4\) the fourth elementary symmetric polynomial. This is the coefficientwise reduction of the Sylvester-Hessian quartic associated with the five-term diagonal Clebsch cubic.

The surface \(Q\) is geometrically integral and normal. Its singular scheme consists of exactly eleven reduced \(k\)-rational ordinary double points: the ten points with coordinate multiset \(\{1,-1,0,0,0\}\), up to scale and permutation, and the point \([1:1:1:1:1]\). Let \(\pi:Y\to Q\) be its minimal resolution. Then \(Y\) is a K3 surface and is maximal over \(\mathbb F_{25}\):
\[
\#Y(\mathbb F_{25})=1176=1+25^2+22\cdot25.
\]
The geometric Frobenius eigenvalues on \(H^2_{\mathrm{\acute et}}(Y_{\overline{k}},\mathbb Q_\ell)\), for every \(\ell\ne5\), are \(+5\) with multiplicity \(18\) and \(-5\) with multiplicity \(4\). For every integer \(m\ge1\), with \(q=5^m\),
\[
\#Y(\mathbb F_q)=1+q^2+(18+4(-1)^m)q,
\qquad
\#Q(\mathbb F_q)=1+q^2+(7+4(-1)^m)q.
\]
In particular,
\[
Z(Q/k,T)=\frac{1}{(1-T)(1-25T)(1-5T)^7(1+5T)^4}.
\]

## Assumptions and scope
The ground field is exactly \(\mathbb F_5\) and its finite extensions, and \(Q\) is the **specified integral Sylvester-Hessian model after coefficientwise reduction**, not the Hessian of a smooth characteristic-five Clebsch cubic (there is no such smooth cubic). The construction uses the ordinary projective hyperplane \(H\), with the indicated symmetric five-coordinate presentation. The resolution is the unique minimal desingularization of eleven \(A_1\) points. The asserted eigenvalues refer to geometric Frobenius acting on degree-two \(\ell\)-adic cohomology.

## Proof
**1. Hessian model.** On \(H\), substitute \(X_4=-(X_0+X_1+X_2+X_3)\). If \(G=\sum_{i=0}^4X_i^3\), the determinant of the four-variable Hessian of \(G\) equals \(1296\sigma_4\), as an exact polynomial identity over \(\mathbb Z\). Thus reducing modulo five yields precisely \(\sigma_4\), since \(1296\equiv1\pmod5\).

**2. Complete singular scheme.** Work on \(X_0=1\) and write \(u=X_1\), \(v=X_2\), \(w=X_3\), \(X_4=-(1+u+v+w)\). For \(f=\sigma_4\) on this chart, the reduced lexicographic Gröbner basis of \((f,f_u,f_v,f_w)\) over \(\mathbb F_5\), ordered \(u>v>w\), is
\[
\begin{aligned}
&u^2+u-w^2-w,&&uv+2w^2+2w,&&uw+2w^2+2w,\\
&v^2+v-w^2-w,&&vw+2w^2+2w,&&w^3-w.
\end{aligned}
\]
Its standard monomial basis is \(\{1,u,v,w,w^2\}\); the quotient has length five. The five distinct roots are \((u,v,w)=(0,0,0),(-1,0,0),(0,-1,0),(0,0,-1),(1,1,1)\), so this quotient is reduced. Any geometric projective point has some nonzero one of the five coordinates. The full \(S_5\)-symmetry moves that coordinate to \(X_0\), hence the preceding chart gives *every* geometric singular point. The orbit of \((0,0,0)\) gives the ten pair-support points; the other orbit consists only of \([1:1:1:1:1]\).

The determinants of the three-variable Hessians of \(f\) at \((0,0,0)\) and \((1,1,1)\) are respectively \(3\) and \(2\) modulo five. By symmetry, every singularity is an ordinary quadratic double point. Since a reducible or nonreduced quartic hypersurface in projective three-space has a positive-dimensional geometric singular locus, the isolated-node classification proves geometric integrality. The isolated hypersurface nodes and Serre's \(R_1\) and \(S_2\) criteria prove normality.

**3. K3 resolution and exact finite counts.** A normal geometrically integral quartic with eleven rational double points has a smooth crepant resolution with trivial canonical bundle and \(H^1(Y,\mathcal O_Y)=0\), hence a K3 surface. All eleven exceptional divisors are smooth conics over finite fields, so each has exactly \(q+1\) rational points over \(\mathbb F_q\); thus \(\#Y(\mathbb F_q)=\#Q(\mathbb F_q)+11q\).

Direct exhaustive evaluation of \(\sigma_4\) on the unique projective representatives whose first nonzero coordinate among \(X_0,\ldots,X_3\) equals \(1\) gives the chart counts \((23,12,5,1)\) over \(\mathbb F_5\) and \((803,72,25,1)\) over \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\). These sum to \(41\) and \(901\) respectively. Therefore \(\#Y(\mathbb F_5)=96\) and \(\#Y(\mathbb F_{25})=1176\).

**4. Frobenius and all extensions.** For a K3 surface, degree-two \(\ell\)-adic cohomology has dimension \(22\), odd cohomology vanishes, and every degree-two Frobenius eigenvalue has complex absolute value \(5\). The second extension count gives
\[
\sum_{j=1}^{22}\alpha_j^2=1176-1-25^2=550=22\cdot25.
\]
Equality in the triangle inequality forces each \(\alpha_j^2=25\), hence \(\alpha_j\in\{+5,-5\}\). The first extension count gives \(\sum_j\alpha_j=96-1-5^2=70\), yielding multiplicities \((18,4)\). The trace formula gives the displayed formulas for every \(m\ge1\). Subtracting eleven copies of the Tate contribution \(q\) gives the point count and zeta function of the singular quartic.

## Verification
The bundled `VERIFY.py`, with dependency specified in `requirements.txt`, verifies the integral Hessian identity, independently recomputes the lexicographic Jacobian Gröbner basis, enumerates the five affine singular points, checks the two Hessian determinants, and exhaustively counts quartic points over \(\mathbb F_5\) and over two separate quadratic field presentations \(\mathbb F_5[t]/(t^2-2)\) and \(\mathbb F_5[t]/(t^2-3)\). Both quadratic presentations yield \(901\) points and eleven rational singular points. The saved `CHECK_OUTPUT.txt` records the successful execution. All-extension formulas are algebraic consequences of the K3 trace formula, not finite numerical extrapolations.

## Relationship to prior work
Dardanelli and van Geemen describe Sylvester Hessian quartics and K3 resolutions in characteristic zero; their classification includes eleven nodes for Hessians of certain nodal cubics and determines the complex Clebsch Hessian lattice. Those geometric antecedents are not new claims here. Dolgachev and Duncan explain the failure of the smooth Clebsch cubic in characteristic five. Katsura, Kondō and Shimada study a distinguished supersingular characteristic-five K3 through different projective models. None of these treatments supplies the displayed characteristic-five \(\sigma_4\) model's complete rational singular scheme, \(\mathbb F_{25}\) maximality calculation, or its \(\mathbb F_5\) Frobenius sign decomposition in the inspected material. The new assertion is the arithmetic refinement for this *specific* model, not that nodal Hessians or maximal K3 surfaces are new concepts.

## Limitations
The computation does not determine the Artin invariant, the complete Néron–Severi lattice, a comparison isomorphism with another supersingular K3 model, or potential/stable reduction of a smooth characteristic-zero Clebsch cubic. Historical priority remains provisional: an earlier numerical zeta computation or an arithmetic description implying this exact model's Frobenius may exist outside the searched literature. The proof requires the standard Weil conjectures and K3 cohomological facts; the bundled code verifies the finite and polynomial identities but is not a replacement for these theorems.

## References
1. E. Dardanelli and B. van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322 (first posted 2004-09-18), especially §§1, 3–4. https://arxiv.org/abs/math/0409322
2. I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167, especially §12.1. https://arxiv.org/abs/1712.01167
3. T. Katsura, S. Kondō and I. Shimada, *On the supersingular K3 surface in characteristic 5 with Artin invariant 1*, arXiv:1312.0687, especially §1. https://arxiv.org/abs/1312.0687
