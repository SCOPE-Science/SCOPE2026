# Sharp condition-number frontier for row swaps in partially pivoted Gaussian elimination

## Finding
Let
\[
A\in\mathbb R^{n\times n}
\]
be symmetric positive definite and let
\[
\kappa
=
\kappa_2(A)
=
\frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}.
\]
Run ordinary Gaussian elimination in the natural order without row swaps. At stage \(k\), write the multiplier used to eliminate row \(i>k\) as
\[
m_{ik}^{(k)}
=
\frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}.
\]
Then every multiplier satisfies the sharp bound
\[
\boxed{
|m_{ik}^{(k)}|
\le
\frac{\kappa-1}{2\sqrt{\kappa}}.
}
\]

Therefore the exact condition-number frontier at which partial pivoting can first be forced to swap an SPD system is
\[
\boxed{
\kappa_*
=
3+2\sqrt2.
}
\]
If
\[
\kappa<\kappa_*,
\]
the current diagonal is strictly the largest-magnitude entry in every active pivot column, so Gaussian elimination with partial pivoting performs no row interchange. With a tie rule that retains the current row, this remains true at
\[
\kappa=\kappa_*.
\]

The threshold is sharp in dimension two. For every \(\kappa>1\), define
\[
A_\kappa
=
\begin{pmatrix}
2\kappa & (\kappa-1)\sqrt{\kappa}\\
(\kappa-1)\sqrt{\kappa} & \kappa^2+1
\end{pmatrix}.
\]
Its eigenvalues are
\[
\kappa+1
\quad\text{and}\quad
\kappa(\kappa+1),
\]
and
\[
\frac{|(A_\kappa)_{21}|}{(A_\kappa)_{11}}
=
\frac{\kappa-1}{2\sqrt{\kappa}}.
\]
Thus at \(\kappa=\kappa_*\) the first pivot column has an exact tie, while every \(\kappa>\kappa_*\) makes the subdiagonal entry strictly larger and forces a row swap.

A rational witness is
\[
A_9
=
\begin{pmatrix}
18&24\\
24&82
\end{pmatrix}.
\]
Its eigenvalues are \(10\) and \(90\), so
\[
\kappa_2(A_9)=9,
\]
yet the first elimination multiplier is
\[
\frac{24}{18}
=
\frac43>1.
\]
Hence partial pivoting swaps the two rows even though the matrix is SPD and unpivoted Gaussian elimination is perfectly well-defined.

## Assumptions and scope
The statement is in exact arithmetic. The matrix is real, symmetric, and positive definite.

“Partial pivoting” means the classical column rule that chooses an entry of maximal magnitude in the active pivot column. The strict result
\[
\kappa<3+2\sqrt2
\]
is independent of tie policy. At equality, whether an actual interchange is performed depends on the implementation's tie convention.

The theorem distinguishes two different facts. Positive definiteness already guarantees that unpivoted Gaussian elimination exists and is stable in the classical growth-factor sense. The new classification asks when a generic partial-pivoting implementation is guaranteed to discover that no row interchange is needed merely from a spectral condition-number bound.

The theorem does not claim that partially pivoted LU is preferable to Cholesky on recognized SPD matrices. Cholesky remains the natural structure-preserving factorization.

## Proof
Put
\[
\mu=\lambda_{\min}(A),
\qquad
L=\lambda_{\max}(A).
\]
Consider any leading Schur complement occurring in unpivoted elimination. Write the current partition as
\[
A=
\begin{pmatrix}
B&C\\
C^{\mathsf T}&D
\end{pmatrix},
\qquad
S=D-C^{\mathsf T}B^{-1}C.
\]
For every vector \(y\),
\[
y^{\mathsf T}Sy
=
\min_x
\begin{pmatrix}
x\\y
\end{pmatrix}^{\mathsf T}
A
\begin{pmatrix}
x\\y
\end{pmatrix}.
\]
Since
\[
\mu I\preceq A\preceq LI,
\]
the lower bound is
\[
y^{\mathsf T}Sy
\ge
\mu\|y\|_2^2.
\]
For the upper bound, choose \(x=0\):
\[
y^{\mathsf T}Sy
\le
\begin{pmatrix}
0\\y
\end{pmatrix}^{\mathsf T}
A
\begin{pmatrix}
0\\y
\end{pmatrix}
\le
L\|y\|_2^2.
\]
Thus every active Schur complement obeys
\[
\mu I\preceq S\preceq LI.
\]

Fix one stage and one row below the pivot. The corresponding \(2\times2\) principal block of \(S\) is SPD. Let its eigenvalues be
\[
0<\lambda\le\Lambda
\]
and put
\[
q=\frac{\Lambda}{\lambda}.
\]
Interlacing with the spectral enclosure gives
\[
q\le\kappa.
\]

After scaling by \(\lambda\) and rotating the eigenbasis by an angle \(\theta\), the block has first diagonal and off-diagonal entries
\[
a
=
\cos^2\theta
+
q\sin^2\theta,
\]
and
\[
|b|
=
(q-1)|\sin\theta\cos\theta|.
\]
Let
\[
t=|\tan\theta|.
\]
Then
\[
\frac{|b|}{a}
=
\frac{(q-1)t}{1+qt^2}.
\]
Differentiation gives
\[
\frac{d}{dt}
\frac{(q-1)t}{1+qt^2}
=
\frac{(q-1)(1-qt^2)}{(1+qt^2)^2}.
\]
Hence the unique maximum occurs at
\[
t=\frac1{\sqrt q},
\]
and the maximum value is
\[
\frac{q-1}{2\sqrt q}.
\]
Because
\[
\frac{q-1}{2\sqrt q}
=
\frac12
\left(
\sqrt q-\frac1{\sqrt q}
\right)
\]
is increasing for \(q\ge1\),
\[
\frac{|b|}{a}
\le
\frac{\kappa-1}{2\sqrt\kappa}.
\]
This is exactly the asserted multiplier bound.

Now
\[
\frac{\kappa-1}{2\sqrt\kappa}<1
\]
is equivalent to
\[
\sqrt\kappa<1+\sqrt2,
\]
or
\[
\kappa<3+2\sqrt2.
\]
Therefore, as long as no previous row interchange has occurred, every subdiagonal entry in the current pivot column is strictly smaller in modulus than the diagonal pivot. Partial pivoting leaves the row in place. Induction over the elimination stages proves that no interchange ever occurs.

For sharpness, choose the \(2\times2\) family
\[
A_\kappa
=
\begin{pmatrix}
2\kappa & (\kappa-1)\sqrt{\kappa}\\
(\kappa-1)\sqrt{\kappa} & \kappa^2+1
\end{pmatrix}.
\]
Its trace and determinant are
\[
(\kappa+1)^2
\quad\text{and}\quad
\kappa(\kappa+1)^2,
\]
so its eigenvalues are
\[
\kappa+1
\quad\text{and}\quad
\kappa(\kappa+1).
\]
Its first multiplier attains the bound exactly. This gives a tie at
\[
\kappa=3+2\sqrt2
\]
and a forced first swap for every larger condition number.

## Verification
The embedded `verify.py` checks the exact rational witness
\[
A_9
=
\begin{pmatrix}
18&24\\
24&82
\end{pmatrix}.
\]
It verifies
\[
\operatorname{tr}(A_9)=100,
\qquad
\det(A_9)=900,
\]
so the eigenvalues are \(10\) and \(90\), and it verifies the exact multiplier
\[
\frac{24}{18}=\frac43.
\]

The checker also verifies to high precision that
\[
\kappa_*=3+2\sqrt2
\]
makes
\[
\frac{\kappa_*-1}{2\sqrt{\kappa_*}}=1,
\]
and that the bound is below one for a representative condition number below the frontier.

Finite checks are corroborative only. The dimension-free multiplier bound and the no-swap theorem are established analytically in the proof.

## Relationship to prior work
Classical Gaussian-elimination theory already provides three pieces of background. Partial pivoting selects an entry of maximal magnitude in the active pivot column and therefore bounds the resulting multipliers by one. Symmetric positive definite matrices admit Gaussian elimination without pivoting, and their classical element-growth factor is one. These facts are standard and are explicitly summarized by Higham.

Broyden studied condition-number bounds for Gaussian elimination and defined a matrix to be “partially pivoted” when the partial-pivoting rules require no row interchanges. His full paper bounds conditioning of triangular factors and analyzes the effect of the multiplier restriction imposed by partial pivoting. It does not specialize this no-interchange property to SPD matrices using the spectral condition number, nor does it state the sharp threshold above.

Higham and Higham study extremal growth factors under partial and complete pivoting and give the classical maximal-column description of partial pivoting. Their full paper does not contain an SPD specialization of the present condition-number frontier.

The contribution here is the exact bridge between the SPD spectral condition number and the actual row-permutation behavior of generic partial pivoting:
\[
|m_{ik}^{(k)}|
\le
\frac{\kappa-1}{2\sqrt\kappa},
\]
with equality already in dimension two, and the resulting sharp row-swap frontier
\[
\kappa_*=3+2\sqrt2.
\]
Targeted searches using Gaussian elimination, partial pivoting, SPD matrices, multiplier bounds, row interchanges, and the displayed constants did not locate an implication-equivalent statement.

## Limitations
The result is an exact-arithmetic structural theorem. It does not quantify the effect of floating-point comparison errors near the boundary.

At the boundary
\[
\kappa=3+2\sqrt2,
\]
a maximum-magnitude tie can occur. An implementation that swaps on a tie can therefore permute even though a diagonal-retaining implementation need not.

The theorem uses the spectral condition number. Diagonal scaling can substantially alter both condition number and pivot decisions, so a separate scale-invariant classification would require different hypotheses.

The result concerns row swaps under ordinary scalar partial pivoting. Threshold pivoting, rook pivoting, complete pivoting, block pivoting, and sparse fill-reducing permutations are different policies.

Recognized SPD problems are normally solved by Cholesky factorization; the value of the theorem is the sharp classification of when a general GEPP rule collapses automatically to the unpivoted path.

## References
1. C. G. Broyden, “Some Condition-Number Bounds for the Gaussian Elimination Process,” Journal of the Institute of Mathematics and its Applications 12 (1973), 273–286. DOI 10.1093/imamat/12.3.273.
2. N. J. Higham and D. J. Higham, “Large Growth Factors in Gaussian Elimination with Pivoting,” SIAM Journal on Matrix Analysis and Applications 10 (1989), 155–164. DOI 10.1137/0610012. Public MIMS EPrint 2006.174.
3. N. J. Higham, “Gaussian Elimination,” Wiley Interdisciplinary Reviews: Computational Statistics 3 (2011), 230–238. DOI 10.1002/wics.164.
