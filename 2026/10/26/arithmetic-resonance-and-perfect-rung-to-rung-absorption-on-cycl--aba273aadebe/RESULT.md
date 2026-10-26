# Arithmetic resonance and perfect rung-to-rung absorption on cyclic quantum ladders

## Finding

A single irreversible absorber on a finite cyclic two-leg ladder has a sharp divisibility-dependent absorption profile. Let \(n\ge3\), let \(G_n=C_n\square K_2\), and use the unweighted adjacency Hamiltonian \(H_n\) on its \(2n\) vertices. Fix a rung \(0\), put a sink of arbitrary strength \(\gamma>0\) at \(v=(0,0)\), and write \(w=(0,1)\) for the other vertex of that rung. The subnormalized state from an initial unit vector \(\psi\) evolves as
\[
 \psi(t)=\exp[-i(H_n-i\gamma|v\rangle\langle v|)t]\psi.
\]
The eventual survival is the nonnegative limit \(S(\psi)=\lim_{t\to\infty}\|\psi(t)\|^2\). Let \(\mathbf1_{d\mid n}\) be \(1\) if \(d\) divides \(n\), and \(0\) otherwise.

**Theorem.** For every integer \(n\ge3\) and every \(\gamma>0\), the dimension of the absorbing (bright) subspace is
\[
 R_n=2\left(\left\lfloor\frac n2\right\rfloor+1\right)
      -2\mathbf1_{4\mid n}-\mathbf1_{6\mid n}.
\]
The complementary nondecaying (dark) subspace has dimension \(2n-R_n\). For the initial excitation at the other vertex of the same rung,
\[
 \boxed{\ S(w)=\frac{8}{3n}\mathbf1_{4\mid n}
                    +\frac{2}{n}\mathbf1_{6\mid n}.\ }
\]
Thus a sink on one leg absorbs an excitation on the opposite leg of its rung **with probability one** precisely when \(4\nmid n\) and \(6\nmid n\); in spite of this, the system always has dark states. For the maximally mixed one-particle initial state, the eventual absorption probability is \(R_n/(2n)\).

For example, the survival from \(w\) equals \(2/3\) for \(n=4\), \(1/3\) for \(n=6\), \(7/18\) for \(n=12\), and zero for \(n=5,7,9,10\). These are exact eventual probabilities, not finite-time approximations.

## Assumptions and scope

The graph is the Cartesian product of the simple cycle \(C_n\) and the single edge \(K_2\). Its vertices are \((j,\ell)\), \(j\in\mathbb Z/n\mathbb Z\), \(\ell\in\{0,1\}\). Edges join \((j,\ell)\) to \((j\pm1,\ell)\), and \((j,0)\) to \((j,1)\). Every edge has hopping amplitude \(1\) and there is no magnetic phase, disorder, or diagonal on-site potential. The non-Hermitian loss is \(-i\gamma|v\rangle\langle v|\); no population is reinjected. The conclusions hold for all \(\gamma>0\), including arbitrarily small loss rates, but \(\gamma=0\) is excluded.

The bright subspace is the smallest \(H_n\)-invariant subspace containing \(|v\rangle\), equivalently \(\operatorname{span}\{H_n^k|v\rangle:k\ge0\}\). The dark subspace is its orthogonal complement. The asymptotic norm equals the squared projection onto the dark subspace, as proved below.

## Proof

**1. Dissipative reduction.** Let \(K=H_n-i\gamma|v\rangle\langle v|\). For \(\psi(t)=e^{-iKt}\psi(0)\),
\[
 \frac{d}{dt}\|\psi(t)\|^2=-2\gamma|\langle v,\psi(t)\rangle|^2\le0.
\]
An eigenvector with an eigenvalue of \(K\) having zero imaginary part must vanish at \(v\), and is then an eigenvector of \(H_n\). Such eigenvectors lie in the dark space. Conversely the entire dark space is \(H_n\)-invariant and has no amplitude at \(v\). Finite-dimensional contractivity rules out nontrivial Jordan blocks on the imaginary axis of \(-iK\); the remaining eigenvalues have strictly negative real parts. Therefore
\[
 \lim_{t\to\infty}\|e^{-iKt}\psi\|^2=\|P_{\rm dark}\psi\|^2.
\]
This also proves loss-rate independence.

**2. Spectrum and cyclic dimension.** The ring adjacency has distinct eigenvalues
\[
 a_k=2\cos(2\pi k/n),\qquad 0\le k\le\lfloor n/2\rfloor.
\]
Their multiplicities are \(m_k=1\) at \(k=0\) and additionally at \(k=n/2\) for even \(n\), and \(m_k=2\) otherwise. The squared norm of the ring spectral projection of \(|0\rangle\) is \(q_k=m_k/n>0\). Tensoring with the two transverse eigenvectors \((|0\rangle\pm|1\rangle)/\sqrt2\) gives energies \(a_k+1\) and \(a_k-1\), and every distinct resulting energy has a nonzero projection of \(|v\rangle\). The bright dimension is therefore the number of *distinct* energies in the union of these two lists, not the sum of their eigenspace multiplicities.

**3. Elementary cyclotomic sign lemma.** Suppose \(\alpha=z+z^{-1}=2\cos\theta\), where \(z\) is a root of unity, and all algebraic conjugates of \(\alpha\) are nonnegative. Then \(\alpha\in\{0,1,2\}\). Here is a proof, included to avoid an unproved classification of trigonometric coincidences.

Let \(m\) be the exact order of \(z\), and set \(\alpha_u=z^u+z^{-u}\) for \(u\) running over the units modulo \(m\). All \(0\le\alpha_u\le2\), hence \(\alpha_u^2\le2\alpha_u\). Write \(\varphi\) for Euler's totient and \(\mu\) for the Möbius function. The elementary Ramanujan sums give
\[
 \sum_u\alpha_u=2\mu(m),\qquad
 \sum_u\alpha_u^2=2\varphi(m)+2c_m(2),\quad
 c_m(2)=\sum_{(u,m)=1}z^{2u}.
\]
Consequently
\[
 \varphi(m)+c_m(2)\le2\mu(m). \tag{1}
\]
For odd \(m>1\), \(c_m(2)=\mu(m)\) and \(\varphi(m)\ge2\), contradicting (1). If \(4\mid m\), then \(\mu(m)=0\), and nonnegative conjugates summing to zero must all vanish: \(\alpha=0\), which requires \(m=4\). For \(m=2q\) with \(q\) odd, units modulo \(2q\) map bijectively to units modulo \(q\). Thus \(c_m(2)=\mu(q)\), \(\mu(m)=-\mu(q)\), and \(\varphi(q)\le-3\mu(q)\). The only possible odd \(q\) is \(q=3\), giving \(m=6\) and \(\alpha=1\). Finally \(m=1\) gives \(\alpha=2\). This proves the lemma.

Now suppose \(a_j-a_k=2\). Every embedding of their common cyclotomic field preserves this equality, and every conjugate of either number lies in \([-2,2]\). Thus all conjugates of \(a_j\) are nonnegative and all those of \(-a_k\) are nonnegative. The lemma applied twice yields
\[
 (a_j,a_k)\in\{(2,0),(1,-1),(0,-2)\}.
\]
All three pairs indeed satisfy the equation. The first and third pairs occur in the cycle spectrum exactly when \(4\mid n\); the middle pair occurs exactly when \(6\mid n\). Their common shifted energies are distinct, so the union of the two lists has precisely \(2\mathbf1_{4\mid n}+\mathbf1_{6\mid n}\) duplicate levels. This proves the bright-dimension formula.

**4. Survival at the opposite end of the rung.** In each noncolliding spectral block, the projections of \(|v\rangle\) and \(|w\rangle\) are parallel or antiparallel, so no dark component of \(|w\rangle\) remains. A collision between the plus sector at one ring energy and the minus sector at another has ring projection weights \(q\) and \(q'\). In the two orthogonal sector directions, the trap and source projections are proportional to
\[
  (\sqrt{q/2},\sqrt{q'/2}),\qquad
  (\sqrt{q/2},-\sqrt{q'/2}),
\]
respectively. Orthogonally subtracting the component parallel to the trap projection leaves squared norm
\[
 \frac{q+q'}2-\frac{(q-q')^2}{2(q+q')}
 =\frac{2qq'}{q+q'}.
\]
For each of the two collisions \((2,0)\) and \((0,-2)\), the weights are \(1/n,2/n\), giving \(4/(3n)\) each. For \((1,-1)\) both weights equal \(2/n\), giving \(2/n\). Different collision energies are orthogonal, so these contributions add. The claimed survival formula follows.

## Verification

The accompanying `verify.py` reconstructs the full \(2n\times2n\) adjacency matrix independently of the spectral formulas. For every \(3\le n\le42\) it compares the predicted bright dimension and opposite-leg asymptotic survival with orthogonal eigenprojector calculations, and separately checks all claimed interbranch trigonometric coincidences. For \(n=3,\ldots,10\), it additionally computes exact rational integer-matrix Krylov ranks using SymPy. The 128 checks pass under Python, NumPy, and SymPy.

These computations test finitely many sizes and finite floating-point precision. The all-\(n\) theorem rests instead on the explicit cyclotomic lemma and spectral projection proof.

## Relationship to prior work

Agliari, Mülken, and Blumen (2009; arXiv:0903.3288) developed coherent trapping on **single cycles**, including the role of degenerate Fourier modes and dependence on trap placement. The present Cartesian prism with one trap, exact divisibility formula for the local spectral support, and opposite-rung capture criterion are different assertions; the one-cycle formulas neither state nor by themselves evaluate the interlayer spectral collisions.

Dalfó and Fiol (2020) gave a broad method for computing graph local and crossed spectral multiplicities from regular partitions. Their general spectral framework encompasses the *method* of decomposing local projections, and is not claimed as new here. The inspected article does not present the prism absorber classification or this arithmetic condition. The product adjacency spectrum and spectral-projector identity are standard; the mathematical contribution assessed here is their complete arithmetic resolution and the source-specific long-time loss law, not a new general theorem on graph spectra.

Conway and Jones (1976) treated much broader trigonometric Diophantine relations. We do not claim the three rational-angle collision identities as historically new. A self-contained restricted proof is provided solely to establish the all-size prism classification without invoking an uninspected classification theorem. An unlocated result on prism spectra or cyclic quantum trapping may subsume these consequences, so historical novelty remains subject to external verification.

## Limitations

This is a one-particle, finite-dimensional, adjacency-driven, single-sink model. Positive absorption rates change time scales but not eventual survival; the theorem says nothing about finite-time profiles, absorption-time means, decoherence, Laplacian walks on irregular networks, magnetic phases, weighted rungs, additional sinks, or quantum many-body evolution. Because \(G_n\) is regular, changing from adjacency to the combinatorial Laplacian adds only a scalar shift and sign to the coherent part, but arbitrary graph perturbations need not preserve the classification. 

## References

1. E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288, first posted 2009-03-19, https://arxiv.org/abs/0903.3288.
2. C. Dalfó and M. À. Fiol, *A general method to obtain the spectrum and local spectra of a graph from its regular partitions*, Electronic Journal of Linear Algebra **36** (2020), 446–460, https://doi.org/10.13001/ela.2020.5225.
3. J. H. Conway and A. J. Jones, *Trigonometric diophantine equations (On vanishing sums of roots of unity)*, Acta Arithmetica **30** (1976), 229–240, https://doi.org/10.4064/aa-30-3-229-240.
4. D. Solenov and L. Fedichkin, *Continuous-time quantum walks on a cycle graph*, arXiv:quant-ph/0506096, first posted 2005-06-13, https://arxiv.org/abs/quant-ph/0506096.
