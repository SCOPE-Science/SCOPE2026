# Exact nearest-neighbor Shapiro doubling on finite cycles
## Finding
For every integer \(n\ge 5\), let
\[
G=\mathbb Z/n\mathbb Z,\qquad U=\{0,\pm1\}.
\]
The two-fold sumset is
\[
2U=\{0,\pm1,\pm2\}.
\]
For the Shapiro extremal quantity of Gaál and Révész,
\[
Q(U,2)=
\sup_{\substack{f:G\to\mathbb R\\ f\ge0,\ f\ {\rm positive\ definite}\\ f\not\equiv0}}
\frac{\sum_{j\in2U}f(j)}{\sum_{j\in U}f(j)},
\]
the exact value is
\[
Q(U,2)=
\begin{cases}
3,&n\ {\rm even},\\[4pt]
4\cos(\pi/n)-1,&n\ {\rm odd}.
\end{cases}
\]
Thus odd cycles have a strict parity defect,
\[
3-Q(U,2)=4\bigl(1-\cos(\pi/n)\bigr)
=\frac{2\pi^2}{n^2}+O(n^{-4}),
\]
whereas every even cycle attains the universal elementary ceiling \(3\).

## Assumptions and scope
Positive definiteness is taken in the usual finite-group sense: the discrete Fourier transform of \(f\) is nonnegative. Since \(f\ge0\), every admissible \(f\) is real and even. The statement concerns exactly the nearest-neighbor neighborhood \(U=\{0,\pm1\}\) and the two-fold sumset \(2U\); no formula is asserted for larger neighborhoods or higher dilations.

Put
\[
c_n=
\begin{cases}
1,&n\ {\rm even},\\
\cos(\pi/n),&n\ {\rm odd},
\end{cases}
\qquad C_n=4c_n-1.
\]

## Proof
It suffices to prove
\[
\sum_{j\in2U}f(j)\le C_n\sum_{j\in U}f(j)
\]
for every admissible \(f\), and then exhibit equality.

Define the even signed function
\[
h=C_n1_U-1_{2U}.
\]
Its only nonzero coefficients are
\[
h(0)=C_n-1,\qquad h(\pm1)=C_n-1,\qquad h(\pm2)=-1.
\]
Set
\[
\sigma=(6c_n-4)(\delta_1+\delta_{-1})
\]
and \(\tau=h-\sigma\). Since \(n\ge5\), one has \(c_n\ge\cos(\pi/5)>2/3\), so \(\sigma\ge0\). Directly,
\[
\tau(0)=4c_n-2,\qquad
\tau(\pm1)=2(1-c_n),\qquad
\tau(\pm2)=-1.
\]

For a character indexed by \(k\), write
\[
x_k=\cos(2\pi k/n).
\]
The Fourier transform of \(\tau\) is
\[
\widehat\tau(k)
=
4c_n+4(1-c_n)x_k-4x_k^2
=
4(1-x_k)(x_k+c_n).
\]
By the definition of \(c_n\), the smallest cosine among the \(n\)-th roots of unity is \(-c_n\). Hence
\[
-\,c_n\le x_k\le1
\]
for every \(k\), and therefore \(\widehat\tau(k)\ge0\). Thus \(\tau\) is of positive type.

For every admissible \(f\),
\[
\sum_j f(j)h(j)
=
\sum_j f(j)\sigma(j)+\sum_j f(j)\tau(j)\ge0.
\]
The first term is nonnegative because both factors are nonnegative. The second is nonnegative by Fourier positivity of both \(f\) and \(\tau\). Therefore
\[
\sum_{j\in2U}f(j)\le C_n\sum_{j\in U}f(j).
\]

For sharpness, let \(q=\lfloor n/2\rfloor\) and define
\[
f_*(j)=\frac{c_n+\cos(2\pi qj/n)}{1+c_n}.
\]
Its Fourier coefficients are nonnegative, so \(f_*\) is positive definite. Moreover,
\[
\cos(2\pi qj/n)\ge-c_n
\]
for every \(j\), so \(f_*\ge0\). Since
\[
\cos(2\pi q/n)=-c_n,
\]
we have \(f_*(0)=1\) and \(f_*(\pm1)=0\). Also,
\[
f_*(\pm2)=2c_n-1.
\]
Consequently
\[
\frac{\sum_{j\in2U}f_*(j)}{\sum_{j\in U}f_*(j)}
=
1+2(2c_n-1)=4c_n-1=C_n.
\]
This proves the formula.

## Verification
The accompanying `verify.py` independently evaluates the proposed witness and the dual Fourier certificate for every \(5\le n\le400\). It checks nonnegativity of the witness, nonnegativity of every Fourier value
\[
4(1-x_k)(x_k+c_n),
\]
and agreement of the attained ratio with the closed formula. It prints `VERIFY_OK`.

The finite replay is not used to prove the theorem. The universal proof is the explicit dual decomposition \(h=\sigma+\tau\) and the closed-form extremizer above.

## Relationship to prior work
Gaál and Révész define \(Q(U,k)\) on general locally compact Abelian groups and prove a dual characterization of the associated Shapiro comparison constants. Their paper contains no finite-cyclic nearest-neighbor evaluation and no parity formula of the form above.

Gorbachev and Tikhonov study doubling constants for nonnegative positive-definite functions on Euclidean symmetric convex bodies. Their setting motivates the local doubling question but does not contain this finite-cycle result.

The Lovász theta number of an odd cycle has the classical value
\[
\vartheta(C_n)=\frac{n\cos(\pi/n)}{1+\cos(\pi/n)}.
\]
That problem imposes zero constraints on graph edges and optimizes a global matrix sum. The present Shapiro problem instead optimizes a five-point to three-point local mass ratio over all nonnegative positive-definite functions, allowing nonzero neighbor values. The displayed dual certificate is specific to this local ratio; the theta-cycle formula by itself does not imply the claimed inequality.

Targeted searches for the exact expression \(4\cos(\pi/n)-1\), the three-point/five-point cyclic comparison, and finite-cyclic Shapiro doubling found no covering statement.

## Limitations
The theorem is restricted to \(n\ge5\), where \(0,\pm1,\pm2\) have the expected multiplicities in \(2U\). It does not classify all extremizers. Search non-detection does not exclude an unindexed or differently phrased equivalent result.

## References
1. M. Gaál and S. Gy. Révész, "Integral comparisons of nonnegative positive definite functions on LCA groups," arXiv:1803.06409, first posted 16 March 2018.
2. D. Gorbachev and S. Tikhonov, "Doubling condition at the origin for non-negative positive definite functions," arXiv:1612.08637.
3. L. Lovász, "On the Shannon capacity of a graph," IEEE Transactions on Information Theory 25 (1979), 1--7.
