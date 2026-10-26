# The three disjoint nonordinary strata of a genus-three Klein-involution family in characteristic three

## Finding

For every field \(k\) of characteristic \(3\), consider the smooth genus-three hyperelliptic family
\[
C_{a,b}:\quad y^2=(x^4+a x^2+1)(x^4+b x^2+1),\qquad
(a,b)\in U(k),
\]
where \(U\subset\mathbb A^2_{\mathbb F_3}\) is defined by \(a,b\notin\{1,-1\}\) and \(a\ne b\). The nonordinary locus of the relative Jacobian on \(U\) is the disjoint union of the three smooth rational curves
\[
\{a+b=1\}\cap U,\qquad\{a+b=-1\}\cap U,\qquad\{ab=1\}\cap U.
\]
Each component is isomorphic over \(\mathbb F_3\) to \(\mathbb A^1\setminus\{0,1,-1\}\). On these components the Jacobian has \(3\)-rank \(2\), \(a\)-number \(1\) and Newton slopes \(0,0,\tfrac12,\tfrac12,1,1\); on their complement it is ordinary, of \(3\)-rank \(3\) and \(a\)-number \(0\). There are no smooth members of \(3\)-rank \(0\) or \(1\).

For \(q=3^m\) and \(m\ge1\), the **ordered coordinate-parameter** counts are
\[
\#\{(a,b)\in U(\mathbb F_q):\operatorname{rank}_3 J(C_{a,b})=2\}=3(q-3),
\]
\[
\#\{(a,b)\in U(\mathbb F_q):\operatorname{rank}_3 J(C_{a,b})=3\}=(q-3)(q-5).
\]
These count ordered parameter pairs with the fixed displayed equation, **not** isomorphism classes of curves or Prym covers. Over \(\mathbb F_3\) the smooth parameter set is empty.

## Assumptions and scope

Throughout, \(k\) has characteristic \(3\), and the \(3\)-rank and \(a\)-number refer to the Jacobian of the smooth projective model. The equation has degree-eight right-hand side. The parameter scheme \(U\) excludes all repeated roots: each quartic is separable iff its parameter is different from \(\pm1\) in characteristic three, and the two quartics are coprime iff \(a\ne b\). Thus every \(C_{a,b}\) here is a smooth hyperelliptic curve of genus \(3\). No assertion is made about the moduli space quotient by automorphisms or about primes other than three.

## Proof

Write \(f(x)\) for the monic degree-eight polynomial in the displayed model and put \(u=a+b\), \(v=ab+2\). Expansion gives
\[
f(x)=x^8+u x^6+v x^4+u x^2+1.
\]
For an odd-characteristic hyperelliptic curve \(y^2=f(x)\) of genus \(3\), the Cartier–Manin matrix with respect to the differentials \(dx/y,x\,dx/y,x^2\,dx/y\) is the matrix whose \((i,j)\)-entry is the coefficient of \(x^{3i-j}\) in \(f(x)^{(3-1)/2}=f(x)\), with \(1\le i,j\le3\). In this case it is
\[
H=\begin{pmatrix}u&0&1\\0&v&0\\1&0&u\end{pmatrix}.
\]
The constant change-of-basis vectors \((1,0,1),(0,1,0),(1,0,-1)\) are defined over \(\mathbb F_3\) and diagonalize this matrix with respective eigenvalues \(u+1,v,u-1\). Since the diagonalizing basis is fixed by Frobenius, all Frobenius-twisted products preserve the three eigenspaces. Each nonzero eigenvalue contributes one to the stable rank, and each zero contributes zero. It follows that the Jacobian's \(3\)-rank equals the number of nonzero elements in \(\{u+1,v,u-1\}\). The dimension of the Cartier kernel, hence the \(a\)-number, is the number of zeros.

The two equalities \(u+1=0\) and \(u-1=0\) cannot hold simultaneously. If \(v=0\), then \(ab=1\). If in addition \(u=s\in\{1,-1\}\), the numbers \(a,b\) are roots of \(T^2-sT+1\), whose discriminant is \(s^2-4=0\) in characteristic \(3\). Thus \(a=b\), excluded on \(U\). Therefore all three exceptional loci are pairwise disjoint on \(U\); exactly one eigenvalue vanishes at each exceptional point. The \(3\)-rank and \(a\)-number statements follow. A genus-three ordinary Jacobian has Newton slopes \(0\) and \(1\), each three times; for a principally polarized abelian threefold with \(3\)-rank two, the remaining symmetric two-dimensional Newton part has both slopes \(1/2\). This proves the stated slopes.

For \(a+b=1\), the admissible values of \(a\) are precisely \(k\setminus\{0,1,-1\}\), and then \(b=1-a\); the same holds for \(a+b=-1\), using \(b=-1-a\). For \(ab=1\), admissible \(a\) likewise lie in \(k\setminus\{0,1,-1\}\), with \(b=a^{-1}\). These explicit parametrizations prove each component is a punctured affine line. For \(\mathbb F_q\) each has \(q-3\) points, hence the rank-two count is \(3(q-3)\). There are \((q-2)(q-3)\) ordered smooth parameter pairs in total, because \(a\) has \(q-2\) choices and \(b\) has \(q-3\). Subtraction yields \((q-3)(q-5)\) ordinary pairs.

As a geometric cross-check, three elliptic quotient equations obtained from the involutions \(x\mapsto-x\) and \(x\mapsto 1/x\) have Hasse invariants, up to nonzero scalars, \(v,u-1,u+1\), respectively. These are exactly the three diagonal Cartier eigenvalues. No complex Prym-moduli statement is assumed to extend automatically to characteristic three: the proof uses the explicit equations and direct Cartier calculation.

## Verification

The accompanying standalone `verify.py` implements exact arithmetic in \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), constructs the coefficient matrix from direct polynomial multiplication, and checks the ranks of Frobenius-twisted products. It also checks each elliptic quotient Hasse invariant and exhausts every ordered smooth parameter pair. Its output is `VERIFY_OK`; it gives distributions \((0,0)\), \((18,24)\), and \((72,528)\) for \(3\)-rank \((2,3)\) at \(q=3,9,27\), respectively. These finite tests corroborate rather than substitute for the proof valid for all characteristic-three fields.

## Relationship to prior work

Borówka and Shatsila (2023), especially Theorem 3.3 and Proposition 4.3, study this two-involution genus-three family through a five-point configuration and give its elliptic quotients and Prym geometry over \(\mathbb C\). They explicitly acknowledge older equations. Gutierrez, Sevilla and Shaska (2012) give genus-three hyperelliptic automorphism normal forms, and Shaska (2013) analyzes completely split Jacobians. Those complex-geometric and isogeny statements motivate the present **characteristic-three rank-locus and uniform finite-field count**, but do not themselves supply these exact nonordinary components or counts in the inspected sections. Published general \(p\)-rank-stratification results were considered for implications; existence or dimension statements on larger moduli spaces do not imply these three disjoint components and their exact counts for this marked pencil.

## Limitations

The counts are of ordered equations, not geometric isomorphism classes; swapping \(a,b\) leaves the equation invariant. The three components can meet in an ambient compactification, but they do not meet on the smooth parameter open \(U\). The characteristic-three classification is proved algebraically rather than inferred from statements over \(\mathbb C\). Prior work may contain equivalent calculations under different involution or dihedral-invariant coordinates, so external independent novelty review is warranted. No classification over other characteristics or of full endomorphism rings is claimed.

## References

- P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038v1 (first posted 2023-08-14), Theorem 3.3, Section 4, especially Propositions 4.3 and 4.5. https://arxiv.org/abs/2308.07038
- J. Gutierrez, D. Sevilla and T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938 (2012), Sections 2–4. https://arxiv.org/abs/1209.2938
- T. Shaska, *Genus 3 hyperelliptic curves with (2,4,4)-split Jacobians*, arXiv:1306.5284 (2013), Sections 1–4. https://arxiv.org/abs/1306.5284
