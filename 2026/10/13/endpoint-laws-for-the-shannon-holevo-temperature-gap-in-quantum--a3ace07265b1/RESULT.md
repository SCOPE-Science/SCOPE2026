# Endpoint laws for the Shannon–Holevo temperature gap in quantum-decoded Gibbs preparation
## Finding
For the uniformly coupled commuting-Pauli setting of QD-HDQI, write the binary entropy in bits as
\[
h_2(x)=\frac{-x\log x-(1-x)\log(1-x)}{\log2},
\]
and use the inverse branch \(h_2^{-1}:(0,1)\to(0,1/2)\). For an associated binary symplectic-code rate \(R\in(0,1)\), the source identifies two information-theoretic channel boundaries: classical decoding is limited by the binary symmetric channel capacity \(1-h_2(p)\), whereas fully quantum decoding is limited by the Holevo capacity of the corresponding binary pure-state channel. The same source maps channel noise to inverse temperature by
\[
p=\frac{1-\operatorname{sech}\beta}{2}.
\]
Consequently the two capacity-boundary inverse temperatures are
\[
\beta_{\mathrm{cl}}(R)=\operatorname{asech}\!\left(1-2h_2^{-1}(1-R)\right)
\]
and
\[
\beta_{\mathrm q}(R)=\operatorname{asech}\!\left(2\sqrt{q_R(1-q_R)}\right),\qquad q_R=h_2^{-1}(R).
\]
The second expression has the exact simplification
\[
\beta_{\mathrm q}(R)=\operatorname{atanh}(1-2q_R)=\frac12\log\frac{1-q_R}{q_R}.
\]
These boundaries have sharply different endpoint separations. If \(\varepsilon=1-R\downarrow0\) and \(L=\log(1/\varepsilon)\), then
\[
\beta_{\mathrm q}(1-\varepsilon)\sim\sqrt{2(\log2)\varepsilon},
\qquad
\beta_{\mathrm{cl}}(1-\varepsilon)\sim2\sqrt{\frac{(\log2)\varepsilon}{L}},
\]
so
\[
\frac{\beta_{\mathrm q}(1-\varepsilon)}{\beta_{\mathrm{cl}}(1-\varepsilon)}\sim\sqrt{\frac{L}{2}}\to\infty.
\]
At the opposite endpoint, if \(R\downarrow0\) and \(L=\log(1/R)\), then
\[
\beta_{\mathrm{cl}}(R)=\frac12L+\frac12\log\frac{2}{\log2}+o(1),
\]
\[
\beta_{\mathrm q}(R)=\frac12L+\frac12\log L-\frac12\log\log2+o(1),
\]
and hence
\[
\beta_{\mathrm q}(R)-\beta_{\mathrm{cl}}(R)=\frac12\log L-\frac12\log2+o(1)\to\infty,
\qquad
\frac{\beta_{\mathrm q}(R)}{\beta_{\mathrm{cl}}(R)}\to1.
\]
Thus the same Shannon–Holevo separation produces an unbounded *multiplicative* temperature advantage near rate one, but only an unbounded *additive* advantage near rate zero.

## Assumptions and scope
The statement concerns the information-theoretic channel boundaries appearing in the uniformly coupled commuting-Hamiltonian reduction, where all coupling magnitudes equal one and the induced channel is i.i.d. It does not assert that a given sparse-code family, BPQM implementation, or other efficient decoder reaches the Holevo boundary. The boundaries are obtained by translating the source's necessary capacity conditions through its temperature-to-noise relation.

Natural logarithms are used in the asymptotic formulas. The binary entropy \(h_2\) is measured in bits. The inverse \(h_2^{-1}\) always means the branch with values in \((0,1/2)\).

## Proof
For classical decoding, the source gives the BSC capacity boundary
\[
R=1-h_2(p),
\]
so \(p=h_2^{-1}(1-R)\). Substituting \(1-2p=\operatorname{sech}\beta\) gives the displayed formula for \(\beta_{\mathrm{cl}}\).

For quantum decoding, put \(q_R=h_2^{-1}(R)\). The source's Holevo boundary is
\[
p=\frac12-\sqrt{q_R(1-q_R)}.
\]
Therefore
\[
\operatorname{sech}\beta_{\mathrm q}=1-2p=2\sqrt{q_R(1-q_R)}.
\]
For \(0<q_R<1/2\), if \(y=1-2q_R\), then \(1-y^2=4q_R(1-q_R)\). Since \(\operatorname{sech}(\operatorname{atanh}y)=\sqrt{1-y^2}\), monotonicity on the nonnegative branch gives
\[
\beta_{\mathrm q}=\operatorname{atanh}(1-2q_R)=\frac12\log\frac{1-q_R}{q_R}.
\]

For the high-rate endpoint, set \(R=1-\varepsilon\). If \(q_R=1/2-\delta\), Taylor expansion at one half gives
\[
1-h_2(1/2-\delta)=\frac{2\delta^2}{\log2}+O(\delta^4),
\]
so \(\delta\sim\sqrt{\varepsilon\log2/2}\). Hence
\[
\beta_{\mathrm q}=\operatorname{atanh}(2\delta)\sim\sqrt{2(\log2)\varepsilon}.
\]
For the classical boundary, \(p=h_2^{-1}(\varepsilon)\to0\) and
\[
h_2(p)=\frac{p\log(1/p)+p+O(p^2)}{\log2}.
\]
It follows that
\[
p\sim\frac{\varepsilon\log2}{\log(1/\varepsilon)}.
\]
Also \(1-\operatorname{sech}\beta=\beta^2/2+O(\beta^4)\), while \(1-\operatorname{sech}\beta=2p\), so \(\beta_{\mathrm{cl}}\sim2\sqrt p\). This proves the high-rate formulas and their ratio.

For the low-rate endpoint, write \(R\downarrow0\) and \(L=\log(1/R)\). For the classical boundary, \(p=1/2-\delta\) with
\[
\delta\sim\sqrt{\frac{R\log2}{2}}.
\]
Then \(\operatorname{sech}\beta_{\mathrm{cl}}=2\delta\), and the small-argument law \(\operatorname{asech}x=\log(2/x)+o(1)\) yields
\[
\beta_{\mathrm{cl}}=\frac12L+\frac12\log\frac{2}{\log2}+o(1).
\]
For the quantum boundary, \(q_R=h_2^{-1}(R)\to0\). Inverting the small-argument entropy expansion gives
\[
\log\frac1{q_R}=L+\log L-\log\log2+o(1).
\]
Using \(\beta_{\mathrm q}=\frac12\log((1-q_R)/q_R)\) proves
\[
\beta_{\mathrm q}=\frac12L+\frac12\log L-\frac12\log\log2+o(1).
\]
Subtracting the two expansions gives the additive gap, while dividing by the common leading term \(L/2\) gives the ratio limit one.

## Verification
The exact channel-to-temperature transformations were checked algebraically from the source formulas. The entropy expansions were reconstructed independently from Taylor series at \(0\) and \(1/2\). A standalone numerical script evaluates the exact boundaries and confirms convergence toward the four stated normalized limits; these numerical checks are corroborative only and are not used as proofs.

## Relationship to prior work
Piveteau, Quek, and Franco Garrido formulate QD-HDQI, identify the BSC Shannon and PSC Holevo capacity limits, and translate a decoding threshold \(p_*\) to an inverse-temperature threshold \(\operatorname{asech}(1-2p_*)\). Their numerical table compares finite-rate Shannon and Holevo temperature bounds. The endpoint classification above is not stated there.

Earlier work on belief propagation with quantum messages compares the same broad BSC-versus-pure-state-channel capacity phenomenon in optical communication and shows a divergent collective-measurement capacity ratio in a weak-signal regime. That result supplies relevant channel-coding context, but it does not use the QD-HDQI Gibbs map and does not imply the two inverse-temperature endpoint laws proved here.

A recent use of pure-state and binary-symmetric channel capacities in binary-code rate bounds concerns rate-versus-distance inequalities rather than Gibbs preparation. Its publicly available abstract-level description does not settle these temperature asymptotics; limited full-text access to that comparison is retained as an originality risk rather than treated as evidence of absence.

## Limitations
This is an information-theoretic boundary theorem inside the uniformly coupled commuting QD-HDQI model. It gives neither an efficient decoder attaining \(\beta_{\mathrm q}(R)\) for arbitrary code families nor a converse for Gibbs-preparation methods outside this reduction. The random-sign average-case assumptions used by the source to convert decoder thresholds into preparation guarantees remain in force. The asymptotics concern capacity ceilings, not finite-blocklength corrections.

## References
1. C. Piveteau, Y. Quek, and M. I. Franco Garrido, *Gibbs state preparation through quantum decoding*, arXiv:2610.03566v1 (2026).
2. N. Rengaswamy, K. P. Seshadreesan, S. Guha, et al., *Belief propagation with quantum messages for quantum-enhanced classical communications*, npj Quantum Information 7, 97 (2021), DOI 10.1038/s41534-021-00422-1.
3. O. Alrabiah and V. Guruswami, *Binary code rate bounds via classical--quantum channels*, arXiv:2608.09347v1 (2026).
