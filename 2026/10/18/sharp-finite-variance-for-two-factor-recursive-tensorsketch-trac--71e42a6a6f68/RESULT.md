# Sharp finite variance for two-factor recursive TensorSketch trace estimation

## Finding

For the real, three-layer, degree-two recursive TensorSketch applied to a separable positive-semidefinite rank-one matrix, the estimator has an exact variance law that depends on only the fourth-power masses of the two tensor factors and the parity of the sketch width. In particular, for every integer \(d\ge 2\), every integer \(m\ge 1\), and all real unit vectors \(u,v\in\mathbb R^d\), set \(A=(u\otimes v)(u\otimes v)^{\mathsf T}\) and \(T=\operatorname{tr}(\Pi_2 A\Pi_2^{\mathsf T})=\|\Pi_2(u\otimes v)\|_2^2\). Define

\[
a=1-\sum_{i=1}^{d}u_i^4,\quad b=1-\sum_{j=1}^{d}v_j^4,\quad q=\frac{2m-1}{m^2},\quad s=\frac{m-1}{m^2},\quad g=\gcd(2,m),\quad U=2q^2+(m+g-2)s^2.
\]

Then \(\mathbb ET=1=\operatorname{tr}A\), and **exactly**

\[
\operatorname{Var}(T)=2q(a+b)+2Uab.
\]

The sharp worst-case variance among these separable rank-one inputs, for fixed \(d,m\), is

\[
\max_{\|u\|_2=\|v\|_2=1}\operatorname{Var}(T)
 =4q\left(1-\frac1d\right)+2U\left(1-\frac1d\right)^2.
\]

Equality holds exactly when both factors have constant coordinate magnitude \(1/\sqrt d\) (with arbitrary signs). Consequently, for each fixed \(d\), as \(m\to\infty\),

\[
m\max\operatorname{Var}(T)\longrightarrow
8\left(1-\frac1d\right)+2\left(1-\frac1d\right)^2.
\]

Taking the subsequent limit \(d\to\infty\) gives the constant \(10\). This is a benchmark for the real recursive sketch, **not** a variance bound for arbitrary positive-semidefinite matrices.

## Assumptions and scope

The independent random layers are the real CountSketch implementation used for the degree-two recursive construction. Two leaf matrices \(T_1,T_2\in\mathbb R^{m\times d}\) each map coordinate \(i\) to one bucket \(h_r(i)\in\mathbb Z_m\) with sign \(\sigma_r(i)\in\{-1,1\}\). An independent internal degree-two TensorSketch \(S\in\mathbb R^{m\times m^2}\) maps intermediate index \((a,b)\) to bucket \(H_1(a)+H_2(b)\pmod m\) with sign \(\eta_1(a)\eta_2(b)\). Thus

\[\Pi_2=S(T_1\otimes T_2).\]

Within and across layers the bucket functions are mutually independent and uniform on their codomains, with at least four-wise independence within each function where relevant; all sign functions are mutually independent and have at least four-wise independent unbiased Rademacher values, also independent of all bucket functions. Fully independent hashes and signs are a valid instance. Only pairwise hash marginals and four-wise sign moments enter the proof. No matrix-vector approximation, floating-point effects, or reuse of layer randomness across different estimator instances is assumed.

The tensor factors are fixed independently of the random sketch. The theorem allows \(m=1\) and both odd and even sketch widths. In the equality characterization, \(u\) and \(v\) may have independent sign patterns.

## Proof

**Step 1: effective one-factor column law.** For each factor define \(F_r(i)=H_r(h_r(i))\pmod m\) and \(X_r(i)=\sigma_r(i)\eta_r(h_r(i))\). The effective map has one signed nonzero per column. For distinct \(i,k\), the bucket difference \(\Delta_r=F_r(i)-F_r(k)\in\mathbb Z_m\) has law

\[
\Pr(\Delta_r=0)=q=\frac1m+\left(1-\frac1m\right)\frac1m,
\qquad
\Pr(\Delta_r=z)=s=\frac{m-1}{m^2}\quad(z\ne0).
\]

Indeed the leaf buckets agree with probability \(1/m\); if they differ, their independent internal images are uniform. Conditional on all buckets and internal signs, independent leaf signs make every product of distinct effective signs of total degree at most four mean zero. Independence of the two factors is preserved.

**Step 2: orthogonal sign expansion.** With \(\Delta_{ik}^{(1)}=F_1(i)-F_1(k)\) and \(\Delta_{j\ell}^{(2)}=F_2(j)-F_2(\ell)\), direct expansion of the squared norm gives \(T-1=A_1+A_2+C\), where

\[
A_1=2\sum_{i<k}u_i u_k X_1(i)X_1(k)\,\mathbf1_{\{\Delta_{ik}^{(1)}=0\}},
\quad
A_2=2\sum_{j<\ell}v_j v_\ell X_2(j)X_2(\ell)\,\mathbf1_{\{\Delta_{j\ell}^{(2)}=0\}},
\]

and

\[
C=2\sum_{i<k}\sum_{j<\ell}u_i u_k v_jv_\ell
X_1(i)X_1(k)X_2(j)X_2(\ell)
\left(\mathbf1_{\{\Delta_{ik}^{(1)}+\Delta_{j\ell}^{(2)}=0\}}+
\mathbf1_{\{\Delta_{ik}^{(1)}-\Delta_{j\ell}^{(2)}=0\}}\right).
\]

Conditional sign orthogonality makes these three terms uncorrelated and kills cross-products between distinct unordered coordinate pairs. It also proves \(\mathbb ET=1\). Using \(\sum_{i<k}u_i^2u_k^2=a/2\) gives \(\operatorname{Var}(A_1)=2qa\), and similarly \(\operatorname{Var}(A_2)=2qb\).

**Step 3: joint modular collisions.** Let \(\Delta_1,\Delta_2\) be independent copies of the distribution in Step 1, and write \(I_+=\mathbf1_{\{\Delta_1+\Delta_2=0\}}\), \(I_-=\mathbf1_{\{\Delta_1-\Delta_2=0\}}\). Symmetry implies

\[
\mathbb E I_+=\mathbb EI_-=q^2+(m-1)s^2,
\quad
\mathbb E(I_+I_-)=q^2+(g-1)s^2.
\]

For the intersection, both signs of the modular difference vanish exactly when \(2\Delta_1=0\pmod m\). There are \(g=\gcd(2,m)\) such residues, including zero. Therefore

\[
\mathbb E(I_++I_-)^2=2\bigl[2q^2+(m+g-2)s^2\bigr]=2U.
\]

Applying conditional sign orthogonality again and \(\sum_{j<\ell}v_j^2v_\ell^2=b/2\), we obtain \(\operatorname{Var}(C)=2Uab\). This proves the claimed variance identity for every \(m\ge1\), including the degenerate one-bucket case.

**Step 4: sharpness and leading scale.** Cauchy–Schwarz gives \(\sum_i u_i^4\ge1/d\) with equality if and only if all \(|u_i|=d^{-1/2}\); the same holds for \(v\). As \(q>0\), \(U>0\), the variance is strictly increasing in each of \(a\) and \(b\). The equality classification and sharp finite-dimensional formula follow. Finally, \(mq\to2\) and \(mU\to1\) as \(m\to\infty\), yielding the stated fixed-\(d\) and subsequent large-\(d\) limits.

## Verification

The standalone `verify_recursive_tensor_variance.py` program evaluates exact rational collision probabilities for widths \(1\le m\le79\), checks worst-case inequalities and attaining flat factors for \(2\le d\le11\), and independently constructs the three random sketching layers using direct bucket assignments, signs, and circular convolution. It passed 395 rational modular-probability checks, 3190 finite worst-case checks, and 8 direct Monte Carlo settings. These are consistency tests; the universal statement and uniqueness of equality cases follow from the proof above.

## Relationship to prior work

Khan, Pratap, and Sharma (2026), arXiv:2609.18577v1, introduce the trace estimator formed using recursive TensorSketch and prove a degree-dependent variance upper bound, rather than this exact two-factor law. Ahle and coauthors (2020) develop the recursive sketch and prove second-moment guarantees through composition of Johnson–Lindenstrauss moment properties. Classical (nonrecursive) TensorSketch estimates use one convolution of factor sketches and have different collision probabilities. The corrected TensorSketch analysis of Pham and Pagh and the complex-random-variable improvement of Sharma and coauthors address different sketch distributions or moment bounds. None of those statements alone gives the two-composed-hash law \(q=(2m-1)/m^2\), the modular two-torsion correction \(g\), and the jointly sharp finite-\(d,m\) extremum proved here. This is a limited comparison to the identified literature, not a claim of exhaustive priority.

## Limitations

Only the real, degree-two recursive construction and separable rank-one positive-semidefinite inputs are classified. For arbitrary positive-semidefinite matrices, nonseparable rank-one vectors, orders greater than two, dependent random hash families that violate the stated moment assumptions, or complex sketches, this particular formula need not apply. Computational runtime and floating-point accuracy are not addressed. General-purpose moment inequalities and unindexed prior exact calculations remain possible sources of overlap; no claim of independent expert validation is made.

## References

1. M. A. Khan, R. Pratap, and A. Sharma, *Accurate Trace Estimation with Fewer Random Bits via Recursive TensorSketch*, arXiv:2609.18577v1 (first public September 16, 2026), https://arxiv.org/abs/2609.18577.
2. T. D. Ahle, M. Kapralov, J. B. T. Knudsen, R. Pagh, A. Velingker, D. P. Woodruff, and A. Zandieh, *Oblivious Sketching of High-Degree Polynomial Kernels*, 2020, https://thomasahle.com/papers/tensorsketch-joint.pdf, especially Sections 3 and 4.1.
3. *Tensor Sketch: Fast and Scalable Polynomial Kernel Approximation*, corrected preprint arXiv:2505.08146v2, https://arxiv.org/html/2505.08146v2 (discussion of nonrecursive TensorSketch variance).
4. A. Sharma, M. A. Khan, R. Pratap, and K. Kang, *Improving TensorSketch Using Complex Random Variables*, PMLR 337 (2026), 6178–6203, https://proceedings.mlr.press/v337/sharma26b.html.
