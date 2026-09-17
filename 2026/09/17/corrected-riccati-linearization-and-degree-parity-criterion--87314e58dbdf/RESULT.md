# Corrected Riccati linearization and a degree-parity irreducibility criterion

## Context

Wu and Hong introduce rank-two generalized conformal modules
\(V_{\alpha,\beta,C(x)}\) for the Virasoro conformal algebra, with
\(C(x)=(c_{ij}(x))\in M_2(\mathbb C[x])\).  For \(\alpha\ne0\), their
Theorem 4.20 reduces irreducibility to the absence of rational solutions of

\[
\gamma'+d\gamma-p\gamma^2+q=0,\qquad
 d=c_{11}-c_{22},\quad p=c_{21},\quad q=c_{12},
\tag{R}
\]

under the necessary assumptions \(p,q\ne0\).

Two useful consequences follow from examining this Riccati equation directly.
First, the linearization displayed in Remark 4.21 misses a logarithmic-derivative
term when \(p\) is nonconstant.  Second, the valuation at infinity gives a broad
coefficient-degree test that rules out rational solutions without running a full
Riccati or differential-Galois algorithm.

## 1. Corrected Riccati-to-linear reduction

### Proposition 1

Let \(p,q\in\mathbb C(x)\) with \(p\ne0\), and let \(d\in\mathbb C(x)\).
Under the substitution

\[
\gamma=-\frac{z'}{p z},
\]

Equation (R) is equivalent, wherever the expressions are defined, to

\[
z''+\left(d-\frac{p'}p\right)z'-pq\,z=0.
\tag{L}
\]

In particular, the equation \(z''+d z'-pqz=0\) displayed in Remark 4.21 is
obtained from this substitution only when \(p'/p=0\), i.e. when \(p\) is
constant.

#### Proof

Differentiate \(\gamma=-z'/(pz)\):

\[
\gamma'=-\frac{z''}{pz}+\frac{(z')^2}{p z^2}
       +\frac{p'z'}{p^2z}.
\]

The quadratic term in (R) is

\[
-p\gamma^2=-\frac{(z')^2}{p z^2}.
\]

These terms cancel.  Multiplication of the remaining equation by \(pz\)
gives

\[
-z''+\left(\frac{p'}p-d\right)z'+pqz=0,
\]

which is equivalent to (L).  The converse follows by reversing the calculation.
\(\square\)

Writing

\[
P=d-\frac{p'}p,
\]

the standard removal of the first-derivative term is

\[
z=\exp\!\left(-\frac12\int P\,dx\right)w,
\]

and it yields

\[
w''+r(x)w=0,\qquad
r=-pq-\frac12P'-\frac14P^2\in\mathbb C(x).
\tag{N}
\]

Equivalently, if one writes \(z=\rho w\), the required condition is
\(2\rho'+P\rho=0\).  Thus the second substitution stated in Remark 4.21 also
needs the multiplying factor \(\rho\), together with the corrected coefficient
\(P\).

### A concrete failure of the uncorrected equation

Take

\[
C(x)=\begin{pmatrix}0&x\\ x&0\end{pmatrix}.
\]

Then (R) is

\[
\gamma'-x\gamma^2+x=0,
\]

which has the rational solution \(\gamma=1\).  By Theorem 4.20 of Wu--Hong,
\(V_{\alpha,\beta,C}\) is therefore reducible for every \(\alpha\ne0\).

For \(z=e^{-x^2/2}\), one has \(-z'/(xz)=1\).  The corrected equation is

\[
z''-\frac1x z'-x^2z=0,
\]

and this \(z\) satisfies it.  The uncorrected equation from Remark 4.21 would be
\(z''-x^2z=0\), but for the same \(z\) its left-hand side is \(-z\ne0\).
Hence the missing logarithmic-derivative term changes the actual reduction; it
is not merely a cosmetic rewrite.

The correction does **not** invalidate Theorem 4.20 or Example 4.22.  In Example
4.22, \(p=c_{21}=1\) is constant, so the omitted term happens to vanish.

## 2. A degree-parity obstruction to rational Riccati solutions

For a nonzero polynomial \(f\), write \(\deg f\) for its ordinary degree and set
\(\deg 0=-\infty\).

### Theorem 2

Assume \(p,q\in\mathbb C[x]\setminus\{0\}\), \(d\in\mathbb C[x]\), and set

\[
B=\deg p,\qquad Q=\deg q,\qquad D=\deg d.
\]

If

\[
2D<B+Q
\tag{1}
\]

and \(B\) and \(Q\) have opposite parity, then Equation (R) has no solution in
\(\mathbb C(x)\).

Consequently, for the Wu--Hong module \(V_{\alpha,\beta,C(x)}\), if
\(\alpha\ne0\), \(c_{12}c_{21}\ne0\),

\[
2\deg(c_{11}-c_{22})
  < \deg c_{21}+\deg c_{12},
\]

and \(\deg c_{21}\not\equiv\deg c_{12}\pmod2\), then
\(V_{\alpha,\beta,C(x)}\) is irreducible.

#### Proof

Suppose that a rational solution \(\gamma\) exists.  Since \(q\ne0\),
\(\gamma\ne0\).  At infinity write

\[
\gamma(x)=\kappa x^m(1+O(x^{-1})),
\qquad \kappa\ne0,\quad m\in\mathbb Z.
\]

The exponent of growth of \(\gamma'\) is at most \(m-1\).  This derivative term
can never be the leading term of (R).  Indeed:

- if \(m\ge -B\), then \(B+2m\ge m\), so \(p\gamma^2\) has strictly larger
  exponent than \(\gamma'\);
- if \(m\le -B-1\), then \(m-1<0\le Q\), so \(q\) has strictly larger exponent
  than \(\gamma'\).

Therefore the maximal exponent among

\[
D+m,\qquad B+2m,\qquad Q
\tag{2}
\]

must occur at least twice (with the first quantity omitted when \(d=0\)).

If \(D+m=B+2m\) is maximal, then \(m=D-B\) and maximality over \(Q\) gives
\(2D-B\ge Q\), hence \(2D\ge B+Q\), contradicting (1).

If \(D+m=Q\) is maximal, then \(m=Q-D\) and maximality over \(B+2m\) gives

\[
B+2Q-2D\le Q,
\]

again implying \(2D\ge B+Q\), a contradiction.

Thus the only possible leading cancellation is

\[
B+2m=Q.
\]

Since \(m\in\mathbb Z\), this forces \(B\equiv Q\pmod2\), contrary to the
hypothesis.  Hence no rational solution exists.  The irreducibility statement
then follows from Wu--Hong Theorem 4.20. \(\square\)

### Corollary 3: equal diagonal entries

If \(c_{11}=c_{22}\), \(c_{12},c_{21}\ne0\), and the two off-diagonal
polynomials have degrees of opposite parity, then
\(V_{\alpha,\beta,C(x)}\) is irreducible for every \(\alpha\ne0\).

This recovers Wu--Hong Example 4.22 (off-diagonal degrees \(1\) and \(0\)) and
extends it to an infinite family with arbitrary nonzero off-diagonal
polynomials.  The parity condition is only sufficient: when the two degrees
have the same parity, the leading-order obstruction disappears and lower-order
terms decide the existence of a rational solution.  The reducible example
\(C=\bigl(\begin{smallmatrix}0&x\\x&0\end{smallmatrix}\bigr)\) above illustrates
that side of the boundary.

## Scope and limitations

The general Riccati-to-linear transformation and valuation-at-infinity method
are classical and are not claimed as new.  The contribution here is the
correction of the reduction stated for the Wu--Hong rank-two modules and the
resulting explicit degree-parity irreducibility criterion in that setting.

The degree criterion is not a classification.  When condition (1) fails, or
when the off-diagonal degrees have the same parity, it is inconclusive; the full
Riccati criterion or a differential-Galois analysis may still be needed.

## References

1. H. Wu and Y. Hong, *Generalized conformal modules over the Virasoro conformal algebra*, arXiv:2609.18184v1 (2026), especially Theorem 4.20, Remark 4.21, and Example 4.22. https://arxiv.org/abs/2609.18184
2. T. Crespo and Z. Hajto, *Algebraic Groups and Differential Galois Theory*, Graduate Studies in Mathematics 122, AMS (2011), Chapter 7. https://doi.org/10.1090/gsm/122

Same-model review: passed. Cross-model review: not yet performed.
