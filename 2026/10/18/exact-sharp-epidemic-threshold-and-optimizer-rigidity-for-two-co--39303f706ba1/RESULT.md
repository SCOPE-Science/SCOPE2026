# Exact sharp epidemic threshold and optimizer rigidity for two contact-rate classes

## Finding

**Theorem (two-rate reciprocal mixing).** Fix any integer \(n\ge 3\), a partition of the \(n\) types into nonempty classes \(A,B\), and strictly positive fractions \(\pi_1,\ldots,\pi_n\) with \(\sum_i\pi_i=1\). Set \(P=\sum_{i\in A}\pi_i\) and \(Q=1-P\). Let \(a,b>0\) be the prescribed total contact rates in the two classes. Among **all** nonnegative \(n\times n\) next-generation matrices \(M\) with row sums \(a\) in \(A\), \(b\) in \(B\), and reciprocity \(\pi_iM_{ij}=\pi_jM_{ji}\), the exact minimum basic reproduction number is

\[
\boxed{\rho_{\min}=\frac12\left[a+b-t_*(P^{-1}+Q^{-1})+\sqrt{\left(a-b-t_*(P^{-1}-Q^{-1})\right)^2+\frac{4t_*^2}{PQ}}\right],\quad t_*=\min\{Pa,Qb\}.}
\]

This minimum is **attained by an irreducible** admissible matrix for every admissible choice of parameters and of the individual fractions. If \(a\ne b\), an admissible \(M\) attains it **if and only if** its total rate of transitions to the other class is constant within each rate class:

\[
\sum_{j\in B}M_{ij}=t_*/P\quad(i\in A),\qquad
\sum_{i\in A}M_{ji}=t_*/Q\quad(j\in B).
\]

Thus every optimizer is lumpable with respect to the two rate classes, even though no lumpability was assumed. The detailed arrangement of within-class edges and of reciprocal edges between individuals does not affect the optimum once these classwise rates and the original constraints hold. If \(a=b\), every admissible matrix has spectral radius \(a\).

A useful threshold consequence is exact: a reciprocal mixing pattern with \(\rho(M)\le1\) exists if and only if \(\rho_{\min}\le1\). In particular, fine subdivision of either rate class cannot improve upon the sharp two-class threshold.

## Assumptions and scope

Entries \(M_{ij}\) are allowed to vanish and the diagonal may be nonzero. No within-class topology, assortativity, or equality of population fractions is assumed. Reciprocity uses the community fractions themselves, not an unweighted symmetry assumption. The Perron root \(\rho(M)\) is the spectral radius of the nonnegative matrix. The class sizes may be arbitrary positive integers. For the genuinely multitype extension, \(n\ge3\); the two-type case is previously known.

All quantified matrices have exactly the prescribed row sums and satisfy reciprocity. The proof also establishes the result for reducible matrices; the explicit minimizing construction is irreducible. It does not determine epidemic final-size extrema or cover heterogeneous individual rates taking more than two values.

## Proof

**1. Self-adjoint reduction.** Introduce the positive weighted inner product \(\langle f,g\rangle_\pi=\sum_i\pi_i f_i g_i\). Detailed balance makes \(M\) self-adjoint for this inner product. Equivalently, \(D_\pi^{1/2}M D_\pi^{-1/2}\) is symmetric and nonnegative. Its largest eigenvalue equals \(\rho(M)\) by Perron--Frobenius. Hence
\[
\rho(M)=\max_{f\ne0}\frac{\langle f,Mf\rangle_\pi}{\langle f,f\rangle_\pi}.
\]

**2. Exact two-dimensional compression.** Define the total reciprocal cross-class contact flux
\[
t=\sum_{i\in A}\sum_{j\in B}\pi_i M_{ij}=\sum_{j\in B}\sum_{i\in A}\pi_j M_{ji}.
\]
Nonnegativity and prescribed row totals imply \(0\le t\le\min\{Pa,Qb\}=t_*\). On the subspace of vectors equal to \(x\) on \(A\) and \(y\) on \(B\), expanding the quadratic form with reciprocity gives the **identity**
\[
\frac{\langle f,Mf\rangle_\pi}{\langle f,f\rangle_\pi}
=\frac{Pa x^2+Qb y^2-t(x-y)^2}{Px^2+Qy^2}.
\]
Its maximization over \(x,y\) is the largest eigenvalue \(L(t)\) of the symmetric matrix
\[
H(t)=\begin{pmatrix}a-t/P&t/\sqrt{PQ}\\t/\sqrt{PQ}&b-t/Q\end{pmatrix}
=\begin{pmatrix}a&0\\0&b\end{pmatrix}
-t\begin{pmatrix}P^{-1/2}\\-Q^{-1/2}\end{pmatrix}
\begin{pmatrix}P^{-1/2}&-Q^{-1/2}\end{pmatrix}.
\]
In particular \(\rho(M)\ge L(t)\).

**3. Strict monotonicity and optimal flux.** Since \(H(t)\) decreases in Loewner order with \(t\), \(L(t)\) is nonincreasing. For \(a\ne b\), it is strictly decreasing on \([0,t_*]\): if \(t_2>t_1\) and equality held, a top eigenvector at \(t_2\) would be orthogonal to \((P^{-1/2},-Q^{-1/2})\), making it a common eigenvector of the rank-one perturbation and \(\operatorname{diag}(a,b)\). Their only such nonzero candidate has both coordinates nonzero, impossible when \(a\ne b\). Thus \(\rho(M)\ge L(t)\ge L(t_*)\). The explicit quadratic formula for the larger eigenvalue of \(H(t_*)\) is precisely the displayed \(\rho_{\min}\). For \(a=b\), \(M\mathbf 1=a\mathbf1\) and its constant row sum directly gives \(\rho(M)=a\).

**4. Sharpness and irreducibility.** Let \(u=t_*/P\) and \(v=t_*/Q\). Define \(M^*\) by
\[
M^*_{ii}=a-u\ (i\in A),\qquad M^*_{jj}=b-v\ (j\in B),
\]
\[
M^*_{ij}=u\pi_j/Q\ (i\in A,j\in B),\qquad
M^*_{ji}=v\pi_i/P\ (j\in B,i\in A),
\]
and set all other within-class off-diagonal entries to zero. Since \(u\le a\), \(v\le b\), all entries are nonnegative. Every cross-class entry is strictly positive, so \(M^*\) is irreducible. Row sums and reciprocity hold exactly because \(\pi_i u\pi_j/Q=\pi_j v\pi_i/P\), using \(Pu=Qv=t_*\). Each class is equitable, with quotient \(\bigl(\begin{smallmatrix}a-u&u\\v&b-v\end{smallmatrix}\bigr)\); its positive Perron eigenvector lifts to an everywhere-positive eigenvector of \(M^*\), with eigenvalue \(L(t_*)\). By Perron--Frobenius, \(\rho(M^*)=L(t_*)\), establishing the bound's attainment.

**5. Classification of all minimizers.** Assume \(a\ne b\) and \(\rho(M)=L(t_*)\). Strict monotonicity forces \(t=t_*\). Let \(f\) be the positive Perron eigenvector of \(H(t_*)\), lifted to constants \(x>0\) on \(A\), \(y>0\) on \(B\). Necessarily \(x\ne y\): otherwise the quotient's row sums \(a,b\) would agree. The Rayleigh quotient of \(f\) for \(M\) equals its top eigenvalue, so self-adjointness requires \(Mf=L(t_*)f\). For \(i\in A\), this reads
\[
a x+(y-x)\sum_{j\in B}M_{ij}=L(t_*)x.
\]
As \(y-x\ne0\), its cross-class row sum is independent of \(i\). Averaging with weights \(\pi_i\) identifies it as \(t_*/P\). The same reasoning on \(B\) gives \(t_*/Q\). Conversely these two constant cross-class row sums make the lifted positive quotient Perron vector an eigenvector of every such \(M\). An everywhere-positive eigenvector of a nonnegative matrix identifies the spectral radius, proving sufficiency. This proves the complete optimizer characterization without assuming within-class symmetry or uniform individual fractions.

**6. Concrete four-type threshold witness.** For population fractions \(\pi=(1/20,1/10,1/10,3/4)\), with class \(A=\{1,2,3\}\), \(B=\{4\}\), and \(a=8/5\), \(b=2/5\), one obtains \(t_*=3/10\), and
\[
M^*=\begin{pmatrix}
2/5&0&0&6/5\\0&2/5&0&6/5\\0&0&2/5&6/5\\2/25&4/25&4/25&0
\end{pmatrix}.
\]
Its quotient is \(\bigl(\begin{smallmatrix}2/5&6/5\\2/5&0\end{smallmatrix}\bigr)\), so \(\rho(M^*)=(1+\sqrt{13})/5<1\), despite the larger class rate being \(8/5>1\). All row sums and detailed-balance identities hold as exact rational equalities.

## Verification

Run `python3 checks/verify.py` in the package root. It uses only the Python standard library. The script checks exact rational reciprocity, row totals and the four-type example, then checks the explicit extremal eigenvalue against a symmetric-matrix Jacobi calculation. It also compares the proposed minimum with 140 sampled feasible reciprocal matrices for each of three additional parameter regimes (420 comparisons total). These numerical comparisons are finite tests, **not** a proof of the quantified inequality or of completeness; the algebraic argument above is the proof.

## Relationship to prior work

Bizzotto, Ball and Britton (2026, arXiv:2602.23885v2) establish an exact numerical semidefinite optimization formulation for an arbitrary number of reciprocal contact types; for two types their Theorem 3.6 gives an explicit sharp lower reproduction-number bound. Their Theorem 3.2 supplies a more general but generally nonsharp analytical bound for many types. This finding is **not** a claim that the original general optimization is unsolved: it evaluates a natural, genuinely multitype two-rate stratum **in closed form**, proves attainment by an irreducible matrix with no symmetry imposed, and characterizes **every** multitype optimizer by obligatory class-lumpability. The two-type eigenvalue formula and reversible-Rayleigh machinery are prior tools; the general-stratum reduction and equality characterization are the specific proposed contribution.

Britton and Ball (arXiv:2408.07298, first public 2024-07-30) motivate fine stratification of social-contact studies into activity groups. Such refinement can introduce numerous types even when measured total contact rates take only two distinct values. Classical equitable-partition/coarse-graining theory provides background for lumpable matrices; here lumpability is forced **at every global minimizer** despite not being an admissibility constraint.

## Limitations

The mathematical optimization includes self-contact diagonal entries. A requirement of zero diagonal or a specified absent-edge topology can invalidate the explicit formula; the theorem makes no claim for such restrictions. When entrywise positivity is imposed, the displayed optimum may have zero entries, but positive detailed-balanced feasible matrices can approach it by convex mixture with the everywhere-positive reciprocal matrix \(M_{ij}=r_i r_j\pi_j/(Pa+Qb)\); thus the infimum is unchanged. The result concerns the next-generation spectral threshold, not realized outbreak prevalence, stochastic extinction probability, or final epidemic sizes. Historical priority beyond the inspected literature requires independent assessment, particularly because the known arbitrary-type semidefinite program already implicitly covers this subfamily.

## References

1. Andrea Bizzotto, Frank Ball, Tom Britton, *Bounds on \(R_0\) and final epidemic size when the next-generation matrix \(M\) is only partially known*, arXiv:2602.23885v1 (2026-02-27), v2 (2026-03-09). https://arxiv.org/html/2602.23885v2
2. Tom Britton and Frank Ball, *Improving the use of social contact studies in epidemic modelling*, arXiv:2408.07298v1 (2024-07-30); later in *Epidemiology* (2025). https://arxiv.org/abs/2408.07298
3. N. O'Clery, Y. Yuan, G.-B. Stan, M. Barahona, *Observability and coarse graining of consensus dynamics through the external equitable partition*, *Physical Review E* **88**, 042805 (2013). https://doi.org/10.1103/PhysRevE.88.042805
