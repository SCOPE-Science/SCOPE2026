# Multiplicity-sensitive first-passage oracle for full e-BH discovery
## Finding
Fix integers \(K\ge m\ge1\) and a target level \(\alpha\in(0,1)\). An oracle knows the set \(\mathcal H_1\) of exactly \(m\) nonnull streams. For each \(i\in\mathcal H_1\), let \(E_i(n)>0\) denote the realized evidence after \(n\) samples from that stream, with \(E_i(0)=1\). Every null coordinate is frozen at the valid e-value \(1\). At each global step, at most one stream receives one new sample; an unselected stream keeps its current evidence value.

Define the pooled e-BH boundary
\[
b_m=\frac{K}{\alpha m}
\]
and the streamwise first-passage count
\[
\tau_i=\inf\big\{n\ge0:E_i(n)\ge b_m\big\}.
\]
Assume every \(\tau_i\) is finite. Then the exact pathwise oracle sample cost for terminal full discovery is
\[
T^\star=\sum_{i\in\mathcal H_1}\tau_i.
\]
An optimal policy may sample the nonnull streams in any order, stop sampling stream \(i\) at its first crossing \(\tau_i\), and permanently park the resulting evidence value. The common parking boundary \(b_m\) is sharp: any smaller common level can fail to produce even one e-BH rejection when all \(m\) nonnull coordinates are placed at that level and all null coordinates equal \(1\).

For likelihood-ratio evidence, this gives an exact first-passage expectation identity. Suppose
\[
\log E_i(n)=\sum_{j=1}^n X_{ij},
\]
where the increments are iid under the alternative with \(\mathbb E X_{i1}=D_i>0\), and suppose the standard integrability hypotheses for Wald's identity hold, including \(\mathbb E\tau_i<\infty\). Set
\[
O_i=\log E_i(\tau_i)-\log b_m\ge0.
\]
Then
\[
\mathbb E T^\star
=\sum_{i\in\mathcal H_1}\frac{\log b_m+\mathbb E O_i}{D_i}.
\]
The leading boundary is therefore \(\log(K/(\alpha m))\) per nonnull in this oracle benchmark. It equals \(\log(K/\alpha)\) for one signal and \(\log(1/\alpha)\) when every hypothesis is nonnull.

## Assumptions and scope
The theorem is a pathwise benchmark for the e-BH rejection geometry. It assumes that the nonnull set and its size are known to the oracle, that null coordinates stay exactly at the e-value \(1\), and that parked nonnull evidence values are not updated after first crossing. These assumptions deliberately isolate the sample cost forced by the step-up rejection rule from the cost of learning which streams are nonnull or controlling evidence fluctuations while streams remain active.

The e-BH rule at level \(\alpha\) sorts the terminal e-values as \(E_{(1)}\ge\cdots\ge E_{(K)}\) and takes
\[
k^\star=\max\left\{k:E_{(k)}\ge\frac{K}{\alpha k}\right\}.
\]
Its rejection set consists of coordinates at least \(K/(\alpha k^\star)\). No independence assumption is needed for the deterministic pathwise statement. When the parked values arise from stopped e-processes and are to be used as inferential e-values, their stopping must also satisfy the relevant filtration conditions for e-process validity.

The likelihood-ratio expectation identity is a corollary under extra probabilistic assumptions; it is not used to prove the pathwise optimum. The overshoot term is retained exactly and is not replaced by an asymptotic approximation.

## Proof
Because \(\alpha<1\), every threshold corresponding to more than \(m\) rejections exceeds the null value \(1\): for \(r>m\),
\[
\frac{K}{\alpha r}\ge\frac1\alpha>1.
\]
At terminal time, the \(K-m\) null coordinates are all equal to \(1\). Hence e-BH cannot have \(k^\star>m\). If all \(m\) nonnulls are rejected, necessarily \(k^\star=m\). Consequently the smallest nonnull terminal e-value must satisfy
\[
\min_{i\in\mathcal H_1}E_i(n_i)\ge\frac{K}{\alpha m}=b_m,
\]
where \(n_i\) is the number of samples allocated to stream \(i\).

By definition of first passage, \(E_i(n_i)\ge b_m\) implies \(n_i\ge\tau_i\). If \(T\) is the total number of samples, then
\[
T\ge\sum_{i\in\mathcal H_1}n_i\ge\sum_{i\in\mathcal H_1}\tau_i.
\]
This proves the universal pathwise lower bound, even for an oracle policy that is allowed to waste samples on null streams.

For achievability, sample each nonnull until its own first crossing of \(b_m\), then freeze that coordinate. At termination every nonnull e-value is at least \(b_m\), while every null e-value equals \(1<b_m\). Thus \(E_{(m)}\ge b_m=K/(\alpha m)\), so \(k^\star=m\) and every nonnull is rejected. The policy uses exactly \(\sum_i\tau_i\) samples. This proves pathwise optimality.

To prove sharpness of the common parking boundary, fix any \(b<b_m\) and consider the deterministic terminal vector with all \(m\) nonnull coordinates equal to \(b\) and every null coordinate equal to \(1\). For \(r\le m\), the e-BH threshold obeys
\[
\frac{K}{\alpha r}\ge\frac{K}{\alpha m}=b_m>b,
\]
while for \(r>m\), the \(r\)-th ordered value is \(1\) and \(1<K/(\alpha r)\). Hence no \(r\) qualifies and e-BH rejects nothing. Therefore \(b_m\) is the least universal common parking level.

Finally, in the likelihood-ratio setting, write \(S_i(n)=\log E_i(n)\). At \(\tau_i\),
\[
S_i(\tau_i)=\log b_m+O_i.
\]
Under the stated Wald conditions,
\[
D_i\,\mathbb E\tau_i=\mathbb E S_i(\tau_i)=\log b_m+\mathbb E O_i.
\]
Summing this exact identity over nonnull streams gives the displayed formula for \(\mathbb E T^\star\).

## Verification
The accompanying `verify.py` implements e-BH using exact rational arithmetic. It checks the common-boundary sharpness over a grid of small values of \(K\) and \(m\), and it exhaustively enumerates terminal sample-count tuples for a nonmonotone three-signal example. The enumeration confirms that the minimum total count achieving full rejection equals the sum of first-passage counts, while parking at those first crossings attains the minimum.

The finite checker verifies the deterministic combinatorial core only. The Wald identity is proved analytically under its stated hypotheses; no finite simulation is used as evidence for an infinite-sample theorem.

## Relationship to prior work
Lin, Ma, Ren, and Wei (2026) study adaptive data collection for multiple testing and use e-BH as the rejection rule. Their simple-versus-simple upper bound contains a nonnull term with leading boundary \(\log(K/\alpha)\), and their expected-stopping-time appendix defines the corresponding per-stream crossing time at that boundary. Their general lower bound has nonnull scale \(\log(1/\alpha)\) as the target errors vanish. The present theorem isolates, for a deliberately favorable oracle benchmark, the exact multiplicity-sensitive e-BH boundary \(\log(K/(\alpha m))\) and the exact sum-of-first-passages cost. It does not sharpen the proved guarantee for their implementable e-PS algorithm.

Wang and Ramdas (2022) introduced e-BH and also considered a multi-armed-bandit procedure that stops pulling an arm when the multiple-testing procedure gains a discovery. That rule waits for an actual discovery. The benchmark here instead parks latent evidence at the lower group boundary \(K/(\alpha m)\) before the group has necessarily become rejectable, using oracle knowledge of the eventual number of nonnulls.

Wang, Dandapanthula, and Ramdas (2025) analyze when stopped e-processes remain suitable inputs to e-BH under global versus local filtrations. Their result governs inferential validity of stopping; it does not give the multiplicity-sensitive pathwise sample optimum above.

## Limitations
The oracle knows \(\mathcal H_1\) and \(m\); an implementable procedure generally does not. Null evidence is fixed at \(1\), so the theorem omits the samples needed to distinguish nulls from nonnulls. It also does not show that e-PS, or any practical adaptive allocation rule, attains the boundary \(K/(\alpha m)\). A live stream that crosses this boundary and is subsequently sampled can fall back below it, which is exactly why parking is part of the benchmark.

The expectation formula requires the stated Wald conditions and retains the mean overshoot. No claim is made that the overshoot is negligible, uniformly bounded, or distribution-free. The theorem concerns terminal full discovery under base e-BH; weighted e-BH, boosting, alternative rejection rules, and unknown nonnull multiplicity are outside its scope.

## References
1. Z. Lin, W. Ma, Z. Ren, and Y. Wei, “Sample-Efficient Multiple Testing with Adaptive Data Collection,” arXiv:2609.26651v1, 2026. https://arxiv.org/abs/2609.26651
2. R. Wang and A. Ramdas, “False Discovery Rate Control with E-values,” *Journal of the Royal Statistical Society: Series B*, 84(3), 822–852, 2022. DOI: 10.1111/rssb.12489.
3. H. Wang, S. Dandapanthula, and A. Ramdas, “Anytime-valid FDR control with the stopped e-BH procedure,” arXiv:2502.08539, 2025. https://arxiv.org/abs/2502.08539
