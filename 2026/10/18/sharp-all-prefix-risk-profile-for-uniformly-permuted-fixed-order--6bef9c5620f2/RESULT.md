# Sharp all-prefix risk profile for uniformly permuted fixed-order blocks

## Finding

Fix integers \(K\ge2\) and \(b\ge2\), and let \(n=Kb\). Partition \(n\) prescribed vectors \(g_{ij}\in\mathbb R^d\) (\(1\le i\le K\), \(1\le j\le b\), \(d\ge1\)) into \(K\) labeled blocks. Uniformly permute the blocks while keeping all \(b\) positions **in their original order inside each block**. Let \(\widehat\mu_m^{\mathrm{block}}\) be the average of the first \(m\) observed vectors, where \(1\le m<n\), and let \(\widehat\mu_m^{\mathrm{RR}}\) denote the average of \(m\) vectors sampled without replacement by a fully uniform permutation of all \(n\) individual vectors. Both target the grand mean \(\mu=n^{-1}\sum_{i,j}g_{ij}\).

Put \(\mathcal R_m^{\mathrm{block}}=\mathbb E\|\widehat\mu_m^{\mathrm{block}}-\mu\|^2\) and \(\mathcal R_m^{\mathrm{RR}}=\mathbb E\|\widehat\mu_m^{\mathrm{RR}}-\mu\|^2\). For every nonconstant vector array and every \(1\le m<n\),

\[
0\le\frac{\mathcal R_m^{\mathrm{block}}}{\mathcal R_m^{\mathrm{RR}}}
\le \frac{Kb-1}{K-1}.
\]

The constant is **globally sharp**. Equality at a nontrivial prefix is possible if and only if \(m=qb\), \(1\le q<K\), and the prescribed vectors are constant within each block (with at least two different block values). For any *incomplete-block* prefix, \(m=qb+r\) with \(1\le r<b\), the inequality is strictly stronger, uniformly over nonconstant vector arrays: its exact smallest comparison constant is \(\mathcal C_m\) below, and \(\mathcal C_m<(Kb-1)/(K-1)\).

For \(m=qb+r\), \(0\le r<b\), define

\[
D=\frac{r(b-r)}b,\qquad
A=\frac{q(K-q)b}{K-1}+\frac{r^2}{b}-\frac{2qr}{K-1},
\qquad
H=\sqrt D\left(\frac r{\sqrt b}-\frac{q\sqrt b}{K-1}\right),
\]
\[
\Lambda_m=\frac{A+D+\sqrt{(A-D)^2+4H^2}}{2K},
\qquad
\boxed{\mathcal C_m=\frac{n(n-1)}{m(n-m)}\Lambda_m}.
\]

Then

\[
\boxed{\sup_{\{g_{ij}\}:\,\mathcal R_m^{\mathrm{RR}}>0}
\frac{\mathcal R_m^{\mathrm{block}}}{\mathcal R_m^{\mathrm{RR}}}=\mathcal C_m.}
\]

The supremum is **attained by real scalar data**, not merely asymptotically. At block boundaries \(r=0\), the sharp ratio simplifies to \((Kb-1)/(K-1)\). The exact formula covers *every* interior prefix, including an incomplete first or last block.

At block boundaries the more data-specific comparison is also exact. Let \(G_i=b^{-1}\sum_jg_{ij}\), \(\sigma_{\mathrm{blk}}^2=K^{-1}\sum_i\|G_i-\mu\|^2\), and \(\sigma_{\mathrm{within}}^2=n^{-1}\sum_{i,j}\|g_{ij}-G_i\|^2\). For every \(1\le q<K\),

\[
\frac{\mathcal R_{qb}^{\mathrm{block}}}{\mathcal R_{qb}^{\mathrm{RR}}}
=\frac{Kb-1}{K-1}
\frac{\sigma_{\mathrm{blk}}^2}{\sigma_{\mathrm{blk}}^2+\sigma_{\mathrm{within}}^2}
\]

when the denominator is positive. Consequently the block scheme has smaller matched-sample prefix mean-square error precisely when

\[
\sigma_{\mathrm{within}}^2>\frac{K(b-1)}{K-1}\sigma_{\mathrm{blk}}^2.
\]

This is a statement about gradients evaluated at a **fixed point**, not an assertion about the performance of iterates whose gradients subsequently change.

## Assumptions and scope

The data vectors are deterministic and may belong to any fixed finite-dimensional Euclidean space. The only randomness is a uniform permutation of labeled equal-size blocks. Internal block positions are fixed. Both sampling schemes use exactly \(m\) individual vector evaluations and form unweighted prefix averages. All expectation and matrix calculations are in exact arithmetic. The formulas do not assume convexity, independence of the data vectors, or equal block means. For the ratio we exclude constant arrays, since both mean-square errors then vanish.

## Proof

**1. Exact finite-population risk, including incomplete blocks.** Set \(y_{ij}=g_{ij}-\mu\), \(B_i=\sum_{j=1}^{b}y_{ij}\), and, for \(r\ge0\), \(C_i=\sum_{j=1}^{r}y_{ij}\) (the empty sum is zero). Write \(\overline C=K^{-1}\sum_i C_i\), \(C_i^\circ=C_i-\overline C\). The unnormalized centered random prefix sum is \(S_m=\sum_{i\text{ among first }q\text{ blocks}}B_i+C_J\), where \(J\) is the block immediately following those \(q\) blocks (the last term is zero when \(r=0\)). Because \(\sum_iB_i=0\), symmetry gives \(\mathbb ES_m=\overline C\).

The first \(q\) blocks form a uniform subset; conditioned on \(J=j\), their mean total is \(-qB_j/(K-1)\). The finite-population covariance identity and this conditioning yield exactly

\[
\begin{split}
m^2\mathcal R_m^{\mathrm{block}}=
&\|\overline C\|^2
+\frac{q(K-q)}{K(K-1)}\sum_i\|B_i\|^2
+\frac1K\sum_i\|C_i^\circ\|^2\\
&-\frac{2q}{K(K-1)}\sum_i\langle B_i,C_i^\circ\rangle.
\end{split}
\tag{1}
\]

In particular, if \(r>0\) and \(\mu_r=(Kr)^{-1}\sum_{i,j\le r}g_{ij}\), then

\[
\mathbb E\widehat\mu_m^{\mathrm{block}}-\mu
=\frac r m(\mu_r-\mu).
\tag{2}
\]

Thus a partial prefix need not even be unbiased; equation (1) includes this squared bias. Fully uniform reshuffling is unbiased and satisfies the standard finite-population identity

\[
\mathcal R_m^{\mathrm{RR}}=
\frac{n-m}{m(n-1)}\frac1n\sum_{i,j}\|y_{ij}\|^2.
\tag{3}
\]

**2. Exact risk operator and its top eigenvalue.** It is enough to analyze scalar arrays, since vector coordinates add orthogonally. Regard each scalar block as \(y_i\in\mathbb R^b\). Split \(y_i=w+z_i\), where \(w=K^{-1}\sum_i y_i\) and \(\sum_i z_i=0\). Global centering gives \(\mathbf1_b^{\mathsf T}w=0\). The deterministic common-block profile contributes \((v_r^{\mathsf T}w)^2\) to \(\mathbb ES_m^2\), where \(v_r\) has \(r\) leading ones and \(b-r\) trailing zeros. Its sharp quotient against the total input squared norm \(K\|w\|^2\) is \(D/K\), since \(\|v_r-(r/b)\mathbf1_b\|^2=D\).

The centered block contrasts \(z_i\) contribute exactly \(K^{-1}\sum_i z_i^{\mathsf T}Mz_i\), where

\[
M=\frac{q(K-q)}{K-1}\mathbf1_b\mathbf1_b^{\mathsf T}
+v_rv_r^{\mathsf T}
-\frac q{K-1}(\mathbf1_bv_r^{\mathsf T}+v_r\mathbf1_b^{\mathsf T}).
\tag{4}
\]

For \(0<r<b\), the orthonormal basis \(e=\mathbf1_b/\sqrt b\), \(f=(v_r-(r/b)\mathbf1_b)/\sqrt D\) reduces \(M\) to the matrix

\[
\begin{pmatrix}A&H\\H&D\end{pmatrix}
\tag{5}
\]

and \(M\) is zero on the orthogonal complement. The same eigenvalue formula holds at \(r=0\) by direct rank-one calculation. Since its largest eigenvalue is at least \(D\), the centered-contrast mode dominates or ties the common-profile mode. Moreover, at least two blocks are available: choosing \(z_1=t\), \(z_2=-t\), all other \(z_i=0\), with \(t\) a top eigenvector of \(M\), **attains** the largest quotient \(\Lambda_m=\lambda_{\max}(M)/K\). Division by the coefficient \(m(n-m)/(n(n-1))\) from equation (3) proves the expression for \(\mathcal C_m\).

**3. Sharp uniform envelope and its equality cases.** Put \(T=m(n-m)/(b(K-1))\). If \(r=0\), then \(D=H=0\) and \(A=T\); therefore \(\lambda_{\max}(M)=T\). Its extremizing direction is constant within blocks, and nonzero block contrasts prove both sharpness and the equality characterization.

For \(0<r<b\), direct algebra gives \(T-A=KD/(K-1)>0\), and

\[
\det\!\left(TI_2-\begin{pmatrix}A&H\\H&D\end{pmatrix}\right)
=-\frac{D}{b(K-1)^2}\,\mathcal H(r),
\]
\[
\mathcal H(r)=-b^2q[K(K-q)-q]-br(K-2q)+r^2.
\]

The polynomial \(\mathcal H\) is strictly convex in \(r\), while

\[
\mathcal H(0)=-b^2q[K(K-q)-q]\le0,\qquad
\mathcal H(b)=b^2(q+1-K)[(K+1)q+1]\le0.
\]

These endpoint values cannot both vanish when \(K\ge2\) and \(0\le q\le K-1\); hence \(\mathcal H(r)<0\) throughout \(0<r<b\). Sylvester's criterion shows \(TI_2-M\) (in the two-dimensional representation (5)) is positive definite. Thus \(\lambda_{\max}(M)<T\), giving a strict partial-prefix gap. Finally,

\[
\frac{n(n-1)}{m(n-m)}\frac{T}{K}
=\frac{Kb-1}{K-1}.
\]

This completes the all-prefix bound and exact equality characterization.

**4. Block-boundary selection rule.** At \(m=qb\), the prefix is a uniform subset of \(q\) block means. The finite-population identity gives \(\mathcal R_{qb}^{\mathrm{block}}=(K-q)\sigma_{\mathrm{blk}}^2/[q(K-1)]\). By (3) and the orthogonal variance decomposition \(\sigma_{\mathrm{ind}}^2=\sigma_{\mathrm{blk}}^2+\sigma_{\mathrm{within}}^2\), the ratio and improvement threshold in the Finding follow.

## Verification

The accompanying standalone `CHECK.py` uses only Python's standard library and exact rational arithmetic. It enumerates uniform block permutations, independently evaluates the closed mean-square error, verifies the proposed uniform inequality across a range of integer block sizes and prefix lengths, and checks sharpness using block-constant data. Run `python3 CHECK.py`; the expected result is `OK 8260 exact checks`. A separate numerical spectrum computation compared the closed \(2\times2\) eigenvalue formula against directly assembled permutation-mask covariance matrices for \(2\le K\le4\) and \(2\le b\le5\). The proof is analytic; finite tests do not certify its universal quantifiers.

As a concrete exact benchmark, for \(K=b=3\) and scalar block values \(-1,0,1\) repeated three times within their respective blocks, the first complete block average has mean-square error \(2/3\). Fully uniform random reshuffling after the same three individual samples has mean-square error \(1/6\), a factor of exactly \(4=(9-1)/(3-1)\).

## Relationship to prior work

Nguyen, Phan, and Kalagnanam (2026) introduce block reshuffling and prove the exact individual-level and block-level without-replacement formulas (their Propositions 3.3 and 3.4). These compare variances of different sampling units. The present result instead holds the number \(m\) of **individual vector evaluations** fixed, treats every incomplete-block prefix, and determines a sharp worst-case spectral comparison for each \(m\). Their variance-decomposition identity supplies background, not the partial-prefix spectral result proved above.

The finite-population random-reshuffling identity is classical; Mishchenko, Khaled, and Richtárik (2020, Section 7) provide a direct derivation. Sampling whole clusters and the associated design effect are also classical. The block-boundary ratio and global best constant are consistent with that cluster-sampling theory and are **not asserted to be new on their own**. The assessed additional statement is the exact arbitrary-prefix profile, including the order-induced bias, attained spectral constant for each incomplete prefix, and strict separation of incomplete from complete prefixes for uniform block permutations with fixed internal ordering.

## Limitations

This is a mean-square statement at a fixed set of vectors or fixed-iterate gradients. It does not compare stochastic optimization iterates, guarantee convergence improvements, measure time or cache cost, or model adaptively selected permutations. Unequal block sizes, internal randomization, dependent block-selection rules, or gradients evolving during the epoch require different analyses. Although the accessible primary sources do not state the exact arbitrary-prefix spectral law, older results on partially sampled survey clusters may contain equivalent formulations; bibliographic novelty is not an independently validated fact.

## References

1. L. M. Nguyen, D. T. Phan, J. Kalagnanam, *Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization*, arXiv:2604.00260v1, first posted 2026-03-31, especially Sections 2.2 and 3.1 and Appendix A.1--A.3. https://arxiv.org/html/2604.00260v1
2. K. Mishchenko, A. Khaled, P. Richtárik, *Random Reshuffling: Simple Analysis with Vast Improvements*, arXiv:2006.05988v1, first posted 2020-06-10, especially Section 7 (finite-population lemma). https://ar5iv.labs.arxiv.org/html/2006.05988
3. R. Arnold, *Sample Surveys*, Chapter 11: Cluster Sampling, especially Sections 11.1--11.3 (classical complete-cluster design effects and two-stage sampling). https://homepages.ecs.vuw.ac.nz/~rarnold/STAT392/SampleSurveysBook/_book/cluster-sampling.html .
4. *Sampling Theory and Methods*, Pennsylvania State University, Lesson 7, https://online.stat.psu.edu/stat506/Lesson07 . Only search excerpts of this additional contextual source were accessible.
