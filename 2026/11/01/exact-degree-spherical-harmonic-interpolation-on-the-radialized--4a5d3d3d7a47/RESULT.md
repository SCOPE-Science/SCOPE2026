# Exact-degree spherical-harmonic interpolation on the radialized rhombic triacontahedron

## Finding
Let \(X\subset S^2\) be the radial projection of the thirty-two vertices of a regular rhombic triacontahedron; equivalently, it is the union of the twelve directions to the vertices of a regular icosahedron and the twenty directions to the vertices of its polar regular dodecahedron, in their **common dual orientation**. Let \(E_\ell\) evaluate the real spherical harmonics of **exact degree** \(\ell\) on \(X\). The exact rank \(r_\ell=\operatorname{rank}E_\ell\), for every integer \(\ell\ge0\), is:

| \(\ell\) | \(r_\ell\) |
|---|---|
| 0 through 16, in order | 1, 3, 5, 7, 9, 6, 10, 10, 14, 10, 15, 13, 15, 13, 14, 13, 15 |
| 17 through 44, excluding \(\{18,20,22,24,26,28,32,34,38,44\}\) | 16 |
| \(\{18,20,22,24,26,28,32,34,38,44\}\) | 15 |
| \(\ell\ge45\) | 16 |

There are sixteen antipodal pairs, so the maximal rank of a **single** harmonic degree is sixteen, not thirty-two. Thus the first degree interpolating every sample vector with the required antipodal parity is \(\ell=17\), but full parity-compatible interpolation is not permanent until \(\ell=45\). In particular degree 44 still has a one-dimensional obstruction. These claims concern individual exact degrees, not sums of harmonic degrees.

## Assumptions and scope
Put \(\varphi=(1+\sqrt5)/2\) and define twelve unnormalized icosahedral vertices
\[
I_0=\{(0,\varepsilon,\delta\varphi),\;(\varepsilon,\delta\varphi,0),\;(\varepsilon\varphi,0,\delta):\varepsilon,\delta\in\{-1,1\}\}.
\]
Let \(\mathcal F\) comprise all three-element subsets \(\{u,v,w\}\subset I_0\) such that each squared pairwise Euclidean distance equals four. There are exactly twenty such faces. Put \(D_0=\{u+v+w:\{u,v,w\}\in\mathcal F\}\). These are the twenty dodecahedral directions dual to \(I_0\), *not* an independently oriented dodecahedron. Each \(u\in I_0\) has squared norm \(\varphi+2\), and each \(d\in D_0\) has squared norm \(6+9\varphi\). Define
\[
X=\left\{u/\sqrt{\varphi+2}:u\in I_0\right\}\cup\left\{d/\sqrt{6+9\varphi}:d\in D_0\right\}.
\]
It consists of thirty-two distinct points arranged in sixteen antipodal pairs. All ranks are over \(\mathbb R\) (equivalently \(\mathbb C\)). The normalization is the usual unit sphere, with \(P_\ell(1)=1\) for Legendre polynomials.

## Proof
Choose one representative \(y_i\) from each antipodal pair, obtaining sixteen unit vectors. For an orthonormal basis of the degree-\(\ell\) spherical harmonics, the spherical addition theorem gives an evaluation Gram matrix that is a positive constant times
\[
G_\ell=(P_\ell(\langle y_i,y_j\rangle))_{1\le i,j\le16}.
\]
The antipodal identity \(f(-y)=(-1)^\ell f(y)\) shows that the rank of evaluation on all thirty-two nodes equals \(\operatorname{rank}G_\ell\). All these ranks are at most sixteen.

The dot products belong to the real quartic number field
\[
F=\mathbb Q(\varphi,\beta),\qquad \varphi^2=\varphi+1,\qquad \beta^2=21+33\varphi.
\]
Indeed, the within-orbit dot products have coefficients in \(\mathbb Q(\varphi)\), and cross-orbit ones equal the exact unnormalized dot product divided by \(\beta=\sqrt{(\varphi+2)(6+9\varphi)}\). The attached standalone `verify.py` computes \(G_\ell\) by the exact Legendre recurrence
\[
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t)
\]
and performs full Gaussian elimination in \(F\), with rational coefficients, for every \(0\le\ell\le44\). This proves precisely the listed low-degree ranks, including every deficit and full-rank degree in that finite interval; the complete forty-five-entry rank sequence is in the code, and is independently reproducible from the geometric definitions above.

For each \(45\le\ell\le249\), invertibility is proved by exact modular reduction, not floating-point eigenvalues. The field relations admit the embeddings \((\varphi,\beta)=(78,99)\) modulo the prime 1201 and \((745,287)\) modulo the prime 1229. The matrix \(G_\ell\) has nonzero determinant modulo 1201 except at degrees 86 and 174, at which its determinant is nonzero modulo 1229. The accompanying `determinants.csv` records all 205 nonzero residues, and `verify.py` independently rebuilds them. A nonzero reduction proves the characteristic-zero determinant is nonzero; no conclusion is drawn from the two vanishing residues modulo 1201.

For higher degrees a real analytic estimate completes the proof. Exact rational interval bounds for the two radicals show
\[
|\langle y_i,y_j\rangle|<4/5\quad(i\ne j).
\]
The classical Bernstein inequality for Legendre polynomials, together with \(\pi>3\), therefore implies
\[
|P_\ell(\langle y_i,y_j\rangle)|
<\sqrt{\frac{10}{9(\ell+1/2)}}\quad(i\ne j).
\]
Each diagonal entry of \(G_\ell\) is one and there are fifteen off-diagonal entries per row. Their absolute row sum is less than
\[
\sqrt{\frac{250}{\ell+1/2}}<1\qquad(\ell\ge250).
\]
By strict diagonal dominance and symmetry, \(G_\ell\) is positive definite for every \(\ell\ge250\). Together with exact field ranks through 44 and modular certificates through 249, this covers **every** nonnegative degree.

## Verification
Run `python3 verify.py` in a directory containing that file; `python3 verify.py --write-certificate` additionally reconstructs `determinants.csv`. The script uses only the Python standard library. It checks exact geometry, the low-degree ranks over \(F\), rational enclosure of every off-diagonal dot product, the two finite-field embeddings and 205 determinant witnesses, and the strict high-degree Bernstein threshold. The CSV is corroborating finite arithmetic evidence; the proof of the infinite tail uses diagonal dominance rather than extrapolation. The exact-rank computation and modular argument are reproducible, rather than externally or independently certified.

## Relationship to prior work
Bannai, Okuda and Tagami [1] established the harmonic-index-design framework and noted the degree-eight and degree-fourteen cancellation on an antipodal half of the **icosahedron alone**. Zhu, Bannai, Bannai, Kim and Yu [2] developed harmonic-index design bounds and applications of the addition formula. Both results provide relevant theory but neither supplies this complete exact-degree interpolation rank sequence for the **two-orbit**, thirty-two-direction dual configuration; in particular they do not imply the first full degree 17, the later degree-44 defect, or permanent fullness at degree 45 without an additional rank calculation. The individual icosahedral and dodecahedral orbit cancellations at some degrees are known representation-theoretic effects, not independently claimed here as novel.

## Limitations
The result is for radial projection of the dual polyhedron's vertices, not the unnormalized two-radius vertex set, and for interpolation using a **single harmonic degree**, not cumulative band-limits. It does not give optimal conditioning constants. Exact field computation verifies the finite low ranks and modular nonvanishing, but no independent mathematical audit has been performed. A prior unindexed character-theoretic calculation specialized to precisely this two-orbit restriction could reduce the originality of the rank table; the cited works did not provide one in the inspected material.

## References
[1] E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1 (first public 2013-08-23), https://arxiv.org/abs/1308.5101.

[2] Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim and W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373v1 (first public 2015-07-20), https://arxiv.org/abs/1507.05373.

[3] G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23 (1975), Section 7.3 (Bernstein bound for Legendre polynomials).
