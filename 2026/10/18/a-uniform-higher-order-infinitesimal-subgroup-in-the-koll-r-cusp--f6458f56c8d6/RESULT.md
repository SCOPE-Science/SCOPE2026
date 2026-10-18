# A uniform higher-order infinitesimal subgroup in the Kollár cusp stabilizers

## Finding

Let \(k=\overline{\mathbb F}_2\), \(q=2^n\) with an integer \(n\ge2\), and let \(C_q\subset\mathbb P^2_k\) be the plane curve
\[
F_q(X,Y,Z)=X^{q+2}+XZ^{q+1}+Y^qZ^2=0.
\]
Write \(G_q\) for the closed subgroup scheme of \(\operatorname{PGL}_{3,k}\) stabilizing this embedded curve. The new assertion is the **explicit higher-order finite subgroup scheme**
\[
K_q\cong\bigl((\alpha_q\times\alpha_q)\rtimes\mu_q\bigr)\rtimes\mu_{q+1}
\quad\hookrightarrow\quad G_q,
\]
with scheme length exactly \(q^3(q+1)\). Here the \(\mu_{q+1}\) factor acts on the two additive parameters with weights \(\lambda^2\) and \(\lambda\) and acts trivially on \(\mu_q\). The subgroup has **all** geometric points of \(G_q\), and its Lie algebra maps isomorphically onto the three-dimensional Lie algebra of \(G_q\). Thus the known first-order infinitesimal symmetries extend to a concrete, connected height-\(n\) thickening of length \(q^3\), with a full reduced-group complement. In particular \(\operatorname{length}(G_q)\ge q^3(q+1)\). Equality with the full scheme \(G_q\) is not asserted.

The exact \(q+1\) geometric points, the reduced cyclic group, and the three-dimensional Lie algebra of \(G_q\) were determined previously and are recalled with independent proofs for completeness. The existence, explicit semidirect structure, and quantitative length of \(K_q\) are the present additional claim.

## Assumptions and scope

All constructions and group schemes are over the algebraically closed field \(k\) of characteristic two. The integer \(n\ge2\) is arbitrary, with \(q=2^n\ge4\). The symbol \(\alpha_q\) denotes the kernel of the \(q\)-th power map on \(\mathbb G_a\); \(\mu_q\) denotes the \(q\)-th roots of unity group scheme. The stabilizer is the **ambient projective** automorphism group scheme for the given embedding, not the automorphism scheme of the abstract singular curve or its normalization. The length of a finite group scheme is the dimension of its coordinate algebra over \(k\).

The defining equation and the unique wild cusp are the family in Kollár's Example 3, arXiv:2603.04211, rather than newly constructed objects. The object studied here is the higher-order scheme-theoretic subgroup inside the previously studied projective stabilizer, not a new calculation of its geometric-point group or tangent dimension.

## Proof

### 1. Geometric singularity and invariant tangent

The curve is integral: in the affine patch \(Z=1\), its equation reads \(Y^q=X^{q+2}+X\). The rational function \(X^{q+2}+X\in k(X)\) has derivative \(1\), hence is not a square; in characteristic two \(Y^q-(X^{q+2}+X)\) is therefore irreducible over \(k(X)\). Its projective closure is integral. Direct differentiation yields
\[
(F_q)_X=Z^{q+1},\qquad(F_q)_Y=0,\qquad(F_q)_Z=XZ^q.
\]
The unique geometric singular point is \(P=[0:1:0]\). On the affine chart \(Y=1\), the local equation at \(P\) is \(z^2+xz^{q+1}+x^{q+2}\). As \(q\ge4\), its tangent cone is \(z^2\), with unique tangent line \(L=\{Z=0\}\). Every \(k\)-point of the projective stabilizer must fix \(P\) and preserve \(L\).

### 2. Geometric-point stabilizer (recalled)

An invertible projective matrix preserving both \(P\) and \(L\) has a representative
\[
X'=aX+bZ,\qquad Y'=cX+fY+gZ,\qquad Z'=dZ,
\]
where \(afd\ne0\). Since \(F_q\) is reduced and irreducible, preservation of the hypersurface means \(F_q(X',Y',Z')=\rho F_q(X,Y,Z)\) for some \(\rho\in k^\times\). The coefficient of \(X^{q+2}\) gives \(\rho=a^{q+2}\). The coefficient of \(X^2Z^q\) gives \(a^2b^q=0\) (distinct from \(X^qZ^2\) because \(q\ge4\)), so \(b=0\). Next the \(X^qZ^2\) and \(Z^{q+2}\) coefficients give \(c^qd^2=0\) and \(g^qd^2=0\), hence \(c=g=0\). The remaining coefficients yield
\[
ad^{q+1}=a^{q+2},\qquad f^qd^2=a^{q+2}.
\]
Putting \(\lambda=d/a\) gives \(\lambda^{q+1}=1\) and, after dividing the matrix by \(a\), \( (f/a)^q=\lambda^{-2}=\lambda^{2q}\). Injectivity of Frobenius on \(k\) gives \(f/a=\lambda^2\). Conversely all \(\operatorname{diag}(1,\lambda^2,\lambda)\), with \(\lambda^{q+1}=1\), preserve \(F_q\). Since \(q+1\) is odd, \(\mu_{q+1}\) is reduced and étale over \(k\), and it is the full reduced group scheme.

### 3. Zariski tangent space (recalled)

Take an arbitrary infinitesimal projective coordinate change \(I+\varepsilon A\), with \(\varepsilon^2=0\). The induced first-order change of \(F_q\) is
\[
\delta F_q=Z^q(Z\,\delta X+X\,\delta Z).
\]
For this to be proportional to \(F_q\), the scalar of proportionality must be zero, since \(\delta F_q\) contains no \(X^{q+2}\) monomial. If \(\delta X=aX+bY+cZ\) and \(\delta Z=dX+eY+fZ\), vanishing of \(Z\,\delta X+X\,\delta Z\) forces
\[
b=c=d=e=0,\qquad f=a.
\]
Thus \(\delta X=aX\), \(\delta Z=aZ\), with the middle row \(\delta Y\) unrestricted. Quotienting by scalar matrices removes \(a\), leaving exactly the three-dimensional space represented by
\[
\left[\begin{pmatrix}0&0&0\\r&s&t\\0&0&0\end{pmatrix}\right],\quad r,s,t\in k.
\]
This computes \(\operatorname{Lie}(G_q)\) directly, without treating finite-field counts as tangent-space evidence.

### 4. New higher-order subgroup scheme and semidirect extension

For any \(k\)-algebra \(R\), consider the matrices
\[
\begin{pmatrix}1&0&0\\a&c&b\\0&0&1\end{pmatrix}
\quad\text{with}\quad a^q=b^q=0,\quad c^q=1.
\]
They form a closed subgroup scheme \(H_q\) of \(\operatorname{PGL}_{3,k}\), with coordinate algebra
\[
k[a,b,c,c^{-1}]/(a^q,b^q,c^q-1).
\]
Indeed the change \(Y\mapsto cY+aX+bZ\) changes \(F_q\) by
\[
Z^2\bigl((c^q-1)Y^q+a^qX^q+b^qZ^q\bigr),
\]
which vanishes identically under these relations. Group multiplication is the affine-linear semidirect product of the two additive parameters by the multiplicative parameter, giving \(H_q\cong(\alpha_q\times\alpha_q)\rtimes\mu_q\). Because \(c^q-1=(c-1)^q\), this subgroup scheme is connected and its coordinate algebra has basis \(a^i b^j(c-1)^\ell\) for \(0\le i,j,\ell<q\), hence length \(q^3\). Its only geometric point is the identity.

The stabilizer \(G_q\) is of finite type as a closed subscheme of \(\operatorname{PGL}_3\) and has only \(q+1\) geometric points, so it has dimension zero and is finite over \(k\). It contains \(H_q\), so it is not reduced or smooth. In addition, the reduced diagonal subgroup \(D_q\cong\mu_{q+1}\) of Step 2 normalizes \(H_q\): conjugation by \(\operatorname{diag}(1,\lambda^2,\lambda)\) sends \((a,b,c)\) to \((\lambda^2 a,\lambda b,c)\). The intersection \(D_q\cap H_q\) is trivial as a group scheme because their lengths are relatively prime and the latter is connected. Therefore multiplication embeds the semidirect product \(K_q=H_q\rtimes D_q\) as a closed finite subgroup scheme of \(G_q\), of length exactly \(q^3(q+1)\). Its geometric points are precisely the \(q+1\) points of \(D_q\), which exhaust those of \(G_q\); its Lie algebra is that of \(H_q\), whose three independent parameters already exhaust the previously computed \(\operatorname{Lie}(G_q)\). Hence \(\operatorname{length}(G_q)\ge(q+1)q^3\). This proves the new finite subgroup scheme result.

## Verification

The self-contained Python 3 file `check_stabilizer.py` evaluates the homogeneous substitution identities over \(\mathbb F_4\) and computes the independent first-order coefficient map over \(\mathbb F_2\). For \(q=4,8,16\), exhaustive enumeration of all invertible matrices in the form forced by the unique cusp and tangent line, normalized to first coefficient \(1\), gives respectively \(1,3,1\) stabilizers, exactly \(\gcd(q+1,3)\). At each parameter the first-order linear map has rank five on nine matrix coefficients, so its kernel modulo scalars has dimension three. `CHECK_OUTPUT.txt` records these actual checks. No finite enumeration is presented as proving the statements for all \(n\); those follow from the symbolic coefficient comparison, differential calculation, and group-scheme construction above.

## Relationship to prior work

Kollár, *Planar, rational curves over* \(\mathbb F_2\) *whose only singularity is a double point* (arXiv:2603.04211, Example 3), supplies the exact curves and proves their unique wild cusp; his note treats singularities, liftings, and related surface constructions, not the projective stabilizer or its infinitesimal group-scheme structure. Borges–Korchmáros–Speziali study large linear automorphism groups of plane curves in characteristic \(p\), but the results inspected concern different invariant curves and do not yield this particular finite, non-smooth stabilizer. Brion studies finite group-scheme actions on curves and provides a general framework for infinitesimal groups; the family-specific stabilizer, its full geometric-point count, and explicit \(q^3\)-length subgroup are not consequences stated in the inspected material.

An earlier determination of the geometric projective symmetries and three-dimensional tangent space of this same embedded family is acknowledged here and is not claimed as new. Those earlier first-order facts do **not** imply the existence of a group-scheme thickening through order \(q\), let alone one with explicit semidirect multiplication and length \(q^3(q+1)\). The new result supplies such a higher-order finite subgroup, while leaving open whether it exhausts \(G_q\).

## Limitations

The theorem determines the exact length of the **constructed subgroup** \(K_q\), but neither determines the exact length of the full scheme \(G_q\) nor classifies its entire connected identity component. It concerns ambient linear projective transformations, not all automorphisms of the normalized rational curve. It does not give a deformation-theoretic or characteristic-zero lifting classification. The supplementary finite-field computations establish only the tested cases. No independent external audit has been performed.

## References

1. J. Kollár, *Planar, rational curves over* \(\mathbb F_2\) *whose only singularity is a double point*, arXiv:2603.04211, original version posted 2026-03-04; especially Example 3. https://arxiv.org/abs/2603.04211
2. H. Borges, G. Korchmáros and P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765. https://arxiv.org/abs/2202.05765
3. M. Brion, *Actions of finite group schemes on curves*, arXiv:2207.08209. https://arxiv.org/abs/2207.08209
