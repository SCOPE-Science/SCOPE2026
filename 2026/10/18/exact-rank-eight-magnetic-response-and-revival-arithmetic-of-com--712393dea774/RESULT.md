# Exact rank-eight magnetic response and revival arithmetic of complete-bipartite Grover walks

## Finding

Let \(m,n\ge 2\) be integers. Consider the arc-space Grover walk on the complete bipartite graph \(K_{m,n}\) with a magnetic phase \(\beta\in\mathbb R\) on one undirected edge, assigned opposite signs in its two orientations. The resulting unitary \(U_\beta\) acts on \(2mn\) directed arcs. Set
\[
\theta=\frac12\arcsin\!\left(\frac{4\sqrt{(m-1)(n-1)}}{mn}|\sin(\beta/2)|\right)\in[0,\pi/4].
\]
**Theorem (exact magnetic spectrum and revivals).** For every \(m,n\ge2\) and every real \(\beta\), the full characteristic polynomial is
\[
\det(zI-U_\beta)=
(z^2-1)^{mn-m-n}(z^2+1)^{m+n-4}
\bigl(z^8-2\cos(4\theta)z^4+1\bigr).
\]
Thus the only eight eigenvalues counted with multiplicity that can move under the phase are the fourth roots of \(e^{4i\theta}\) and of \(e^{-4i\theta}\). For every positive integer \(k\),
\[
\|U_\beta^{4k}-I\|_{\mathrm{op}}=2|\sin(2k\theta)|,
\qquad
\|U_\beta^{4k}-I\|_{\mathrm F}^{2}=32\sin^2(2k\theta).
\]
In particular, for \(\beta\notin2\pi\mathbb Z\), the operator \(U_\beta^4-I\) has **rank exactly eight**, irrespective of the graph size, and
\[
\|U_\beta^4-I\|_{\mathrm{op}}=
\frac{8\sqrt{(m-1)(n-1)}}{mn}|\sin(\beta/2)|.
\]
Full exact periodicity \(U_\beta^T=I\) for some positive integer \(T\) holds if and only if \(\theta/\pi\in\mathbb Q\). If \(\theta/\pi=p/q\) in lowest terms, with \(q\ge1\), the **minimal** such period is
\[
T_{\min}=\frac{4q}{\gcd(q,2)}.
\]
For every fixed \(m,n\ge2\), the exactly periodic magnetic phases are countable and dense modulo \(2\pi\), but form a Lebesgue-null set. At an aperiodic phase, arbitrarily accurate operator-norm revivals still occur at multiples of four.

## Assumptions and scope

Choose the bipartition \(L=\{1,\ldots,m\}\), \(R=\{1,\ldots,n\}\); every pair \((u,v)\in L\times R\) is an edge. The arc set \(\mathcal A\) comprises both orientations of all \(mn\) edges. On \(\mathbb C^{\mathcal A}\), define the incidence coisometry \(d\) by
\[
(d\psi)(u)=\frac{1}{\sqrt{\deg u}}
\sum_{a:\,o(a)=u}\psi(a).
\]
Define \(C=2d^*d-I\). Select the undirected edge joining the first vertices of \(L\) and \(R\); define \(B(a)=\beta\) on its orientation from \(L\) to \(R\), \(B(a)=-\beta\) on the reverse orientation, and zero elsewhere. The magnetic flip is \((S_\beta\psi)(a)=e^{iB(a)}\psi(a^{-1})\). The walk is \(U_\beta=S_\beta C\). Both factors are unitary involutions. Edge transitivity makes the reference-edge choice immaterial to the spectrum. This is the single-edge magnetic Grover convention of Sekido and Segawa (2026); simultaneous phases on multiple edges are not assumed.

The operator norm is the induced Hilbert-space norm, and \(\|M\|_{\mathrm F}^2=\operatorname{tr}(M^*M)\). No small-phase expansion, balanced-size assumption, or large-graph limit is used.

## Proof

**1. An exact determinant identity.** Let \(v=m+n\) and \(e=mn\). By construction \(dd^*=I_v\), \(S_\beta^2=I\), and \(S_\beta^*=S_\beta\). Define the Hermitian discriminant \(Q_\beta=dS_\beta d^*\). For \(z\notin\{-1,1\}\), the matrix determinant lemma yields
\[
\begin{aligned}
\det(zI-U_\beta)
&=\det(zI+S_\beta-2S_\beta d^*d)\\
&=\det(zI+S_\beta)\,
\det\!\left(I_v-2d(zI+S_\beta)^{-1}S_\beta d^*\right).
\end{aligned}
\]
The magnetic flip has \(e\) independent two-dimensional arc-pair blocks with eigenvalues \(+1,-1\), so \(\det(zI+S_\beta)=(z^2-1)^e\). Moreover,
\[
(zI+S_\beta)^{-1}S_\beta=\frac{zS_\beta-I}{z^2-1}.
\]
Therefore
\[
\det(zI-U_\beta)=(z^2-1)^{e-v}
\det\!\left((z^2+1)I_v-2zQ_\beta\right).
\tag{1}
\]
Both sides are polynomials after cancellation and thus the identity holds for every \(z\). Here \(e-v=mn-m-n\ge0\) because \(m,n\ge2\).

**2. The magnetic discriminant is rank two.** In the vertex order \(L,R\), \(Q_\beta\) has the form
\[
Q_\beta=\frac1{\sqrt{mn}}
\begin{pmatrix}0&B_\beta\\B_\beta^*&0\end{pmatrix},
\qquad
B_\beta=\mathbf1_m\mathbf1_n^\top+(e^{i\beta}-1)e_1e_1^\top.
\]
For a nontrivial phase, the rank of \(B_\beta\) is two. Its two nonzero squared singular values before dividing by \(mn\) have sum \(mn\) (the sum of the squares of all entries) and product
\[
4(m-1)(n-1)\sin^2(\beta/2).
\tag{2}
\]
For completeness, factor the first special row of \(B_\beta\) and the repeated remaining rows through orthogonal left vectors \(e_1\) and \(\sum_{j=2}^m e_j\). The determinant of the resulting \(2\times2\) Gram matrix equals
\[
(m-1)\bigl(n^2-|n-1+e^{i\beta}|^2\bigr),
\]
which gives (2). For \(\beta\in2\pi\mathbb Z\), the second singular value is zero, and the formulas below hold by continuity.

After normalization, write the two singular values as \(c,s\) with \(c\ge s\ge0\). They obey
\[
c^2+s^2=1,
\qquad
c^2s^2=\frac{4(m-1)(n-1)}{m^2n^2}\sin^2(\beta/2).
\]
Since \(4\sqrt{(m-1)(n-1)}\le mn\), there is a unique \(\theta\in[0,\pi/4]\) such that \(c=\cos\theta\), \(s=\sin\theta\). This angle is the stated one. The eigenvalues of \(Q_\beta\) are \(\pm c,\pm s\), together with zero of multiplicity \(m+n-4\), interpreted with their algebraic multiplicities at degeneracies.

**3. Factorization and exact four-step defect.** Insert this spectrum into (1). Pairing \(c\) and \(-c\), then \(s\) and \(-s\), gives
\[
\begin{aligned}
&\bigl((z^2+1)^2-4c^2z^2\bigr)
\bigl((z^2+1)^2-4s^2z^2\bigr)\\
&\hspace{12mm}=(z^4-e^{4i\theta})(z^4-e^{-4i\theta})
=z^8-2\cos(4\theta)z^4+1.
\end{aligned}
\]
The remaining discriminant-zero modes contribute \((z^2+1)^{m+n-4}\), while the determinant factor contributes \((z^2-1)^{mn-m-n}\). This proves the characteristic polynomial. Unitarity ensures diagonalizability, even when eigenvalues collide.

At time \(4k\), every eigenvalue from the first two factors becomes one. The last factor supplies four occurrences of \(e^{4ik\theta}\) and four of \(e^{-4ik\theta}\), counted with multiplicity. Taking the maximum modulus and the sum of squared moduli of the deviations from one proves the two norm identities. If \(\beta\notin2\pi\mathbb Z\), then \(0<\theta\le\pi/4\), so \(e^{\pm4i\theta}\ne1\), and the defect at four steps has rank precisely eight. The explicit four-step revival deficit follows on substituting \(\sin(2\theta)=4\sqrt{(m-1)(n-1)}|\sin(\beta/2)|/(mn)\).

**4. Complete period classification.** The eight-factor eigenvalues can be listed as \(i^j e^{i\theta}\) and \(i^j e^{-i\theta}\), for \(j=0,1,2,3\), with multiplicities retained at collisions. If \(U_\beta^T=I\), the ratio of two consecutive \(j\)-values forces \(4\mid T\). Conversely, for \(T=4k\), every eigenvalue returns to one precisely when \(e^{4ik\theta}=1\). This happens for some \(k\ge1\) exactly when \(\theta/\pi\) is rational. If \(\theta/\pi=p/q\) is reduced, the condition becomes \(q\mid2k\); hence the least \(k\) is \(q/\gcd(q,2)\), giving the minimal period. The zero-phase case is included by \(p/q=0/1\).

On \([0,\pi]\), \(\theta\) is continuous and strictly increasing from zero to a positive maximum; on \([\pi,2\pi]\), it is symmetric and strictly decreasing. Thus the preimage of \(\pi\mathbb Q\) is countable and dense modulo \(2\pi\), hence null. For irrational \(\theta/\pi\), the multiples \(2k\theta\) are dense modulo \(\pi\); the exact norm identity therefore gives arbitrarily accurate approximate revivals without any exact period. This completes the proof.

## Verification

The included standalone Python checker `verify.py` constructs \(U_\beta\) directly from oriented arcs, the Grover coin, and the magnetic flip, independently of the closed characteristic-polynomial expression. It verifies unitarity, eigenvalue multisets (with multiplicities), four-step norm identities, fourth-step traces, and an explicitly chosen exact rational-angle period. Ten graph/phase cases include \(K_{2,2}\), \(K_{2,3}\), \(K_{3,3}\), \(K_{3,4}\), \(K_{4,5}\), \(K_{5,6}\), and \(K_{6,7}\), as well as zero and maximal flux. A symbolic identity checks the degree-eight factor. Execution passed 193 counted independent assertions (including three exact polynomial reconstructions); numerical evidence is auxiliary, not a substitute for the determinant proof.

The exact \(\beta\)-uniform operator-norm bound tends to zero as either part size tends to infinity while the other remains at least two; for balanced \(m=n=N\), it is at most \(8(N-1)/N^2\). An explicit rational-angle example with \(m=3,n=4\) and \(\theta=\pi/17\) has minimal period \(68\), independently checked by exact spectral reasoning and numerical matrix powers.

## Relationship to prior work

Sekido and Segawa (arXiv:2607.14797, first posted July 16, 2026) introduce the magnetic arc-flip perturbation and study small-phase robustness through an effective Hermitian generator. Their Section 5 treats paths, cycles, and **regular** complete bipartite graphs \(K_{k,k}\) in that perturbative framework. That work supplies the central model and motivates asking what happens for finite, non-small flux; it does not state the full finite-flux characteristic polynomial, the eight-dimensional four-step defect, the arbitrary \(K_{m,n}\) classification, or the dense exact-periodicity set.

Standard Grover spectral mapping and determinant techniques are established. Chen (arXiv:2211.02752, 2022) treats periodicity for unmagnetized bipartite quantum walks under spectral hypotheses, not a single-edge magnetic phase. Kubota (arXiv:2609.08315, 2026) classifies certain **unmagnetized** periodic Grover graph families. Related models of magnetic or driven discrete-time walks with different lattice geometries and coins do not directly determine this one-edge, arbitrary-part-size spectrum.

The new mathematical content assessed here is the exact finite-flux rank-two singular-value reduction, rank-eight fourth-step identity, and complete arithmetic revival classification. A generic spectral mapping theorem alone leaves the graph-specific magnetic singular values and their unexpectedly single-angle factorization to be established. No claim is made to invent the Grover walk, magnetic phases, or spectral mapping.

## Limitations

The theorem concerns simple complete bipartite graphs with both parts of size at least two, the precise arc-based Grover coin and one magnetic edge (opposite orientations assigned opposite phases). It makes no claim for arbitrary multiple independent fluxes, non-Grover coins, weighted bonds of non-unit modulus, or infinite graphs. The dense exact-periodicity phases require perfectly specified real phases; experimental tolerances yield approximate, not exact, revivals. The proof is finite-dimensional and complete; the absence of prior exact formulations remains subject to the stated literature-access and indexing limitations. No external independent validation has been performed.

## References

1. H. Sekido and E. Segawa, *Robustness of periodicity in Grover walks under a magnetic vector potential*, arXiv:2607.14797v1 (first publicly posted 2026-07-16). https://arxiv.org/abs/2607.14797
2. Q. Chen, *Periodicity of bipartite walk on biregular graphs with conditional spectra*, arXiv:2211.02752v1 (2022); *Physica Scripta* **99** (2024), 105120. https://arxiv.org/abs/2211.02752
3. S. Kubota, *Spectral characterization of the uniform theta graph and classification of 6-periodic Grover walks*, arXiv:2609.08315 (2026). https://arxiv.org/abs/2609.08315
4. S. Kubota, K. Saito, and Y. Yoshie, *A new type of spectral mapping theorem for quantum walks with a moving shift on graphs*, arXiv:2103.05235 (2021). https://arxiv.org/abs/2103.05235
