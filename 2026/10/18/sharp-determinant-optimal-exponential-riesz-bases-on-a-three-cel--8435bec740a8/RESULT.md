# Sharp determinant-optimal exponential Riesz bases on a three-cell multittile

## Finding
For the threefold unit-lattice multittile \(\Omega=[0,1)\cup[1,2)\cup[3,4)\), consider
\[\mathcal E_\theta=\{e^{2\pi i(n+\theta_j)x}:n\in\mathbb Z,\ j=0,1,2\}\]
for three distinct phases modulo one. The maximal determinant of the three-by-three analysis Gram matrix is
\[D_{\max}=\frac{9748+1360\sqrt{10}}{729}=19.271190147913\ldots.\]
The complete equality family, up to permutation, is
\[\{\theta_0,\theta_1,\theta_2\}=\left\{\tau-\frac{t_*}{2\pi},\tau,\tau+\frac{t_*}{2\pi}\right\}\pmod1,
\qquad t_*=\arccos\!\left(\frac{\sqrt{10}-2}{6}\right),\]
for arbitrary \(\tau\in\mathbb R/\mathbb Z\). The optimum has two equal short angular gaps and is not a regular three-gon. For the regular triple \(\theta_j=\tau+j/3\), the exponent-three row is \(e^{6\pi i\tau}\) times the exponent-zero row, making the determinant zero. No system in this class is orthogonal or tight.

## Assumptions and scope
The exponentials have their raw unit-modulus normalization on \(\Omega\) (squared norm \(3\)) and the measure is Lebesgue measure. Integer changes to a phase do not change its coset. Let
\[V=\big(e^{2\pi i r\theta_j}\big)_{r\in\{0,1,3\},\ j=0,1,2}.\]
The objective is \(D=\det(VV^*)=|\det V|^2\), the product of the three squared analysis singular values. The theorem does not separately optimize the lower frame bound or the condition number. The three cosets may have any real phases.

## Proof
**Fiber analysis.** Write \(f_r(t)=f(t+r)\) for \(0\le t<1\). Parseval in the integer frequency index gives, for each \(j\),
\[\sum_{n\in\mathbb Z}|\langle f,e^{2\pi i(n+\theta_j)\cdot}\rangle|^2=\int_0^1\left|\sum_{r\in\{0,1,3\}}f_r(t)e^{-2\pi i r\theta_j}\right|^2dt.\]
Here the omitted factor \(e^{-2\pi i\theta_jt}\) has modulus one. Summing over \(j\) gives the Gram matrix \(VV^*\) in the fibers. The synthesis map, after three Fourier-series isometries and multiplication by the diagonal phase factors \(e^{2\pi i\theta_jt}\), acts by \(V\). It is invertible exactly when \(V\) is, which is therefore the Riesz basis criterion. Repeated phases have determinant zero, so they may be included in the compact maximization domain.

**Algebraic reduction.** Set \(z_j=e^{2\pi i\theta_j}\). The known generalized Vandermonde identity is
\[\det V=(z_1-z_0)(z_2-z_0)(z_2-z_1)(z_0+z_1+z_2).\]
A common rotation preserves \(|\det V|\), so choose \(z_0=1\) and write \(z_1=e^{i(u+v)}\), \(z_2=e^{i(u-v)}\). With \(X=\cos u\), \(Y=\cos v\), the pairs \((X,Y)\) sweep all of \([-1,1]^2\). Taking squared magnitudes of the factors gives
\[D=F(X,Y)=16(1-Y^2)(X-Y)^2(1+4Y^2+4XY).\]

**Boundary candidates.** At \(Y=\pm1\), \(F=0\). At \(X=1\) the function is \(16(1-Y)^3(1+Y)(1+2Y)^2\), whose derivative is \(-32(Y-1)^2(2Y+1)(6Y^2+4Y-1)\). The two positive critical values are
\[D_\pm=\frac{9748\pm1360\sqrt{10}}{729}\quad\text{at}\quad Y=\frac{-2\pm\sqrt{10}}6,\]
respectively. The edge \(X=-1\) gives the same values by \((X,Y)\mapsto(-X,-Y)\).

**Interior candidates.** At a positive interior stationary point, the identity
\[\frac{\partial F}{\partial X}=-32(X-Y)(Y-1)(Y+1)(6XY+2Y^2+1)\]
forces \(Y\ne0\) and \(X=-(1+2Y^2)/(6Y)\). Substitution gives \(4(1-Y^2)(1+8Y^2)^3/(27Y^2)\). Its derivative must vanish because the partial derivative in \(X\) vanishes there. For \(s=Y^2>0\), the derivative in \(s\) is \(-4(1+8s)^2(24s^2-16s+1)/(27s^2)\). Thus \(Y^2=(4\pm\sqrt{10})/12\), and substitution gives \(D_\pm\) respectively. A global maximum exists on the square; the candidate list gives \(D_+\) as the maximum, attained already on the edge.

**Equality.** On \(X=1\), the positive maximizer has \(Y=\cos t_*\), giving the nodes \(1,e^{it_*},e^{-it_*}\). Reflection of the cosine pair \((X,Y)\mapsto(-X,-Y)\) can be realized by adding \(\pi\) to both angles \(u,v\), which leaves the nodes unchanged. For the interior maximizers \(Y^2=\cos^2(t_*/2)\), and the stationary equation gives \(X=4Y^3-3Y=\cos 3v\), so \(u\equiv\pm3v\pmod{2\pi}\). The nodes are then \(1,e^{2iv},e^{4iv}\) or their conjugates, with \(2v\equiv\pm t_*\pmod{2\pi}\). A common rotation moves the middle node to 1 and gives the same edge configuration. This exhausts the equality cases.

**Nonorthogonality.** Vanishing of an off-diagonal column inner product would require \(1+z+z^3=0\) with \(|z|=1\). Three unit numbers summing to zero and including 1 must be the three cube roots of unity. This would make \(z\) a primitive cube root, but then \(z^3=1\), a contradiction. Since each column has squared norm 3, a square tight analysis matrix would require orthogonal columns. The same obstruction prevents orthogonality of the exponential system (for example, the functions with integer index zero and different phases have an inner product containing this nonzero column factor and a nonzero integral over \([0,1)\)).

## Verification
The supporting `checker.py` uses NumPy and SymPy. It checks the derivative identities and candidate values symbolically. It tests the Gram determinants against the polynomial and the proposed bound for 2000 seeded samples, reports the largest numerical Gram eigenvalue-product discrepancy, tests five local perturbations, and checks the pointwise matrix norm identity underlying the fiber formula. The frozen `checker_output.txt` gives the recorded output of `python3 checker.py`. The samples do not prove the optimum or the equality classification; those are obtained by the compact-square proof.

## Relationship to prior work
Frederick and Okoudjou [1, Theorem 2.1] give the multittile finite-fiber characterization, and Frederick and Yacoubou Djima [2] give constructions and bounds. Lundengård, Österberg, and Silvestrov [3] give the generalized Vandermonde factorization for rows \(\{0,1,3\}\), but their sphere extremization uses real nodes with a Euclidean norm constraint. Dubickas and Pritsker [4] optimize weighted Vandermondes on the unit circle with one-point external-field weights; the factor \(|z_0+z_1+z_2|\) here depends jointly on all nodes. The claim is the unrestricted three-node maximum on the unit circle for this specific exponent set, and its full equality orbit in the multittile problem.

## Limitations
This is a determinant optimum for this exact multittile and the three integer-frequency cosets, not a claim about individual singular values, condition-number optimization, other multittiles, or arbitrary spectral sets. None of the cited computations establishes historical priority; less easily indexed exact unit-circle results may overlap.

## References
1. C. Frederick and K. A. Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles*, Applied and Computational Harmonic Analysis 51 (2021), 104–117, [arXiv:1910.09257](https://arxiv.org/abs/1910.09257).
2. C. Frederick and K. Yacoubou Djima, *Examples of Riesz Bases of Exponentials for Multi-tiling Domains and Their Duals*, La Matematica 3 (2024), 108–123, [DOI:10.1007/s44007-023-00078-7](https://doi.org/10.1007/s44007-023-00078-7).
3. K. Lundengård, J. Österberg, and S. Silvestrov, *Extreme points of the Vandermonde determinant on the sphere and some limits involving the generalized Vandermonde determinant*, [arXiv:1312.6193](https://arxiv.org/abs/1312.6193).
4. A. Dubickas and I. E. Pritsker, *Weighted Fekete points on the real line and the unit circle*, [arXiv:1902.08348](https://arxiv.org/abs/1902.08348).
