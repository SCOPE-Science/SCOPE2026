# A six-point \(5\)-rank-zero locus of Prym fourfolds in a cyclic-trigonal pencil

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\), and put
\[
C_a:\quad y^3=x^8+a x^4+1,\qquad
D_a:\quad v^3=t^4+a t^2+1,
\]
for every \(a\in U(k)\), where \(U=\mathbb A_k^1\setminus V(a^2+1)\). In each case the equation denotes its smooth projective normalization. The map \(\pi_a:C_a\to D_a\), \((x,y)\mapsto(x^2,y)\), is a connected double cover ramified at exactly four geometric points; the genera are \(7\) and \(3\), respectively. Let \(P_a=\ker(\operatorname{Nm}_{\pi_a}:\operatorname{Jac}(C_a)\to\operatorname{Jac}(D_a))^0\), an abelian fourfold.

For every geometric parameter in \(U\), the geometric \(5\)-ranks and \(a\)-numbers of these varieties are exactly
\[
\begin{array}{c|c|c}
&\text{geometric }5\text{-rank}&a\text{-number}\\\hline
\operatorname{Jac}(D_a)&2&1\\
P_a&0\text{ if }1+3a^6=0;\ 2\text{ otherwise}&2\\
\operatorname{Jac}(C_a)&2\text{ if }1+3a^6=0;\ 4\text{ otherwise}&3.
\end{array}
\]
In particular the \(5\)-rank-zero Prym locus in the coefficient-marked smooth pencil is *exactly six distinct geometric parameter points*, all lying in \(U\). Its reduced parameter equation is \(1+3a^6=0\). This assertion concerns the set-theoretic rank locus and its reduced structure, **not** any unspecified multiplicity of a Hasse divisor or an isomorphism-class count.

## Assumptions and scope

All field extensions and geometric ranks are taken over algebraically closed characteristic-\(5\) fields. The reduced automorphism \(x\mapsto ix\) (for \(i^4=1\)) preserves the marked family; the involution \(x\mapsto-x\) supplies the natural double cover. The \(a\)-number of an abelian variety is the dimension of \(\operatorname{Hom}(\alpha_5,A[5])\), equivalently the nullity of its Cartier operator. The geometric \(5\)-rank is the dimension of the stable image of Cartier (or of Hasse–Witt Frobenius).

The squarefreeness calculation below shows that \(a^2+1\ne0\) is precisely the smoothness condition for these Kummer models. The coefficients and branch marking, not their abstract isomorphism classes, are the parameters being classified.

## Proof

**1. Smoothness, genera, and the double cover.** In characteristic \(5\), for \(f_a(x)=x^8+ax^4+1\),
\[
f'_a(x)=x^3(3x^4+4a).
\]
Since \(f_a(0)=1\), a repeated root must satisfy \(x^4=2a\), and substitution gives \(f_a(x)=a^2+1\). Thus \(f_a\) is separable precisely on \(U\). The cover \(C_a\to\mathbb P^1_x\) is a tame degree-three Kummer cover branched at eight simple finite roots and infinity; Riemann–Hurwitz gives \(g(C_a)=7\). Likewise \(D_a\to\mathbb P^1_t\) is branched at four roots and infinity and has genus \(3\).

The involution \(\iota:(x,y)\mapsto(-x,y)\) has invariant function field \(k(x^2,y)\), giving \(D_a\). Over \(t=0\) there are three distinct points with \(v^3=1\), each ramified in \(x^2=t\). At the unique point of \(D_a\) over infinity, \(\operatorname{ord}_{\infty}(t)=-3\), so the quadratic extension ramifies there too. No other place is ramified. This gives four branch points and a connected ramified double cover. Consequently \(\dim P_a=7-3=4\).

**2. Complete Cartier calculation.** Write
\[
A_0=\frac{dx}{y},\quad A_1=\frac{x\,dx}{y},\qquad
B_j=\frac{x^j\,dx}{y^2}\quad(0\le j\le4).
\]
These seven differentials are regular and form a basis: at infinity \(\operatorname{ord}(x)=-3\), \(\operatorname{ord}(y)=-8\), and \(\operatorname{ord}(dx)=-4\); at finite ramification points \(\operatorname{ord}(dx/y^j)=2-j\ge0\). The same valuation computation gives the stated exhaustive index ranges.

For a polynomial \(F\), \(\mathcal C(F(x)dx)\) retains exactly the monomials with exponent congruent to \(4\bmod5\), dividing the exponent-plus-one by \(5\), and taking fifth roots of coefficients. The identities
\[
y^{-1}=y^{-10}f_a^3,\qquad y^{-2}=y^{-5}f_a
\]
therefore yield an exact Cartier matrix. The needed coefficients of \(f_a^3\), written as a polynomial in \(x^4\), are \(3a\) in degree one, \(3(1+a^2)\) in degree two, and \(1\) in degree six. The complete action is
\[
\begin{aligned}
\mathcal C(A_0)&=(3a)^{1/5}B_0+B_4,&
\mathcal C(A_1)&=[3(1+a^2)]^{1/5}B_1,\\
\mathcal C(B_0)&=a^{1/5}A_0,&
\mathcal C(B_1)&=A_1,\\
\mathcal C(B_2)&=0,&
\mathcal C(B_3)&=0,&
\mathcal C(B_4)&=A_0.
\end{aligned}
\]
All fractional powers are uniquely defined in the perfect field \(k\); Cartier is additive and fifth-root semilinear. In particular
\[
\mathcal C^2(A_0)=(1+3a^6)^{1/25}A_0,
\qquad
\mathcal C^2(A_1)=[3(1+a^2)]^{1/25}A_1.
\]
Because \(a^2+1\ne0\), the two-dimensional \(A_1,B_1\) Cartier block has stable rank two. The \(A_0,B_0,B_2,B_4\) block has stable rank two when \(1+3a^6\ne0\), and is nilpotent when that expression vanishes. The remaining differential \(B_3\) is killed. On \(U\), the full one-step Cartier rank is always four, so \(a(\operatorname{Jac}(C_a))=7-4=3\); its stable rank is four or two exactly as claimed.

**3. Prym versus quotient.** The involution acts on \(x^jdx/y^m\) by \((-1)^{j+1}\). The invariant differential subspace is \(\langle A_1,B_1,B_3\rangle\), exactly the pullback of \(H^0(D_a,\Omega^1)\). Its Cartier rank and stable rank are both two, whence \(\operatorname{Jac}(D_a)\) has \(5\)-rank two and \(a\)-number one. The anti-invariant subspace \(\langle A_0,B_0,B_2,B_4\rangle\) has one-step Cartier rank two and stable rank either zero or two as above.

The standard decomposition \(\operatorname{Jac}(D_a)\times P_a\to\operatorname{Jac}(C_a)\) is an isogeny with kernel killed by a power of two. In characteristic five it induces an isomorphism of \(5\)-divisible groups, and the invariant and anti-invariant Cartier summands yield exactly the quotient and Prym \(5\)-ranks and \(a\)-numbers displayed in the finding.

**4. Distinct exceptional points.** The polynomial \(H(a)=1+3a^6\) has degree six and derivative \(H'(a)=3a^5\), so it has six simple nonzero roots. If \(a^2+1=0\), then \(a^6=-1\) and \(H(a)=-2\ne0\) in characteristic five. Hence all six rank-zero Prym parameters correspond to smooth curves.

## Verification

Run `python3 verify_cartier.py` in the directory containing this document. The program uses exact arithmetic in \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\), independently reconstructs the complete \(7\)-by-\(7\) Cartier matrix from polynomial coefficient selection, tests its semilinear iterates, and checks the invariant and anti-invariant summands for every parameter in \(\mathbb F_{25}\). It verifies 23 smooth parameters, six exceptional parameters, the three constant \(a\)-numbers, and the two stable-rank cases. These finite tests corroborate, rather than replace, the proof for all algebraically closed fields of characteristic five.

## Relationship to prior work

Obus and Shaska (2020) classify superelliptic curves with many automorphisms; their cyclic reduced-group case includes \(y^3=x^8+1\), a high-symmetry member motivating the deformation \(x^8+ax^4+1\). They do not give the full characteristic-five Prym or Cartier stratification of this pencil. Celik, Elias, Güneş, Newton, Ozman, Pries and Thomas (2017) study low-\(p\)-rank Pryms and explicitly develop the arithmetic motivation, but their principal results and constructions concern **unramified** double covers of genus-three curves and two-dimensional Pryms. The cover studied here is branched at four points and has a four-dimensional Prym. Clingher, Malmendier and Shaska (2020) study special bielliptic Prym pencils of different genera and unramified covers, not this characteristic-five fourfold family. General Cartier coefficient procedures are standard; the concrete six-point Prym stratification and stable-rank classification are the assertion under assessment.

## Limitations

The result gives geometric \(5\)-ranks and \(a\)-numbers, **not** full Newton polygons or Ekedahl–Oort types; in particular, \(5\)-rank zero of the Prym does not by itself prove supersingularity. The parameter points are coefficient-marked and may represent fewer abstract isomorphism classes. No multiplicity for a nonordinary or Hasse divisor on the parameter line is claimed. Priority searches cannot exclude an unindexed earlier calculation. An independent mathematical audit has not been performed.

## References

- T. O. Celik, Y. Elias, B. Güneş, R. Newton, E. Ozman, R. Pries, L. Thomas, *Non-ordinary curves with a Prym variety of low \(p\)-rank*, arXiv:1708.03652 (first public version 2017-08-11), https://arxiv.org/abs/1708.03652.
- A. Obus and T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685 (first public version 2020-06-23), https://arxiv.org/abs/2006.12685.
- A. Clingher, A. Malmendier, and T. Shaska, *Geometry of Prym varieties for special bielliptic curves of genus three and five*, arXiv:2005.04839 (first public version 2020-05-11), https://arxiv.org/abs/2005.04839.
