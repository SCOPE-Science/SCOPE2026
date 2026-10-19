# Positive covariance with nonmonotone root-degree regression in preferential attachment trees

## Finding

Start with one edge between vertices 1 and 2. For each integer \(n\geq2\), given the resulting tree on vertices \(1,\ldots,n\), attach vertex \(n+1\) to an existing vertex \(v\) with probability \(\deg_n(v)/[2(n-1)]\). Write \(D_n=\deg_n(1)\) and \(L_n=|\{v:\deg_n(v)=1\}|\). Define
\[
p_n=\frac{1}{4^{n-2}}\binom{2n-4}{n-2},\qquad n\ge2.
\]

**Theorem.** For every integer \(n\ge3\),
\[
\Pr(D_n=1)=\Pr(D_n=2)=p_n,
\qquad
\mathbb E[L_n\mid D_n=1]=\frac{2n}{3},
\]
\[
\mathbb E[L_n\mid D_n=2]=\frac{2n}{3}-\frac{2n-6}{2n-5}.
\]
In particular, for every \(n\ge4\), the conditional leaf-count regression falls strictly between the two equally likely lowest degrees, although the total covariance is strictly positive. Explicitly, for \(n\ge3\),
\[
\boxed{\operatorname{Cov}(D_n,L_n)=
\sum_{k=3}^{n-1}\left[
\frac{k-3}{3(k-1)}p_k+
\frac{2k-3}{3(k-1)^2}p_k^2
\right].}
\]
The sum is empty when \(n=3\). The covariance is zero for \(n=2,3\), positive for all \(n\ge4\), and equals \(1/16\) at \(n=4\). As \(n\to\infty\),
\[
\operatorname{Cov}(D_n,L_n)\sim\frac{2}{3\sqrt\pi}\sqrt n,
\qquad
\operatorname{Corr}(D_n,L_n)\sim
\sqrt{\frac{2}{\pi-2}}\,n^{-1/2}.
\]
The regression is not monotone in degree: at \(D_n=n-1\) the tree is a star and \(L_n=n-1\), which is greater than the conditional mean at degree 2 for \(n\ge4\).

## Assumptions and scope

All edges are undirected, all degrees are ordinary graph degrees, the seed is exactly the two-vertex edge, and each attachment probability uses the degree **before** adding the new edge. The leaf count includes both seed vertices whenever they remain leaves. The conditional degree-1 and degree-2 statements require \(n\ge3\); at \(n=2\), \(D_2=1\), \(L_2=2\) deterministically. No extra initial attractiveness, multiple edges per arrival, or alternative root initialization is permitted. The formulas are finite exact identities, except for the two explicitly stated limits.

## Proof

Write \(q_n=2(n-1)\), \(B_n=\mathbf 1\{n+1\text{ attaches to vertex }1\}\), and \(A_n=\mathbf 1\{n+1\text{ attaches to a leaf}\}\). The growth rule implies
\[
D_{n+1}=D_n+B_n,\qquad L_{n+1}=L_n+1-A_n,
\]
\[
\mathbb E(B_n\mid T_n)=D_n/q_n,\qquad
\mathbb E(A_n\mid T_n)=L_n/q_n.
\]
When vertex 1 is a leaf, it has degree 1. Consequently
\[
\mathbb E(B_n A_n\mid T_n)=\frac{\mathbf1\{D_n=1\}}{q_n}.
\]

**Degree and leaf means.** Put \(d_n=\mathbb E D_n\), \(m_n=\mathbb E L_n\), and \(p_n=\Pr(D_n=1)\). Since a root of degree 1 can remain so only by avoiding attachment,
\[
p_{n+1}=(1-q_n^{-1})p_n,
\quad d_{n+1}=(1+q_n^{-1})d_n,
\quad m_{n+1}=(1-q_n^{-1})m_n+1.
\]
The initial values are \(p_2=d_2=1\), \(m_2=2\). Induction gives
\[
p_n=4^{2-n}\binom{2n-4}{n-2},\quad
 d_n=(2n-3)p_n,\quad
 m_n=\frac23(n-1)+\frac43p_n.
\]

**Conditional regression at the two lowest root degrees.** For \(n\ge3\), set \(r_n=\Pr(D_n=2)\), \(u_n=\mathbb E[L_n\mathbf1\{D_n=1\}]\), and \(v_n=\mathbb E[L_n\mathbf1\{D_n=2\}]\). Conditional on degree 1, selecting the root preserves the number of leaves while raising its degree to 2; selecting a nonroot nonleaf raises the number of leaves by 1. Conditional on degree 2, selecting the root moves the root outside the tracked degree class. These cases yield
\[
\begin{aligned}
r_{n+1}&=(1-2/q_n)r_n+p_n/q_n,\\
u_{n+1}&=(1-2/q_n)u_n+p_n,\\
v_{n+1}&=(1-3/q_n)v_n+(1-2/q_n)r_n+u_n/q_n.
\end{aligned}
\]
At \(n=3\), \(r_3=p_3=1/2\) and \(u_3=v_3=1\). Substituting the previous recurrence for \(p_n\), direct induction gives
\[
r_n=p_n,\quad u_n=\frac{2n}{3}p_n,\quad
v_n=\left(\frac{2n}{3}-\frac{2n-6}{2n-5}\right)p_n.
\]
Division by \(p_n>0\) proves both conditional expectations and their strict difference \((2n-6)/(2n-5)>0\) for \(n\ge4\). The maximal root degree \(n-1\) occurs with positive probability when every arrival chooses the root; in that event the tree is a star, proving the nonmonotone-regression statement.

**Exact covariance and positivity.** Let \(t_n=\mathbb E[D_nL_n]\) and \(C_n=t_n-d_nm_n\). Expanding \((D_n+B_n)(L_n+1-A_n)\), using the three conditional expectations above, gives
\[
t_{n+1}=t_n+(1+q_n^{-1})d_n-q_n^{-1}p_n.
\]
Hence
\[
C_{n+1}=C_n+\frac{d_nm_n}{q_n^2}-\frac{p_n}{q_n}
=C_n+\frac{n-3}{3(n-1)}p_n+
\frac{2n-3}{3(n-1)^2}p_n^2.
\]
Since \(C_2=0\), and the increment at \(n=2\) is zero, summing from \(n=3\) proves the exact formula. Each summand is nonnegative for \(k\ge3\), and the second is strictly positive; this proves \(C_n>0\) for \(n\ge4\).

**Asymptotics and correlation.** Stirling's formula yields \(p_n\sim(\pi n)^{-1/2}\). In the covariance increment, the first term is asymptotic to \(p_n/3\) and the second is \(O(n^{-2})\). Integral comparison therefore gives \(C_n\sim 2\sqrt{n}/(3\sqrt\pi)\).

The degree second moment obeys
\[
\mathbb E[D_{n+1}^{2}]=(1+2/q_n)\mathbb E[D_n^2]+d_n/q_n,
\]
which, with its initial condition, gives
\[
\mathbb E[D_n^2]=2(n-1)-d_n,\qquad
\operatorname{Var}(D_n)=2(n-1)-d_n-d_n^2
\sim(2-4/\pi)n.
\]
Set \(V_n=\operatorname{Var}(L_n)\). Applying conditional variance to the Bernoulli increment \(1-A_n\) gives the exact recursion
\[
V_{n+1}=\left(1-\frac{1}{n-1}\right)V_n+
\frac{m_n}{q_n}\left(1-\frac{m_n}{q_n}\right).
\]
Because \(m_n/q_n\to1/3\), multiplying by \(n-1\) and telescoping shows \(V_n/n\to1/9\). Combining the two marginal variance limits with \(C_n\) proves the claimed correlation asymptotic.

## Verification

Run `python verify.py` with standard Python 3. The script independently enumerates every parent-selection history through nine vertices, weighting each history by its exact product of attachment probabilities rather than by a presumed joint-moment recurrence. It checks all exact mean, conditional, second-moment, and covariance identities against those independently enumerated probability spaces. Additional exact rational recurrences are compared through 79 vertices, followed by numerical checks of the derived asymptotic constants. At packaging, it completed 397 deterministic assertions. Finite checks corroborate; they do not substitute for the inductive and asymptotic proofs.

## Relationship to prior work

Preferential attachment and its degree-count statistics are classical. Krapivsky and Redner (2002) derive exact finite-network statistics for global degree-one counts and some covariances among *global* degree counts; they do not identify the present distinguished-root mixed moment. Brightwell and Luczak (2010) study evolving degrees and degree-count concentration in the same degree-proportional tree. Peköz, Röllin, and Ross (2014) treat joint limits of finitely many *individual* vertex degrees, which do not determine the joint law with an extensive leaf count. Hartle and Krapivsky (2026) calculate extensive leaf statistics and joint degree/leafdegree profiles, not this root-degree conditional regression. The finding is the combination of an exact positive root/global covariance with a strict initial fall in its conditional regression, together with its scaling law; neither marginal degree formulas nor aggregate degree-count covariances alone imply that combination.

## Limitations

The result applies only to the seed-edge, one-new-edge, degree-proportional model. It does not assert analogous signs under different attachment kernels or initial graphs. It supplies mixed first and second moments, not a full bivariate law or a bivariate central limit theorem. Its mathematical priority is provisionally assessed from accessible sources; earlier implicit derivations, especially in work on plane-oriented recursive trees and branch leaves, cannot be excluded without additional archival comparison. No independent validation or audit has been performed.

## References

1. P. L. Krapivsky and S. Redner, *Finiteness and Fluctuations in Growing Networks*, arXiv:cond-mat/0207107, first submitted 2002-07-03; J. Phys. A 35 (2002), 9517–9534.
2. G. Brightwell and M. J. Luczak, *Vertices of High Degree in the Preferential Attachment Tree*, arXiv:1012.5550, first submitted 2010-12-26.
3. E. A. Peköz, A. Röllin, and N. Ross, *Joint Degree Distributions of Preferential Attachment Random Graphs*, arXiv:1402.4686, first submitted 2014-02-19; Adv. Appl. Probab. 49 (2017), 368–387.
4. H. Hartle and P. L. Krapivsky, *Leaves of Preferential Attachment Trees*, arXiv:2602.01021, first submitted 2026-02-01.
5. H. M. Mahmoud, R. T. Smythe, and J. Szymański, *On the Structure of Random Plane-Oriented Recursive Trees and Their Branches*, Random Structures & Algorithms 4 (1993), 151–176, DOI:10.1002/rsa.3240040204 (abstract consulted; full text not inspected).
