# Powered-Bohr upper bounds and duality for the \(\ell_p\) shift calculus

Let \(L\) denote the canonical left shift on \(\ell_p(\mathbb N_0)\),
\[
L(x_0,x_1,x_2,\dots)=(x_1,x_2,\dots),
\]
and define
\[
R_p:=\sup\Bigl\{0\le r\le1:\ \|f(rL)\|_{\ell_p\to\ell_p}
\le \|f\|_{H^\infty(\mathbb D)}\ \text{for every polynomial }f\Bigr\}.
\]
This is the \(\ell_p\) specialization of the shift radius introduced in the recent work of Kania on algebraic numerical-range spectral constants. That work gives the interpolation lower bound
\[
R_p\ge 3^{-|1-2/p|}.
\]
The following gives a complementary upper theory and an exact duality symmetry.

## Theorem

For \(1\le p\le\infty\), put
\[
q=q(p):=\min\{p,p'\}\in[1,2],
\]
with the usual endpoint convention. Define
\[
\beta_q:=\inf_{0\le a<1}
\frac{1-a^q}{a^q(1-a^q)+(1-a^2)^q}.
\]
Then:

1. For \(1<p<\infty\),
   \[
   R_p=R_{p'}.
   \]

2. For every \(1\le p\le\infty\),
   \[
   R_p\le \beta_q^{1/q}.
   \]
   For \(1<q<2\), \(\beta_q\) is exactly the powered Bohr radius of Kayumov--Ponnusamy, with their radial variable equal to \(r^q\).

3. Consequently,
   \[
   3^{-(2-q)/q}\le R_p\le \beta_q^{1/q}
   \le \bigl(2^{q/2}-1\bigr)^{1/q}.
   \]
   In particular,
   \[
   R_1=R_\infty=\frac13,\qquad R_2=1,
   \]
   and
   \[
   R_p<1\qquad (p\ne2).
   \]

4. The endpoint limits are exact:
   \[
   \lim_{p\downarrow1}R_p=\lim_{p\to\infty}R_p=\frac13,
   \qquad
   \lim_{p\to2}R_p=1.
   \]
   Moreover, if \(q=q(p)\), then
   \[
   \frac{\log2}{2}
   \le
   \liminf_{p\to2,\ p\ne2}
   \frac{1-R_p}{2-q}
   \le
   \limsup_{p\to2,\ p\ne2}
   \frac{1-R_p}{2-q}
   \le
   \frac{\log3}{2}.
   \]
   Since \((2-q(p))/|p-2|\to1\), the same bounds hold with \(|p-2|\) in the denominator. Thus the loss of contractivity away from the Hilbert point has exact linear order in \(|p-2|\).

## Proof

### 1. Forward and backward polynomial shifts have the same \(\ell_s\)-norm

Let \(1\le s<\infty\), let \(R\) be the unilateral right shift on \(\ell_s(\mathbb N_0)\), and let \(U\) be the bilateral right shift on \(\ell_s(\mathbb Z)\). For every polynomial \(f\), both \(f(R)\) and \(f(L)\) are compressions of the corresponding bilateral convolution operator, so their norms do not exceed the bilateral norm. Conversely, a finitely supported vector in \(\ell_s(\mathbb Z)\) can be translated far enough into \(\mathbb N_0\) that applying all powers occurring in \(f\) sees no boundary. Since finitely supported vectors are dense in \(\ell_s(\mathbb Z)\), each unilateral norm is at least the bilateral norm. Reflection of \(\mathbb Z\) conjugates \(U\) to \(U^{-1}\). Hence
\[
\|f(L)\|_{\ell_s\to\ell_s}
=
\|f(R)\|_{\ell_s\to\ell_s}.
\tag{1}
\]

Now let \(1<p<\infty\). Under the \(\ell_p\)-\(\ell_{p'}\) duality,
\[
 f(L)^*=\widetilde f(R),
 \qquad
 \widetilde f(z):=\sum_k\overline{a_k}z^k
 \quad\text{if }f(z)=\sum_k a_kz^k.
\]
Using (1),
\[
\|f(rL)\|_p
=
\|\widetilde f(rR)\|_{p'}
=
\|\widetilde f(rL)\|_{p'}.
\]
Since \(f\mapsto\widetilde f\) preserves the disk supremum norm and is a bijection on polynomials, contractivity at exponent \(p\) is equivalent to contractivity at \(p'\). This proves
\[
R_p=R_{p'}.
\tag{2}
\]

### 2. A Möbius test converts the operator problem into a powered Bohr obstruction

The admissible radii form an interval: if contractivity holds at \(r_0\) and \(0\le s\le r_0\), apply it at \(r_0\) to \(z\mapsto f((s/r_0)z)\). It is therefore enough to obtain the upper bound for \(1\le q\le2\). Fix \(0<a<1\) and consider the disk automorphism
\[
\phi_a(z)=\frac{a-z}{1-az}
=a-(1-a^2)\sum_{k\ge1}a^{k-1}z^k.
\]
Because its pole lies outside the closed unit disk, its Taylor truncations \(P_N\) converge uniformly on \(\overline{\mathbb D}\), and
\[
\|P_N\|_{H^\infty(\mathbb D)}\longrightarrow1.
\]
If \(r<R_q\), apply the defining contractivity inequality to \(P_N\) and to the basis vector \(e_N\). Since
\[
L^ke_N=e_{N-k}\qquad(0\le k\le N),
\]
the resulting coordinates are disjoint, and therefore
\[
\|P_N(rL)e_N\|_q^q
=
a^q+(1-a^2)^q r^q
\sum_{k=1}^N a^{q(k-1)}r^{q(k-1)}.
\]
Letting \(N\to\infty\) yields
\[
a^q+\frac{(1-a^2)^q r^q}{1-a^q r^q}\le1.
\]
Equivalently,
\[
r^q\le
\frac{1-a^q}{a^q(1-a^q)+(1-a^2)^q}.
\]
Taking the infimum over \(a\), and then letting \(r\uparrow R_q\), gives
\[
R_q^q\le\beta_q.
\tag{3}
\]
Together with (2), this proves the powered-Bohr upper bound for every \(p\).

Kayumov and Ponnusamy proved for \(1<q<2\) that the same infimum \(\beta_q\) is the exact powered Bohr radius for Schur functions under the sum
\(
\sum_k|a_k|^q s^k
\).
Thus (3) identifies a precise scalar obstruction governing the \(\ell_p\) shift calculus, with \(s=r^q\).

### 3. Explicit strictness away from \(p=2\)

Choosing \(a=2^{-1/2}\) in (3) gives
\[
\beta_q\le
\frac{1-2^{-q/2}}
{2^{-q/2}(1-2^{-q/2})+2^{-q}}
=2^{q/2}-1.
\]
Hence, for \(q<2\),
\[
R_p\le(2^{q/2}-1)^{1/q}<1.
\tag{4}
\]
At \(p=2\), von Neumann's inequality for the Hilbert-space contraction \(L\) gives \(R_2=1\).

At \(p=1\) and \(p=\infty\), a polynomial \(f(z)=\sum_{k=0}^d a_kz^k\) satisfies
\[
\|f(rL)\|=\sum_{k=0}^d|a_k|r^k,
\]
by the column-sum formula on \(\ell_1\) and the row-sum formula on \(\ell_\infty\). The classical Bohr theorem therefore gives
\[
R_1=R_\infty=\frac13.
\tag{5}
\]

### 4. Endpoint geometry

Kania's interpolation lower bound can be rewritten as
\[
R_p\ge3^{-(2-q)/q}.
\tag{6}
\]
As \(q\to1\), (6) has limit \(1/3\). For any fixed \(a<1\), (3) gives
\[
\limsup_{q\downarrow1}R_p
\le
\lim_{q\downarrow1}
\left(
\frac{1-a^q}{a^q(1-a^q)+(1-a^2)^q}
\right)^{1/q}
=
\frac1{1+2a}.
\]
Letting \(a\uparrow1\) gives the matching upper limit \(1/3\). This proves the non-Hilbert endpoint limits. The limit \(R_p\to1\) as \(p\to2\) follows immediately from (4) and (6).

Finally, put \(\varepsilon=2-q\). From (4),
\[
(2^{q/2}-1)^{1/q}
=1-\frac{\log2}{2}\varepsilon+O(\varepsilon^2),
\]
whereas (6) gives
\[
3^{-\varepsilon/q}
=1-\frac{\log3}{2}\varepsilon+O(\varepsilon^2).
\]
The stated two-sided asymptotic bounds for \(1-R_p\) follow.

## Significance

The recent shift construction shows that a contractive disk polynomial calculus can coexist with an infinite algebraic-numerical-range spectral constant. The parameter \(R_p\) measures how far one may radially dilate the canonical \(\ell_p\) shift while retaining disk contractivity. The new bounds show that the Hilbert exponent \(p=2\) is the unique point with full radius, that the radius is exactly invariant under Banach duality, and that its departure from one is linear at the Hilbert point. They also connect the operator-theoretic radius to the exact scalar powered Bohr radius.

## Limitations

The exact value of \(R_p\) for \(1<p<\infty\), \(p\ne2\), remains open. The powered-Bohr obstruction need not be attained by the operator norm of a Möbius truncation, so no equality \(R_p=\beta_q^{1/q}\) is claimed. The result concerns the canonical unilateral shift on \(\ell_p\); it does not classify analogous radii for general Banach sequence spaces. The duality argument uses the one-sided/bilateral shift structure and should not be transferred to arbitrary contractions without proof.

## References

1. T. Kania, *Spectral constants for algebraic numerical ranges*, arXiv:2609.18963 (2026), https://arxiv.org/abs/2609.18963.
2. I. R. Kayumov and S. Ponnusamy, *On a powered Bohr inequality*, Ann. Acad. Sci. Fenn. Math. **44** (2019), 301--310, https://doi.org/10.5186/aasfm.2019.4416; arXiv:1809.00157.
