# Strict likelihood-ratio ordering of normalized heat kernel gaps on Hamming graphs

## Finding

On the unweighted graph \(H(d,q)=K_q^{\square d}\), with integers \(d,q\ge2\), let \(p_s(k)=(e^{-sL})_{uv}\) where the vertices have Hamming distance \(k\) and \(L\) is the combinatorial Laplacian. For \(1\le k\le d\), define the probability density on positive times
\[
 f_k(s)=\frac{p_s(0)-p_s(k)}{\int_0^\infty[p_v(0)-p_v(k)]\,dv}.
\]
For every \(1\le k<d\), \(f_{k+1}/f_k\) is strictly increasing on \((0,\infty)\). In particular, the normalized heat gap at larger separation has strictly higher upper-tail probability at every positive time, and strictly higher expectation for every increasing test function with finite expectations that is not almost everywhere constant.

For a spectral consequence, let \(G_\alpha\) act as \(\lambda^{-\alpha}\) on each positive Laplacian eigenspace and as zero on the constants, and set \(\delta_\alpha(k)=(G_\alpha)_{uu}-(G_\alpha)_{uv}\) for \(d_H(u,v)=k\). For **every real \(\alpha>1\)** the ratio \(\delta_\alpha(k)/\delta_1(k)\) is strictly increasing in \(k\). This distinguishes the higher inverse-Laplacian spectral distances relative to effective resistance, not just their unnormalized magnitudes. At \(\alpha=2\) the ratio is the mean under \(f_k\), and is precisely the second distance-dependent correction to the two-leader grounded inverse trace.

## Proof

Put \(N=q^d\), \(x=e^{-qs}\), \(h(x)=1+(q-1)x\), and \(r(s)=(1-x)/h(x)\). The one-coordinate semigroup has diagonal entry \(h(x)/q\) and off-diagonal entry \((1-x)/q\), by separating the constants from their orthogonal complement. Tensor products give
\[
 \Delta_k(s):=p_s(0)-p_s(k)=N^{-1}h(x)^d(1-r(s)^k).
\]
The gap is positive and bounded at positive times and decays as \(O(e^{-qs})\) at infinity, so its normalizer is finite and positive. The map \(s\mapsto r(s)\) increases strictly from zero to one. For every adjacent pair,
\[
 \frac{\Delta_{k+1}(s)}{\Delta_k(s)}=1+\frac{1}{\sum_{j=1}^k r(s)^{-j}}.
\]
This is strictly increasing, and normalizing the gaps only multiplies this ratio by a positive constant. For an increasing test function \(g\) integrable under both densities, the expectation difference is \(\operatorname{Cov}_{f_k}(g,f_{k+1}/f_k)\). Twice this covariance is the expectation over independent \(S,T\) of \((g(S)-g(T))((f_{k+1}/f_k)(S)-(f_{k+1}/f_k)(T))\). The integrand is nonnegative, and positive on a set of positive measure if \(g\) is not almost everywhere constant. This includes each upper-tail indicator from a positive finite threshold. For \(\alpha>1\), the spectral Laplace transform formula gives \(\delta_\alpha(k)=\Gamma(\alpha)^{-1}\int_0^\infty s^{\alpha-1}\Delta_k(s)\,ds\), and \(\delta_1(k)=\int_0^\infty\Delta_k(s)\,ds\). Apply the expectation result to \(s^{\alpha-1}\).

## Application: exact two-leader grounded costs

Ground distinct vertices \(u,v\) and let \(J_k\) be the trace of the inverse of the remaining principal submatrix of \(L\), for \(d_H(u,v)=k\). Write \(a_d=(L^+)_{uu}\) and \(R_{uv}=2\delta_1(k)\). The effective resistance from \(z\) to common ground is the minimum over \(b\in\mathbb R\) of the energy of \(e_z-be_u-(1-b)e_v\), computed with \(L^+\). The minimum is
\[
 \frac{R_{zu}+R_{zv}}2-\frac{R_{uv}}4-\frac{(R_{zu}-R_{zv})^2}{4R_{uv}}.
\]
It equals the \(z\)-th diagonal entry of the grounded inverse for followers and is zero for leaders. Since the diagonal of \(L^+\) is constant and its row sums are zero, \(\sum_z R_{zu}=2Na_d\) and \(\sum_z(R_{zu}-R_{zv})^2=8\delta_2(k)\). Thus
\[
 J_k=2Na_d-\tfrac N2\delta_1(k)-\frac{\delta_2(k)}{\delta_1(k)}.
\]
The unnormalized \(\Delta_k(s)\) increases strictly in \(k\) for each \(s>0\), so \(\delta_1(k)\) increases strictly. The spectral ratio result for \(\alpha=2\) shows that the other correction also increases strictly; hence \(J_1>\cdots>J_d\). The number of optimal unordered pairs is \(N(q-1)^d/2\).

For an exact rational evaluation put \(D_k(x)=h(x)^d-(1-x)^kh(x)^{d-k}\), and write \(D_k(x)=\sum_{j=1}^d c_{k,j}x^j\). Substituting \(x=e^{-qs}\) gives \(\delta_1(k)=\sum_j c_{k,j}/(Nqj)\) and \(\delta_2(k)=\sum_j c_{k,j}/(Nq^2j^2)\). The positive Laplacian eigenvalues are \(qj\) with multiplicities \(\binom dj(q-1)^j\); hence \(a_d=\sum_j\binom dj(q-1)^j/(Nqj)\).

## Verification and scope

The proofs use the unit-conductance combinatorial Laplacian, and the grounded-cost application concerns exactly two perfectly grounded leaders, with cost equal to the trace rather than half the trace. The accompanying rational checker `verify.py` (see the original `requirements.txt`) concerns the cost application: it checks finite rational distance comparisons, direct grounded inversions and optimal-pair counts. The analytic proof above establishes the full likelihood-ratio conclusion and all the spectral ratio inequalities; finite matrix checks are not evidence for every real exponent.

## Relationship to prior work

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (https://arxiv.org/abs/1407.1569), §V-C, discuss the resistance-maximizing optimal pair. Patterson, Yi, and Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks* (https://arxiv.org/abs/1708.06873), §III-A and Theorem 9, give the resistance formulation and the cycle specialization. Neither the optimal pair nor the general resistance identity is claimed as new.

The earlier [strict Hamming-distance ordering of unequal-gain two-leader coherence](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-strict-hamming-distance-ordering-of-unequal-gain-two-leader-cohe--09287ef2a00c) proves a strict ranking on the binary cube for finite pin strengths. Its analytic bounds also give the strict grounded ranking, and the pointwise-gap and maximum-principle argument extends to the \(q\)-ary product kernel. These comparisons use monotonicity of the **unnormalized** gap and of two separate integrals of that gap. The finding here is the strict ordering after normalization, quantified by the increasing likelihood ratio and the resulting relative spectral distances. The grounded costs are an application of the stronger ordering, not a claim to priority for the ranking itself.
