# Sharp three-sum covering of the split modular hyperbola over finite fields

## Finding
Let \(q\ge13\) be a prime power and put
\[
H_q=\{(t,t^{-1}):t\in\mathbb F_q^\times\}\subseteq\mathbb F_q^2.
\]
Then the **exact** threefold Minkowski sum is
\[
3H_q=H_q+H_q+H_q=
\begin{cases}
\mathbb F_q^2,&3\mid q\text{ or }q\equiv1\pmod3,\\
\mathbb F_q^2\setminus\{(0,0)\},&q\equiv2\pmod3.
\end{cases}
\]
The universal lower bound \(q\ge13\) is sharp among prime-power field sizes: over \(\mathbb F_{11}\), \((1,6)\notin3H_{11}\). In particular the zero vector is the sole possible obstruction at every field size at least thirteen, and that obstruction is controlled exactly by third roots of unity.

## Assumptions and scope
All sums are coordinatewise in \(\mathbb F_q^2\); summands may repeat, and \(\mathbb F_q\) may have any characteristic. A point \((s,v)\) belongs to \(3H_q\) exactly when some \(x,y,z\in\mathbb F_q^\times\) satisfy
\[
x+y+z=s,\qquad x^{-1}+y^{-1}+z^{-1}=v.
\]
Equivalently, with \(e_2=xy+xz+yz\) and \(e_3=xyz\), these equations are \(e_1=s\), \(e_2=ve_3\), and \(e_3\ne0\). No assertion is made for the complete classification of the smaller fields.

## Proof
**1. Targets on a coordinate axis.** If \(s=0\) and \(v\ne0\), choose \(t\in\mathbb F_q\) away from the at most four roots of \(t(t+1)(t^2+t+1)\). Set
\[
\lambda=\frac{t^2+t+1}{v t(t+1)},\quad
(x,y,z)=(\lambda,t\lambda,-(1+t)\lambda).
\]
All coordinates are nonzero. Their sum is zero, and \(e_2=-\lambda^2(t^2+t+1)=v e_3\), so their inverse sum is \(v\). If \(s\ne0\) and \(v=0\), choose the same kind of \(t\) and set
\[
\lambda=\frac{s(1+t)}{t^2+t+1},\quad
(x,y,z)=(\lambda,t\lambda,s-(1+t)\lambda).
\]
Now \(z=-st/(t^2+t+1)\ne0\), \(e_1=s\), and \(e_2=0\). Such \(t\) always exist for \(q\ge13\).

**2. Targets with both coordinates nonzero.** The linear automorphism \((u,v)\mapsto(au,a^{-1}v)\) preserves \(H_q\). By taking \(a=s^{-1}\), it suffices to realize \((1,w)\), where \(w=sv\in\mathbb F_q^\times\). Consider the plane cubic
\[
C_w:\quad x+y+z=1,\qquad xy+xz+yz=wxyz.
\]
Writing \(z=1-x-y\), the projective closure in coordinates \([X:Y:T]\) is
\[
T\bigl[XY+(X+Y)(T-X-Y)\bigr]
-wXY(T-X-Y)=0.\tag{1}
\]
Exactly three rational points lie at infinity, namely \([1:0:0]\), \([0:1:0]\), \([1:-1:0]\), and all three are nonsingular for \(w\ne0\). Affine points having a zero coordinate are exactly the permutations of \((1,0,0)\), hence there are exactly **six** forbidden rational projective points. All remaining rational points give the required three nonzero summands.

We next check smoothness. Along the affine plane \(x+y+z=1\), differences of the partial derivatives of \(e_2-we_3\) are
\[
(y-x)(1-wz),\quad(z-y)(1-wx),\quad(x-z)(1-wy).
\]
If all three coordinates are distinct, vanishing would force \(wx=wy=wz=1\), a contradiction. If exactly two are equal, say \(x=y\ne z\), vanishing forces \(wx=1\); using \(z=1-2x\) in \(e_2=we_3\) then forces \(w=1\). If all are equal, \(3x=1\), and \(e_2=we_3\) forces \(w=9\) (this alternative does not occur in characteristic three). Thus \(C_w\) is a smooth plane cubic, hence a genus-one curve, whenever \(w\notin\{1,9\}\). The Hasse bound yields
\[
\#C_w(\mathbb F_q)\ge q+1-2\sqrt q>6\qquad(q\ge13).
\]
Therefore at least one rational point is not among the six forbidden points, proving \((1,w)\in3H_q\).

The singular parameters are represented directly: for \(w=1\) choose \((x,y,z)=(1,t,-t)\) with any \(t\ne0\). For \(w=9\), provided the characteristic is not three, choose \(x=y=z=1/3\). If the characteristic is three, \(9=0\) and is excluded by \(w\ne0\). These cases include the possibility \(1=9\) in characteristic two. Hence every target with \(s,v\ne0\) is attained.

**3. The zero vector.** The equation \(x+y+z=x^{-1}+y^{-1}+z^{-1}=0\), with nonzero variables, is equivalent to \(e_1=e_2=0\). In characteristic three, \(x=y=z=1\) works. Outside characteristic three, \(x,y,z\) are precisely the three roots of \(T^3-e_3\), with \(e_3\ne0\). Since this polynomial is separable, all three roots lie in \(\mathbb F_q\) if and only if \(\mathbb F_q\) contains all third roots of unity, which is equivalent to \(q\equiv1\pmod3\). Thus the displayed threefold-sum classification holds.

**4. Sharp lower threshold.** Over \(\mathbb F_{11}\), direct substitution into the two-summand equation shows that the target \((1,6)\) is missing. For a fully reproducible certificate, test each \(x\in\{1,\ldots,10\}\) and let \(A=1-x\), \(B=6-x^{-1}\). If \(A=B=0\) then any nonzero pair \((y,-y)\) works; if exactly one of \(A,B\) is zero, there is no pair; otherwise \(y,z\) must be roots of \(T^2-AT+A/B\) with both roots nonzero. In each of the ten cases the latter polynomial has no two roots in \(\mathbb F_{11}\); an independent exhaustive verifier supplies the finite certificate. As eleven is the largest prime-power size below thirteen, the universal threshold is sharp. \(\square\)

## Verification
The standalone program `artifacts/verify_hyperbola.py` builds finite fields independently, enumerates all graph-point sums, tests the exact formula for selected prime and extension fields, and prints the explicit missing target at \(q=11\). Enumeration is not used in the proof for the infinite family \(q\ge13\), which follows from the smooth cubic and Hasse bound. In particular, the six excluded points, their smoothness, and the two singular values are verified algebraically above.

## Relationship to prior work
The archival study of Bower, Evans, Luo and Miller (2012, arXiv:1212.2930) studies **scalar coordinate sumsets** \(\{x_1+\cdots+x_d:x_1\cdots x_d=a\}\), and proves scalar coverage for \(d\ge3\) when prime factors exceed seven. That statement does not imply simultaneous coverage of a specified scalar sum **and reciprocal sum**, which is the two-coordinate problem here. Khan, Magner, Senger and Winterhof (2013, arXiv:1304.6943) study ordinary lines and radial statistics on modular hyperbolas, not this threefold vector sum. A related result about the **nonsplit** norm-one torus inside \(\mathbb F_{q^2}\) has threefold additive coverage with a different origin obstruction; its torus has \(q+1\) elements, versus the split torus's \(q-1\) elements, and its key pigeonhole bound does not establish this theorem. The split case needs the genus-one estimate and has a sharp small-field obstruction at eleven.

## Limitations
The theorem gives exact support, not the multiplicities of each three-sum representation. It neither establishes a complete classification for fields of order below thirteen nor addresses prime-power residue rings, higher sumsets or general twisted hyperbolas. Historical novelty remains subject to discovery of further equivalences in additive-combinatorial and algebraic-curve literature. Independent mathematical validation has not been performed.

## References
1. A. Bower, R. Evans, V. Luo and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930 (v1 submitted 2012-12-12), https://arxiv.org/abs/1212.2930.
2. M. R. Khan, R. Magner, S. Senger and A. Winterhof, *Two Combinatorial Geometric Problems Involving Modular Hyperbolas*, arXiv:1304.6943 (v1 submitted 2013-04-25), https://arxiv.org/abs/1304.6943.
3. H. Hasse, the classical Hasse bound for the number of rational points of a nonsingular genus-one curve over a finite field.
