# Exact exponential-realizer window for line-deleted critical Fock zero sets

## Finding

Let
\[
s=\sqrt{\pi},
\qquad
\mathcal L=s(\mathbb Z+i\mathbb Z),
\qquad
\mathcal V=is\mathbb Z.
\]
Choose distinct points
\[
a_1,\ldots,a_N\in\mathcal L\setminus\mathcal V,
\qquad N\ge1,
\]
and define
\[
\Sigma_N
=
\mathcal L\setminus
\bigl(\mathcal V\cup\{a_1,\ldots,a_N\}\bigr),
\]
\[
g_N(z)
=
\frac{\sigma(z)}
{\sinh(sz)\prod_{j=1}^N(z-a_j)},
\]
where \(\sigma\) is the Weierstrass sigma function of the square lattice.

Every Bargmann--Fock function whose exact zero divisor is \(\Sigma_N\) is of the form
\[
F(z)=C e^{tz}g_N(z),
\qquad C\ne0,
\qquad t\in\mathbb R.
\]
The admissible parameter window is exactly
\[
|t|<\sqrt\pi
\]
when \(N=1\), and exactly
\[
|t|\le\sqrt\pi
\]
when \(N\ge2\).

The source proves that the exact insertion index of \(\Sigma_N\) is \(N-1\). Hence the exponential-realizer window is open precisely at insertion index zero and becomes closed at both endpoints for every positive insertion index.

## Assumptions and scope

The Bargmann--Fock space is normalized by
\[
\mathcal F^2
=
\left\{
 f\in\mathcal O(\mathbb C):
 \frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty
\right\}.
\]

The points \(a_j\) are arbitrary distinct points of \(\mathcal L\setminus\mathcal V\). All zeros are simple.

The source establishes that \(g_N\in\mathcal F^2\), that \(\mathcal Z(g_N)=\Sigma_N\), that the insertion index is \(N-1\), and that \(e^{tz}g_N\in\mathcal F^2\) for real \(|t|<\sqrt\pi\). The new statement classifies every exact realizer and settles both endpoint parameters.

No classification is claimed for all functions in the vanishing space \(\mathcal I(\Sigma_N)\), since such functions may have additional zeros.

## Proof

Write
\[
s=\sqrt\pi,
\qquad
P_N(z)=\prod_{j=1}^N(z-a_j).
\]
The source proves the line-deletion estimate
\[
\frac{|\sigma(z)|e^{-|z|^2/2}}{|\sinh(sz)|}
\le
C e^{-s|\operatorname{Re}z|}.
\]
Since
\[
|P_N(z)|\ge c_N|z|^N
\]
outside a fixed disk, it follows that
\[
|g_N(z)|^2e^{-|z|^2}
\le
C_N
\frac{e^{-2s|\operatorname{Re}z|}}
{(1+|z|^2)^N}.
\tag{1}
\]

The source also constructs shifted cell-center disks \(Q_{p,q}\) and proves, on every sufficiently remote one,
\[
(1+|z|^2)^N|g_N(z)|^2e^{-|z|^2}
\ge
c_N e^{-2s|\operatorname{Re}z|}.
\tag{2}
\]

Now let \(F\in\mathcal F^2\) have exact zero divisor \(\Sigma_N\). The source Hadamard-rigidity lemma gives
\[
F(z)=C e^{Az^2+Bz}g_N(z)
\]
for some \(A,B,C\in\mathbb C\) with \(C\ne0\).

Suppose \(A\ne0\). There is an open sector on which
\[
\operatorname{Re}(Az^2)\ge c_A|z|^2
\]
for some \(c_A>0\). A smaller sector contains infinitely many remote shifted cell disks. On those disks, (2) implies that the weighted integrand of \(F\) is bounded below by a polynomial factor times
\[
\exp\!\left(2c_A|z|^2-C|z|\right),
\]
so the Fock norm diverges. Therefore
\[
A=0.
\]

Write
\[
B=u+iv.
\]
If \(v\ne0\), use the vertical shifted-cell family from the source, whose real parts stay bounded while the imaginary parts tend to both signs of infinity. Choosing the sign for which
\[
-v\operatorname{Im}z\to+\infty,
\]
(2) gives an exponentially growing lower bound divided only by \((1+|z|^2)^N\). Thus the Fock norm diverges. Hence
\[
v=0,
\]
so \(B=t\in\mathbb R\).

It remains to determine the real parameter window. Multiplying (1) by \(e^{2t\operatorname{Re}z}\) shows immediately that
\[
e^{tz}g_N\in\mathcal F^2
\]
whenever
\[
|t|<s.
\]

At the endpoint \(t=s\), the exponential decay in (1) cancels only on the right half-plane. There the remaining upper bound is
\[
C_N(1+|z|^2)^{-N}.
\]
This is integrable in two dimensions exactly when
\[
N>1.
\]
The same argument applies at \(t=-s\). Therefore both endpoints belong to the window for every \(N\ge2\).

For \(N=1\) and \(t=s\), take shifted cells with large positive horizontal index \(p\) and \(|q|\le p\). On each such cell the factors
\[
e^{-2s\operatorname{Re}z}
\quad\text{and}\quad
e^{2s\operatorname{Re}z}
\]
cancel up to a uniform constant. By (2), the contribution of that cell is bounded below by a constant multiple of
\[
\frac1{p^2+q^2}.
\]
Hence the norm dominates
\[
\sum_{p\ge P}\sum_{|q|\le p}\frac1{p^2+q^2}.
\]
For each \(p\), the inner sum is bounded below by a constant multiple of \(p^{-1}\), so the series diverges. The endpoint \(t=-s\) is symmetric.

Finally, if \(t>s\), use a horizontal sequence of shifted cells with positive real part. Formula (2) then gives a lower bound containing
\[
\exp\!\left(2(t-s)\operatorname{Re}z\right)
\]
divided by a fixed polynomial power, and the norm diverges. The case \(t<-s\) is symmetric.

These cases prove the complete classification.

## Verification

The primary source was inspected through the square-lattice normalization, the definition of \(g_N\), the line-deletion upper estimate, the shifted-cell lower estimate, Hadamard rigidity for exact realizers, the insertion-index theorem, and the proof that \(e^{tz}g_N\) belongs to the Fock space for \(|t|<\sqrt\pi\).

The endpoint calculation uses the same source estimates without numerical approximation. At \(|t|=\sqrt\pi\), one half-plane loses its exponential damping and is governed by the two-dimensional power tail \((1+|z|^2)^{-N}\), which is integrable exactly for \(N\ge2\). The shifted-cell lower estimate proves divergence in the remaining cases.

The exclusion of complex linear parameters and quadratic exponential factors is likewise obtained from the source lower bound on explicit cell families. No finite experiment is used.

## Relationship to prior work

Hou and Ma construct \(\Sigma_N\) to show that an infinite-dimensional vanishing space can have any prescribed finite insertion index. Their Proposition on infinite-dimensionality exhibits the subfamily
\[
e^{tz}g_N,
\qquad |t|<\sqrt\pi,
\]
but does not classify all exact realizers and does not decide the endpoint parameters.

Earlier work on Fock zero sets studies dependence on the Fock exponent, hereditary zero-set properties, and stability of uniqueness sets. Those results do not give the exact exponential multiplier window for this newly introduced line-deleted critical-lattice family.

The complete window reveals an additional link between the source's two structures: endpoint inclusion occurs exactly when the insertion index \(N-1\) is positive.

## Limitations

The theorem classifies exact realizers of the specific line-deleted square-lattice family \(\Sigma_N\). It does not classify all elements of \(\mathcal I(\Sigma_N)\) that may carry additional zeros.

No analogous classification is asserted for other critical lattices, multiple deleted lines, or non-lattice critical configurations.

The endpoint closure is a feature of this explicit family and is not claimed as a universal characterization of positive insertion index.

## References

1. S. Hou and P. Ma, *On the zero sets of the Bargmann--Fock space*, arXiv:2609.37704v1, 2026.
2. D. Aadi, B. Bouya, and Y. Omari, *On zero sets in Fock spaces*, Journal of Mathematical Analysis and Applications 466 (2018), 1299--1307.
3. D. Aadi and Y. Omari, *Zero and uniqueness sets for Fock spaces*, Canadian Mathematical Bulletin 66 (2023), 532--543.
4. K. Zhu, *Analysis on Fock Spaces*, Graduate Texts in Mathematics 263, Springer, 2012.
