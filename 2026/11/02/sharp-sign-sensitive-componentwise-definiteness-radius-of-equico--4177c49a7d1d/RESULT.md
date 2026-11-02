# Sharp sign-sensitive componentwise definiteness radius of equicorrelated Gram matrices

## Finding

For an integer \(n\ge 2\) and \(-1/(n-1)<\rho<1\), let
\[
G_\rho=(1-\rho)I_n+\rho\mathbf{1}\mathbf{1}^{\mathsf T}.
\]
This positive-definite matrix is the Gram matrix of a full-column-rank real matrix. For \(u\ge0\), consider **all real symmetric** matrices \(H\) satisfying the independent relative-entry uncertainty bounds
\[
|H_{ij}-(G_\rho)_{ij}|\le u |(G_\rho)_{ij}|\quad(1\le i,j\le n).
\]
The universal positive-definiteness statement \(H\succ0\) for every such \(H\) holds **if and only if** \(0\le u<\tau_n(\rho)\), where the sharp radius is
\[
\boxed{\tau_n(\rho)=
\begin{cases}
\dfrac{1+(n-1)\rho}{1-(n-1)\rho},&-\dfrac1{n-1}<\rho<0,\\[5pt]
1,&\rho=0,\\[5pt]
\dfrac{K_n(\rho)-\rho}{K_n(\rho)+\rho},&0<\rho<1,
\end{cases}}
\]
with \(p=\lfloor n/2\rfloor\), \(q=\lceil n/2\rceil\), and
\[
K_n(\rho)=\sqrt{\rho^2+
\frac{(1-\rho)(1+(n-1)\rho)}{pq}}.
\]
At the radius there is an explicit singular positive-semidefinite member of the uncertainty family. Above the radius there is an explicit indefinite member. For \(\rho<0\), the first singular member uses coherently decreased entries; for \(\rho>0\), a balanced bipartition and opposite-sign cross-block perturbations attain the threshold.

For positive correlation, the formula has an exact parity consequence. Write \(c=\operatorname{cond}_2(G_\rho)=(1+(n-1)\rho)/(1-\rho)\). If \(n\) is even, then
\[
\tau_n(\rho)=\frac1c.
\]
If \(n\) is odd, then
\[
\tau_n(\rho)=
\frac{\sqrt{(c+1)^2+4c/(n^2-1)}-(c-1)}
{\sqrt{(c+1)^2+4c/(n^2-1)}+(c-1)}
>\frac1c.
\]
In particular, for fixed \(n\) and \(\rho\uparrow1\),
\[
\lim_{\rho\uparrow1}c\tau_n(\rho)=
\begin{cases}1,&n\text{ even},\\ n^2/(n^2-1),&n\text{ odd}.
\end{cases}
\]
These bounds use the condition number of the Gram matrix, **not** its square. If \(G_\rho=M^{\mathsf T}M\), then \(c=\operatorname{cond}_2(M)^2\).

## Assumptions and scope

The perturbations are arbitrary real symmetric matrices in the stated *entrywise relative interval*, with no restrictions linking their different entries. The diagonal of \(G_\rho\) equals one; every off-diagonal entry equals \(\rho\). For \(\rho=0\), off-diagonal entries remain exactly zero under the model. The parameter \(\rho\) belongs strictly to the positive-definite range; \(u\ge0\) is an uncertainty radius, not a measured machine precision. Statements about computed Gram matrices require the independently justified inclusion of their errors in this interval.

## Proof

**1. Reduction to finitely many sign matrices.** Write \(B=|G_\rho|\) for entrywise absolute value. For a nonzero real vector \(x\) and any admissible perturbation \(H\),
\[
x^{\mathsf T}Hx\ge x^{\mathsf T}G_\rho x-u|x|^{\mathsf T}B|x|.
\]
Choose signs \(s_i\in\{-1,1\}\) that agree with the nonzero coordinates of \(x\), and put \(S=\operatorname{diag}(s)\). Then the right side equals \(x^{\mathsf T}H_s(u)x\), where
\[
H_s(u)=G_\rho-uSBS.
\]
Every \(H_s(u)\) is itself admissible and symmetric. Thus every admissible \(H\) is positive definite if and only if **each** \(H_s(u)\) is positive definite. This argument holds even for zero coordinates of \(x\), whose signs can be chosen arbitrarily.

**2. Negative correlation.** If \(\rho<0\), the off-diagonal entries of \(G_\rho\) are negative. Hence, for every \(x\), \(x^{\mathsf T}G_\rho x\ge |x|^{\mathsf T}G_\rho|x|\). The bound in step 1 therefore strengthens to
\[
x^{\mathsf T}Hx\ge |x|^{\mathsf T}(G_\rho-uB)|x|.
\]
The matrix \(H_{\mathbf{1}}(u)=G_\rho-uB\) has diagonal \(1-u\) and off-diagonal \(\rho(1+u)\). Its eigenvalue on \(\mathbf{1}^\perp\) is \((1-\rho)-u(1+\rho)\); its eigenvalue on \(\operatorname{span}\{\mathbf{1}\}\) is
\[
1+(n-1)\rho-u[1-(n-1)\rho].
\]
The latter reaches zero first, at \(\tau_n(\rho)=[1+(n-1)\rho]/[1-(n-1)\rho]\in(0,1)\); the former is strictly positive there. The lower bound proves universal positivity below this radius. At the radius \(H_{\mathbf{1}}\) is singular with kernel \(\mathbf{1}\), and a larger radius permits an indefinite \(H_{\mathbf{1}}\).

**3. Zero correlation.** If \(\rho=0\), the interval consists of diagonal matrices with diagonal entries in \([1-u,1+u]\). All are positive definite precisely for \(u<1\). The zero matrix is admissible at \(u=1\).

**4. Positive correlation.** Here \(B=G_\rho\). Fix a sign vector \(s\), with \(r\) plus signs and \(n-r\) minus signs. If all signs are equal, then \(H_s(u)=(1-u)G_\rho\), so its threshold is one. If both groups are nonempty and \(u<1\), the within-group orthogonal complements have strictly positive eigenvalue \((1-u)(1-\rho)\). On the two-dimensional space of vectors that are constant within each group, use a value \(\alpha/r\) in the first group and \(-\beta/(n-r)\) in the second. The quadratic form is
\[
\begin{pmatrix}\alpha&\beta\end{pmatrix}
\begin{pmatrix}
(1-u)[\rho+(1-\rho)/r]&-\rho(1+u)\\
-\rho(1+u)&(1-u)[\rho+(1-\rho)/(n-r)]
\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\end{pmatrix}.
\]
Its diagonal entries are positive; positive definiteness is equivalent to positivity of its determinant. Define
\[
K_r^2=\left(\rho+\frac{1-\rho}{r}\right)
\left(\rho+\frac{1-\rho}{n-r}\right)
=\rho^2+\frac{(1-\rho)(1+(n-1)\rho)}{r(n-r)}.
\]
Consequently \(H_s(u)\succ0\) exactly when
\[
u<\frac{K_r-\rho}{K_r+\rho}.
\]
For fixed \(n\) and \(\rho>0\), the ratio is strictly increasing in \(K_r\), and \(K_r\) is minimized when \(r(n-r)\) is maximized. The latter occurs at the balanced sizes \(p=\lfloor n/2\rfloor\) and \(q=\lceil n/2\rceil\). The sign-vertex reduction then gives precisely \(\tau_n(\rho)\).

To exhibit a kernel at equality, choose any balanced sign vector with \(p\) positive and \(q\) negative entries. Set \(t=\tau_n(\rho)\), and define a vector with each positive-group coordinate equal to \(a=\rho(1+t)q\) and each negative-group coordinate equal to \(-b=-(1-t)[(1-\rho)+\rho p]\). The two group-row equations for \(H_s(t)x=0\) follow respectively from the definition of \(a,b\) and from the vanishing two-by-two determinant. The matrix is positive semidefinite at equality because all other eigenvalues are positive and the remaining two-by-two block has one zero and one positive eigenvalue. Choosing any \(u\) strictly between \(t\) and \(1\) makes this same balanced vertex indefinite; if the allowed radius is larger than one, that smaller indefinite vertex is still admissible.

**5. Parity formulas.** When \(n\) is even, \(pq=n^2/4\) and the positive square root simplifies to \(K_n=\rho+2(1-\rho)/n\). Substitution yields \(\tau_n=(1-\rho)/(1+(n-1)\rho)=1/c\). When \(n\) is odd, \(pq=(n^2-1)/4\); using \(\rho=(c-1)/(c+n-1)\) gives the displayed formula. For positive \(\rho\), the odd value exceeds \(1/c\) strictly because its balanced product is smaller than \(n^2/4\). The limiting ratios follow by expanding \(K_n-\rho\) as \(\rho\uparrow1\), or directly from the rationalized identity
\[
\tau_n(\rho)=\frac{(1-\rho)(1+(n-1)\rho)}
{pq\,[K_n(\rho)+\rho]^2}.
\]
This completes all quantifiers, both endpoints, and the sharpness witnesses.

## Verification

Run `python3 verify.py` using the adjacent standalone Python 3 source. It enumerates all sign vertices up to a global sign reversal for 36 rational parameter settings, spanning dimensions \(2\) to \(7\), negative, zero and positive correlations. Exact-rational symmetric Schur-complement elimination checks positive definiteness immediately below the proposed threshold and failure immediately above it. There were **1,512** exact-rational vertex checks. Separate comparisons test the parity formula. These finite checks are independent cross-checks and are *not* the proof for arbitrary dimension, real correlation, or uncertainty radius; those statements are established in the preceding argument.

## Relationship to prior work

Balabanov, Melnichenko and Mahoney (2026) establish the motivation from matrix-free Cholesky-QR: Gram formation squares the condition number, and their componentwise error-shaping framework gives algorithmic stability guarantees (especially Section 4 and Appendix C). They do not state this exact interval robustness radius for equicorrelation Gram matrices. The present theorem does not reinterpret their rounding model as independent adversarial entry perturbations without additional justification.

Rohn (1994) already establishes generic finite-vertex characterizations for positive definiteness of interval matrices; his related 1994 paper proves complexity hardness in the general case. Roustant and Deville (2017) already give the two-block mean-reduction criterion for compound-symmetry correlation matrices. Those generic reductions are *not new* here; the claimed additional statement is the globally optimized, explicit, sign-sensitive and parity-sensitive radius for an **entire independent-entry uncertainty family**, with attaining sign patterns and kernel vectors. Demmel (1992) established the general framework of componentwise distance to singularity; Rump (2003) studied structured componentwise perturbations. None of those background frameworks is claimed as a novel invention.

## Limitations

This is a mathematical **worst-case uncertainty-model** theorem, not a prediction that a particular floating-point product or Cholesky implementation realizes an adverse perturbation. Independent entry errors are deliberately more permissive than many actual arithmetic-error dependencies. It treats real symmetric matrices of a single equicorrelation family and does not give a general algorithmic guarantee for arbitrary Gram matrices, nonsymmetric perturbations, or finite-precision Cholesky success at a sharp boundary. Direct priority comparison with some older paywalled full texts remained incomplete; the formula may have an undiscovered classical equivalent.

## References

1. O. Balabanov, M. Melnichenko, and M. W. Mahoney, *Stable Matrix-Free Q-less QR via Preconditioning and Randomization*, arXiv:2610.16101v1 (first public 2026-10-12), https://arxiv.org/abs/2610.16101.
2. J. Rohn, *Positive Definiteness and Stability of Interval Matrices*, SIAM J. Matrix Anal. Appl. 15 (1994), 175–184, https://doi.org/10.1137/S0895479891219216.
3. J. Rohn, *Checking Positive Definiteness or Stability of Symmetric Interval Matrices Is NP-hard*, Comment. Math. Univ. Carol. 35 (1994), 795–797, https://dml.cz/handle/10338.dmlcz/118721.
4. O. Roustant and Y. Deville, *On the Validity of Parametric Block Correlation Matrices with Constant Within and Between Group Correlations*, arXiv:1705.09793 (2017), https://arxiv.org/abs/1705.09793.
5. J. Demmel, *The Componentwise Distance to the Nearest Singular Matrix*, SIAM J. Matrix Anal. Appl. 13 (1992), 10–19, https://doi.org/10.1137/0613003.
6. S. M. Rump, *Structured Perturbations Part II: Componentwise Distances*, SIAM J. Matrix Anal. Appl. 25 (2003), 31–56, https://doi.org/10.1137/S0895479802405744.
