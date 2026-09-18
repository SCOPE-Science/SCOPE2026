# Rectangular low-rank masking has the same dimension-free maximal-correlation scale

## Result

Let \(q\) be a prime power, let \(A\) be uniform on
\(\mathbb F_q^{m\times n}\), and let \(X=A+R\), where \(R\) is independent of
\(A\).  Put
\[
 C_{a,b}(t)=\prod_{j=0}^{t-1}
 \frac{(q^a-q^j)(q^b-q^j)}{q^t-q^j},
 \qquad
 V_{a,b}(r)=\sum_{t=0}^r C_{a,b}(t).
\]
Thus \(C_{a,b}(t)\) is the number of \(a\times b\) matrices of rank \(t\),
and \(V_{a,b}(r)\) is the rank-ball volume.

For \(1\le r<\min\{m,n\}\):

1. **Uniform factor masks.**  If \(R=UV\), where
   \(U\in\mathbb F_q^{m\times r}\) and
   \(V\in\mathbb F_q^{r\times n}\) have independent uniform entries, then
   \[
   \boxed{\rho_{\rm m}(A;X)=q^{-r}.}
   \]

2. **Uniform rank-ball masks.**  If \(R\) is uniform on
   \(\{M:\operatorname{rank}M\le r\}\), then
   \[
   \boxed{
   \rho_{\rm m}(A;X)
   =\frac{q^r C_{m-1,n-1}(r)}{V_{m,n}(r)}
   \le q^{-r}.}
   \]

3. **Rectangular converse.**  More generally, let
   \[
   X=L_1(A+K)L_2,
   \]
   where \((L_1,L_2,K)\) is independent of \(A\),
   \(L_1\in {\rm GL}_m(\mathbb F_q)\),
   \(L_2\in {\rm GL}_n(\mathbb F_q)\), and
   \(\operatorname{rank}K\le r\) almost surely.  If
   \(r\le \min\{m,n\}-2\), then
   \[
   \boxed{
   \rho_{\rm m}(A;X)\ge
   \frac{q^{m+n-r}-q^m-q^n+1}
        {(q^m-1)(q^n-1)}
   \ge \frac{q^{-r}}2.}
   \]
   Hence the factor-mask value \(q^{-r}\), and therefore also the
   rank-ball upper bound, is within a factor two of optimal for every
   rectangle in this regime.  If \(r=o(\min\{m,n\})\), the displayed
   converse is \((1-o(1))q^{-r}\).

For rectangular matrix multiplication
\(A\in\mathbb F_q^{m\times n}\),
\(B\in\mathbb F_q^{n\times p}\), with independent uniform inputs and
independent additive masks, the complete server view is
\((X,Y,XY)\).  Since \(XY\) is determined by \((X,Y)\),
\[
 \rho_{\rm m}((A,B);(X,Y,XY))
 =\max\{\rho_{\rm m}(A;X),\rho_{\rm m}(B;Y)\}.
\]
Thus with independent factor masks of ranks \(r_A,r_B\), respectively,
the exact leakage scale is
\[
 \boxed{q^{-\min\{r_A,r_B\}}.}
\]
The weaker of the two rank budgets controls maximal-correlation secrecy.

There is also a rectangular form of the rank-bounded differential-privacy
obstruction.  If an input-independent \(m\times n\) mask \(K\) has
\(\operatorname{rank}K\le r<\min\{m,n\}\) almost surely and \(A+K\) is
entry-level \((\varepsilon,\delta)\)-differentially private, then
\[
\boxed{
\delta\ge
1-
\frac{(e^\varepsilon+q-1)\log_2 q}{2(q-1)}
\frac{(m+n)r}{mn}.}
\]
No such rank-bounded mask gives pure differential privacy for finite
\(\varepsilon\).

## Context

Cohen, D'Oliveira, and Sprintson introduced low-rank masking for
single-server matrix multiplication in arXiv:2609.18876.  Their protocol
is formulated for rectangular products \(m\times n\) by \(n\times p\),
but their maximal-correlation theorems, matching converse, approximate
individual-security theorem, and differential-privacy obstruction are
stated for square \(n\times n\) inputs.  The result above removes the
square restriction for maximal correlation and the differential-privacy
obstruction, and gives the exact dependence on both rectangular
dimensions.

The maximal-correlation definition and its guessing interpretation are
from Li and El Gamal, *Maximal Correlation Secrecy*, IEEE Transactions on
Information Theory 64(5), 3916--3926 (2018).

## Proof

### Additive channels diagonalize in characters

For \(H\in\mathbb F_q^{m\times n}\), let
\[
 \chi_H(M)=\psi\!\left(\sum_{ij}H_{ij}M_{ij}\right),
\]
where \(\psi\) is a fixed nontrivial additive character of \(\mathbb F_q\).
The characters form an orthonormal basis of functions on the additive
group \(\mathbb F_q^{m\times n}\).  Since \(A\) is uniform,
\[
 \mathbb E[\chi_H(A)\mid X=x]
 =
 \chi_H(x)\,\overline{\mathbb E[\chi_H(R)]}.
\]
Therefore
\[
 \rho_{\rm m}(A;X)
 =
 \max_{H\ne0}\left|\mathbb E\chi_H(R)\right|.
 \tag{1}
\]

### Uniform factor masks

For \(R=UV\), average first over \(V\).  The character average is nonzero
exactly when
\[
 H^TU=0.
\]
If \(s=\operatorname{rank}H\), a uniform column of \(U\) lies in
\(\ker H^T\) with probability \(q^{-s}\), independently for the \(r\)
columns.  Hence
\[
 \mathbb E\chi_H(UV)=q^{-rs}.
\]
The maximum over nonzero \(H\) occurs at \(s=1\), proving
\(\rho_{\rm m}=q^{-r}\).

### Uniform rectangular rank balls

By invertible row and column operations, for nonzero \(H\) we may arrange
\[
 H=\begin{pmatrix}1&0\\0&H'\end{pmatrix}.
\]
Write
\[
 M=\begin{pmatrix}a&b\\c&D\end{pmatrix},
\]
where \(D\) is \((m-1)\times(n-1)\).

Fix \(b,c,D\).  If \(\operatorname{rank}D<r\), then either all \(q\)
choices of \(a\) satisfy \(\operatorname{rank}M\le r\) or none do, so the
sum of the character over \(a\) vanishes.  If
\(\operatorname{rank}D=r\), reducing \(D\) to
\(\operatorname{diag}(I_r,0)\) shows that rank at most \(r\) forces
\(b\) and \(c\) into the row and column spaces of \(D\), and then fixes
\(a\) to their Schur-complement value.  Summing the character over the
\(q^r\) choices in one of the two spaces leaves exactly a factor \(q^r\).
Consequently
\[
 \sum_{\operatorname{rank}M\le r}\chi_H(M)
 =
 q^r\sum_{\operatorname{rank}D=r}\chi_{H'}(D).
 \tag{2}
\]
The absolute value is at most \(q^r C_{m-1,n-1}(r)\), with equality when
\(H\) has rank one, because then \(H'=0\).  Dividing by \(V_{m,n}(r)\)
and using (1) proves the exact formula.

Moreover, every rank-\(r\) matrix \(D\) has \(q^{2r}\) extensions \(M\)
of rank at most \(r\): choose \(b\) in its row space and \(c\) in its
column space, after which \(a\) is forced.  Hence
\[
 V_{m,n}(r)\ge q^{2r}C_{m-1,n-1}(r),
\]
which gives the upper bound \(q^{-r}\).

### Rectangular universal converse

Regard \(A\) as a linear map
\(\mathbb F_q^n\to\mathbb F_q^m\), and define
\[
 g(A)=|\ker A|=q^{n-\operatorname{rank}A}.
\]
Left and right multiplication by invertible matrices preserve \(g\), so
\(g(X)=g(A+K)\).

Put \(N=q^n\) and \(M=q^m\).  Directly counting pairs of kernel vectors
gives
\[
 \mathbb E g(A)=1+\frac{N-1}{M},
\qquad
 \operatorname{Var}(g(A))
 =
 \frac{(N-1)(q-1)(M-1)}{M^2}.
 \tag{3}
\]
For fixed \(K\) of rank \(t\), count ordered pairs \((v,w)\) satisfying
\[
 Av=0,\qquad Aw=-Kw.
\]
There are \((N-1)(N-q)\) linearly independent nonzero pairs, each
contributing probability \(M^{-2}\).  For a dependent pair
\(w=cv\ne0\), consistency holds exactly for \(v\in\ker K\), giving
\((q-1)(q^{n-t}-1)\) pairs, each with probability \(M^{-1}\).
The zero cases are immediate.  After subtracting the squared mean and
dividing by (3),
\[
 \operatorname{Corr}(g(A),g(A+K))
 =
 \frac{q^{m+n-t}-q^m-q^n+1}
 {(q^m-1)(q^n-1)}.
 \tag{4}
\]
For random \(K\), replace \(q^{-t}\) in the numerator by
\(\mathbb E q^{-\operatorname{rank}K}\).  Under
\(\operatorname{rank}K\le r\), this is at least \(q^{-r}\).
When \(r\le\min\{m,n\}-2\), the resulting lower bound is positive and
\[
 q^{-m}+q^{-n}\le \frac{q^{-r}}2,
\]
so (4), together with a denominator below \(1\) after normalization by
\(q^{m+n}\), yields the factor-two bound.

### Two independent masked inputs

For independent inputs and masks, the conditional-expectation operator
for \((A,B)\mapsto(X,Y)\) is a tensor product.  Its nontrivial singular
values are pairwise products of the singular values of the two marginal
operators.  Therefore its largest nonconstant singular value is the
larger marginal maximal correlation:
\[
 \rho_{\rm m}((A,B);(X,Y))
 =
 \max\{\rho_{\rm m}(A;X),\rho_{\rm m}(B;Y)\}.
\]
Adding \(XY\), a deterministic function of \((X,Y)\), changes nothing.

### Rectangular differential-privacy obstruction

For each matrix entry \(i\), let \(h_i(K_{-i})\) be a most likely
conditional value of \(K_i\) given the other entries and put
\[
 p_i=\Pr[K_i=h_i(K_{-i})].
\]
Apply entry-level \((\varepsilon,\delta)\)-DP to the event
\(x_i=h_i(x_{-i})\), comparing zero with each of the \(q-1\) nonzero
changes to entry \(i\).  Summing gives
\[
 (q-1)p_i\le e^\varepsilon(1-p_i)+(q-1)\delta.
\]
For every conditioning value, a distribution whose largest atom is
\(p\) has entropy at least \(2(1-p)\) bits.  Averaging over
\(K_{-i}\) therefore gives
\[
 H(K_i\mid K_{-i})
 \ge
 \frac{2(q-1)(1-\delta)}
      {e^\varepsilon+q-1}.
\]
Summing over the \(mn\) entries gives
\[
 H(K)\ge
 \frac{2mn(q-1)(1-\delta)}
      {e^\varepsilon+q-1}.
\]
Every rank-at-most-\(r\) matrix has a factorization \(UV\) with
\(U\in\mathbb F_q^{m\times r}\),
\(V\in\mathbb F_q^{r\times n}\), so
\[
 H(K)\le (m+n)r\log_2q.
\]
Combining the inequalities proves the stated bound.  For \(\delta=0\),
finite-\(\varepsilon\) DP forces the support to be invariant under every
single-entry translation and hence to have full support, impossible when
all masks have rank below \(\min\{m,n\}\).

## Verification

`artifacts/verify_rectangular_privacy.py` performs exact finite checks
over \(\mathbb F_2\).  It enumerates complete rectangular rank balls for
several small parameter sets, computes every nontrivial Fourier
coefficient, and confirms the exact rank-ball maximal-correlation
formula.  It also enumerates all \(3\times4\) matrices and verifies the
kernel-correlation formula for a rank-one additive mask.  The saved
output is in `artifacts/verification.txt`.

The finite checks support the algebra but are not used in place of the
general proof.

## Limitations

* The maximal-correlation statements assume uniform inputs.  Standard
  maximal-correlation secrecy results can convert them into guessing
  bounds for more general priors, but those extensions are not claimed
  here.
* The factor-two universal converse is stated for
  \(r\le\min\{m,n\}-2\).  Equation (4) remains an exact correlation
  identity for fixed-rank masks outside this range, but it need not give
  a positive monotone lower bound after only using
  \(\operatorname{rank}K\le r\).
* The result concerns input-independent additive low-rank masks.  It
  does not establish security against active servers or computational
  attacks.
* Classical bilinear-forms association schemes contain closely related
  rank-metric character sums.  No novelty is claimed for that general
  spectral machinery; the contribution claimed here is the rectangular
  privacy theorem, converse, and protocol-level consequences.

## References

1. A. Cohen, R. G. L. D'Oliveira, and A. Sprintson,
   *Low-Rank Masking for Single-Server Matrix Multiplication*,
   arXiv:2609.18876, 16 September 2026.
   https://arxiv.org/abs/2609.18876
2. C. T. Li and A. El Gamal, *Maximal Correlation Secrecy*,
   IEEE Transactions on Information Theory 64(5), 3916--3926, 2018.
   https://doi.org/10.1109/TIT.2018.2816066
