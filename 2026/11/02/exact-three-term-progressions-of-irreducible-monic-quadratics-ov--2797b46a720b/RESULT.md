# Exact three-term progressions of irreducible monic quadratics over odd finite fields

## Finding
Let \(q\) be any odd prime power, \(F=\mathbb F_q\), and \(h(T)=uT+v\) with \(u\in F^\times\), \(v\in F\). Then the number \(N_q(h)\) of monic quadratics \(f\in F[T]\) for which the three *distinct* polynomials \(f\), \(f+h\), and \(f+2h\) are simultaneously irreducible is
\[
N_q(h)=\frac{(q-1)(q-3)}8.
\]
In particular, the count is independent of both coefficients of \(h\). Such a progression exists if and only if \(q\ge 5\). Summing over all \(q(q-1)\) nonconstant affine steps gives exactly \(q(q-1)^2(q-3)/8\) ordered pairs \((f,h)\).

## Assumptions and scope
The characteristic is odd, so \(2\) and \(4\) are invertible. The step must have nonzero linear coefficient. Quadratics are monic and irreducibility is over \(F\). Let \(\chi:F\to\{-1,0,1\}\) be the quadratic character, with \(\chi(0)=0\). We use the standard identity \(\sum_{t\in F}\chi(t(t+c))=-1\) for every nonzero \(c\in F\); equivalently, for nonzero \(c\), \(\sum_t\chi(t(c-t))=-\chi(-1)\). This holds over all finite fields of odd order.

## Proof
Write \(f(T)=T^2+aT+b\). For \(j\in\{0,1,2\}\), its translate \(f+jh\) has discriminant
\[
D_j=(a+ju)^2-4(b+jv).
\]
A monic quadratic is irreducible precisely when its discriminant is a nonsquare (not zero). Put \(x=D_0/u^2\) and \(y=D_1/u^2\). As \(D_1-D_0=2au+u^2-4v\), the map \((a,b)\mapsto(x,y)\) is a bijection of \(F^2\): \(y-x\) determines \(a\), then \(x\) determines \(b\). Also
\[
D_2/u^2=2y-x+2=:z.
\]
Thus \(N_q(h)\) is the number of \((x,y)\in F^2\) with \(x,y,z\) all nonsquares.

Set \(W(x,y)=(1-\chi(x))(1-\chi(y))(1-\chi(z))\). When \(xyz\ne0\), its value is \(8\) if all three are nonsquares, and \(0\) otherwise. To calculate \(S=\sum_{x,y}W(x,y)\), expand the product. Every linear character sum vanishes, as do all pairwise products, since any two of \(x,y,z\) are independent affine coordinates of \(F^2\). Therefore
\[
S=q^2-\sum_{x,y\in F}\chi(x)\chi(y)\chi(2y-x+2).
\]
For \(c\ne0\), \(\sum_x\chi(x(c-x))=-\chi(-1)\); for \(c=0\), it is \((q-1)\chi(-1)\). Apply this with \(c=2(y+1)\), separate \(y=-1\), and use \(\sum_{y\ne-1}\chi(y)=-\chi(-1)\). The triple sum equals \(q\). Hence \(S=q^2-q\).

The function \(W\) is not identically zero on the discriminant-zero lines; their contribution must be subtracted. The three lines \(x=0\), \(y=0\), and \(z=0\) have respective weighted sums
\[
q-\chi(2),\qquad q-\chi(-1),\qquad q-\chi(2).
\]
For example, the first follows by summing \((1-\chi(y))(1-\chi(2(y+1)))\) and using \(\sum_y\chi(y(y+1))=-1\). The other two are analogous. Their pairwise intersection weights are \(1-\chi(2)\), \(1-\chi(-1)\), and \(1-\chi(2)\), respectively. There is no triple intersection because \(z(0,0)=2\ne0\). Inclusion–exclusion therefore gives weighted union sum \(3q-3\). Consequently
\[
8N_q(h)=S-(3q-3)=q^2-4q+3=(q-1)(q-3).
\]
This establishes the formula. For odd prime-power \(q\), the formula is zero exactly at \(q=3\) and strictly positive otherwise. There are \(q(q-1)\) affine steps with nonzero slope, giving the final total.

## Verification
The accompanying standalone `verify.py` constructs finite fields using explicit irreducible moduli over prime subfields and exhaustively enumerates all nonzero-slope affine steps, all monic quadratics, and their discriminants. It independently tests nonsquareness by constructing the set of field squares; no quadratic-character character-sum identity is used in the checker. It passed \(2322\) step cases across the fields of orders \(3,5,7,9,11,13,17,19,25,27\). This finite verification corroborates but does not substitute for the proof for all odd prime powers. For illustration, for \(q=5\), \(h(T)=T\), the single admissible monic quadratic is \(T^2+4T+2\).

## Relationship to prior work
Bary-Soroker's Hardy–Littlewood tuple theorem (2012 preprint, Theorem 1.1) covers the *same tuple-counting function* for arbitrary fixed polynomial shifts but yields the asymptotic \(q^n/n^r+O_{n,r}(q^{n-1/2})\). Specializing to degree \(2\) and a three-term linear progression gives \(q^2/8+O(q^{3/2})\), not the exact lower-order correction or sharp small-field existence criterion proved here. The 2015 preprint of Gómez-Pérez, Ostafe, and Sha uses “consecutive polynomial” for a different construction: polynomials of successive degrees made by appending a coefficient, rather than three translates of one monic quadratic. Bender–Pollack (2009) studies the corresponding two-prime and Goldbach asymptotics. Earlier work of Effinger, Hicks, and Mullen (2002) on twin irreducibles is relevant historical background; its full chapter was not available for a decisive comparison. The exact result here concerns three distinct prime polynomials, not just pairs or a single-polynomial irreducibility count.

## Limitations
No claim is made for characteristic two, where \(f+2h=f\) and a three-term progression degenerates. The nonzero-slope restriction is essential to the coordinate-bijection proof; constant shifts and longer progressions require separate analysis. The historical originality check cannot exclude an equivalent elementary character-sum computation in uncatalogued or inaccessible work, particularly the 2002 chapter noted above. Independent mathematical validation has not been performed.

## References
1. L. Bary-Soroker, *Hardy–Littlewood Tuple Conjecture Over Large Finite Fields*, arXiv:1206.3930 (first posted 2012-06-18), Theorem 1.1. https://arxiv.org/abs/1206.3930
2. D. Gómez-Pérez, A. Ostafe, M. Sha, *The Arithmetic of Consecutive Polynomial Sequences over Finite Fields*, arXiv:1509.01936 (first posted 2015-09-07), Sections 1 and 5. https://arxiv.org/abs/1509.01936
3. A. O. Bender, P. Pollack, *On quantitative analogues of the Goldbach and twin prime conjectures over \(\mathbb F_q[t]\)*, arXiv:0912.1702 (first posted 2009-12-09). https://arxiv.org/abs/0912.1702
4. G. W. Effinger, K. H. Hicks, G. L. Mullen, *Twin Irreducible Polynomials over Finite Fields*, in *Finite Fields with Applications to Coding Theory, Cryptography and Related Areas*, pp. 94–111, 2002. doi:10.1007/978-3-642-59435-9_8. (Full text not inspected.)
