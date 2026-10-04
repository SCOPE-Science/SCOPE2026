# Exact privacy–Choi-concurrence tradeoff for unital qubit channels
## Finding
For a unital qubit channel \(\mathcal N\), write its Bloch action as
\[
\mathcal N\!\left(\frac{I+r\cdot\sigma}{2}\right)=\frac{I+(Tr)\cdot\sigma}{2},
\]
where \(T\in\mathbb R^{{3\times3}}\), and let \(s_1\ge s_2\ge s_3\ge0\) be the singular values of \(T\). Let
\[
J_{{\mathcal N}}=(\operatorname{{id}}\otimes\mathcal N)(|\Phi^+\rangle\langle\Phi^+|)
\]
be the normalized Choi state. Then
\[
\varepsilon_*(\mathcal N)=2\operatorname{{arctanh}}(s_1)
\]
when \(s_1<1\), with \(\varepsilon_*(\mathcal N)=+\infty\) when \(s_1=1\), and
\[
C(J_{{\mathcal N}})=\frac{[s_1+s_2+s_3-1]_+}{2}.
\]
Consequently, for every \(\varepsilon\ge0\),
\[
\sup_{{\substack{{\mathcal N\;\mathrm{{unital}}\;\mathrm{{qubit}}\;\mathrm{{CPTP}}\\\mathcal N\;\mathrm{{is}}\;\varepsilon\text{{-QLDP}}}}}} C(J_{{\mathcal N}})
=\frac{[3\tanh(\varepsilon/2)-1]_+}{2}.
\]
The bound is attained by the depolarizing channel
\[
\mathcal D_t(\rho)=t\rho+(1-t)\frac{I}{2},\qquad t=\tanh(\varepsilon/2).
\]
Thus the sharp qubit privacy threshold \(\varepsilon=\log 2\) at which all channels are entanglement breaking is, within the natural unital class, the zero endpoint of an exact quantitative privacy–entanglement curve.

## Assumptions and scope
Pure quantum local differential privacy means \(\delta=0\): for every pair of input states \(\rho,\sigma\) and every effect \(0\le M\le I\),
\[
\operatorname{{Tr}}[M\mathcal N(\rho)]\le e^\varepsilon\operatorname{{Tr}}[M\mathcal N(\sigma)].
\]
The result is restricted to unital qubit channels. Concurrence is the ordinary two-qubit concurrence of the normalized Choi state. The theorem does not claim the same quantitative curve for nonunital channels, higher input dimension, or approximate \((\varepsilon,\delta)\)-privacy with \(\delta>0\).

## Proof
Let \(s_1=\|T\|_2\). Every input Bloch vector satisfies \(\|r\|_2\le1\), hence every output Bloch vector has length at most \(s_1\). Therefore every output state obeys the operator bounds
\[
\frac{1-s_1}{2}I\le\mathcal N(\rho)\le\frac{1+s_1}{2}I.
\]
For \(s_1<1\), these imply
\[
\mathcal N(\rho)\le\frac{1+s_1}{1-s_1}\mathcal N(\sigma)
\]
for all \(\rho,\sigma\), so the channel is \(\varepsilon\)-QLDP with \(\varepsilon=\log((1+s_1)/(1-s_1))\). Equality is forced: choose a unit right singular vector \(r_*\) with \(\|Tr_*\|_2=s_1\), use the antipodal pure inputs \(r_*\) and \(-r_*\), and measure the rank-one projector along \(Tr_*\). The two outcome probabilities are \((1+s_1)/2\) and \((1-s_1)/2\). Hence
\[
\varepsilon_*(\mathcal N)=\log\frac{1+s_1}{1-s_1}=2\operatorname{{arctanh}}(s_1).
\]
If \(s_1=1\), the smaller probability vanishes while the larger one does not, so no finite pure-privacy parameter is possible.

Pre- and post-composition by qubit unitaries acts on \(T\) by rotations and on \(J_{{\mathcal N}}\) by local unitaries. It therefore preserves both \(\varepsilon_*\) and Choi concurrence. A unital qubit channel can consequently be put in diagonal Pauli form with signed contractions \(\lambda_1,\lambda_2,\lambda_3\), whose absolute values are \(s_1,s_2,s_3\). Its Choi state is Bell diagonal. The standard unital-qubit entanglement-breaking octahedron is
\[
|\lambda_1|+|\lambda_2|+|\lambda_3|\le1.
\]
Outside this octahedron, complete positivity places the channel in one Bell-vertex sector, where the largest Bell weight is
\[
p_{{\max}}=\frac{1+s_1+s_2+s_3}{4}.
\]
For a Bell-diagonal two-qubit state, Wootters' formula gives \(C=[2p_{{\max}}-1]_+\). Combining the inside- and outside-octahedron cases yields
\[
C(J_{{\mathcal N}})=\frac{[s_1+s_2+s_3-1]_+}{2}.
\]

Now suppose \(\mathcal N\) is \(\varepsilon\)-QLDP. The exact privacy formula gives
\[
s_1\le t:=\tanh(\varepsilon/2),
\]
and therefore \(s_1+s_2+s_3\le3t\). Thus
\[
C(J_{{\mathcal N}})\le\frac{[3t-1]_+}{2}.
\]
For sharpness take \(\mathcal D_t(\rho)=t\rho+(1-t)I/2\). Its three Bloch singular values all equal \(t\), its exact privacy parameter is \(2\operatorname{{arctanh}}(t)=\varepsilon\), and its Bell-diagonal Choi state has weights \((1+3t)/4\) and three copies of \((1-t)/4\). Hence its concurrence equals \([3t-1]_+/2\), proving the stated supremum.

## Verification
The proof was checked independently at each structural step: the QLDP parameter was derived directly from extremal output eigenvalues and an attaining antipodal input pair; the Choi concurrence formula was reduced to the canonical Bell-diagonal form; and the optimizing depolarizing channel was substituted explicitly. A deterministic checker included with this package exhausts a rational grid of Pauli channels, verifies the concurrence upper bound against the exact largest Bloch singular value, checks the entanglement-breaking octahedron on that grid, and verifies equality for representative depolarizing channels. These finite checks are consistency tests only; the proof above is analytic.

## Relationship to prior work
Bhalerao, Nuradha, and Leditzky prove that every \(\varepsilon\)-QLDP channel with qubit input is entanglement breaking for \(\varepsilon\le\log 2\), and that the constant is optimal. Their theorem is binary: it identifies when entanglement must vanish, but it does not quantify how much Choi entanglement a private channel can retain above the threshold. Their earlier privacy–utility work gives the exact privacy parameter of the depolarizing mechanism and proves its optimality for several state-utility metrics, not for Choi-state entanglement. Standard unital-qubit channel geometry supplies the Pauli singular-value canonical form and the entanglement-breaking octahedron, while Wootters supplies the Bell-diagonal concurrence formula. Combining those ingredients with the exact QLDP extremal-output calculation yields the quantitative curve above; targeted literature and semantic-index comparisons did not locate this exact statement.

## Limitations
The quantitative optimum is proved only for unital qubit channels and pure QLDP. The recent all-channel theorem already determines the zero branch up to \(\varepsilon=\log 2\), but the positive branch here should not be extrapolated to nonunital channels or higher dimensions without a separate optimization. The originality check was targeted rather than exhaustive; an equivalent formula could exist under different terminology for channel-resource tradeoffs. The standard canonical-form and concurrence ingredients are classical; the new content is the exact privacy–concurrence optimization and its sharp depolarizing realization.

## References
1. S. Bhalerao, T. Nuradha, and F. Leditzky, *High quantum local differential privacy breaks entanglement*, arXiv:2609.13418v1 (first public 2026-09-11).
2. T. Nuradha, S. Bhalerao, and F. Leditzky, *Privacy-Utility Tradeoffs in Quantum Information Processing*, arXiv:2602.10510v1 (2026), especially the exact depolarizing-channel privacy condition.
3. M. B. Ruskai, *Qubit Entanglement Breaking Channels*, arXiv:quant-ph/0302032 (2003).
4. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, arXiv:quant-ph/9709029; Phys. Rev. Lett. 80, 2245–2248 (1998).
5. M.-D. Choi and C.-K. Li, *On unital qubit channels*, Quantum Information and Computation 23 (2023), 562–576.
