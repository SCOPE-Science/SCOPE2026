# Exact equitable-partition closure for coupled inverse-Gaussian subordinators

## Finding

Let \(B\) be a nonsingular \(d\times d\) \(M\)-matrix and \(\eta\in(0,\infty)^d\). Consider the multitype inverse-Gaussian subordinator \(Z^{B,\eta}\) with Laplace exponent \(\eta^{\mathsf T}z_B(u)\), where \(z_B(u)\in[0,\infty)^d\) is the unique solution of
\[
 B^{\mathsf T}z+\tfrac12 z^{\circ2}=u,\qquad u\in[0,\infty)^d.
\]
Fix a partition of its types into \(r\ge1\) nonempty classes and let \(P\in\{0,1\}^{d\times r}\) be the class-incidence matrix. The following are equivalent:

1. There is an \(r\times r\) nonsingular \(M\)-matrix \(C\), independent of \(\eta\), such that **for every** \(\eta\in(0,\infty)^d\) the aggregated subordinator \(P^{\mathsf T}Z^{B,\eta}\) has exactly the process law of \(Z^{C,P^{\mathsf T}\eta}\).
2. The partition is equitable for the transposed drift: \(B^{\mathsf T}P=PC^{\mathsf T}\). Equivalently, for every pair of classes \(\alpha,\beta\), the sum \(\sum_{j\in\beta}B_{ji}\) is constant over \(i\in\alpha\).

If these conditions hold, \(C\) is unique and automatically a nonsingular \(M\)-matrix. Thus type aggregation preserves **the entire correlated Lévy law**, not merely means or variances.

For a single class, the total mass \(\sum_i Z_i\) is an ordinary inverse-Gaussian subordinator with exponent
\[
(\sum_i\eta_i)(\sqrt{b^2+2u}-b)
\]
if and only if the column sums of \(B\) equal a common \(b>0\), under the same uniform-in-\(\eta\) interpretation. This includes genuinely coupled systems with non-inverse-Gaussian component margins.

## Assumptions and scope

A nonsingular \(M\)-matrix is a real matrix with nonpositive off-diagonal entries and entrywise nonnegative inverse. The reference family \(Z^{B,\eta}\) is the well-defined Lévy subordinator specified by the stated coupled quadratic Laplace equation (Wang--Xu--Zhu, 2026). Every class in \(P\) is nonempty; hence \(P\) has full column rank, \(P\mathbf1_r=\mathbf1_d\), and \((Pv)^{\circ2}=P(v^{\circ2})\). The equivalence requires the **same** reduced matrix \(C\) for **all** strictly positive immigration vectors; it does not characterize exceptional fixed-\(\eta\) coincidences. Equality means equality of all finite-dimensional laws for every \(t\ge0\); no pathwise coupling is asserted.

## Proof

**Sufficiency and admissibility.** Assume \(B^{\mathsf T}P=PC^{\mathsf T}\). Since \(B\) is invertible and \(P\) has full column rank, \(C\) is invertible. For distinct reduced classes \(\alpha\ne\beta\), the entry \(C_{\beta\alpha}\) equals a sum of entries \(B_{ji}\) with \(j\in\beta\), \(i\in\alpha\), so is nonpositive. Multiplying the intertwining identity by \(B^{-\mathsf T}\) and \(C^{-\mathsf T}\) gives \(B^{-\mathsf T}P=PC^{-\mathsf T}\). For a representative \(i\) in class \(\alpha\), each entry \((C^{-\mathsf T})_{\alpha\beta}\) equals \((B^{-\mathsf T}P)_{i\beta}\ge0\). Thus \(C^{-1}\ge0\) and \(C\) is a nonsingular \(M\)-matrix.

For arbitrary \(u\ge0\), let \(w=z_C(u)\). Then
\[
B^{\mathsf T}(Pw)+\tfrac12(Pw)^{\circ2}
=P(C^{\mathsf T}w+\tfrac12w^{\circ2})=Pu.
\]
By uniqueness of the nonnegative quadratic solution, \(z_B(Pu)=Pz_C(u)\). The Laplace transform of \(P^{\mathsf T}Z_t^{B,\eta}\) is consequently
\[
\exp\{-t\eta^{\mathsf T}z_B(Pu)\}
=\exp\{-t(P^{\mathsf T}\eta)^{\mathsf T}z_C(u)\}.
\]
Both objects are subordinators, so matching the time-homogeneous increment laws implies equality of all finite-dimensional distributions, and hence equality of their càdlàg-process laws.

**Necessity.** Conversely, assume the process-law equality for every \(\eta>0\) with one fixed reduced \(C\). Equating logarithms of one-time Laplace transforms yields
\[
\eta^{\mathsf T}\bigl(z_B(Pu)-Pz_C(u)\bigr)=0
\]
for all \(u\ge0\) and all strictly positive \(\eta\). Such vectors span \(\mathbb R^d\), so \(z_B(Pu)=Pz_C(u)\) for every nonnegative \(u\). At the origin the implicit-function theorem applies because the derivative of the defining equation in \(z\) is \(B^{\mathsf T}\), which is invertible. The one-sided derivatives are \(Dz_B(0)=B^{-\mathsf T}\) and \(Dz_C(0)=C^{-\mathsf T}\). Differentiation along nonnegative coordinate directions gives
\[
B^{-\mathsf T}P=PC^{-\mathsf T},
\]
which after multiplying by the invertible matrices is equivalent to \(B^{\mathsf T}P=PC^{\mathsf T}\). Full column rank of \(P\) ensures uniqueness of the quotient \(C\).

**Scalar specialization.** For \(r=1\), \(P=\mathbf1_d\) and \(C=(b)\). The intertwining equation is \(B^{\mathsf T}\mathbf1_d=b\mathbf1_d\), i.e. all column sums are \(b\). Because \(C\) is an invertible \(M\)-matrix, \(b>0\). The scalar quadratic equation has solution \(z_C(u)=\sqrt{b^2+2u}-b\).

**A coupled, nontrivial instance.** Take
\[
B=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad \eta=\begin{pmatrix}1\\1\end{pmatrix}.
\]
Both column sums equal one. Hence the sum is scalar inverse Gaussian with exponent \(2(\sqrt{1+2u}-1)\). Yet the exact unit-time covariance of the two coordinates is \(4/9>0\). The first marginal has cumulants \(\kappa_1=1\), \(\kappa_2=5/9\), \(\kappa_3=8/9\), whereas any scalar inverse-Gaussian law with those first two cumulants must have \(\kappa_3=3\kappa_2^2/\kappa_1=25/27\). Therefore even its marginal is not scalar inverse Gaussian. The aggregation phenomenon is not a restatement of the independent-coordinate diagonal case.

## Verification

The standalone `verify_ig_lumping.py` checks with exact SymPy rational arithmetic a four-type-to-two-type non-diagonal quotient, its nonnegative inverses, 16 separate quadratic-system substitutions, and a coupled two-type example's first three marginal cumulants and positive cross-covariance. It returns `PASS`. For the four-type example use
\[
B=\begin{pmatrix}3&-1&-1/2&0\\-1&3&0&-1/2\\-1/4&0&2&-1/2\\0&-1/4&-1/2&2\end{pmatrix},\quad
P=\begin{pmatrix}1&0\\1&0\\0&1\\0&1\end{pmatrix},\quad
C=\begin{pmatrix}2&-1/2\\-1/4&3/2\end{pmatrix}.
\]
All process-law and necessity statements follow from the analytical proof, not the finite verification cases.

## Relationship to prior work

Wang, Xu, and Zhu (arXiv:2610.10525, first posted 2026-10-07), especially Section 2 and the multitype quadratic uniqueness lemma in Section 4, define this new coupled inverse-Gaussian family and prove its Hawkes origin and diagonal independence. The present statement is an algebraic **if-and-only-if closure classification** for deterministic group aggregation, uniform over the immigration vector; it does not claim the defining quadratic equation or generic subordinator projection as novel. Achab et al. (arXiv:1607.06333) discuss integrated multivariate Hawkes covariance and identifiability, rather than full-law inverse-Gaussian lumpability. The equitable-partition intertwining principle itself is classical in other Markov and branching settings, and analogous hidden results are the chief originality risk.

## Limitations

The inverse statement is uniform over all strictly positive \(\eta\), not a fixed-parameter characterization. Class incidence cannot be replaced by arbitrary nonnegative weights because the componentwise square no longer commutes with the map. No finite-prelimit Hawkes equality, convergence rate, identification of \(B\) from one aggregate distribution, or independence between aggregated components is proved. The cited literature may implicitly contain an analogous intertwining corollary; this is not an independent certification of originality.

## References

1. Y. Wang, W. Xu, and L. Zhu, *A Hawkes Microfoundation for Multitype Inverse Gaussian Subordinators*, arXiv:2610.10525, first submitted 2026-10-07, especially Sections 2 and 4. https://arxiv.org/abs/2610.10525
2. M. Achab et al., *Uncovering Causality from Multivariate Hawkes Integrated Cumulants*, arXiv:1607.06333 (2016). https://arxiv.org/abs/1607.06333
3. L. Chaumont and R. Marolleau, *Fluctuation theory for spectrally positive additive Lévy fields*, arXiv:1912.10474 (2019), first-passage background; only abstract-level comparison made. https://arxiv.org/abs/1912.10474
