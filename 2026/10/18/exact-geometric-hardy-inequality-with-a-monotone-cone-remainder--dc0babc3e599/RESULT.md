# Exact geometric Hardy inequality with a monotone-cone remainder

## Finding

Fix \(0<\rho<1\). Equip sequences indexed by \(\mathbb N=\{1,2,\ldots\}\) with the probability weights \(\pi_n=(1-\rho)\rho^{n-1}\), and set \((Hf)_n=\sum_{j=1}^{n}f_j\). For every \(2\le p\le\infty\), the optimal constant in
\[
 \|Hf\|_{\ell^2(\pi)}\le C_{\rho,p}\|f\|_{\ell^p(\pi)}
\]
over nonnegative nonincreasing sequences \(f\) is
\[
 \boxed{C_{\rho,p}=\frac{\sqrt{1+\rho}}{1-\rho}.}
\]
The only nonzero equality sequences are the positive constants; the zero sequence also gives equality.

There is an exact squared-deficit formula at \(p=2\). Put \(c=\lim_{n\to\infty}f_n\) and \(d_k=f_k-f_{k+1}\ge0\). Then
\[
\boxed{\begin{aligned}
\frac{1+\rho}{(1-\rho)^2}\|f\|_{\ell^2(\pi)}^2-\|Hf\|_{\ell^2(\pi)}^2
=\frac1{1-\rho}\Bigg[2c\sum_{k\ge1}k\rho^k d_k\\
+\sum_{k,l\ge1}\min(k,l)\bigl(\rho^{\min(k,l)}+\rho^{\max(k,l)}\bigr)d_kd_l\Bigg].
\end{aligned}}
\]
Every summand is nonnegative. In particular, any nonconstant nonnegative nonincreasing sequence has strictly positive deficit.

The monotonicity restriction has a genuine quantitative effect: on the *unrestricted* weighted Hilbert space the same cumulative-sum operator has norm \((1-\sqrt\rho)^{-1}\), which exceeds \(C_{\rho,2}\) by the factor \((1+\sqrt\rho)/\sqrt{1+\rho}>1\).

## Assumptions and scope

Here \(\ell^p(\pi)\) has norm \(\bigl(\sum_{n\ge1}\pi_n|f_n|^p\bigr)^{1/p}\) for finite \(p\), and \(\ell^\infty(\pi)\) has its usual supremum norm. Only real nonnegative nonincreasing sequences are considered in the cone inequality and remainder identity. The sequence may be constant and need not tend to zero. For every such \(f\) in \(\ell^p(\pi)\), its first coordinate is finite, so \(f\) is bounded and the identity is well defined.

## Proof

**Geometric reduction.** Let \(N\) be geometric on \(\{1,2,\ldots\}\) with \(\mathbb P(N=n)=\pi_n\). Write
\[
 \mu=\mathbb EN=\frac1{1-\rho},\qquad \Lambda=\mathbb EN^2=\frac{1+\rho}{(1-\rho)^2}.
\]
For each positive integer \(k\), define \(I_k(n)=\mathbf1_{\{n\le k\}}\) and \(A_k(n)=\min(n,k)\). The telescoping decomposition, valid pointwise, is
\[
 f_n=c+\sum_{k\ge n}d_k,
 \quad f_N=c+\sum_{k\ge1}d_kI_k(N),
 \quad (Hf)_N=cN+\sum_{k\ge1}d_kA_k(N).
\]
Because \(\sum_{k\ge1}d_k=f_1-c<\infty\), all expansions below converge absolutely after taking expectations.

**Kernel computation.** For \(1\le k\le l\), geometric memorylessness gives
\[
 \mathbb E[I_k(N)I_l(N)]=1-\rho^k,
\]
\[
 \mathbb E[N A_k(N)]=\Lambda(1-\rho^k)-\frac{k\rho^k}{1-\rho},
\]
\[
 \mathbb E[A_k(N)A_l(N)]
 =\Lambda(1-\rho^k)-\frac{k(\rho^k+\rho^l)}{1-\rho}.
\]
For the middle identity, subtract \(\mathbb E[N(N-k)\mathbf1_{N>k}]\) from \(\mathbb EN^2\). On \(\{N>k\}\), the conditional variable \(N-k\) has the same geometric law as \(N\), which evaluates the subtraction. For the last identity, subtract \(\mathbb E[A_k(N)(N-l)\mathbf1_{N>l}]=k\rho^l/(1-\rho)\) from the middle identity.

**Remainder.** Expand \(\Lambda\mathbb Ef_N^2-\mathbb E(Hf)_N^2\) using the telescoping formulas. The constant-constant term vanishes. The constant-drop terms are \(2c\sum_{k\ge1}k\rho^kd_k/(1-\rho)\). The drop-drop terms are precisely
\[
 \frac1{1-\rho}\sum_{k,l\ge1}\min(k,l)
 \bigl(\rho^{\min(k,l)}+\rho^{\max(k,l)}\bigr)d_kd_l.
\]
This proves the displayed exact identity. All coefficients of the drops are strictly positive. Hence its right side vanishes exactly when every \(d_k\) is zero, that is, precisely when \(f\) is constant.

**All exponents and sharpness.** Since \(\pi\) is a probability measure, \(\|f\|_{\ell^2(\pi)}\le\|f\|_{\ell^p(\pi)}\) for every \(p\ge2\), including \(p=\infty\). The identity gives \(\|Hf\|_2\le\sqrt\Lambda\|f\|_2\), and hence the asserted inequality. Each positive constant sequence \(f_n=c\) has \((Hf)_n=cn\) and realizes the ratio \(\sqrt{\mathbb EN^2}=\sqrt\Lambda\). For nonzero nonconstant \(f\), the strict quadratic remainder already prevents equality, independently of the strictness of the \(p\)-norm comparison.

**Unrestricted comparison.** The unitary map \(f\mapsto(\sqrt{\pi_n}f_n)_{n\ge1}\) transforms \(H\) into \(\sum_{j\ge0}\rho^{j/2}S^j=(I-\sqrt\rho S)^{-1}\), where \(S\) is the unilateral right shift. The Neumann series gives norm at most \((1-\sqrt\rho)^{-1}\); normalized long constant blocks (approximate eigenvectors for eigenvalue \(1\) of \(S\)) make the upper bound sharp. The strict ratio follows algebraically.

## Verification

The accompanying `CHECK.py` evaluates both sides of the remainder identity with rational arithmetic for 600 generated eventually-constant nonincreasing sequences and rational weights, summing the geometric tails exactly. It separately verifies exact sharp equality for constant sequences. The cone-versus-unrestricted norm gap follows analytically from the weighted-shift resolvent. The analytic proof establishes the infinite-sequence statement; finite computations alone would not do so.

## Relationship to prior work

Kalybay, Persson, and Temirkhanova (2015) characterize bounded weighted discrete Hardy inequalities for nonnegative nonincreasing sequences in the range \(1<q<p<\infty\), including a finite/infinite-weight dichotomy. Their Theorem 2.1 and Theorem 5.2 give best constants up to two-sided comparability, not an exact sharp expression or a quadratic remainder for the present geometric model. The present result provides both for output exponent \(q=2\) and every input exponent \(p\ge2\).

Bennett and Grosse-Erdmann (2006) provide a weight characterization and estimates for decreasing-sequence Hardy inequalities. Gao (2014) improves estimates for same-exponent weighted *averaging* inequalities. Neither the fully inspected Gao paper nor the accessible characterization statements in Bennett and Grosse-Erdmann imply the precise geometric cross-exponent constant or its quadratic remainder. Only the abstract and bibliographic data, not the full 2006 article, could be inspected; equivalent older coverage is an acknowledged possibility. Andersen (1991) treats generalized Hardy inequalities for nonincreasing functions. The unrestricted norm is a standard unilateral-shift resolvent fact and is **not** claimed as new.

## Limitations

The sharp formula and exact remainder use a common geometric weight on both sides, nonnegative decreasing input, output exponent two and input exponent at least two. They do not characterize general kernels, arbitrary unrelated weights, or input exponents below two. General weighted Hardy characterizations can yield boundedness and quantitative estimates and might, after a nonobvious specialization, imply some sharp bounds. The complete original text of Bennett and Grosse-Erdmann (2006) was unavailable for comparison; the possibility of prior equivalent coverage remains open.

## References

1. A. Kalybay, L.-E. Persson, and A. Temirkhanova, “A new discrete Hardy-type inequality with kernels and monotone functions,” *Journal of Inequalities and Applications* **2015**, article 321 (2015), doi:10.1186/s13660-015-0843-9; first published 2015-10-06.
2. K. F. Andersen, “Weighted Generalized Hardy Inequalities for Nonincreasing Functions,” *Canadian Journal of Mathematics* **43** (1991), 1121–1135, doi:10.4153/CJM-1991-065-9.

3. G. Bennett and K.-G. Grosse-Erdmann, “Weighted Hardy inequalities for decreasing sequences and functions,” *Mathematische Annalen* **334** (2006), 489–531, doi:10.1007/s00208-005-0678-7 (abstract and accessible citations consulted; full text not inspected).
4. P. Gao, “On weighted Hardy inequalities for non-increasing sequences,” arXiv:1401.7156v1 (2014), especially Theorem 1.1 and Lemma 2.5 (full HTML inspected).
