# Exact Pauli-fidelity symmetry and quadratic breaking for anticommuting coherent gate errors

## Finding

Let \(L\ne I\) be an \(n\)-qubit Hermitian Pauli operator, let \(U=\exp(-i\pi L/4)\), and let a static Hamiltonian \(H=\alpha L+R\) have \(R\) equal to a real linear combination of Hermitian Pauli operators that anticommute with \(L\) and are pairwise anticommuting. Define the error unitary \(E=U^\dagger\exp(-itH)\), its Pauli twirl \(\mathcal T_E\), and the Pauli fidelity \(f_P=2^{-n}\operatorname{Tr}[P\mathcal T_E(P)]\). This is the fidelity of the **error channel**, not of the ideal gate itself.

Partition the Pauli operators anticommuting with \(L\) into projective two-element orbits \(\{Q,Q^\star\}\) with \(Q^\star=-iLQ\). Choose a Hermitian signed representative \(Q\) in each orbit, and write uniquely
\[
R=\sum_{\mathcal O}(a_{\mathcal O}Q_{\mathcal O}+b_{\mathcal O}Q_{\mathcal O}^\star),
\qquad a_{\mathcal O},b_{\mathcal O}\in\mathbb R.
\]
Put \(\omega=\sqrt{\alpha^2+\sum_{\mathcal O}(a_{\mathcal O}^2+b_{\mathcal O}^2)}\) and \(s=\sin(t\omega)/\omega\), with \(s=t\) if \(\omega=0\). **For every integer \(n\ge1\), every such Hamiltonian, and every real \(t\)**, the following equivalence holds:
\[
\boxed{\quad f_P=f_{UPU^\dagger}\ \text{for every Pauli }P\quad\Longleftrightarrow\quad s\,a_{\mathcal O}b_{\mathcal O}=0\ \text{for every orbit }\mathcal O.\quad}
\]
The exact aggregate defect is
\[
\boxed{\quad 4^{-n}\sum_{P\in\mathcal P_n}\bigl(f_P-f_{UPU^\dagger}\bigr)^2
=8s^4\sum_{\mathcal O}(a_{\mathcal O}b_{\mathcal O})^2.\quad}
\]
Here \(\mathcal P_n=\{I,X,Y,Z\}^{\otimes n}\) has \(4^n\) representatives; a sign on a Pauli argument never changes its fidelity. Because the nonzero transverse terms are mutually anticommuting, **at most one orbit** can contain two nonzero coefficients. Consequently a single transverse Pauli error obeys the equality *exactly at all strengths*, whereas simultaneously driving its \(L\)-rotated quadrature breaks it at order two unless \(\sin(t\omega)=0\).

For example, for \(n=1\), \(L=Z\), and \(H=\alpha Z+aX+bY\), one has the exact difference
\[
f_X-f_Y=4ab\frac{\sin^2(t\sqrt{\alpha^2+a^2+b^2})}{\alpha^2+a^2+b^2},
\]
with the continuous interpretation at a zero denominator.

## Assumptions and scope

The matrices \(I,X,Y,Z\) are the standard Hermitian qubit Pauli matrices with \(ZX=iY\). Each transverse term anticommutes with \(L\); *all distinct active transverse terms mutually anticommute*. This hypothesis is essential to \(H^2=\omega^2I\). The amplitude \(\alpha\) and time \(t\) are arbitrary real numbers; to interpret \(H\) as a perturbed physical implementation of \(U\), one may impose \(t\alpha=\pi/4\) at vanishing transverse error, but this calibration is not required for the identity. All equations are finite-dimensional exact identities. There are no Markovian dissipators, no gate compilation errors beyond \(H\), and no inference about measurement noise or fault-tolerance thresholds.

An orbit \(\{Q,Q^\star\}\) refers to projective Pauli classes modulo signs: \(Q^\star=-iLQ\) is Hermitian because \(LQ=-QL\), and applying the same transformation twice gives its negative, so its projective class returns to \(Q\). The displayed coefficients refer to these *signed*, fixed representatives. The condition \(a_{\mathcal O}b_{\mathcal O}=0\) and its square are invariant under the orientation or sign choice.

## Proof

**Step 1: Exact unitary expansion.** The pairwise anticommutations and the anticommutations with \(L\) imply \(H^2=\omega^2I\). With \(c=\cos(t\omega)\), continuity covers \(\omega=0\), and
\[
\exp(-itH)=cI-isH,\qquad U^\dagger=(I+iL)/\sqrt2.
\]
For a transverse orbit representative, \(LQ=iQ^\star\) and \(LQ^\star=-iQ\). Direct multiplication, without a small-noise expansion, gives
\[
E=\frac1{\sqrt2}\left[(c+\alpha s)I+i(c-\alpha s)L
-is\sum_{\mathcal O}\bigl((a_{\mathcal O}+b_{\mathcal O})Q_{\mathcal O}
+(b_{\mathcal O}-a_{\mathcal O})Q_{\mathcal O}^\star\bigr)\right].
\]

**Step 2: Exact Pauli probabilities.** For the unitary channel \(X\mapsto EXE^\dagger\), Pauli twirling suppresses the off-diagonal Pauli-basis terms. If \(p_T=|2^{-n}\operatorname{Tr}(TE)|^2\), its Pauli channel is \(\mathcal T_E(X)=\sum_{T\in\mathcal P_n}p_TTXT\). The only possibly nonzero weights are
\[
p_I=(c+\alpha s)^2/2,\quad p_L=(c-\alpha s)^2/2,
\quad p_Q=s^2(a+b)^2/2,\quad p_{Q^\star}=s^2(b-a)^2/2.
\]
In the last two terms, \(Q,Q^\star,a,b\) belong to one orbit and \(p_{Q^\star}\) means the weight of its unsigned canonical class. The weights add to \(c^2+s^2\omega^2=1\). Their within-orbit difference is
\[
p_Q-p_{Q^\star}=2s^2ab.
\]

**Step 3: Fourier characterization of conjugate fidelity.** For Hermitian Paulis define \(\chi(P,T)\in\{+1,-1\}\) by \(PT=\chi(P,T)TP\). Then
\[
f_P=\sum_{T\in\mathcal P_n}p_T\chi(P,T).
\]
The Clifford adjoint fixes a Pauli class if it commutes with \(L\), and sends an anticommuting class \(P\) to the class of \(-iLP\). In the latter case the character on every transverse \(T\) changes sign, while the characters on \(I\) and \(L\) do not. For each such \(P\), \(\chi(P,Q^\star)=-\chi(P,Q)\). Thus
\[
f_P-f_{UPU^\dagger}=
\begin{cases}
0,&[P,L]=0,\\
4s^2\sum_{\mathcal O}a_{\mathcal O}b_{\mathcal O}\chi(P,Q_{\mathcal O}),&\{P,L\}=0.
\end{cases}
\]
The restriction of distinct Pauli characters to the affine coset \(\{P:\chi(P,L)=-1\}\) is orthogonal unless their labels differ by multiplication by \(L\). The construction picks one representative per such orbit; hence the displayed restricted characters are pairwise orthogonal. In particular, the difference vanishes for every \(P\) **if and only if** all \(s^2a_{\mathcal O}b_{\mathcal O}\) vanish. Since \(s,a,b\) are real, that is equivalent to \(sa_{\mathcal O}b_{\mathcal O}=0\). Squaring, summing over \(4^n\) Pauli arguments, and observing that the anticommuting coset has \(4^n/2\) elements yields
\[
4^{-n}\sum_P\bigl(f_P-f_{UPU^\dagger}\bigr)^2
=(16s^4)(1/2)\sum_{\mathcal O}(a_{\mathcal O}b_{\mathcal O})^2,
\]
which is the claimed formula. This also covers the case \(s=0\) exactly.

**Step 4: Restriction to one active paired orbit.** If \(Q\) and \(Q^\star=-iLQ\) are both active, another Pauli \(T\) anticommuting with both \(L\) and \(Q\) necessarily **commutes** with \(Q^\star\), because \(\chi(T,Q^\star)=\chi(T,L)\chi(T,Q)=(+1)\). Thus no third active Pauli can coexist in the mutually anticommuting family. This proves the stated one-pair simplification. The single-qubit example follows by taking \(Q=X\), \(Q^\star=Y\), and \(P=X\).

## Verification

The included script `artifacts/verify.py` constructs all \(4^n\) Pauli matrices in the tested dimensions, exponentiates the Hamiltonian independently using `scipy.linalg.expm`, directly computes twirled probabilities and all Pauli fidelities, and compares both the exact weight formulas and the aggregate defect. It checks 106 deterministic finite configurations (including paired and unpaired transverse axes, a three-axis family, negative amplitudes, randomized strengths, and a sine-zero case) to tolerance \(3\times10^{-10}\); output: `VERIFY_OK 106 matrix experiments`. These tests corroborate but do not replace the all-dimension analytic proof. To replay, install `artifacts/requirements.txt` and execute `python artifacts/verify.py` from the extracted package root.

## Relationship to prior work

Malekakhlagh, Chen, Govia, and Seif (arXiv:2607.02481v1) identify *first-order* conjugate-Pauli-fidelity symmetry under coherent Lindbladian perturbations and derive first-order dissipative selection rules. The present claim is a nonperturbative **if-and-only-if** criterion and exact squared-defect identity for the narrower static, mutually anticommuting Hamiltonian family. In particular, the quadratic two-quadrature term agrees with the reported absence of any linear coherent asymmetry; the claim does not challenge that perturbative conclusion. The publicly accessible abstract and targeted descriptions of that manuscript were compared; an inaccessible primary full-text comparison remains an originality risk.

Cai, Xu, and Benjamin (arXiv:1906.06270) study mitigation of coherent error via Pauli conjugation, including its action on interference among error amplitudes and on *logical* fidelities after error correction. They provide standard Pauli-twirling background, but the inspected discussion does not give this gate-adjoint all-order criterion or its squared fidelity-defect identity. Cai and Benjamin (arXiv:1807.04973) study construction of reduced twirling sets, a different objective. The classical Pauli-character Fourier transform underlying the proof is standard; originality is claimed only for its exact Hamiltonian-orbit application and quantitative classification, not the transform itself.

## Limitations

The theorem makes no assertion about general sums of nonanticommuting errors, dissipative generators, temporally varying Hamiltonians, SPAM ambiguity removal, or experimentally accessible fidelity estimates. It is a statement about the mathematical Pauli-twirled unitary error channel, not the untwirled coherent channel. It does not prove that an arbitrary all-orders coherent-noise model enjoys the symmetry. The cited anchor's complete full text could not be inspected; a differently described appendix specialization could affect novelty. No independent audit is asserted.

## References

1. M. Malekakhlagh, E. H. Chen, L. C. G. Govia, A. Seif, *Symmetries of Pauli Noise from Lindbladian Dynamics*, arXiv:2607.02481v1 (first posted 2026-07-02), https://arxiv.org/abs/2607.02481.
2. Z. Cai, X. Xu, S. C. Benjamin, *Mitigating Coherent Noise Using Pauli Conjugation*, arXiv:1906.06270; *npj Quantum Information* **6**, 17 (2020), https://doi.org/10.1038/s41534-019-0233-0.
3. Z. Cai, S. C. Benjamin, *Constructing Smaller Pauli Twirling Sets for Arbitrary Error Channels*, arXiv:1807.04973, https://arxiv.org/abs/1807.04973.
