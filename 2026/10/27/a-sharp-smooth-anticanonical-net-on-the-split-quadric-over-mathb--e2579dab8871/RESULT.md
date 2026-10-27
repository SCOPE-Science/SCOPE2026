# A sharp smooth anticanonical net on the split quadric over \(\mathbf F_3\)

## Finding
Let \(S=\mathbf P^1_{\mathbf F_3}\times\mathbf P^1_{\mathbf F_3}\). There exists a three-dimensional vector space \(W\subset H^0(S,\mathcal O(2,2))\) with **all thirteen** rational projective members geometrically smooth; no vector space of dimension four can have this property. Thus the maximum possible vector-space dimension is exactly three (projective dimension two). Every maximal all-smooth system has no rational base point.

## Assumptions and scope
Coordinates are \(([s:t],[u:v])\), with \(s,t\) homogeneous coordinates on the first ruling and \(u,v\) on the second. Everything is defined over \(\mathbf F_3\). Smoothness always means smoothness after extension to the algebraic closure. The assertion concerns all nonzero \(\mathbf F_3\)-linear combinations, up to \(\mathbf F_3^*\); it does not assert that every geometric member of the net is smooth.

The explicit generators of \(W\) are
\[
\begin{aligned}
F&=s^2u^2+stv^2+t^2u^2,\\
G&=s^2u^2+s^2uv+2s^2v^2+t^2uv,\\
H&=s^2u^2+2s^2uv+2stu^2+2stuv+t^2v^2.
\end{aligned}
\]
The displayed coefficients are elements of \(\mathbf F_3\); an integer \(2\) means the residue class of \(-1\).

## Proof
**Upper bound.** Fix any rational point \(P\in S(\mathbf F_3)\). For any linear subspace \(U\subset H^0(S,\mathcal O(2,2))\), the first-jet evaluation map \(U\to \mathcal O(2,2)\otimes \mathcal O_{S,P}/\mathfrak m_P^2\) has a three-dimensional target over \(\mathbf F_3\) (one value and two partial derivatives). If \(\dim U\ge4\), a nonzero section lies in its kernel, so the associated divisor is singular at \(P\) (or the zero section of the ambient bundle, which is also disallowed). Hence every all-smooth \(U\) has dimension at most three.

**Attainment.** Write the coefficient vector of a bidegree-\((2,2)\) form in the order \(s^{2-i}t^i u^{2-j}v^j\) with \(0\le i,j\le2\), ordered lexicographically by \((i,j)\). The three displayed generators have vectors

```
F = 1 0 0 0 0 1 1 0 0
G = 1 1 2 0 0 0 0 1 0
H = 1 2 0 2 2 0 0 0 1
```

These are independent: their coefficients at positions \((i,j)=(2,0),(2,1),(2,2)\) respectively form a nonsingular matrix. (Equivalently, the exhaustive check in the accompanying script finds exactly thirteen distinct projective combinations.)

For each normalized \((a,b,c)\in\mathbf P^2(\mathbf F_3)\), put \(T=aF+bG+cH\) and write \(T=A(s,t)u^2+B(s,t)uv+C(s,t)v^2\). Its binary-quartic discriminant is \(\Delta_T=B^2-AC\), since \(4=1\) in \(\mathbf F_3\). The accompanying exact certificate records all thirteen five-term discriminant coefficient vectors. For each, the dehomogenized polynomial has degree at least three and is coprime to its derivative. Consequently each discriminant has four distinct geometric roots in \(\mathbf P^1\). The three quadratic coefficients cannot vanish simultaneously at any geometric first-ruling point (that would force a double root of \(\Delta_T\)); the corresponding degree-two family is therefore finite, and a reduced discriminant proves that the double cover is geometrically smooth. As a separate direct check, the Jacobian ideal \((T,\partial T/\partial x,\partial T/\partial y)\) is the unit ideal on **each of four affine charts** for each of the thirteen members. These 52 chart tests are exact Gröbner-basis computations modulo three, not tests of a bounded list of extension-field points.

The divisor of a smooth positive-bidegree section is geometrically connected (by the cohomology sequence and \(H^1(S_{\overline{\mathbf F}_3},\mathcal O(-2,-2))=0\)); smooth and connected implies geometrically integral. Its genus by adjunction is \((2-1)(2-1)=1\). Thus the exhibited space is an all-smooth genus-one net and attains the bound.

**Base-point corollary.** If a three-dimensional all-smooth \(U\) had a rational base point \(P\), its first-jet map at \(P\) would have zero value coordinate and image dimension at most two, forcing a nonzero member singular at \(P\). Hence no such rational base point exists.

## Verification
Execute `python verify.py` with Python 3 and SymPy. It enumerates all thirteen normalized combinations, checks linear independence, tests a squarefree discriminant for each, and directly verifies all 52 affine-chart Jacobian unit ideals. The exact discriminant coefficient vectors and success output appear in `verify.txt`. Both the binary-quartic branch test and the independent direct chart tests agree.

## Relationship to prior work
Asgarli–Ghioca (2022) formulate the all-smooth rational-member linear-system problem for projective hypersurfaces and provide small-field nets of plane conics. Asgarli–Ghioca–Reichstein (2022) establish sharp existence results for linear systems of smooth hypersurfaces in projective spaces over finitely generated fields. The local first-jet dimension obstruction used here is the same standard principle; **the upper-bound technique by itself is not claimed as new**. Neither inspected work provides the displayed thirteen-member genus-one anticanonical net on the split quadric, and the hypersurface statements do not automatically imply smooth intersections with a fixed quadric. Earlier enumerations of all-smooth biquadratic **pencils** on the split quadric over \(\mathbf F_3\) do not imply the additional existence of a three-dimensional extension with all thirteen members smooth.

## Limitations
No enumeration or uniqueness classification of all smooth nets is claimed. The result concerns only \(\mathbf F_3\)-rational combinations, not smoothness of all geometric linear combinations. A comprehensive catalogue of unindexed computational examples was not accessible; the existence example's absolute publication priority remains subject to specialist comparison. Independent external mathematical review has not been performed.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (2022), arXiv:2203.07169, https://arxiv.org/abs/2203.07169.
2. S. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields* (2022), arXiv:2207.00918, https://arxiv.org/abs/2207.00918.
