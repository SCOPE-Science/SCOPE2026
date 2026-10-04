# Exact non-Dirichlet spectrum and triple multiplicity for the preferred-orientation cube

## Finding
For the unit-edge cube quantum graph with the Exner–Tater preferred-orientation coupling, every positive spectral wave number \(k>1\) with \(\sin k\neq0\) is characterized exactly by
\[
\cos k=\pm\frac{{k^2-1}}{{k^2+3}}.
\]
Conversely, every \(k>1\) satisfying either scalar equation is spectral. Each such eigenvalue \(k^2\) has multiplicity exactly three. A root with \(\cos k>0\) occurs in rotation sectors \(j=1,2,3\), while a root with \(\cos k<0\) occurs in sectors \(j=0,1,3\).

If \(N_n=n\pi\), the two high-energy branches adjacent to \(N_n\) obey
\[
k_{{n,\pm}}=N_n\pm\frac{{2\sqrt{{2}}}}{{N_n}}+O(N_n^{{-3}}),
\]
so
\[
k_{{n,\pm}}^2=N_n^2\pm4\sqrt{{2}}+O(N_n^{{-2}}).
\]
Thus the published cube localization envelope with coefficient \(2\sqrt{{3}}\) can be sharpened to an exact scalar spectral law, exact triple degeneracy, and sharp leading energy offsets.

## Assumptions and scope
The graph is the equilateral cube with every edge of length one. At every degree-three vertex the preferred-orientation coupling is defined by the cyclic permutation matrix used by Exner and Lipovský. The source decomposes the Hamiltonian into the four eigenspaces of the quarter-turn rotation, with \(\omega_j=e^{{i\pi j/2}}\), \(j=0,1,2,3\). The claim concerns positive wave numbers \(k>1\) outside the exact Dirichlet family \(\sin k=0\). It does not change or reclassify the multiplicities of those Dirichlet levels.

## Proof
Let \(c=\cos k\). The source gives, in rotation sector \(j\), the preferred-orientation secular equation
\[
k^6\omega_j^2\sin^3 k+k^4\sin k\,A_j(c)+k^2\sin k\,B_j(c)=0,
\]
where
\[
A_j(c)=\omega_j^4+2\omega_j^3c-6\omega_j^2c^2+2\omega_jc+1
\]
and
\[
B_j(c)=-\omega_j^4+6\omega_j^3c-9\omega_j^2c^2-\omega_j^2+6\omega_jc-1.
\]
For \(k>0\) and \(\sin k\neq0\), divide by \(k^2\omega_j^2\sin k\). Writing \(q=k^2+3\), direct algebra gives the following exact factorizations:
\[
Q_0=-(c-1)q\bigl(qc+k^2-1\bigr),
\]
\[
Q_1=Q_3=-\bigl(qc-(k^2-1)\bigr)\bigl(qc+(k^2-1)\bigr),
\]
and
\[
Q_2=-(c+1)q\bigl(qc-(k^2-1)\bigr).
\]
Because \(\sin k\neq0\), the factors \(c-1\) and \(c+1\) cannot vanish. Hence sector \(j=0\) contributes exactly \(c=-(k^2-1)/q\), sectors \(j=1,3\) contribute both signs, and sector \(j=2\) contributes exactly \(c=(k^2-1)/q\). For \(k>1\), the ratio \(r(k)=(k^2-1)/(k^2+3)\) lies strictly between zero and one. Therefore every non-Dirichlet root occurs in exactly three rotation sectors, with the sector pattern stated above.

It remains to rule out an internal multiplicity in any one sector. For either sign set \(F_\sigma(k)=\cos k-\sigma r(k)\), where \(\sigma\in\{-1,1\}\). At a root,
\[
\sin^2 k=1-r(k)^2=\frac{{8(k^2+1)}}{{(k^2+3)^2}},
\]
while
\[
r'(k)=\frac{{8k}}{{(k^2+3)^2}}.
\]
Moreover
\[
\sin^2 k-r'(k)^2=\frac{{8(k^6+7k^4+7k^2+9)}}{{(k^2+3)^4}}>0.
\]
Thus \(|\sin k|>|r'(k)|\), so \(F_\sigma'(k)\neq0\). Every scalar root is simple. Since the four rotation components form an orthogonal direct sum and the relevant component secular zero is simple, each such \(k^2\) has multiplicity exactly three.

For the asymptotics, set \(N_n=n\pi\) and \(k=N_n+\delta\). The sign in the scalar equation near \(N_n\) is \(\sigma=(-1)^n\). Since
\[
\frac{{k^2-1}}{{k^2+3}}=1-\frac{{4}}{{k^2+3}}
\]
and
\[
(-1)^n\cos(N_n+\delta)=1-\frac{{\delta^2}}2+O(\delta^4),
\]
one obtains \(\delta^2=8N_n^{-2}+O(N_n^{-4})\). Both signs are realized on the two sides of \(N_n\), yielding the stated wave-number and energy expansions.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to expand the four sector polynomials at a grid of rational values and compare them to the displayed factorizations. It also checks the identity
\[
1-\left(\frac{{k^2-1}}{{k^2+3}}\right)^2=\frac{{8(k^2+1)}}{{(k^2+3)^2}}
\]
and numerically brackets representative roots on both sides of several large multiples of \(\pi\). These finite checks corroborate the algebra and asymptotics; the proof above is analytic and does not infer the infinite statement from computation.

## Relationship to prior work
Exner and Lipovský derive the four-sector cube secular determinant and prove only that all large preferred-orientation cube wave numbers lie in intervals of radius \(2\sqrt{{3}}/k+O(k^{-2})\) about \(n\pi\). Their paper does not state the sector factorization above, the unified scalar equations, or the exact triple multiplicity of the non-Dirichlet roots. Targeted searches for the exact cosine law, its equivalent sine-square law, cube multiplicity, and sharper high-energy coefficient did not identify a published statement with the same implication. A later review of preferred-orientation quantum graphs summarizes the Platonic-solid asymptotic picture but likewise reports the asymptotic localization rather than this exact cube reduction.

## Limitations
The claim excludes \(k=1\) and the Dirichlet family \(\sin k=0\); no new assertion is made about their multiplicities. The originality search cannot exclude an unindexed equivalent derivation using different secular variables. The result concerns the equilateral unit-edge cube with the stated preferred-orientation coupling and does not claim an analogous exact law for unequal edge lengths.

## References
1. P. Exner and J. Lipovský, “Spectral asymptotics of the Laplacian on Platonic solids graphs,” arXiv:1906.09091v1, first public 2019-06-21; Journal of Mathematical Physics 60 (2019), 122101, DOI 10.1063/1.5116100.
2. J. Lipovský, “Graphs with preferred-orientation coupling and their spectral properties,” QGRAPH 2020 conference abstract, summarizing the Platonic-solid high-energy results.
