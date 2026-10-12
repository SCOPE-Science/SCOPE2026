# Exact half-flux spectral criterion and logarithmic deficit in the magnetic preferred-orientation square lattice
## Finding
Consider the equilateral magnetic square-lattice quantum graph with preferred-orientation vertex coupling, unit edge length, and magnetic flux \(\Phi=\pi\) through each plaquette. Let
\[
\Sigma^{(k)}=\{k>0:k^2\in\sigma(H)\}
\]
be its positive momentum spectrum. For every \(k>1\), define
\[
a(k)=\frac{1}{k^2+1},\qquad c(k)=\frac{2k^2}{(k^2+1)^2},\qquad b(k)=\frac{k^2}{k^2+1}.
\]
Then
\[
k\in\Sigma^{(k)}
\quad\Longleftrightarrow\quad
\sin^2 k\in[a(k),c(k)]\cup[1/2,b(k)].
\]
This exact decomposition yields
\[
\bigl|\Sigma^{(k)}\cap[0,K]\bigr|
=\frac K2-\frac{2(2-\sqrt2)}{\pi}\log K+O(1)
\qquad(K\to\infty).
\]
Thus the known momentum-band density \(1/2\) has a definite second-order logarithmic deficit.

## Assumptions and scope
The graph, normalization, and half-flux case are exactly those of arXiv:2302.04601v1, Section 3.1: unit edge length, preferred-orientation coupling with coupling length normalized to one, and flux \(\Phi=\pi\) per plaquette. The statement concerns only the positive momentum spectrum and does not claim an analogous formula for flux denominators \(q\ge3\). The exceptional point \(k=1\), where the rational form of the published band condition has a zero denominator, is irrelevant to the large-\(K\) asymptotic and is excluded from the exact criterion above.

## Proof
The source gives the exact half-flux condition
\[
-2\le F(k)\le2,
\]
where
\[
F(k)=\frac{-4k^2+(k^2-1)^2\cos 2k-(k^2+1)^2\cos4k}{(k^2-1)^2\sin^2k}.
\]
For \(k>1\) and \(\sin k\ne0\), the denominator is positive. Writing \(s=\sin^2k\), direct trigonometric algebra gives the exact factorizations
\[
(F(k)+2)(k^2-1)^2s
=-8\bigl(1-(k^2+1)s\bigr)\bigl(k^2-(k^2+1)s\bigr),
\]
\[
(F(k)-2)(k^2-1)^2s
=-4(2s-1)\bigl((k^2+1)^2s-2k^2\bigr).
\]
Since \(k>1\),
\[
0<a(k)<c(k)<\frac12<b(k)<1.
\]
Hence \(F(k)\ge-2\) is equivalent to \(a(k)\le s\le b(k)\), while \(F(k)\le2\) is equivalent to \(s\le c(k)\) or \(s\ge1/2\). Their intersection is precisely
\[
s\in[a(k),c(k)]\cup[1/2,b(k)].
\]
At \(k=n\pi\) the source's unreduced secular equation is nonzero, and the displayed criterion also excludes these points because \(s=0<a(k)\).

For the narrow branch, put \(N=n\pi\) and \(k=N+x\). Its inner and outer boundaries solve
\[
\sin^2x=\frac1{(N+x)^2+1},
\qquad
\sin^2x=\frac{2(N+x)^2}{((N+x)^2+1)^2},
\]
respectively. Scaling \(x=y/N\) and using \(\sin x=x+O(x^3)\) shows that the inner roots have \(|y|=1+O(N^-1)\) and the outer roots have \(|y|=\sqrt2+O(N^-1)\). Therefore the two narrow components together have width
\[
\frac{2(\sqrt2-1)}N+O(N^-2)
=\frac{2(\sqrt2-1)}{n\pi}+O(n^-2).
\]

For the wide branch, the lower inequality \(s\ge1/2\) gives exactly the interval
\[
[n\pi+\pi/4,\,n\pi+3\pi/4]
\]
in each period. The additional restriction \(s\le b(k)\) removes a central gap characterized by
\[
\cos^2k<\frac1{k^2+1}.
\]
With \(M=(n+1/2)\pi\) and \(k=M+x\), the two gap edges solve
\[
\sin^2x=\frac1{(M+x)^2+1}.
\]
Again scaling \(x=y/M\) gives \(y=\pm1+O(M^-1)\), so the gap width is
\[
\frac2M+O(M^-2)
=\frac2{(n+1/2)\pi}+O(n^-2).
\]

The unperforated wide base intervals occupy exactly one half of momentum space up to an \(O(1)\) endpoint error. Summing the two narrow-band widths contributes
\[
\frac{2(\sqrt2-1)}\pi\log K+O(1),
\]
while summing the central gaps removes
\[
\frac2\pi\log K+O(1).
\]
Combining them proves
\[
\bigl|\Sigma^{(k)}\cap[0,K]\bigr|
=\frac K2+\frac{2(\sqrt2-2)}\pi\log K+O(1)
=\frac K2-\frac{2(2-\sqrt2)}\pi\log K+O(1).
\]

## Verification
The bundled `verify.py` checks the exact inequality equivalence at deterministic sample points, solves the exact branch-boundary equations by bisection, confirms the scaled narrow-band and central-gap widths, and estimates the logarithmic coefficient from differences of cumulative measures at two large cutoffs. A successful replay ends with `VERIFY_OK`. These finite checks corroborate the algebra and asymptotics; the proof above, not numerical sampling, establishes the infinite statement.

## Relationship to prior work
Baradaran, Exner, and Lipovský derive the exact half-flux band condition and show that the narrow bands have momentum width \((\sqrt2-1)/(n\pi)+O(n^{-3})\) individually, while the wide bands give limiting momentum-band density \(1/2\). They do not factor the exact band inequality into the two explicit \(\sin^2k\) branches above, quantify the central \(k^{-1}\)-scale gaps in the wide branch, or state the resulting logarithmic second-order term. Band and Berkolaiko develop the limiting momentum-band-density observable \(\lim_{K\to\infty}K^{-1}|\Sigma^{(k)}\cap[0,K]|\); that limit does not determine a sublinear logarithmic correction.

## Limitations
The result is specific to the exactly solvable half-flux case \(\Phi=\pi\). It does not establish a corresponding logarithmic law for other rational or irrational fluxes. The \(O(1)\) remainder is not evaluated explicitly. The finite checker is not an exhaustive proof and is used only as a reproducibility aid.

## References
1. M. Baradaran, P. Exner, J. Lipovský, *Magnetic square lattice with vertex coupling of a preferred orientation*, arXiv:2302.04601v1; Annals of Physics 454 (2023), 169339, DOI:10.1016/j.aop.2023.169339.
2. R. Band, G. Berkolaiko, *Universality of the Momentum Band Density of Periodic Networks*, arXiv:1304.6028v1; Physical Review Letters 111 (2013), 130404, DOI:10.1103/PhysRevLett.111.130404.
