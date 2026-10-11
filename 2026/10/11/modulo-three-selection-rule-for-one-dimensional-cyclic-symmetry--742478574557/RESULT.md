# Modulo-three selection rule for one-dimensional cyclic symmetry breaking
## Finding
For the one-dimensional Ohta--Kawasaki and SKT cosine-Fourier settings of arXiv:2609.38629v1, fix an integer \(n\ge 2\). For \(0\le r\le \lfloor n/2\rfloor\), let \(E_r^{(n)}\) denote the closed residue-pair sector whose cosine coefficients can be nonzero only at indices
\[
k\equiv r\pmod n\qquad	ext{{or}}\qquad k\equiv-r\pmod n.
\]
Thus \(E_0^{(n)}\) is the symmetry space consisting of multiples of \(n\).

Consider a simple symmetry-breaking bifurcation satisfying the hypotheses and nondegeneracy condition of Theorem 2.4 of arXiv:2609.38629v1. Let \(L\) be the linearization and let its one-dimensional kernel be spanned by \(\varphi_\circ\notin E_0^{(n)}\). Then \(\varphi_\circ\) belongs to one unique nonzero residue-pair sector \(E_r^{(n)}\).

Whenever the doubled sector \(E_{2r}^{(n)}\) is distinct from both \(E_0^{(n)}\) and \(E_r^{(n)}\), assume that
\[
L:E_{2r}^{(n)}\longrightarrow Y_{2r}^{(n)}
\]
is Fredholm of index zero, the same type of sector condition used by the source for its \(n=5\) pitchfork proof. Then
\[
3r\not\equiv0\pmod n
\]
forces the bifurcation to be pitchfork. Hence, under the same sector-Fredholm hypothesis, transcriticality is possible only in the exceptional arithmetic sector
\[
3\mid n,\qquad r\equiv n/3\pmod n,
\]
where the pair \(\pm r\) is understood modulo \(n\).

This is sharp as a symmetry selection rule, not as an existence theorem for transcriticality: arXiv:2609.38629v1 rigorously validates one-dimensional transcritical examples with \(n=3\), while its one-dimensional \(n=2\) and \(n=5\) examples are pitchforks.

## Assumptions and scope
The statement concerns exactly the one-dimensional cosine-series symmetry spaces used for the Ohta--Kawasaki and SKT applications in arXiv:2609.38629v1. The bifurcation is assumed simple: \(\dim\ker L=1\), and the hypotheses of the source's Theorem 2.4, including its nondegeneracy condition, hold.

The residue sectors are taken componentwise for the two-component SKT system. If \(E_{2r}^{(n)}\) is a genuinely new nonsymmetric sector, the restriction of \(L\) to that sector is assumed Fredholm of index zero. No extra sector hypothesis is needed when \(E_{2r}^{(n)}=E_0^{(n)}\).

The result does not say that every case with \(3r\equiv0\pmod n\) is transcritical. It says only that this congruence is the unique way the quadratic symmetry obstruction can fail. It also makes no claim for multiple kernels, two-dimensional symmetry lattices, or a doubled-sector restriction that is not known to be Fredholm of index zero.

## Proof
Because the equilibrium \(u_\circ\) is in \(E_0^{(n)}\), multiplication by \(u_\circ\) preserves each residue-pair sector. The differential parts of both one-dimensional models are diagonal in cosine modes. The identity
\[
\cos(px)\cos(qx)=\frac12\cos((p+q)x)+\frac12\cos((p-q)x)
\]
therefore shows that \(L\) preserves every sector \(E_r^{(n)}\), not only their direct sum.

Write \(\varphi_\circ\) as the sum of its residue-pair components. Since \(L\varphi_\circ=0\) and \(L\) preserves the sectors, every nonzero component is itself in \(\ker L\). The kernel is one-dimensional, so exactly one such component can be nonzero. Thus \(\varphi_\circ\in E_r^{(n)}\) for a unique nonzero residue pair.

The same cosine product identity gives the quadratic selection rule
\[
D_{uu}F(\lambda_\circ,u_\circ)[\varphi_\circ,\varphi_\circ]
\in Y_0^{(n)}\oplus Y_{2r}^{(n)}.
\]
For Ohta--Kawasaki, the second derivative of the nonlinear term at a symmetric state consists of products of \(u_\circ\) with two critical factors; for SKT it consists of quadratic component products. In either case, the only residues produced by the square of the critical pair are \(0\) and \(\pm2r\).

The source's Lemma 5.1 proves \(Y_0^{(n)}\subset R(L)\). If \(E_{2r}^{(n)}\) is a distinct nonsymmetric sector and its restriction of \(L\) is Fredholm of index zero, then this restriction has zero kernel: any nonzero restricted kernel vector would be linearly independent of the kernel vector in \(E_r^{(n)}\). Index zero therefore makes the restricted map onto, so \(Y_{2r}^{(n)}\subset R(L)\). If \(E_{2r}^{(n)}=E_0^{(n)}\), Lemma 5.1 already gives the same conclusion. Hence the quadratic bifurcation term belongs to \(R(L)\) unless
\[
E_{2r}^{(n)}=E_r^{(n)}.
\]
For a nonzero residue pair this equality is equivalent to
\[
2r\equiv-r\pmod n,
\]
because \(2r\equiv r\pmod n\) would imply \(r\equiv0\pmod n\). Thus the exceptional equality is exactly
\[
3r\equiv0\pmod n.
\]
If the congruence fails, the quadratic term lies in \(R(L)\), and Theorem 2.4(b) of arXiv:2609.38629v1 gives a pitchfork bifurcation. A nonzero solution of \(3r\equiv0\pmod n\) exists exactly when \(3\mid n\), and the unique residue pair is \(r\equiv n/3\pmod n\).

## Verification
The proof is symbolic and uses no finite experiment as an infinite certificate. The critical implications were checked directly against the source: Theorem 2.4 identifies membership of the quadratic term in \(R(L)\) as the pitchfork criterion; Lemma 5.1 puts the symmetric target sector in \(R(L)\); Section 5.1.1 proves the \(n=5\) case by the same invariant-sector plus Fredholm-index-zero argument.

As a finite sanity check only, all residue pairs for \(2\le n\le30\) were enumerated. In every case, equality of the doubled residue pair with the original pair occurred exactly when \(3r\equiv0\pmod n\). This check is not used in the proof.

## Relationship to prior work
Breden, Sander, and Wanner develop the general transcritical/pitchfork validation framework and, in the one-dimensional applications, prove pitchfork behavior separately for \(n=2\) and \(n=5\). They explicitly note that the same argument fails for \(n=3\), where their validated examples are transcritical. The result above replaces those isolated arithmetic cases by a complete residue-pair criterion for arbitrary \(n\), under the same sector-Fredholm hypothesis used in their \(n=5\) proof.

The earlier Rizzi--Sander--Wanner work treats a zero-mass, odd-nonlinearity setting in which the reduced equation is odd and symmetry breaking is pitchfork. That theorem does not cover the non-odd/nonzero-mass setting in which transcritical bifurcations arise, and it does not state the modulo-three residue selection rule.

Targeted searches under cyclic equivariant bifurcation, quadratic Fourier interaction, residue-pair, pitchfork/transcritical, and modulo-three terminology did not locate a statement implying the criterion above. General equivariant-bifurcation literature remains a residual bibliographic risk because an equivalent character-theoretic statement could be phrased differently.

## Limitations
The result is conditional on the same type of Fredholm-index-zero check used by the motivating paper whenever the doubled residue sector is distinct from both the symmetric and critical sectors. It does not establish that this condition holds for every conceivable nonlinear diffusion operator.

The exceptional congruence \(3r\equiv0\pmod n\) removes the symmetry-forced pitchfork conclusion but does not by itself prove transcriticality. The result concerns one-dimensional cosine symmetry spaces and simple kernels only; it does not classify the two-dimensional symmetry lattices treated elsewhere in the source.

## References
1. M. Breden, E. Sander, T. Wanner, “Validation of Symmetry Induced Bifurcation Points in Nonlinear Diffusion Problems,” arXiv:2609.38629v1, first public 2026-09-29.
2. P. Rizzi, E. Sander, T. Wanner, “Cyclic symmetry induced pitchfork bifurcations in the diblock copolymer model,” arXiv:2212.08492v1; DOI 10.3934/dcdsb.2023109.
