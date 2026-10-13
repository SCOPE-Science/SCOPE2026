# A nonunital Frobenius region where arbitrary qubit filters cannot delay entanglement breaking
## Finding
Let \(\Phi\) be a completely positive trace-preserving qubit channel with Bloch action
\[
r\longmapsto Mr+c,
\]
where \(M\in\mathbb R^{3\times3}\) and \(c\in\mathbb R^3\). Write \(\|M\|_{\mathrm F}\) for the Frobenius norm and \(\|c\|_2\) for the Euclidean norm. If \(\Phi\) is not entanglement breaking and
\[
\|M\|_{\mathrm F}+\|c\|_2\le 1,
\]
then for every qubit CPTP filter \(\Psi\), the concatenation \(\Phi\Psi\Phi\) is entanglement breaking. Hence the general filtered index, unitary-filtered index, and repeated-single-unitary index all equal two:
\[
N(\Phi)=N_U(\Phi)=\max_{U\in U(2)}n(U\Phi)=2.
\]
This proves the qubit unitary-filter optimality conjecture of Lami--Giovannetti on a rotation-invariant region that contains nonunital channels.

## Assumptions and scope
The channel and every intermediate filter act on one qubit. Composition is read from right to left. The statement uses the entanglement-breaking indices of Lami--Giovannetti: \(N(\Phi)\) permits arbitrary CPTP filters between copies of \(\Phi\), while \(N_U(\Phi)\) restricts those filters to unitaries. The non-entanglement-breaking hypothesis excludes the trivial index-one case.

The hypothesis is sufficient, not necessary. No assertion is made about channels with \(\|M\|_{\mathrm F}+\|c\|_2>1\), about higher-dimensional systems, or about the full conjecture for qubit channels whose filtered index exceeds two.

## Proof
Let the arbitrary CPTP filter \(\Psi\) have Bloch data \(r\mapsto Nr+d\). The composite \(\Phi\Psi\Phi\) has Bloch data
\[
A=MNM,\qquad b=MNc+Md+c.
\]
Set
\[
s=\|M\|_{\mathrm F},\qquad r_c=\|c\|_2,\qquad a=\|MN\|_{\mathrm F}.
\]
Schatten Hölder with indices two, two, and one gives
\[
\|A\|_1=\|MNM\|_1\le \|MN\|_{\mathrm F}\,\|M\|_{\mathrm F}=as.
\]
For the translation part,
\[
\|b\|_2\le \|MNc\|_2+\|Md\|_2+r_c
\le ar_c+\|Md\|_2+r_c,
\]
because \(\|MN\|_{\mathrm{op}}\le\|MN\|_{\mathrm F}=a\).

Lemma 7 of Lami--Giovannetti applies to every positive trace-preserving qubit map, hence in particular to \(\Psi=(N,d)\). Taking their auxiliary matrix to be \(M\) yields
\[
\|Md\|_2+\|MN\|_{\mathrm F}\le\|M\|_{\mathrm F},
\]
so \(\|Md\|_2\le s-a\). Therefore
\[
\begin{aligned}
\|A\|_1+\|b\|_2
&\le as+ar_c+s-a+r_c\\
&=s+r_c+a(s+r_c-1)\\
&\le s+r_c\le1.
\end{aligned}
\]
Proposition 5 of the same paper states that a qubit Bloch map \((A,b)\) is entanglement breaking whenever \(\|A\|_1+\|b\|_2\le1\). Thus \(\Phi\Psi\Phi\) is entanglement breaking for every CPTP filter \(\Psi\).

Since \(\Phi\) itself is not entanglement breaking, the general filtered index satisfies \(N(\Phi)=2\). The standard inequalities \(n(\Phi)\le N_U(\Phi)\le N(\Phi)\), together with non-entanglement-breaking of \(\Phi\), give \(N_U(\Phi)=2\). For any unitary channel \(U\), the channel \(U\Phi\) is also non-entanglement breaking, while
\[
(U\Phi)^2=U(\Phi U\Phi)
\]
is entanglement breaking because \(U\) is an admissible filter and left unitary composition preserves the entanglement-breaking property. Hence \(n(U\Phi)=2\) for every \(U\), proving the displayed equality.

The region is genuinely nonunital. For the generalized amplitude-damping channel \(\operatorname{GAD}_{p,\gamma}\), the source gives
\[
M=\operatorname{diag}(\sqrt p,\sqrt p,p),\qquad
c=(1-p)(2\gamma-1)(0,0,1)^{\mathsf T}.
\]
At \(p=1/5\) and \(\gamma=3/5\),
\[
\|M\|_{\mathrm F}=\frac{\sqrt{11}}5,\qquad
\|c\|_2=\frac4{25},\qquad
\frac{\sqrt{11}}5+\frac4{25}<1.
\]
The source's PPT criterion for generalized amplitude damping is algebraically equivalent to
\[
p\le \gamma(1-\gamma)(1-p)^2
\]
for entanglement breaking. Here the left side is \(125/625\), while the right side is \(96/625\), so this channel is not entanglement breaking. It therefore has all three filtered indices equal to two by the theorem above.

## Verification
The proof is symbolic and does not infer an infinite statement from numerical sampling. The critical external ingredients are Proposition 5 and Lemma 7 of arXiv:1411.2517; both were read in the primary full text. The accompanying `verify.py` checks the exact rational inequalities for the explicit generalized amplitude-damping witness and the algebraic equivalence of the PPT threshold used for that witness.

The norm chain is dimension-specific only through the source's qubit separability criterion and Lemma 7. The final step uses the ideal property of entanglement-breaking channels under composition with arbitrary channels.

## Relationship to prior work
Lami and Giovannetti introduce the filtered indices, state Conjecture 1 that arbitrary CPTP filtering offers no advantage over unitary filtering for qubits, and prove a partial result: for unital qubit channels, \(N_U(\Phi)=2\) implies \(N(\Phi)=2\). Their proof uses the same Proposition 5 and Lemma 7, but its hypothesis is unital and is converted into a Frobenius bound on the linear Bloch part. The nonunital condition \(\|M\|_{\mathrm F}+\|c\|_2\le1\) and the resulting arbitrary-filter theorem are not stated there.

The later optical study of Cuevas and collaborators demonstrates amendment by an intermediate unitary for rotated phase- and amplitude-damping channels. It studies chosen unitary filters rather than equality between arbitrary CPTP-filtered and unitary-filtered indices, so it does not imply the present norm region. Their cut-and-paste work studies reordering distinct noisy channel segments, again a different operation from optimizing arbitrary filters between copies of one fixed channel.

## Limitations
The theorem gives only a sufficient region for the index-two case. It neither characterizes all nonunital qubit channels with \(N(\Phi)=2\) nor resolves Conjecture 1 for channels with larger filtered index. The generalized amplitude-damping point is an explicit witness that the region is not merely a reformulation of the unital theorem; it is not claimed to be an extremal point of the region.

A residual literature risk remains that the same sufficient condition may have appeared later under different Bloch-norm or amendability terminology. Searches by the source identifier, the filtered-index notation, Frobenius/Bloch aliases, arbitrary-filter wording, and the generalized amplitude-damping parameters did not locate an implication-equivalent theorem.

## References
1. L. Lami and V. Giovannetti, *Entanglement--Breaking Indices*, arXiv:1411.2517; Journal of Mathematical Physics 56, 092201 (2015), DOI:10.1063/1.4931482. In particular Conjecture 1, Proposition 5, Lemma 7, Theorem 8, and Example 1.
2. A. Cuevas et al., *Amending entanglement-breaking channels via intermediate unitary operations*, arXiv:1707.00161; Physical Review A 96, 022322 (2017), DOI:10.1103/PhysRevA.96.022322.
3. A. Cuevas et al., *Cut-and-paste restoration of entanglement transmission*, arXiv:1604.08350; Physical Review A 96, 012314 (2017), DOI:10.1103/PhysRevA.96.012314.
