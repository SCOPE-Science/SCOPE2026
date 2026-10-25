# A plane and a cubic scroll in the characteristic-two second osculating sextic

## Finding
Let \(k\) be algebraically closed of characteristic \(2\). The closure of the union of the second Hasse-osculating planes to the rational normal quartic \(C_4\subset\mathbb P^4_k\) is the irreducible sextic hypersurface
\[
X=V(F),\quad F=x_0^2x_3^4+x_1^4x_4^2+x_0x_2^4x_4+x_0^3x_4^3.
\]
Its **entire reduced singular locus** is a plane plus a smooth cubic scroll:
\[
\operatorname{Sing}(X)_{\mathrm{red}}=P\cup S,
\quad P=V(x_0,x_4),
\]
\[
S=V(G,K,L),\quad
G=x_2^2+x_0x_4,\quad K=x_0x_3+x_1x_2,\quad L=x_1x_4+x_2x_3.
\]
The underlying reduced intersection is the line \(P\cap S=V(x_0,x_2,x_4)\). Both components have dimension two inside the threefold \(X\), hence \(X\) fails Serre's \(R_1\) condition and is nonnormal.

## Assumptions and scope
The rational normal quartic is embedded by
\[
\nu_4:[s:t]\longmapsto[s^4:s^3t:s^2t^2:st^3:t^4].
\]
At the point with affine coordinate \(t\), the second osculating plane means the span of the zeroth, first, and second **Hasse derivatives** of the affine parametrization \((1,t,t^2,t^3,t^4)\). This definition is valid even when ordinary second derivatives vanish in characteristic two. The result describes the reduced singular *support*, not the complete nonreduced Jacobian singular scheme.

## Proof
**1. Compute the osculating image.** The three Hasse jets at \(t\) are
\[
(1,t,t^2,t^3,t^4),\quad(0,1,0,t^2,0),\quad(0,0,1,t,0).
\]
Thus a dense affine family of points in the union of osculating planes is
\[
\Phi(t,s,r)=(1,t+s,t^2+r,t^3+s t^2+r t,t^4).
\]
Writing \(A=t+s\), \(B=t^2+r\), \(C=t^3+s t^2+r t\), and \(D=t^4\), cancellation in characteristic two gives \(C=A t^2+B t+t^3\). Taking fourth powers gives \(C^4=A^4D^2+B^4D+D^3\). Hence \(F\circ\Phi=0\). The determinant of the derivative of the three coordinates \((A,B,C)\) with respect to \((s,r,t)\) is \(r\), which is nonzero generically. Therefore the image is three-dimensional. On \(x_0=1\), the defining polynomial is \(x_3^4+x_1^4x_4^2+x_2^4x_4+x_4^3\). Regard this as a polynomial in \(x_3\) over \(k(x_1,x_2,x_4)\). Its constant term has nonzero derivative \(x_2^4+x_4^2\) with respect to \(x_4\), and hence is not a square in that rational-function field; the degree-four purely inseparable polynomial is irreducible. Since \(F\) is not divisible by \(x_0\), the homogeneous \(F\) is irreducible. The three-dimensional osculating image is consequently dense in \(V(F)\).

**2. Compute all singular points.** Define \(H=x_0x_3^2+x_1^2x_4\). In characteristic two the *polynomial identity* is
\[
F=H^2+x_0x_4G^2.
\]
Consequently all five partial derivatives of \(F\) vanish except possibly
\[
F_{x_0}=x_4G^2,\qquad F_{x_4}=x_0G^2.
\]
Every point of \(P=V(x_0,x_4)\) is thus singular. Away from \(P\), at least one of \(x_0,x_4\) is nonzero, and the partials force \(G=0\); the hypersurface equation then forces \(H=0\). Two identities,
\[
K^2=x_0H+x_1^2G,\qquad x_0L=x_1G+x_2K,
\]
show that whenever \(x_0\ne0\), \(G=H=0\) is equivalent set-theoretically to \(G=K=L=0\). When \(x_0=0\), \(x_4\ne0\), the equations \(G=H=0\) force \(x_2=x_1=0\), which again forces \(G=K=L=0\). Conversely \(G=K=L=0\) implies \(H=0\) on \(x_0\ne0\) by the first identity, and also on \(x_0=0\) by inspection; therefore \(S\) is contained in the singular locus. These inclusions establish \(\operatorname{Sing}(X)_{\mathrm{red}}=P\cup S\).

**3. Identify the scroll and its intersection.** The equations \(G,K,L\) are the three \(2\times2\) minors of
\[
\begin{pmatrix}x_0&x_1&x_2\\x_2&x_3&x_4\end{pmatrix}.
\]
The explicit parametrization \([u:v:w]\mapsto[u^2:uv:uw:vw:w^2]\) is the complete linear system of plane conics through \([0:1:0]\). On the blowup of that point it defines the standard smooth cubic rational normal scroll, with degree \((2H-E)^2=3\). Directly, the open charts where one of \(x_0,x_1,x_3,x_4\) is nonzero are all affine planes: on \(x_0=1\), \((x_3,x_4)=(x_1x_2,x_2^2)\); on \(x_1=1\), \((x_2,x_4)=(x_0x_3,x_0x_3^2)\); on \(x_3=1\), \((x_2,x_0)=(x_1x_4,x_1^2x_4)\); on \(x_4=1\), \((x_0,x_1)=(x_2^2,x_2x_3)\). The four charts cover \(S\), confirming geometric smoothness. Imposing \(x_0=x_4=0\) in the scroll ideal gives \(x_2^2=0\) and terms divisible by \(x_2\); hence the **reduced** intersection is the line \(V(x_0,x_2,x_4)\). For the stronger scheme-theoretic assertion one must check the ideal \((x_0,x_4,G,K,L)=(x_0,x_4,x_2^2,x_1x_2,x_2x_3)\) on \(P\); this actually defines a possibly nonreduced intersection, not automatically the reduced line. Thus the theorem's only unconditional intersection claim is about its reduced support unless further saturation removes the thickening.

**4. Nonnormality.** The irreducible hypersurface \(X\) has dimension three; its singular components \(P\) and \(S\) each have dimension two. Since \(X\) is singular in codimension one, it fails \(R_1\) and is not normal.

## Verification
The standalone `CHECKER.py` recomputes the quartic jet substitution, sextic identity, Jacobian ideal identities, projected-Veronese scroll relations, four smooth affine charts and a complete \(\mathbb P^4(\mathbb F_2)\) rational-point sanity check. This finite check confirms thirteen rational singular points (seven on \(P\), nine on \(S\), with three on both). The proof of geometric completeness is the polynomial argument above, **not** the finite census.

## Relationship to prior work
Bernardi, Catalisano, Gimigliano and Idà (2004) develop osculating varieties of Veronese embeddings and their higher secants, working explicitly in characteristic zero. Their \(k=2,n=1,d=4\) setup motivates this object, but neither the characteristic-two sextic equation nor the two-component reduced singular locus follows from their characteristic-zero statements. Aprodu and collaborators (2018) treat characteristic-independent syzygies of *first* tangential varieties of rational normal curves; a second osculating threefold is not that tangential surface. Targeted mathematical-record and literature searches identified only structurally different scroll/plane singular-locus examples, which do not imply this theorem.

## Limitations
The theorem concerns the reduced singular support of one natural characteristic-two osculating hypersurface; it does not determine its full Jacobian scheme, normalization, conductor or singularity multiplicities. The intersection's **scheme structure** requires separate attention, and only its reduced support is established here. Equivalent results in older modular projective geometry remain possible. No independent scientific audit has been performed.

## References
1. A. Bernardi, M. V. Catalisano, A. Gimigliano, and M. Idà, *Osculating Varieties of Veronesean and their Higher Secant Varieties*, arXiv:math/0403132 (first posted 2004-03-08), https://arxiv.org/pdf/math/0403132 .
2. M. Aprodu, G. Farkas, S. Papadima, C. Raicu, and J. Weyman, *Koszul modules and Green's conjecture*, arXiv:1810.11635 (first posted 2018-10-27), https://arxiv.org/abs/1810.11635 .
