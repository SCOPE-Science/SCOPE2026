# Distance-conditioned endpoint degree in bipartite uniform spanning trees: likelihood-ratio decay and a Rayleigh-scale crossover

## Finding

Let \(a,b\ge 2\). Choose a spanning tree \(\mathcal T\) uniformly from the labeled spanning trees of the complete bipartite graph \(K_{a,b}\), with parts \(A,B\) of sizes \(a,b\). Fix \(u\in A\), \(v\in B\), write \(H=\deg_{\mathcal T}(u)\), and define the integer half-distance \(T=(d_{\mathcal T}(u,v)-1)/2\). Then \(T\) ranges over \(0,\ldots,\min(a,b)-1\).

For \(t\) in this range set \(s=t+1\), \(B_t=b-s\), and \(C_t=s(a+b-s)\). The exact distance tail and conditional degree law are

\[
\Pr(T\ge t)=\prod_{j=1}^{t}\left(1-\frac ja\right)\left(1-\frac jb\right),
\]

\[
H\mid(T=t)\ \overset{d}=\ 1+\operatorname{Bin}\left(B_t-1,\frac1a\right)+\operatorname{Bern}\left(\frac b{C_t}\right),\qquad B_t\ge1,
\]

with independent summands. When \(B_t=0\), \(H=1\) surely. In particular, for every successive admissible pair, the conditional law at the longer distance is **strictly smaller in monotone likelihood-ratio order**:

\[
H\mid(T=t+1)\ <_{\mathrm{lr}}\ H\mid(T=t),\qquad 0\le t<\min(a,b)-1.
\]

Here likelihood-ratio order means that for any two supported values \(i<j\), \(p_{t+1}(i)p_t(j)\ge p_{t+1}(j)p_t(i)\), with at least one strict inequality; equivalently the ratio of the longer-distance mass to the shorter-distance mass decreases wherever both are positive. This gives negative covariance of \(T\) with every strictly increasing real function of \(H\).

The unconditional expected degree is \(1+(b-1)/a\). Its conditional deviation is exactly

\[
\delta_t:=\mathbb E[H\mid T=t]-\mathbb E[H]
=\frac b{s(a+b-s)}-\frac sa.
\]

Thus there is a unique real \(s_*\in(1,\min(a,b))\) solving

\[
s_*^2(a+b-s_*)=ab.
\]

The deviation is positive for \(s<s_*\), zero if an admissible integer \(s\) equals \(s_*\), and negative for \(s>s_*\). For example, in \(K_{20,20}\), it equals \(67/2220\) at distance five and \(-11/180\) at distance seven.

Set \(r_{a,b}=\sqrt{ab/(a+b)}\). If both part sizes diverge with their ratio bounded away from zero and infinity, then \(T/r_{a,b}\) converges to a Rayleigh variable with survival \(e^{-x^2/2}\). Moreover \(s_*/r_{a,b}\to1\), so the mean-degree sign change occurs at the mode of the limiting distance scale. More precisely, if \(b/(a+b)\to\theta\in(0,1)\) and \(t/r_{a,b}\to x\in(0,\infty)\), then

\[
r_{a,b}\delta_t\longrightarrow \theta\left(\frac1x-x\right).
\]

## Assumptions and scope

Every edge in the host graph has unit weight; a uniform spanning tree is one selected with equal probability among its \(a^{b-1}b^{a-1}\) spanning trees. The two marked vertices lie in opposite parts. Degrees count undirected tree edges. The strict ordering is asserted only when two distinct distance levels exist; \(a,b\ge2\) ensures this. The Bernoulli-plus-binomial expression is not used at the terminal value \(B_t=0\), where the conditional degree is deterministically one. The asymptotic assertions require both part sizes to diverge and a nondegenerate limiting ratio.

## Proof

**1. Counting completions of a fixed path.** Choose a particular simple \(u\)-to-\(v\) path \(P\) of length \(2t+1\), with \(s=t+1\) vertices in each part. Put \(A_t=a-s\), \(B_t=b-s\). Deleting its path edges from a tree containing \(P\) yields a rooted forest with the vertices of \(P\) as distinct roots. By the all-minors matrix-tree theorem, its number of completions is the determinant of the Laplacian restricted to vertices outside \(P\):

\[
F(A_t,B_t)=\det\begin{pmatrix}bI_{A_t}&-J_{A_t,B_t}\\-J_{B_t,A_t}&aI_{B_t}\end{pmatrix}
=b^{A_t}a^{B_t}\left(1-\frac{A_tB_t}{ab}\right).
\]

The formula also holds when either outside-part size is zero, by the empty-block determinant convention. The matrix determinant lemma (or a rank-one Schur complement) proves the displayed identity. There are \((a-1)_{\underline t}(b-1)_{\underline t}\) possible ordered paths. Dividing their total completion count by \(a^{b-1}b^{a-1}\), and noting \(ab-A_tB_t=C_t\), gives

\[
\Pr(T=t)=\frac{(a-1)_{\underline t}(b-1)_{\underline t}C_t}{(ab)^{t+1}}.
\]

Let \(S_t=\prod_{j=1}^t(1-j/a)(1-j/b)\). The preceding expression is \(S_t-S_{t+1}\), with \(S_0=1\) and \(S_{\min(a,b)}=0\). Telescoping proves the stated exact distance tail.

**2. The degree law.** On the fixed path \(P\), \(u\) has exactly one neighbor within \(P\). Let \(Z=H-1\) count its neighbors among the \(B_t\) opposite-part vertices outside the path. Requiring \(j\) specified such vertices to be neighbors of \(u\) appends \(j\) pendant edges to the forced tree. Deleting those edges makes their endpoints additional forest roots, so the number of completions is \(F(A_t,B_t-j)\). Consequently the conditional factorial moments, for \(0\le j\le B_t\), satisfy

\[
\mathbb E[(Z)_{\underline j}\mid P]
=(B_t)_{\underline j}\frac{F(A_t,B_t-j)}{F(A_t,B_t)}
=(B_t)_{\underline j}a^{-j}\left(1+\frac{A_tj}{ab-A_tB_t}\right).
\]

If \(B_t\ge1\), expand \(\mathbb E[z^Z]=\sum_j \mathbb E[(Z)_{\underline j}](z-1)^j/j!\) and factor:

\[
\mathbb E[z^Z\mid P]
=\left(1+\frac{z-1}{a}\right)^{B_t-1}
\left(1+\frac b{C_t}(z-1)\right).
\]

This proves the independent binomial/Bernoulli representation. It is identical for every path of the same length, proving the law conditional on \(T=t\). If \(B_t=0\), no other neighbor of \(u\) exists.

**3. Likelihood-ratio ordering.** The sequence \(q_t=b/C_t\) strictly decreases along the admissible distance levels, since \(C_{t+1}-C_t=a+b-2t-3>0\). For consecutive levels with \(B_t\ge2\), write \(W\sim\operatorname{Bin}(B_t-2,1/a)\) and take independent Bernoulli variables. Then \(H-1\mid(T=t)\) is \(W+\operatorname{Bern}(1/a)+\operatorname{Bern}(q_t)\), whereas \(H-1\mid(T=t+1)\) is \(W+\operatorname{Bern}(q_{t+1})\).

For a log-concave mass sequence \(w_k\), the ratio \(w_{k-1}/w_k\) increases with \(k\). Thus for \(0<q'<q\le1\), the laws \(W+\operatorname{Bern}(q')\) and \(W+\operatorname{Bern}(q)\) are likelihood-ratio ordered: their masses are \((1-q)w_k+qw_{k-1}\), and the ratio for \(q'\) versus \(q\) decreases with \(k\). A convolution of Bernoulli distributions is log-concave (this follows inductively by expanding adjacent \(2\times2\) determinants). The same mass-ratio argument shows \(Y\le_{\mathrm{lr}}Y+\operatorname{Bern}(1/a)\) for such a \(Y\). Applying the two comparisons proves the order, strictly. At a final level with \(B_t=1\), the next law is the point mass at one, which is strictly below the preceding law. First-order stochastic ordering and strict increasing-transform covariance follow.

**4. Crossover and Rayleigh scale.** By symmetry, the sum of the degrees of the \(a\) vertices in the first part is always \(a+b-1\). Therefore \(\mathbb E H=(a+b-1)/a\). Subtracting this from the conditional binomial/Bernoulli expectation gives \(\delta_t\), including the terminal case by direct substitution. Its sign is the sign of \(ab-s^2(a+b-s)\). The function \(s\mapsto s^2(a+b-s)\) is strictly increasing on \([1,\min(a,b)]\), and its values at the endpoints straddle \(ab\) for \(a,b\ge2\), proving uniqueness.

For the asymptotics, the exact tail gives

\[
\log\Pr(T\ge\lfloor xr_{a,b}\rfloor)
=\sum_{j=1}^{\lfloor xr_{a,b}\rfloor}\left[\log(1-j/a)+\log(1-j/b)\right]
\longrightarrow -x^2/2
\]

for every fixed \(x>0\); the quadratic Taylor remainders vanish when the part ratio is bounded. The equation for \(s_*\) is \((s_*/r_{a,b})^2(1-s_*/(a+b))=1\); the unique solution has \(s_*/r_{a,b}\to1\). Substitution \(s\sim xr_{a,b}\) into the exact deviation proves the stated scaled regression profile.

## Verification

The accompanying `verify_exact.py` enumerates every spanning tree of \(K_{a,b}\) for a documented finite set of small part sizes, independently computes distances and endpoint degrees, and compares exact rational distributions with the formulas. It also checks all distance probabilities, likelihood-ratio inequalities, conditional means, and the unique-switch property on additional parameter grids. Running `python verify_exact.py` produced `PASS 47930 exact assertions`. A further exact rational parameter sweep through both part sizes at most 34 checked 1,566,873 likelihood-ratio cross-products. These experiments test the formulas but do not replace the general determinant and ordering proofs.

## Relationship to prior work

Uniform spanning-tree probability and local edge-count methods are classical; see Pemantle's 2004 survey. Ge and Dong (arXiv:1904.07766, first posted April 16, 2019, Theorem 1.4 and Section 4) already counted spanning trees of a complete bipartite graph containing any fixed tree. Dong and Ge (arXiv:2103.05294, first posted March 9, 2021, Theorem 4) gave the corresponding formula for any fixed forest. Those results supply the enumerative input used here; neither the fixed-tree completion formula nor the elementary distance count is asserted as independently new. The contribution assessed here is the all-parameter strict likelihood-ratio comparison of the conditional endpoint degrees, together with the exact unique mean-bias crossing and its Rayleigh-scale localization. A separate complete-graph result concerning endpoint degree conditioned on distance is not a specialization of the bipartite model.

## Limitations

The result concerns a uniform spanning tree of a complete bipartite host graph and marked vertices in opposite parts; no claim is made for arbitrary host graphs, same-part marked vertices, nonuniform tree weights, or minimum spanning trees. The asymptotic regression profile is stated only in the balanced-divergence regime. Earlier general fixed-tree enumeration formulas make the conditional law accessible, so historical priority for the additional qualitative ordering remains subject to broader literature verification. Independent verification of scientific originality has not been performed.

## References

1. R. Pemantle, *Uniform random spanning trees*, arXiv:math/0404099 (first posted 2004-04-05). https://arxiv.org/abs/math/0404099
2. J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766 (first posted 2019-04-16). https://arxiv.org/abs/1904.07766
3. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294 (first posted 2021-03-09). https://arxiv.org/abs/2103.05294
