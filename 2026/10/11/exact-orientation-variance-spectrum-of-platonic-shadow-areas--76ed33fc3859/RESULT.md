# Exact orientation-variance spectrum of Platonic shadow areas
## Finding
For a regular Platonic solid \(P\subset\mathbb R^3\), let \(U\) be uniform on the unit sphere \(S^2\). Its brightness in direction \(u\) is the projected area
\[
b_P(u)=\operatorname{area}(P\mid u^\perp).
\]
Write \(S(P)\) for the total surface area. Cauchy's surface-area formula gives the mean brightness
\[
\mu_P=\mathbb E[b_P(U)]=\frac{S(P)}4.
\]
The dimensionless relative variance of shadow area is
\[
V(P)=\frac{\operatorname{Var}(b_P(U))}{\mu_P^2}.
\tag{1}
\]
The exact values for the complete Platonic family are
\[
\boxed{\begin{aligned}
V(\mathrm{cube})
 &=\frac{16}{9\pi}-\frac59,\\
V(\mathrm{tetrahedron})=V(\mathrm{octahedron})
 &=\frac{4\sqrt2+2\arcsin(1/3)}{3\pi}-\frac23,\\
V(\mathrm{dodecahedron})
 &=\frac{20\bigl(2+\arcsin(1/\sqrt5)\bigr)}{9\pi\sqrt5}-\frac79,\\
V(\mathrm{icosahedron})
 &=\frac{16\sqrt2+8+8\arcsin(1/3)+4\sqrt5\arcsin(\sqrt5/3)}{15\pi}-\frac{13}{15}.
\end{aligned}}
\tag{2}
\]
All four distinct values are positive and are ordered sharply:
\[
\boxed{V(\mathrm{cube})>V(\mathrm{tetrahedron})=V(\mathrm{octahedron})>
V(\mathrm{dodecahedron})>V(\mathrm{icosahedron}).}
\tag{3}
\]
The decimal values are, in the same order,
\[
0.010328686549,\quad0.005659842751,\quad0.005659842751,\quad
0.001569817007,\quad0.000597460473.
\]

The result has an exact sampling consequence. For independent uniform orientations \(U_1,\ldots,U_k\), set
\[
\widehat S_k=\frac4k\sum_{j=1}^k b_P(U_j).
\tag{4}
\]
Then \(\mathbb E[\widehat S_k]=S(P)\), and
\[
\sqrt{\mathbb E\left[\left(\frac{\widehat S_k}{S(P)}-1\right)^2\right]}
=\sqrt{\frac{V(P)}k}.
\tag{5}
\]
The *smallest integer* \(k\) making (5) at most \(1\%\) is exactly \(104\) for the cube, \(57\) for each of the tetrahedron and octahedron, \(16\) for the dodecahedron, and \(6\) for the icosahedron. This is an RMS, not a tail-probability or confidence-interval, guarantee.

## Assumptions and scope
All five bodies are regular Euclidean convex polyhedra, up to similarity. Rotation and scaling do not change (1). View directions are independently sampled from normalized spherical area measure, not chosen optimally or from another distribution.

For a polyhedron with facets having unit outward normals \(\nu_i\) and areas \(a_i\), Cauchy's projection formula reads
\[
b_P(u)=\frac12\sum_{i=1}^m a_i\,|u\cdot\nu_i|.
\tag{6}
\]
Every regular Platonic solid has equal facet areas. Hence the normalized brightness is
\[
Y_P(u):=\frac{b_P(u)}{\mu_P}
=\frac2m\sum_{i=1}^m |u\cdot\nu_i|,
\qquad\mathbb E Y_P(U)=1.
\tag{7}
\]
Thus only the combinatorics and angles of the facet normal configuration matter.

## Proof
**Spherical absolute-product kernel.** Let \(v,w\in S^2\) and \(t=|v\cdot w|\). Then
\[
\mathbb E[|U\cdot v|\,|U\cdot w|]
=\frac{2}{3\pi}\,F(t),
\quad F(t)=\sqrt{1-t^2}+t\arcsin t.
\tag{8}
\]
To derive it, let \(G=RU\) be a standard three-dimensional Gaussian, with \(R\) independent of the uniform direction \(U\) and \(\mathbb E R^2=3\). Rotate the plane of \(v,w\), put \(\alpha=\arccos t\), and write the planar Gaussian as \(r(\cos\theta,\sin\theta)\). Its squared radius has mean \(2\), while \(\theta\) is uniform. Directly splitting the integral at the four zeros of the cosines gives
\[
\frac1{2\pi}\int_0^{2\pi}
|\cos\theta\cos(\theta-\alpha)|\,d\theta
=\frac1\pi\bigl(\sin\alpha+(\pi/2-\alpha)\cos\alpha\bigr).
\]
Multiplying by \(\mathbb E r^2=2\) and dividing by \(\mathbb E R^2=3\) gives (8). The formula is continuous at \(t=0,1\).

Squaring (7), applying (8) to every ordered pair, and subtracting \((\mathbb EY_P)^2=1\) yields the finite exact identity
\[
V(P)=\frac8{3\pi m^2}
\sum_{i,j=1}^m F(|\nu_i\cdot\nu_j|)-1.
\tag{9}
\]

**Complete facet-normal correlation count.** For the tetrahedron, use the four sign triples \((\pm1,\pm1,\pm1)\) with sign product \(+1\). For the cube use the six signed coordinate vectors. For the octahedron use all eight sign triples. For the dodecahedron use the twelve icosahedral vertex directions obtained by cyclic permutation of \((0,\pm1,\pm\varphi)\), and for the icosahedron use the twenty dodecahedral vertex directions consisting of the eight sign triples and the twelve cyclic permutations of \((0,\pm\varphi^{-1},\pm\varphi)\), where \(\varphi=(1+\sqrt5)/2\). Normalize all listed vectors to unit length. These are precisely the outward normal directions of the five corresponding regular solids; polarity interchanges the dodecahedron and icosahedron.

Their **ordered** pair counts, grouped by absolute inner product, are:

| Solid | Faces \(m\) | \(t=1\) | \(t=0\) | \(t=1/3\) | \(t=1/\sqrt5\) | \(t=\sqrt5/3\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Tetrahedron | 4 | 4 | 0 | 12 | 0 | 0 |
| Cube | 6 | 12 | 24 | 0 | 0 | 0 |
| Octahedron | 8 | 16 | 0 | 48 | 0 | 0 |
| Dodecahedron | 12 | 24 | 0 | 0 | 120 | 0 |
| Icosahedron | 20 | 40 | 0 | 240 | 0 | 120 |

The row sums are exactly \(m^2\), so no ordered pairs are omitted. Each entry is obtained by dot products in the explicit algebraic coordinates; the complete enumeration is reconstructed in `verify.py` using exact arithmetic in \(\mathbb Q(\sqrt5)\). The known tetrahedron--octahedron brightness equivalence also follows because the octahedral normal multiset is the tetrahedral normal set together with its negatives.

The kernel values needed in (9) simplify to
\[
\begin{aligned}
F(0)&=1,\qquad F(1)=\pi/2,\\
F(1/3)&=2\sqrt2/3+\arcsin(1/3)/3,\\
F(1/\sqrt5)&=(2+\arcsin(1/\sqrt5))/\sqrt5,\\
F(\sqrt5/3)&=2/3+(\sqrt5/3)\arcsin(\sqrt5/3).
\end{aligned}
\]
Substitution of each count row in (9) proves all four expressions (2). A rational-interval certificate for \(\pi\), the square roots and inverse sines proves the strict inequalities (3), not merely their floating-point analogues.

**Sharp sampling counts.** Independence in (4) gives
\[
\operatorname{Var}(\widehat S_k)=\frac{16}{k}\operatorname{Var}(b_P(U)),
\]
which proves (5). Its square is at most \(10^{-4}\) if and only if \(k\ge10^4 V(P)\). The certified rational intervals prove separately for each of the five classes that \(k-1<10^4V(P)\le k\), where \(k\) is the integer listed after (5), so every cutoff is sharp for the specified independent-uniform sampling model.

## Verification
The standalone standard-library-only program `verify.py` enumerates each explicit normal set without a mathematical data file, normalizes dot products exactly in \(\mathbb Q(\sqrt5)\), and independently matches every ordered pair-count row. It uses rigorous rational intervals for \(\sqrt2\), \(\sqrt5\), \(\pi\) (Machin's arctangent identity), and the needed inverse sines (positive-term Taylor series with a certified remainder). It proves the four-way strict order and the five sharp integer \(1\%\) cutoffs by rational inequalities.

A separate fixed-seed \(60{,}000\)-orientation Gaussian-direction simulation agrees numerically. Sampling cannot prove the exact formulas or strict inequalities; those rest on (6)--(9), the complete algebraic normal enumeration, and the rational interval tests.

## Relationship to prior work
Moran's 1944 work motivates estimation of surface area from observations of small convex objects. Cauchy's classical mean projection formula, made explicit in the modern open paper by Tsukerman and Veomett, gives the exact **first** moment of brightness. Horváth's open full survey gives (6), explains projection bodies, and explicitly identifies the regular octahedron as the Blaschke body of the regular tetrahedron. The consequent equality of their normalized brightness functions, and therefore of their variances, is **prior-covered**, not a claim of novelty here.

What (6) and first-moment Cauchy theory do not furnish without additional angular integration is the complete second-moment spectrum and its rigorous ordering. Existing extrema tables for Platonic shadows do not determine their variance. The new content is the exact full five-solid evaluation (2)--(3), with its sharp independent-random-orientation RMS sample counts.

Betke and McMullen's 1983 *Estimating the Sizes of Convex Bodies from Projections* is especially relevant to the statistical motivation. Its accessible abstract discusses weighted finite families of projections; the full paper was not accessible in the available open routes. We therefore record it as a material historical overlap risk and do **not** infer noncoverage from its abstract alone. Likewise the original Moran works were bibliographically and abstract-verified but not exhaustively full-text compared. Exact-alias, shadow/brightness, covariance, projection-body and cube/icosahedron variance searches did not locate a stronger covering theorem, but absence of a search hit is not treated as proof of novelty.

## Limitations
The exact table concerns only the five regular Platonic solids in three dimensions. It does not classify variance over all polyhedra, prove a universal extremal inequality, or optimize an adaptive viewing design.

The sample-count result is an exact **root-mean-square** guarantee for independent uniform orientations, not a probability-of-error or confidence guarantee. Correlated, deterministic, or adaptively chosen directions are outside the claim.

An older source may already have performed equivalent Platonic second-moment integrations. In particular, the full 1983 projection-estimation paper and Moran's early original works were not materially readable in this investigation; no whole-document noncoverage statement is made about them.

## References
1. P. A. P. Moran, *Surface Area of Small Objects*, *Nature* 154 (1944), 490--491. DOI: 10.1038/154490b0. First public date verified as 14 October 1944.
2. P. A. P. Moran, *Measuring Surface Area of a Convex Body*, *Annals of Mathematics* 45 (1944), 793--803. DOI: 10.2307/1969305.
3. U. Betke and P. McMullen, *Estimating the Sizes of Convex Bodies from Projections*, *Journal of the London Mathematical Society* s2-27 (1983), 525--538. DOI: 10.1112/jlms/s2-27.3.525.
4. E. Tsukerman and E. Veomett, *A Simple Proof of Cauchy's Surface Area Formula*, arXiv:1604.05815v1, 20 April 2016.
5. Á. G. Horváth, *On Convex Bodies that are Characterizable by Volume Function*, *Arnold Mathematical Journal* 6 (2020), 1--20. DOI: 10.1007/s40598-020-00132-0.
