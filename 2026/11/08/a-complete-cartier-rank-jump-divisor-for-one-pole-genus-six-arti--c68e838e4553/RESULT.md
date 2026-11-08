# A complete Cartier-rank jump divisor for one-pole genus-six Artin–Schreier curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). For all \(a,b,c,d\in k\), let \(C_{a,b,c,d}\) be the smooth projective curve with function field
\[
 k(x,y),\qquad y^3-y=x^7+a x^5+b x^4+c x^2+d x.
\]
This is the complete monic reduced polynomial family of degree-seven one-pole Artin–Schreier covers, with the branch point and covering coordinate marked. Each curve has genus \(6\) and Jacobian \(3\)-rank \(0\). Write \(\mathcal C\) for Cartier acting on \(H^0(C_{a,b,c,d},\Omega^1)\). The ranks of its positive iterates are exactly
\[
\big(\operatorname{rk}\mathcal C,\operatorname{rk}\mathcal C^2,\operatorname{rk}\mathcal C^3,\ldots\big)
=\begin{cases}(3,1,0,0,\ldots),&a\ne0,\\ (2,1,0,0,\ldots),&a=0.\end{cases}
\]
Consequently the Jacobian \(a\)-number is \(3\) on the nonempty Zariski-open set \(a\ne0\), and \(4\) precisely on the nonempty smooth irreducible hyperplane \(a=0\). Both strata occur for arbitrary \(b,c,d\). The vanishing condition \(a=0\) is unchanged by affine changes of the base coordinate together with Artin–Schreier reduction, so it defines a geometric condition for the marked covers rather than an artifact of a chosen translation.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(3\). The cover \(C\to\mathbb P^1\) comes from the rational function \(x\); it is branched only at \(x=\infty\) with wild lower jump \(7\). The displayed family is reduced: degree multiples of three and constants can be removed by \(y\mapsto y+h(x)\), and the coefficient of the degree-seven term is normalized to one. This is a classification of Cartier ranks **within this marked one-pole family**, not a classification of all genus-six curves or of their full Ekedahl–Oort types.

## Proof
Because \(3\nmid7\), the polynomial \(x^7+a x^5+b x^4+c x^2+d x\) is not of the form \(h^3-h\) in \(k(x)\). Hence the degree-three extension is a connected Artin–Schreier cover. Its affine model is smooth, since the derivative with respect to \(y\) is \(-1\); take the smooth projective normalization at infinity. Riemann–Hurwitz gives \(2g-2=-6+2(7+1)=10\), so \(g=6\). The Deuring–Shafarevich formula for a single branch point gives \(3\)-rank zero.

There is one point \(P_\infty\) above infinity, where \(\operatorname{ord}_{P_\infty}(x)=-3\), \(\operatorname{ord}_{P_\infty}(y)=-7\), and \(\operatorname{ord}_{P_\infty}(dx)=10\). It follows that the six differentials
\[
 \omega_0=dx,\quad \omega_1=x\,dx,\quad \omega_2=x^2\,dx,\quad
 \omega_3=x^3\,dx,\quad \eta_0=y\,dx,\quad \eta_1=xy\,dx
\]
are regular. They are linearly independent (using the independent \(1,y\) terms in the function field), and their number equals the genus, hence form a basis.

In characteristic \(3\), \(\mathcal C(x^{3m+2}\,dx)=x^m\,dx\) and \(\mathcal C(x^i\,dx)=0\) for \(i\not\equiv2\pmod3\). From \(y=y^3-f(x)\) and the \(1/3\)-linearity of Cartier,
\[
\begin{aligned}
\mathcal C(\omega_2)&=\omega_0,\\
\mathcal C(\eta_0)&=-c^{1/3}\omega_0-a^{1/3}\omega_1,\\
\mathcal C(\eta_1)&=-d^{1/3}\omega_0-b^{1/3}\omega_1-\omega_2,
\end{aligned}
\]
while \(\mathcal C(\omega_0)=\mathcal C(\omega_1)=\mathcal C(\omega_3)=0\). The image is thus spanned by \(\omega_0\), \(c^{1/3}\omega_0+a^{1/3}\omega_1\), and \(d^{1/3}\omega_0+b^{1/3}\omega_1+\omega_2\). The last vector has a nonzero \(\omega_2\)-coordinate, while the middle one contributes an additional independent \(\omega_1\)-coordinate exactly when \(a\ne0\). Therefore the first Cartier rank is \(3\) if \(a\ne0\) and \(2\) otherwise.

Every first Cartier image lies in \(\langle\omega_0,\omega_1,\omega_2\rangle\), on which Cartier maps \(\omega_2\) to \(\omega_0\) and annihilates \(\omega_0,\omega_1\). Since the image of \(\eta_1\) has nonzero \(\omega_2\)-coordinate, \(\operatorname{rk}\mathcal C^2=1\) and \(\mathcal C^3=0\), uniformly. The Jacobian \(a\)-number is \(6-\operatorname{rk}\mathcal C\).

For the coordinate-invariance assertion, translation \(x\mapsto ux+v\) with \(u\ne0\) cannot create an \(x^5\)-term from the leading \(x^7\)-term because \(\binom72=21=0\) in characteristic \(3\). Its \(x^5\)-coefficient is consequently a nonzero scalar multiple of \(a\); lower-degree terms cannot contribute. An Artin–Schreier change \(y\mapsto y+h(x)\) removing the \(x^6\) and \(x^3\) terms changes no \(x^5\)-coefficient, because \(h^3\) only contains exponents divisible by three. Hence \(a=0\) is intrinsic under the stated equivalences. As a hyperplane in affine four-space it is smooth and irreducible.

## Verification
The supplied standalone Python program `verify_cartier_g6.py` uses only the Python standard library. Independently of the displayed matrix, it reconstructs Cartier images monomial-by-monomial from \(y^3=y+f(x)\), builds the resulting six-by-six matrix for each of the \(3^4=81\) coefficient tuples over \(\mathbb F_3\), computes ranks by exact modular elimination, and checks every second and third iterate. It reports 54 tuples of initial rank \(3\) and 27 of rank \(2\); all have second-iterate rank \(1\) and third-iterate rank \(0\). The actual output is included in `verification_output.txt`. These finite-field checks are corroboration only; the symbolic proof covers every algebraically closed characteristic-three field and all its coefficients.

## Relationship to prior work
Farnell and Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank* (first public arXiv version 19 February 2012, arXiv:1202.4183), prove coefficient-independent \(a\)-numbers when the characteristic is congruent to one modulo the least common multiple of pole orders. Here \(3\not\equiv1\pmod7\); their main theorem does not imply the present coefficient-dependent jump. Farnell's 2010 dissertation treats the underlying genus-six one-pole ramification partition and the isolated monomial model \(y^3-y=x^7\), but the inspected relevant sections do not provide the full coefficient-level jump locus. Zhou's 2021 study of large \(a\)-numbers of Artin–Schreier curves gives bounds and forms for \(a=g-2\), but its cited propositions do not identify the \(a=0\) divisor in this entire family. Booher and Cais (2020), Example 7.3, give a different coefficient-dependent a-number jump for characteristic-five, degree-three covers, but not the characteristic-three, degree-seven genus-six profile here. The novelty assessed here is specifically the **complete genus-six coefficient-level rank stratification and full Cartier-image filtration**, not the general Cartier algorithm, genus calculation, p-rank formula, or monomial example. A related previously reported two-pole genus-eight rank-jump family has a different branch type, genus, and coefficient condition, and does not imply this classification.

## Limitations
No Newton polygon, individual Jacobian isomorphism class, full Ekedahl–Oort type, or unmarked-moduli stratification is claimed. The result does not establish first historical priority against all unindexed tables or uninspected specialist literature. The pointwise hyperplane classification is proved; no claim about a canonical scheme structure on the relative semilinear Cartier degeneracy locus is made. Although all \(81\) parameters over \(\mathbb F_3\) were checked independently, this finite census does not prove the theorem for other fields.

## References
1. Shawn Farnell and Rachel Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, arXiv:1202.4183v1, 2012-02-19, https://arxiv.org/pdf/1202.4183 .
2. Shawn Farnell, *Artin–Schreier Curves*, Colorado State University dissertation, 2010, https://mountainscholar.org/bitstreams/b29bf91f-4848-4aca-b33f-e67f23037554/download .
3. Jeremy Booher and Bryden Cais, *a-Numbers of Curves in Artin–Schreier Covers*, Algebra & Number Theory 14 (2020), arXiv:1807.10313, https://arxiv.org/pdf/1807.10313 .
4. Zijian Zhou, *On the existence of curves with prescribed a-number*, Arkiv för Matematik 59 (2021), 229–246, DOI:10.4310/ARKIV.2021.v59.n1.a9, https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/11959-ARKIV-2021-0059-0001-a009.pdf .
