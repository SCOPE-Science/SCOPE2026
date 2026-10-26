# Odd-Cardinality Phase Twirling Preserves a Super-Exponential Squeezed-Light Advantage

## Finding

Let \(\mathcal T_M\) be the ideal uniform phase-twirling channel
\[
\mathcal T_M(\rho)=\frac1M\sum_{j=0}^{M-1}e^{2\pi i j\hat N/M}\rho e^{-2\pi i j\hat N/M},
\]
followed by local phase encoding \(R_\delta=e^{i\delta\hat N}\). For every odd integer \(M\ge3\), a squeezed-vacuum input supported on even photon numbers satisfies \(R_\delta\mathcal T_M(\rho_{\rm SV})R_\delta^*=R_\delta\mathcal T_{2M}(\rho_{\rm SV})R_\delta^*\) for every \(\delta\). In particular, with mean photon number one, its quantum Fisher information \(\mathcal J_{\rm SV}(M)\) and that of a coherent state of amplitude \(1\), \(\mathcal J_{\rm coh}(M)\), obey
\[
\frac{\mathcal J_{\rm SV}(M)}{\mathcal J_{\rm coh}(M)}=8e\left(\frac{M}{2e}\right)^M(1+o(1))
\]
as odd \(M\to\infty\). Thus the super-exponential separation persists for odd phase-alphabet sizes, with a different leading base from the even-\(M\) case.

## Assumptions and scope

There is one bosonic mode with number operator \(\hat N\), no loss or thermal noise, and the unknown parameter is encoded locally after the independent uniform discrete phase twirl. The squeezed-vacuum probe has \(\sinh^2 r=1\), hence mean photon number one and support only on \(\{|0\rangle,|2\rangle,|4\rangle,\ldots\}\). The coherent benchmark is the single coherent state \(|\alpha=1\rangle\), also of mean photon number one. The result compares these two specified probes; it does not claim optimality against every nonclassical or classical protocol, nor does it cover noisy channels.

## Proof

For any state, the twirl multiplies a Fock matrix element \(\langle n|\rho|m\rangle\) by \(1\) if \(M\mid(n-m)\), and by \(0\) otherwise. If \(n,m\) are even and \(M\) is odd, then \(M\mid(n-m)\) if and only if \(2M\mid(n-m)\): write \(n-m=2k\), and use that \(M\) is odd, so \(M\mid 2k\iff M\mid k\iff 2M\mid 2k\). Therefore the two twirled density operators agree on the even-photon subspace. Both the twirl and \(R_\delta\) preserve that subspace, proving equality of the full parameterized output families and hence
\[
\mathcal J_{\rm SV}(M)=\mathcal J_{\rm SV}(2M).
\]

For a pure input with photon probabilities \(p_n\), write \(a_{r,k}=p_{r+kM}\) and \(\lambda_r=\sum_{k\ge0}a_{r,k}\). The residue-block QFI identity is
\[
\mathcal J(M)=4M^2\sum_{r:\lambda_r>0}\frac1{\lambda_r}\sum_{0\le k<\ell}a_{r,k}a_{r,\ell}(\ell-k)^2.
\]
For mean-one squeezed vacuum, put \(q=1/2\) and \(d_k=\binom{2k}{k}/4^k\). Its photon probabilities are \(p_{2k}=d_kq^k/\sqrt2\), with \(p_{2k+1}=0\). For even twirl modulus \(L\), the first adjacent residue-pair terms and the tail bound from the same identity give
\[
\mathcal J_{\rm SV}(L)=4L^2\sqrt2\,d_{L/2}q^{L/2}(1+o(1)).
\]
Indeed, the lower bound is \(4L^2(1-q^{L/2})\Pr(L\le N<2L)\), and the block probability is \(\sqrt2\,d_{L/2}q^{L/2}(1+o(1))\); the upper bound \(4\sum_{n\ge L}n^2p_n\) has the same asymptotic. Taking \(L=2M\), using \(d_M\sim(\pi M)^{-1/2}\), and using the exact twirl equivalence above yields
\[
\mathcal J_{\rm SV}(M)=16\sqrt{2/\pi}\,M^{3/2}2^{-M}(1+o(1)).
\]

For the coherent state \(|\alpha=1\rangle\), \(p_n=e^{-1}/n!\). The residue-block identity gives the lower bound from the \(|0\rangle,|M\rangle\) pair,
\[
\mathcal J_{\rm coh}(M)\ge\frac{4M^2e^{-1}}{M!\sum_{k\ge0}1/(kM)!}=\frac{4M^2e^{-1}}{M!}(1+o(1)).
\]
For the upper bound, the same identity implies \(\mathcal J_{\rm coh}(M)\le4\sum_{n\ge M}n^2p_n\). With \(t_n=n^2e^{-1}/n!\),
\[
\frac{t_{n+1}}{t_n}=\frac{n+1}{n^2}\le\frac{M+1}{M^2}=:r_M<1\qquad(n\ge M),
\]
so \(\mathcal J_{\rm coh}(M)\le4M^2e^{-1}/[M!(1-r_M)]\). Since \(r_M\to0\), the upper and lower bounds match:
\[
\mathcal J_{\rm coh}(M)=\frac{4M^2e^{-1}}{M!}(1+o(1)).
\]
Dividing the two QFI asymptotics and applying Stirling's formula \(M!/\sqrt M=\sqrt{2\pi}(M/e)^M(1+o(1))\) gives
\[
\frac{\mathcal J_{\rm SV}(M)}{\mathcal J_{\rm coh}(M)}=8e\left(\frac{M}{2e}\right)^M(1+o(1)),
\]
as claimed. All asymptotic statements are along odd positive integers \(M\to\infty\); no finite-cutoff computation is used as an infinite proof.

## Verification

The parity reduction is exact at the level of every Fock matrix element. The squeezed-vacuum asymptotic follows from the residue-block QFI identity, the geometric bound on successive photon-probability ratios, and the central-binomial asymptotic. The coherent-state asymptotic is independently bracketed by a single residue-pair lower bound and a geometric-tail upper bound. The final constant is checked by dividing \(16\sqrt{2/\pi}\,M^{3/2}2^{-M}\) by \(4M^2e^{-1}/M!\) and applying Stirling's formula. The proof is analytic and does not rely on numerical truncation. Independent validation has not been performed.

## Relationship to prior work

Conlon et al. study discrete phase twirling and prove a super-exponential squeezed-vacuum/coherent-state QFI separation for even \(M\); their paper states an even-modulus assumption and gives the residue-block QFI identity, a coherent-state factorial bound, and the even-modulus squeezed-vacuum asymptotic [1]. The present statement is the odd-modulus extension: the even-photon support makes the odd-\(M\) twirl exactly equal to the \(2M\)-twirl on the squeezed probe, while the coherent benchmark is evaluated at odd \(M\). The resulting ratio has the explicit asymptotic base \(M/(2e)\). This does not extend the noisy-channel theorems and does not assert a bound for the entire phase-covariant classical family.

## Limitations

The result concerns the ideal single-mode model, a fixed mean of one photon, and a coherent-state comparator. It is asymptotic rather than an exact finite-\(M\) ratio. The source is a recent arXiv preprint; an exhaustive literature search cannot be guaranteed, and independent audit remains unperformed. The proof establishes persistence of the separation for odd \(M\), not optimality of the squeezed vacuum over all probes for odd \(M\).

## References

[1] L. O. Conlon et al., “Super-Exponential Advantage of Squeezed Light in Phase Estimation under Discrete Phase Randomisation,” arXiv:2610.03657v1, first posted 2026-10-02, especially Secs. III.1–III.2 and Appendix A.1–A.3.2.
