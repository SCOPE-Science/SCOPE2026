# Sharp trace-distance amplification under projective postselection
## Finding
Let \(\rho\) and \(\sigma\) be density operators on a finite-dimensional Hilbert space and let \(P\) be an orthogonal projector. Put
\[
p=\operatorname{Tr}(P\rho),\qquad q=\operatorname{Tr}(P\sigma),
\]
and assume \(p,q>0\). For the normalized accepted states
\[
\rho_P=\frac{P\rho P}{p},\qquad \sigma_P=\frac{P\sigma P}{q},
\]
write \(c=D(\rho_P,\sigma_P)\), \(d=|p-q|\), and \(\varepsilon=D(\rho,\sigma)\), where \(D(\alpha,\beta)=\tfrac12\|\alpha-\beta\|_1\).

Then
\[
\varepsilon\ge \max\left\{d,\max\{p,q\}c\right\}.
\]
Consequently, if \(D(\rho,\sigma)\le \tau\),
\[
D(\rho_P,\sigma_P)\le \min\left\{1,\frac{\tau}{\max\{p,q\}}\right\}.
\]
This bound is best possible for every pair \(p,q>0\) and every feasible budget \(\tau\ge |p-q|\).

## Assumptions and scope
The result concerns a common orthogonal-projector postselection applied to two finite-dimensional quantum states. It makes no commutativity assumption on the input states. The acceptance probabilities must be nonzero so that normalization is defined. A feasible perturbation budget necessarily satisfies \(\tau\ge |p-q|\), because the binary measurement \(\{P,I-P\}\) cannot increase trace distance.

The theorem does not claim the same sharp formula for arbitrary trace-nonincreasing completely positive maps with different Kraus structure. It also does not address sequential composition of several postselection maps; the statement is a one-step sharp stability law.

## Proof
Let \(Q=I-P\) and apply the pinching channel
\[
\mathcal P(X)=PXP+QXQ.
\]
Trace-distance contractivity and additivity of the trace norm across the two orthogonal blocks give
\[
\varepsilon
\ge D(\mathcal P(\rho),\mathcal P(\sigma))
=\delta_P+\delta_Q,
\]
where
\[
\delta_P=\frac12\|p\rho_P-q\sigma_P\|_1,
\qquad
\delta_Q=\frac12\|Q\rho Q-Q\sigma Q\|_1.
\]
Since the trace of the accepted-block difference is \(p-q\) and the trace of the rejected-block difference is \(q-p\), the elementary bound \(\|X\|_1\ge |\operatorname{Tr}X|\) yields
\[
\delta_P\ge\frac d2,
\qquad
\delta_Q\ge\frac d2.
\]
Assume first that \(p\ge q\), so \(d=p-q\). By the triangle inequality,
\[
2pc
=\|p(\rho_P-\sigma_P)\|_1
=\|(p\rho_P-q\sigma_P)-d\sigma_P\|_1
\le 2\delta_P+d.
\]
Hence
\[
\delta_P\ge pc-\frac d2.
\]
Combining the two lower bounds for \(\delta_P\) with \(\delta_Q\ge d/2\),
\[
\varepsilon
\ge \delta_P+\delta_Q
\ge \max\left\{\frac d2,pc-\frac d2\right\}+\frac d2
=\max\{d,pc\}.
\]
If \(q\ge p\), interchange the two states. This proves
\[
\varepsilon\ge\max\left\{d,\max\{p,q\}c\right\}.
\]
The stated upper bound follows immediately from \(\varepsilon\le\tau\) and \(c\le1\).

It remains to prove sharpness. Suppose without loss of generality that \(p\ge q\), and let
\[
c_*=\min\left\{1,\frac{\tau}{p}\right\}.
\]
On a three-dimensional space with basis \(\{|0\rangle,|1\rangle,|2\rangle\}\), take \(P=|0\rangle\!\langle0|+|1\rangle\!\langle1|\) and define the commuting states
\[
\rho=pc_*|0\rangle\!\langle0|+p(1-c_*)|1\rangle\!\langle1|+(1-p)|2\rangle\!\langle2|,
\]
\[
\sigma=q|1\rangle\!\langle1|+(1-q)|2\rangle\!\langle2|.
\]
Their acceptance probabilities are exactly \(p\) and \(q\), while
\[
D(\rho_P,\sigma_P)=c_*.
\]
Direct evaluation of the diagonal trace norm gives
\[
D(\rho,\sigma)
=\frac12\left(pc_*+|p-q-pc_*|+p-q\right)
=\max\{p-q,pc_*\}.
\]
Because \(\tau\ge p-q\), this equals \(\tau\) when \(\tau<p\) and is \(p\le\tau\) when \(\tau\ge p\). Thus the universal envelope is attained for every feasible \(p,q,\tau\).

## Verification
A standalone checker in `artifacts/verify.py` performs two independent finite checks. First, it generates random density matrices and random projectors and verifies the inequality numerically. Second, it evaluates the explicit commuting sharpness family over representative regimes including unequal acceptance, equal acceptance, the minimal feasible budget, and the clipped regime.

These computations corroborate the formulas but are not the proof. The all-dimension statement follows from pinching contractivity, block additivity of the trace norm, the trace lower bound, and the triangle inequality as shown above.

## Relationship to prior work
Makwana, Patel, Joshi, and Mulherkar prove in Theorem 6 of arXiv:2609.33567v1 that the same postselection setup satisfies
\[
D(\rho_P,\sigma_P)
\le
\min\left\{1,\frac{\tau+|p-q|/2}{\max\{p,q\}\right\},
\]
and give an equal-acceptance family showing that inverse-acceptance scaling is necessary. The result here removes the extra \( |p-q|/2\) term and proves the exact optimal envelope for arbitrary unequal acceptance probabilities. The improvement is strict whenever the source bound is not already clipped at \(1\), \(p\ne q\), and \(\tau<\max\{p,q\}\).

Gavorová's arXiv:2011.08487v1 develops trace-induced and diamond-type distances for postselected computations and a conversion lemma relating postselected and ordinary map distances under additional hypotheses. That map-level framework is broader in a different direction, but the inspected conversion bounds are constant-factor statements and do not give the state-pair sharp envelope above. Shi and Waks, arXiv:2110.02290v5 and Phys. Rev. A 108, 032609, study normalized outputs of non-trace-preserving operations through an operation-level metric and renormalization method; their inspected main bounds likewise do not state this acceptance-resolved projector inequality.

## Limitations
The theorem is a sharp one-step statement for a common orthogonal projector. No claim is made for arbitrary effects, for different postselection operations on the two states, or for multistage compositions without additional analysis. The originality search found no statement with the exact \(\tau/\max\{p,q\}\) envelope, but an elementary classical conditioning analogue could exist in probability or statistics literature under terminology not captured by the inspected searches. The quantum statement and sharp commuting witnesses should therefore be read with that residual literature risk in mind.

## References
1. B. Makwana, K. Patel, M. Joshi, and J. Mulherkar, “Terminal-Register Certification for Finite-Measurement Learning of Multiscale Quantum States,” arXiv:2609.33567v1, first public 2026-09-27.
2. Z. Gavorová, “Notes on distinguishability of postselected computations,” arXiv:2011.08487v1, 2020.
3. Y. Shi and E. Waks, “Error metric for non-trace-preserving quantum operations,” arXiv:2110.02290v5; Phys. Rev. A 108, 032609 (2023).
