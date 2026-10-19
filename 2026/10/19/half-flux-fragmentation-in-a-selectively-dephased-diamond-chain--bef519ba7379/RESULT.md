# Half-flux fragmentation in a selectively dephased diamond chain

## Finding

**Theorem.** Let \(n\ge3\) and \(0<\phi<2\pi\). For the finite periodic diamond-chain Hamiltonian and pure-site dephasing defined below, the full limiting density matrix exists for every initial state and all strictly positive dephasing rates. The stationary operator algebra has complex dimension \(n^2+1\) when \(\phi\ne\pi\), but dimension \(n^2+n\) at \(\phi=\pi\). The bright part has a single stationary population away from half flux and \(n\) independently conserved cage populations at half flux.

For a walker initially at a monitored backbone vertex \(A_0\), its long-time return probability is exactly
\[
R^{(A)}_n(\phi)=
\begin{cases}
(2n)^{-1},&\phi\ne\pi,\\
1/2,&\phi=\pi.
\end{cases}
\]
For a walker initially at the unmonitored bridge vertex \(B_0\), its half-flux return is \(R^{(B)}_n(\pi)=5/16\), while
\[
\lim_{\substack{\phi\to\pi\\\phi\ne\pi}} R^{(B)}_n(\phi)
=\frac14+\frac{1}{8n}.
\]
Consequently the finite-size bridge-return jump is \((n-2)/(16n)>0\), and, with the infinite-time limit always taken first,
\[
\lim_{n\to\infty}R^{(B)}_n(\phi)
=\begin{cases}1/4,&0<\phi<2\pi,\ \phi\ne\pi,\\5/16,&\phi=\pi.\end{cases}
\]
These discontinuities do not depend on the positive dephasing rates.

## Assumptions and scope

Indices \(j\) run through \(\mathbb Z/n\mathbb Z\). The one-particle Hilbert space has orthonormal site vectors \(A_j,B_j,C_j\), and is ordered as the \(n\) backbone sites followed by the \(2n\) bridge sites. The only nonzero hoppings directed from bridge to backbone are \(\langle A_j|H|B_j\rangle=1\), \(\langle A_{j+1}|H|B_j\rangle=1\), \(\langle A_j|H|C_j\rangle=1\), and \(\langle A_{j+1}|H|C_j\rangle=e^{i\phi}\), with conjugate reverse hoppings. Thus
\[
H=\begin{pmatrix}0&Q\\Q^\dagger&0\end{pmatrix},
\quad Q_{j,B_j}=Q_{j+1,B_j}=Q_{j,C_j}=1,
\quad Q_{j+1,C_j}=e^{i\phi}.
\]
The magnetic phase is the flux around each rhombus in the specified gauge; the ring closing bonds carry the same rule. There are no onsite potentials or bridge-to-bridge/backbone-to-backbone hoppings.

With \(P_j=|A_j\rangle\langle A_j|\) and arbitrary rates \(\gamma_j>0\), the density matrix solves
\[
\dot\rho=-i[H,\rho]+\sum_{j=0}^{n-1}\gamma_j
\left(P_j\rho P_j-\tfrac12\{P_j,\rho\}\right).
\]
No bath acts on a bridge site. All statements concern a finite ring first; thermodynamic limits of the return probabilities are taken only after \(t\to\infty\). Flux endpoints \(\phi=0,2\pi\) are excluded because a separate rank-resonance can arise for even \(n\).

Let \(D\) project onto the bridge-supported nullspace \(\ker Q\) (extended by zero on the backbone), and put \(F=I-D\). For all phases in the stated open interval, \(\operatorname{rank}Q=n\) and \(\operatorname{rank}D=n\). The exact limiting states, which are part of the theorem, are
\[
\rho_\infty=D\rho_0D+\frac{\operatorname{Tr}(F\rho_0)}{2n}F
\qquad(\phi\ne\pi)
\]
and
\[
\rho_\infty=D\rho_0D+\frac12\sum_{j=0}^{n-1}
\operatorname{Tr}(S_j\rho_0)S_j
\qquad(\phi=\pi),
\]
where \(S_j=|A_j\rangle\langle A_j|+|r_j\rangle\langle r_j|\) is a rank-two projection and \(|r_j\rangle=Q^\dagger|A_j\rangle/2\). At half flux these \(S_j\) are mutually orthogonal and \(\sum_jS_j=F\).

## Proof

**1. Row Gram matrix and dark space.** Direct multiplication of the four hopping amplitudes incident to each rhombus gives
\[
(QQ^\dagger)_{jj}=4,
\quad (QQ^\dagger)_{j,j+1}=1+e^{-i\phi},
\]
with Hermitian transposed entries and all other entries zero (indices modulo \(n\)). For \(n\ge3\), the Fourier eigenvalues are \(4+2\cos k+2\cos(k-\phi)\), where \(k\) runs over \(2\pi\mathbb Z/n\mathbb Z\). For \(0<\phi<2\pi\) their values exceed or equal \(4-4|\cos(\phi/2)|>0\). Hence \(Q\) has full row rank, and the \(n\)-dimensional bridge nullspace is the kernel of \(H\) on the bridge sector. At \(\phi=\pi\), \(QQ^\dagger=4I_n\), so the normalized vectors \(r_j\) are orthonormal.

**2. Complete stationary algebra.** For any operator \(X\), use the Hilbert--Schmidt inner product to obtain
\[
\operatorname{Re}\langle X,\mathcal LX\rangle
=-\frac12\sum_j\gamma_j\|[P_j,X]\|_2^2.
\]
Consequently a fixed operator, or an eigenoperator with an imaginary-axis eigenvalue, must commute with every \(P_j\). Such an operator has block form \(X=\operatorname{diag}(A,T)\), where \(A=\operatorname{diag}(a_0,\ldots,a_{n-1})\) on the backbone and \(T\) acts on the bridge sector. Commuting with \(H\) gives \(QT=AQ\) and \(TQ^\dagger=Q^\dagger A\), hence \([A,QQ^\dagger]=0\).

When \(\phi\ne\pi\), every nearest-neighbor offdiagonal of \(QQ^\dagger\) is nonzero; cycle connectivity implies all \(a_j\) are equal. Since \(Q\) is surjective, the two equations force \(T\) to equal that same scalar on \(\operatorname{im}Q^\dagger\), with no mixing to \(\ker Q\), while its action on \(\ker Q\) is unrestricted. The fixed algebra is therefore \(\mathbb C F\oplus\mathcal B(\operatorname{ran}D)\), of complex dimension \(1+n^2\).

At \(\phi=\pi\), the row Gram matrix is diagonal, so the \(a_j\) are unrestricted. The corresponding bright action is scalar \(a_j\) separately on each orthogonal two-dimensional space spanned by \(A_j,r_j\). The fixed algebra is \(\bigoplus_j\mathbb C S_j\oplus\mathcal B(\operatorname{ran}D)\), of complex dimension \(n+n^2\).

To rule out nonstationary oscillations, suppose \(\mathcal LX=i\omega X\) for real \(\omega\ne0\). Dissipation again forces \([P_j,X]=0\) for every \(j\). Then \(-i[H,X]\) has only backbone--bridge offdiagonal blocks, whereas \(i\omega X\) has only diagonal blocks. Thus \(X=0\). The semigroup is Hilbert--Schmidt contractive and finite-dimensional, so the zero eigenvalue has no nontrivial Jordan block and all other eigenvalues have negative real part. Its limit is the trace-preserving Hilbert--Schmidt projection onto the displayed fixed algebra. The stated two density-matrix formulas follow by taking the normalized trace on each scalar bright block and retaining the full dark compression.

**3. Return from a backbone site.** An initial \(A_0\) is orthogonal to \(D\). Away from half flux it therefore mixes uniformly over the rank-\(2n\) bright sector, giving return \(1/(2n)\). At half flux it belongs to the rank-two sector \(S_0\), which relaxes to \(S_0/2\), giving return \(1/2\).

**4. Return from a bridge site.** At half flux, \(\langle B_0|r_j\rangle\) has squared modulus \(1/4\) for precisely \(j=0,1\), and vanishes for all other \(j\). Thus its bright weight is \(1/2\), its dark weight is \(1/2\), and its limiting return is
\[
(1/2)^2+2\cdot(1/4)(1/4)/2=5/16.
\]
Away from half flux, set \(p_n(\phi)=\langle B_0|D|B_0\rangle\). The generic stationary formula gives
\[
R^{(B)}_n(\phi)=p_n(\phi)^2+
\frac{(1-p_n(\phi))^2}{2n}.
\]
The Fourier diagonalization from Step 1 yields the exact finite-size expression
\[
p_n(\phi)=1-\frac1n\sum_{m=0}^{n-1}
\frac{2+2\cos(2\pi m/n)}{4+2\cos(2\pi m/n)+2\cos(2\pi m/n-\phi)}.
\]
At \(\phi=\pi\), \(QQ^\dagger=4I\) gives \(p_n=1/2\), and the orthogonal projector varies continuously in \(\phi\) throughout the open interval. This proves the finite jump. For fixed \(0<\phi<2\pi\), the Fourier sum tends to its Riemann integral. Recenter its angular variable at \(\phi/2\); the integrand is one half plus an odd sine term divided by the even positive factor \(1+\cos(\phi/2)\cos\theta\). The sine term integrates to zero. Thus \(p_n(\phi)\to1/2\), proving the thermodynamic assertions.

## Verification

Run `python verify.py` in an environment with the dependencies listed in `requirements.txt`. The program constructs \(Q,H,D,F,S_j\) directly; checks orthogonal-projection identities, exact finite-size return formulas and Fourier sums for several phases and sizes; computes the full Lindblad superoperator at small sizes with unequal dephasing rates; and compares long-time matrix evolution against the claimed stationary states and the predicted fixed-algebra dimensions. The computation is finite-dimensional corroboration. The arbitrary-size proof is the algebraic argument above.

## Relationship to prior work

Aharonov--Bohm localization and the half-flux collapse of dispersive bands are established prior physics, especially in Vidal, Mosseri and Douçot (1998). Baumgartner and Narnhofer (2008) developed general finite-dimensional Lindblad asymptotic-state theory. Perrin, Fuchs and Mosseri (2022) investigate cages of **discrete-time** quantum walks under noise and repeated measurements. Kolovsky (2026) analyzes dephasing-sensitive **reservoir-driven current** in open finite rhombic and SSH lattices, rather than isolated, periodically closed chains subject to dephasing only on the backbone. The present claim concerns a different, explicitly specified Lindblad generator: its full stationary algebra, its flux-triggered splitting into \(n\) bright stationary sectors, and the exact return discontinuities. None of those facts is asserted here as a consequence of the earlier band-localization statement alone.

## Limitations

The result is a one-particle finite-dimensional theorem with precisely defined hoppings and rank-one dephasing on all backbone sites. It makes no claim about finite-time robustness, disorder, interactions, chemical-potential-driven currents, non-Markovian baths, or the spectral gap near half flux. The two limits \(t\to\infty\) and \(\phi\to\pi\) do not commute; the theorem does not offer a uniform mixing-time estimate. An equivalent result in specialized literature on site-selective dephasing of rhombic chains cannot be categorically excluded.

## References

1. J. Vidal, R. Mosseri and B. Douçot, *Aharonov--Bohm cages in two-dimensional structures*, arXiv:cond-mat/9806068 (first posted 1998-06-05), Phys. Rev. Lett. 81, 5888 (1998), DOI: 10.1103/PhysRevLett.81.5888.
2. B. Baumgartner and H. Narnhofer, *Analysis of quantum semigroups with GKS--Lindblad generators II. General*, arXiv:0806.3164 (2008), J. Phys. A 41, 395303 (2008), DOI: 10.1088/1751-8113/41/39/395303.
3. H. Perrin, J.-N. Fuchs and R. Mosseri, *Robustness of Aharonov--Bohm cages in quantum walks*, arXiv:2203.04644 (2022), Phys. Rev. B 105, 235404 (2022), DOI: 10.1103/PhysRevB.105.235404.
4. A. R. Kolovsky, *Sensing decoherence by using edge states*, Phys. Rev. A 113, 042411 (2026), DOI: 10.1103/bznq-n86l.
