# Sharp magic and Ehrhart positivity thresholds for twisted Cayley rectangles

## Finding
For positive integers \(a,b\), form the three-dimensional lattice polytope
\[
T_{a,b}=\operatorname{conv}\!\bigl(([0,a]\times[0,b])\times\{0\}\ \cup\ ([0,b]\times[0,a])\times\{1\}\bigr)\subset\mathbb R^3.
\]
It is smooth, has eight vertices and a regular unimodular flag triangulation. Write \(s=a+b\) and \(\delta=|a-b|\). Its Ehrhart polynomial is
\[
L_{a,b}(n)=\frac{a^2+4ab+b^2}{6}n^3+(ab+a+b)n^2+\left(s+1-\frac{\delta^2}{6}\right)n+1.
\]
Its magic-basis expansion \(L_{a,b}(n)=\sum_{i=0}^3m_i n^i(n+1)^{3-i}\) has the exact coefficients
\[
(m_0,m_1,m_2,m_3)=\left(1,\ s-2-\frac{\delta^2}{6},\ \frac{(a-1)^2+(a-1)(b-1)+(b-1)^2}{3},\ 0\right).
\]
Consequently:

* Magic positivity (all \(m_i\ge0\)) holds **if and only if** \(\delta^2\le6(s-2)\).
* Ehrhart positivity (all ordinary coefficients strictly positive) holds **if and only if** \(\delta^2<6(s+1)\).
* The Ehrhart boundary equality \(\delta^2=6(s+1)\) has no positive-integer solutions. The magic boundary \(\delta^2=6(s-2)\) consists exactly of \((a,b)=(3k^2+3k+1,3k^2-3k+1)\), up to exchange, for integers \(k\ge0\).

Among this entire family, the minimum normalized volume of a polytope that is **not magic positive** is \(97\), attained only at \(\{a,b\}=\{1,8\}\); the minimum normalized volume of a polytope that is **not Ehrhart positive** is \(141\), attained only at \(\{a,b\}=\{1,10\}\). Thus for \(b=1\) and integer \(a\ge1\), magic positivity holds precisely for \(a\le7\), ordinary Ehrhart positivity precisely for \(a\le9\), and the linear Ehrhart coefficient is negative for \(a\ge10\).

## Assumptions and scope
The two layers are axis-parallel rectangles with exchanged integer side lengths, in the stated fixed lattice \(\mathbb Z^3\). Positive integral \(a,b\) are essential. The normalized volume means six times Euclidean volume. For the magic basis the final \(m_3=0\) is allowed: magic positivity is nonnegative, not strict. No claim is made for arbitrary nonrectangular layers or Cayley sums at greater height.

## Proof
The polytope has the inequalities
\[
0\le z\le1,\qquad 0\le x\le a+(b-a)z,\qquad 0\le y\le b+(a-b)z.
\]
Thus it has eight vertices and the combinatorics of a cube. At every vertex the three primitive edge rays are two coordinate unit rays and an integer vector with last coordinate \(\pm1\). Their determinant has absolute value one. This proves smoothness. The general regular unimodular flag triangulation for these Cayley boxes is established by Ferroni [1]; smoothness also follows directly here.

At integral height \(k\) in \(nT_{a,b}\), for \(0\le k\le n\), the horizontal slice is
\[
[0,a(n-k)+bk]\times[0,b(n-k)+ak].
\]
Therefore its number of lattice points is exactly the product of the two side lengths plus one, yielding
\[
L_{a,b}(n)=\sum_{k=0}^{n}\bigl(1+a(n-k)+bk\bigr)\bigl(1+b(n-k)+ak\bigr).
\]
Expand the quadratic summand and apply \(\sum_{k=0}^n k=n(n+1)/2\), \(\sum_{k=0}^n k^2=n(n+1)(2n+1)/6\). This gives the polynomial asserted above, including \(L_{a,b}(0)=1\).

For any cubic \(L(n)=c_0+c_1n+c_2n^2+c_3n^3\), the magic-basis coefficients are uniquely \(m_0=c_0\), \(m_1=c_1-3c_0\), \(m_2=c_2-2m_1-3c_0\), \(m_3=c_3-m_0-m_1-m_2\). Substitution gives the displayed \(m_i\). Since \(a,b\ge1\), \(m_2\ge0\) as an explicit sum of three nonnegative terms; hence only \(m_1\) controls magic positivity. Since \(c_0,c_2,c_3>0\), only \(c_1=s+1-\delta^2/6\) controls Ehrhart positivity.

For the boundary equations, \(\delta^2\) divisible by six forces \(\delta=6k\), and \(s\) has the same parity as \(\delta\). The magic equality forces \(s=6k^2+2\), giving exactly the two integer values \(a=3k^2+3k+1\), \(b=3k^2-3k+1\). Both are positive for every integer \(k\ge0\). The ordinary boundary forces \(s=6k^2-1\), which is odd, contradicting the even parity of \(\delta\) and hence \(s\).

For sharp volume minima, assume \(a\ge b\), put \(t=a-b\ge0\), and observe
\[
\operatorname{Vol}_{\mathbb Z}(T_{a,b})=t^2+6bt+6b^2.
\]
Failure of magic positivity gives \(t^2>6(2b+t-2)\ge6t\), hence \(t\ge7\), so volume is at least \(49+42+6=97\), with equality only at \(t=7,b=1\). Failure of Ehrhart positivity means \(t^2\ge6(2b+t+1)\ge6(t+3)\); the last inequality forces \(t\ge9\), so volume is at least \(81+54+6=141\), with equality only at \(t=9,b=1\). The two explicit pairs attain their respective failures. For \(b=1\), solving the two inequalities directly yields the three stated phases. This proves all claims.

## Verification
Run `python3 check_twisted.py` in a Python 3 environment. The standalone standard-library checker counts integer points directly in each integer-height slice, interpolates independently from four Ehrhart values using exact rational arithmetic, transforms to magic-basis coefficients, and compares every formula and phase decision on all \(3{,}600\) ordered pairs \(1\le a,b\le60\). It also tests extra dilations and the first-volume extremizers. The observed output is `TWISTED_RECTANGULAR_CAYLEY_OK cases= 3600  min_magic_failure= (97, (1, 8))  min_ehrhart_nonpositive= (141, (1, 10))`. The general result depends on the preceding proof, not the finite checks.

## Relationship to prior work
Ferroni [1, §§2–3] introduced general Cayley sums of boxes, proved their regular unimodular flag triangulations, and gave their lattice-point formula. Liu [2, §7.3] restates the box formula and examines preservation questions for broader Cayley operations. Castillo–Liu–Nill–Paffenholz [3] demonstrated that smooth three-dimensional polytopes can have negative Ehrhart coefficients by different, chiseling-based constructions. The present classification isolates the exchange-symmetric two-rectangle specialization and gives its two exact positivity boundaries, all equality cases, and first failure volumes; the broad source formulas alone do not state these conclusions. This is a specialized phase diagram, not a claim to have originated the general Cayley-box counting formula or smooth-negative phenomenon.

## Limitations
Historical priority is provisional, particularly for descriptions of this same eight-vertex family under toric scroll or Nakajima-polytope terminology. Comparisons with inaccessible or differently indexed literature cannot establish global uniqueness. The sharp volume assertions concern only the stated twisted rectangular Cayley family, not all smooth lattice three-polytopes. No independent mathematical audit has been performed.

## References
[1] Luis Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v1 (first public 2026-09-09), especially §§2–3. https://arxiv.org/html/2609.10513v1

[2] Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338v1 (first public 2026-10-05), especially §7.3; full inspected revision v2 (2026-10-16). https://arxiv.org/html/2610.06338v2

[3] Federico Castillo, Fu Liu, Benjamin Nill, Andreas Paffenholz, *Smooth polytopes with negative Ehrhart coefficients*, arXiv:1704.05532 (2017), especially §§1–2. https://arxiv.org/abs/1704.05532
