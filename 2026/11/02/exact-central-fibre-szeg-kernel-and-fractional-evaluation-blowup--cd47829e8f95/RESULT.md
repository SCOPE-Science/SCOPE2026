# Exact central-fibre Szegő kernel and fractional evaluation blowup for the pentablock

## Finding
Let \(\mathcal P\subset\mathbb C^3\) be the pentablock, with coordinates \((a,s,p)\), and let \(H^2(\mathcal P)\) be the canonical Hardy space of [1]. The natural central fibre is \(A(a)=(a,0,0)\), \(|a|<1\). For every \(|a|,|b|<1\), set \(t=a\overline b\). Then its reproducing kernel restricted to this fibre is exactly
\[
K_{\mathcal P}(A(a),A(b))=\sum_{k=0}^\infty\frac{4^k}{\binom{2k}{k}}t^k
={}_2F_1(1,1;\tfrac12;t)
=\frac{1}{1-t}+\frac{\sqrt t\arcsin\sqrt t}{(1-t)^{3/2}}.
\]
The last expression means its holomorphic continuation from \(t=0\), so it is single-valued for \(|t|<1\). The associated exact evaluation bound is
\[
|f(A(a))|^2\le K_{\mathcal P}(A(a),A(a))\,\|f\|_{H^2(\mathcal P)}^2
\quad (f\in H^2(\mathcal P)),
\]
with best possible constant and equality for nonzero multiples of the reproducing kernel. If \(r=|a|\uparrow1\), then
\[
K_{\mathcal P}(A(a),A(a))
=\frac\pi2(1-r^2)^{-3/2}-\frac\pi4(1-r^2)^{-1/2}+\frac13+O(\sqrt{1-r^2}).
\]
In particular, the optimal evaluation norm has the sharp fractional growth
\[
\|E_{A(a)}\|=\sqrt{K_{\mathcal P}(A(a),A(a))}
\sim\sqrt{\pi/2}\,(1-|a|^2)^{-3/4}.
\]

## Assumptions and scope
Let \(m_3\) denote normalized Haar probability measure on \(\mathbb T^3\). The boundary map is
\[
\Psi(\xi,\lambda_1,\lambda_2)
=\left(\frac{\xi(\lambda_1-\lambda_2)}2,\lambda_1+\lambda_2,\lambda_1\lambda_2\right),
\quad (\xi,\lambda_1,\lambda_2)\in\mathbb T^3.
\]
Put \(\mu=\Psi_*m_3\) and \(H^2(\mathcal P)=\overline{\mathbb C[a,s,p]}^{L^2(\mu)}\), with its bounded point evaluations on \(\mathcal P\) and their unique holomorphic realizations as proved in [1, Sections 2--3]. The points \(A(a)\) belong to \(\mathcal P\) for \(|a|<1\), as witnessed by the strict contraction \(\begin{pmatrix}0&0\\a&0\end{pmatrix}\). The theorem concerns **this unweighted canonical Hardy norm**, not either Jacobian-weighted space also discussed in [1].

## Proof
**1. Orthogonal reduction to the pure fibre powers.** Under an independent phase rotation of \(\xi\), the monomial \(a^j s^m p^n\) transforms by \(\xi^j\). Under the simultaneous change \((\lambda_1,\lambda_2)\mapsto(\omega\lambda_1,\omega\lambda_2)\), it transforms by \(\omega^{j+m+2n}\). Both changes preserve \(m_3\). Hence, for nonnegative integers \(j,k,m,n\),
\[
\langle a^k,a^j s^m p^n\rangle=0
\quad\text{unless }j=k\text{ and }m+2n=0.
\]
The sole remaining possibility is \(j=k,m=n=0\). Thus the closed span \(\mathcal H_a=\overline{\operatorname{span}\{a^k:k\ge0\}}\) is orthogonal to the closed span of all monomials involving \(s\) or \(p\). These subspaces together span the polynomial closure. Every polynomial in the latter subspace vanishes on \(A(\mathbb D)\); continuity of evaluations from [1, Theorem 2.4] extends this vanishing to its closure. All evaluation vectors on the fibre therefore belong to \(\mathcal H_a\).

**2. Exact norms.** Integrating on the parameter torus and using Vandermonde's identity gives
\[
\|a^k\|^2=4^{-k}\int_{\mathbb T^2}|\lambda_1-\lambda_2|^{2k}\,dm_2
=4^{-k}\sum_{j=0}^k\binom kj^2
=4^{-k}\binom{2k}{k}.
\]
Distinct pure powers are orthogonal by the first phase rotation. Consequently, the functions \(a^k/\|a^k\|\) are an orthonormal basis of \(\mathcal H_a\) and the restricted reproducing kernel is
\[
K_{\mathcal P}(A(a),A(b))=\sum_{k\ge0}\frac{(a\overline b)^k}{\|a^k\|^2}
=\sum_{k\ge0}\frac{4^k}{\binom{2k}{k}}(a\overline b)^k.
\]
The series converges normally on compact subsets of \(|a\overline b|<1\), since the coefficients are asymptotic to \(\sqrt{\pi k}\).

**3. Hypergeometric and elementary evaluations.** The identity \(4^k/\binom{2k}k=(1)_k(1)_k/((\tfrac12)_k k!)\) gives the hypergeometric expression. For an independent elementary derivation note the beta-integral identity
\[
\frac{4^k}{\binom{2k}k}=(2k+1)\int_0^1[4u(1-u)]^k\,du.
\]
Summing the absolutely convergent series when \(|t|<1\),
\[
K(t)=\int_0^1\frac{1+4tu(1-u)}{[1-4tu(1-u)]^2}\,du.
\]
The substitution \(v=2u-1\) and elementary integration produce
\[
K(t)=\frac1{1-t}+\frac{\sqrt t\arcsin\sqrt t}{(1-t)^{3/2}},
\]
first for \(0<t<1\), then throughout the disk by the identity theorem. The product \(\sqrt t\arcsin\sqrt t\) has a holomorphic Taylor series at zero, so the formula does not depend on a square-root branch there.

**4. Sharp boundary law.** Put \(u=\sqrt{1-t}\) for \(t\in(0,1)\). Since \(\arcsin\sqrt{1-u^2}=\pi/2-\arcsin u\), Taylor expansion yields
\[
\sqrt t\arcsin\sqrt t
=\frac\pi2-u-\frac\pi4u^2+\frac13u^3+O(u^4).
\]
Substitution into \(K(t)=u^{-2}+u^{-3}\sqrt t\arcsin\sqrt t\) cancels the apparent \(u^{-2}\) term and yields
\[
K(t)=\frac\pi2u^{-3}-\frac\pi4u^{-1}+\frac13+O(u).
\]
Finally the Hilbert-space reproducing property and Cauchy--Schwarz prove the sharp evaluation bound; the kernel vector attains it. This completes the proof for every \(|a|<1\).

## Verification
The standalone `verify_axial_kernel.py` checks the exact central-binomial moment identity, the hypergeometric coefficient recurrence and elementary closed form, and the boundary expansion numerically. Its finite calculations are auxiliary; steps 1--4 prove the identities for every integer degree and every point of the open fibre. It uses only the Python standard library.

## Relationship to prior work
Su--Tomar [1] construct this canonical Hardy space and prove its orthogonal decompositions (Proposition 2.2), abstract reproducing-kernel representation (Proposition 3.5), and an averaged boundary-diagonal identity (Proposition 3.6). Their results provide the functional-analytic premises but do **not explicitly state** the hypergeometric kernel on the central fibre or its fractional singularity and leading constant. The present calculation isolates a natural symmetry-fixed fibre, determines its full two-point kernel and gives the exact sharp point-evaluation rate there. The known averaged radial-diagonal identity in [1] concerns a different observable and does not by itself determine this pointwise fibre law. Jindal--Kumar [2] treat pentablock operator tuples, without a formula for the kernel of the subsequently defined canonical Hardy space.

## Limitations
This is a restriction of the kernel to \((a,0,0)\) and does not describe the full three-variable kernel or either Jacobian-weighted Hardy space. It is not a uniform estimate along arbitrary approaches to the pentablock boundary. Its historical originality is assessed against accessible primary literature and indexed records; an equivalent unpublished or differently indexed formula remains possible. No external or independent mathematical audit is asserted.

## References
[1] G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Pentablock*, arXiv:2610.17729v1 (first posted 2026-10-13), Sections 2--3, especially Propositions 2.2, 3.5 and 3.6. https://arxiv.org/abs/2610.17729

[2] A. Jindal and P. Kumar, *Operator Theory on the Pentablock*, arXiv:2406.05996v2 (2024), https://arxiv.org/abs/2406.05996
