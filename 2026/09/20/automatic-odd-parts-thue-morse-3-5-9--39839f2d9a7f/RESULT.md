# Automatic odd parts for the cubic, fifth and ninth Thue–Morse powers

Let
\[
T(x)=\prod_{k\ge 0}(1-x^{2^k}),\qquad T(x)^m=\sum_{n\ge0}t_m(n)x^n,
\]
and define the signed odd part by
\[
\operatorname{odd}(a)=a/2^{\nu_2(a)}\quad(a\ne0),\qquad \operatorname{odd}(0)=0.
\]
Zhao Shen recently conjectured that, for every positive integer \(m\) and every \(s\ge1\), the sequence
\[
\bigl(\operatorname{odd}(t_m(n))\bmod 2^s\bigr)_{n\ge0}
\]
is 2-automatic. The conjecture was proved there for \(m=2^r\), for \(m=3\cdot2^r\) with \(r\ge2\), and for \(m=6\). The cases \(m=3,5,9\) were not covered.

## Theorem

For every \(s\ge1\) and each
\[
m\in\{3,5,9\},
\]
the sequence
\[
\bigl(\operatorname{odd}(t_m(n))\bmod 2^s\bigr)_{n\ge0}
\]
is 2-automatic.

Consequently, Shen's automatic-odd-part conjecture is now verified for every exponent \(1\le m\le9\) except \(m=7\).

The proof uses three different finite-state reductions. For \(m=3\), the coefficient recurrences close directly on two odd-part sequences. For \(m=5\) and \(m=9\), exact valuation formulas of Shen and Wang allow their matrix recurrences to be divided by the full powers of 2; the resulting normalized units satisfy constant integer recurrences in \(\nu_2(n+1)\). Modulo any fixed \(2^s\), the companion-matrix powers are eventually periodic, which turns the unbounded valuation parameter into finite-state data.

## 1. The cubic power

The functional equation \(T(x)=(1-x)T(x^2)\) gives
\[
t_3(2n)=t_3(n)+3t_3(n-1),\qquad
t_3(2n+1)=-3t_3(n)-t_3(n-1),
\]
with \(t_3(-1)=0\). Hence
\[
t_3(4n+2)=8t_3(n-1),\qquad
t_3(4n+3)=8t_3(n).
\]
Gawron, Miska and Ulas proved that \(t_3(4n)\) and \(t_3(4n+1)\) are odd for all \(n\ge0\).

Fix \(s\), and put
\[
a(n)=\operatorname{odd}(t_3(n))\bmod2^s,
\]
with \(a(-1)=0\), and
\[
b(0)=0,\qquad b(n)=a(n-1)\quad(n\ge1).
\]
Also set
\[
A_0(n)=t_3(4n)\bmod2^s,\qquad A_1(n)=t_3(4n+1)\bmod2^s.
\]
Since \(t_3(n)\) is 2-regular, its reduction modulo \(2^s\) is 2-automatic; therefore \(A_0,A_1\) are 2-automatic. The identities above give
\[
\begin{aligned}
a(4n)&=A_0(n),& a(4n+1)&=A_1(n),\\
a(4n+2)&=b(n),& a(4n+3)&=a(n),
\end{aligned}
\]
and
\[
\begin{aligned}
b(4n)&=b(n),& b(4n+1)&=A_0(n),\\
b(4n+2)&=A_1(n),& b(4n+3)&=b(n).
\end{aligned}
\]
Thus the 4-kernels of \(a\) and \(b\) lie in the union of \(\{a,b\}\) and finitely many 4-kernel elements of \(A_0,A_1\). Hence \(a\) is 4-automatic, and therefore 2-automatic because bases 4 and 2 are powers of one another. This argument includes the zero coefficients automatically through the convention \(\operatorname{odd}(0)=0\).

## 2. A finite-recurrence lifting principle

We use the following elementary principle for \(m=5,9\). Suppose an integer block is indexed by
\[
q+1=2^r u,\qquad u\text{ odd},
\]
and, after division by its known exact power of 2, the normalized block \(Y_r(u)\) satisfies on each parity class of \(r\) a fixed finite-order recurrence with integer coefficients. If the finitely many required initial slices \(Y_e(u)\bmod2^s\) are 2-automatic functions of \(u\), then the composed block sequence in \(q\) is 2-automatic modulo \(2^s\).

Indeed, write the recurrence in companion-matrix form. Modulo \(2^s\), the sequence of powers of the companion matrix is eventually periodic because it takes values in a finite matrix monoid. Thus each normalized coordinate is a finite combination of automatic initial-slice functions of \(u\), with coefficients that are eventually periodic functions of \(r\). The sequences
\[
u=\operatorname{odd}(q+1),\qquad r=\nu_2(q+1)
\]
can be inserted without leaving the class of 2-automatic sequences: automatic sequences remain automatic under the odd-part substitution, and every eventually periodic function of \(\nu_2(q+1)\) is 2-automatic. Finite block interleaving then preserves automaticity.

The initial-slice hypothesis follows here from the known 2-regularity of \(t_m\). For fixed \(e\), recovering
\[
2^{-g(e)}t_m(2^d u+c)\pmod{2^s}
\]
requires only \(t_m(2^d u+c)\bmod2^{g(e)+s}\), a fixed modulus; division by the fixed power \(2^{g(e)}\) is then a finite map on residues.

## 3. The fifth power

Shen and Wang proved that, for \(j\in\{0,1,2,3\}\),
\[
\nu_2(t_5(4q+j))=g_5(\nu_2(q+1)),
\]
where
\[
g_5(r)=4\left\lceil\frac r2\right\rceil-(r\bmod2).
\]
They also proved the exact recurrence
\[
t_5(16n-k)=80t_5(4n-k)-1024t_5(n-k),\qquad k\in\{1,2,3,4\}.
\]
Write \(q+1=2^r u\) with \(u\) odd, and define
\[
Y_r^{(j)}(u)=2^{-g_5(r)}t_5(2^{r+2}u-4+j).
\]
The valuation theorem shows that every \(Y_r^{(j)}(u)\) is odd. Since
\[
g_5(r)-g_5(r-2)=4,
\]
normalizing the recurrence gives, for \(r\ge4\),
\[
\boxed{Y_r^{(j)}(u)=5Y_{r-2}^{(j)}(u)-4Y_{r-4}^{(j)}(u).}
\]
This is a constant second-order recurrence on each parity class of \(r\). By the lifting principle, every sequence
\[
\bigl(\operatorname{odd}(t_5(4q+j))\bmod2^s\bigr)_{q\ge0}
\]
is 2-automatic; interleaving the four residue classes proves the theorem for \(m=5\).

There is also a useful explicit form. On either parity class, the characteristic roots are \(1\) and \(4\). For example,
\[
Y_{2h}=\frac{4Y_0-Y_2}{3}+\frac{Y_2-Y_0}{3}4^h,
\]
with the analogous formula from \(Y_1,Y_3\) for odd indices. Since 3 is invertible modulo every \(2^s\), for fixed \(u,j,s\) the normalized unit becomes constant modulo \(2^s\) separately on even and odd sufficiently large \(r\).

## 4. The ninth power

Shen and Wang proved, for \(j\in\{0,\ldots,7\}\),
\[
\nu_2(t_9(8q+j))=g_9(\nu_2(q+1)),
\]
where
\[
g_9(r)=5\left\lceil\frac r2\right\rceil-2(r\bmod2).
\]
They use the vector
\[
X_n=(t_9(2n-1),\ldots,t_9(2n-8))^T
\]
and obtain, from the minimal polynomial of the block matrix,
\[
\begin{aligned}
X_{2^{r+2}u}={}&6560X_{2^r u}-8472576X_{2^{r-2}u}\\
&+2235564032X_{2^{r-4}u}-68719476736X_{2^{r-6}u}.
\end{aligned}
\]
Define
\[
Y_r(u)=2^{-g_9(r)}X_{2^{r+2}u}.
\]
Using
\[
g_9(r)-g_9(r-2)=5
\]
and dividing the four coefficients by \(2^5,2^{10},2^{15},2^{20}\), respectively, gives the exact normalized vector recurrence, for \(r\ge8\),
\[
\boxed{
Y_r=205Y_{r-2}-8274Y_{r-4}+68224Y_{r-6}-65536Y_{r-8}.
}
\]
Again this is a fixed recurrence on each parity class. The lifting principle therefore makes each of the eight normalized coordinates 2-automatic modulo \(2^s\) after the substitution \(q+1=2^r u\). Since the coordinates of \(X_{2^{r+2}u}\) are precisely the eight coefficients in the block \(t_9(8q),\ldots,t_9(8q+7)\), interleaving proves the theorem for \(m=9\).

## Verification

The accompanying exact-integer script recomputes the coefficients from the functional equation, independently checks the cubic identities and oddness classes, checks the published valuation formulas for large finite ranges, and checks the two normalized recurrences. Its deterministic output is recorded in `artifacts/verification.txt`.

The finite checks support the algebra but are not used in place of the general proof.

## Relation to prior work and originality

Gawron, Miska and Ulas developed the coefficient recurrences and the detailed cubic arithmetic, including the zero set of \(t_3\). Shen and Wang later proved the exact 2-adic valuation formulas for \(m=5\) and \(m=9\) and the matrix recurrences used above. Shen's September 2026 paper introduced the automatic-odd-part problem, proved several even-exponent families, and stated the all-exponent assertion as Conjecture 6.1. That paper explicitly notes the cubic zero set but leaves the full \(m=3\) odd-part sequence within the conjecture.

To the best of our knowledge, the automaticity conclusions for \(m=3,5,9\), and the normalized recurrences displayed above as a mechanism for automatic odd parts, have not previously been stated or proved. Searches by the recent arXiv identifiers, the phrases "automatic odd parts" and "2-automatic" together with the fifth and ninth Thue–Morse powers, and equivalent coefficient notation did not locate prior coverage.

A residual originality risk remains. Xinping Wang's May 2026 undergraduate thesis, *Research on the Properties of Coefficients of Integer Powers of Generating Functions for Thue-Morse and Rudin-Shapiro Sequences*, is cited by Shen and Wang as background for the fifth-power valuation work, but its full text was not inspected. The available June paper derived from that work states valuation results, not odd-part automaticity. In addition, Shen's conjecture paper is very recent, so unindexed concurrent work cannot be excluded.

## Limitations

This result proves only the three exponents \(m=3,5,9\); it does not settle Conjecture 6.1 for arbitrary \(m\), and in particular does not settle \(m=7\). No minimal automata or sharp state-complexity bounds are constructed. The finite verification is corroborative only.

## References

1. Zhao Shen, *Powers of the Thue–Morse Series: 2-Adic Valuations and Automatic Odd Parts*, arXiv:2609.16966, 2026. https://arxiv.org/abs/2609.16966
2. Zhao Shen and Xinping Wang, *2-adic Valuations of Coefficients of the Fifth and Ninth Powers of the Thue–Morse Generating Function*, arXiv:2606.28718, 2026. https://arxiv.org/abs/2606.28718
3. Maciej Gawron, Piotr Miska, and Maciej Ulas, *Arithmetic properties of coefficients of power series expansion of \(\prod_{n=0}^{\infty}(1-x^{2^n})^t\)*, Monatshefte für Mathematik 185 (2018), 307–360; arXiv:1703.01955. https://arxiv.org/abs/1703.01955
