# No one-angle dual for the non-tight real four-vector equiangular frame
## Finding
Every non-tight real equiangular frame of four unit vectors spanning \(\mathbb R^3\) has coherence \(1/\sqrt5\) and, up to an orthogonal transformation, a permutation, and independent vector sign changes, belongs to one switching class. No dual frame is a one-angle frame: for every dual \(\{g_i\}_{i=1}^4\), the six quantities \(|\langle g_i,g_j\rangle|\) with \(i<j\) assume at least two distinct values.

The canonical dual has exactly the three off-diagonal moduli
\[
\frac{\sqrt5}{20},\qquad \frac{5-\sqrt5}{10},\qquad \frac{5+\sqrt5}{10},
\]
and exactly two squared norms,
\[
\frac{3(5-\sqrt5)}{20},\qquad \frac{3(5+\sqrt5)}{20},
\]
each occurring twice.

## Assumptions and scope
A real equiangular frame here means four unit vectors \(\{f_i\}_{i=1}^4\subset\mathbb R^3\) spanning \(\mathbb R^3\) such that \(|\langle f_i,f_j\rangle|\) is constant for \(i\ne j\). A dual \(\{g_i\}_{i=1}^4\) satisfies
\[
x=\sum_{i=1}^4\langle x,f_i\rangle g_i\qquad(x\in\mathbb R^3).
\]
A one-angle frame means that its off-diagonal Gram entries have one modulus; equal norms are not assumed. Thus the nonexistence statement is stronger than merely ruling out a unit-norm equiangular dual.

The result concerns real frames with four vectors in dimension three. It does not assert an analogous obstruction for complex frames or for other cardinalities.

## Proof
Write the Gram matrix of the unit-norm equiangular frame as \(G=I+\alpha Q\), where \(Q\) is a real symmetric signature matrix with zero diagonal and off-diagonal entries in \(\{\pm1\}\). Switching vector signs makes the first row of \(Q\) positive. The remaining three signs are \(a,b,c\in\{\pm1\}\). Direct characteristic-polynomial calculation gives three possibilities:
\[
(t-3)(t+1)^3,
\]
when \((a,b,c)=(1,1,1)\),
\[
(t+3)(t-1)^3,
\]
when \((a,b,c)=(-1,-1,-1)\), and
\[
(t^2-1)(t^2-5)
\]
for each of the six mixed sign triples. Since \(G\) must be positive semidefinite of rank three, the all-positive case is impossible, the all-negative case gives the tight simplex with \(\alpha=1/3\), and every non-tight case has \(\alpha=1/\sqrt5\). The six mixed triples form one switching-permutation class: their four triangle-sign products consist of two positive and two negative signs, and permutations act transitively on such two-subsets.

It is therefore enough to use
\[
Q=\begin{pmatrix}
0&1&1&1\\
1&0&1&-1\\
1&1&0&-1\\
1&-1&-1&0
\end{pmatrix},\qquad
G=I+\frac1{\sqrt5}Q.
\]
A kernel vector is
\[
z=\left(-1,\frac{\sqrt5-1}{2},\frac{\sqrt5-1}{2},1\right)^{\mathsf T}.
\]
The Moore--Penrose inverse \(K=G^\dagger\), which is the Gram matrix of the canonical dual, is
\[
\begin{pmatrix}
\frac34-\frac{3\sqrt5}{20}&\frac{\sqrt5}{20}&\frac{\sqrt5}{20}&\frac12-\frac{\sqrt5}{10}\\
\frac{\sqrt5}{20}&\frac34+\frac{3\sqrt5}{20}&-\frac12-\frac{\sqrt5}{10}&-\frac{\sqrt5}{20}\\
\frac{\sqrt5}{20}&-\frac12-\frac{\sqrt5}{10}&\frac34+\frac{3\sqrt5}{20}&-\frac{\sqrt5}{20}\\
\frac12-\frac{\sqrt5}{10}&-\frac{\sqrt5}{20}&-\frac{\sqrt5}{20}&\frac34-\frac{3\sqrt5}{20}
\end{pmatrix}.
\]
This immediately gives the stated canonical-dual norm and angle sets.

Now let \(T\) and \(U\) be the synthesis matrices of the original frame and an arbitrary dual, respectively, and put \(H=U^{\mathsf T}U\). Duality gives \(UT^{\mathsf T}=I\), hence
\[
GHG=G.
\]
Also \(H\) is a Gram matrix of four vectors in \(\mathbb R^3\), so \(\operatorname{rank}H\le3\).

Every symmetric solution of \(GHG=G\) has the form
\[
H=K+za^{\mathsf T}+az^{\mathsf T}
\]
for some \(a\in\mathbb R^4\). Indeed, if \(D=H-K\), then \(GDG=0\); since \(G\) is invertible on \(z^\perp\), the bilinear form of \(D\) vanishes on \(z^\perp\times z^\perp\), which is exactly the displayed form.

Suppose a dual were one-angle. There would be a scalar \(\beta\) and signs \(\varepsilon_{ij}\in\{\pm1\}\) such that
\[
H_{ij}=\beta\varepsilon_{ij}\qquad(i<j).
\]
The case of common modulus zero is included by \(\beta=0\). Absorbing the sign of the first off-diagonal entry into \(\beta\) fixes \(\varepsilon_{12}=1\), leaving exactly \(2^5=32\) sign patterns. For each pattern, the six equations above are linear in the four coordinates of \(a\) and \(\beta\), over \(\mathbb Q(\sqrt5)\). Exact row reduction gives twenty inconsistent systems. The remaining twelve systems each determine a matrix \(H\) with nonzero determinant. Thus every algebraically possible one-angle generalized inverse has rank four, contradicting \(\operatorname{rank}H\le3\). Therefore no dual is one-angle.

## Verification
The accompanying checker performs arithmetic exactly in \(\mathbb Q(\sqrt5)\). It verifies the three signature-matrix characteristic-polynomial classes, verifies \(GKG=G\) and \(Gz=0\), enumerates all thirty-two relative one-angle sign patterns, solves every overdetermined linear system exactly, and checks that all twelve consistent candidates have nonzero determinant. Its success line is:

`VERIFY_OK signature_classes=1,1,6 one_angle_patterns=32 inconsistent=20 full_rank_candidates=12`

The proof does not infer an infinite statement from a numerical sample: the finite enumeration is the complete sign-pattern reduction of the one-angle condition.

## Relationship to prior work
Christensen, Datta, and Kim study real non-tight equiangular frames and explicitly examine when such frames can have equiangular duals; when an equiangular dual is unavailable, they study few-angle canonical duals. Their four-eigenvalue theorem assumes a different spectral form, including an integral extremal eigenvalue and a specified regular eigenvector. The signature matrix above has spectrum \(\{-\sqrt5,-1,1,\sqrt5\}\), so that theorem does not imply this result. Their full accepted manuscript was inspected through the statements and proofs governing equiangular and few-angle duals.

Datta's later chapter again studies the angle set of canonical duals of non-tight equiangular frames. Available metadata and abstract describe general conditions rather than this all-duals obstruction. Full text of that chapter was not available in the inspected public source, so it remains a residual literature risk rather than negative evidence.

## Limitations
The obstruction is proved only for the real non-tight four-vector, three-dimensional class. It does not classify the minimum number of angles among all noncanonical duals beyond proving that one angle is impossible. The later book chapter just noted could contain a specialized low-dimensional calculation not visible from the accessible abstract; no such statement was found in the inspected sources or semantic searches.

## References
1. Ole Christensen, Somantika Datta, and Rae Young Kim, *Equiangular frames and generalizations of the Welch bound to dual pairs of frames*, Linear and Multilinear Algebra, DOI: 10.1080/03081087.2019.1586825. Published online 18 March 2019.
2. Somantika Datta, *Equiangular Frames and Their Duals*, in *Excursions in Harmonic Analysis, Volume 6*, DOI: 10.1007/978-3-030-69637-5_9.
