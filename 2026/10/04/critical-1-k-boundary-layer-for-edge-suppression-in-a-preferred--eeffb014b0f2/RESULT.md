# Critical \(1/k\) boundary layer for edge suppression in a preferred-orientation rectangular strip
## Finding
Consider the rectangular strip with preferred-orientation coupling introduced by Exner and Lipovský. On the left boundary let
\[
g_1(x)=a e^{-ikx}+b e^{ikx},\qquad f_1(x)=c e^{-ikx}+d e^{ikx},
\]
where \(g_1\) lies on the boundary vertical edge of length \(\ell_2\), \(f_1\) lies on the adjacent horizontal edge of length \(\ell_1\), and \(\theta\) is the vertical Bloch phase. Write
\[
k\ell_2=n\pi+\delta,\qquad \varepsilon=(-1)^n.
\]
There is a sharp shrinking-resonance crossover at phase width \(1/k\).

If \(\delta\to0\) while \(k|\delta|\to\infty\), then
\[
\frac ac,\frac bc=O\!\left(\frac1{k|\delta|}\right),\qquad \frac dc\to1.
\]
For generalized eigenfunctions normalized on one period cell this implies
\[
\|g_1\|_{L^2(0,\ell_2)}=O\!\left(\frac1{k|\delta|}\right)\to0.
\]

In contrast, fix a parity \(\varepsilon\in\{-1,1\}\), a Bloch phase \(\theta\), and \(\xi\in\mathbb R\), and suppose along a sequence of spectral pairs that
\[
k\ell_2=n\pi+\frac{\xi}k+o(k^{-1}),\qquad \varepsilon\xi\ne2\sin\theta.
\]
Then every nonzero local solution satisfies \(c\ne0\) for all sufficiently large \(k\), and
\[
\frac ac,\frac bc\longrightarrow
A_{\varepsilon,\theta,\xi}
:=\frac{\varepsilon-e^{i\theta}}{i(\varepsilon\xi-2\sin\theta)},
\qquad
\frac dc\longrightarrow1.
\]
Consequently
\[
\frac{\|g_1\|_{L^2(0,\ell_2)}^2}{\|f_1\|_{L^2(0,\ell_1)}^2}
\longrightarrow
\frac{2\ell_2}{\ell_1}
\frac{1-\varepsilon\cos\theta}{(\varepsilon\xi-2\sin\theta)^2}.
\]
Thus windows wider than \(1/k\) still exhibit boundary suppression, whereas the critical \(1/k\) window can carry order-one boundary mass with an explicit phase-dependent profile.

## Assumptions and scope
The claim concerns the left boundary vertex of the rectangular strip in Exner--Lipovský and uses their orientation conventions for \(g_1,f_1\) and the Bloch phase. It is a statement along actual spectral pairs \((k,\theta)\) admitting a global generalized eigenfunction; it does not claim that every prescribed \((\xi,\theta)\) occurs on a dispersion branch. The critical formula excludes the singular curve \(\varepsilon\xi=2\sin\theta\), where the leading denominator cancels and a finer scale is required. The right boundary has an analogous local analysis after applying the corresponding orientation convention, but it is not part of the claim.

## Proof
For the degree-three preferred-orientation vertex, the exact scattering matrix in the source simplifies to
\[
S(k)=\frac1{k^2+3}
\begin{pmatrix}
k^2-1&2(k+1)&2(1-k)\\
2(1-k)&k^2-1&2(k+1)\\
2(k+1)&2(1-k)&k^2-1
\end{pmatrix}.
\]
Set
\[
q=e^{i(k\ell_2-\theta)},\qquad r=e^{-i(k\ell_2+\theta)}.
\]
The exact boundary relation displayed in the source is
\[
S(k)\begin{pmatrix}a\\bq\\c\end{pmatrix}
=\begin{pmatrix}b\\ar\\d\end{pmatrix}.
\]
Solving its first two equations gives, with
\[
D=k^2(q-r)+2k(qr-1)+(2qr-q-3r+2),
\]
the identities
\[
\frac ac=\frac{2(k+1)(q-1)}D,
\qquad
\frac bc=\frac{2(k-1)(r-1)}D.
\]
The third equation then gives \(d/c\) from these two ratios.

For the mesoscopic regime, \(q-r=2i\varepsilon e^{-i\theta}\sin\delta\). Since \(\delta\to0\) and \(k|\delta|\to\infty\),
\[
D=2i\varepsilon e^{-i\theta}k^2\delta\,(1+o(1)),
\]
while both numerators are \(O(k)\). Hence \(a/c,b/c=O((k|\delta|)^{-1})\). The third scattering equation and \(S(k)=I+O(k^{-1})\) give \(d/c\to1\). The same normalization estimate used in the source then bounds \(|c|\), which proves the stated decay of \(\|g_1\|\).

For the critical regime, put \(\delta=\xi/k+o(k^{-1})\). Because \(qr=e^{-2i\theta}\),
\[
D=2ik e^{-i\theta}(\varepsilon\xi-2\sin\theta)+o(k).
\]
Moreover \(q,r\to\varepsilon e^{-i\theta}\). Division in the exact formulas gives
\[
\frac ac,\frac bc\to
\frac{\varepsilon-e^{i\theta}}{i(\varepsilon\xi-2\sin\theta)}.
\]
Again the third scattering equation gives \(d/c\to1\). Finally, for fixed edge length \(L\),
\[
\int_0^L|A e^{-ikx}+B e^{ikx}|^2\,dx
=L(|A|^2+|B|^2)+O(k^{-1}|A||B|).
\]
Applying this to \(g_1\) and \(f_1\), and using
\[
|A_{\varepsilon,\theta,\xi}|^2
=\frac{2(1-\varepsilon\cos\theta)}{(\varepsilon\xi-2\sin\theta)^2},
\]
yields the mass-ratio limit.

## Verification
The accompanying `verify.py` reconstructs the exact matrix coefficients and the solved amplitude formulas, evaluates the exact scattering residual, and tests two critical sequences of opposite parity. It also tests a shrinking mesoscopic sequence with \(\delta\asymp k^{-1/2}\). The script returns `VERIFY_OK`. These computations are finite checks of the algebra and asymptotic numerics; the all-sequence statements above follow from the analytic expansions in the proof.

## Relationship to prior work
Exner and Lipovský prove that for a fixed \(K>0\), after excluding fixed phase neighborhoods \(|k\ell_2-n\pi|<K\), the normalized boundary component is \(O(k^{-1})\). Their proof explicitly stops at the estimate involving \(\sin(k\ell_2)\), and their discussion describes the excluded regions only as particular narrow intervals. The present statement instead lets the excluded phase width shrink with \(k\), proves suppression whenever \(k|\delta|\to\infty\), and resolves the nontrivial \(\delta\sim1/k\) boundary layer with an explicit Bloch-phase-dependent transfer law.

The earlier Exner--Tater paper supplies the preferred-orientation coupling and its vertex scattering formalism, including the odd-degree high-energy decoupling mechanism, but it does not study a strip boundary or this joint resonance/high-energy limit. Searches using the aliases preferred-orientation coupling, rectangular strip, boundary suppression, narrow intervals, resonance window, boundary layer, and high-energy transport did not locate an equivalent scaling law.

## Limitations
The singular curve \(\varepsilon\xi=2\sin\theta\) is deliberately excluded because the leading denominator vanishes. No next-order law is asserted there. The result is local to the left boundary relation and conditional on the existence of global Bloch eigenfunctions at the chosen spectral pairs. It does not classify which \((\xi,\theta)\) are realized by the full strip dispersion relation. The explicit limit is an analytic consequence of the published exact scattering equations, so there remains a residual literature risk that an equivalent double-scaling consequence has appeared under different terminology.

## References
1. P. Exner and J. Lipovský, *Topological bulk-edge effects in quantum graph transport*, Physics Letters A 384 (2020), 126390; arXiv:2001.10735v1.
2. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, Physics Letters A 382 (2018), 283--287; arXiv:1710.02664v1.
