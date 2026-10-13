# A sharp max-entry transient law for maximum-pivot Jacobi diagonalization
## Finding
Let
\[
A=A^{\mathsf T}\in\mathbb R^{n\times n}
\]
and perform one classical maximum-pivot Jacobi eigenvalue rotation. Thus \((p,q)\) is chosen so that
\[
m=|a_{pq}|=\max_{i<j}|a_{ij}|>0,
\]
and the Jacobi plane rotation annihilates \(a_{pq}\).

Define the second-largest off-diagonal magnitude
\[
s=
\max_{\substack{i<j\\(i,j)\ne(p,q)}}|a_{ij}|,
\]
with \(s=0\) when \(n=2\), and put
\[
\tau=\frac{s}{m}.
\]
If
\[
m^+=\max_{i<j}|a^+_{ij}|
\]
denotes the largest off-diagonal magnitude after the rotation, then
\[
\boxed{
m^+\le\sqrt2\,s
}
\]
and therefore
\[
\boxed{
\frac{m^+}{m}\le\sqrt2\,\tau.
}
\]

Consequently the exact universal gap condition for guaranteed one-step max-entry nonincrease is
\[
\boxed{
\tau\le\frac1{\sqrt2}.
}
\]

The constant is sharp even after fixing the spectral condition number. For every
\[
\kappa>1
\]
and every
\[
0<\tau<1,
\]
there is a \(3\times3\) SPD matrix of condition number exactly \(\kappa\), with a unique maximum pivot and second-largest-to-pivot ratio exactly \(\tau\), for which
\[
\frac{m^+}{m}
=
\sqrt2\,\tau.
\]

An explicit family is
\[
A_{\kappa,\tau}
=
cI+
\begin{pmatrix}
0&1&\tau\\
1&0&-\tau\\
\tau&-\tau&0
\end{pmatrix},
\]
where
\[
D=\sqrt{1+8\tau^2},
\qquad
\beta_-=\frac{-1-D}{2},
\qquad
c=\frac{1-\kappa\beta_-}{\kappa-1}.
\]
The first Jacobi rotation leaves exactly one off-diagonal entry, of magnitude
\[
\sqrt2\,\tau.
\]
The next maximum-pivot rotation diagonalizes the matrix exactly.

Thus whenever
\[
\tau>\frac1{\sqrt2},
\]
the largest off-diagonal entry can increase strictly even though the classical total off-diagonal Frobenius energy decreases at the same step. The spike can be made arbitrarily close to the universal factor
\[
\sqrt2
\]
while the pivot remains unique.

## Assumptions and scope
The result concerns exact arithmetic and the classical two-sided Jacobi eigenvalue method for real symmetric matrices.

A maximum-pivot step means that an off-diagonal entry of largest magnitude is selected and an orthogonal plane rotation is chosen to annihilate that entry. The upper bound applies to every such step, including ties.

The sharpness family is positive definite and allows an arbitrary prescribed spectral condition number
\[
\kappa>1.
\]
The condition-number statement is therefore not an asymptotic large-conditioning construction.

The monitored quantity is the largest individual off-diagonal magnitude. This is distinct from the standard aggregate off-diagonal Frobenius measure, which decreases monotonically under Jacobi rotations.

No finite-precision or pivot-search complexity claim is made.

## Proof
Let the Jacobi rotation in the \((p,q)\)-plane have cosine \(c_\theta\) and sine \(s_\theta\). For every
\[
k\notin\{p,q\},
\]
the pair of off-diagonal entries touching the pivot coordinates transforms by a two-dimensional orthogonal map:
\[
\begin{pmatrix}
a^+_{pk}\\
a^+_{qk}
\end{pmatrix}
=
R_\theta
\begin{pmatrix}
a_{pk}\\
a_{qk}
\end{pmatrix}.
\]
Hence
\[
|a^+_{pk}|^2+|a^+_{qk}|^2
=
|a_{pk}|^2+|a_{qk}|^2.
\]
Because every nonpivot off-diagonal entry has magnitude at most \(s\),
\[
|a_{pk}|\le s,
\qquad
|a_{qk}|\le s.
\]
Therefore each transformed component satisfies
\[
|a^+_{pk}|,
|a^+_{qk}|
\le
\sqrt{|a_{pk}|^2+|a_{qk}|^2}
\le
\sqrt2\,s.
\]

Every off-diagonal entry whose two indices avoid \(p\) and \(q\) is unchanged, hence remains at most \(s\). The pivot itself is annihilated. Thus
\[
m^+
\le
\sqrt2\,s,
\]
which proves the universal bound and the nonincrease guarantee
\[
\tau\le\frac1{\sqrt2}.
\]

It remains to prove sharpness with an arbitrary prescribed condition number. Put
\[
B_\tau=
\begin{pmatrix}
0&1&\tau\\
1&0&-\tau\\
\tau&-\tau&0
\end{pmatrix},
\qquad
0<\tau<1.
\]
The pivot \(b_{12}=1\) is unique in magnitude, and the other two off-diagonal entries both have magnitude \(\tau\).

Use the orthogonal matrix
\[
Q=
\begin{pmatrix}
1/\sqrt2&1/\sqrt2&0\\
-1/\sqrt2&1/\sqrt2&0\\
0&0&1
\end{pmatrix}.
\]
Direct multiplication gives
\[
Q^{\mathsf T}B_\tau Q
=
\begin{pmatrix}
-1&0&\sqrt2\,\tau\\
0&1&0\\
\sqrt2\,\tau&0&0
\end{pmatrix}.
\]
This is exactly the Jacobi rotation that diagonalizes the leading \(2\times2\) pivot block. Therefore the first-step maximum is
\[
m^+=\sqrt2\,\tau,
\]
and equality holds in the universal bound.

The eigenvalues of \(B_\tau\) are
\[
1,
\qquad
\frac{-1+\sqrt{1+8\tau^2}}2,
\qquad
\beta_-=
\frac{-1-\sqrt{1+8\tau^2}}2.
\]
Since
\[
0<\tau<1,
\]
the largest eigenvalue is \(1\) and the smallest is \(\beta_-<0\).

For a prescribed
\[
\kappa>1,
\]
set
\[
c=
\frac{1-\kappa\beta_-}{\kappa-1}.
\]
Then
\[
c+\beta_-
=
\frac{1-\beta_-}{\kappa-1}>0,
\]
so
\[
A_{\kappa,\tau}=cI+B_\tau
\]
is SPD. Moreover
\[
\frac{\lambda_{\max}(A_{\kappa,\tau})}
{\lambda_{\min}(A_{\kappa,\tau})}
=
\frac{c+1}{c+\beta_-}
=
\kappa.
\]
Adding a scalar multiple of the identity does not change any off-diagonal entry or the Jacobi angle, so the same equality
\[
m^+=\sqrt2\,\tau m
\]
holds at condition number exactly \(\kappa\).

After the first rotation, coordinate \(2\) is decoupled and the only remaining off-diagonal entry is the \((1,3)\) entry. A second maximum-pivot rotation therefore diagonalizes the remaining \(2\times2\) block exactly.

Finally, when \(n=2\), a single Jacobi rotation diagonalizes every real symmetric matrix. Thus dimension three is minimal for a max-entry spike.

## Verification
The embedded `verify.py` uses high-precision arithmetic to reconstruct the sharp family, its spectrum, the prescribed condition number, and the Jacobi-transformed matrix.

For the representative values
\[
\tau=\frac34,
\qquad
\kappa=2,
\]
the checker confirms a unique pivot of magnitude \(1\), second-largest magnitude \(3/4\), and first-step maximum
\[
\frac{3\sqrt2}{4}>1.
\]
It also verifies that the shifted matrix is SPD with condition number \(2\), and that the transformed matrix has only one nonzero off-diagonal pair.

The universal upper bound is analytic. Finite replay is supporting evidence only.

## Relationship to prior work
The maximum-element Jacobi strategy and monotone decrease of the aggregate off-diagonal measure are classical. Modern descriptions state that Jacobi's original strategy annihilates the largest remaining off-diagonal element at every rotation. Standard convergence arguments use the identity that the sum of squared off-diagonal entries decreases by exactly twice the squared pivot magnitude.

Hari proves global convergence for a broad block-oriented quasi-cyclic Jacobi method for symmetric matrices and places the Jacobi eigenvalue problem under primary MSC \(65F15\). Matejaš proves sharp eigenvalue perturbation bounds arising from a single Jacobi step for scaled diagonally dominant symmetric matrices. These convergence and perturbation results are prior work.

The finding here concerns a different local diagnostic: the largest individual off-diagonal magnitude immediately after a maximum-pivot rotation. The aggregate off-diagonal energy can decrease while the maximum entry increases, because the rotation can combine two near-largest nonpivot entries into one component. The theorem quantifies that mechanism by the exact gap threshold
\[
\frac1{\sqrt2},
\]
proves the sharp amplification factor
\[
\sqrt2\,\tau,
\]
and shows that the obstruction persists at every prescribed SPD condition number greater than one, with exact diagonalization on the following rotation.

Targeted searches under maximum-element Jacobi pivoting, largest off-diagonal transients, max-entry norms, and one-step growth did not locate this sharp statement.

## Limitations
The result classifies a single maximum-pivot rotation, not an entire sweep or the number of rotations required for a tolerance.

The maximum-entry diagnostic is not the classical Jacobi Lyapunov function. The aggregate off-diagonal Frobenius measure still decreases at every nontrivial rotation.

The sharp family is three-dimensional. In higher dimensions the same one-step upper bound remains valid, but subsequent pivot dynamics can be more complicated.

Older Jacobi literature is extensive, and an equivalent elementary max-entry inequality may exist under different terminology. This remains the principal originality risk.

## References
1. V. Hari, “Convergence of a Block-Oriented Quasi-Cyclic Jacobi Method,” SIAM Journal on Matrix Analysis and Applications 29 (2007), 349–369. DOI 10.1137/05064552X.
2. J. Matejaš, “Accuracy of the Jacobi Method on Scaled Diagonally Dominant Symmetric Matrices,” SIAM Journal on Matrix Analysis and Applications 31 (2009), 133–153. DOI 10.1137/070685993.
3. G. A. Valdiviesso, “The Case for Adopting the Sequential Jacobi’s Diagonalization Algorithm in Neutrino Oscillation Physics,” Symmetry 16 (2024), 1617. DOI 10.3390/sym16121617.
