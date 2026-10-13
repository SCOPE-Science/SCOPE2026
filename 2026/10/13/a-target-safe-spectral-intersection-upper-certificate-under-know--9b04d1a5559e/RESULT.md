# A target-safe spectral-intersection upper certificate under known-readout query access
## Finding
Let \(\mathcal Q=(\mathcal H,U,\{M_j\}_{j\in\mathcal C})\) be a finite-dimensional pure-state quantum classifier whose fixed total priority order \(\prec\) resolves ties, with earlier priority winning. Fix a desired target class \(k\). For every competitor \(j\neq k\), set \(A_{kj}=M_k-M_j\) and define
\[
\mathcal S_k=\left(\bigcap_{j\prec k}\operatorname{Ran}\mathbf 1_{(0,\infty)}(A_{kj})\right)\cap
\left(\bigcap_{k\prec j}\operatorname{Ran}\mathbf 1_{[0,\infty)}(A_{kj})\right).
\]
If \(P_k\) is the orthogonal projector onto \(\mathcal S_k\), \(\chi=U|\psi\rangle\), and \(p_k=\langle\chi|P_k|\chi\rangle>0\), then
\[
\varepsilon_k^*(\psi)\le 1-\sqrt{p_k},
\]
where \(\varepsilon_k^*(\psi)=\inf\{D_F(\psi,\varphi):\mathcal Q(\varphi)=k\}\). Thus a class-specific upper certificate is obtained from one binary projector probability whenever the target-safe spectral intersection has nonzero overlap with the encoded input.

## Assumptions and scope
The classifier, fidelity distance, known-readout access model, and tie-priority convention are those of Guan and Huang, arXiv:2609.11637v2. The input and witness states are pure, the internal evolution \(U\) is unitary, and the readout POVM \(\{M_j\}\) is known. The upper-bound access model permits binary projector readouts derived from that POVM. If attacks are restricted to the image of an external public encoder, the pulled-back witness must additionally belong to that image, exactly as for the source paper's upper-bound witnesses.

The order notation is used in the source sense: \(j\prec k\) means that \(j\) wins a probability tie against \(k\). The result makes no claim for unknown or noisy readout operators, mixed-state inputs, or nonunitary hidden evolution.

## Proof
Take a nonzero vector \(v\in\mathcal S_k\). If \(j\prec k\), then \(v\) lies in the strictly positive spectral subspace of \(A_{kj}\), hence
\[
\langle v|M_k|v\rangle>\langle v|M_j|v\rangle.
\]
If instead \(k\prec j\), then \(v\) lies in the nonnegative spectral subspace of \(A_{kj}\), hence
\[
\langle v|M_k|v\rangle\ge\langle v|M_j|v\rangle.
\]
Therefore every higher-priority competitor is beaten strictly, while every lower-priority competitor is beaten weakly; the fixed tie rule makes \(k\) the predicted label of every normalized vector in \(\mathcal S_k\).

Now suppose \(p_k>0\) and define
\[
|\widehat\eta_k\rangle=\frac{P_k|\chi\rangle}{\sqrt{p_k}},
\qquad
|\varphi_k\rangle=U^\dagger|\widehat\eta_k\rangle.
\]
The vector \(|\widehat\eta_k\rangle\) is normalized and belongs to \(\mathcal S_k\), so \(\mathcal Q(\varphi_k)=k\). Since \(P_k\) is an orthogonal projector,
\[
|\langle\psi|\varphi_k\rangle|
=|\langle\chi|\widehat\eta_k\rangle|
=\sqrt{p_k}.
\]
With the source's fidelity distance \(D_F(\psi,\varphi)=1-|\langle\psi|\varphi\rangle|\), this witness has distance \(1-\sqrt{p_k}\). Taking the infimum over all inputs classified as \(k\) proves the bound.

Finally, \(P_k\) is computable from the known POVM by finite-dimensional spectral decomposition and subspace intersection. Therefore \(p_k\) is the first-outcome probability of the binary readout \(\{P_k,I-P_k\}\), which is of the same derived-projector form allowed for upper-bound estimation in the known-readout model.

## Verification
The argument is analytic and finite-dimensional. The critical checks are: each spectral-subspace condition implies the required pairwise score inequality; the strict versus non-strict choice exactly matches tie priority; intersection preserves all pairwise conditions simultaneously; and orthogonal projection gives overlap \(\sqrt{p_k}\). No finite experiment, numerical optimization, or unproved computational certificate is used.

## Relationship to prior work
Guan and Huang construct pairwise positive-gap kernel spaces for \(M_k-M_t\). Their current version explicitly notes that, in a multiclass classifier, a state in the positive gap subspace can make \(k\) beat the original label \(t\) without making \(k\) the predicted label. Their Theorem 4.7 therefore supplies an untargeted upper bound by measuring pairwise kernel projectors. The present result adds a sufficient target-specific construction: impose the score inequalities against every competitor simultaneously, with the boundary chosen according to tie priority, and then apply the same projection geometry.

Dowling, West, Southwell et al. study adversarial robustness guarantees for quantum classifiers in npj Quantum Information 12, 16 (2026), including targeted robustness in a binary readout setting. That framework does not state the multiclass known-readout spectral-intersection certificate above.

## Limitations
The target-safe subspace can be \(\{0\}\), and even when it is nonzero the encoded input can have \(p_k=0\); in either case this certificate gives no nontrivial target-specific upper bound. The construction is sufficient rather than complete and need not attain the true targeted robustness radius. Noncommuting gap operators can make the intersection much smaller than the set of all states classified as \(k\). No optimality or converse is claimed.

## References
1. Ji Guan and Mingyu Huang, *Certifying Adversarial Robustness of Quantum Classifiers under Known-Readout Query Access*, arXiv:2609.11637v2 (2026), especially Sections 2, 4.1, and 4.2.
2. N. Dowling, M. T. West, A. Southwell et al., *Adversarial robustness guarantees for quantum classifiers*, npj Quantum Information 12, 16 (2026), DOI 10.1038/s41534-025-01129-3.
