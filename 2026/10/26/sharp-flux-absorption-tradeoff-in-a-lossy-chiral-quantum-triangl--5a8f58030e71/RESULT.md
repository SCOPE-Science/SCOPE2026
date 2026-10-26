# Sharp flux–absorption tradeoff in a lossy chiral quantum triangle

## Finding

For a unit-hopping, three-site coherent quantum ring with one irreversible point absorber and an initially occupied neighboring site, the **mean absorption time** has an exact expression over the full physical parameter range. Write the flux around the oriented triangle as \(\phi\), the positive absorber amplitude loss as \(g\), and \(s=\sin\phi\). For \(s\ne0\), the absorption time is finite and equals
\[
T(g,\phi)=\frac{3}{2g}+\frac{g}{2s^2}+\frac{1}{2s}.
\]
For \(s=0\), the initially occupied site has a nonzero overlap with a dark state and the mean time is infinite.

For a **prescribed** \(g\), every optimal flux satisfies
\[
\sin\phi_*=-\min\{2g,1\}.
\]
Thus there are two distinct minimizing fluxes modulo \(2\pi\) when \(0<g<1/2\); they merge into the unique maximally chiral flux \(\phi_*=3\pi/2\) when \(g\ge1/2\). The exact flux-optimized time is
\[
T_*(g)=\begin{cases}\dfrac{11}{8g},&0<g\le1/2,\\[3pt]
\dfrac{3}{2g}+\dfrac g2-\dfrac12,&g\ge1/2.
\end{cases}
\]
Optimizing over **both** parameters yields the sharp bound
\[
\boxed{T(g,\phi)\ge\sqrt3-\frac12,}
\]
with equality if and only if \(g=\sqrt3\) and \(\phi\equiv3\pi/2\pmod{2\pi}\).

## Assumptions and scope

The Hilbert space is \(\mathbb C^3\), with ordered site basis \(\lvert0\rangle,\lvert1\rangle,\lvert2\rangle\). Site \(0\) is the absorbing site; the normalized initial state is \(\lvert1\rangle\). In units where the hopping magnitude and \(\hbar\) are one, the Hermitian tight-binding Hamiltonian and no-jump amplitude generator are
\[
H(\phi)=\begin{pmatrix}0&1&e^{-i\phi}\\1&0&1\\e^{i\phi}&1&0\end{pmatrix},
\qquad A(g,\phi)=-iH(\phi)-g\lvert0\rangle\langle0\rvert,
\qquad g>0,\quad\phi\in\mathbb R.
\]
The no-jump survival probability is \(S(t)=\|e^{At}\lvert1\rangle\|^2\). The expected arrival time of the irreversible absorption event is \(T=\int_0^\infty S(t)\,dt\), interpreted as \(+\infty\) when survival is not integrable. The escape channel has probability flux \(2g\lvert\langle0\lvert\psi(t)\rangle\rvert^2\). For a physical hopping magnitude \(J>0\) and amplitude loss \(\gamma>0\), substitute \(g=\gamma/J\); physical time is \(T/J\).

No dephasing, pumping, on-site energy mismatch, additional detection operations or multiple absorbing sites is included.

## Proof

**1. Finiteness and dark states.** Since \(A+A^\dagger=-2g\lvert0\rangle\langle0\rvert\), every eigenvalue \(\lambda\) obeys \(\operatorname{Re}\lambda\le0\). Equality requires the corresponding eigenvector \(v\) to satisfy \(v_0=0\). The remaining two components must form an eigenvector of \(\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\), hence \(v_2=\pm v_1\). The zero component at site \(0\) then imposes \(v_1+e^{-i\phi}v_2=0\), possible exactly when \(\sin\phi=0\). Therefore for \(\sin\phi\ne0\), all eigenvalues of \(A\) have strictly negative real parts, making \(T\) finite. When \(\sin\phi=0\), an explicitly nonzero dark eigenvector \((0,1,\pm1)^\top\) persists and has nonzero overlap with the initial state, so \(T=+\infty\).

**2. Exact integrated survival.** For \(s=\sin\phi\ne0\) and \(c=\cos\phi\), define
\[
Q=\begin{pmatrix}
\frac{3}{2g}&-\frac{c}{2s}+\frac i2&\frac1{2s}\\
-\frac{c}{2s}-\frac i2&\frac{3}{2g}+\frac g{2s^2}+\frac1{2s}&-\frac{gc}{2s^2}\\
\frac1{2s}&-\frac{gc}{2s^2}&\frac{3}{2g}+\frac g{2s^2}-\frac1{2s}
\end{pmatrix}.
\]
Direct multiplication, using only \(s^2+c^2=1\), proves \(A^\dagger Q+QA=-I_3\). Since \(A\) is stable, the continuous Lyapunov equation has the unique solution \(Q=\int_0^\infty e^{A^\dagger t}e^{At}\,dt\). Consequently \(T=\langle1\lvert Q\rvert1\rangle=Q_{11}=3/(2g)+g/(2s^2)+1/(2s)\), with the stated normalization.

**3. Flux optimum and threshold.** At every \(s\in(0,1]\), replacement by \(-s\) strictly decreases \(T\). Thus minimize over \(-1\le s<0\). The flux-dependent portion has derivative \(-\bigl(2g+s\bigr)/(2s^3)\). It is strictly decreasing on \([-1,-2g)\), when this interval exists, and strictly increasing on \((-2g,0)\). Its unique optimal sine is \(s_*=-2g\) for \(0<g<1/2\) and \(s_*=-1\) for \(g\ge1/2\). The former sine has exactly two phases modulo \(2\pi\), the latter one. Substitution gives the piecewise expression for \(T_*(g)\), continuous at \(g=1/2\).

**4. Sharp joint optimum.** For \(0<g\le1/2\), \(11/(8g)\) is strictly decreasing and has minimum \(11/4\) at the endpoint. For \(g\ge1/2\), differentiation of \(3/(2g)+g/2-1/2\) yields \(-3/(2g^2)+1/2\); it vanishes only at \(g=\sqrt3\), with strictly negative derivative before and positive derivative after. Its value \(\sqrt3-1/2<11/4\) is the unique joint minimum. All equality conditions follow from the strict inequalities in Steps 3–4.

## Verification

The accompanying standalone `check.py` symbolically verifies the full Lyapunov matrix identity after reducing by \(c^2+s^2=1\), then independently solves the complex Lyapunov equation numerically for 81 combinations of positive absorber strength and nondegenerate flux. It checks the piecewise flux optimum, an independent scalar minimization, and the global bound across additional samples. Running `python check.py` produced `PASS: 11 symbolic matrix/identity checks; 139 independent numerical/optimization checks`. These samples test the derivation; the universal theorem is proven in the preceding four steps, not inferred from sampling.

## Relationship to prior work

Zimborás et al. (arXiv:1208.4049, publicly posted 2012-08-20) established chirality-controlled transport, including a triangle switch, open-system sinks and half-arrival-time improvements. Their stated objective is site occupation or half-arrival time, not the integral over survival; the exact three-site loss–flux optimization and its \(g=1/2\) transition are not the published claim. Lu et al. (arXiv:1405.6209) classify time-reversal effects and demonstrate coherent state transfer, not the absorbing survival-time extremum. Longhi (arXiv:1312.4693) investigates non-Hermitian ring spectra in a different continuum model. Finocchiaro et al. (arXiv:2507.10669) optimize detection probabilities for stroboscopic local *projective measurements*, not the continuous sink model used here. Their later work emphasizes that different monitoring protocols have different optimization objectives. These distinctions are necessary; similarity of titles or physical motivation does not by itself establish either coverage or novelty.

## Limitations

The result treats exactly a homogeneous three-site tight-binding cycle, the specified site initialization, one continuous absorber, and infinite-horizon mean absorption time. It makes no claim for unequal hopping, finite detection horizons, arbitrary initial superpositions, many-site cycles, or stroboscopic detection. The direct numerical checker is finite and cannot independently certify the infinite parameter range. Historical scientific priority remains subject to older equivalent formulations not found in the examined sources; in particular the physical model is established even though the exact objective and complete joint optimum appear distinct in the inspected literature. Independent validation has not been performed.

## References

1. Z. Zimborás, M. Faccin, Z. Kádár, J. D. Whitfield, B. P. Lanyon and J. Biamonte, *Quantum Transport Enhancement by Time-Reversal Symmetry Breaking*, arXiv:1208.4049 (initial public version 2012-08-20). https://arxiv.org/abs/1208.4049
2. D. Lu et al., *Chiral Quantum Walks*, arXiv:1405.6209 (initial public version 2014-05-23). https://arxiv.org/abs/1405.6209
3. S. Longhi, *Non-Hermitian quantum rings*, arXiv:1312.4693 (initial public version 2013-12-17). https://arxiv.org/abs/1312.4693
4. S. Finocchiaro et al., *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669 (initial public version 2025-07-14). https://arxiv.org/abs/2507.10669
