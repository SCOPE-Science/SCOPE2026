# Sharp one-defect phase-only Gabor tomography on finite abelian groups

## Finding
Let \(G\) be a finite abelian group of order \(N\ge 6\), and let \(E\) denote its exponent (the largest order of an element). Fix \(0\in G\). For \(|z|=1\), define \(g_z(0)=z\) and \(g_z(x)=1\) for \(x\ne0\). Write \(u_z=g_z/\sqrt N\), and form the \(N^2\) projectors \(P_{a,\chi}=|M_\chi T_a u_z\rangle\langle M_\chi T_a u_z|\), indexed by \(a\in G\) and \(\chi\in\widehat G\).

For **every** constant-modulus window, these projectors span at most \(N^2-N+1\) complex matrix dimensions. This bound is attained by the one-defect windows specified below. Among one-defect phases attaining this maximal rank, the sharp smallest positive singular value of the lifting \(X\mapsto (\operatorname{tr}(XP_{a,\chi}))_{a,\chi}\), after the common normalization shown below, and hence the sharp condition number, depends only on \(N\) and \(E\):

\[
m_E=\begin{cases}4\sin(\pi/(2E)),&E\text{ odd},\\2\sin(\pi/E),&E\text{ even},\end{cases}\qquad
\kappa_{\min}=N/m_E.
\]

For odd \(E\), the unique optimal defect phase is \(z=-1\). For even \(E\), the only optimal phases are \(z=e^{\pm i(\pi-\pi/E)}\). Each gives a projector-span rank of precisely \(N^2-N+1\). Here \(m_E\) is the minimum magnitude of the **unnormalized** Weyl ambiguity coefficients \(A_z(a,\chi)\) over the non-forced coordinates; the corresponding nonzero lifting singular values are \(|A_z(a,\chi)|/\sqrt N\). The smallest is therefore \(m_E/\sqrt N\), and the largest is \(\sqrt N\).

For example, the three abelian groups of order eight have respective best phase-only lifting condition numbers \(8/(2\sin(\pi/8))\), \(4\sqrt2\), and \(4\) for \(\mathbb Z_8\), \(\mathbb Z_4\times\mathbb Z_2\), and \((\mathbb Z_2)^3\). Thus exponent, not just order, changes the optimum.

## Assumptions and scope
Throughout, \(G\) is finite abelian and \(N\ge6\). Define \((T_a f)(x)=f(x-a)\) and \((M_\chi f)(x)=\chi(x)f(x)\). Characters are unitary. The (complex-linear) lifting maps matrices with the Hilbert–Schmidt norm to the ordinary Euclidean observation norm. Its **visible-subspace** condition number is the ratio of largest to smallest nonzero singular values, and a phase for which any ambiguity coefficient other than those forced by constant modulus vanishes is inadmissible in this optimization. This is linear matrix tomography, not a claim of recovery of every arbitrary matrix with a constant-modulus window. Multiplying the entire window by a common scalar phase does not change projectors, but the convention \(g_z(x)=1\) for all \(x\ne0\) fixes that freedom.

## Proof
**1. Weyl diagonalization and the forced nullspace.** For any unit window \(u\), the Weyl matrices \(M_\chi T_a\) form an orthogonal Hilbert–Schmidt basis. Conjugation by all Weyl matrices acts on each such basis vector by a character of \(G\times\widehat G\). Consequently the orbit of \(uu^*\) has Fourier-diagonal lifting singular values \(\sqrt N|\langle u,M_\chi T_a u\rangle|\); equivalently, for \(u=g/\sqrt N\), they are \(|A_g(a,\chi)|/\sqrt N\), where
\[
A_g(a,\chi)=\sum_{x\in G}g(x+a)\overline{g(x)}\overline{\chi(x)}.
\]
The phase conventions only permute these magnitudes. Constant modulus makes \(A_g(0,\chi)=0\) for every nontrivial \(\chi\), hence at least \(N-1\) singular values vanish. Equivalently, every rank-one projector has constant diagonal, so its span meets the diagonal matrix subspace in only the scalar diagonal direction. Therefore its rank never exceeds \(N^2-N+1\).

**2. The two-point defect identity.** Put \(z=e^{it}\). Directly separating the two terms indexed by \(x=0\) and \(x=-a\), for \(a\ne0\) one finds
\[
A_{g_z}(a,1)=N-2+2\cos t,
\quad A_{g_z}(a,\chi)=(\overline z-1)+(z-1)\chi(a)
\quad(\chi\ne1).
\]
Thus \(|A_{g_z}(a,\chi)|=|z-1|\,|z-\overline{\chi(a)}|\) for \(a\ne0\), \(\chi\ne1\). The identity \(A_{g_z}(0,1)=N\) and the forced vanishing for \(a=0\), \(\chi\ne1\), complete the spectrum. Every \(E\)-th root of unity is achieved as \(\chi(a)\) for some element \(a\) of order \(E\), because finite abelian character restriction to \(\langle a\rangle\) is surjective. Every **nontrivial** such root can be achieved with \(\chi\ne1\).

**3. Sharp circle spacing.** Set \(\zeta_j=e^{2\pi i j/E}\). Every candidate obeys
\[
\min_{a\ne0,\,\chi\ne1}|A_{g_z}(a,\chi)|
\le |z-1|\min_{1\le j<E}|z-\zeta_j|.
\]
Conjugating \(z\) if needed reduces the maximization to \(z=e^{it}\) with \(0\le t\le\pi\). On each arc between successive nonidentity \(E\)-th roots, the product is controlled by the distance to the nearer endpoint. On the half-arc from \(0\) to the first nonidentity root it has maximum \(4\sin^2(\pi/(2E))\), attained at \(t=\pi/E\); at successive gap midpoints it has value \(4\sin(t/2)\sin(\pi/(2E))\), strictly increasing toward \(t=\pi\). Indeed, before each midpoint both sine factors increase; after it, for right endpoint angle \(r\), the product is \(2[\cos(t-r/2)-\cos(r/2)]\), which decreases since \(t\ge r/2\) on that half of every gap beyond the first. The final gap midpoint is \(t=\pi\) when \(E\) is odd and \(t=\pi-\pi/E\) when \(E\) is even; for \(E=2\), the same assertion reduces to maximizing \(2\sin t\). This proves the sharp upper bounds
\[
\max_{|z|=1}|z-1|\min_{1\le j<E}|z-\zeta_j|
=\begin{cases}4\sin(\pi/(2E)),& E\text{ odd},\\2\sin(\pi/E),& E\text{ even}.
\end{cases}
\]
It also proves uniqueness up to conjugation and identifies the phases claimed above.

**4. No additional zeros and no hidden smaller coefficient at the optimizer.** At these phases, the root \(1\) is at least as far from \(z\) as the closest nontrivial \(E\)-th root. Hence allowing nontrivial characters with \(\chi(a)=1\) does not change the minimum. At each optimal phase the scalar correlation \(N-2+2\cos t\) exceeds \(m_E\): for \(N\ge8\), it is at least \(N-4\ge4>m_E\); at \(N=6\), where \(E=6\), it is \(4-\sqrt3>1=m_E\); at \(N=7\), where \(E=7\), it is \(3>4\sin(\pi/14)\). Therefore every non-forced ambiguity coefficient is nonzero and the least one has magnitude \(m_E\), while the largest ambiguity magnitude is \(N\) by Cauchy–Schwarz and is attained at \((0,1)\). The universal rank upper bound is reached, and the condition number is \(N/m_E\), as asserted.

## Verification
The accompanying standalone Python checker enumerates characters and shifts for cyclic and noncyclic examples, confirms the forced-zero count, checks the proposed least magnitude, and compares with a dense finite angular scan. The check is empirical and finite; the proof above establishes all groups and all phases without relying on discretizing the phase circle. Its direct character-sum computation avoids assuming the two-point identity numerically.

## Relationship to prior work
Bojarovska–Flinth (2015) established the finite cyclic Gabor phase-retrieval nonvanishing criterion and Weyl lifting framework; Goldberger–Kang–Okoudjou (2021) computed its rank-one-projector Gram spectrum and explored deficient POVMs. Their general spectral identities are premises here, not new discoveries. Existing one-coordinate cyclic Gabor work studies rank discriminants, and earlier prime-cyclic impulse conditioning results allow arbitrary amplitude changes. The present sharp statement is specifically the **phase-only** optimal smallest visible singular value, its unique phases, and the all-finite-abelian exponent law; those conclusions are not asserted in the accessible prior material. The most closely matching cyclic-only research records could not be inspected in complete form, and that limits the strength of the novelty conclusion.

## Limitations
The result only optimizes within windows equal to \(1\) except at one site. It is not a global conditioning optimum over all constant-modulus windows, and its visible-subspace condition number does not represent stable recovery of traceless diagonal matrices, which remain unobservable. Orders below six have additional scalar-correlation boundary effects and are not covered. An equivalent phase-constrained optimization in older cyclic or finite quantum measurement literature may exist.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, publicly submitted March 19, 2015; J. Fourier Anal. Appl. 22 (2016), 542–567.
2. A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (2021), especially Theorems 1–2 and Section 3.
3. *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, publicly indexed research record (2026), identifiable at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rank-discriminant-for-one-coordinate-cyclic-gabor-measurem--4ad1eba7465a (record summary accessible; full text not retrievable during the comparison).
4. *Optimal complex impulse in prime-cyclic Gabor tomography: a sharp conditioning barrier*, publicly indexed research record (2026), identifiable at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-optimal-complex-impulse-in-prime-cyclic-gabor-tomography-a-sharp--c114096c73ba (record summary accessible; full text not retrievable during the comparison).
