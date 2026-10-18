# Sharp six-atom dependence threshold for Walsh–Gabor frames on the Boolean three-cube

## Finding
Let \(G=\mathbb F_2^3\), identified with the integers \(0,\ldots,7\) under bitwise exclusive-or. For every \(g\in\mathbb C^G\), form the \(8\)-by-\(64\) synthesis matrix \(V_g\) with columns
\[
  (P_{x,y}g)(t)=(-1)^{\langle t,y\rangle}g(t\oplus x),
  \qquad (x,y)\in G\times G,
\]
where \(\langle t,y\rangle\) is the binary dot product and \(\oplus\) is coordinatewise addition in \(G\). The spark is the minimum size of a linearly dependent set of columns.

**Theorem.** For every complex window \(g\), \(\operatorname{spark}(V_g)\le6\). Equality holds for the explicit positive integer window
\[
 g_*=(31,47,61,73,89,107,127,149),
\]
and on a nonempty Zariski-open dense subset of \(\mathbb C^8\) (hence for almost every complex window). In particular, every synthesis representation supported on at most two Gabor atoms is unique for generic \(g\), but for every such generic window there are distinct three-atom representations of the same vector.

A six-element dependent configuration for **every** window is
\[
 \Lambda=\{(2,2),(2,4),(6,3),(6,4),(7,0),(7,1)\}.
\]
The coordinates in this display are binary labels interpreted as integers; this is not a claim about the ordinary cyclic group of order eight.

## Assumptions and scope
The Hilbert space is \(\mathbb C^{\mathbb F_2^3}\), with arbitrary complex-valued windows and the full orbit of \(64\) time-frequency shifts. Matrices are unnormalized; multiplying columns by nonzero scalars does not change spark. "Generic" means outside a proper algebraic subset of the eight-dimensional complex window space. The upper bound includes degenerate windows, while the exact generic claim does not assert spark six for every nonzero window.

## Proof
**1. A universal six-column dependence.** Write \(P_\lambda=P_{x,y}\) for \(\lambda=(x,y)\in\Lambda\). Define three real \(8\)-by-\(8\) matrices \(B_1,B_2,B_3\) by listing their only nonzero entries \((\text{row},\text{column}):\text{value}\), with row and column labels \(0,\ldots,7\):

- \(B_1\): \((0,3):1\), \((1,2):-1\), \((4,7):-1\), \((5,6):1\).
- \(B_2\): \((0,5):1\), \((1,4):1\), \((2,7):-1\), \((3,6):-1\), \((4,1):-1\), \((5,0):-1\), \((6,3):1\), \((7,2):1\).
- \(B_3\): \((2,1):1\), \((3,0):-1\), \((6,5):-1\), \((7,4):1\).

A direct calculation using \((P_{x,y})_{t,u}=(-1)^{\langle t,y\rangle}\mathbf1_{u=t\oplus x}\) proves all eighteen identities
\[
 B_j^{\mathsf T}P_\lambda+P_\lambda^{\mathsf T}B_j=0
 \quad(j=1,2,3;\ \lambda\in\Lambda).
\]
Consequently, for every \(g\), the vectors \(B_jg\) annihilate all six columns in the **bilinear** pairing:
\[
 (B_jg)^{\mathsf T}P_\lambda g
 =g^{\mathsf T}B_j^{\mathsf T}P_\lambda g=0.
\]
The three annihilators are generically independent. Indeed, at \(\mathbf1=(1,\ldots,1)^{\mathsf T}\), the first three rows of the matrix \((B_1\mathbf1\;B_2\mathbf1\;B_3\mathbf1)\) are
\[
 \begin{pmatrix}1&1&0\\-1&1&0\\0&-1&1\end{pmatrix},
 \qquad\det=2.
\]
Thus on a nonempty Zariski-open subset the common left annihilator has dimension at least three, and the six columns have rank at most five. Every six-by-six minor is a polynomial in the entries of \(g\); since each vanishes on this dense open set, each is identically zero. The six columns therefore have rank at most five **for every** window. The standalone exact checker additionally expands every one of the \(\binom{8}{6}=28\) maximal minors coefficient by coefficient and verifies its vanishing without relying on numerical experimentation.

**2. A window with every five columns independent.** Use \(g_*\) as displayed above and reduce the integer matrix \(V_{g_*}\) modulo the prime \(p=1000003\). The composition law for time-frequency shifts implies that multiplying all selected columns on the left by \(P_{x_0,y_0}^{-1}\) translates their phase-space labels by \((-x_0,-y_0)\), up to individual nonzero signs. Thus it suffices to test five-column subsets containing \((0,0)\). There are exactly
\[
 \binom{63}{4}=595665
\]
such subsets. The complete deterministic modular-elimination program `verify_lower.cpp` enumerates each of them, constructs the exact \(8\)-by-\(5\) matrix, and finds rank five in \(\mathbb F_{1000003}\) in every case. This is an exhaustive finite computation, **not** a random sample. The elementary prime check and elimination algorithm are included in the source file. A nonzero minor modulo a prime is a nonzero integer determinant and hence a nonzero complex determinant; every five columns of \(V_{g_*}\) are therefore independent. This also implies all smaller subsets are independent.

**3. Sharpness and genericity.** The universal dependence proves spark at most six for all \(g\), while step 2 proves spark at least six for \(g_*\). Hence \(\operatorname{spark}(V_{g_*})=6\). For each five-element phase-space set, at least one five-by-five minor is a nonzero polynomial (because it is nonzero at \(g_*\)). The finite intersection of the corresponding nonvanishing Zariski-open sets contains \(g_*\), and on this intersection every five columns are independent. The universal upper bound gives generic spark exactly six.

**4. Sharp synthesis ambiguity.** Suppose \(g\) belongs to this generic set. Two distinct representations using at most two atoms would subtract to a nontrivial dependence involving at most four columns, which is impossible. For the six columns indexed by \(\Lambda\), step 1 and five-column independence imply rank exactly five and a unique (up to scalar) dependence with all six coefficients nonzero. Splitting those six terms into two groups of three yields distinct representations of the same vector by exactly three Gabor atoms. This establishes the asserted sharp two-versus-three synthesis threshold.

## Verification
The self-contained sources `verify_upper.py` and `verify_lower.cpp` are part of this package. From their directory, run

```bash
python3 verify_upper.py
g++ -O3 -std=c++17 verify_lower.cpp -o verify_lower
./verify_lower
```

The first checker independently tests all eighteen skew-symmetry identities, the explicit three-dimensional annihilator minor, and all \(28\) six-by-six minors using integer polynomial coefficient cancellation (\(720\) determinant terms per minor). The second checks \(595665\) normalized five-column sets by exact modular row reduction at the explicit integer window; it reports zero failures. Both were executed successfully. The theorem's universal part follows from polynomial identities, while its optimal lower bound uses finite exhaustive computation over a completely specified finite combinatorial domain. The modular calculation is an exact nonvanishing certificate over \(\mathbb C\), not an approximation.

## Relationship to prior work
Malikiosis, *Spark Deficient Gabor Frames* (first arXiv version dated 2016-02-29), proves that no window on a noncyclic finite abelian group generates a full-spark Gabor frame. For \(G=\mathbb F_2^3\), this only forces a dependence among at most eight atoms; the present six-atom upper bound and the matching five-column independence certificate are strictly sharper. Pfander's 2012 chapter develops the general finite-abelian Gabor, spark, and sparse-synthesis framework but does not provide the stated sharp six-atom threshold. Lawrence–Pfander–Walnut's full-spark theorem addresses prime cyclic dimensions rather than the noncyclic Boolean cube. Bui Dang and collaborators study linear dependencies in cyclic Weyl–Heisenberg orbits, especially special fiducial vectors, not generic windows for the elementary abelian eight-point group. The present claim is an exact group-specific refinement, not a claim of a corresponding theorem in all finite groups.

## Limitations
The threshold is proved only for the full time-frequency orbit over the eight-point elementary abelian two-group. No general dimension formula is inferred. The finite lower certificate uses an explicit integer window and a named prime, and the source must be compiled/executed to reproduce its exhaustive rank enumeration. Published results not accessible through the inspected primary sources could contain an equivalent or stronger statement; publication priority is not independently established. The exact theorem concerns algebraic genericity, not a uniform lower bound on the smallest singular value of every five-column submatrix.

## References
1. R.-D. Malikiosis, *Spark Deficient Gabor Frames*, arXiv:1602.09012 (first public version 2016-02-29), especially Theorem 1.2 and §3.
2. G. E. Pfander, *Gabor Frames in Finite Dimensions*, in *Finite Frames: Theory and Applications* (2012), §6 on linear independence; author-posted full text at `https://www.mathematik.uni-marburg.de/~pfander/pubs/FiniteGaborFramesChapter.pdf`.
3. J. F. Lawrence, G. E. Pfander, and D. F. Walnut, *Linear Independence of Gabor Systems in Finite Dimensional Vector Spaces*, *J. Fourier Anal. Appl.* **11** (2005), 715–726, DOI:10.1007/s00041-005-5017-6.
4. H. Bui Dang, K. Blanchfield, I. Bengtsson, and D. M. Appleby, *Linear Dependencies in Weyl-Heisenberg Orbits*, arXiv:1211.0215 (first public version 2012-11-01), §§1–2, 4–5.
