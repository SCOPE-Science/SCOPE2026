# The characteristic-three Igusa quartic is a cone over a zeta-maximal nodal K3 model

## Finding
Let \(I_3\subset\mathbb P^5_{\mathbb F_3}\) be the coefficientwise reduction of the integral symmetric Igusa quartic model
\[
\sum_{i=0}^{5}x_i=0,\qquad 4e_4(x_0,\ldots,x_5)-e_2(x_0,\ldots,x_5)^2=0.
\]
Here \(e_j\) is the elementary symmetric polynomial of degree \(j\). Then \(I_3\) is an integral, normal quartic threefold and is a projective cone with vertex \(E=[1:1:1:1:1:1]\) over the quartic surface \(S\subset\mathbb P^3_{\mathbb F_3}\) obtained by imposing \(x_5=0\). The geometric singularities of \(S\) are precisely fifteen \(\mathbb F_3\)-rational ordinary double points. They are indexed by partitions of six coordinate positions into three unordered pairs. Consequently, the reduced geometric singular locus of \(I_3\) consists of the fifteen lines joining \(E\) to these nodes, pairwise meeting only at \(E\); away from \(E\) their transverse type is \(A_1\). The vertex has multiplicity four.

Let \(Y\to S\) be the minimal resolution. Then \(Y\) is a K3 surface over \(\mathbb F_3\), and its zeta function is exactly
\[
Z(Y,T)=\frac{1}{(1-T)(1-9T)(1-3T)^{21}(1+3T)}.
\]
In particular, for every integer \(r\ge1\), with \(q=3^r\), the point counts are
\[
\#Y(\mathbb F_q)=1+q^2+(21+(-1)^r)q,\quad
\#S(\mathbb F_q)=1+q^2+(6+(-1)^r)q,
\]
\[
\#I_3(\mathbb F_q)=1+q\#S(\mathbb F_q).
\]
The Frobenius eigenvalues on \(H^2_{\mathrm{\acute et}}(Y_{\overline{\mathbb F}_3},\mathbb Q_\ell)\), for \(\ell\ne3\), are \(3\) with multiplicity \(21\) and \(-3\) with multiplicity one. In particular, \(Y\) is supersingular (all Newton slopes equal one).

## Assumptions and scope
The statement concerns this *specified coefficientwise integral model*, not a claim that its reduction represents a flat moduli interpretation or is the dual of the characteristic-three Segre cubic. All singularity assertions are geometric, over an algebraic closure of \(\mathbb F_3\); all point-count assertions concern the displayed \(\mathbb F_3\)-model. The scheme structure of the Jacobian locus at the cone vertex is not determined.

## Proof
Write \(p_j=\sum_{i=0}^{5}x_i^j\). Newton's identities on \(e_1=0\) give \(p_2=-2e_2\) and \(p_4=2e_2^2-4e_4\). Thus in characteristic three, the Igusa equation is identically \(F=p_2^2-p_4=0\). For simultaneous translation \(x_i\mapsto x_i+t\) of the six coordinates, \(p_2\mapsto p_2\) and \(p_4\mapsto p_4+t p_3+t^3p_1=p_4\) on \(p_1=0\), since \(p_3=p_1^3=0\). Moreover, the vector \(\mathbf1=(1,\ldots,1)\) lies in the five-dimensional linear subspace \(H=\{p_1=0\}\). Thus the quartic on \(\mathbb P(H)\) is invariant under addition in the \(\mathbf1\)-direction. A complement is the hyperplane \(x_5=0\); the equation there depends only on four projective coordinates. This proves the projective-cone assertion, with vertex \(E\).

For completeness of the geometric singular locus, the restricted gradient vanishes at \(x\in H\) precisely when the six quantities \(p_2 x_i-x_i^3\) are all equal. Put \(a=p_2\). If \(a=0\), injectivity of the Frobenius cube map over the algebraic closure forces all \(x_i\) equal, giving \(E\). If \(a\ne0\), fix \(r\) with \(r^2=a\). The roots of \(T^3-aT+b\) differ by elements of \(r\mathbb F_3\), so every critical point has \(x_i=t+r c_i\), with \(c_i\in\{0,1,-1\}\). The hyperplane equation and \(a=p_2\) imply \(\sum c_i=0\) and \(\sum c_i^2=1\) in \(\mathbb F_3\). Hence exactly two \(c_i\)'s are each of \(0,1,-1\). Conversely, each such vector does satisfy the gradient condition and the quartic equation, by Euler's identity (degree four is invertible in characteristic three). Modulo affine relabeling \(c_i\mapsto\pm c_i+b\) over \(\mathbb F_3\), the \(90\) labeled vectors give precisely \(90/6=15\) projective directions. They are the three-pair partitions of the six indices and are defined over \(\mathbb F_3\). In a complement to \(\mathbf1\), they give all fifteen singular points of \(S\); in \(I_3\), they generate fifteen distinct lines through \(E\).

To determine singularity type, the ambient Hessian of \(F\) on \(H\), at a nonvertex critical point \(x\), is the bilinear form \(a\langle v,w\rangle-\langle x,v\rangle\langle x,w\rangle\), with \(\langle v,w\rangle=\sum v_iw_i\). The radical of \(\langle\ ,\ \rangle\) on \(H=\mathbf1^\perp\) is \(k\mathbf1\). On the nondegenerate four-space \(H/k\mathbf1\), the vector \(x\) has norm \(a\ne0\); the displayed Hessian has radical precisely \(kx\). It therefore becomes nondegenerate on the three-dimensional affine tangent space to \(\mathbb P(H/k\mathbf1)\) at \([x]\). Since the characteristic is not two, every such singularity is an ordinary double point. No additional geometric singularities remain. If \(S\) were reducible or nonreduced, its hypersurface singular locus would have positive dimension, a contradiction. Thus \(S\) is geometrically integral, and the cone \(I_3\) is geometrically integral and normal (the singular locus has codimension two). The multiplicity at \(E\) is the base degree four.

The minimal resolution \(Y\) is a smooth projective K3: nodal \(A_1\) singularities are rational double points and resolve crepantly; the adjunction formula gives \(\omega_S\simeq\mathcal O_S\), and \(H^1(S,\mathcal O_S)=0\) follows from the quartic hypersurface sequence. Resolution preserves \(H^1(\mathcal O)\). Each exceptional divisor is a smooth conic over \(\mathbb F_3\), hence isomorphic to \(\mathbb P^1\) over every finite extension. It follows that \(\#Y(\mathbb F_q)=\#S(\mathbb F_q)+15q\).

Exact exhaustive finite-field enumerations in the bundled checker give \(\#S(\mathbb F_3)=25\) among all \(40\) points of \(\mathbb P^3(\mathbb F_3)\), and \(\#S(\mathbb F_9)=145\) among all \(820\) points of \(\mathbb P^3(\mathbb F_9)\). Therefore \(\#Y(\mathbb F_3)=70\) and \(\#Y(\mathbb F_9)=280\). For any K3 surface over \(\mathbb F_3\), \(H^1\) and \(H^3\) vanish and \(H^2\) has dimension \(22\); its Frobenius eigenvalues \(\alpha_j\) have complex absolute value \(3\). The Lefschetz trace formula at degrees one and two gives \(\sum_j\alpha_j=60\) and \(\sum_j\alpha_j^2=198=22\cdot9\). Equality in the triangle inequality forces all \(\alpha_j^2=9\); the first sum then determines the respective multiplicities \(21\) and \(1\) of \(3\) and \(-3\). This proves the entire zeta function and all claimed point counts. The Newton slopes are one because the Frobenius eigenvalues have three-adic valuation one, yielding supersingularity. Finally, a projective cone has one rational vertex and exactly \(q\) nonvertex points per rational point of its projective base, giving the final cone count.

## Verification
Execute `python check_igusa.py` with Python 3 and SymPy. The script exactly verifies the translation polynomial identity modulo three, enumerates all \(40\) projective base points over \(\mathbb F_3\) and all \(820\) over \(\mathbb F_9\), checks fifteen rational singular points and their rank-three Hessians, and establishes the counts \(25\) and \(145\). The all-extension statements follow **from the written argument and the Weil bounds**, not from a finite-field extrapolation. The finite-field checker uses the irreducible polynomial \(u^2+1\) to represent \(\mathbb F_9\).

## Relationship to prior work
Hulek--Sankaran (first public arXiv posting 1998-10-27, Section IV.1) review the complex Igusa quartic equation and its fifteen singular lines. Rito (first public arXiv posting 2013-10-15, Section 2) writes down the corresponding five-coordinate fifteen-nodal quartic surface in characteristic zero. Thus neither the general Igusa equation, its classical fifteen lines, nor the complex fifteen-nodal quartic model is claimed as new. The current result concerns the **characteristic-three cone degeneration of the integral six-coordinate model** and the **exact Frobenius/zeta data of the resulting nodal K3 resolution**; these do not follow from either characteristic-zero description. The standard duality with the Segre cubic is not asserted to specialize: in characteristic three the usual six-coordinate sum-of-cubes equation becomes redundant on the sum-zero hyperplane.

## Limitations
The full nonreduced Jacobian singular scheme at the cone vertex, an integral moduli interpretation in characteristic three, and the Artin invariant of the resolved K3 surface are not computed. No independent scientific audit has been performed. Literature searches do not prove global priority; an equivalent treatment in historical modular or K3 literature could exist.

## References
- K. Hulek and G. K. Sankaran, *The Geometry of Siegel Modular Varieties*, arXiv:math/9810153 (first public posting 1998-10-27), Section IV.1, especially pages 38--40. https://arxiv.org/abs/math/9810153
- C. Rito, *Cuspidal quintics and surfaces with \(p_g=0\), \(K^2=3\) and 5-torsion*, arXiv:1310.4071 (first public posting 2013-10-15), Section 2, especially page 3. https://arxiv.org/abs/1310.4071
- P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), 137--252 (Weil bounds for the cohomology of smooth proper varieties).
