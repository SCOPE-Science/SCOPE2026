# Exact determinant tightness of the subgroup-plus-one-point family
## Finding
Let
\[
G_m=\mathbb Z_m^2,\qquad
H_m=\mathbb Z_m\times\{0\},\qquad
E_m=H_m\cup\{(0,1)\},
\]
with \(m\ge2\). Write the characters of \(G_m\) as
\[
\chi_{a,b}(x,y)=\exp\!\left(\frac{2\pi i}{m}(ax+by)\right).
\]

For every exponential basis partner \(B\) of \(E_m\), exactly one character-restriction class on \(H_m\) is represented twice and every other class is represented once. If the repeated characters are \(\chi_{s,b_1}\) and \(\chi_{s,b_2}\), put
\[
k\equiv b_2-b_1\pmod m,\qquad 1\le k\le m-1.
\]
Then the absolute determinant of the corresponding Fourier matrix is
\[
D_{E_m}(B)
=
m^{m/2}\left|1-e^{2\pi i k/m}\right|
=
2m^{m/2}\sin\!\left(\frac{\pi\min(k,m-k)}{m}\right).
\]

Therefore the set-level determinant tightness is
\[
D(E_m)=
\begin{cases}
2m^{m/2},&m\ \text{even},\\[4pt]
2m^{m/2}\cos\!\left(\dfrac{\pi}{2m}\right),&m\ \text{odd}.
\end{cases}
\]
Since \(|E_m|=m+1\), the normalized determinant tightness is
\[
\widetilde D(E_m)
=
\frac{\sqrt{m+1}}{D(E_m)^{1/(m+1)}}
\longrightarrow1.
\]

Ferguson--Mayeli--Sothanaphan proved for the same family that
\[
\rho(E_m)\ge\frac{m+1}{2},
\]
so \(\rho(E_m)\to\infty\). Thus normalized determinant tightness can converge to its spectral optimum while the Riesz ratio simultaneously diverges.

## Assumptions and scope
The determinant quantity \(D(E)\) and its normalization \(\widetilde D(E)\) are those of Ferguson--Mayeli--Sothanaphan. The group is exactly \(G_m=\mathbb Z_m^2\), and the set is exactly the subgroup-plus-one-point family \(E_m\). No statement is made here about arbitrary one-point perturbations of general subgroups, or about the exact value of \(\rho(E_m)\).

## Proof
Let \(B\) be an exponential basis partner of \(E_m\). Two characters \(\chi_{a,b}\) and \(\chi_{a',b'}\) have the same restriction to \(H_m\) exactly when \(a=a'\).

There are \(m\) restriction classes and \(m+1\) columns in the Fourier matrix \(T(E_m,B)\), so at least one class is repeated. If some restriction class were absent, then the \(m+1\) columns would occupy at most \(m-1\) classes. After choosing one representative from each occupied class and subtracting it from every other column in that class, at least two transformed columns would vanish on all \(m\) rows belonging to \(H_m\). Such columns can be nonzero only on the single row corresponding to \((0,1)\), so they are linearly dependent. That would make \(T(E_m,B)\) singular. Hence every restriction class occurs, and exactly one occurs twice.

Reorder columns so that the repeated characters are the last two, \(\chi_{s,b_1}\) and \(\chi_{s,b_2}\). Subtract the first repeated column from the second. The new column is zero on every row in \(H_m\), while at \((0,1)\) its entry is
\[
e^{2\pi i b_2/m}-e^{2\pi i b_1/m}.
\]
Expanding the determinant along this column leaves the \(m\times m\) Fourier matrix of \(\mathbb Z_m\), up to row and column permutations and unit-modulus column factors. Its absolute determinant is \(m^{m/2}\), since after division by \(\sqrt m\) it is unitary. Therefore
\[
D_{E_m}(B)
=
m^{m/2}\left|e^{2\pi i b_2/m}-e^{2\pi i b_1/m}\right|
=
m^{m/2}\left|1-e^{2\pi i k/m}\right|.
\]
The identity
\[
\left|1-e^{2\pi i k/m}\right|
=
2\sin\!\left(\frac{\pi\min(k,m-k)}{m}\right)
\]
gives the determinant spectrum.

Every \(k\in\{1,\dots,m-1\}\) occurs: take one character from each first-coordinate class and use \(\chi_{0,0}\) together with \(\chi_{0,k}\) in the repeated class. Hence maximizing over basis partners gives a factor \(2\) when \(m\) is even, because \(-1\) is an \(m\)-th root of unity, and a factor \(2\cos(\pi/(2m))\) when \(m\) is odd, because the two closest \(m\)-th roots to \(-1\) have arguments \(\pi\pm\pi/m\).

Finally, write
\[
s_m=
\begin{cases}
1,&m\ \text{even},\\
\cos(\pi/(2m)),&m\ \text{odd}.
\end{cases}
\]
Then
\[
\log\widetilde D(E_m)
=
\frac{\frac12(m+1)\log(m+1)-\frac12m\log m-\log(2s_m)}{m+1}.
\]
The numerator is \(O(\log m)\), so this tends to \(0\), proving \(\widetilde D(E_m)\to1\).

## Verification
The accompanying `verify.py` constructs canonical basis partners for every \(2\le m\le24\) and every nonzero second-coordinate difference \(k\), computes the complex determinant directly by Gaussian elimination, and checks it against
\[
m^{m/2}\left|1-e^{2\pi i k/m}\right|.
\]
It also checks the parity-dependent maximizing formula and the decay of \(\log\widetilde D(E_m)\). The script prints `VERIFY_OK`.

These finite computations are consistency checks only. The determinant formula and the asymptotic statement are proved analytically above.

## Relationship to prior work
Ferguson--Mayeli--Sothanaphan introduced the determinant tightness quantity and its normalization, and their Example 4.19 studies exactly the family \(E_m\). For that family they prove the restriction-class structure needed for invertibility and derive the lower bound
\[
\rho(E_m)\ge\frac{m+1}{2},
\]
showing that the Riesz ratio diverges. Their example does not compute \(D(E_m)\), does not give the determinant spectrum of all basis partners, and does not identify the asymptotic separation
\[
\widetilde D(E_m)\to1
\quad\text{while}\quad
\rho(E_m)\to\infty.
\]

Targeted searches for the exact determinant formula, the subgroup-plus-one-point family, and the normalized-determinant/Riesz-ratio separation found no covering statement.

## Limitations
The result is specific to the subgroup-plus-one-point family in \(\mathbb Z_m^2\). It does not determine the exact Riesz ratio, lower Riesz constant, or upper Riesz constant of this family. The literature search cannot rule out an unindexed or differently phrased equivalent result.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, "Riesz bases of exponentials and multi-tiling in finite abelian groups," arXiv:1904.04487, first posted 9 April 2019.
