# Sharp two-row mean-square guarantee for Gaussian-sketch pivoting with two columns

## Finding

**Theorem (exact law and sharp sketch-row threshold).** Fix integers \(d\ge2\) and \(s\ge1\). Let \(M=[a\ b]\in\mathbb R^{d\times2}\) have full column rank, and write its singular values as \(\sigma_1\ge\sigma_2>0\). Independently draw \(\Omega\in\mathbb R^{s\times d}\) with entries \(N(0,1/s)\). Select the column of \(M\) maximizing its sketched Euclidean norm \(\|\Omega a\|_2\) or \(\|\Omega b\|_2\), and denote orthogonal projection onto that selected original column by \(P\). Put \(E_s=\|(I-P)M\|_2\).

Reorder columns without loss so that \(u=\|a\|_2^2\ge v=\|b\|_2^2\), and define

\[
\tau=a^\mathsf{T}b,\quad D=uv-\tau^2>0,\quad
\Delta=\sqrt{(u+v)^2-4\tau^2},\quad
q=\frac12\left(1-\frac{u-v}{\Delta}\right).
\]

For the regularized incomplete beta function \(I_q\), the exact selection probability and exact squared-error risk are

\[
\Pr(\text{select }b)=p_s=I_q(s/2,s/2),\qquad
\mathbb E E_s^2=D\left(\frac{1-p_s}{u}+\frac{p_s}{v}\right).
\]

For every integer \(s\ge2\), the sharp uniform guarantee is

\[
\boxed{\mathbb E E_s^2\le\frac{2D}{u+v}
=\frac{2\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2}
\le2\sigma_2^2.}
\]

For each fixed \(s\ge2\), the supremum of \(\mathbb E E_s^2/\sigma_2^2\) over full-column-rank matrices is exactly \(2\), approached by explicitly balanced-column families. Consequently \(\mathbb E E_s\le\sqrt2\,\sigma_2\) also holds.

By contrast, for \(s=1\) there is **no finite** uniform constant multiplying \(\sigma_2^2\). In particular, for \(M_\kappa=\operatorname{diag}(\kappa,1)\), \(\kappa>1\),

\[
\frac{\mathbb E E_1^2}{\sigma_2^2}
=1+(\kappa^2-1)\frac2\pi\arctan(1/\kappa)
\sim\frac{2\kappa}{\pi}\longrightarrow\infty.
\]

Thus two rows are necessary and sufficient for a dimension-free, conditioning-independent **mean-square** spectral-error guarantee in this precise two-column pivot procedure.

## Assumptions and scope

The input is any fixed real matrix with exactly two linearly independent columns; the ambient row dimension is arbitrary. The sketch is independent, isotropic Gaussian with exactly \(s\) rows. The pivot uses the **maximum sketched column norm** and returns a one-column orthogonal projector in the original ambient space. Ties have probability zero unless the input column norms coincide in a special degenerate manner; for equal original column norms both rank-one projection errors are identical, so arbitrary tie resolution does not alter the result. The spectral and Frobenius residual norms coincide because the residual matrix has rank at most one. Probabilities and expectations refer only to the Gaussian sketch.

## Proof

**1. Exact projection losses.** Let \(P_a=aa^\mathsf T/u\) and \(P_b=bb^\mathsf T/v\). Since \((I-P_a)a=0\) and \((I-P_b)b=0\), both residuals have rank one. Direct Gram-matrix algebra gives

\[
\|(I-P_a)M\|_2^2=\|b\|_2^2-\tau^2/u=D/u,
\qquad
\|(I-P_b)M\|_2^2=D/v.
\]

**2. Exact Gaussian mispivot law.** For one standard Gaussian row \(g\), the difference in squared projected column norms is \(g^\mathsf T(aa^\mathsf T-bb^\mathsf T)g\). The symmetric rank-at-most-two matrix in this quadratic form has nonzero eigenvalues

\[
\lambda_+=\frac{u-v+\Delta}{2}>0,\qquad
\lambda_-=\frac{u-v-\Delta}{2}<0.
\]

(The strict signs follow from \(D>0\), which implies \(\Delta>|u-v|\).) Orthogonal Gaussian invariance and independence across sketch rows show that the sketched squared-norm difference has the same sign as \(\lambda_+X+\lambda_-Y\), where \(X,Y\) are independent chi-square variables with \(s\) degrees of freedom. Therefore

\[
\begin{aligned}
\Pr(\text{select }b)
&=\Pr\!\left(\frac{X}{X+Y}<\frac{-\lambda_-}{\lambda_+-\lambda_-}\right)\\
&=\Pr\!\left(\operatorname{Beta}(s/2,s/2)<q\right)
=I_q(s/2,s/2).
\end{aligned}
\]

Combining this probability with the two exact projection losses proves the risk identity.

**3. Dominance for at least two sketch rows.** Because \(u\ge v\), \(0<q\le1/2\); because \(\Delta\le u+v\),

\[
q=\frac12\left(1-\frac{u-v}{\Delta}\right)
\le\frac12\left(1-\frac{u-v}{u+v}\right)=\frac{v}{u+v}.
\]

For \(k=s/2\ge1\), the symmetric \(\operatorname{Beta}(k,k)\) density is nondecreasing on \([0,1/2]\) and has total mass \(1/2\) there. The elementary average-density inequality implies \(I_q(k,k)\le q\) for every \(0\le q\le1/2\). Hence \(p_s\le v/(u+v)\). Since \(D/v\ge D/u\), inserting this bound into the exact risk gives

\[
\mathbb E E_s^2\le D\left[
\frac{1-v/(u+v)}{u}+
\frac{v/(u+v)}{v}\right]=\frac{2D}{u+v}.
\]

Finally \(D=\det(M^\mathsf TM)=\sigma_1^2\sigma_2^2\) and \(u+v=\operatorname{tr}(M^\mathsf TM)=\sigma_1^2+\sigma_2^2\). Jensen's inequality gives the first-moment spectral-error bound.

**4. Attainment of the sharp constant.** Fix \(\kappa>1\) and consider

\[
M_\kappa=\frac1{\sqrt2}
\begin{pmatrix}\kappa&-\kappa\\1&1\end{pmatrix}.
\]

Its singular values are \(\kappa,1\), while both original columns have squared norm \((\kappa^2+1)/2\). Either pivot therefore has the same deterministic residual squared, namely \(2\kappa^2/(\kappa^2+1)\). Thus, for every sketch row count,

\[
\frac{\mathbb E E_s^2}{\sigma_2^2}
=\frac{2\kappa^2}{\kappa^2+1}\longrightarrow2
\quad(\kappa\to\infty),
\]

which makes the universal upper constant exactly \(2\).

**5. Necessity of two rows.** Let \(M_\kappa=\operatorname{diag}(\kappa,1)\). For one Gaussian row, the smaller column wins iff \(g_2^2>\kappa^2g_1^2\). The ratio \(g_2/g_1\) is standard Cauchy, giving

\[
p_1(\kappa)=\frac2\pi\arctan(1/\kappa).
\]

The two squared residuals are \(1\) and \(\kappa^2\); therefore the expected squared error is exactly \(1+(\kappa^2-1)p_1(\kappa)\). As \(p_1(\kappa)\sim2/(\pi\kappa)\), the risk ratio grows like \(2\kappa/\pi\), proving unboundedness. This also shows that the one-row obstruction is specifically an expectation-tail effect, not a failure of Gaussian sketch isotropy.

## Verification

The standalone `check_pivot.py` reconstructs the beta-law and risk for nonorthogonal random columns, confirms analytic expectations against independent Gaussian simulations, tests the universal inequality over thousands of randomly generated matrices with varying conditioning and ambient dimensions, and checks the sharpness family and one-row Cauchy formula. It completed 21,092 deterministic and Monte-Carlo assertions on a local Python environment with NumPy and SciPy. These tests are finite consistency checks; the theorem's universal quantifiers and divergence are proved analytically above.

Reproduce with `python check_pivot.py` (requires `numpy` and `scipy`).

## Relationship to prior work

Grigori and Xue (2025, arXiv:2503.18496v1) analyze randomized strong rank-revealing QR using a sketch satisfying a high-probability subspace-embedding condition; the inspected sections give conditional strong rank-revealing bounds for general matrices. Those bounds do not directly assert the unconditional exact beta mispivot law or the sharp one-versus-two Gaussian row transition in expected squared error here. The present rule corresponds to the **first norm pivot** of Gaussian-sketched column-pivoted QR in the special case of exactly two columns; it is not a full analysis of subsequent strong rank-revealing swaps.

The bound \(2D/(u+v)\) is also the known exact expected squared projection error of **norm-squared-proportional one-column sampling** on two columns. The new comparison proved here is that Gaussian **maximum-sketch-norm** selection with at least two rows never has larger mean-square risk than that baseline, while just one sketch row lacks any uniform guarantee. The norm-proportional identity by itself does not establish this dominance because the sampling rules are different.

Duersch and Gu (2017) study randomized QR with column pivoting more generally; only accessible bibliographic material was available for this comparison. Exact overlap in inaccessible portions cannot be excluded.

## Limitations

Only two input columns, full rank, one selected original column, real Gaussian sketches, exact norm comparisons, and mean-square spectral error are covered. No claim is made for arbitrary multi-column CSS, downstream strong-RRQR refinement, deterministic sketches, floating-point arithmetic, uniformly small failure probabilities, or total work-optimal sketch dimension. The sharpness family is a limit, not an attained worst-case input of finite condition number. Bibliographic uniqueness cannot be established from bounded searching.

## References

1. L. Grigori and Z. Xue, *Randomized strong rank-revealing QR for column subset selection and low-rank matrix approximation*, arXiv:2503.18496v1, first submitted 24 March 2025. https://arxiv.org/abs/2503.18496 .
2. J. Duersch and M. Gu, *Randomized QR with Column Pivoting*, SIAM Journal on Scientific Computing, DOI:10.1137/15M1044680 (2017).
3. Standard chi-square/Beta ratio and Gaussian orthogonal-invariance identities, used as established probability facts.
