# Alternating boundary-zero entry and exact local counts for odd weighted Bergman kernels

## Finding
For every integer \(k\ge1\), put \(\alpha=4k-2\) and let \(-1<\beta<0\). On the weighted analytic Bergman space with normalized radial measure
\[
d\mu_{\alpha,\beta}(z)=\frac{|z|^{2\beta}(1-|z|^2)^\alpha}{\pi B(\alpha+1,\beta+1)}\,dx\,dy,
\]
let \(K^-_{\alpha,\beta}\) be the reproducing kernel of the closed subspace of odd functions. Its scalar numerator \(J_{\alpha,\beta}(s)\), with \(s=z\overline w\), has two simple roots \(s_\pm(\beta)\) approaching \(\pm i\) as \(\beta\uparrow0\). They satisfy
\[
s_\pm(\beta)=\pm i\left(1+\frac{S_{4k}}{2k}\,\beta+O_k(\beta^2)\right),
\quad S_{4k}=\sum_{j=0}^{k-1}(-4)^j\left(\frac1{4j+1}+\frac2{4j+2}+\frac2{4j+3}\right),
\]
and \(\operatorname{sgn}S_{4k}=(-1)^{k-1}\). Thus the two boundary roots move **inside** \(|s|<1\) for odd \(k\), and **outside** for even \(k\), when \(\beta\) decreases slightly below zero.

More precisely, for each fixed \(k\) there exists \(\delta_k>0\) such that, for \(-\delta_k<\beta<0\), the number of roots of \(J_{4k-2,\beta}\) in \(|s|<1\), counted with multiplicity, is exactly
\[
\boxed{\Theta_{4k-2,\beta}=2k+(-1)^{k-1}.}
\]
This count includes the simple root at \(s=0\); the number of **attainable nonzero scalar zero fibres** on the punctured disk is \(\Theta_{4k-2,\beta}-1\). In particular, for \(\alpha=6\) (\(k=2\)),
\[
s_\pm(\beta)=\pm i\left(1-\frac{16}{105}\beta+O(\beta^2)\right),\qquad \Theta_{6,\beta}=3.
\]
There are therefore infinitely many integer boundary exponents for which a previously proposed unscaled boundary-root inclusion fails near \(\beta=0^-\).

## Assumptions and scope
Use the disk \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), its punctured version \(\mathbb D^*=\mathbb D\setminus\{0\}\), and the beta function \(B\). The density above is a probability density with respect to planar Lebesgue measure \(dx\,dy\), since the displayed factor contains \(1/\pi\). For \(-1<\beta<0\), every square-integrable holomorphic function on \(\mathbb D^*\) extends holomorphically through zero. The odd subspace is spanned by odd monomials and has kernel \(K^-_{\alpha,\beta}(z,w)=\tfrac12(K_{\alpha,\beta}(z,w)-K_{\alpha,\beta}(-z,w))\). The scalar parameter \(s=z\overline w\) is attainable with \(z,w\in\mathbb D^*\) precisely when \(0<|s|<1\). Counts at \(s=0\) concern the numerator polynomial, not an attainable punctured-disk pair.

The proof treats each fixed \(k\) and sufficiently small negative \(\beta\). No uniform neighborhood in \(k\), nor a count for all \(-1<\beta<0\), is asserted.

## Proof
**1. Kernel and numerator.** For \(m=\alpha+2=4k\), radial monomial integration gives
\[
\|z^n\|^2=\frac{B(n+\beta+1,m-1)}{B(\beta+1,m-1)}\qquad(n\ge0).
\]
Summing reciprocal norms gives the rational formula, valid for integer \(m\ge2\),
\[
K_{\alpha,\beta}(z,w)=\frac{H_{m,\beta}(s)}{(1-s)^m},\qquad
H_{m,\beta}(s)=\sum_{j=0}^{m-1}\binom{m-1}{j}\frac{\beta(-s)^j}{j+\beta}.
\]
Here the \(j=0\) summand is interpreted as \(1\). This identity can also be verified by multiplying both sides by \((1-s)^m\) and comparing the beta-moment coefficient series; it is the polynomial kernel representation in Ghiloufi--Snoun. Consequently
\[
K^-_{\alpha,\beta}(s)=\frac{F_{m,\beta}(s)}{2(1-s^2)^m},\quad
F_{m,\beta}(s)=(1+s)^m H_{m,\beta}(s)-(1-s)^m H_{m,\beta}(-s).
\]
The positive normalizations do not affect zeros. The numerator \(F_{m,\beta}\) is odd with real coefficients, and its coefficients are analytic for \(\beta\) near zero.

**2. Unperturbed roots.** Since \(H_{m,0}(s)=1\),
\[
F_{m,0}(s)=(1+s)^m-(1-s)^m.
\]
Its finite, simple roots are exactly \(s=i\tan(\pi j/m)\), \(-m/2<j<m/2\), \(j\in\mathbb Z\). For \(m=4k\), exactly \(2k-1\) lie strictly in the disk; \(s=\pm i\) lie on its boundary, and all other roots lie strictly outside. In particular, \(F_{m,0}'(i)=m(-4)^k\ne0\).

**3. Transverse boundary motion.** Write
\[
H_{m,\beta}(s)=1+\beta h_m(s)+O_m(\beta^2),\qquad
h_m(s)=\sum_{j=1}^{m-1}\binom{m-1}{j}\frac{(-s)^j}{j}
=\int_0^1\frac{(1-st)^{m-1}-1}{t}\,dt.
\]
Set
\[
S_m=\int_0^1\frac{\operatorname{Im}(1+it)^{m-1}}t\,dt.
\]
Because \((1+i)^m=(1-i)^m=(-4)^k\), the derivative of the numerator with respect to \(\beta\) at \((\beta,s)=(0,i)\) is \(-2i(-4)^kS_m\). The implicit-function theorem therefore gives the unique nearby root \(s_+(\beta)\) with
\[
s_+'(0)=\frac{2iS_m}{m}.
\]
Oddness and reality force the nearby conjugate root to be \(s_-(\beta)=-s_+(\beta)\) and each branch to remain on the imaginary axis for real \(\beta\) near zero.

**4. An exact sign law.** The integral obeys \(S_1=0\) and
\[
S_{n+1}-S_n=\operatorname{Im}\frac{(1+i)^n}{n}\quad(n\ge1),
\]
by subtracting integrands and integrating a polynomial. Grouping \(n\) modulo four and using \((1+i)^4=-4\) yields
\[
S_{4k}=\sum_{j=0}^{k-1}(-4)^j A_j,\qquad
A_j=\frac1{4j+1}+\frac2{4j+2}+\frac2{4j+3}>0.
\]
The magnitudes \(4^jA_j\) strictly increase: \(4A_1=344/105>8/3=A_0\), and for every \(j\ge1\) and \(r\in\{1,2,3\}\), \(4/(4j+4+r)>1/(4j+r)\). Pairing adjacent terms of this alternating sum shows its sign is that of the last term, namely \((-1)^{k-1}\). Since this sign is nonzero, both boundary crossings are transverse.

**5. Exact count.** Choose small disjoint disks around the simple roots of \(F_{m,0}\) intersecting \(|s|\le1\), and a compact root-free remainder. Uniform convergence of \(F_{m,\beta}\) to \(F_{m,0}\), together with Rouché's theorem (or root continuity), preserves the \(2k-1\) strictly interior roots and prevents other roots from entering. The two boundary roots contribute either two (odd \(k\)) or zero (even \(k\)). This proves the formula for \(\Theta\). The origin is a simple zero throughout a sufficiently small parameter interval, but is excluded from nonzero scalar zero fibres.

## Verification
The standalone `check.py` uses only Python 3 standard-library exact rational arithmetic. It independently evaluates \(S_{4k}\) by its binomial-integral coefficients and grouped series for \(1\le k\le12\), checks the alternating signs and the explicit \(k=2\) slope, and verifies exact sign brackets for the imaginary roots at small negative \(\beta\) in four representative cases. Executing `python3 check.py` produced: `PASS: 75 exact rational assertions; k=1..12 derivative and sign; four exact root brackets.` The program does **not** establish the infinitely quantified sign law or the limiting root count; these follow from the proof above.

## Relationship to prior work
Ghiloufi and Snoun, *Zeros of new Bergman kernels* (first public preprint September 9, 2020; published in J. Korean Math. Soc. 59 (2022), 449--468), derive the polynomial kernel representation, identify the unperturbed roots, and prove endpoint counting statements that explicitly omit the critical odd case \(\alpha\equiv2\pmod4\). Their final open-problem discussion asks whether an enlarged-disk endpoint count can be asserted with the enlargement factor set to one. The calculation here determines the missing crossing direction for the whole infinite critical odd family, and shows that the suggested inclusion is false for \(\alpha\equiv6\pmod8\), beginning at \(\alpha=6\). It does not challenge their published theorem for enlargement factors strictly greater than one.

Ghiloufi and Zaway's *Meromorphic Bergman spaces* establishes the underlying weighted spaces and functional-analytic framework, not this boundary-root sign classification. Related radial Bergman zero laws for different weights or noninteger outer exponents do not imply the parity-projected crossing formula. Historical priority beyond the inspected sources is not independently certified.

## Limitations
The result is local in \(\beta\) and does not classify zeros at arbitrary weights. The asserted count includes the formal scalar zero at the origin, which does not correspond to two points of the punctured disk; this exclusion is explicit. The argument relies on integer \(\alpha=4k-2\) and the odd subspace; it does not settle the analogous even-subspace boundary cases or the opposite \(\beta\to-1^+\) endpoint. Exact neighborhood sizes \(\delta_k\) are not optimized. No independent mathematical validation has been performed.

## References
1. N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307 (first public 2020-09-09), https://arxiv.org/abs/2009.04307 ; J. Korean Math. Soc. 59 (2022), 449--468, DOI:10.4134/JKMS.j200373.
2. N. Ghiloufi and M. Zaway, *Meromorphic Bergman spaces*, arXiv:2309.00552, https://arxiv.org/abs/2309.00552.
3. N. Ghiloufi and S. Snoun, *Berezin transforms on modified Bergman spaces*, arXiv:2401.03941, https://arxiv.org/abs/2401.03941 (related framework, not used in the proof).
