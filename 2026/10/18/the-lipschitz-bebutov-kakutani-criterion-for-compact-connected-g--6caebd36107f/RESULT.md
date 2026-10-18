# The Lipschitz Bebutov–Kakutani criterion for compact connected groups

## Finding

**Theorem.** Let \(G\) be any compact connected metrizable topological group, not necessarily a Lie group. Let \(d\) be **any compatible right-invariant metric** on \(G\). Let \(X\) be any compact metrizable space with a continuous left \(G\)-action. The following are equivalent:

1. The fixed-point set \(\operatorname{Fix}(X,G)\) admits a topological embedding into \([0,1]\).
2. There is a topological \(G\)-equivariant embedding \(X\hookrightarrow\operatorname{Lip}_1(G,[0,1])\), where the target consists of functions satisfying \(|u(g)-u(h)|\le d(g,h)\) and carries the right-argument action \((a\cdot u)(g)=u(ga)\).

This establishes the compact-connected case of Problem 1.3 in Gutman–Huo–Ouyang (2026), without a finite-dimensional Lie-group assumption. It includes, for example, the infinite product \(G=\prod_{j\ge1}\mathbb T\) and connected compact solenoids.

The central ingredient is also valid **without connectedness**: for every compact metrizable group with any compatible right-invariant metric, there exists a positive, constant-preserving, injective linear convolution operator \(Q:C(G,\mathbb R)\to\operatorname{Lip}(G,\mathbb R)\) that commutes with right translations and satisfies
\[
\operatorname{Lip}_d(Qf)\le L\inf_{c\in\mathbb R}\|f-c\|_\infty
\]
for a finite constant \(L\) depending only on \(G,d\).

## Assumptions and scope

A compact metrizable group has normalized Haar probability \(m\). The metric is right-invariant in the literal sense \(d(xb,yb)=d(x,y)\) for all \(x,y,b\in G\); it need not be bi-invariant, geodesic, or induced by a smooth structure. The action on \(X\) is jointly continuous. The target has its uniform topology, equivalent here to the compact-open topology. The theorem does not apply to noncompact or disconnected groups without additional hypotheses.

For scalar functions, define convolution by
\[
(f*g)(x)=\int_G f(a)g(a^{-1}x)\,dm(a),
\qquad f^*(x)=\overline{f(x^{-1})}.
\]
The displayed \(f^*\) is used only to define the kernel; all resulting kernels and final observables are real-valued.

## Proof

**1. Positive Lipschitz approximate identities.** Choose \(r_n>0\) decreasing to zero. Write \(e\) for the identity and set
\[
b_n(g)=\left(1-\frac{d(g,e)}{r_n}\right)_+,
\quad c_n=\int_G b_n\,dm>0,
\quad u_n=\frac{b_n}{c_n}.
\]
The positivity of \(c_n\) follows from full support of Haar measure and continuity at \(e\). The functions \(u_n\) are nonnegative, continuous, \(d\)-Lipschitz, have integral one and support in the closed \(r_n\)-ball about \(e\). Consequently, for every continuous finite-dimensional unitary representation \(\pi\) of \(G\),
\[
\widehat u_n(\pi):=\int_G u_n(g)\pi(g)\,dm(g)\longrightarrow I
\]
in operator norm, by continuity of \(\pi\) at the identity.

**2. Correlations remain Lipschitz for an arbitrary right-invariant metric.** Let
\[
k_n=u_n*u_n^*,\qquad
k_n(x)=\int_G u_n(xb)u_n(b)\,dm(b).
\]
The equality uses a left-Haar change of variables; Haar measure is bi-invariant because \(G\) is compact. Thus \(k_n\ge0\), \(\int k_n\,dm=1\), and
\[
|k_n(x)-k_n(y)|
\le\int_G |u_n(xb)-u_n(yb)|u_n(b)\,dm(b)
\le\operatorname{Lip}_d(u_n)d(x,y).
\]
Importantly, this estimate needs **right** invariance only; it does not assert that inversion is an isometry.

Choose positive numbers \(w_n\) with \(\sum_n w_n=1\) and
\[
\sum_n w_n\bigl(\|u_n\|_\infty+\operatorname{Lip}_d(u_n)\bigr)<\infty.
\]
For instance, normalize the sequence \(2^{-n}/(1+\|u_n\|_\infty+\operatorname{Lip}_d(u_n))\). Then
\[
k=\sum_{n\ge1}w_nk_n
\]
converges uniformly and in Lipschitz seminorm; it is a nonnegative real Lipschitz probability density.

**3. Every irreducible Fourier block of the kernel is invertible.** Fix an irreducible continuous unitary representation \(\pi\) and use the convention \(\widehat f(\pi)=\int f(g)\pi(g)\,dm(g)\). Then convolution respects matrix multiplication, and
\[
\widehat{k_n}(\pi)
=\widehat u_n(\pi)\widehat u_n(\pi)^*\succeq0.
\]
Since \(\widehat u_n(\pi)\to I\), at least one, in fact all sufficiently late, of these matrices is strictly positive definite. Therefore
\[
\widehat k(\pi)
=\sum_{n\ge1}w_n\widehat{k_n}(\pi)\succ0
\]
for **every** irreducible \(\pi\). No uniform lower bound across all representations is required.

**4. An information-preserving Lipschitz convolution filter.** Define \(Qf=k*f\). Its positivity and \(Q1=1\) follow from the normalization of \(k\). Associativity of left convolution with right-argument translations gives \(Q R_a=R_a Q\). The change of variables \(b=a^{-1}x\) gives
\[
Qf(x)=\int_G k(xb^{-1})f(b)\,dm(b).
\]
Hence right invariance implies \(\operatorname{Lip}_d(Qf)\le\operatorname{Lip}_d(k)\|f\|_\infty\). Since constants map to constants, replace \(f\) by \(f-c\) to get the asserted estimate with \(L=\operatorname{Lip}_d(k)\).

If \(Qf=0\), then for every irreducible \(\pi\),
\(\widehat k(\pi)\widehat f(\pi)=0\). Step 3 implies \(\widehat f(\pi)=0\). The Peter–Weyl density theorem then forces \(f=0\), proving injectivity on all of \(C(G,\mathbb R)\).

**5. Upgrade the classical continuous embedding.** The connected locally compact Bebutov–Kakutani theorem of Jaworski and Chen supplies, from condition 1, a continuous equivariant embedding \(J_{f_0}:X\to C(G,[0,1])\), where \(J_{f_0}(x)(g)=f_0(gx)\). (For compact \(G\), a bounded real-valued version can equivalently be affinely rescaled into \([0,1]\).) Pick
\[
0<\varepsilon\le\min\left\{1,\frac{2}{1+L}\right\},\qquad
f_\varepsilon=\frac12+\varepsilon\left(f_0-\frac12\right).
\]
Set \(F(x)=Q(J_{f_\varepsilon}(x))\). Since \(Q\) is positive and fixes constants, \(F(x)(G)\subset[0,1]\). Centering the integrand at \(1/2\) gives
\[
\operatorname{Lip}_d(F(x))
\le\frac{\varepsilon L}{2}\le1.
\]
The map \(F\) is continuous and equivariant because \(Q\) has both properties; it is injective because \(Q\) is injective and \(J_{f_\varepsilon}\) was an embedding. Compactness of \(X\) and the Hausdorff target make \(F\) a topological embedding.

**6. Necessity.** A function fixed by every right-argument shift is constant on \(G\). Therefore the fixed-point space of \(\operatorname{Lip}_1(G,[0,1])\) is canonically \([0,1]\). An equivariant embedding restricts to an embedding of \(\operatorname{Fix}(X,G)\) into this interval, proving condition 1.

## Verification

The analytic proof verifies all quantifiers, including non-Lie compact metrizable groups, arbitrary compatible right-invariant metrics, possibly nonfree actions, and nonabelian irreducible Fourier blocks. The supporting standard-library script `examples/check_convolution.py` performs exact-rational finite-group checks on the cyclic group of order five and the nonabelian symmetric group of degree three. It confirms normalization, convolution injectivity via an exact nonsingular matrix, equivariance and the Lipschitz estimate. Finite checks are diagnostics, **not** a substitute for Peter–Weyl or the general proof.

## Relationship to prior work

Gutman, Huo, and Ouyang (arXiv:2610.13091v1, Theorem 1.1 and Problem 1.3) prove the Lipschitz criterion for connected Lie groups and explicitly ask whether it extends to connected second-countable locally compact groups. The present theorem settles their question on the compact connected branch, including non-Lie groups. Their heat-semigroup injective smoother is replaced by a Haar-convolution construction with strictly positive Fourier blocks.

The older Jaworski–Chen theorem gives embedding into **continuous** function shifts for connected locally compact groups; it is used as an input rather than claimed anew. Gutman–Huo–Tsukamoto (arXiv:2510.08706v1) treat Lipschitz shifts for Euclidean actions, while Gutman–Huo (arXiv:2505.14653v2) give a Borel, not a continuous topological, embedding for arbitrary locally compact group actions. None of these statements implies the compact non-Lie Lipschitz criterion merely by substituting a group parameter. The Peter–Weyl theorem and positive-definite correlation kernels are classical ingredients.

## Limitations

This proof does not settle Problem 1.3 for noncompact non-Lie groups or extend the fixed-point criterion to disconnected groups. The smoothing kernel is existential and generally lacks uniform representation-independent spectral conditioning; inverse continuity is used only on compact image sets. Older harmonic-analysis literature might contain equivalent injective Lipschitz convolution constructions, and a separately formulated dynamical corollary could exist outside the sources inspected. The result has undergone only self-review, not independent audit.

## References

1. Y. Gutman, Q. Huo, K. Ouyang, *A Lipschitz refinement of the Bebutov–Kakutani dynamical embedding theorem for connected Lie group actions*, arXiv:2610.13091v1, first posted 2026-10-09. https://arxiv.org/html/2610.13091v1
2. Y. Gutman, Q. Huo, M. Tsukamoto, *A Lipschitz Refinement of the Multidimensional Bebutov–Kakutani Dynamical Embedding Theorem*, arXiv:2510.08706v1 (2025). https://arxiv.org/html/2510.08706v1
3. Y. Gutman, Q. Huo, *On the representation of measurable and continuous dynamical systems by Lipschitz functions*, arXiv:2505.14653v2 (2026 revision). https://arxiv.org/html/2505.14653v2
4. A. Jaworski, *The Kakutani–Bebutov theorem for groups*, PhD thesis, University of Maryland (1974); S. Chen, *An extension of the Kakutani–Beboutov system*, J. Differential Equations 18 (1975), 275–276. Their connected locally compact theorem is quoted and discussed in references 1–3.
5. Peter–Weyl density and Fourier decomposition for compact Hausdorff groups (classical theorem).
