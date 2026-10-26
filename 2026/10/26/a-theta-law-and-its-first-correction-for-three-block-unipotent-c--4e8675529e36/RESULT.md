# A theta law and its first correction for three-block unipotent commutativity

## Finding

For a prime power \(q\) and an integer \(m\geq1\), let \(G_m(q)\) be the group of block matrices

\[
\begin{pmatrix}
 I_{2m}&A&C\\0&I_m&B\\0&0&I_{2m}
\end{pmatrix},
\quad
 A\in M_{2m\times m}(\mathbb F_q),\quad
 B\in M_{m\times2m}(\mathbb F_q),\quad
 C\in M_{2m}(\mathbb F_q).
\]

Choose \(g,h\) independently and uniformly from this group. Define \(X=[A_g\; -A_h]\in M_{2m}(\mathbb F_q)\), and condition on \(gh=hg\). Write \(T_m=\operatorname{rank}(X)-m\). Introduce

\[
\Phi_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\qquad
\Phi_\infty(q)=\prod_{i=1}^{\infty}(1-q^{-i}),
\]
\[
\Theta(q)=\sum_{t\in\mathbb Z}q^{-t^2},\qquad
\Xi(q)=\sum_{t\in\mathbb Z}q^{-t^2+t}.
\]

**Theorem.** For every \(q\) and \(m\) as above, the exact commutativity probability is

\[
\operatorname{cp}(G_m(q))
 =q^{-3m^2}\sum_{t=-m}^{m}q^{-t^2}
 \frac{\Phi_{2m}(q)^2}{\Phi_{m+t}(q)\Phi_{m-t}(q)^2}.
\tag{1}
\]

Let \(k(G_m(q))\) count conjugacy classes. At fixed \(q\), as \(m\to\infty\),

\[
\boxed{\quad
k(G_m(q))
=\frac{q^{5m^2}}{\Phi_\infty(q)}
\left[\Theta(q)-\frac{3\Xi(q)}{(q-1)q^m}
+O_q(q^{-2m})\right].\quad}
\tag{2}
\]

The law of \(T_m\), conditioned on commutativity, converges in total variation at rate \(O_q(q^{-m})\) to the discrete-theta law

\[
\pi_q(t)=\frac{q^{-t^2}}{\Theta(q)},\qquad t\in\mathbb Z.
\tag{3}
\]

The finite-dimensional asymmetry survives one order deeper:

\[
\boxed{\quad
\mathbb E[T_m\mid gh=hg]
=-\frac{\Xi(q)}{2(q-1)\Theta(q)}q^{-m}
+O_q(q^{-2m}).\quad}
\tag{4}
\]

The leading discrete-theta limit is symmetric, but the first nonzero mean correction is strictly negative. Formula (2) gives a two-term expansion of the number of conjugacy classes of the specified three-block parabolic unipotent radical.

## Assumptions and scope

The field has any prime-power order \(q\ge2\), including even characteristic. The block dimensions are exactly \((2m,m,2m)\), with integer \(m\ge1\). The asymptotic statements keep the field fixed as \(m\) tends to infinity; constants in the error terms may depend on \(q\). The group is the unipotent radical of the standard three-block parabolic in \(\mathrm{GL}_{5m}(\mathbb F_q)\), not the full parabolic subgroup. The rank statistic is attached to an ordered commuting pair of group elements; it is not claimed to be a statistic of one conjugacy class.

## Proof

**1. Reduction to a zero product.** Multiplying two displayed block matrices shows that their commutator is trivial if and only if

\[
A_gB_h-A_hB_g=0.
\]

Put \(Y=\begin{bmatrix}B_h\\B_g\end{bmatrix}\). The map from the four independent off-diagonal blocks to \((X,Y)\) is a linear bijection onto two independent uniformly sampled matrices in \(M_{2m}(\mathbb F_q)\), and the commutation condition is exactly \(XY=0\). The central blocks \(C_g,C_h\) are unrestricted, so they cancel in the probability.

**2. Exact rank enumeration.** Let \(n=2m\). The number of \(n\times n\) matrices of rank \(s\) is

\[
R_n(s)= {n\brack s}_q\prod_{i=0}^{s-1}(q^n-q^i)
=q^{s(2n-s)}\frac{\Phi_n(q)^2}{\Phi_s(q)\Phi_{n-s}(q)^2}.
\tag{5}
\]

Here \({n\brack s}_q\) is the Gaussian binomial coefficient. To verify the count, first choose an \(s\)-dimensional image and then choose a surjective map from an \(n\)-space onto it. Given \(X\) of rank \(s\), exactly \(q^{n(n-s)}\) matrices \(Y\) satisfy \(XY=0\), because each column of \(Y\) lies in the \((n-s)\)-dimensional kernel of \(X\). Dividing by the \(q^{2n^2}\) possible ordered matrix pairs and setting \(s=m+t\) gives (1), including the boundary ranks \(s=0\) and \(s=n\).

The group has \(|G_m(q)|=q^{8m^2}\). The standard class-counting identity \(k(G)=|G|\operatorname{cp}(G)\) therefore converts (1) into the *exact* conjugacy-class count

\[
k(G_m(q))
=q^{5m^2}\sum_{t=-m}^{m}q^{-t^2}
\frac{\Phi_{2m}(q)^2}{\Phi_{m+t}(q)\Phi_{m-t}(q)^2}.
\tag{6}
\]

In particular, the number of conjugacy classes here equals the integer number of ordered pairs \((X,Y)\) of \(2m\)-square matrices with \(XY=0\).

**3. A uniform product expansion.** Write

\[
Q_j(q)=\prod_{i>j}(1-q^{-i}),\qquad
\alpha_q=\frac1{1-q^{-1}},\qquad j\ge0.
\]

Then \(\Phi_j=\Phi_\infty/Q_j\), and the elementary product inequality with the inclusion-exclusion remainder gives, uniformly for all integers \(j\ge0\),

\[
Q_j=1-\alpha_q q^{-j-1}+O_q(q^{-2j-2}).
\tag{7}
\]

Indeed, the omitted tail sum is \(\sum_{i>j}q^{-i}=\alpha_q q^{-j-1}\); the combined terms of degree at least two in its product are bounded in absolute value by a constant times the square of that sum. Also \(Q_{2m}^{-2}=1+O_q(q^{-2m})\), and \(Q_j\in[\Phi_\infty,1]\). Thus, uniformly for \(|t|\le m\),

\[
\frac{\Phi_{2m}^2}{\Phi_{m+t}\Phi_{m-t}^2}
=\frac1{\Phi_\infty}\left[
1-\alpha_q q^{-m-1}(q^{-t}+2q^t)
+O_q\big(q^{-2m}(1+q^{2|t|})\big)\right].
\tag{8}
\]

The uniform error follows by multiplying three factors of (7); no assumption that \(t\) is fixed is required. Upon multiplying by \(q^{-t^2}\), the error is summable over all integers because

\[
\sum_{t\in\mathbb Z}q^{-t^2}(1+q^{2|t|})<\infty.
\]

The tails of the displayed theta sums beyond \(|t|=m\) are \(O_q(q^{-(m+1)^2+m+1})\), hence are absorbed by the \(O_q(q^{-2m})\) error. Symmetry under \(t\mapsto-t\) yields

\[
\sum_{t\in\mathbb Z}q^{-t^2}(q^{-t}+2q^t)=3\Xi(q).
\]

Using (8) in (6), and the identity \(\alpha_qq^{-m-1}=q^{-m}/(q-1)\), proves (2).

**4. Conditioned limit and first bias.** Given \(XY=0\), the probability of \(T_m=t\) is the \(t\)-th nonnegative summand of (1), divided by the sum, and zero outside \([-m,m]\). The same product expansion (8), now summed in absolute value, shows that the unnormalized weights differ in \(\ell^1(\mathbb Z)\) from \(q^{-t^2}/\Phi_\infty(q)\) by \(O_q(q^{-m})\). The normalizer tends to \(\Theta(q)/\Phi_\infty(q)>0\). This establishes (3) with the stated total-variation error.

Because the corresponding error is still summable after multiplying each term by \(|t|\), the same expansion gives a numerator for the conditional mean of

\[
-\frac{\alpha_q q^{-m-1}}{\Phi_\infty(q)}
\sum_{t\in\mathbb Z}tq^{-t^2}(q^{-t}+2q^t)
+O_q(q^{-2m}).
\]

The first-order sum equals \(\Xi(q)/2\): the first component is the negative of \(\sum_t tq^{-t^2+t}\), and the latter equals \(\Xi(q)/2\) by the involution \(t\mapsto1-t\). Dividing by the normalizer \(\Theta/\Phi_\infty+O_q(q^{-m})\) proves (4). The positive factors in its coefficient show that the leading bias is strictly negative for every \(q\).

## Verification

The accompanying dependency-free Python checker exhausts all \(q^8\) ordered pairs of \(2\times2\) matrices for each of \(q=2,3,4\), using the polynomial-basis model of \(\mathbb F_4\). It independently computes ranks, products, and the rank-stratum counts predicted by (5). Separately, it enumerates conjugacy orbits of the actual five-dimensional three-block groups by the translation action on the central block, recovering exactly 58, 417, and 1636 classes over the three fields. It also enumerates all \(2^{16}\) matrices of size \(4\times4\), checks their rank counts, and counts zero products by the kernel-size formula. For several increasing dimensions it compares the exact normalized rank sum against the first-correction approximation in (2). The checker is a finite test of the enumeration and the anticipated asymptotic scaling; it is not an infinite proof.

Run `python3 verify_threeblock.py`. Expected final line: `THREE_BLOCK_COMMUTING_THETA_CHECKS_PASSED`. The plain-text log `verification_output.txt` records the actual executed results.

## Relationship to prior work

The group is a concrete three-block unipotent radical studied structurally in the context of parabolic conjugacy; Goodwin and Röhrle proved that the number of conjugacy classes of unipotent radicals for parabolics with flags of length at most five is a polynomial in the field order. That result includes this *family's polynomiality* but does not state its growing-block-size two-term theta asymptotic or the conditional rank law and signed bias. Their theorem is fully credited, not reasserted as new.

Cocke and Ho study general probability distributions of finite-group word maps, including the relevance of commutator fibers; the present specialized quantitative limit is not among their theorems. Fulman and Guralnick count commuting matrix pairs in classical Lie algebras, not the group family in (1). Huang studies **mutually annihilating** pairs satisfying both \(XY=YX=0\), whereas the displayed group commutator reduces to the *one-sided* equation \(XY=0\). The elementary count of matrices of fixed rank and the equivalence between group commutativity probability and class count are standard and are not claimed as new.

Kousidis established theta-function asymptotics for Gaussian-binomial and generalized flag-count sums. Thus neither theta notation nor the general phenomenon of theta asymptotics is new. The present specific contribution is the two-term expansion and conditioned rank law, including its signed finite-size bias, for the three-block group above. The preceding comparisons concern mathematical implications rather than solely shared vocabulary.

## Limitations

The field is fixed while the block parameter grows; no simultaneous large-field bound is claimed. The theorem treats the ratio of block dimensions \((2:1:2)\) only, and it does not classify individual conjugacy classes or higher commutator-word fibers. The exact finite sum arises from classical rank enumeration, and the theta function is classical; significance rests on the specific group statistic and correction/conditional law. Literature coverage is not exhaustive. In particular, a different expression for the same class number in older parabolic-group enumeration could imply (6), and a previously unindexed weighted-rank asymptotic could imply (2)–(4). Independent mathematical evaluation has not been performed.

## References

1. W. Cocke and M.-C. Ho, *The Probability Distribution of Word Maps on Finite Groups*, arXiv:1807.07111 (first public 2018-07-18), Sections 1–3.
2. S. M. Goodwin and G. Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of \(\mathrm{GL}_n(q)\)*, arXiv:0901.0667 (2009), Theorem 1.2 and Section 3.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016), Theorem 1.1 and Section 2.
4. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first public 2021-10-29), Section 3.1.
5. S. Kousidis, *Asymptotics of generalized Galois numbers via affine Kac–Moody algebras*, arXiv:1109.2546 (2011), Theorem 3.2 and Corollary 3.6.
