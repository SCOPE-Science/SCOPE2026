# A sharp ordinary-modulus median bound for two-summand expansive decompositions

## Result

Let \(X_1,\ldots,X_m\in M_d(\mathbb C)\), put
\[
S=\sum_{j=1}^m X_j,\qquad Q=\sum_{j=1}^m |X_j|,
\]
and assume that \(S\) is expansive:
\[
|S|\ge I_d.
\]
Write the eigenvalues of the positive matrix \(Q\) in decreasing order,
\[
\lambda_1(Q)\ge\cdots\ge\lambda_d(Q).
\]

### The dimension-leakage bound

If
\[
d\ge m(k-1)+1,
\]
then
\[
\boxed{\lambda_k(Q)\ge \frac1{\sqrt m}.}
\]

In particular, for two summands and the median indices occurring in the recent Bourin--Lee question, if
\[
d\in\{2n-1,2n\},\qquad |A+B|\ge I_d,
\]
then
\[
\boxed{\lambda_n(|A|+|B|)\ge \frac1{\sqrt2}.}
\]

The constant \(1/\sqrt2\) is sharp in \(M_3\), in \(M_6\), in every odd median dimension \(d=2n-1\ge3\), and in every even median dimension \(d=2n\ge6\).

## Proof of the dimension-leakage bound

Set
\[
c=\lambda_k(Q).
\]
Let \(E\) be the spectral subspace of \(Q\) spanned by eigenvectors corresponding to
\(\lambda_k(Q),\ldots,\lambda_d(Q)\), and let \(F=E^\perp\). Then
\[
\dim E=d-k+1,\qquad \dim F=k-1,
\]
and
\[
Q|_E\le cI_E,\qquad P_FQP_E=0.
\]

For \(j=1,\ldots,m-1\), consider
\[
L_j=P_F|X_j||_E:E\to F.
\]
Since each \(L_j\) has rank at most \(k-1\),
\[
\dim\bigcap_{j=1}^{m-1}\ker L_j
\ge d-k+1-(m-1)(k-1)
=d-mk+m.
\]
The assumed dimension inequality makes the right-hand side at least \(1\). Choose a unit vector
\[
x\in\bigcap_{j=1}^{m-1}\ker L_j.
\]
Because
\[
\sum_{j=1}^m P_F|X_j|P_E=P_FQP_E=0,
\]
the same vector also satisfies \(P_F|X_m|x=0\). Hence
\[
|X_j|x\in E\qquad(1\le j\le m).
\]

Define the positive compressions
\[
C_j=P_E|X_j||_E.
\]
For the chosen \(x\),
\[
C_jx=|X_j|x,
\]
while
\[
0\le C_j\le \sum_{\ell=1}^m C_\ell=Q|_E\le cI_E.
\]
Thus \(C_j^2\le cC_j\), and therefore
\[
\begin{aligned}
\sum_{j=1}^m\|X_jx\|^2
&=\sum_{j=1}^m\||X_j|x\|^2\\
&=\sum_{j=1}^m\|C_jx\|^2\\
&\le c\left\langle\sum_{j=1}^m C_jx,x\right\rangle\\
&=c\langle Qx,x\rangle\\
&\le c^2.
\end{aligned}
\]
On the other hand, \(|S|\ge I_d\) implies \(\|Sx\|\ge1\). Cauchy--Schwarz gives
\[
1\le\|Sx\|^2
=\left\|\sum_{j=1}^mX_jx\right\|^2
\le m\sum_{j=1}^m\|X_jx\|^2
\le mc^2.
\]
Hence \(c\ge m^{-1/2}\), as claimed.

For \(m=2\) and \(d=2n-1\) or \(2n\), the condition
\[
d\ge 2(n-1)+1
\]
is automatic, yielding the stated median bound.

## A sharp \(3\times3\) family

For \(t>0\), set
\[
A_t=
\begin{pmatrix}
0&0&t\\
0&1&t\\
0&0&0
\end{pmatrix},
\qquad
B_t=I_3-A_t=
\begin{pmatrix}
1&0&-t\\
0&0&-t\\
0&0&1
\end{pmatrix}.
\]
Then \(A_t+B_t=I_3\), so the expansivity hypothesis holds with equality.

Direct multiplication gives
\[
A_t^*A_t=
\begin{pmatrix}
0&0&0\\
0&1&t\\
0&t&2t^2
\end{pmatrix},
\qquad
B_t^*B_t=
\begin{pmatrix}
1&0&-t\\
0&0&0\\
-t&0&2t^2+1
\end{pmatrix}.
\]
For a positive \(2\times2\) matrix \(M\),
\[
M^{1/2}
=
\frac{M+\sqrt{\det M}\,I}
{\sqrt{\operatorname{tr}M+2\sqrt{\det M}}},
\]
whenever the displayed denominator is nonzero. Applying this to the nonzero
\(2\times2\) blocks above shows that the compression of
\[
Q_t=|A_t|+|B_t|
\]
to \(\operatorname{span}\{e_1,e_2\}\) is diagonal with entries
\[
a_t=
\frac{1+\sqrt{t^2+1}}
{\sqrt{2t^2+2+2\sqrt{t^2+1}}},
\qquad
b_t=
\frac{1+t}{\sqrt{2t^2+2t+1}}.
\]
Both satisfy
\[
a_t\longrightarrow \frac1{\sqrt2},
\qquad
b_t\longrightarrow \frac1{\sqrt2}.
\]
Cauchy interlacing for this \(2\times2\) compression gives
\[
\lambda_2(Q_t)\le \max\{a_t,b_t\}.
\]
The two-summand lower bound gives the reverse asymptotic obstruction
\[
\lambda_2(Q_t)\ge \frac1{\sqrt2}.
\]
Consequently
\[
\boxed{\lambda_2(|A_t|+|B_t|)\longrightarrow\frac1{\sqrt2}.}
\]
Thus \(1/\sqrt2\) is already sharp in \(M_3\). Taking two copies by direct sum gives
sharpness in \(M_6\), since
\[
\lambda_3(Q_t\oplus Q_t)=\lambda_2(Q_t).
\]

## Sharpness in the remaining median dimensions

A useful \(2\times2\) filler is
\[
C_t=
\begin{pmatrix}
0&t\\
0&1
\end{pmatrix},
\qquad
D_t=I_2-C_t.
\]
With \(s=\sqrt{t^2+1}\), one computes
\[
|C_t|+|D_t|
\quad\hbox{has eigenvalues}\quad
s+t,\;s-t.
\]
Hence one filler eigenvalue tends to \(+\infty\) and the other tends to \(0\).

For odd dimension \(d=2n-1\), \(n\ge2\), take one \(3\times3\) sharp block
\((A_t,B_t)\) and \(n-2\) filler blocks \((C_t,D_t)\). Their direct sums still add
to the identity. There are exactly \(n-1\) eigenvalues above the active middle
eigenvalue for large \(t\), while all filler low eigenvalues tend to \(0\). Therefore
the \(n\)-th eigenvalue tends to \(1/\sqrt2\).

For even dimension \(d=2n\), \(n\ge3\), take two \(3\times3\) sharp blocks and
\(n-3\) filler blocks. Again there are exactly \(n-1\) asymptotically large
eigenvalues, and the \(n\)-th eigenvalue tends to \(1/\sqrt2\).

Thus the two-summand constant is sharp for
\[
d=3,5,7,\ldots
\quad\hbox{and}\quad
d=6,8,10,\ldots.
\]
The \(4\times4\) median case is not resolved by this construction.

## Relation to the recent literature

Bourin and Lee asked for lower control of median eigenvalues of sums of ordinary
moduli and symmetric moduli under an expansivity hypothesis. Zhang subsequently
gave two real \(3\times3\) matrices summing to the identity for which
\(\lambda_2(|A|+|B|)\) is approximately \(0.8835\), showing that a lower bound of
\(1\) fails for ordinary moduli.

Aouichaoui and Lee recently proved a \(1/2\) lower bound for the symmetric-modulus
version. For ordinary moduli they constructed three \(3\times3\) summands whose
sum is the identity while
\[
\lambda_2\!\left(\sum_{j=1}^3|X_j|\right)
\]
can be arbitrarily small.

The theorem above identifies a sharp structural distinction. For two summands,
the ordinary-modulus median cannot fall below \(1/\sqrt2\); for three summands in
the first critical \(3\times3\) case, no positive lower bound survives. More
generally, the sufficient threshold
\[
d\ge m(k-1)+1
\]
comes exactly from the existence of a nonzero vector annihilating all leakage maps.
The three-summand \(d=3,k=2\) example lies at the immediately preceding dimension
\(d=m(k-1)\), so the extra \(+1\) in this general dimension criterion cannot simply
be removed.

## Limitations

The general bound \(m^{-1/2}\) is proved under the sufficient dimension condition
\(d\ge m(k-1)+1\); no claim is made that it is sharp for every triple \((d,m,k)\).
The \(4\times4\) two-summand median constant is not determined here. The result is
finite-dimensional and does not by itself give an infinite-dimensional essential
spectral analogue.

Originality is asserted only to the best of our knowledge. Standard spectral
subspace arguments, Cauchy interlacing, positive compression inequalities and
direct-sum constructions are not claimed as new. The novelty claim is restricted
to the dimension-leakage bound in this expansive ordinary-modulus setting, its
sharp two-summand median consequence, and the explicit sharp families above.

## References

1. J.-C. Bourin and E.-Y. Lee, *Triangle inequalities for the operator symmetric modulus*, arXiv:2602.19607v1 (2026), https://arxiv.org/abs/2602.19607.
2. L. Zhang, *Operator symmetric moduli and sharp triangle inequalities*, arXiv:2603.01046v1 (2026), https://arxiv.org/abs/2603.01046.
3. A. Aouichaoui and E.-Y. Lee, *Solutions to some open problems in matrix analysis*, arXiv:2609.20094v1 (2026), https://arxiv.org/abs/2609.20094.
