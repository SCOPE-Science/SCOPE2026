# Sharp boundary for antipodal-pair eigenstate classification

## Finding

Let a periodic spin-\(1/2\) chain have length \(N=4m\), \(m\geq1\), and let \(\lvert\Psi\rangle\) be any entangled-antipodal-pair (EAP) Bell product state. Its signs \(\omega_j^x\in\{-1,+1\}\) obey
\[
\sigma_j^x\lvert\Psi\rangle=\omega_j^x\sigma_{j+N/2}^x\lvert\Psi\rangle.
\]
For \(j=1\), define
\[
P_0=\sigma_1^x\sigma_{1+m}^x,\quad
P_1=\sigma_{1+m}^x\sigma_{1+2m}^x,\quad
P_2=\sigma_{1+2m}^x\sigma_{1+3m}^x.
\]
Each support has ordinary site-index diameter \(D=m=N/4\). For real \(a,b,c\),
\[
(aP_0+bP_1+cP_2)\lvert\Psi\rangle=0
\quad\Longleftrightarrow\quad
a\omega_1^x+b+c\omega_{1+m}^x=0.
\]
The annihilator in this three-string coefficient space is therefore a two-dimensional plane. It contains vectors with \(b\ne0\), whereas the published antipodal coefficient-pair rule, if extended to \(D\leq N/4\), would force \(b=0\) and \(c=-a\omega_1^x\omega_{1+m}^x\), leaving only a line. Thus the strict cutoff \(D<N/4\) cannot be weakened to \(D\leq N/4\) in that classification.

## Assumptions and scope

The chain has periodic boundary conditions and spin \(1/2\) at every site. The state is a product of Bell pairs between sites \(j\) and \(j+N/2\). The diameter convention is the ordinary index diameter \(D(X)=\max_{r,s\in X}|r-s|\), as in the source theorem, not circular distance. The claim concerns only the displayed three-string subspace at the equality boundary; it is not a classification of all Hamiltonians with support diameter at or above \(N/4\).

## Proof

The EAP identity and commutation on distinct sites give
\[
P_0\lvert\Psi\rangle
=\sigma_{1+m}^x\sigma_1^x\lvert\Psi\rangle
=\omega_1^xP_1\lvert\Psi\rangle,
\qquad
P_1\lvert\Psi\rangle=\omega_{1+m}^xP_2\lvert\Psi\rangle.
\]
Since the signs square to one, \(P_2\lvert\Psi\rangle=\omega_{1+m}^xP_1\lvert\Psi\rangle\). Hence
\[
(aP_0+bP_1+cP_2)\lvert\Psi\rangle
=(a\omega_1^x+b+c\omega_{1+m}^x)P_1\lvert\Psi\rangle.
\]
The vector \(P_1\lvert\Psi\rangle\) has unit norm and is nonzero. The scalar must therefore vanish, giving one nonzero linear constraint on \((a,b,c)\in\mathbb R^3\), whose kernel has dimension two.

The antipodal translate of the support of \(P_0\) is the support of \(P_2\), so the source coefficient-pair rule requires \(c=-a\omega_1^x\omega_{1+m}^x\). The antipodal translate of \(P_1\) is \(\{1,1+3m\}\), of ordinary diameter \(3m>N/4\); under a proposed \(D\leq N/4\) extension its coefficient is zero, and the pair rule would force \(b=0\). Those two constraints leave only a line, strictly smaller than the exact plane. This disproves that cutoff weakening.

## Verification

The proof uses only the EAP stabilizer identity, commutation on distinct sites, and \((\sigma_j^x)^2=I\). The included standalone checker enumerates the four possible sign pairs and verifies that the exact kernel contains an independent vector with \(b\ne0\), while the pair-rule line is a strict subset. This finite check corroborates the coefficient algebra; the universal statement follows from the symbolic proof, not from enumeration.

## Relationship to prior work

Chiba and Yoneta define EAP states and prove a coefficient-pair characterization under the strict assumption \(D(X)<N/4\). Their operator-pushing identity is the input here, but the three-string equality-boundary kernel and its dimension increase are not stated in their theorem. Related crosscap-state work later broadens operator-pushing constructions; its primary full text was not read in this run, so it remains a plausible overlap risk. The claim is limited to the explicit boundary witness.

## Limitations

This is a sharpness witness for one three-string subspace, not a classification of all overlapping Pauli supports. The derivation is short and uses an identity already present in the primary paper; an independent reviewer may judge the contribution too elementary despite its precise implication for the cutoff. No claim is made about new phase transitions or all support geometries at equality.

## References

1. Y. Chiba and Y. Yoneta, “Exact Thermal Eigenstates of Nonintegrable Spin Chains at Infinite Temperature,” *Physical Review Letters* 133 (2024), 170404. First public version submitted 2024-03-19, arXiv:2403.12330. https://arxiv.org/abs/2403.12330
2. M. Mestyán and B. Pozsgay, “Crosscap states with tunable entanglement as exact eigenstates of local spin chain Hamiltonians,” arXiv:2503.15640, first submitted 2025-03-19. https://arxiv.org/abs/2503.15640
