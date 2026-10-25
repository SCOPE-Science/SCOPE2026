# Countable-translate entropy equals \(-\log_2 \alpha\) on compact groups

## Finding

Let \(G\) be a compact metrizable group with normalized Haar probability measure \(\mu\). Let \(A\subseteq G\) be Haar-measurable and let \(\alpha=\mu(A)\in(0,1]\). Write \(\mathcal I_A=\{gA:g\in G\}\) for the family of left translates of \(A\). Define the countable-mixture entropy by
\[
\overline H_{\rm cnt}(\mathcal I_A,\mu)
=\inf_{a\in\operatorname{VP}_{\rm cnt}(\mathcal I_A)}
\int_G-\log_2 a(x)\,d\mu(x),
\]
where \(\operatorname{VP}_{\rm cnt}(\mathcal I_A)\) consists of countable convex combinations \(a=\sum_{k\ge1}q_k\mathbf 1_{g_kA}\), with \(q_k\ge0\), \(\sum_kq_k=1\), and \(g_k\in G\); use \(-\log_2 0=+\infty\). Then
\[
\boxed{\overline H_{\rm cnt}(\mathcal I_A,\mu)=-\log_2\alpha.}
\]
Thus the infimum over countable mixtures agrees with the value available from unrestricted mixtures for every measurable positive-measure set in a compact metrizable group.

## Assumptions and scope

- \(G\) is compact and metrizable, and \(\mu\) is its normalized Haar probability measure. In particular, \(\mu\) is invariant under left and right translations and under inversion.
- \(A\) is Haar-measurable and \(0<\alpha=\mu(A)\le1\). Every translate \(gA\) has measure \(\alpha\).
- The admissible functions are countable convex combinations of indicators of left translates. The theorem concerns the infimum; it does not claim that a countable combination attains it.
- Entropies are measured in bits, so logarithms are base \(2\).

## Proof

If \(\alpha=1\), every translate agrees with \(G\) up to a null set, so the entropy is \(0=-\log_2\alpha\). Assume \(0<\alpha<1\). A Haar-measurable set may be replaced by a Borel representative modulo a null set: each fixed translate changes only on a null set, and any countable family of translates changes only on a countable union of null sets. Thus every admissible countable-mixture cost is unchanged, and we may assume \(A\) is Borel when applying product-measure arguments below.

**Lower bound.** For every admissible \(a=\sum_k q_k\mathbf 1_{g_kA}\), Tonelli's theorem and translation invariance give
\[
\int_G a\,d\mu=\sum_kq_k\mu(g_kA)=\alpha.
\]
By Jensen's inequality for the concave logarithm, interpreted in the extended sense if \(a=0\) on a positive-measure set,
\[
\int_G\log_2 a\,d\mu\le\log_2\!\left(\int_Ga\,d\mu\right)=\log_2\alpha.
\]
Consequently \(\int_G-\log_2a\,d\mu\ge-\log_2\alpha\), and hence
\[
\overline H_{\rm cnt}(\mathcal I_A,\mu)\ge-\log_2\alpha.
\]

**A countable positive baseline.** Let \(U_1,U_2,\ldots\) be independent Haar-uniform group elements and set
\[
a_0(x)=\sum_{k\ge1}2^{-k}\mathbf 1_{U_kA}(x).
\]
For each fixed \(x\in G\), the events \(x\in U_kA\) are independent and each has probability \(\alpha\): indeed, \(x\in U_kA\) is equivalent to \(U_k\in xA^{-1}\), whose Haar measure is \(\alpha\). Let \(K(x)\) be the first successful index. Then \(K(x)\) is geometric with mean \(1/\alpha\), and \(a_0(x)\ge2^{-K(x)}\). Therefore
\[
\mathbb E[-\log_2a_0(x)]\le\mathbb E K(x)=1/\alpha.
\]
Tonelli's theorem yields
\[
\mathbb E\!\left[\int_G-\log_2a_0\,d\mu\right]\le1/\alpha.
\]
Thus there is a realization of the sequence \((U_k)\) for which \(a_0>0\) almost everywhere and \(g_0=-\log_2a_0\) is integrable. Fix such a realization.

**Approximation of the constant \(\alpha\).** Fix \(0<\delta<\alpha\). For each \(N\), take independent Haar-uniform elements \(V_1,\ldots,V_N\) and put
\[
f_N(x)=\frac1N\sum_{i=1}^N\mathbf 1_{V_iA}(x),\qquad
B_N=\{x\in G:f_N(x)<\alpha-\delta\}.
\]
For each fixed \(x\), \(Nf_N(x)\) has the binomial distribution with parameters \(N\) and \(\alpha\). Hoeffding's inequality and Fubini's theorem imply
\[
\mathbb E[\mu(B_N)]\le e^{-2N\delta^2}.
\]
For every sufficiently large \(N\), one can therefore choose a deterministic \(N\)-tuple of translates with \(\mu(B_N)\le e^{-N\delta^2}\). Choose one such tuple for each \(N\); then \(\mu(B_N)\to0\). Since \(g_0\) is integrable, absolute continuity of its integral gives \(\int_{B_N}g_0\,d\mu\to0\).

For \(0<\varepsilon<1\), define
\[
a_{N,\varepsilon}=(1-\varepsilon)f_N+\varepsilon a_0.
\]
This is a countable convex combination of indicators of translates. On \(G\setminus B_N\),
\(a_{N,\varepsilon}\ge(1-\varepsilon)(\alpha-\delta)\); on \(B_N\),
\(a_{N,\varepsilon}\ge\varepsilon a_0\). Hence
\[
\begin{aligned}
\int_G-\log_2a_{N,\varepsilon}\,d\mu
&\le-\log_2((1-\varepsilon)(\alpha-\delta))\\
&\quad+\mu(B_N)(-\log_2\varepsilon)+\int_{B_N}g_0\,d\mu.
\end{aligned}
\]
Letting \(N\to\infty\) gives
\[
\overline H_{\rm cnt}(\mathcal I_A,\mu)
\le-\log_2((1-\varepsilon)(\alpha-\delta)).
\]
Finally let \(\delta\downarrow0\) and \(\varepsilon\downarrow0\). This proves
\(\overline H_{\rm cnt}(\mathcal I_A,\mu)\le-\log_2\alpha\). Together with the lower bound, equality follows.

## Verification

The lower bound uses only the common measure \(\mu(gA)=\alpha\) and Jensen's inequality. The upper bound uses an explicit existence argument: a geometrically weighted countable mixture gives an integrable positive baseline, while finite random averages have exponentially small lower-tail measure by Hoeffding's inequality. Mixing the finite averages with the baseline makes every candidate admissible and keeps its logarithmic cost controlled on the exceptional set.

No finite enumeration is used, and no numerical experiment is treated as proof. The argument establishes an infimum equality, not attainment by one countable mixture and not an effective algorithm for finding the translates. Compactness, Haar invariance, measurability, and positive measure are essential stated hypotheses.

## Relationship to prior work

Harangi, Niu, and Bai's *Generalizing Körner's graph entropy to graphons* (arXiv:2208.14899; published in *European Journal of Combinatorics* 114 (2023), article 103779) treats the circle-translation family in Example 6.15. It identifies the unrestricted-mixture entropy as \(-\log\alpha\), notes that the countable-mixture value appears to be the same, and states the broader equality of unrestricted and countable-mixture entropy as Conjecture 6.16. The paper also explains that for a positive-measure nowhere-dense Cantor set the finite-mixture entropy can be infinite. For a compact group, averaging the indicators of \(gA\) over Haar-uniform \(g\) gives the constant function \(lpha\), so the unrestricted-mixture value is \(-\log_2lpha\) by the same Jensen lower bound. The present theorem proves the countable-mixture equality for translates of every positive-measure measurable set under compact metrizable group actions; it does not prove Conjecture 6.16 for arbitrary set systems.

Harangi, Niu, and Bai's *Conditional graph entropy as an alternating minimization problem* (arXiv:2209.00283) provides related coding-rate and entropy-optimization context, but does not establish the countable-mixture translate result.

## Limitations

- The result covers left translates under normalized Haar measure on compact metrizable groups only. It does not cover arbitrary measure-preserving actions, noncompact groups, or non-invariant source measures.
- The general unrestricted-versus-countable-mixture conjecture for arbitrary set systems remains open here.
- The proof shows equality of infima. It does not show that the countable-mixture infimum is attained.
- The baseline and approximating translates are obtained by an existence argument; the proof does not give a computationally efficient deterministic selection algorithm.

## References

1. V. Harangi, X. Niu, and B. Bai, “Generalizing Körner's graph entropy to graphons,” arXiv:2208.14899 (first public version posted 2022-08-31); *European Journal of Combinatorics* 114 (2023), 103779. See Example 6.15 and Conjecture 6.16.
2. V. Harangi, X. Niu, and B. Bai, “Conditional graph entropy as an alternating minimization problem,” arXiv:2209.00283 (first public version posted 2022-09-01).
