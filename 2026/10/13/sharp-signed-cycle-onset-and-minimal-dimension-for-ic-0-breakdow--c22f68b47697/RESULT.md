# Sharp signed-cycle onset and minimal dimension for IC(0) breakdown

## Finding
Consider exact-arithmetic, unshifted level-zero incomplete Cholesky factorization IC(0). The lower-triangular sparsity pattern is fixed to that of a real symmetric positive-definite matrix \(A\), and the natural ordering is used.

There are two conclusions.

First, IC(0) cannot break down for an SPD matrix of order at most three. Consequently, dimension four is the smallest order at which an exact-arithmetic zero or negative pivot can occur.

Second, the classical four-cycle obstruction has an exact phase diagram. Define
\[
A(t)=
\begin{pmatrix}
1&-t&0&t\\
-t&1&-t&0\\
0&-t&1&-t\\
t&0&-t&1
\end{pmatrix},
\qquad t\ge0.
\]
Then \(A(t)\) is SPD exactly for
\[
0\le t<\frac1{\sqrt2}.
\]
For IC(0), the squared pivots are
\[
q_1=1,\qquad
q_2=1-t^2,
\]
\[
q_3=\frac{1-2t^2}{1-t^2},
\qquad
q_4=
\frac{(1-t^2)(1-3t^2)}
{1-2t^2}.
\]
Hence IC(0) has strictly positive pivots exactly for
\[
0\le t<\frac1{\sqrt3},
\]
has a zero fourth pivot at
\[
t=\frac1{\sqrt3},
\]
and breaks down with a negative fourth pivot throughout
\[
\frac1{\sqrt3}<t<\frac1{\sqrt2}.
\]

The eigenvalues of \(A(t)\) are
\[
1-\sqrt2\,t
\quad\text{and}\quad
1+\sqrt2\,t,
\]
each twice. Therefore the sharp condition-number onset of breakdown within this Jacobi-scaled signed-cycle family is
\[
\boxed{
\kappa_*
=
5+2\sqrt6
=
9.898979485566\ldots
}.
\]

Kershaw's classical matrix
\[
K=
\begin{pmatrix}
3&-2&0&2\\
-2&3&-2&0\\
0&-2&3&-2\\
2&0&-2&3
\end{pmatrix}
\]
is exactly
\[
K=3A\!\left(\frac23\right).
\]
Its IC(0) squared pivots are
\[
3,\qquad
\frac53,\qquad
\frac35,\qquad
-5.
\]
Thus the historical isolated counterexample sits strictly inside the negative-pivot phase of an exact one-parameter family.

## Assumptions and scope
IC(0) means that the Cholesky recurrences are executed only at positions present in the lower triangle of \(A\); fill positions are discarded. No diagonal shift, pivot repair, reordering, threshold dropping, or finite-precision safeguard is used.

Breakdown means that the quantity under a required Cholesky square root is nonpositive. The statement is therefore about exact arithmetic, not overflow or rounding-error breakdown.

The minimal-dimension theorem ranges over all real SPD matrices and all their zero patterns at orders \(1\), \(2\), and \(3\), with the natural ordering. The condition-number value
\[
5+2\sqrt6
\]
is asserted only for the displayed Jacobi-scaled signed four-cycle family. It is not claimed to be a global condition-number threshold over all four-dimensional sparsity patterns or all dimensions.

## Proof
For \(n=1\), positivity of the unique pivot is the definition of positive definiteness.

For \(n=2\), either the off-diagonal entry is zero or IC(0) coincides with complete Cholesky. In both cases the two pivots are positive because the leading principal minors are positive.

Now let
\[
A=
\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{12}&a_{22}&a_{23}\\
a_{13}&a_{23}&a_{33}
\end{pmatrix}
\]
be SPD.

If the lower-triangular zero pattern generates no dropped fill, IC(0) is the complete Cholesky factorization and cannot break down.

The only genuinely incomplete three-dimensional case, up to deleting additional edges, occurs when
\[
a_{23}=0,\qquad
a_{12}\ne0,\qquad
a_{13}\ne0.
\]
After the first column, complete Cholesky would create a fill entry in position \((3,2)\), while IC(0) discards it. The IC(0) pivots satisfy
\[
q_1=a_{11}>0,
\]
\[
q_2
=
a_{22}-\frac{a_{12}^2}{a_{11}}
>0,
\]
and, because the dropped position \((3,2)\) is not used,
\[
q_3
=
a_{33}-\frac{a_{13}^2}{a_{11}}.
\]
The \(2\times2\) principal submatrix on indices \(\{1,3\}\) is SPD, so
\[
a_{11}a_{33}-a_{13}^2>0,
\]
which is exactly \(q_3>0\). Deleting any of the two retained first-column edges only removes a nonnegative square from these formulas. Therefore every SPD matrix of order at most three has a well-defined IC(0) factorization.

For the four-dimensional family, write
\[
A(t)=I+tB,
\]
where
\[
B=
\begin{pmatrix}
0&-1&0&1\\
-1&0&-1&0\\
0&-1&0&-1\\
1&0&-1&0
\end{pmatrix}.
\]
A direct multiplication gives
\[
B^2=2I.
\]
Thus the spectrum of \(B\) is
\[
\{-\sqrt2,-\sqrt2,\sqrt2,\sqrt2\},
\]
and the spectrum of \(A(t)\) is
\[
\{1-\sqrt2\,t,1-\sqrt2\,t,1+\sqrt2\,t,1+\sqrt2\,t\}.
\]
Hence \(A(t)\) is SPD exactly when
\[
t<1/\sqrt2.
\]

Run IC(0) in the natural order. The first squared pivot is
\[
q_1=1.
\]
The retained entry in position \((2,1)\) is \(-t\), so
\[
q_2=1-t^2.
\]
The retained entry in position \((3,2)\) equals
\[
-\frac{t}{\sqrt{1-t^2}},
\]
giving
\[
q_3
=
1-\frac{t^2}{1-t^2}
=
\frac{1-2t^2}{1-t^2}.
\]

The complete factorization would create fill at position \((4,2)\), but IC(0) drops that position because \(a_{42}=0\). Consequently the retained \((4,3)\) entry is simply
\[
-\frac{t}{\sqrt{q_3}}.
\]
The final squared pivot is therefore
\[
q_4
=
1-t^2-\frac{t^2}{q_3}
=
\frac{(1-t^2)(1-3t^2)}
{1-2t^2}.
\]
Throughout the SPD range one has
\[
1-t^2>0.
\]
Before the fourth pivot is reached one also requires
\[
q_3>0,
\]
which is equivalent to
\[
t^2<\frac12
\]
and is already guaranteed by positive definiteness. Thus the sign of the final pivot is exactly the sign of
\[
1-3t^2.
\]
This proves the stated phase diagram.

Finally,
\[
\kappa_2(A(t))
=
\frac{1+\sqrt2\,t}
{1-\sqrt2\,t}.
\]
At
\[
t=\frac1{\sqrt3},
\]
this becomes
\[
\frac{1+\sqrt{2/3}}
{1-\sqrt{2/3}}
=
5+2\sqrt6.
\]
The value is finite because the matrix is still strictly SPD at the IC(0) breakdown boundary.

## Verification
The embedded `verify.py` uses exact rational arithmetic to replay the pivot recurrences for the classical Kershaw point
\[
t=\frac23
\]
and for a safe point
\[
t=\frac12.
\]
It confirms the squared-pivot sequences
\[
1,\frac59,\frac15,-\frac53
\]
for \(A(2/3)\), and
\[
1,\frac34,\frac23,\frac38
\]
for \(A(1/2)\). After scaling the first sequence by three it obtains the Kershaw pivots
\[
3,\frac53,\frac35,-5.
\]

The checker also verifies exactly that the fourth-pivot numerator vanishes at
\[
t^2=\frac13
\]
and numerically confirms the identity
\[
\frac{1+\sqrt{2/3}}
{1-\sqrt{2/3}}
=
5+2\sqrt6.
\]

The proof that dimensions at most three are safe is analytic and does not rely on finite enumeration.

## Relationship to prior work
Incomplete factorization breakdown is classical. Kershaw's work on incomplete Cholesky and incomplete LU methods raised and analyzed the problem of unstable or nonpositive pivots. A 1978 Lawrence Livermore report records this issue explicitly and develops pivot repair strategies.

Eijkhout's 1999 full survey of the existence problem states that incomplete factorizations can have zero or negative pivots even for symmetric positive-definite matrices. It reproduces Kershaw's \(4\times4\) SPD matrix
\[
\begin{pmatrix}
3&-2&0&2\\
-2&3&-2&0\\
0&-2&3&-2\\
2&0&-2&3
\end{pmatrix}
\]
and notes that its fourth ILU(0) pivot is negative. This historical witness is therefore not new.

The contribution here is the exact minimality and phase structure around that witness: all orders at most three are proved breakdown-free for IC(0), the Kershaw matrix is embedded in the natural signed-cycle family \(3A(t)\), the full SPD interval is separated from the positive-pivot interval, and the sharp Jacobi-scaled condition-number onset
\[
5+2\sqrt6
\]
is derived.

Later incomplete-Cholesky literature continues to treat breakdown avoidance as a practical issue. Lin and Moré's limited-memory incomplete Cholesky work is classified primarily under MSC 65F10 and 65F50. Modern robust-IC work gives larger explicit SPD examples in which dropped fill drives later pivots negative and discusses shifts and safeguards. These broader works establish the importance of breakdown control but do not imply the displayed signed-cycle phase diagram.

## Limitations
The condition-number threshold
\[
5+2\sqrt6
\]
is a theorem only for the displayed unit-diagonal signed four-cycle family. No claim is made that it is the smallest condition number permitting IC(0) breakdown among all four-dimensional SPD matrices.

The natural ordering is part of the statement. Symmetric reorderings can change which fill positions are dropped and can remove or create breakdown.

No finite-precision effects are analyzed. Overflow, underflow, loss of significance, and implementation-specific pivot tolerances are distinct failure modes.

The Kershaw counterexample itself is prior work. The new content is the all-\(n\le3\) safety theorem together with the complete one-parameter signed-cycle breakdown phase diagram and its sharp conditioning boundary.

## References
1. D. S. Kershaw, “Problem of unstable pivots in the incomplete LU-conjugate gradient method,” Lawrence Livermore Laboratory report UCRL-81103, June 19, 1978.
2. D. S. Kershaw, “The incomplete Cholesky—conjugate gradient method for the iterative solution of systems of linear equations,” Journal of Computational Physics 26 (1978), 43–65. DOI 10.1016/0021-9991(78)90098-0.
3. V. Eijkhout, “On the existence problem of incomplete factorisation methods,” LAPACK Working Note 144, UT-CS-99-435, December 1, 1999.
4. C.-J. Lin and J. J. Moré, “Incomplete Cholesky Factorizations with Limited Memory,” SIAM Journal on Scientific Computing 21 (1999), 24–45. DOI 10.1137/S1064827597327334.
5. J. Scott and M. Tůma, “Developing robust incomplete Cholesky factorizations in half precision arithmetic,” Numerical Algorithms (2025). DOI 10.1007/s11075-025-02015-x.
