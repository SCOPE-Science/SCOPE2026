# Samplewise trace dominance of sketch-before-function Nyström approximation at every rank

## Finding

Let \(A\succeq0\) be a real symmetric \(n\)-by-\(n\) matrix and let \(G\) be any real \(n\)-by-\(k\) sketch, including rank-deficient sketches. For a positive-semidefinite matrix \(X\), set
\[
\mathcal N_G(X)=XG(G^{\mathsf T}XG)^\dagger G^{\mathsf T}X.
\]
For every **continuous nonzero operator-monotone** function \(f:[0,\infty)\to[0,\infty)\) with \(f(0)=0\), the following **same-sketch, all-ranks** inequality holds:
\[
\boxed{\operatorname{tr}f(\mathcal N_G(A))\ge
\operatorname{tr}\mathcal N_G(f(A)).}
\tag{1}
\]
Both approximants lie below \(f(A)\) in the positive-semidefinite order; consequently (1) is equivalent to the nuclear-error guarantee
\[
\boxed{\big\|f(A)-f(\mathcal N_G(A))\big\|_*
\le\big\|f(A)-\mathcal N_G(f(A))\big\|_*.}
\tag{2}
\]
The inequality is deterministic: no Gaussian assumption, sketch distribution, spectral gap, or oversampling hypothesis is needed. The power functions \(f(x)=x^\alpha\) for \(0<\alpha\le1\), \(f(x)=\log(1+x)\), and ridge functions \(f(x)=x/(x+s)\) for \(s>0\) are covered.

## Assumptions and scope

All matrices are finite-dimensional and real. The Moore–Penrose pseudoinverse is used, so \(G\) need not have full column rank. A nonzero continuous operator-monotone \(f\) with \(f(0)=0\) is positive on positive arguments and is operator concave. Let \(F=f(A)\). Define \(P_X\) to be the orthogonal projector onto \(\operatorname{range}(X^{1/2}G)\). The precise conclusion is a **trace/nuclear norm comparison for the same sketch matrix**; it does not assert an operator-order relation between the two different low-rank approximants or a comparison after unrelated truncations.

## Proof

**1. Positive residuals and compression.** For any \(X\succeq0\), the Nyström formula is
\[
\mathcal N_G(X)=X^{1/2}P_X X^{1/2},\qquad
0\preceq\mathcal N_G(X)\preceq X.
\tag{3}
\]
In particular, the operator monotonicity of \(f\) yields \(0\preceq f(\mathcal N_G(A))\preceq f(A)=F\), and (3) for \(X=F\) yields \(0\preceq\mathcal N_G(F)\preceq F\). Therefore nuclear norms of both residuals are their traces.

Choose an orthonormal basis \(Q\) for \(\operatorname{range}(A^{1/2}G)\), so \(P_A=QQ^{\mathsf T}\). Nonzero eigenvalues of \(\mathcal N_G(A)=A^{1/2}QQ^{\mathsf T}A^{1/2}\) are those of \(Q^{\mathsf T}AQ\). Since \(f(0)=0\), the traces of their matrix functions agree. By operator concavity and the compression form of Jensen's inequality,
\[
\operatorname{tr}f(\mathcal N_G(A))
=\operatorname{tr}f(Q^{\mathsf T}AQ)
\ge\operatorname{tr}(Q^{\mathsf T}f(A)Q)
=\operatorname{tr}(P_A F).
\tag{4}
\]
For completeness, the compression inequality follows from the standard integral representation of continuous nonnegative operator-monotone functions vanishing at zero as nonnegative combinations of \(x\) and \(x/(x+s)\), \(s>0\). For each resolvent kernel, the Schur-complement inverse inequality \((Q^{\mathsf T}(A+sI)Q)^{-1}\preceq Q^{\mathsf T}(A+sI)^{-1}Q\) proves the desired Jensen direction, and the linear term gives equality.

**2. Spectral reweighting lemma.** We prove the more precise assertion
\[
\operatorname{tr}(P_A F)\ge\operatorname{tr}(P_F F).
\tag{5}
\]
Restrict to the support of \(A\), because the support of \(F\) is the same and the kernel components of \(G\) affect neither projector. In an eigenbasis of \(A\), write the strictly positive eigenvalues as \(\lambda_i\) and \(u_i=f(\lambda_i)>0\). Ordinary scalar concavity with \(f(0)=0\) implies that \(\lambda_i/u_i\) is nondecreasing with \(\lambda_i\).

On the supporting coordinate space, set \(D_t=(1-t)F+tA\) for \(0\le t\le1\), and let \(P_t\) project onto \(\operatorname{range}(D_t^{1/2}G)\). This subspace has constant dimension along the path. Put
\[
h_i(t)=\frac12\frac{\lambda_i-u_i}{(1-t)u_i+t\lambda_i}
=\frac12\frac{r_i-1}{1-t+tr_i},\qquad
r_i=\lambda_i/u_i.
\tag{6}
\]
The scalar derivative of the right side with respect to \(r_i\) is \(1/[2(1-t+tr_i)^2]>0\). Thus \(h_i(t)\) is nondecreasing with \(\lambda_i\), just like \(u_i\). If \(H_t\) denotes the diagonal matrix with entries \(h_i(t)\), differentiating the orthogonal projector gives the exact identity
\[
P_t'=(I-P_t)H_tP_t+P_tH_t(I-P_t).
\tag{7}
\]
Writing \(p_{ij}(t)\) for the entries of \(P_t\), using \(P_t^2=P_t\), and pairing indices yields
\[
\begin{aligned}
\frac{d}{dt}\operatorname{tr}(P_tF)
&=2\big(\operatorname{tr}(P_tFH_t)-\operatorname{tr}(P_tFP_tH_t)\big)\\
&=\sum_{i,j}(u_i-u_j)(h_i(t)-h_j(t))\,|p_{ij}(t)|^2\ge0.
\end{aligned}
\tag{8}
\]
This is a genuinely **pairwise spectral covariance** formula; each summand is nonnegative. Integrating from \(t=0\) to \(t=1\) proves (5).

**3. Combine the two comparisons.** Since \(\operatorname{tr}\mathcal N_G(F)=\operatorname{tr}(P_F F)\), (4) and (5) give
\[
\operatorname{tr}f(\mathcal N_G(A))\ge
\operatorname{tr}(P_A F)\ge
\operatorname{tr}(P_F F)=\operatorname{tr}\mathcal N_G(F).
\]
This proves (1), and the positive-residual argument proves (2). If \(A=0\), both sides vanish and the inequality is immediate; if \(G\) has no component on the support of \(A\), both sides vanish and the same conclusion holds.

**4. No matrix-order conclusion.** Take \(A=\operatorname{diag}(4,1)\), \(G=(1,1)^{\mathsf T}\), and \(f(x)=\sqrt{x}\). Direct evaluation gives
\[
\mathcal N_G(A)=\frac15\begin{pmatrix}16&4\\4&1\end{pmatrix},\qquad
\mathcal N_G(f(A))=\frac13\begin{pmatrix}4&2\\2&1\end{pmatrix}.
\]
The traces in (1) are \(\sqrt{17/5}\) and \(5/3\), respectively; the inequality is strict because \(153>125\). However,
\[
\det\!\left(f(\mathcal N_G(A))-\mathcal N_G(f(A))\right)
=-\frac{4}{15\sqrt{17/5}}<0.
\]
The difference is indefinite despite the trace/nuclear dominance.

## Verification

Run `python verify.py` after installing the single dependency in `requirements.txt` and setting an appropriate single-thread numerical library environment if desired. The supplied script checks the exact rational inequality and negative determinant in the two-dimensional witness and exercises the same-sketch trace inequality and pairwise-derivative positivity at multiple sizes, ranks, and operator-monotone functions. On the supplied run it completed **38,400 finite numerical comparisons**, as well as the exact witness checks. These experiments are stress tests, not the source of the universal proof; equations (3)–(8) supply that proof.

## Relationship to prior work

Persson and Kressner introduced funNyström in 2022 and compared applying a function **after** approximating the underlying matrix against applying Nyström **directly to the matrix function**. Their §4.3 observed better or equal numerical errors in the tested cases; §§3 and 5 furnish probability/error bounds for the sketch-before-function method, not (1) or (2). This finding identifies the precise **untruncated, common-sketch, nuclear-norm** setting in which that comparison is universally valid, and proves it at every sketch rank. It does not assert that their numerical observations in other norms or with differing subspace-iteration sketches become theorems.

Persson, Meyer, and Musco subsequently proved that near-optimal positive-semidefinite approximations to the original matrix yield near-optimal approximations after an operator-monotone function. Their Theorem 1.1 compares errors with best-rank tails, not the two simultaneous same-sketch Nyström constructions. The general-purpose low-rank preservation theorem does not imply the samplewise pairwise inequality here. The prior exact two-dimensional asymptotic funNyström calculations likewise do not imply the all-ranks, arbitrary-sketch comparison.

## Limitations

The theorem controls trace and nuclear error only. It does not compare Frobenius or operator errors, does not compare two independently drawn sketch matrices, does not compare truncated approximants with different final ranks, and requires a common \(G\). It assumes a continuous nonnegative operator-monotone function with \(f(0)=0\) and exact matrix functions/inverses. The pairwise covariance mechanism uses that \(f\) is concave and that \(\lambda/f(\lambda)\) preserves spectral order. The existence of equivalent formulations of the projector covariance lemma outside the inspected literature is a residual priority risk; independent literature validation has not been performed.

## References

1. D. Persson and D. Kressner, *Randomized Low-Rank Approximation of Monotone Matrix Functions*, arXiv:2209.11023 (first posted 2022-09-22), especially §§2–3, 4.3 and 5; https://arxiv.org/abs/2209.11023.
2. D. Persson, R. A. Meyer, and C. Musco, *Algorithm-Agnostic Low-Rank Approximation of Operator Monotone Matrix Functions*, arXiv:2311.14023 (first posted 2023-11-23), especially Theorem 1.1 and §2; https://arxiv.org/abs/2311.14023.
3. D. Persson, *Randomized Low-Rank Approximation and Its Applications*, doctoral thesis, École polytechnique fédérale de Lausanne (2024), Chapter 4; https://infoscience.epfl.ch/server/api/core/bitstreams/27e0cc2a-aa2c-440b-a081-f9b1212202f0/content.
4. R. Bhatia, *Matrix Analysis*, Springer (1997), operator monotonicity/concavity, Jensen compression and integral representations.
