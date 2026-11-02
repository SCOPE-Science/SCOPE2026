# A sharp fourth-moment instability threshold for entry-sampled Gauss–Seidel on orthogonal systems

## Finding

A well-conditioned linear system can be solved almost surely and in mean square by entry-sampled Gauss–Seidel while its fourth error moment grows exponentially. There is an exact, nontrivial threshold in the relative size of the matrix entries.

Fix \(0<r\le1\), and consider
\[
 A_r=\begin{pmatrix}1&r\\r&-1\end{pmatrix},\qquad A_rx=0.
\]
The eigenvalues of the symmetric matrix \(A_r\) are \(\pm\sqrt{1+r^2}\); in particular \(A_r^{\mathsf T}A_r=(1+r^2)I\) and \(\kappa_2(A_r)=1\) for every \(r\).

Use the entry-sampled doubly stochastic Gauss–Seidel iteration of Razaviyayn–Hong–Reyhanian–Luo, with independent samples, \(\alpha=1/2\), and
\[
\mathbb P\{(i,j)\}=\frac{a_{ij}^2}{\|A_r\|_F^2},\qquad
x_{k+1}=x_k-\frac{(A_rx_k)_i}{2a_{ij}}e_j.
\]
All four entries of \(A_r\) are nonzero for the stated range.

**Theorem.** Let \(r_*\) be the exact algebraic constant
\[
 r_* =\sqrt{\frac{47-2\sqrt{546}}5}=0.230960697006\ldots.
\]
For every deterministic \(x_0\ne0\),
\[
\mathbb E\|x_k\|_2^2=\left(\frac34\right)^k\|x_0\|_2^2,
\qquad x_k\longrightarrow0\quad\text{almost surely}.
\]
Nevertheless, with \(\lambda_r\) defined exactly below, the fourth moment satisfies
\[
 \mathbb E\|x_k\|_2^4=\Theta_{r,x_0}(\lambda_r^k).
\]
It grows exponentially if \(0<r<r_*\), stays bounded above and away from zero if \(r=r_*\), and tends to zero exponentially if \(r_*<r\le1\). In particular at \(r=1/5\), \(\lambda_r\approx1.16011022646\) while the squared error contracts at exactly \(3/4\) per iteration.

## Assumptions and scope

The problem is the homogeneous, consistent, real two-dimensional system displayed above. The entry sample is drawn independently anew at every step, proportional to its squared coefficient magnitude. The step size is fixed at \(1/2\). Moments are taken only over the sequence of entry samples. All claims concern exact arithmetic and arbitrary nonzero deterministic initial vectors. The fourth-moment exponent is a spectral radius of a finite, explicitly specified operator; the theorem does not claim a limiting stationary distribution.

## Proof

**1. Exact second moment and almost-sure convergence.** For arbitrary deterministic \(x\), put \(F=\|A_r\|_F^2=2(1+r^2)\). Expanding the update and averaging over all four entries gives
\[
\begin{aligned}
\mathbb E[\|x^+\|_2^2\mid x]
 &=\|x\|_2^2-\frac{2\alpha}{F}\|A_rx\|_2^2
   +\frac{2\alpha^2}{F}\|A_rx\|_2^2\\
 &=\bigl(1-\alpha+\alpha^2\bigr)\|x\|_2^2
 =\frac34\|x\|_2^2,
\end{aligned}
\]
where \(\alpha=1/2\) and \(\|A_rx\|_2^2=(1+r^2)\|x\|_2^2\). Iteration proves the second-moment identity. Markov's inequality and the first Borel–Cantelli lemma give \(x_k\to0\) almost surely.

**2. The exact quartic transfer.** Let \(\mathcal L f(x)=\mathbb E[f(x^+)\mid x]\). The four update matrices are
\[
\begin{aligned}
M_{11}&=\begin{pmatrix}1/2&-r/2\\0&1\end{pmatrix},
&M_{12}&=\begin{pmatrix}1&0\\-1/(2r)&1/2\end{pmatrix},\\
M_{21}&=\begin{pmatrix}1/2&1/(2r)\\0&1\end{pmatrix},
&M_{22}&=\begin{pmatrix}1&0\\r/2&1/2\end{pmatrix}.
\end{aligned}
\]
Their respective probabilities are \(1/[2(1+r^2)]\), \(r^2/[2(1+r^2)]\), \(r^2/[2(1+r^2)]\), \(1/[2(1+r^2)]\).

Rotation by a right angle permutes the four transitions with their probabilities. Thus the three-dimensional space of rotation-invariant homogeneous quartics is invariant. In the ordered polynomial basis
\[
 P=x_1^4+x_2^4,\qquad
 Q=x_1^3x_2-x_1x_2^3,\qquad R=x_1^2x_2^2,
\]
write \(\mathcal L (P,Q,R)=(P,Q,R)C_r\). Direct polynomial expansion gives
\[
 C_r=\begin{pmatrix}
 (r^4+16r^2+1)/(32r^2)&(1-r^2)/(16r)&1/8\\
 (r^2-1)/(8r)&1/8&0\\
 3/8&0&1/4
 \end{pmatrix}.
\]
Consequently, for any \(k\ge0\), \(\mathbb E[P(x_k)]=(P,Q,R)(x_0)C_r^k e_1\). Direct expansion also yields
\[
 \det(I-C_r)=-\frac{3(5r^4-94r^2+5)}{1024r^2}.
\]

**3. Why the spectral radius controls every initial vector.** Let \(\mathcal K\) be the closed proper cone of nonnegative polynomials in the displayed three-dimensional rotation-invariant quartic space, normalized by their average over the unit circle. Its normalized section is compact and convex. Since all four update matrices are invertible, \(\mathcal L\) maps every nonzero element of \(\mathcal K\) to another nonzero element. Brouwer's fixed-point theorem on the normalized section supplies a nonzero \(H\in\mathcal K\) and \(\lambda>0\) such that \(\mathcal LH=\lambda H\).

This \(H\) is strictly positive away from the origin. If \(H(v)=0\) for nonzero \(v\), positivity of the sampling weights implies \(H(M_{ij}v)=0\) for each pair, and inductively for every finite word of update matrices. A nonzero homogeneous quartic can vanish on only finitely many real projective directions. For a diagonalizable real \(2\times2\) matrix with distinct positive eigenvalues \(1/2\) and \(1\), a projective orbit is finite only for its eigenlines. Thus \(v\) would have to lie on an eigenline of both \(M_{11}\) and \(M_{22}\). The former has eigenlines \(\operatorname{span}(1,0)\) and \(\operatorname{span}(-r,1)\), while the latter has eigenlines \(\operatorname{span}(0,1)\) and \(\operatorname{span}(1,r)\). No lines coincide when \(r>0\), a contradiction. Therefore \(H(v)>0\) whenever \(v\ne0\).

By compactness of the unit circle, \(m\|v\|_2^4\le H(v)\le M\|v\|_2^4\) for constants \(0<m\le M<\infty\). The order-unit comparison bounds \(\mathcal L^k f\) by a multiple of \(\lambda^kH\) for every quartic \(f\) in the invariant space, so \(\lambda=\rho(C_r)\). Taking expectations of \(H(x_k)\) gives \(\mathbb E H(x_k)=\lambda^k H(x_0)\), and the displayed two-sided bounds prove \(\mathbb E\|x_k\|_2^4=\Theta_{r,x_0}(\lambda^k)\) for every nonzero \(x_0\).

**4. Sharp crossing.** At \(r=1\), the three eigenvalues are \(1/8\) and \((13\pm\sqrt{73})/32\), all inside the unit disk. As \(r\downarrow0\), the trace of \(C_r\) tends to infinity, so \(\rho(C_r)\to\infty\). By the cone argument, \(\rho(C_r)\) is always a positive real eigenvalue. It depends continuously on \(r\); hence a crossing of \(\rho(C_r)=1\) requires \(\det(I-C_r)=0\). The determinant has exactly one root in \((0,1]\), namely \(r_*\). Continuity and the endpoint inequalities establish precisely the three regimes claimed.

## Verification

The standalone `verify.py` rebuilds the four update matrices and sampling weights symbolically; computes all three quartic polynomial images; verifies every entry of the transfer matrix, its determinant, and the exact eigenvalues at \(r=1\); and exhaustively sums sampling paths through depth five for three rational values of \(r\), independently checking both the second and fourth moments against the closed recurrences. It also checks the exact algebraic equation for \(r_*\) and numerical spectra on both sides of the boundary. Execute `python verify.py` after installing the packages in `requirements.txt`. These finite computations corroborate the exact formulas; the infinite-horizon threshold and positivity arguments are proved above rather than inferred from tests.

For comparison, randomized row Kaczmarz on the same orthogonal system with relaxation \(1/2\) is a nonexpansive projection at every step. In the orthonormal row basis with initial coordinates \(c_1,c_2\), its exact fourth moment equals \((17/32)^k(c_1^4+c_2^4)+2(1/4)^kc_1^2c_2^2\), which always vanishes.

## Relationship to prior work

Razaviyayn, Hong, Reyhanian and Luo introduce the squared-entry-probability doubly stochastic Gauss–Seidel update and prove mean-square convergence under an appropriate step choice. Du and Sun develop the block extension and linear mean-square estimates; their later pseudoinverse-free framework likewise emphasizes first/second moments. Han and Xie study a broader family of randomized linear-system algorithms and momentum with convergence bounds. The present theorem uses the original sampling and step convention but characterizes an independent fourth-moment phenomenon; none of those second-moment bounds controls the fourth-moment spectral radius. The exact algebraic threshold and the uniform condition-number-one obstruction are the method-specific additions. General positive-operator facts used in the proof are standard and are not claimed as new.

## Limitations

The sharp constant pertains to the specified two-dimensional orthogonal family, independent squared-entry sampling, and relaxation exactly \(1/2\). The phenomenon does not claim fourth-moment divergence for row Kaczmarz, all coefficient matrices, or every DSGS relaxation choice. Although expected fourth powers diverge in the low-\(r\) regime, individual trajectories still converge to zero almost surely; no claim is made about a stationary heavy-tailed law. Independent external review and comprehensive historical priority verification have not been performed.

## References

1. M. Razaviyayn, M. Hong, N. Reyhanian and Z.-Q. Luo, *A Linearly Convergent Doubly Stochastic Gauss-Seidel Algorithm for Solving Linear Equations and A Certain Class of Over-Parameterized Optimization Problems*, arXiv:1810.05251, initial public version October 11, 2018, particularly Algorithm 1 and its mean-square theorem.
2. K. Du and X.-H. Sun, *A doubly stochastic block Gauss–Seidel algorithm for solving linear equations*, arXiv:1912.13291, initial public version December 31, 2019, Algorithm 1, Theorem 8, and Remarks 9 and 13.
3. K. Du and X.-H. Sun, *Pseudoinverse-free randomized block iterative algorithms for consistent and inconsistent linear systems*, arXiv:2011.10353, initial public version November 20, 2020.
4. D. Han and J. Xie, *On pseudoinverse-free randomized methods for linear systems: unified framework and acceleration*, arXiv:2208.05437, initial public version August 10, 2022.
