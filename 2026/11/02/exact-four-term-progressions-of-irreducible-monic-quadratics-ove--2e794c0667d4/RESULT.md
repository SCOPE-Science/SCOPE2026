# Exact four-term progressions of irreducible monic quadratics over all finite fields

## Finding
Let \(q\) be any prime power, \(K=\mathbb F_q\), and \(h(T)=uT+v\in K[T]\) with \(u\ne0\). Define \(N_4(q;h)\) to be the number of monic quadratics \(f(T)=T^2+aT+b\) for which \(f,f+h,f+2h,f+3h\) are all irreducible over \(K\). The count is independent of \(u,v\), and, writing \(N_4(q)=N_4(q;h)\), the following exhaustive formulas hold.

If \(\operatorname{char}K=2\), then
\[
N_4(q)=\frac{q(q-2)}4.
\]
If \(\operatorname{char}K=3\), then
\[
N_4(q)=\frac{(q-1)(q-3)}8.
\]
For characteristic at least five, let \(\chi\) be the quadratic character of \(K\), extended by \(\chi(0)=0\), and write \(\epsilon=\chi(-1)\). Define three exact cubic character sums
\[
H_q=\sum_{t\in K}\chi(t(t-1)(t+1)),\quad
V_q=\sum_{t\in K}\chi(t(t+2)(t+3)),\quad
U_q=\sum_{t\in K}\chi(t(2t-1)(3t-2)).
\]
Then
\[
\boxed{16N_4(q)=q^2-7q+8+2(1+\epsilon)\chi(3)
+(1+\epsilon)\chi(6)H_q+2\chi(-2)V_q-U_q.}
\]
The three cubic sums are elliptic Frobenius-trace sums, each of absolute value at most \(2\sqrt q\). Consequently, the sharp existence classification, with no conditions on the slope other than nonvanishing, is
\[
\boxed{N_4(q)>0\quad\Longleftrightarrow\quad q\notin\{2,3,5\}.}
\]
For \(q=7\) a concrete example is \(h(T)=T\) and \(f(T)=T^2+2T+5\). For odd characteristic at least five, \(N_4(q)=q^2/16-7q/16+O(\sqrt q)\), with absolute implied constant.

## Assumptions and scope
The symbols \(2h\) and \(3h\) are field scalar multiples, so shifts coincide in characteristics two and three. Irreducibility is over \(K\) (not over the prime subfield). All formulas apply to every extension degree; no asymptotic hypothesis is used. For an odd finite field, monic \(T^2+cT+d\) is irreducible exactly when its discriminant \(c^2-4d\) is a nonsquare. The three character sums above are defined only in the characteristic-at-least-five branch.

## Proof
**Normalization in odd characteristic.** Put
\[
X=\frac{a^2-4b}{u^2},\qquad Y=\frac{2au-4v}{u^2}.
\]
For fixed \(u\ne0,v\), this is a bijection \((a,b)\leftrightarrow(X,Y)\). The normalized discriminant of \(f+jh\) is \(z_j=X+jY+j^2\), for \(j=0,1,2,3\). Hence the count is independent of \(h\), and counts pairs for which all distinct \(z_j\) have character \(-1\).

**Characteristic two.** Because \(2h=0\) and \(3h=h\), there are only two distinct quadratic conditions. A monic quadratic \(T^2+aT+b\) is irreducible precisely when \(a\ne0\) and \(\operatorname{Tr}(b/a^2)=1\), where the trace is to \(\mathbb F_2\). Both the leading linear coefficients \(a\) and \(a+u\) must be nonzero, so \(a\notin\{0,u\}\). For each such \(a\), the two trace constraints on \(b\) have distinct nonzero multipliers \(a^{-2}\) and \((a+u)^{-2}\). They therefore define independent \(\mathbb F_2\)-linear functionals; exactly \(q/4\) values of \(b\) work (in the sole case \(q=2\), there are no admissible \(a\)). This proves \(q(q-2)/4\).

**Characteristic three.** Now \(3h=0\), so only \(z_0,z_1,z_2\) remain. In \(\sum_{X,Y}\prod_{j=0}^{2}(1-\chi(z_j))\), single and pair character sums vanish and the triple product has sum \(q\), by the universal three-linear-factor correlation proved below. The unrestricted sum is thus \(q^2-q\). Each zero line removes \(q-\epsilon\), and each of the three pairwise-zero intersections was removed twice and contributes \(1-\epsilon\). There are no triple-zero intersections. Therefore \(8N_4(q)=q^2-q-3(q-\epsilon)+3(1-\epsilon)=q^2-4q+3\), as claimed.

**Characteristic at least five: the unrestricted sign moment.** For any distinct \(i,j,k\in\{0,1,2,3\}\), use \(z_i=s,z_j=t\) as coordinates. Then
\[
z_k=As+Bt+C,\quad A=\frac{j-k}{j-i},\quad B=\frac{k-i}{j-i},\quad C=(k-i)(k-j),\quad \frac{C}{AB}=-(j-i)^2.
\]
The basic identity \(\sum_{s,t\in K}\chi(st(s+t+1))=q\chi(-1)\) follows by summing the quadratic \(t(t+s+1)\) in \(t\), including the exceptional \(s=-1\). Rescaling gives \(\sum_{X,Y}\chi(z_iz_jz_k)=q\) for every triple. Single and double character sums vanish (sum first over one free linear coordinate). Write
\[
B=\sum_{X,Y}\prod_{j=0}^3(1-\chi(z_j))=q^2-4q+Q,
\qquad Q=\sum_{X,Y}\chi(z_0z_1z_2z_3).
\]
To compute \(Q\), set \(s=z_0\) and, for \(s\ne0\), set \(t=z_1/s\). Then \(z_2=(2t-1)s+2\), \(z_3=(3t-2)s+6\), and \(\chi(z_0z_1)=\chi(t)\). For \(t\ne1/3\), the usual quadratic character-sum identity gives a sum over \(s\) of \(-\chi((2t-1)(3t-2))\), with the zero \(s\) term subtracted. At \(t=1/3\) the two linear factors coincide, increasing the sum by \(q\chi((2t-1)(3t-2))\). Since \(\chi(t(2t-1)(3t-2))=1\) at this exceptional \(t\) and the omitted \(s=0\) terms sum to zero over \(t\), it follows that \(Q=q-U_q\). Thus \(B=q^2-3q-U_q\).

**Correction for zero discriminants.** The sign indicator \((1-\chi(z_j))/2\) gives half weight at zero, so the unrestricted sign moment must be corrected. Distinct zero lines intersect pairwise, but no three meet. Define
\[
E_j=\sum_{z_j=0}\prod_{k\ne j}(1-\chi(z_k)),\qquad
E_{jk}=\prod_{\ell\notin\{j,k\}}(1-\chi((\ell-j)(\ell-k))).
\]
The inclusion-exclusion formula is \(16N_4=B-\sum_j E_j+\sum_{j<k}E_{jk}\). On \(z_j=0\), the remaining values are \(z_k=(k-j)(Y+j+k)\). Expanding these products and applying the quadratic character-sum identity yields
\[
\sum_{j=0}^3E_j=4q-A-(1+\epsilon)\chi(6)H_q-2\chi(-2)V_q,
\]
where
\[
A=2\bigl(2\chi(2)+\chi(3)+\chi(6)+\epsilon+\chi(-2)\bigr).
\]
A direct calculation at the six pairwise-zero points gives
\[
\sum_{j<k}E_{jk}=2(1-\chi(2))(1-\chi(6))
+2(1-\epsilon)(1-\chi(3))
+(1-\chi(-2))^2+(1-\chi(2))^2.
\]
Because the characters of nonzero field elements have square one, these last two displayed constant expressions satisfy
\[
A+\sum_{j<k}E_{jk}=8+2(1+\epsilon)\chi(3).
\]
Substitution gives the exact characteristic-at-least-five formula.

**Sharp existence.** Each cubic defining \(H_q,V_q,U_q\) has three distinct roots in characteristic at least five, so Hasse's bound yields \(|H_q|,|V_q|,|U_q|\le2\sqrt q\). The exact formula implies
\[
16N_4(q)\ge q^2-7q+4-10\sqrt q>0\quad(q\ge11).
\]
For prime-power orders below eleven, the characteristic-two and characteristic-three formulas handle \(q=2,3,4,8,9\); a direct character sum gives \(N_4(5)=0\); and the explicit \(q=7\) example above proves positivity. These are all cases. The complete sharp existence criterion follows.

## Verification
The accompanying standalone `verify.py` constructs finite fields, classifies monic quadratics by an independent root-existence test (rather than a discriminant test), and exhaustively checks the formulas for four shifts. Executing `python3 verify.py` produced: `VERIFY_OK fields=19 shift_cases=258 polynomial_pairs=103856 root_test=independent`. Fields include nonprime fields of orders \(4,8,9,16,25,27,49,125\). These are finite checks and not an infinite certificate; the proof supplies the universal quantifiers.

## Relationship to prior work
Bary-Soroker's Hardy–Littlewood theorem gives the same prime-polynomial tuple family for distinct shifts in odd characteristic, with \(q^2/16+O(q^{3/2})\) in degree two with four shifts. That bound cannot recover the exact arithmetic elliptic terms, the linear coefficient in \(q\), or the sharp exceptional fields; it does not address repetitions caused by characteristics two and three. Bank–Bary-Soroker–Rosenzweig address short intervals and polynomial congruence classes, rather than an exact four-translate intersection. Pollack addresses general simultaneous prime polynomial specializations with asymptotic counting, not this four-translate degree-two evaluation. An existing exact three-shift quadratic-progression theorem gives the characteristic-three branch here because the fourth shift then repeats the first; in all other characteristics the fourth condition is an additional constraint. The principal new content is the exact four-shift count (notably in characteristic at least five), its elliptic terms and global existence criterion. An earlier exact equivalent character-sum identity not found in the surveyed literature remains a residual possibility.

## Limitations
Only monic quadratics and nonconstant affine polynomial differences are classified. The exact elliptic sums can depend on the finite field; no closed elementary expression without those three sums is asserted in general. This does not extend to longer progressions or higher polynomial degrees. Scientific review here is not independent mathematical certification.

## References
1. Bary-Soroker, *Hardy–Littlewood tuple conjecture over large finite fields*, arXiv:1206.3930, first submitted 2012-06-18, https://arxiv.org/html/1206.3930v3.
2. Bank, Bary-Soroker, Rosenzweig, *Prime polynomials in short intervals and in arithmetic progressions*, arXiv:1302.0625, first submitted 2013-02-04, https://arxiv.org/html/1302.0625v3.
3. Pollack, *Simultaneous prime specializations of polynomials over finite fields*, https://www.pollack-math.net/twinsl.pdf.
4. Hasse's classical bound for elliptic curves over finite fields (applied to the three squarefree cubic character sums).
