# Exact cherry–cophenetic covariance and rapid decorrelation in Yule trees

## Finding

For a Yule–Harding–Kingman random rooted binary tree with \(n\ge 2\) leaves, let \(C_n\) count cherries (internal vertices with two leaf children), and let \(\Phi_n\) be the total cophenetic index, the sum of depths of the lowest common ancestors of all unordered pairs of distinct leaves, with root depth zero. The exact mixed covariance is

\[
\operatorname{Cov}(C_n,\Phi_n)=-\frac{(n-3)(5n-8)}{9(n-1)}\qquad(n\ge3),
\]

with covariance zero at \(n=2\). It vanishes at \(n=3\), is strictly negative for every \(n\ge4\), and equals \(-5n/9+O(1)\) as \(n\to\infty\). Using the established marginal Yule variance asymptotics \(\operatorname{Var}(C_n)\sim 2n/45\) and \(\operatorname{Var}(\Phi_n)\sim n^4/12\),

\[
 n^{3/2}\operatorname{Corr}(C_n,\Phi_n)\longrightarrow -\frac{5\sqrt{30}}{3}.
\]

The unusually rapid vanishing of the normalized correlation contrasts with the linear growth of the exact covariance.

## Assumptions and scope

The distribution is the standard pure-birth Yule tree-shape distribution: begin with two leaves and repeatedly choose a leaf uniformly and split it into two leaves. Equivalently, the two daughter-subtree leaf counts at the root of an \(n\)-leaf tree are \(k\) and \(n-k\), where \(k\) is uniform on \(\{1,\ldots,n-1\}\), and, conditional on the split, the daughter subtrees are independent Yule trees. Root orientation, leaf labels, and any arbitrary left/right ordering do not change the two statistics. Depth counts tree edges. The formula concerns the **standard, unconditioned Yule distribution**, not the uniform distribution on labeled phylogenetic topologies or the uniform Catalan distribution.

## Proof

Write \(c_n=\mathbb E C_n\), \(p_n=\mathbb E\Phi_n\), and \(K_n=\operatorname{Cov}(C_n,\Phi_n)\). For daughter-subtree sizes \(k\) and \(j=n-k\), and \(n\ge3\), the additive recurrences are

\[
 C_n=C_k+C_j,\qquad \Phi_n=\Phi_k+\Phi_j+\binom{k}{2}+\binom{j}{2}.
\]

The second identity holds because each leaf pair inside a daughter subtree has its common-ancestor depth increased by one; cross-daughter pairs have lowest common ancestor at the root. At \(n=1\), \(c_1=p_1=0\); at \(n=2\), \(c_2=1,p_2=0\). The uniform-split recurrences imply, for \(n\ge3\),

\[
 c_n=\frac n3,\qquad p_n=n(n-1)-2n(H_n-1),\qquad H_n=\sum_{j=1}^n\frac1j.
\]

The \(p_n\) identity holds also for \(n=1,2\). Define

\[
 W_n(k)=p_k+p_{n-k}+\binom{k}{2}+\binom{n-k}{2}.
\]

Conditional independence and total covariance give, for \(n\ge3\),

\[
 K_n=\frac{2}{n-1}\sum_{k=1}^{n-1}K_k+
 \operatorname{Cov}_{U_n}\big(c_k+c_{n-k},W_n(k)\big),
\]

where \(U_n\) is uniform on \(k=1,\dots,n-1\). Here \(K_1=K_2=K_3=0\). For \(n\ge4\), the departure of \(c_k+c_{n-k}\) from its constant linear baseline \(n/3\) is concentrated at \(k=1,2,n-2,n-1\): the correction at size one is \(-1/3\), and at size two is \(+1/3\). These corrections sum to zero, including their coinciding positions for \(n=4\). The symmetry \(W_n(k)=W_n(n-k)\) therefore yields

\[
 R_n:=\operatorname{Cov}_{U_n}\big(c_k+c_{n-k},W_n(k)\big)
 =\frac{2}{3(n-1)}\big(W_n(2)-W_n(1)\big).
\]

Substitution of the displayed \(p_n\) formula yields

\[
 W_n(2)-W_n(1)=2H_{n-2}-3n+7,
 \quad R_n=\frac{2(2H_{n-2}-3n+7)}{3(n-1)}.
\]

We now prove the stated covariance by induction on \(n\). It holds for \(n=3\). Supposing it holds for all smaller indices, the sum of the preceding covariance terms simplifies to

\[
 \sum_{k=3}^{n-1}K_k=-\frac19\left(\frac52n(n-1)-18n+33+6H_{n-2}\right).
\]

Insert this and \(R_n\) into the total-covariance recurrence. The harmonic terms cancel exactly, giving

\[
 K_n=-\frac{5n^2-23n+24}{9(n-1)}
 =-\frac{(n-3)(5n-8)}{9(n-1)}.
\]

For \(n\ge4\), both numerator factors are positive, so the covariance is negative. The asymptotic covariance and correlation follow from this expression and the cited marginal variance asymptotics.

## Verification

The standalone standard-library program `verify_yule_cherry_cophenetic.py` computes the exact distribution of unordered Yule tree shapes through fourteen leaves by uniformly splitting each available leaf. It separately computes the cophenetic index as the sum of common prefixes of all pairs of leaf paths through eleven leaves. It tests the exact covariance, marginal means, and a separately implemented root-split mixed-moment recurrence through 300 leaves. Its recorded run passed 4,746 exact rational/integer assertions. Those finite computations check the derivation but do not replace the induction proof.

To reproduce: `python3 verify_yule_cherry_cophenetic.py`.

## Relationship to prior work

Cardona, Mir, and Rosselló (2012, arXiv:1202.6573v1) establish exact Yule moments and variances for the total cophenetic index, and analyze its relationship with the Sackin and Colless indices. Wu and Choi (2015, arXiv:1508.03139v1) establish joint laws for cherries and pitchforks under evolutionary tree models. Their inspected statements supply relevant marginal and nearby joint information, but neither supplies the cherry–cophenetic mixed covariance above. The standard Yule/BST correspondence transports some other cherry–path-length formulas, but the cophenetic sum is not determined by the Sackin index; those earlier mixed moments do not imply this claim.

## Limitations

The statement is confined to the standard Yule leaf-splitting distribution. It does not establish analogous formulas under conditioned birth-death, uniform topology, or uniform Catalan models. The originality comparison is based on specifically inspected primary works and related indexed results; additional older literature could contain an equivalent expression. The analytical theorem needs no finite-enumeration extrapolation. The correlation asymptotic invokes known marginal variance asymptotics rather than reproving their full formulas here.

## References

- Cardona, G., Mir, A., and Rosselló, F. (2012). *Exact formulas for the variance of several balance indices under the Yule model*. arXiv:1202.6573v1. https://arxiv.org/abs/1202.6573
- Wu, T., and Choi, K. P. (2015). *On joint subtree distributions under two evolutionary models*. arXiv:1508.03139v1. https://arxiv.org/abs/1508.03139
