# Complete Cartier strata for a genus-four cyclic trigonal family in characteristic eleven

## Finding

Let \(k\) be an algebraically closed field of characteristic \(11\). For \(a,b\in k\), define \(C_{a,b}\) to be the smooth projective model of \(y^3=x^5+ax+b\). Write \(\Delta=b^4+3a^5\); the curve is smooth of genus four exactly when \(\Delta\ne0\). On this smooth locus the Jacobian \(11\)-rank \(f_{11}\) and \(a\)-number have the following complete classification:

\[
(f_{11},a(C_{a,b}))=\begin{cases}
(0,4),&b=0,\\
(0,2),&b\ne0\text{ and }b^4=9a^5,\\
(2,2),&b\ne0\text{ and }b^4\ne9a^5.
\end{cases}
\]

In particular, the family has no smooth member of \(11\)-rank one, three or four, and contains two distinct \(11\)-rank-zero strata distinguished by their \(a\)-number. Over \(\mathbf F_{11}\), among the \(110\) smooth ordered coefficient pairs, these three strata contain respectively \(10\), \(10\), and \(90\) pairs.

## Assumptions and scope

All curve-theoretic rank assertions apply over algebraically closed \(k\) of characteristic \(11\), without restricting coefficients to the prime field. \(f_{11}\) is the rank of the stable Frobenius action on \(H^1(C,\mathcal O_C)\), equivalently the stable Cartier rank on regular differentials. The \(a\)-number is the dimension of the kernel of the Cartier operator. The finite coefficient census refers to the ordered pairs in \(\mathbf F_{11}^2\), not to isomorphism classes. The cyclic trigonal map is induced by \(x\), and has degree three.

## Proof

**Smoothness and genus.** The derivative of \(f(x)=x^5+ax+b\) is \(5x^4+a\). The resultant/discriminant calculation gives \(\operatorname{disc}_x(f)=256a^5+3125b^4\equiv3a^5+b^4\pmod{11}\). Thus \(f\) is squarefree exactly when \(\Delta\ne0\). Since \(\gcd(3,5)=1\), the Kummer map \(x:C\to\mathbf P^1\) has degree three, totally ramified at the five roots and at infinity; Riemann–Hurwitz gives \(2g-2=-6+6\cdot2=6\), hence \(g=4\).

**Regular differentials.** At infinity, \(\operatorname{ord}_\infty(x)=-3\), \(\operatorname{ord}_\infty(y)=-5\), \(\operatorname{ord}_\infty(dx)=-4\). The following are regular at infinity and everywhere else, and form a basis by dimension four:
\[\omega_0=dx/y,\quad\omega_1=dx/y^2,\quad\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2.\]

**Cartier matrix.** Write \(f=x^5+ax+b\). Because \(y^{21}=f^7\) and \(y^9=f^3\), the Cartier identities \(\mathcal C(g^{11}\eta)=g\mathcal C(\eta)\) give
\[\mathcal C(dx/y)=y^{-2}\mathcal C(f^7dx),\qquad \mathcal C(x^i dx/y^2)=y^{-1}\mathcal C(x^if^3dx).\]
For a polynomial \(H(x)\), the Cartier operator \(\mathcal C(H\,dx)\) selects terms with exponent \(10\) modulo \(11\); the coefficient of \(x^{11j+10}\) contributes its \(11\)-th root times \(x^j dx\). In \(f^7\), the relevant coefficients of \(x^{10}\), \(x^{21}\), \(x^{32}\) are respectively
\[P=10b^5+9a^5b=b(9a^5-b^4),\quad R=6ab^2,\quad0.\]
In \(f^3\), the coefficients of \(x^{10},x^9,x^8\) are \(3b,0,0\). Therefore in the displayed differential basis
\[\mathcal C(\omega_0)=P^{1/11}\omega_1+R^{1/11}\omega_2,\qquad \mathcal C(\omega_1)=(3b)^{1/11}\omega_0,\qquad \mathcal C(\omega_2)=\mathcal C(\omega_3)=0.\]
Because the base field is perfect, taking the indicated roots does not change which coefficients vanish. The Cartier matrix has rank zero exactly when \(b=0\): if \(b\ne0\), its images of \(\omega_0\) and \(\omega_1\) are independent (since \(P\) and \(R\) cannot simultaneously vanish: \(R=0\Rightarrow a=0\Rightarrow P=-b^5\ne0\)). Thus the \(a\)-number is four or two as claimed.

**Stable Cartier rank.** If \(b\ne0\) and \(P\ne0\), Cartier interchanges the two independent directions spanned by \(\omega_0\) and \(\omega_1\) modulo the nilpotent direction \(\omega_2\). The stable semilinear image has dimension two. If \(P=0\), then \(\omega_1\mapsto\omega_0\mapsto\omega_2\mapsto0\) and all of Cartier is nilpotent, so the stable rank is zero. If \(b=0\), Cartier vanishes. These stable ranks are exactly the Jacobian \(11\)-ranks. For \(b\ne0\), the equation \(P=0\) is \(b^4=9a^5\). On this locus \(a\ne0\) and \(\Delta=(9+3)a^5=a^5\ne0\); hence the exceptional rank-zero stratum is genuinely smooth, not a discriminant artifact.

**Prime-field census.** For \(b=0\), the ten nonzero choices of \(a\) give smooth curves of the first type. For \(a,b\ne0\), the relation \(b^4=9a^5\) has precisely ten ordered solutions over \(\mathbf F_{11}\): because fifth powering is bijective on \(\mathbf F_{11}^{\times}\), every \(b\ne0\) has exactly one corresponding \(a\), and that pair is smooth. The smooth-locus total is \(110\): for each \(b\ne0\) there is one nonsmooth \(a\) satisfying \(b^4=-3a^5\), while \((a,b)=(0,0)\) is the sole nonsmooth pair with \(b=0\). The remaining \(90\) smooth pairs have \(11\)-rank two.

## Verification

The standalone exact programs `verify_cartier.py` and `verify_independent.py` independently construct the Cartier matrices: the first uses multinomial expansion and modular row reduction, while the second uses direct polynomial convolution and nonzero-minor rank tests. Both exhaust all \(121\) prime-field coefficient pairs and reproduce the three smooth-stratum counts. The second program also verifies smoothness by polynomial gcd and counts rational points on three example curves over \(\mathbf F_{121}\), obtaining \(210\), \(144\), and \(162\), respectively, for parameters \((a,b)=(1,0),(1,5),(1,1)\). These finite checks corroborate but do not replace the symbolic proof for every algebraically closed coefficient field.

## Relationship to prior work

Kudo and Harashita (2017) enumerate nonhyperelliptic superspecial genus-four curves over small prime fields, including characteristic eleven. Kudo (2018) gives a different explicit genus-four superspecial family. Kudo, Harashita and Senda (2019) prove existence of supersingular genus-four curves using Howe curves. The present result does not assert that the existence of superspecial genus-four curves, or the individual special case \(b=0\), is new; it classifies the complete stable Cartier ranks together with \(a\)-numbers and defines both exceptional strata in this particular cyclic trigonal family. The usual general superelliptic Cartier coefficient-selection identity is used as a tool, not claimed as new.

## Limitations

The theorem concerns this two-parameter family only, not all genus-four trigonal curves. The \(11\)-rank-zero, \(a\)-number-two stratum is not thereby proved supersingular. Prime-field parameter counts are not geometric isomorphism-class counts. Superspeciality of the \(b=0\) stratum follows from Cartier vanishing but is not claimed as a novel existence theorem. A prior unindexed specialization or table could independently give these coefficient conditions; priority requires external checking.

## References

1. M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields* (2017), arXiv:1702.05313.
2. M. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4* (2018), arXiv:1804.09063.
3. M. Kudo, S. Harashita and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic* (2019), arXiv:1903.08095.
