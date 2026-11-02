# Prime cyclic quantum tori have a sharp single-sink capture resonance

## Finding
Let \(p,q\ge5\) be odd primes, let \(a,b,\kappa>0\) with \(a/b\in\mathbb Q_{>0}\), and consider coherent single-excitation hopping on the periodic grid \(C_p\square C_q\). A sole irreversible trap is at \((0,0)\). For the exact eventual trapping probability \(\eta(x,y)\) from site \((x,y)\), the following exhaustive alternative holds.

**Nonresonant case:** If \(p\ne q\), or if \(p=q\) and \(a\ne b\), then
\[
\eta(x,y)=f_p(x)f_q(y),\qquad f_s(z)=\begin{cases}1,&z=0,\\[2pt]1/2,&z\ne0.\end{cases}
\]
Thus the only site probabilities are \(1\), \(1/2\), and \(1/4\). The active (trap-visible) subspace has dimension \((p+1)(q+1)/4\), and the maximally mixed initial state is trapped with probability \((p+1)(q+1)/(4pq)\).

**Isotropic square resonance:** If \(p=q\) and \(a=b\), then
\[
\eta(x,y)=\begin{cases}
1,&x=y=0,\\[2pt]
1/4,&\text{exactly one of }x,y\text{ is zero},\\[2pt]
1/4,&xy\ne0\text{ and }y\equiv x\text{ or }-x\pmod p,\\[2pt]
1/8,&xy\ne0\text{ and }y\not\equiv\pm x\pmod p.
\end{cases}
\]
The active dimension is \((p+1)(p+3)/8\), so the maximally mixed capture probability is \((p+1)(p+3)/(8p^2)\). In this case exactly \(4(p-1)\) nonsink sites have probability \(1/4\), and \((p-1)(p-3)\) sites have probability \(1/8\). The formulas do not depend on the positive loss rate.

In particular, tuning equal prime-sided tori from any positive rational anisotropy \(a/b\ne1\) to precisely \(a=b\) makes the trapping dimension fall discontinuously from \((p+1)^2/4\) to \((p+1)(p+3)/8\), while a new \(1/8\) site-probability class appears.

## Assumptions and scope
Write \(V=\mathbb Z_p\times\mathbb Z_q\). The cycle adjacency \(A_s\) connects \(j\) to \(j\pm1\) modulo \(s\). With standard position basis \(\{|x,y\rangle\}_{(x,y)\in V}\), define the Hermitian Hamiltonian and no-jump generator by
\[
H=a(A_p\otimes I_q)+b(I_p\otimes A_q),\quad
G=-iH-\frac\kappa2 |0,0\rangle\langle0,0|.
\]
For each site, let \(\eta(x,y)=1-\lim_{t\to\infty}\|e^{tG}|x,y\rangle\|^2\). This equals integrated absorber loss \(\kappa\int_0^\infty|\langle0,0|e^{tG}|x,y\rangle|^2\,dt\). The "active dimension" is the dimension of the smallest \(H\)-invariant subspace containing the sink site. The maximally mixed probability is the average of \(\eta(x,y)\) over all \(pq\) starting sites. There is no assumption of weak absorption.

All claims are made for *odd prime* factors and *positive rational* coupling ratio; no formula here is asserted for composite factor lengths or other algebraic or irrational couplings. Sign changes, added magnetic flux, dephasing, and time-dependent loss are not included.

## Proof
**1. Nondecaying modes and spectral projections.** Let \(P_E\) be the orthogonal spectral projector of \(H\) at its distinct real eigenvalue \(E\), and let \(|o\rangle=|0,0\rangle\). Set \(\mathcal B=\operatorname{span}\{H^j|o\rangle:j\ge0\}=\bigoplus_E\operatorname{span}\{P_E|o\rangle\}\). This is invariant under both \(H\) and \(|o\rangle\langle o|\); so is its orthogonal complement. On \(\mathcal B^\perp\) the evolution is unitary, since the rank-one sink annihilates it. On \(\mathcal B\), any eigenvector \(v\) of \(G\) with purely imaginary eigenvalue would satisfy
\[
2\operatorname{Re}\langle v,Gv\rangle=-\kappa|\langle o,v\rangle|^2=0.
\]
It would therefore be an \(H\)-eigenvector orthogonal to \(o\), hence orthogonal to \(\mathcal B\), a contradiction. All eigenvalues of the finite-dimensional contraction \(G|_{\mathcal B}\) have strictly negative real parts, so its semigroup decays. Consequently
\[
\eta(x,y)=\sum_{E}\frac{|\langle x,y|P_E|o\rangle|^2}{\langle o|P_E|o\rangle},
\]
where every denominator is positive by translation invariance of the torus; also \(\sum_{x,y}\eta(x,y)=\dim\mathcal B\).

**2. Spectral blocks on prime cycles.** For odd prime \(s\), set \(m_s=(s-1)/2\). Distinct cycle eigenvalues and multiplicities are
\[
\alpha_{s,k}=2\cos(2\pi k/s),\quad k=0,\ldots,m_s,\qquad d_0=1,\quad d_k=2\ (k>0).
\]
If \(Q_{s,k}\) is the corresponding projector, define \(w_{s,k}=d_k/s\) and \(c_{s,k}(z)=\cos(2\pi kz/s)\). Fourier orthogonality gives
\[
\langle z|Q_{s,k}|0\rangle=w_{s,k}c_{s,k}(z),\qquad
\langle0|Q_{s,k}|0\rangle=w_{s,k}.
\]
The elementary prime-root sum \(\sum_{k=1}^{m_s}\cos(2\pi kt/s)=(s-1)/2\) when \(t=0\) and \(-1/2\) otherwise yields
\[
\sum_{k=0}^{m_s}w_{s,k}c_{s,k}(z)^2=f_s(z).
\]

**3. Exhaustiveness of the spectral collisions.** The numbers \(\alpha_{s,0},\ldots,\alpha_{s,m_s}\) have just one rational linear relation, up to scaling:
\[
\alpha_{s,0}+2\sum_{k=1}^{m_s}\alpha_{s,k}=0.
\]
Indeed, if \(\zeta\) is a primitive \(s\)-th root, any relation gives a rational polynomial of degree at most \(s-1\) vanishing at \(\zeta\). It is a rational multiple of \(1+z+\cdots+z^{s-1}\), forcing the stated coefficient ratio. Since the coefficients of that relation sum to \(s\ne0\), the \(\alpha_{s,k}\) are rationally *affinely* independent: a rational relation with coefficient sum zero must be trivial.

For distinct primes \(p,q\), the two cyclotomic fields \(\mathbb Q(\zeta_p)\) and \(\mathbb Q(\zeta_q)\) intersect in \(\mathbb Q\) (coprime-conductor cyclotomic disjointness). If \(a\alpha_{p,k}+b\alpha_{q,l}=a\alpha_{p,k'}+b\alpha_{q,l'}\), rationality of \(a/b\) implies the differences of the respective \(\alpha\)'s are rational. A nonzero difference \(\alpha_{s,k}-\alpha_{s,k'}\) is irrational: every \(\alpha_{s,k}\) with \(k>0\) has \(m_s\ge2\) distinct Galois conjugates and is therefore irrational. If both indices are positive and distinct, their difference has field trace zero, so a rational difference would be zero, contrary to distinctness. Thus \(k=k'\) and \(l=l'\).

For \(p=q\), an equality of two pair energies reduces to a rational relation among the same \(\alpha_{p,k}\), whose coefficient sum is zero. Affine independence therefore makes the coefficient of each \(\alpha_{p,j}\) vanish. With \(a\ne b\), the unordered support cannot swap unless indices coincide, yielding equality only of identical ordered pairs. With \(a=b\), the only possibility is equality of unordered pairs \(\{k,l\}=\{k',l'\}\). Thus no other energy degeneracies occur under the hypotheses.

**4. Distinct coordinate energies.** In the nonresonant case, each distinct energy corresponds to one projector \(Q_{p,k}\otimes Q_{q,l}\). Inserting its matrix entries into the formula from step 1 and factoring the double sum proves \(\eta(x,y)=f_p(x)f_q(y)\). The number of active eigenvalues (one bright vector per energy) is \((m_p+1)(m_q+1)=(p+1)(q+1)/4\).

**5. Equal-prime isotropic resonance.** Write \(p=q\), \(a=b\), \(w_k=w_{p,k}\), \(c_k=c_{p,k}\). The spectral projectors are \(Q_k\otimes Q_k\) and \(Q_k\otimes Q_l+Q_l\otimes Q_k\) for \(k<l\). Expanding their contributions in step 1 produces exactly
\[
\eta(x,y)=\frac12\left[f_p(x)f_p(y)+B_p(x,y)^2\right],\quad
B_p(x,y)=\sum_{k=0}^{m_p}w_kc_k(x)c_k(y).
\]
By \(2\cos u\cos v=\cos(u+v)+\cos(u-v)\) and the same root sum from step 2,
\[
B_p(x,y)=\frac12\left(\mathbf1_{x\equiv y\ (p)}+\mathbf1_{x\equiv-y\ (p)}\right).
\]
For odd \(p\), this equals \(1\) at \((0,0)\), \(1/2\) on the two nonzero diagonals, and \(0\) elsewhere. Substitution proves all four position classes. The number of unordered pairs \(\{k,l\}\) with \(0\le k,l\le m_p\) is \((m_p+1)(m_p+2)/2=(p+1)(p+3)/8\). Alternatively summing the site probabilities gives the same dimension. This finishes the proof for every admissible prime and coupling.

## Verification
The independent checker `verify_prime_tori.py` constructs each full real symmetric Hamiltonian, uses dense eigendecomposition, groups equal eigenvalues, and calculates site absorption by *projecting directly onto the complete Hamiltonian eigenspaces*. It never calls the theorem's Fourier or cyclotomic reductions. Its 24 comparisons cover prime pairs \((5,5),(7,7),(11,11),(5,7),(5,11),(7,11)\), each at coupling pairs \((1,1),(2,1),(1,2),(3,2)\); all 1,448 site values, bright ranks, and site sums agree within approximately \(10^{-14}\). Execute `python verify_prime_tori.py` with NumPy installed. The arbitrary-prime proof is analytic, not an extrapolation from the checked finite cases.

## Relationship to prior work
Mülken and Blumen, *Continuous-Time Quantum Walks: Models for Coherent Transport on Complex Networks* (2011), analyze Bloch spectra on periodic two-dimensional lattices in Section IV.1.1 (especially equations 39–41) and phenomenological absorption on rings and networks in Section VI (especially equations 99–114). Those known spectral and sink formulations underlie this work; neither their general presentation nor the inspected ring-trap case states the rational-coupling prime-torus single-sink site law or the equal-prime \(1/8\) resonance classification.

Giusteri, Mattiotti and Celardo (2014; revised 2015) analyze the validity of non-Hermitian sink descriptions for a ring coupled to a lead, including a disordered setting and generic-network applicability. Their central-ring geometry and finite-bandwidth concern differ from the ideal Markovian rank-one sink on an anisotropic prime torus. Earlier one-dimensional ring-trap work by Agliari, Mülken and Blumen (2009) addresses trap arrangements on a ring, not the two-factor site-resolved theorem.

The Fourier eigenvalue formula and the general rank-one spectral-projector reduction are standard antecedents. The mathematical content assessed here is the *joint* all-prime rational-coupling collision classification and the resulting exact site probabilities and isolated isotropic rank collapse. A general algorithm that evaluates projectors in any fixed finite network is not being claimed as new.

## Limitations
The result concerns zero-noise, single-excitation quantum transport on finite prime cyclic products with one absorbing site and infinite-time observation. It does not give a finite-time approach rate, treat broadband lead corrections, arbitrary irrational coupling ratios, composite cycle orders, additional traps, dephasing, or disorder. The precise historical novelty relative to unidentified specialized works remains subject to independent literature assessment; no independent audit is claimed.

## References
1. O. Mülken and A. Blumen, *Continuous-Time Quantum Walks: Models for Coherent Transport on Complex Networks*, arXiv:1101.2572v1, first public 2011-01-12, https://arxiv.org/html/1101.2572v1 (especially Sections IV.1.1 and VI).
2. G. G. Giusteri, F. Mattiotti, and G. L. Celardo, *Non-Hermitian Hamiltonian approach to quantum transport in disordered networks with sinks: validity and effectiveness*, arXiv:1411.0567v1, first public 2014-11-03, https://arxiv.org/html/1411.0567v3 (Sections II, III, VII).
3. E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288, first public 2009-03-19, https://arxiv.org/abs/0903.3288 (abstract and cited context).
