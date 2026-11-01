# Identical integer Fourier-null sets for two dimensionally distinct triangular measures

## Finding

Define two finite planar digit sets
\[
D_3=\{(0,0),(1,0),(0,1)\},\qquad
D_6=\{(a,b)\in\mathbb Z_{\ge0}^{2}:a+b\le2\}.
\]
For \(r\in\{3,6\}\), let independent random vectors \(U_j^{(r)}\) be uniform on \(D_r\), and let \(\mu_r\) be the probability law of the absolutely convergent random series
\[
X_r=\sum_{j=1}^{\infty}3^{-j}U_j^{(r)}.
\]
Use the convention \(\widehat\mu_r(m,n)=\int e^{-2\pi i(mx+ny)}\,d\mu_r(x,y)\). For every nonzero lattice frequency \((m,n)\in\mathbb Z^2\setminus\{(0,0)\}\), put
\[
v=\max\{k\ge0:3^k\mid m\text{ and }3^k\mid n\},
\quad (a,b)=(m/3^v,n/3^v).
\]
Then the two measures have **exactly the same integer Fourier-null set**:
\[
\boxed{\widehat\mu_3(m,n)=0\ \Longleftrightarrow\
\widehat\mu_6(m,n)=0\ \Longleftrightarrow\
(a,b)\bmod3\in\{(1,2),(2,1)\}.}
\]
Neither Fourier coefficient vanishes at \((m,n)=(0,0)\). The shared zero set has natural density
\[
\boxed{\lim_{N\to\infty}\frac{\#\{(m,n)\in[-N,N]^2\cap\mathbb Z^2:\widehat\mu_6(m,n)=0\}}{(2N+1)^2}=\frac14.}
\]
For any integer \(L\ge1\), the number of residue classes in \((\mathbb Z/3^L\mathbb Z)^2\) at which **at least one of the first \(L\) Fourier-mask factors** vanishes is exactly
\[
\boxed{(9^L-1)/4.}
\]
Despite this shared lattice Fourier-null set, their attractor supports have distinct Hausdorff dimensions:
\[
\boxed{\dim_H\operatorname{supp}(\mu_3)=1,\qquad
\dim_H\operatorname{supp}(\mu_6)=\log_3 6.}
\]
Consequently the torus convolution operators \(f\mapsto\mu_3*f\) and \(f\mapsto\mu_6*f\) on \(L^2(\mathbb T^2)\), with each measure periodized modulo \(\mathbb Z^2\), have **identical closed kernels**, even though their underlying measures and support dimensions differ.

## Assumptions and scope

All digits at each level are independent and equally weighted within their respective digit sets. Both similarities have scalar contraction ratio \(1/3\); the Fourier convention above fixes signs, which do not affect the zero set. The lattice means all frequencies in \(\mathbb Z^2\), including negative coordinates. Divisibility of zero by every positive integer is understood in the usual way; because the frequency pair is nonzero, \(v\) is finite. The natural density is taken over centered square boxes, and the finite-level count refers to the first \(L\) factors, not to a periodicity assertion about the entire infinite Fourier transform.

## Proof

**1. Fourier products and their nonzero tails.** The digit masks are
\[
M_3(z,w)=\frac{1+z+w}{3},\qquad
M_6(z,w)=\frac{1+z+w+z^2+zw+w^2}{6}.
\]
Independence gives the infinite products
\[
\widehat\mu_r(m,n)=\prod_{j=1}^{\infty}
M_r\big(e^{-2\pi i m/3^j},e^{-2\pi i n/3^j}\big).
\]
For fixed integers \(m,n\), the \(j\)-th factor is \(1+O((|m|+|n|)3^{-j})\). Thus a product with no zero factor is nonzero: after finitely many factors, the deviations from \(1\) are summable, and the tail factors are uniformly bounded away from zero. Accordingly the Fourier coefficient vanishes exactly when some finite mask factor vanishes.

**2. Primitive-cyclotomic obstruction.** Let \(s\ge1\), \(N=3^s\), \(\zeta\) be a primitive \(N\)-th root, and let integers \(a,b\) not both divisible by \(3\). For either digit set, form the integer polynomial of degree less than \(N\) obtained by reducing exponents \(ax+by\) modulo \(N\):
\[
C_{r;a,b}(t)=\sum_{(x,y)\in D_r}t^{(ax+by)\bmod N}.
\]
It vanishes at \(\zeta\) if and only if it is divisible by the minimal polynomial \(\Phi_N(t)=1+t^{N/3}+t^{2N/3}\). For each \(h\in\{0,\ldots,N/3-1\}\), this divisibility means the coefficients of \(t^h,t^{h+N/3},t^{h+2N/3}\) are equal. Indeed, on collecting monomials into these three-term blocks, the remainder is expressed in independent coefficients of \(t^h\) and \(t^{h+N/3}\), with total degree less than \(2N/3\).

For \(s\ge2\), the three exponents in each such block are congruent modulo \(3\), so **each** number of digit exponents in a given residue class modulo \(3\) must be divisible by \(3\). For \(D_6\), direct counting gives the complete table below (columns are the counts in residue classes \(0,1,2\), in that order):

| \((a,b)\bmod3\) | class counts |
|---|---|
| \((0,1)\) | \((3,2,1)\) |
| \((0,2)\) | \((3,1,2)\) |
| \((1,0)\) | \((3,2,1)\) |
| \((1,1)\) | \((1,2,3)\) |
| \((1,2)\) | \((2,2,2)\) |
| \((2,0)\) | \((3,1,2)\) |
| \((2,1)\) | \((2,2,2)\) |
| \((2,2)\) | \((1,3,2)\) |

In all eight primitive mod-\(3\) pairs at least one class count is not divisible by \(3\). Hence the six-digit mask has **no zero at primitive \(3^s\)-th roots for any \(s\ge2\)**. For \(D_3\), the mod-\(3\) class counts arise from the three exponents \(0,a,b\); divisibility by \(3\) would require all three to be in one class, forcing \(a\equiv b\equiv0\pmod3\), excluded. Thus the same higher-order obstruction holds for the three-digit mask.

At \(s=1\) the condition is simply equality of all three mod-\(3\) class counts. Directly counting exponents in \(D_6\) gives equality \((2,2,2)\) exactly for \((a,b)\equiv(1,2),(2,1)\pmod3\). For \(D_3\), equality \((1,1,1)\) occurs for exactly those same two pairs. This proves the complete primitive mask-zero classification for both digit sets.

**3. All integer Fourier zeros.** For the pair \((m,n)\ne(0,0)\), the first \(v\) factors equal \(1\). At level \(j=v+1\) the character pair has primitive order \(3\); at every later level it has primitive order \(3^{j-v}\ge9\). Step 2 excludes every later factor and identifies the precise two residue configurations at level \(v+1\). This proves the boxed common-zero formula.

**4. Density and finite-resolution count.** For each \(v\ge0\), there are exactly two residue classes modulo \(3^{v+1}\) satisfying the displayed condition with this \(v\). Such classes have planar density \(2/9^{v+1}\), and the classes belonging to different \(v\) are disjoint. The union of classes at \(v\ge L\) is contained in \(3^L\mathbb Z^2\), of density \(9^{-L}\). This uniform tail bound justifies passage to the infinite disjoint union, giving
\[
\sum_{v=0}^{\infty}\frac{2}{9^{v+1}}=\frac14.
\]
Modulo \(3^L\), the first-zero layer \(v\in\{0,\ldots,L-1\}\) has exactly \(2\,9^{L-v-1}\) classes, so their sum is \(2\sum_{h=0}^{L-1}9^h=(9^L-1)/4\).

**5. Distinct geometries and equal convolution kernels.** Let \(T=\{(x,y):x>0,y>0,x+y<1\}\). For either \(r\), the six or three contractions \(x\mapsto(x+d)/3\) map \(T\) into itself and have mutually disjoint image interiors. The open set condition and the standard similarity-dimension theorem therefore give dimensions \(\log_3r\) for the two supports. The Fourier characters form an orthonormal basis of \(L^2(\mathbb T^2)\), and convolution by a periodized finite measure multiplies each character by its corresponding integer Fourier coefficient. Identical multiplier zero sets imply identical closed operator kernels.

## Verification

Run `python3 checker.py` from this package directory. The dependency-free checker performs exact integer-polynomial divisibility tests modulo \(\Phi_{3^s}\) on every primitive pair for \(1\le s\le5\), independently for both digit sets. It then enumerates every residue class modulo \(3^L\) for \(1\le L\le5\) and compares direct finite-factor cancellation against the closed formula and the exact class counts. The completed run returned `SIX_TRIANGLE_FOURIER_ZERO_EQUIVALENCE_OK 59048 primitive pairs`; the finite-level zero counts were \(2,20,182,1640,14762\). The universal classification and density are established by the proof, not by these finite checks.

## Relationship to prior work

Lam and Leung's cyclotomic vanishing-sum analysis supplies general root-of-unity context; the present coefficient-multiplicity obstruction is the direct specialized argument needed to classify this particular six-digit mask. Dutkay and Jorgensen establish the Fourier-product and spectral-IFS framework and analyze the three-vertex simplex model. A published analysis of the **same six-point triangular frequency aperture** determines optimized fourth moments of arbitrary phase coefficients, not the primitive \(3\)-power mask zeros for the all-positive digit weights or the infinite-product integer-null set. In particular, its fourth-moment conclusions do not imply the two-measure equality, the finite-level census, or the support-dimension contrast. The six-digit polynomial is not a multiple of \(1+z+w\) in \(\mathbb C[z,w]\): substituting \(w=-1-z\) gives \(z^2+z+1\), which is nonzero as a polynomial, so the zero-set agreement is not a tautological factorization into the three-digit mask.

## Limitations

The theorem concerns exactly these two uniformly weighted measures, scalar base-three dilation, **integer** Fourier frequencies, and torus convolution kernels. It does not assert coincidence of their Fourier zeros at all real frequencies, equality of nonzero Fourier magnitudes, spectral-measure status, or equality of the measures. Earlier equivalent computations of cyclotomic masks in specialized fractal-wavelet literature remain possible; no claim of exhaustive historical originality or independent validation is made.

## References

- T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, first public preprint 1995-11-13, arXiv:math/9511209, https://arxiv.org/abs/math/9511209.
- D. E. Dutkay and P. E. T. Jorgensen, *Analysis of Orthogonality and of Orbits in Affine Iterated Function Systems*, first public 2006-06-14, arXiv:math/0606349, https://arxiv.org/abs/math/0606349. See the Fourier-product formula (2.5) and the simplex examples in Section 5.
- *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, publicly available mathematical research finding (2026-10-11). It concerns fourth-moment phase optimization on the same six-point aperture, not its integer Fourier zeros under ternary refinement.
