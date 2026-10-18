# Even-semiprime cyclotomic nodes and rational singular points in diagonal hyperplane sections

## Finding

Let \(p\ge3\) be an odd prime and \(N\ge5\). Over \(\mathbb Q\), define the projective hypersurface
\[
X_{p,N}=\left\{[x_1:\cdots:x_N]\in\mathbb P^{N-1}:\ \sum_{i=1}^N x_i=0,\quad \sum_{i=1}^N x_i^{2p+1}=0\right\}.
\]
The linear equation defines the ambient hyperplane, so \(\dim X_{p,N}=N-3\). The variety is geometrically integral and normal. Its singular scheme is finite etale over \(\mathbb Q\), and every geometric singular point is an ordinary quadratic double point.

For each nonnegative integer \(k\), set
\[
H_k(z)=\sum_{a\ge0}\frac{z^{2a+k}}{a!(a+k)!},\qquad
A_{p,N}=\frac{N!}{2p}[z^N]\left(H_0(z)^p+2\sum_{k=1}^{\lfloor N/p\rfloor}H_k(z)^p\right).
\]
Define
\[
R_{p,N}=\begin{cases}\frac12\binom N{N/2},&N\text{ even},\\0,&N\text{ odd},\end{cases}
\qquad Q_{p,N}=\frac{A_{p,N}-R_{p,N}}{p-1}.
\]
These are nonnegative integers. The entire **scheme-theoretic** singular locus is
\[
\boxed{\ \operatorname{Sing}(X_{p,N})\ \cong\
\coprod_{j=1}^{R_{p,N}}\operatorname{Spec}\mathbb Q\ 
\sqcup\ \coprod_{j=1}^{Q_{p,N}}\operatorname{Spec}\mathbb Q(\zeta_p).\ }
\]
In particular, the only possible residue degrees of singular closed points are \(1\) and \(p-1\), and \(X_{p,N}\) is smooth exactly when \(N\) is odd and \(N<p\). Unlike the prime-cyclotomic exponent case, even values of \(N\) produce rational ordinary double points.

There is also an exact permutation-orbit refinement. Under coordinate permutations, the number of orbits of geometric nodes is
\[
\boxed{\quad
O_{p,N}=\sum_{\substack{k\ge0\\N-pk\in2\mathbb Z_{\ge0}}}\frac1p\left[\binom{a+p-1}{p-1}+(p-1)\mathbf1_{p\mid a}\right],\qquad a=\frac{N-pk}{2}.
\quad}
\]
In this expression \(\mathbf1_{p\mid a}\) is one if \(p\) divides \(a\) and zero otherwise. The formula counts necklaces of the nonnegative integer multiplicities of antipodal root pairs.

Exact examples are:

| \(p\) | \(N\) | Geometric nodes \(A_{p,N}\) | Rational closed points \(R_{p,N}\) | Degree-\(p-1\) closed points \(Q_{p,N}\) | Permutation orbits \(O_{p,N}\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 5 | 60 | 0 | 30 | 1 |
| 3 | 6 | 340 | 10 | 165 | 5 |
| 3 | 7 | 1680 | 0 | 840 | 2 |
| 3 | 8 | 9135 | 35 | 4550 | 6 |
| 5 | 5 | 24 | 0 | 6 | 1 |
| 5 | 6 | 1090 | 10 | 270 | 7 |

## Assumptions and scope

Everything is in characteristic zero over \(\mathbb Q\) and its algebraic closure. The integer \(p\) is prime and odd; \(N\ge5\). The singular scheme is formed for the hypersurface inside its linear ambient hyperplane, rather than using the unconstrained ambient Jacobian of two equations without its rank condition. The phrase ordinary double point means a nondegenerate quadratic tangent cone in the \(N-2\) local coordinates of the ambient projective hyperplane. The asserted finite etale decomposition is over \(\mathbb Q\), not a claim about the singularities of reductions in positive characteristic.

## Proof

**1. Jacobian and roots.** On the hyperplane \(L=\sum_i x_i=0\), the differential of \(F=\sum_i x_i^{2p+1}\) vanishes precisely when its vector of partial derivatives is a scalar multiple of the differential of \(L\). Because \(2p+1\ne0\), this says all \(x_i^{2p}\) are equal. They cannot all be zero at a projective point, so each coordinate is nonzero. Scaling the common root gives a unique projective representative with \(x_1=1\) and every \(x_i\in\mu_{2p}\). For these representatives, \(F=\sum_i x_i^{2p+1}=\sum_i x_i=L=0\), so the sole remaining condition is a zero sum of \(2p\)-th roots of unity. This classification works scheme-theoretically once the nondegenerate Hessian below is established.

**2. Exactly which root multisets cancel.** Write the roots uniquely as \(+\zeta_p^j\) or \(-\zeta_p^j\), for \(0\le j<p\). Denote their multiplicities by \(c_j^+\) and \(c_j^-\). The sum vanishes exactly when
\[
\sum_{j=0}^{p-1}(c_j^+-c_j^-)\zeta_p^j=0.
\]
The minimal polynomial \(1+T+\cdots+T^{p-1}\) of \(\zeta_p\) shows that all the differences \(c_j^+-c_j^-\) equal one integer \(k\). Necessarily and sufficiently,
\[
c_j^+=a_j+\max(k,0),\quad c_j^-=a_j+\max(-k,0),\quad
\sum_j a_j=\frac{N-p|k|}{2},\quad a_j\in\mathbb Z_{\ge0}.
\]
Thus the allowable node lengths are exactly the integers \(N=2A+p|k|\), which also follow from the two-prime vanishing-sum framework of Lam and Leung. For \(N\ge5\), there is no solution exactly when \(N\) is odd and \(N<p\).

**3. Geometric counts.** For fixed integer \(k\) and fixed multiplicities \(a_j\), the ordered root list has
\[
\frac{N!}{\prod_{j=0}^{p-1}a_j!(a_j+|k|)!}
\]
possible orderings. Summing over all allowed \(k\) and \(a_j\) gives the numerator \(N![z^N](H_0^p+2\sum_{k\ge1}H_k^p)\). Multiplication of every coordinate by a root of unity acts freely on ordered lists, with orbit size \(2p\); projective points are exactly these orbits. Hence the displayed formula for \(A_{p,N}\).

**4. Rational points and Galois degrees.** Let \(K=\mathbb Q(\zeta_p)=\mathbb Q(\zeta_{2p})\). All projective singularities are \(K\)-rational. The Galois group is \((\mathbb Z/2p\mathbb Z)^\times\), acting by odd power maps. If a nonidentity automorphism corresponding to \(s\) fixes a projective node \([x_i]\), then \((x_i/x_1)^{s-1}=1\) for every \(i\). Since \(s\not\equiv1\pmod p\), one has \(\gcd(s-1,2p)=2\). All ratios must therefore be \(\pm1\). Conversely, such a projective point is rational. There are none for odd \(N\); for even \(N\), balanced lists of the signs have \(\frac12\binom N{N/2}\) projective classes. Every other singularity has trivial stabilizer in the Galois group and hence has residue field exactly \(K\), yielding \(Q_{p,N}\) components of residue degree \(p-1\).

**5. Nondegenerate quadratic singularities and reduced singular scheme.** On the affine projective chart \(x_1=1\), eliminate \(x_N=-1-\sum_{i=2}^{N-1}x_i\). At a singular configuration, the Hessian of \(F\) in the \(N-2\) independent coordinates is
\[
(2p+1)(2p)\left(\operatorname{diag}(x_2^{-1},\ldots,x_{N-1}^{-1})+x_N^{-1}\mathbf1\mathbf1^{\mathsf T}\right).
\]
The matrix determinant lemma and \(\sum_i x_i=0\) give its determinant exactly
\[
-\frac{((2p+1)(2p))^{N-2}}{\prod_{i=2}^N x_i}\ne0.
\]
Each singular point is consequently an ordinary quadratic double point, and the Jacobian ideal is reduced in its local ring. Since all singularities have been enumerated over the finite splitting field \(K\), the entire Jacobian singular scheme is finite, reduced and etale over \(\mathbb Q\). A hypersurface of dimension at least two with only isolated singularities is normal by Serre's criterion; its irreducibility follows because two positive-degree hypersurface components in the hyperplane would intersect in positive dimension, forcing nonisolated singularities. This proves geometric integrality and normality.

**6. Coordinate-permutation orbits.** Coordinate permutations preserve the multiplicities \((c_j^+,c_j^-)\). Scaling all roots by a \(p\)-th root cyclically rotates the index \(j\), while scaling by \(-1\) sends \(k\) to \(-k\). Thus for each \(|k|\), the permutation orbits correspond to length-\(p\) cyclic necklaces of \(a_0,\ldots,a_{p-1}\), where \(\sum a_j=(N-p|k|)/2\). Burnside's lemma counts these by \(p^{-1}\bigl(\binom{a+p-1}{p-1}+(p-1)\mathbf1_{p\mid a}\bigr)\), since any nonidentity rotation fixes exactly the constant composition when \(p\mid a\). Summing over the admissible \(|k|\) proves \(O_{p,N}\).

## Verification

The included standalone script `verify_nodes.py` uses only integer arithmetic and the Python standard library. Run `python verify_nodes.py`. It calculates the generating-function multinomial formula independently of direct root-list enumeration, normalizes the first root to one, tests exact cyclotomic cancellation by integer coefficient differences, identifies rational antipodal configurations, and computes permutation orbits by direct action. It checks \(p=3\) with \(N=5,6,7,8\) and \(p=5\) with \(N=5,6\); its successful completion prints `VERIFY_OK`. These are finite checks of the explicitly stated cases, not a substitute for the all-parameter proof.

## Relationship to prior work

Lam and Leung's 1995 preprint and subsequent paper establish the weight semigroup and two-prime cancellation structures for roots of unity. Those root-of-unity facts are not claimed as new. Lee's 2014 Fermat ED-degree work also studies counts of vanishing root sums, but for a different critical-point problem; it does not supply this hyperplane section's reduced singular scheme, rational/cyclotomic residue degrees, and symmetric-group orbit classification. General work on symmetric hypersurfaces by Cafure, Matera and Privitelli likewise addresses different defining families and singular-locus bounds. The proposed contribution is the combined exact arithmetic-geometric classification and orbit refinement for the even-semiprime exponent. The corresponding prime-exponent family is a distinct special case with no rational nodes; its known formulas do not imply these opposite-pair phases.

## Limitations

No assertion is made about the singular schemes of the hypersurface reductions in positive characteristic; these can have additional singularities. The ordinary quadratic normal form is over fields of characteristic zero. The count of coordinate-permutation orbits is not a classification of their stabilizer subgroups. While targeted literature and mathematical-record searches did not identify an equivalent all-parameter geometric statement, an implicit corollary of broader arithmetic or geometric literature could still cover the result.

## References

1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (13 November 1995), particularly Theorem 3.3 and Corollary 3.4; subsequently *Journal of Algebra* 224 (2000), 91–109.
2. Hwangrae Lee, *The Euclidean Distance Degree of Fermat Hypersurfaces*, arXiv:1409.0684v1 (2 September 2014), in particular Definition 2.1 and Theorem 2.2.
3. A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265v1 (10 September 2011), sections 3–4.
