# A maximal K3 resolution behind the characteristic-three symmetric Burkhardt quartic

## Finding

Let \(k=\mathbb F_3\), and let \(\sigma_r\) denote the elementary symmetric polynomial of degree \(r\) in six variables. Consider the **specific integral-model reduction**
\[
B=V(\sigma_1,\sigma_4)\subset\mathbb P^5_k.
\]
Put \(P=[1:1:1:1:1:1]\), and set \(Q=B\cap\{x_0=0\}\), which is a quartic surface in the projective three-space \(\sigma_1=x_0=0\).

**Claim.** The threefold \(B\) is the projective cone with vertex \(P\) over the geometrically integral normal surface \(Q\). The surface \(Q\) has exactly fifteen geometric singularities, all rational ordinary double points. They are indexed by the unordered pairs \(\{i,j\}\subset\{0,1,2,3,4,5\}\). The reduced singular locus of \(B\) is precisely the union of the fifteen distinct lines
\[
L_{ij}=\mathbb P\bigl(k(1,1,1,1,1,1)+k(e_i-e_j)\bigr),\qquad 0\le i<j\le5,
\]
all passing through \(P\). The vertex has multiplicity four.

Let \(Y\to Q\) be the minimal resolution. Then \(Y\) is a K3 surface and the eigenvalues of geometric Frobenius on \(H^2_{\mathrm{\acute et}}(Y_{\bar k},\mathbb Q_\ell)\), for any \(\ell\ne3\), are \(+3\) with multiplicity \(21\) and \(-3\) with multiplicity \(1\). In particular \(Y\) is maximal over \(\mathbb F_9\):
\[
\#Y(\mathbb F_3)=70,\qquad \#Y(\mathbb F_9)=280=1+9^2+22\cdot9.
\]
For every integer \(m\ge1\), writing \(q=3^m\),
\[
\begin{aligned}
\#Y(\mathbb F_q)&=1+q^2+\bigl(21+(-1)^m\bigr)q,\\
\#Q(\mathbb F_q)&=1+q^2+\bigl(6+(-1)^m\bigr)q,\\
\#B(\mathbb F_q)&=1+q+q^3+\bigl(6+(-1)^m\bigr)q^2.
\end{aligned}
\]
Thus the complete zeta function of the singular threefold is
\[
Z(B/\mathbb F_3,T)=\frac{1}{(1-T)(1-3T)(1-27T)(1-9T)^6(1+9T)}.
\]

## Assumptions and scope

The base field is exactly \(\mathbb F_3\), with point formulas valid over all its finite extensions. The defining equations are the reduction of \(\sigma_1=\sigma_4=0\) with their integral coefficients; they are not the coefficientwise reduction of every characteristic-zero projectively equivalent equation of the Burkhardt threefold. In particular, the alternative five-coordinate model \(y_0(y_0^3+\sum_{i=1}^4y_i^3)+3y_1y_2y_3y_4=0\) has a reducible characteristic-three fiber \(y_0(y_0+\sum_{i=1}^4y_i)^3=0\), and must **not** be substituted for \(B\). Singular loci described above are reduced supports; no claim about the infinitesimal singular scheme at the vertex is made. The K3 statement concerns the minimal resolution of \(Q\), not a smooth model of the whole threefold.

## Proof

**1. Cone identity.** On the hyperplane \(\sigma_1=0\), characteristic-three Newton identities give
\[
\sigma_2=\sum_i x_i^2=:p_2,\qquad \sigma_4=-\sum_i x_i^4-p_2^2.
\]
For every scalar \(c\), the elementary-symmetric translation formula yields
\[
\sigma_4(x+c(1,\ldots,1))=\sigma_4(x)
\]
when \(\sigma_1(x)=0\), since the remaining terms have coefficients \(3,6,10\sigma_1,15\), all zero in characteristic three. Also \(\sigma_1(x+c(1,\ldots,1))=\sigma_1(x)\). The vector \((1,\ldots,1)\) lies in \(\sigma_1=0\) and does not lie in \(x_0=0\), so the equations do not involve its coordinate in the direct-sum decomposition. This proves the cone assertion and multiplicity four at its vertex.

**2. Complete geometric singular support.** Write \(p_2=\sum_i x_i^2\). Up to an irrelevant common minus sign, the derivatives of the restricted quartic are
\[
g_i=x_i^3+p_2x_i.
\]
The singularity condition on the hyperplane \(\sigma_1=0\) is that all six values \(g_i\) agree. Euler's identity (degree four is invertible modulo three) then puts every such point on the quartic automatically. If \(p_2=0\), the Frobenius injectivity of the algebraic closure forces all \(x_i\) equal, giving \(P\). If \(p_2\ne0\), choose \(s\) with \(s^2=-p_2\). Subtraction of derivative equations shows that every coordinate is one of \(a,a+s,a-s\) for some \(a\). Let \(n_+,n_-\) be the multiplicities of the latter two values relative to \(a\). The equations \(\sigma_1=0\) and \(p_2=\sum x_i^2\) give
\[
n_+-n_-\equiv0\pmod3,\qquad n_++n_-\equiv2\pmod3.
\]
As there are six coordinates, this forces either \((n_+,n_-)=(1,1),(1,4),(4,1)\); in every case exactly four coordinates agree and the other two differ from that value by opposite nonzero multiples of \(s\). Consequently the singular support is exactly the union of the fifteen lines \(L_{ij}\), including \(P\). All these lines and their distinct intersections with \(x_0=0\) are rational over \(\mathbb F_3\).

**3. Ordinary nodes and integrality.** Permutation symmetry reduces every point of \(\operatorname{Sing}(Q)\) to the point represented by \((0,0,0,0,1,-1)\). In the affine chart \(x_4=1\) of \(x_0=0\), put \(x_1=u,x_2=v,x_3=w\), and \(x_5=-1-u-v-w\). The quartic is
\[
uv\!w(1+x_5)+x_5(uv+uw+vw),
\]
whose quadratic part at the origin is \(-(uv+uw+vw)\). Its Hessian is
\[
\begin{pmatrix}0&2&2\\2&0&2\\2&2&0\end{pmatrix}
\]
with determinant \(1\) modulo three. Since characteristic is not two, this is an ordinary double point. The fifteen isolated singularities exhaust the geometric singularities of \(Q\). If its degree-four defining equation were reducible or nonreduced, distinct components would intersect along a curve or a repeated component would be everywhere singular. Both contradict isolated singularities. Therefore \(Q\) is geometrically integral, and normal by the hypersurface form of Serre's criterion. The cone \(B\) is likewise geometrically integral and normal: its singular locus has dimension one in a threefold, hence codimension two.

**4. Two exact finite counts.** `verify.py` enumerates each projective point exactly once via the first nonzero coordinate equal to one, implementing \(\mathbb F_9=\mathbb F_3[\omega]/(\omega^2+1)\). There are exactly \(40\) and \(820\) projective points in \(\mathbb P^3(\mathbb F_3)\) and \(\mathbb P^3(\mathbb F_9)\), respectively. Evaluation of the specified polynomial at every point gives
\[
\#Q(\mathbb F_3)=25,\qquad \#Q(\mathbb F_9)=145.
\]
The same independent projective enumeration in the ambient hyperplane gives \(\#B(\mathbb F_3)=76\) and \(\#B(\mathbb F_9)=1306\), agreeing with the cone identity \(\#B(\mathbb F_q)=1+q\#Q(\mathbb F_q)\). This is an exhaustive finite computation, not an inference from random points.

**5. K3 resolution and all extensions.** The minimal resolution \(Y\) of a normal quartic surface with only ordinary rational double points is a K3 surface: adjunction yields trivial canonical bundle and the rational double points do not alter its \(H^1(\mathcal O)\). Each node is rational over \(\mathbb F_3\); its exceptional conic is smooth and has a rational point over every finite field, hence is a copy of \(\mathbb P^1\). Replacing a node by its exceptional conic adds exactly \(q\) rational points. Thus
\[
\#Y(\mathbb F_3)=25+15\cdot3=70,\quad
\#Y(\mathbb F_9)=145+15\cdot9=280.
\]
For a K3 surface over \(\mathbb F_3\), \(H^1=H^3=0\), \(b_2=22\), and all Frobenius eigenvalues \(\alpha_j\) on \(H^2\) have complex absolute value \(3\). The second count gives \(\sum_{j=1}^{22}\alpha_j^2=198=22\cdot9\). Equality in the triangle inequality forces \(\alpha_j^2=9\) for every \(j\); the first count gives \(\sum_j\alpha_j=60\), so exactly twenty-one eigenvalues are \(+3\) and one is \(-3\). The trace formula gives all three point-count identities. Summing the resulting exponential series yields the stated zeta function. No conjectural Tate assertion or higher-extension enumeration is needed.

## Verification

Run `python3 verify.py` using only the Python standard library. The saved verifier reported `F_3: Q=25 B=76 Q_singular=15 B_singular=46`, `F_9: Q=145 B=1306 Q_singular=15 B_singular=136`, `NODE_HESSIAN_DETERMINANT_MOD3=1`, `K3_F9_MAXIMAL=280`, and `VERIFY_OK`. The proof supplies the geometric classification and Weil-bound argument independently of the finite numerical checks.

## Relationship to prior work

Beauville's 2012 work presents the \(S_6\)-symmetric quartic pencil and identifies its characteristic-zero parameter \(t=2\) with the Burkhardt quartic. Reduction of this **particular symmetric integral equation** yields the equation studied here, but Beauville's analysis is over the complex numbers and does not determine its characteristic-three fiber. Ren–Sam–Sturmfels study the classical Burkhardt model through tropical moduli in characteristic zero. Bruin–Nasserden's treatment explicitly assumes characteristic different from three and uses a five-coordinate model whose integral reduction is not isomorphic to the chosen symmetric special fiber. Dolgachev studies general fifteen-nodal quartics over the complex numbers; the generic classification does not determine this specific finite-field model's Frobenius spectrum. The new assertion is the combined exact characteristic-three geometry and the maximal \(\mathbb F_9\)-K3 zeta determination, **not** the general 15-node surface theory or the original Burkhardt equation.

## Limitations

The finding does not identify the Artin invariant, geometric Picard lattice, minimal desingularization of the threefold, or stable reduction of an arbitrary model. The reduced singular support does not give the singular scheme structure at the vertex. The exact counting program covers only the first two extensions; the all-extension conclusion additionally uses standard K3 cohomology and the Weil bounds. Earlier characteristic-three computations in unindexed literature or other integral models may exist, so historical priority remains provisional.

## References

1. A. Beauville, *Non-rationality of the \(S_6\)-symmetric quartic threefolds*, arXiv:1212.5345, first posted 2012-12-21. https://arxiv.org/abs/1212.5345
2. Q. Ren, S. V. Sam, B. Sturmfels, *Tropicalization of classical moduli spaces*, arXiv:1303.1132, first posted 2013-03-05. https://arxiv.org/html/1303.1132v2
3. N. Bruin, B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006, first posted 2017-05-25. https://arxiv.org/html/1705.09006v3
4. I. Dolgachev, *15-nodal quartic surfaces. I: quintic del Pezzo surfaces and congruences of lines in projective three-space*, arXiv:1906.12295, first posted 2019-06-28. https://arxiv.org/abs/1906.12295
5. N. Bruin, E. Filatov, *Twists of the Burkhardt Quartic Threefold*, arXiv:2207.04393, first posted 2022-07-10. https://arxiv.org/html/2207.04393v2
