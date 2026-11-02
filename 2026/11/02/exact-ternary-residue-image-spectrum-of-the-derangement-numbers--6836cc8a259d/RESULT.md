# Exact ternary residue-image spectrum of the derangement numbers

## Finding

Let \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for every integer \(n\ge1\). These are the classical derangement (subfactorial) numbers. For each integer \(a\ge1\), let
\[
R_a=\#\{D_n\bmod 3^a:n\in\mathbb Z_{\ge0}\}.
\]
Define \(Q_0=1\), and for integers \(h\ge1\) put
\[
Q_h=1+\sum_{j=0}^{\lfloor(h-1)/2\rfloor}3^{h-2j-1}.
\]
Define \(I_0=1\), \(I_1=3\), \(I_2=7\), and for \(m\ge3\) put
\[
I_m=2\cdot3^{m-1}+3^{m-3}+2Q_{\max(m-4,0)}.
\]
Then **for every integer \(a\ge1\)**,
\[
\boxed{R_1=3,\qquad R_a=2\cdot3^{a-1}+I_{a-2}\quad(a\ge2).}
\]
The initial values for \(a=1,\ldots,9\) are \(3,7,21,61,183,545,1633,4895,14683\). In particular, the proportion of residue classes attained has the exact limit
\[
\boxed{\lim_{a\to\infty}\frac{R_a}{3^a}=\frac{725}{972}.}
\]
This is a count of **distinct attained values**, not a count of indices satisfying a congruence.

## Assumptions and scope

All residue classes are taken in \(\mathbb Z/3^a\mathbb Z\). No lower bound on the index \(n\) other than \(n\ge0\) is required. The result concerns the usual derangement recurrence with the displayed sign and normalization; it does not assert an analogous formula at a different prime.

Write \(\mathbb Z_3\) for the three-adic integers and \(\mathbb Z_3^\times\) for their units. For \(h\ge0\), \(Q_h\) is exactly the number of distinct square classes modulo \(3^h\), including zero; at \(h=0\), the quotient ring has one element. A restricted integral power series on \(\mathbb Z_3\) means a power series whose three-adic integral coefficients tend to zero, and is one-Lipschitz on \(\mathbb Z_3\).

## Proof

**1. A continuous arithmetic interpolation and the sign split.** Define
\[
F(x)=\sum_{j\ge0}(-1)^j\prod_{i=0}^{j-1}(x-i),\qquad x\in\mathbb Z_3.
\]
On every residue disc \(x=r+3t\), each block of three consecutive factors contains a factor divisible by three. Thus the \(j\)-th summand has coefficientwise divisibility by \(3^{\lfloor j/3\rfloor}\) in the variable \(t\); the series converges as a restricted power series on each disc. At a nonnegative integer \(n\), the series terminates and gives
\[
F(n)=(-1)^nD_n.
\]
Consequently \(F(n)\bmod 3^a\) depends only on \(n\bmod3^a\). As \(3^a\) is odd, both parities occur among nonnegative integers in any fixed class modulo \(3^a\). Density of nonnegative integers in \(\mathbb Z_3\) now gives
\[
\{D_n\bmod3^a:n\ge0\}
=\bigl(F(\mathbb Z_3)\cup -F(\mathbb Z_3)\bigr)\bmod3^a.
\]
The falling-factorial representation also proves the identity \(F(x)=1-xF(x-1)\), initially at nonnegative integers and then on all of \(\mathbb Z_3\) by continuity.

**2. Unit values and the singular disc.** The elementary finite polynomial reductions (obtained by omitting terms with sufficiently many factors divisible by three) are
\[
F(3t)\equiv1+6t\pmod9,
\qquad F(-1+3t)\equiv1+9(1+t+t^2)\pmod{27}.
\]
Also \(F(2+3t)\equiv1\pmod3\). Therefore the restricted series \(g(t)=(F(3t)-1)/3\) satisfies \(g(t)\equiv-t\pmod3\) *coefficientwise*. Every series of the form \(-t+3H(t)\), for restricted integral \(H\), is a bijection of \(\mathbb Z_3\), because solving for \(t\) is a strict contraction. Hence
\[
F(3\mathbb Z_3)=1+3\mathbb Z_3,
\]
and the union with its negative contains **all** of \(\mathbb Z_3^\times\).

For the remaining disc, twice applying the recurrence gives
\[
F(1+3t)=3t[-1+(1+3t)F(-1+3t)].
\]
The reduction above implies \(A(t):=F(1+3t)/9\) is a restricted integral power series. More precisely, writing \(F(-1+3t)=1+9E(t)\) yields
\[
A(t)=t^2+3t(1+3t)E(t),
\qquad A(t)\equiv t^2\pmod3.
\]
Direct reduction of the falling-factorial sum modulo \(81\), followed by division by nine, gives the stronger coefficientwise congruence
\[
A(t)\equiv4t^2+3t+3t^3\pmod9.
\]
These reductions involve only the terms \(j\le11\), since every later term on the disc \(1+3\mathbb Z_3\) has four factors divisible by three.

**3. An exact three-adic quadratic normal form.** Since \(A'(t)\equiv2t\pmod3\) and \(A''(t)\equiv2\pmod3\), there is a unique critical point \(t_0\in\mathbb Z_3\). Indeed the equation \(A'(t)=0\) is a strict-contraction fixed-point equation because \(A'(t)=2t+3H(t)\), with restricted integral \(H\). The displayed congruence modulo nine gives \(t_0\equiv3\pmod9\).

Set \(c=A(t_0)\). A Taylor expansion at \(3\), using \(t_0\equiv3\pmod9\) and \(A'(3)\equiv0\pmod9\), shows \(c\equiv A(3)\pmod{27}\). As \(F(10)=D_{10}=1{,}334{,}961\),
\[
c\equiv D_{10}/9\equiv18\pmod{27},
\qquad \nu_3(c)=2.
\]
Taylor expansion at the critical point gives
\[
A(t_0+z)=c+z^2B(z),\qquad B(z)\equiv1\pmod3,
\]
with restricted integral \(B\). The three-adic square root \(\sqrt{B(z)}\equiv1\pmod3\) is again a restricted integral series. The change of coordinates \(z\mapsto z\sqrt{B(z)}\) is \(z+3H_1(z)\), hence a bijection of \(\mathbb Z_3\) by contraction. Therefore the **entire image**, not merely its valuation pattern, is
\[
\boxed{A(\mathbb Z_3)=c+\{u^2:u\in\mathbb Z_3\}.}
\]
It follows that
\[
F(\mathbb Z_3)\cup-F(\mathbb Z_3)
=\mathbb Z_3^\times\ \cup\ 9\bigl((c+\mathrm{Sq})\cup(-c-\mathrm{Sq})\bigr),
\]
where \(\mathrm{Sq}=\{u^2:u\in\mathbb Z_3\}\); the two parts are disjoint.

**4. Counting the signed quadratic image.** Let \(I_m\) denote the number of classes modulo \(3^m\) in \((c+\mathrm{Sq})\cup(-c-\mathrm{Sq})\). Because \(c\in9\mathbb Z_3\), direct counts give \(I_0=1\), \(I_1=3\), and \(I_2=7\). For every \(m\ge3\), the square arguments \(u\) which are units give *all* the classes congruent to \(1\pmod3\) in the positive branch and *all* classes congruent to \(2\pmod3\) in the negative branch. They contribute \(2\cdot3^{m-1}\) classes. All remaining arguments have \(u=3v\), so their values are \(9(d+v^2)\) and their negatives, where \(d=c/9\equiv2\pmod3\). Put \(k=m-2\). For \(k\ge1\), units \(v\) give \(d+v^2\in3\mathbb Z_3\), in fact **all** of \(3\mathbb Z_3\) (since unit squares fill \(1+3\mathbb Z_3\)). This accounts for \(3^{k-1}\) classes modulo \(3^k\). Divisible \(v\) give \(d+9w^2\) in the residue class \(2\pmod3\) and their negatives in \(1\pmod3\), producing \(2Q_{\max(k-2,0)}\) further classes. The three sets are disjoint. Hence for \(m\ge3\),
\[
I_m=2\cdot3^{m-1}+3^{m-3}+2Q_{\max(m-4,0)}.
\]
For any \(h\ge1\), a nonzero square modulo \(3^h\) has some even valuation \(2j<h\). At that valuation there are exactly \(3^{h-2j-1}\) square classes, and zero adds one. This proves the stated formula for \(Q_h\).

The units account for \(2\cdot3^{a-1}\) classes modulo \(3^a\); for \(a\ge2\) the multiple-of-nine branch has \(I_{a-2}\) distinct values, including the sole zero class when \(a=2\). This proves the formula for \(R_a\) (and \(R_1=3\) directly).

Finally, the geometric sum gives \(Q_h/3^h\to3/8\). Using the formula for \(I_{a-2}\),
\[
\lim_{a\to\infty}\frac{R_a}{3^a}
=\frac23+\frac2{27}+\frac1{243}+\frac{2}{3^6}\frac38
=\frac{725}{972}.
\]
This completes the proof.

## Verification

Run \(\texttt{python3 verify.py}\) using the Python standard library. The program independently enumerates the residues of the recurrence over one full period of length \(2\cdot3^a\) for each \(1\le a\le9\), checks the three finite polynomial congruences underlying the proof and the critical-value residue, and independently enumerates signed shifted squares at small powers. Its expected terminal line is:

```text
VERIFY_OK polynomial_certificates=3 image_indices=59046 signed_square_inputs=3280 limiting_density=725/972
```

The computer checks are finite corroborations; the unrestricted statement follows from the analytic normal form and exact counting proof above.

## Relationship to prior work

Sun and Zagier (2010) gave classical derangement congruences involving Bell numbers modulo primes. Miska (2015) established periodicity of derangement residues modulo arbitrary integers, the associated pseudo-polynomial interpolation, and Hensel criteria for prime-adic valuations. In particular the period \(2\cdot3^a\) and existence of interpolation are **not** new claims. O'Desky and Richman (2020) developed much broader prime-adic interpolation of derangements and related incomplete-gamma functions, also extending older work of Barsky (1981). The claim here is specifically the **entire image set's cardinality at every ternary prime power** and its limiting occupancy density, obtained from the quadratic critical-point normal form; it does not follow merely from a period or a zero-fiber valuation criterion. A historically earlier equivalent special-purpose image theorem cannot be ruled out from the sources inspected.

## Limitations

The result does not determine the frequency with which each attained residue occurs over one index period, or analogous image spectra for other primes or generalized derangement sequences. Independent mathematical validation is not included. The literature survey cannot establish absolute priority; Barsky's older full article was not completely inspected.

## References

- Zhi-Wei Sun and Don Zagier, *On a curious property of Bell numbers*, arXiv:1008.1573, first publicly posted 2010-08-09, https://arxiv.org/abs/1008.1573.
- Piotr Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, arXiv:1508.01987, first publicly posted 2015-08-09, https://arxiv.org/abs/1508.01987; especially the sections on exact modular periods and three-adic interpolation.
- Andrew O'Desky and David Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, first publicly posted 2020-12-08, https://arxiv.org/abs/2012.04615.
- Daniel Barsky, *Analyse p-adique et suites classiques de nombres*, Séminaire Lotharingien de Combinatoire B05b (1981), abstract and access paths at https://www.mat.univie.ac.at/~slc/opapers/s05barsky.html.
