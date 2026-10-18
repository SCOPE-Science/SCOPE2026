# Sharp prescribed reversals of ridge leverage-score rankings

## Finding

**Theorem (sharp pairwise regularization-path complexity).** Let \(A\in\mathbb R^{N\times d}\) be real with positive rank and let \(q\) be the number of *distinct positive* eigenvalues of \(A^{\mathsf T}A\). For row \(a_i\), let its ridge leverage score at \(\lambda>0\) be
\[
\ell_i(\lambda)=a_i(A^{\mathsf T}A+\lambda I)^{-1}a_i^{\mathsf T}.
\]
For any two rows, the score difference is either zero for all \(\lambda>0\), or has at most \(q-1\) distinct positive zeros. In particular, the rows exchange their strict score ordering at most \(q-1\) times as the regularization parameter runs through \((0,\infty)\).

The bound is **strongly sharp**: for every integer \(q\ge2\), every prescribed \(0<d_1<\cdots<d_q\), and every prescribed \(0<t_1<\cdots<t_{q-1}\), there is a full-column-rank \(A\in\mathbb R^{(q+2)\times q}\) whose squared singular values are precisely \(d_1,\ldots,d_q\) and whose first two ridge leverage scores satisfy
\[
\ell_1(\lambda)-\ell_2(\lambda)
=\varepsilon\frac{\prod_{j=1}^{q-1}(\lambda-t_j)}{\prod_{k=1}^{q}(\lambda+d_k)}
\qquad(\lambda>0)
\]
for a positive constant \(\varepsilon\). Their relative order changes strictly at all and only the \(q-1\) prescribed values. The corresponding assertion for column selection follows by transposing the matrix.

## Assumptions and scope

The matrix, all row vectors, and the ridge parameter are real. No normalization or probabilistic hypothesis is imposed on the rows. The score is computed with the *same fixed matrix* at every positive regularization parameter. If the positive spectrum has repetitions, \(q\) counts distinct values rather than multiplicities. A pair tied identically along the entire path is expressly excepted from the finite-zero statement; such a pair makes no strict ordering reversals.

For \(q=1\), no strict ranking reversal is possible. Each nonzero row leverage score is individually strictly decreasing with \(\lambda\); the theorem concerns **relative** ranking, which need not be monotone.

## Proof

**1. A finite-pole identity gives the universal upper bound.** Write the distinct positive eigenvalues of \(A^{\mathsf T}A\) as \(d_1,\ldots,d_q\) and their mutually orthogonal spectral projectors as \(P_1,\ldots,P_q\). Since a row of \(A\), regarded as a column, belongs to the range of \(A^{\mathsf T}A\), it has no component in that matrix's zero eigenspace. Therefore
\[
\ell_i(\lambda)=\sum_{k=1}^q
\frac{\|P_k a_i^{\mathsf T}\|_2^2}{\lambda+d_k}.
\]
For rows \(i,j\) put \(c_k=\|P_k a_i^{\mathsf T}\|_2^2-\|P_k a_j^{\mathsf T}\|_2^2\). Their difference is
\[
F_{ij}(\lambda)=\sum_{k=1}^q\frac{c_k}{\lambda+d_k}
=\frac{N_{ij}(\lambda)}{\prod_{k=1}^q(\lambda+d_k)},
\quad
N_{ij}(\lambda)=\sum_{k=1}^q c_k\prod_{h\ne k}(\lambda+d_h).
\]
The numerator is a real polynomial of degree at most \(q-1\). If it is nonzero, it has at most \(q-1\) positive roots (even when multiplicities are counted), and the denominator is strictly positive on \((0,\infty)\). If the numerator is zero identically, the partial fractions have distinct poles, so each \(c_k=0\), and the curves coincide. A strict reversal must occur at a positive root of the nonzero numerator.

**2. Prescribing arbitrary reversals while satisfying the singular-vector constraints.** Fix positive increasing numbers \(d_1,\ldots,d_q\) and \(t_1,\ldots,t_{q-1}\), and form
\[
P(z)=\prod_{j=1}^{q-1}(z-t_j),\qquad
Q(z)=\prod_{k=1}^{q}(z+d_k),\qquad
R_k=\frac{P(-d_k)}{\prod_{h\ne k}(d_h-d_k)}.
\]
The exact partial-fraction identity is
\[
\frac{P(z)}{Q(z)}=\sum_{k=1}^q\frac{R_k}{z+d_k}.
\]
Because the numerator evaluations \(P(-d_k)\) all have the same nonzero sign while the denominator factors alternate sign as \(k\) increases, all residues \(R_k\) are nonzero and alternate in sign. Define \(w_k=R_k/d_k\) and choose any
\[
0<\varepsilon<\left(\sum_{k=1}^q |w_k|\right)^{-1}.
\]
Construct nonnegative-coordinate vectors \(x,y\in\mathbb R^q\) by
\[
x_k=\sqrt{\varepsilon\max(w_k,0)},\qquad
y_k=\sqrt{\varepsilon\max(-w_k,0)}.
\]
Their supports are disjoint, so \(x^{\mathsf T}y=0\), and
\(\|x\|_2^2+\|y\|_2^2=\varepsilon\sum|w_k|<1\).
Consequently \(M=I_q-xx^{\mathsf T}-yy^{\mathsf T}\) is strictly positive definite. Let \(B=M^{1/2}\) be its *positive* symmetric square root and set
\[
U=\begin{pmatrix}x^{\mathsf T}\\y^{\mathsf T}\\B\end{pmatrix}
\in\mathbb R^{(q+2)\times q},\qquad
A=U\operatorname{diag}(\sqrt{d_1},\ldots,\sqrt{d_q}).
\]
Directly, \(U^{\mathsf T}U=xx^{\mathsf T}+yy^{\mathsf T}+B^2=I_q\), and hence the squared singular values of \(A\) are exactly the prescribed \(d_k\). By the score definition, its first-two-row difference is
\[
\sum_{k=1}^q\frac{d_k(x_k^2-y_k^2)}{\lambda+d_k}
=\varepsilon\sum_{k=1}^q\frac{R_k}{\lambda+d_k}
=\varepsilon\frac{P(\lambda)}{Q(\lambda)}.
\]
Every prescribed positive zero is simple, the denominator never vanishes for positive arguments, and therefore the strict ranking alternates exactly at \(t_1,\ldots,t_{q-1}\). This proves sharpness and arbitrary-location realizability.

**3. An exact three-mode witness.** Take the distinct squared singular values \(d_1=1,d_2=2,d_3=3\) and prescribed crossover values \(t_1=1,t_2=4\). The identity
\[
\frac{(\lambda-1)(\lambda-4)}{(\lambda+1)(\lambda+2)(\lambda+3)}
=\frac{5}{\lambda+1}-\frac{18}{\lambda+2}+\frac{14}{\lambda+3}
\]
allows \(\varepsilon=1/30\). Choose
\[
x=\left(\sqrt{1/6},\,0,\,\sqrt{7/45}\right)^{\mathsf T},\qquad
y=\left(0,\,\sqrt{3/10},\,0\right)^{\mathsf T}.
\]
Since \(\|x\|_2^2+\|y\|_2^2=28/45<1\), the above construction gives an explicit real \(5\)-by-\(3\) matrix. Its first-two-row score difference is exactly
\[
\frac{(\lambda-1)(\lambda-4)}{30(\lambda+1)(\lambda+2)(\lambda+3)}.
\]
It is positive for \(0<\lambda<1\), negative for \(1<\lambda<4\), and positive again for \(\lambda>4\). Despite these reversals, both row scores decrease strictly with \(\lambda\).

## Verification

The self-contained script `verify.py` requires Python, NumPy, and SymPy (versions in `requirements.txt`). Running `python verify.py` executes exact partial-fraction identities and constructs full-column-rank matrices from the positive matrix square root, checking their orthonormal columns and direct normal-equation ridge scores. It covers the exact three-mode witness and several independently prescribed crossover sets for every dimension from two through nine. The recorded execution passed **540 exact-algebraic and numerical matrix-resolvent assertions**. These finitely many calculations test the formulas; they do not replace the argument for arbitrary dimension and continuous parameter ranges.

## Relationship to prior work

McCurdy [1] defines ridge leverage scores and, in Algorithm 1, explicitly **sorts** them to select a deterministic column subset; its analyzed approximation and risk guarantees do not bound changes in their relative order as the regularization parameter varies. Meier and Nakatsukasa [2] explicitly consider regularized numerical least-squares problems for multiple values of the ridge parameter and develop reusable randomized preconditioners, but do not analyze the pairwise leverage-score ranking path. Cohen, Musco, and Musco [3] use ridge leverage scores for randomized sampling and prove monotonicity under a different perturbation: matrix modifications rather than a sequence of relative score orderings along the ridge parameter.

The theorem addresses the distinct question of **sharp pairwise order-change complexity**; none of those cited approximation or preconditioning guarantees imply the arbitrary-location realization result. Related claims expressed through rational Stieltjes transforms, Cauchy systems or interpolation theory might independently contain an equivalent theorem, so historical priority outside the inspected literature is unresolved.

## Limitations

The result bounds pairwise ordering reversals only; it does not determine the complexity of maintaining an entire sorting permutation for many rows, nor claim an improvement in a sketching algorithm's error, cost or convergence. The examples are exact real matrices without noise, and may have strongly varying row norms. The construction prescribes crossings between two rows using \(q+2\) total rows; it does not assert minimal possible row count, or prescribe all simultaneous pairwise crossovers. Identical score curves tie at every parameter and are treated separately. The statements concern positive ridge parameters; multiplicity and singular-limit issues at a zero parameter are excluded.

## References

[1] S. R. McCurdy, *Ridge Regression and Provable Deterministic Ridge Leverage Score Sampling*, arXiv:1803.06010, originally posted 15 March 2018. https://arxiv.org/abs/1803.06010

[2] M. Meier and Y. Nakatsukasa, *Randomized algorithms for Tikhonov regularization in linear least squares*, arXiv:2203.07329, originally posted 14 March 2022. https://arxiv.org/abs/2203.07329

[3] M. B. Cohen, C. Musco, and C. Musco, *Input Sparsity Time Low-Rank Approximation via Ridge Leverage Score Sampling*, arXiv:1511.07263, first posted 23 November 2015. https://arxiv.org/abs/1511.07263
