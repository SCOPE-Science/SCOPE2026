# Arbitrarily many coextinction-variance peaks in connected ecological networks

## Finding
For every integer \(k\ge2\), there is a **finite, connected, simple bipartite ecological interaction network** in which every primary-guild vertex has degree exactly two, every secondary species has positive degree, and the number of secondary extinctions under independent primary losses has at least \(k\) distinct strict local variance maxima as the common primary extinction probability \(q\) ranges through \((0,1)\). There are at least \(k-1\) strict local variance minima between them. Meanwhile, its expected secondary-extinction count is strictly increasing throughout \((0,1)\).

The construction uses exactly \(k+1\) secondary species, without repeated secondary neighborhoods. Let \(s_i=100^{i-1}\) for \(1\le i\le k\) and \(N=\sum_{i=1}^{k}s_i\). Partition \(N\) primary species into disjoint blocks \(B_i\) of sizes \(s_i\). The secondary guild consists of one species \(C_i\) dependent on all primary species in \(B_i\), for each \(i\), and one generalist species \(G\) dependent on all \(N\) primary species. Thus each primary vertex is adjacent to precisely its own \(C_i\) and \(G\), and the bipartite graph is connected.

For each \(i\), define the two rational parameter values
\[
 a_i=\frac{s_i}{s_i+2},\qquad b_i=\frac{5s_i}{5s_i+1}.
\]
They satisfy \(0<a_1<b_1<a_2<b_2<\cdots<a_k<b_k<1\). Writing \(V(q)\) for the secondary-extinction count variance, the theorem proves \(V'(a_i)>0\) and \(V'(b_i)<0\) for every \(i\). Every interval \((a_i,b_i)\) therefore contains a strict variance maximum, and every intervening \((b_i,a_{i+1})\) contains a strict variance minimum.

## Assumptions and scope
The network is fixed and undirected as a bipartite incidence graph. Each primary species is removed independently with the same probability \(q\). A secondary species is removed **if and only if all its primary partners have been removed**; no other extinction mechanism or feedback is imposed. The random variable \(X(q)\) counts secondary extinctions, not primary extinctions or extinction times. The theorem concerns unnormalized count variance; dividing by the fixed square of the secondary-guild size preserves all critical points.

## Proof
For each block \(B_i\), let \(Y_i\) be the indicator that every primary species in \(B_i\) disappears. The variables \(Y_i\) are independent Bernoulli variables with means \(q^{s_i}\). The generalist disappears if and only if all blocks disappear, so \(Z=\prod_iY_i\) and \(X=\sum_iY_i+Z\). Since \(\mathbb E[Y_iZ]=\mathbb E[Z]=q^N\), direct covariance expansion gives
\[
\mathbb E X=\sum_{i=1}^k q^{s_i}+q^N,
\]
\[
 V(q)=\sum_{i=1}^k\bigl(q^{s_i}-q^{2s_i}\bigr)
       +q^N-q^{2N}+2\sum_{i=1}^k\bigl(q^N-q^{N+s_i}\bigr).
\tag{1}
\]
In particular, the mean derivative is strictly positive for \(0<q<1\). Split \(V=B+R\) into the first sum and the remaining terms. Multiplying the derivatives by the positive \(q\),
\[
 qB'(q)=\sum_j s_j q^{s_j}(1-2q^{s_j}),
\]
\[
 qR'(q)=Nq^N(1-2q^N)
  +2q^N\sum_j\bigl[N(1-q^{s_j})-s_jq^{s_j}\bigr].\tag{2}
\]
We verify alternating strict signs using elementary bounds, uniformly in \(k\).

**Positive derivative at \(a_i\).** Put \(s=s_i\) and \(a=s/(s+2)\). Bernoulli's inequality and \(1+t\le e^t\) give \(1/8<a^s\le1/3\). The concave quadratic \(u(1-2u)\) is at least \(3/32\) on \([1/8,1/3]\). Terms with \(j<i\) in \(qB'\) are each at least \(-s_j\), and \(\sum_{j<i}s_j<s/99\). Terms with \(j>i\) are nonnegative, since \(a^{s_j}\le(1/3)^{100}<1/2\). Thus
\[
 aB'(a)>s\left(\frac3{32}-\frac1{99}\right)>0.
\]
Also \(a^N\le a^s\le1/3\), so the first term of \(aR'(a)\) is positive. For every \(j\), Bernoulli's inequality yields
\[
 a^{-s_j}-1=(1+2/s)^{s_j}-1\ge2s_j/s\ge s_j/N.
\]
This is equivalent to \(N(1-a^{s_j})-s_ja^{s_j}\ge0\), so the other terms in (2) are nonnegative. Hence \(V'(a_i)>0\).

**Negative derivative of the independent-block part at \(b_i\).** Put \(b=5s/(5s+1)\). The inequalities \(e^{-1/5}\le b^s\le5/6\) imply \(4/5<b^s\le5/6\), and therefore the \(i\)-th summand of \(bB'(b)\) is at most \(-12s/25\). All earlier-index summands are negative, since \(b^{s_j}\ge b^s>1/2\). As \(-\log b=\log(1+1/(5s))\ge1/(6s)\), later-index terms contribute at most
\[
 s\sum_{r\ge1}100^r e^{-100^r/6}<s/100.
\]
The last inequality follows because the first summand is below \(100\cdot2^{-16}\), and successive summands decrease by a factor below \(1/2\). Consequently \(bB'(b)<-47s/100\).

**Generalist term when \(i=k\).** Here \(s=s_k\) and \(1\le N/s\le100/99\). At \(b_i\), \(b^N\ge e^{-N/(5s)}>1/2\); hence the first term of \(bR'(b)\) is negative. For each \(j\),
\[
 b^{-s_j}-1\le e^{s_j/(5s)}-1
 \le\frac{s_j}{5s}e^{1/5}<\frac{s_j}{N},
\]
where the final step uses \((N/s)e^{1/5}/5<1\). Thus each covariance derivative contribution in (2) is negative as well. Therefore \(V'(b_k)<0\).

**Generalist term when \(i<k\).** Put \(r=k-i\ge1\) and \(t=N/s\ge100^r\). At \(b_i\), use \(1-b^{s_j}\le s_j/(5s)\) for \(j\le i\), and \(1-b^{s_j}\le1\) for \(j>i\), dropping negative terms in (2). Since \(\sum_{j\le i}s_j\le100s/99\) and \(b^N\le e^{-t/6}\),
\[
 \frac{bR'(b)}s
 \le\left(1+\frac{40}{99}+2r\right)t e^{-t/6}
 <(2r+3)100^r e^{-100^r/6}<\frac1{100}.
\tag{3}
\]
For the last inequality, the right-hand side decreases with integral \(r\ge1\) (the ratio of consecutive terms is below \(1/2\)); at \(r=1\) it is \(500e^{-100/6}<500/2^{16}<1/100\). Combining with the previous \(bB'(b)<-47s/100\) yields \(V'(b_i)<0\).

Finally, direct cross-multiplication proves \(a_i<b_i<a_{i+1}\) for all applicable \(i\). A polynomial with derivative positive at the left and negative at the right endpoint of a closed interval attains an interior strict local maximum; the reversed endpoint signs similarly force an interior strict local minimum. All indicated intervals are disjoint. This completes the proof for every integer \(k\ge2\).

## Verification
The standalone Python program `verify.py` constructs (1) as an exact integer-coefficient polynomial and checks the signs of \(qV'(q)\) by clearing strictly positive denominators at all \(2k\) rational probes for \(k=1,2,3\). The exact output is `VERIFY_OK [(1, 2, [(1, -1)]), (2, 8, [(1, -1), (1, -1)]), (3, 11, [(1, -1), (1, -1), (1, -1)])]`. The finite calculations corroborate the symbolic formulas; the proof above, not the finite checks, establishes all \(k\).

## Relationship to prior work
Eklöf, Tang, and Allesina (2013) study extinction probabilities through ecological interaction networks, including the binary response in which a consumer disappears after losing all resources. Jones, Zurell, and Wiesner (2024) give analytic predictions for mean network robustness and degree-based effects, while Chabert-Liddell, Barbillon, and Donnet (2021/2022) study expectation and variance of robustness in bipartite stochastic-block models. These provide motivating models and moment techniques. The present claim is specifically the **unbounded number of distinct local variance maxima under one continuously varying common independent primary-loss probability**, in finite connected networks whose primary nodes all have degree two; it is not a new claim of the basic marginal extinction formula.

## Limitations
The explicitly constructed networks have exponentially separated consumer partner-set sizes and rapidly growing total size as \(k\) increases. Later variance peaks occur near complete primary-guild loss. The model assumes independent identical primary extinction probabilities and the topological all-partners-lost rule; it does not establish empirical frequency, finite-population dynamical persistence, unique critical points inside each interval, or an upper bound on the total number of critical points. The 2021 blockmodel paper's accessible abstract does not permit a decisive full-text comparison, leaving a specific originality risk.

## References
1. Eklöf, A., Tang, S., and Allesina, S. (2013), *Secondary extinctions in food webs: a Bayesian network approach*, Methods in Ecology and Evolution 4, 760–770. First public date verified 2013-04-26. DOI: https://doi.org/10.1111/2041-210X.12062
2. Chabert-Liddell, S.-C., Barbillon, P., and Donnet, S. (2021 preprint; 2022 journal), *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*. arXiv:2106.06348; DOI: https://doi.org/10.1002/env.2709
3. Jones, C., Zurell, D., and Wiesner, K. (2024), *Novel analytic methods for predicting extinctions in ecological networks*, Ecological Monographs 94, e1601. DOI: https://doi.org/10.1002/ecm.1601
