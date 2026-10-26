# Seven 5-rank-zero members of a reciprocal genus-four hyperelliptic family in characteristic five

## Finding

Let \(k=\overline{\mathbf F}_5\). The smooth members of the two-parameter family
\[
H_{a,b}:\quad y^2=x^{10}+a x^8+b x^6+b x^4+a x^2+1,\qquad (a,b)\in k^2,
\]
have Jacobian \(5\)-rank in \(\{0,2,4\}\) and \(a\)-number in \(\{0,2\}\). Define
\[
\begin{aligned}
u&=a^2+2b,&h&=2a,&\ell&=2b(a+1),&v&=b^2+2ab+2a,\\
D&=uv-h\ell,&N&=u^6+h^5\ell,\\
S&=(a+b+1)(b+2a)(a^2+2a+b).
\end{aligned}
\]
All these expressions are interpreted in characteristic five. A member is smooth exactly when \(S\ne0\). On that locus its Jacobian has \(5\)-rank \(4\) if \(D\ne0\), \(5\)-rank \(2\) if \(D=0\) and \(N\ne0\), and \(5\)-rank \(0\) if \(D=N=0\). Its \(a\)-number is \(0\) for \(D\ne0\) and \(2\) for \(D=0\). In particular none is superspecial.

The entire rank-zero locus consists of exactly seven distinct coefficient-marked parameter pairs over \(k\): one \((a,b)=(3,2)\) over \(\mathbf F_5\), and the six conjugate pairs
\[
\bigl(\alpha,\beta(\alpha)\bigr),\qquad
Q(\alpha)=0,
\]
where
\[
Q(z)=z^6+z^5+z^2+z-1,\qquad
\beta(z)=-2z^5-2z^4+z^3-z^2+2z-1.
\]
Here \(Q\) is irreducible over \(\mathbf F_5\), so the six nonrational pairs have field of definition exactly \(\mathbf F_{5^6}\). Consequently, for every positive integer \(m\), exactly
\[
1+6\mathbf1_{6\mid m}
\]
smooth marked members of this family defined over \(\mathbf F_{5^m}\) have Jacobian \(5\)-rank zero.

## Assumptions and scope

The displayed family is the reciprocal-even genus-four family used in Ohashi and Kudo, arXiv:2312.16858, Section 3.1, equation (3.6). We work with the smooth projective model of the displayed affine hyperelliptic equation, in characteristic exactly five. The coefficients \(a,b\) are *marked* parameters in this fixed normalized equation; different pairs need not represent different geometric isomorphism classes. The Jacobian \(5\)-rank means the integer \(f\) characterized by \(\#J[5](k)=5^f\). The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J[5])\). Rank zero is not asserted to imply a supersingular Newton polygon.

## Proof

**Smoothness.** Set \(t=x^2\) and
\[
g(t)=t^5+at^4+bt^3+bt^2+at+1.
\]
Direct multiplication gives
\[
g(t)=(t+1)t^2\left((t+t^{-1})^2+(a-1)(t+t^{-1})+b-a-1\right)
\]
for \(t\ne0\). The quadratic factor in \(z=t+t^{-1}\) has discriminant \(a^2+2a+b\). A repeated root of \(g\) arises precisely if this discriminant vanishes, or if either \(z=2\) or \(z=-2\) is a root of the quadratic; the latter conditions are \(a+b+1=0\) and \(b+2a=0\), respectively. Since \(g(0)=1\) and \(\operatorname{char}(k)=5\ne2\), the polynomial \(g(x^2)\) is squarefree if and only if \(S\ne0\). The smooth completion then has genus four.

**Cartier matrix.** Relative to the standard basis \(x^{j-1}dx/y\) of regular differentials, use \(m_{ij}=[x^{5i-j}]f(x)^2\), where \(f(x)=g(x^2)\). An exact expansion gives
\[
M=\begin{pmatrix}
u&0&h&0\\0&v&0&\ell\\\ell&0&v&0\\0&h&0&u\end{pmatrix}.
\]
After permuting the basis to \((1,3,2,4)\), this is a direct sum \(B\oplus JBJ\), with
\[
 B=\begin{pmatrix}u&h\\\ell&v\end{pmatrix},\qquad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Here the letter \(u\) in the displayed matrix is the same quantity denoted \(u=a^2+2b\) above. Both summands have determinant \(D\) and identical ranks.

The rank of the Cartier operator is \(4\) if \(D\ne0\) and is \(2\) if \(D=0\) on the smooth locus: the block cannot vanish entirely there. Indeed, if \(D=u=0\) then \(h\ell=0\), forcing \((a,b)=(0,0)\) or \((4,2)\), and in each case \(S=0\). Thus on the smooth determinant-zero locus \(u\ne0\) and both blocks have rank one.

For a Cartier matrix, the scalar twisting must be respected: after a fixed invertible Frobenius power of coefficients, the second iterate is represented by \(M^{(5)}M\), not generally by \(MM^{(5)}\). When \(D=0\) and \(u\ne0\), write
\[
B=\begin{pmatrix}u\\\ell\end{pmatrix}\begin{pmatrix}1&h/u\end{pmatrix}.
\]
The scalar governing the second iterate of this rank-one semilinear block, multiplied by \(u^5\), is \(u^6+h^5\ell=N\). If \(N=0\), each block has square-zero Cartier iterate and stable rank zero. If \(N\ne0\), the twisted rank-one image remains nonzero under every further iterate, so each block has stable rank one. Hence the Jacobian \(5\)-ranks are precisely \(0\) and \(2\), respectively, and the Cartier ranks give the asserted \(a\)-numbers. If \(D\ne0\), the operator is invertible and the curve is ordinary.

**The exact zero-dimensional locus.** Over \(\mathbf F_5\), exact elimination yields
\[
\operatorname{Res}_b(D,N)
=2a^{18}(a+1)(a+2)(a-2)^6Q(a),
\quad Q(a)=a^6+a^5+a^2+a-1.
\]
The factors \(a\), \(a+1\), \(a+2\) and \(a-2\) correspond to the special values \(a=0,4,3,2\), respectively. The corresponding common zeros of \(D,N\) in \(b\) are, respectively, \((0,0),(4,2),(3,2),(2,1)\); the first, second and fourth are singular, and \((3,2)\) is smooth. For \(a=0\), the common zero has nontrivial intersection multiplicity but no additional support.

The polynomial \(Q\) is squarefree and irreducible of degree six over \(\mathbf F_5\). Modulo \(Q(a)\), the common-zero ideal \((D,N)\) has the unique solution \(b=\beta(a)\) given above: a lexicographic Gröbner relation is linear in \(b\) with coefficient \(a^6\); substitution proves that \(D=N=0\) modulo \((Q,b-\beta)\). Since \(Q(0)\ne0\), that relation establishes uniqueness. Finally,
\[
\gcd\bigl(Q(a),S(a,\beta(a))\bigr)=1,
\]
so all six geometric parameters are smooth. These calculations prove the complete seven-point classification and the extension-degree census.

## Verification

The standalone `verify.py` (requiring `sympy`, version constraints in `requirements.txt`) regenerates the coefficient-extraction Cartier matrix; checks the exact resultant identity, irreducibility by the finite-field criterion, the Gröbner uniqueness relation and substitutions; checks smoothness and the rank-zero locus for all \(25\) rational marked parameters over \(\mathbf F_5\); and enumerates points of \(H_{3,2}(\mathbf F_5)\), obtaining \(6\). Run `python verify.py` and expect `VERIFY_OK`. The symbolic calculations substantiate the identities used above; the argument for all algebraic extensions uses the factorization and irreducibility proofs, not empirical interpolation.

## Relationship to prior work

Ohashi and Kudo, arXiv:2312.16858v1 (2023-12-28), give this exact reciprocal genus-four family as equation (3.6) and study the superspecial problem, principally in characteristics at least seven. They do not supply the displayed complete characteristic-five \(5\)-rank-zero locus or the rank stratification in the inspected sections. Ohashi, Kudo and Harashita's related superspecial automorphism-family work does not imply these \(5\)-rank assertions: having rank zero is substantially weaker than superspeciality. Achter and Howe, arXiv:1710.10726, explain semilinear Cartier versus Hasse--Witt matrix conventions, essential to the correctly ordered rank computation. This result is a characteristic-five arithmetic refinement of the established family, not a discovery of the family itself.

## Limitations

All counts are of coefficient-marked presentations, not isomorphism classes. No claim is made that the six nonrational parameters give six nonisomorphic curves, or that rank-zero implies Newton-supersingularity. The global zeta functions and Newton polygons are not determined here. Historical arithmetic computations outside the inspected literature could contain an equivalent parameter classification; novelty is a best-knowledge conclusion, not an independence certification.

## References

- R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858v1 (first public 2023-12-28), Section 3.1, especially equation (3.6). https://arxiv.org/abs/2312.16858
- J. D. Achter and E. W. Howe, *Hasse--Witt and Cartier--Manin matrices: a warning and a request*, arXiv:1710.10726 (2017). https://arxiv.org/abs/1710.10726
- R. Ohashi, M. Kudo and S. Harashita, *Fast enumeration of superspecial hyperelliptic curves of genus 4 with automorphism group containing the Klein 4-group* (related prior superspecial-enumeration literature).
