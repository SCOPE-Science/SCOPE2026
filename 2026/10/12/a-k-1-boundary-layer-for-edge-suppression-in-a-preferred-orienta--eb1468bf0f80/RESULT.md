# A \(k^{-1}\) boundary layer for edge suppression in a preferred-orientation quantum-graph strip

## Finding
For the rectangular lattice strip of Exner--Lipovský with preferred-orientation coupling, let \(g_1(x)=a e^{-ikx}+b e^{ikx}\) be the left boundary vertical edge of length \(\ell_2\), let \(f_1(x)=c e^{-ikx}+d e^{ikx}\) be the adjacent horizontal edge of length \(\ell_1\), and let \(\theta\) be the vertical Floquet phase. Put \(\delta=k\ell_2-n\pi\in(-\pi/2,\pi/2]\). For every sequence of normalized Bloch generalized eigenfunctions with \(k\to\infty\) and \(k|\sin\delta|\to\infty\),
\[
\|g_1\|_{L^2(0,\ell_2)}=O\!\left(\frac{1}{k|\sin\delta|}\right).
\]
Thus the fixed-width exclusion used in the published edge-suppression theorem can be replaced, at the left boundary, by any shrinking exclusion whose angular detuning still satisfies \(k|\sin\delta|\to\infty\).

The complementary transition scale is \(|\delta|\asymp k^{-1}\). More precisely, suppose \(n=n(k)\) has fixed parity \(s=(-1)^n\in\{\pm1\}\), \(k\delta\to\xi\in\mathbb R\), and \(s\xi\ne2\sin\theta\). Whenever \(c\ne0\), the exact boundary matching equations imply
\[
\frac{a}{c},\frac{b}{c}\longrightarrow R_s(\theta,\xi):=\frac{s-e^{i\theta}}{i(s\xi-2\sin\theta)},\qquad \frac{d}{c}\longrightarrow1,
\]
and hence
\[
\frac{\|g_1\|_{L^2(0,\ell_2)}^2}{\|f_1\|_{L^2(0,\ell_1)}^2}
\longrightarrow
\frac{\ell_2}{\ell_1}\,
\frac{2(1-s\cos\theta)}{(s\xi-2\sin\theta)^2}.
\]
The limiting transfer law has a Floquet-dependent pole on \(s\xi=2\sin\theta\), identifying the local resonance curve inside the narrow windows left unresolved by the published theorem. No claim is made that every point of this local resonance curve belongs to the full-strip spectrum, and the singular curve itself is excluded from the ratio limit.

## Assumptions and scope
Consider the rectangular strip in Exner--Lipovský, arXiv:2001.10735, with horizontal edge length \\(\\ell_1>0\\), vertical edge length \\(\\ell_2>0\\), and preferred-orientation coupling at every vertex. Fix a vertical Floquet phase \\(\\theta\\). At the left boundary use the source notation
\[
g_1(x)=a e^{-ikx}+b e^{ikx},\qquad f_1(x)=c e^{-ikx}+d e^{ikx}.
\]
The statement concerns Bloch generalized eigenfunctions for which the restriction to one period cell is normalized. It is local to the left boundary; the full-strip dispersion relation is not replaced or solved here. The boundary-layer ratio statement assumes \\(c\\neq0\\) and excludes \\(s\\xi=2\\sin\\theta\\).

## Proof
Write \\(q=e^{ik\\ell_2}\\) and \\(z=e^{i\\theta}\\). For a degree-three preferred-orientation vertex, the exact scattering matrix from the source can be written
\[
S(k)=\frac1{k^2+3}
\begin{pmatrix}
k^2-1&2(k+1)&2(1-k)\\
2(1-k)&k^2-1&2(k+1)\\
2(k+1)&2(1-k)&k^2-1
\end{pmatrix}.
\]
The source boundary equation is
\[
S(k)\begin{pmatrix}a\\bqz^{-1}\\c\end{pmatrix}
=\begin{pmatrix}b\\aq^{-1}z^{-1}\\d\end{pmatrix}.
\]
Solving its first two rows for \\(a/c\\) and \\(b/c\\) gives the exact formulas
\[
\frac ac=\frac{2q(k+1)(q-z)z}{D},\qquad
\frac bc=-\frac{2(k-1)(qz-1)z}{D},
\]
where
\[
D=k^2z(q^2-1)+2kq(1-z^2)-q^2z+2qz^2+2q-3z.
\]
Because \\(|q|=|z|=1\\),
\[
|D|\ge 2k^2|\sin(k\ell_2)|-4k-8
=2k^2|\sin\delta|-4k-8.
\]
If \\(k|\\sin\\delta|\\to\\infty\\), the two numerators are \\(O(k)\\), hence
\[
|a|+|b|=O\!\left(\frac{|c|}{k|\sin\delta|}\right).
\]
The third row has diagonal entry \\((k^2-1)/(k^2+3)\\) and off-diagonal entries \\(O(k^{-1})\\), so \\(d/c=1+o(1)\\) whenever \\(c\\neq0\\); if \\(c=0\\), the same nonvanishing denominator forces \\(a=b=0\\), making the boundary estimate trivial. For \\(c\\neq0\\),
\[
\|f_1\|_2^2=\ell_1(|c|^2+|d|^2)+O(k^{-1}|cd|),
\]
so normalization of the period cell yields a uniform bound on \\(|c|\\). Therefore
\[
\|g_1\|_2\le \sqrt{\ell_2}(|a|+|b|)
=O\!\left(\frac1{k|\sin\delta|}\right).
\]

For the boundary layer let \\(k\delta\to\xi\\), \\(q=s e^{i\delta}\\), and keep the parity \\(s=(-1)^n\\) fixed. Dividing the exact denominator by \\(k\\) gives
\[
\frac Dk\longrightarrow 2i s z\,(s\xi-2\sin\theta).
\]
The two numerators divided by \\(k\\) have the corresponding limits that give
\[
\frac ac,\frac bc\longrightarrow
\frac{s-z}{i(s\xi-2\sin\theta)}=R_s(\theta,\xi).
\]
The third row again gives \\(d/c\to1\\). Finally, the oscillatory cross terms in both edge norms are \\(O(k^{-1})\\), so
\[
\frac{\|g_1\|_2^2}{|c|^2}\to2\ell_2|R_s|^2,
\qquad
\frac{\|f_1\|_2^2}{|c|^2}\to2\ell_1.
\]
Since \\(|s-e^{i\theta}|^2=2(1-s\cos\theta)\\), the displayed norm-ratio formula follows.

## Verification
The accompanying `verify.py` evaluates the exact scattering matrix and solved amplitude ratios, checks the two exact boundary equations for deterministic test points, and checks convergence to the boundary-layer formula for both parities. These finite computations corroborate the algebra only; the asymptotic estimate and limit are proved above from exact formulas.

## Relationship to prior work
Exner--Lipovský prove \\(O(k^{-1})\\) suppression at the boundary after excluding a fixed-width neighborhood of every \\(n\pi/\ell_2\\). Their proof reduces the boundary equations to \\(b\sin(k\ell_2)=O(k^{-1})b+O(k^{-1})c\\), but it does not resolve a shrinking detuning, identify the \\(k^{-1}\\) transition scale, or compute a Floquet-dependent limiting transfer profile. The same fixed-width theorem is restated in Lipovský's 2022 habilitation thesis without such a refinement.

Exner--Tater derive the underlying preferred-orientation scattering matrix and its odd-degree high-energy limit. That fixed-vertex statement supplies the local matrix used here but does not include a periodic strip, the near-resonant vertical propagation factor, or the joint limit \\(k(k\ell_2-n\pi)\\to\xi\\).

## Limitations
The boundary-layer formula is conditional on a full-strip Bloch generalized eigenfunction and describes its local left-boundary matching. It does not prove that every \\((\theta,\xi)\\) on or near the pole curve is realized by the full-strip dispersion relation. The singular curve \\(s\xi=2\sin\theta\\) is excluded; a finer scaling would be needed there. No statement is made about eigenvalues at exact commensurate edge energies, about the right-boundary profile, or about the brick lattice.

## References
1. P. Exner and J. Lipovský, *Topological bulk-edge effects in quantum graph transport*, arXiv:2001.10735v1; Phys. Lett. A 384 (2020), 126390.
2. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664v1; Phys. Lett. A 382 (2018), 283--287.
3. J. Lipovský, *Spectral Theory Problems on Graphs and Their Applications*, habilitation thesis, Czech Technical University in Prague (2022), Section 2.8.2.
