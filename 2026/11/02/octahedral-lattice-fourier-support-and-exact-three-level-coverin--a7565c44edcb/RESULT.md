# Octahedral lattice Fourier support and exact three-level covering multiplicities

## Finding
Let \(B=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\). With the Fourier normalization
\[\widehat{\mathbf1_B}(k)=\int_B e^{-2\pi i k\cdot x}\,dx,\qquad k\in\mathbb Z^3,\]
the **complete nonzero integer-frequency support** is exactly the reflection arrangement
\[\{k\in\mathbb Z^3:\ |k_i|=|k_j|\text{ for some }i<j\}.\]
Its intersection with \([-N,N]^3\), for every integer \(N\ge0\), has precisely \(24N^2+2N+1\) points. All its coefficients are as follows, with permutations and coordinate sign changes understood:

| Absolute-coordinate pattern | Fourier coefficient |
| --- | --- |
| \((0,0,0)\) | \(4/3\) |
| \((a,0,0)\), \(a\ge1\) | \(2/(\pi^2 a^2)\) |
| \((a,a,a)\), \(a\ge1\) | \(-1/(4\pi^2a^2)\) |
| \((a,a,b)\), \(a\ge1\), \(b\ge0\), \(b\ne a\) | \(1/(\pi^2(b^2-a^2))\) |
| all remaining patterns | \(0\) |

For each positive integer \(m\), define the periodic integer-valued multiplicity
\[P_m(u)=\sum_{n\in\mathbb Z^3}\mathbf1_{\{\|u-n\|_1<m\}}.\]
For all \(u\) outside the boundaries of these octahedra, **simultaneously for every** \(m\ge1\),
\[\boxed{P_m(u)=\frac43(m^3-m)+mP_1(u).}\]
Moreover \(P_1\in\{0,1,2\}\); the three values occur on regions of the unit torus having Lebesgue fractions, respectively, \(1/6,1/3,1/2\). Consequently the integer-radius \(m\) covering multiplicities are *exactly* the three values \(\frac43(m^3-m)\), \(\frac43(m^3-m)+m\), \(\frac43(m^3-m)+2m\), with those same volume fractions for every \(m\).

## Assumptions and scope
The body is the standard radius-one three-dimensional \(\ell_1\)-ball centered at the integer origin, and the frequency lattice and translation lattice are \(\mathbb Z^3\) under the displayed \(2\pi\) Fourier normalization. The Fourier classification includes every integer frequency and all sign and permutation degeneracies. The covering identity is pointwise off the countable union of boundaries \(\bigcup_{n\in\mathbb Z^3,m\ge1}\partial(n+mB)\), and therefore holds almost everywhere. There is no claim about arbitrary real radii, general lattice deformations, or nonintegral frequency lattices.

## Proof
**1. Fourier transform.** For \(t>0\), put \(B_t=tB\), and \(W_k(t)=\int_{B_t}e^{-2\pi i k\cdot x}\,dx\). Direct integration over all three real coordinates, followed by integration over \(t\), gives the identity for \(s>0\):
\[\int_0^\infty e^{-st}W_k(t)\,dt=\frac1s\prod_{j=1}^3\int_{\mathbb R}e^{-s|x_j|-2\pi i k_jx_j}\,dx_j=\frac{8s^2}{\prod_{j=1}^3(s^2+4\pi^2 k_j^2)}.\]
This is a genuine Laplace transform; Fubini follows from exponential integrability. Invert it at \(t=1\) by elementary real partial fractions, using \(\sin(2\pi a)=0\) and \(\cos(2\pi a)=1\) for \(a\in\mathbb Z\).

For the origin, the transform is \(8/s^4\), giving \(4/3\). For \((a,0,0)\), with \(A=2\pi a\), it becomes \(8/[s^2(s^2+A^2)]\), giving \(8/A^2\). For \((a,a,0)\) it becomes \(8/(s^2+A^2)^2\), giving \(-4/A^2\). For \((a,a,a)\), it is \(8s^2/(s^2+A^2)^3\), giving \(-1/A^2\).

For \((a,a,b)\) with \(b\ne a\) and \(a>0\), put \(A=2\pi a\), \(C=2\pi b\). Its Laplace transform is
\[\frac{8s^2}{(s^2+A^2)^2(s^2+C^2)}.\]
The coefficient of \((s^2+A^2)^{-2}\) in its partial fractions is \(-8A^2/(C^2-A^2)\). At integral-frequency phase \(t=1\), the two simple-pole terms yield sine values zero, while the repeated-pole inverse is \(-1/(2A^2)\). The result is \(4/(C^2-A^2)=1/[\pi^2(b^2-a^2)]\), including \(b=0\). For all distinct nonzero absolute frequencies, only simple quadratic poles occur and their sine inverses vanish at \(t=1\); likewise the case \((a,b,0)\) with nonzero distinct \(a,b\). Thus the table is exhaustive and every displayed nonzero expression is nonzero.

The support count follows by disjoint enumeration: the origin contributes 1; nonzero coordinate axes contribute \(6N\); configurations \((a,a,0)\) contribute \(12N\); configurations \((a,a,a)\) contribute \(8N\); and configurations \((a,a,b)\) with distinct positive \(a,b\) contribute \(24N(N-1)\). Their sum is \(24N^2+2N+1\).

**2. Dilation rigidity.** Every nonzero coefficient in the Fourier table is homogeneous of degree \(-2\) along positive integer frequency multiples. Scaling the body therefore yields, for \(k\ne0\),
\[\widehat{\mathbf1_{mB}}(k)=m^3\widehat{\mathbf1_B}(mk)=m\widehat{\mathbf1_B}(k).\]
The zeroth coefficient is \(4m^3/3\). Periodizing over \(\mathbb Z^3\) identifies these with torus Fourier coefficients of \(P_m\). Uniqueness of Fourier coefficients for \(L^1(\mathbb T^3)\) proves the boxed identity almost everywhere. Since the integer-valued functions are locally constant off their boundaries, the equality holds at every point outside those boundaries, simultaneously over countably many integer radii.

There is also a separate combinatorial proof. Reduce to \(u\in(0,1)^3\) away from boundaries. Each integer-center coordinate contributes either \(u_j+t_j\) or \(1-u_j+t_j\), for \(t_j\in\mathbb Z_{\ge0}\). For each of eight choices, let \(r\in(0,3)\setminus\mathbb Z\) be the sum of the three base contributions and \(c=\lceil r\rceil\). The number of admissible nonnegative triples for radius \(m\) is \(\binom{m+3-c}{3}\), with zero if the upper argument is below 3. The complementary choice has \(r'=3-r\) and \(c'=4-c\). Each of four paired choices contributes \((m^3+2m)/3\) if \(c\in\{1,3\}\), or \((m^3-m)/3\) if \(c=2\). At radius one the first type contributes one and the second zero. Summing proves the same identity for every positive integer \(m\), independently of Fourier analysis.

**3. Exact multiplicity distribution.** If two distinct integer centers both lie within \(\ell_1\)-distance \(<1\) of a point, their mutual integer distance is \(<2\), hence exactly 1. Three such centers would form a triangle in the bipartite cubic lattice graph, which is impossible. Thus \(P_1\le2\). Integration over a unit torus cell gives \(\mathbb E P_1=\operatorname{vol}(B)=4/3\). The overlap volume of two unit octahedra at adjacent lattice centers is
\[\int_{|y|+|z|<1/2}(1-2|y|-2|z|)\,dy\,dz=4\int_0^{1/2}r(1-2r)\,dr=1/6.\]
There are three unoriented nearest-neighbor edge types per unit cell, giving \(\mathbb E\binom{P_1}{2}=3/6=1/2\). As \(P_1\in\{0,1,2\}\), the two moment equations and normalization give probabilities \(1/6,1/3,1/2\). Each is positive, so all three covering levels occur.

## Verification
The standalone `checker.py` uses exact rational arithmetic to verify the support description, nonzero-frequency lattice counts for \(1\le N\le8\), and homogeneous scaling on tested lattice frequencies. It independently enumerates translated lattice centers for five generic rational shifts and all radii \(1\le m\le7\), then checks the overlap and fraction identities. A second direct quadrature of the positive-octant simplex confirms the listed transform coefficients at representative distinct and repeated frequencies. These tests confirm finite instances; the proofs above establish the unbounded lattice and all-radius assertions.

## Relationship to prior work
Diaz, Le and Robins (arXiv:1602.08593, first posted 2016-02-27) give a general combinatorial Stokes representation of Fourier transforms of polytopes and examine generic versus nongeneric frequency directions. Borda (arXiv:1608.02417, first posted 2016-08-08), especially §2.3 and Theorem 3, gives a residue representation for simplices and discusses general cross-polytopes; that is directly relevant general machinery, but its principal discrepancy theorems assume rational independence of reciprocal axis lengths, unlike the equal-axis body here. Neither inspected full text states the exact six-plane integer-frequency support, coefficients, or three probability fractions.

McMullen's translated lattice enumerator results, as discussed by Higashitani, Murai and Yoshinaga (arXiv:2307.08151, §1–2), already imply polynomiality for a fixed translate of an integral polytope. Combining that general polynomiality with reciprocity and central symmetry can explain why the three-dimensional integer-radius count has only cubic and linear terms. Accordingly the *mere cubic-linear shape* is **not** claimed as a new general phenomenon; the contribution is the explicit Fourier-support arrangement, exact coefficients, and complete three-level translation profile with exact fractions.

## Limitations
The theorem is specific to the standard three-dimensional octahedron and the standard integer lattice. General polytope Fourier formulas and translated Ehrhart theory supply significant antecedent machinery. Equivalent specialized residue computations or covering distributions may exist in older literature not found during bounded searches; originality is not independently certified. The numerical quadrature and finite enumeration are secondary checks and not substitutes for the algebraic and combinatorial proofs.

## References
1. R. Diaz, Q.-N. Le and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593 (first public version 2016-02-27), https://arxiv.org/abs/1602.08593.
2. B. Borda, *Lattice points in algebraic cross-polytopes and simplices*, arXiv:1608.02417 (first public version 2016-08-08), https://arxiv.org/abs/1608.02417.
3. A. Higashitani, S. Murai and M. Yoshinaga, *Ehrhart quasi-polynomials and parallel translations*, arXiv:2307.08151 (first public version 2023-07-16), https://arxiv.org/abs/2307.08151.
