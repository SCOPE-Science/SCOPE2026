# Complete positive point-spectrum classification for a phase-twisted preferred-orientation square lattice
## Finding
Consider the periodic square metric graph with common edge length \(\ell>0\). At every degree-four vertex impose the phase-twisted preferred-orientation condition determined by \(U=e^{i\mu}R\), where \(R\) is the cyclic shift matrix, the coupling-length scale is normalized to one, and \(0<\mu<\pi/2\). Then
\[
\sigma_{\mathrm p}(H)\cap(0,\infty)=
\begin{cases}
\{1\},&\sin(2(\mu+\ell))=0,\\
\varnothing,&\sin(2(\mu+\ell))\neq0.
\end{cases}
\]
Thus a positive flat Bloch band exists exactly at momentum \(k=1\) and only on the parameter locus \(\mu+\ell\in(\pi/2)\mathbb Z\). When it exists, the eigenvalue \(E=1\) has infinite multiplicity. In particular, the candidate momenta \(k=n\pi/\ell\) do not produce positive flat bands for \(0<\mu<\pi/2\).

## Assumptions and scope
The graph, normalization, and coupling are those of Exner and Tater, arXiv:2108.04708, Eqs. (15)--(21): the lattice edge length is \(\ell\), while the length scale in the vertex condition is set equal to one. The statement concerns only positive energies \(E=k^2>0\) and interior phase \(0<\mu<\pi/2\). The endpoint couplings \(\mu=0\) and \(\mu=\pi/2\) are excluded because their spectral structure is qualitatively different.

## Proof
Let \(Q=\cos\theta_1+\cos\theta_2\in[-2,2]\). The published Floquet determinant is a nonzero prefactor times \(F(k,Q)=\sum_{j=0}^4 c_jk^j\), where
\[
\begin{aligned}
c_0=c_4&=-\sin(2\mu)\sin^2(k\ell),\\
c_2&=\sin(2\mu)\bigl(1+3\cos(2k\ell)\bigr),\\
c_1&=2\bigl(2\cos(2\mu)\cos(k\ell)-Q\bigr)\sin(k\ell),\\
c_3&=2\bigl(2\cos(2\mu)\cos(k\ell)+Q\bigr)\sin(k\ell).
\end{aligned}
\]
Collecting the quasimomentum-dependent terms gives the exact affine decomposition
\[
F(k,Q)=A(k)+2k(k^2-1)\sin(k\ell)Q,
\]
with \(A(k)=F(k,0)\).

For a fixed \(k>0\), an eigenvalue of the full periodic operator requires the fiber determinant to vanish on a set of quasimomenta of positive two-dimensional measure. If the coefficient of \(Q\) is nonzero, the equation fixes one level set of \(Q\), which has measure zero. Hence a positive point-spectrum energy must satisfy
\[
k(k^2-1)\sin(k\ell)=0.
\]
Since \(k>0\), the only possibilities are \(k=1\) or \(\sin(k\ell)=0\).

If \(\sin(k\ell)=0\), then \(\cos(2k\ell)=1\), and the constant part is
\[
F(k,Q)=4k^2\sin(2\mu)\neq0
\]
because \(0<\mu<\pi/2\). Therefore no such momentum is spectral for every quasimomentum.

At \(k=1\), direct substitution and the addition formula give
\[
F(1,Q)=4\sin(2\mu)\cos(2\ell)+4\cos(2\mu)\sin(2\ell)
=4\sin(2(\mu+\ell)),
\]
independently of \(Q\). Thus \(k=1\) is a flat band exactly when \(\sin(2(\mu+\ell))=0\). In that case every Floquet fiber has the eigenvalue \(1\); the direct integral therefore contains an infinite-dimensional eigenspace at \(E=1\). Conversely, if this sine is nonzero, no positive momentum can satisfy the positive-measure fiber condition, so the positive point spectrum is empty.

## Verification
The accompanying `verify.py` reconstructs the published polynomial \(F(k,Q)\), checks its affine decomposition in \(Q\) on a deterministic grid, verifies the identity \(F(1,Q)=4\sin(2(\mu+\ell))\), and verifies the nonvanishing value \(4k^2\sin(2\mu)\) at \(k\ell=n\pi\). Its successful output is `VERIFY_OK`. The script is a consistency check; the infinite statement is proved analytically above.

## Relationship to prior work
Exner and Tater derive the exact square-lattice Floquet determinant for \(U=e^{i\mu}R\) and observe that for interior phase the infinite family of flat bands present at \(\mu=0\) disappears. They then exhibit \(k=1\) as a flat band under a parameter relation equivalent, away from singular cotangent presentations, to \(\sin(2(\mu+\ell))=0\). The source does not state that this is the only possible positive flat band or classify the whole positive point spectrum.

The endpoint paper arXiv:1710.02664 shows that the unphased preferred-orientation square lattice has infinitely many degenerate loop-supported eigenvalues, so the interior-phase classification is not inherited from that model. The magnetic follow-up arXiv:2302.04601 checks possible flat-band factors in a different magnetic square-lattice problem; its spectral determinant and parameter family are different and do not imply the classification above.

## Limitations
The result does not address negative point spectrum, the endpoint phases \(\mu=0\) or \(\mu=\pi/2\), magnetic flux, or perturbations of edge lengths. It classifies positive point spectrum only for the equilateral nonmagnetic square lattice with the phase-twisted coupling and normalization stated above.

## References
1. P. Exner and M. Tater, *Quantum graphs: self-adjoint, and yet exhibiting a nontrivial PT-symmetry*, arXiv:2108.04708; Physics Letters A 416 (2021), 127669.
2. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664; Physics Letters A 382 (2018), 283--287.
3. M. Baradaran, P. Exner, and J. Lipovský, *Magnetic square lattice with vertex coupling of a preferred orientation*, arXiv:2302.04601; Annals of Physics 454 (2023), 169339.
