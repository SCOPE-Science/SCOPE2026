# Three dimensions are minimal for Jacobi equilibration to worsen SPD conditioning

## Finding
For a real symmetric positive-definite matrix \(A\), write
\[
D=\operatorname{diag}(A)
\]
and define its symmetric Jacobi equilibration by
\[
J(A)=D^{-1/2}AD^{-1/2}.
\]
This scaling gives \(J(A)\) unit diagonal.

In dimensions one and two, Jacobi equilibration never increases the spectral condition number:
\[
\boxed{
\kappa_2(J(A))\le \kappa_2(A).
}
\]
Dimension three is the first dimension in which the inequality can reverse.

More strongly, for every prescribed
\[
\kappa>1
\]
there is a \(3\times3\) SPD matrix with condition number exactly \(\kappa\) whose Jacobi equilibration is strictly worse conditioned. Let
\[
u=(1,-2,-2)^{\mathsf T}
\]
and
\[
A_\kappa
=
I+\frac{\kappa-1}{9}uu^{\mathsf T}.
\]
Then
\[
\operatorname{spec}(A_\kappa)=\{1,1,\kappa\},
\]
while
\[
\boxed{
\kappa_2(J(A_\kappa))
=
\frac{
2\kappa+1+
2(\kappa-1)\sqrt{\frac{\kappa+2}{\kappa+8}}
}{3}
>
\kappa.
}
\]
The relative worsening in this family approaches
\[
\frac43:
\qquad
\frac{\kappa_2(J(A_\kappa))}{\kappa}
\longrightarrow
\frac43.
\]

At the integer example \(\kappa=10\),
\[
A=
\begin{pmatrix}
2&-2&-2\\
-2&5&4\\
-2&4&5
\end{pmatrix}
\]
has condition number \(10\), but its Jacobi equilibration has condition number
\[
7+2\sqrt6
=
11.898979485566\ldots.
\]

## Assumptions and scope
The matrix is real symmetric positive definite and the condition number is the spectral \(2\)-norm condition number. Jacobi equilibration means the symmetric congruence
\[
D^{-1/2}AD^{-1/2},
\qquad
D=\operatorname{diag}(A),
\]
not the generally nonsymmetric left-preconditioned matrix \(D^{-1}A\).

The dimension-two statement is universal. The dimension-three family proves minimal dimension and fixed-condition-number failure for every \(\kappa>1\), but it is not claimed to maximize the possible deterioration among all \(3\times3\) SPD matrices.

## Proof
For \(n=1\), the claim is immediate.

Let
\[
A=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix}
>0.
\]
Define
\[
\rho=\frac{|c|}{\sqrt{ab}}.
\]
Positive definiteness gives \(0\le\rho<1\), and
\[
J(A)=
\begin{pmatrix}
1&c/\sqrt{ab}\\
c/\sqrt{ab}&1
\end{pmatrix},
\]
so
\[
\kappa_2(J(A))
=
\frac{1+\rho}{1-\rho}.
\]

The eigenvalues of \(A\) are
\[
\frac{a+b}{2}
\left(
1\pm q
\right),
\qquad
q=
\frac{\sqrt{(a-b)^2+4c^2}}{a+b},
\]
hence
\[
\kappa_2(A)=\frac{1+q}{1-q}.
\]
A direct subtraction gives
\[
q^2-\rho^2
=
\frac{
(a-b)^2(ab-c^2)
}{
ab(a+b)^2
}
\ge0.
\]
Therefore \(q\ge\rho\), and the function
\[
t\longmapsto\frac{1+t}{1-t}
\]
is increasing on \([0,1)\). This proves
\[
\kappa_2(J(A))\le\kappa_2(A).
\]
Because \(ab-c^2>0\), equality occurs exactly when \(a=b\).

Now take
\[
A_\kappa
=
I+suu^{\mathsf T},
\qquad
s=\frac{\kappa-1}{9},
\qquad
u=(1,-2,-2)^{\mathsf T}.
\]
Since
\[
\|u\|_2^2=9,
\]
the rank-one update has eigenvalues
\[
1,\ 1,\ 1+9s=\kappa.
\]

Its diagonal is
\[
D=
\operatorname{diag}
\left(
\frac{\kappa+8}{9},
\frac{4\kappa+5}{9},
\frac{4\kappa+5}{9}
\right).
\]
The symmetry between the last two coordinates shows that
\[
(0,1,-1)^{\mathsf T}
\]
is an eigenvector of \(J(A_\kappa)\) with eigenvalue
\[
\lambda_0=\frac{9}{4\kappa+5}.
\]

On the orthogonal subspace spanned by the first coordinate and
\[
(0,1,1)^{\mathsf T}/\sqrt2,
\]
the remaining two eigenvalues are
\[
\lambda_\pm
=
\frac{3}{4\kappa+5}
\left(
2\kappa+1
\pm
2(\kappa-1)
\sqrt{\frac{\kappa+2}{\kappa+8}}
\right).
\]
Moreover,
\[
\lambda_- - \lambda_0
=
\frac{
6(\kappa-1)
}{
4\kappa+5
}
\left(
1-\sqrt{\frac{\kappa+2}{\kappa+8}}
\right)
>0.
\]
Thus \(\lambda_0\) is the smallest eigenvalue and \(\lambda_+\) is the largest. Their ratio is
\[
\kappa_2(J(A_\kappa))
=
\frac{
2\kappa+1+
2(\kappa-1)\sqrt{\frac{\kappa+2}{\kappa+8}}
}{3}.
\]

Subtracting \(\kappa\) gives
\[
\frac{\kappa-1}{3}
\left(
2\sqrt{\frac{\kappa+2}{\kappa+8}}-1
\right).
\]
The parenthesis is positive because
\[
4(\kappa+2)>\kappa+8
\]
for every \(\kappa>0\). Therefore every \(\kappa>1\) yields strict worsening.

Finally,
\[
\sqrt{\frac{\kappa+2}{\kappa+8}}\longrightarrow1,
\]
so
\[
\frac{\kappa_2(J(A_\kappa))}{\kappa}
\longrightarrow\frac43.
\]

For \(\kappa=10\), the matrix becomes the displayed integer example. The three Jacobi-scaled eigenvalues reduce to
\[
\frac15,
\qquad
\frac{7-2\sqrt6}{5},
\qquad
\frac{7+2\sqrt6}{5},
\]
which gives the exact condition number
\[
7+2\sqrt6.
\]

## Verification
The embedded `verify.py` uses exact rational arithmetic for the two-dimensional comparison identity and for the \(\kappa=10\) rank-one family. It verifies the eigenvalue structure of the unscaled integer example through the rank-one identity, checks the generalized eigenvalue relations for its Jacobi scaling, and numerically evaluates the closed family formula at representative condition numbers.

These checks replay consequences of the proof. The all-\(\kappa\) and all-\(2\times2\) statements are analytic and do not depend on finite enumeration.

## Relationship to prior work
Diagonal equilibration is classical. Van der Sluis studied condition numbers and equilibration and proved, for positive-definite Hermitian matrices with equal diagonal, that the resulting symmetric scaling is within a dimension-dependent factor of the best symmetric diagonal scaling. His theorem motivates equal-diagonal scaling as reasonably near-optimal but does not assert that it always improves the condition number relative to the unscaled matrix.

Braatz and Morari later solved Euclidean condition-number minimization under diagonal row and column scaling through convex optimization and emphasized the numerical importance of condition-reducing scalings. Their work concerns optimal diagonal scaling rather than the exact low-dimensional behavior of the Jacobi choice.

The result here isolates a different comparison: Jacobi equilibration versus doing no scaling at all. It proves universal safety through dimension two and gives a three-dimensional fixed-\(\kappa\) obstruction for every nontrivial condition number. Targeted searches for unit-diagonal scaling, Jacobi equilibration, minimal dimension, and fixed-condition-number worsening did not locate an implication-equivalent theorem.

## Limitations
The three-dimensional family is an obstruction family, not a proof of the largest possible Jacobi-induced deterioration at fixed \(\kappa\). In particular, the asymptotic factor \(4/3\) is a property of this family and is not claimed as a global sharp upper bound.

The theorem concerns symmetric Jacobi equilibration of SPD matrices. Nonsymmetric matrices, one-sided row scaling, block-Jacobi scaling, and condition numbers in other norms can behave differently.

The literature comparison leaves a residual risk that an older matrix-scaling source contains the same \(2\times2\) monotonicity observation or an equivalent three-dimensional counterexample under different notation.

## References
1. A. van der Sluis, “Condition Numbers and Equilibration of Matrices,” Numerische Mathematik 14 (1969), 14–23. DOI 10.1007/BF02165096.
2. R. D. Braatz and M. Morari, “Minimizing the Euclidean Condition Number,” SIAM Journal on Control and Optimization 32 (1994), 1763–1768. DOI 10.1137/S0363012992238680.
