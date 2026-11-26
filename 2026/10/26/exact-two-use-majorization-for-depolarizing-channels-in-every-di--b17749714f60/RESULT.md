# Exact two-use majorization for the negative depolarizing coefficient in dimension at least three

## Finding

Let \(d\ge3\) and \(1<p\le d^2/(d^2-1)\). For the depolarizing channel on \(d\)-dimensional matrices
\[
\mathcal D_{p,d}(X)=(1-p)X+(p/d)\operatorname{Tr}(X)I_d,
\qquad \tau=\mathcal D_{p,d}(|0\rangle\langle0|),
\]
and every density operator \(\rho\) on \(\mathbb C^d\otimes\mathbb C^d\),
\[
\lambda^\downarrow\!\left((\mathcal D_{p,d}\otimes\mathcal D_{p,d})(\rho)\right)
\prec \lambda^\downarrow(\tau\otimes\tau).
\]
Thus a pure product input simultaneously maximizes every Ky Fan output sum for two identical uses throughout the negative-coefficient physical branch in local dimension at least three, including its complete-positivity endpoint.

## Assumptions and scope

Here \(x\prec y\) means that all partial sums of the decreasing rearrangements of \(x,y\) satisfy the inequality in that order, with equal total sum. Let \(c=p-1\), \(b=p/d\), and \(\alpha=b-c\). The range is \(0<c\le 1/(d^2-1)\), so \(c/b\le1/d\) and \(0<\alpha<b\). The spectrum of \(\tau\otimes\tau\) in decreasing order consists of \((d-1)^2\) copies of \(b^2\), \(2d-2\) copies of \(\alpha b\), and one copy of \(\alpha^2\). The theorem compares two identical channels, not unequal channels or three or more uses.

## Proof

First take a pure input. By local unitary covariance we may write its state vector as \(|\psi\rangle=\sum_i\sqrt{\lambda_i}|ii\rangle\), where \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\). Write \(v_i=\sqrt{\lambda_i}\), \(\Lambda=\operatorname{diag}(\lambda)\), and \(T=\Lambda\otimes I+I\otimes\Lambda\). The output is
\[
Z=b^2 I-bcT+c^2|\psi\rangle\langle\psi|.
\]
On the subspace spanned by the vectors \(|ii\rangle\) it is \(b^2I-2bc\Lambda+c^2vv^*\). On each \(|ij\rangle\), \(i\ne j\), its eigenvalue is \(b^2-bc(\lambda_i+\lambda_j)\ge\alpha b\).

The following Gram identity bounds the diagonal block from below:
\[
I+vv^*-2\Lambda
=\sum_{i<j}(\sqrt{\lambda_j}e_i+\sqrt{\lambda_i}e_j)
(\sqrt{\lambda_j}e_i+\sqrt{\lambda_i}e_j)^*\succeq0.
\]
Indeed its diagonal entries are \(1-\lambda_i\) and off-diagonal entries are \(\sqrt{\lambda_i\lambda_j}\). Hence the diagonal block is at least \(\alpha b I-c\alpha vv^*\) in Loewner order. The comparison matrix has eigenvalue \(\alpha^2\) along \(v\) and \(\alpha b\) on its orthogonal complement. The eigenvalue variational principle and the off-diagonal estimates imply that the smallest eigenvalue of \(Z\) is at least \(\alpha^2\) and all but possibly this smallest one are at least \(\alpha b\).

For an upper bound, for any vector \(u=(u_{ij})\) Cauchy–Schwarz gives
\[
|\langle\psi,u\rangle|^2\le d\sum_i\lambda_i|u_{ii}|^2\le (d/2)\langle u,Tu\rangle.
\]
Thus \(Z-b^2I\preceq(-bc+dc^2/2)T\preceq0\), using \(T\succeq0\) and \(c/b\le1/d\). Consequently for \(1\le k\le(d-1)^2\) the largest \(k\) eigenvalues sum to at most \(kb^2\). For \((d-1)^2<k<d^2\), let \(m=d^2-k\). The smallest \(m\) eigenvalues sum to at least \(\alpha^2+(m-1)\alpha b\); subtract from the trace of one. These are exactly the bounds of the pure-product Lorenz curve. Equality of the total traces holds at \(k=d^2\).

Finally decompose a mixed input into pure states. The sum of the largest \(k\) eigenvalues is convex, by its variational formula as the maximum of \(\operatorname{Tr}(PZ)\) over rank-\(k\) orthogonal projections. Linearity of the channel then extends each inequality to the mixed input. A pure product attains the reference spectrum.

## Reproducibility and limitations

The argument uses only the exact block and Gram identities, elementary operator inequalities, and the Ky Fan variational formula. The accompanying numerical verifier also exercises a larger parameter range and checks exact rational Gram examples; only the negative-branch comparisons in dimensions at least three are part of this finding. Finite tests do not certify the all-input, all-dimension theorem. No statement is made beyond the completely positive interval or about historical priority outside the cited and inspected literature.

## Relationship to prior work

Song, Wang, Tomamichel, and Fang [1] state the full majorization conjecture at arbitrary copy number and prove shifted log-determinant ordering and approximate majorization. Version 2 explicitly credits Fujiwara and Hashizumé [2] with the exact two-use order for \(0\le p\le1\). That positive-coefficient result is not claimed here; the exact boundaries of the available comparison to [2] are based on the attribution in [1], not direct inspection of the older full text. For qubits, changing the sign of the depolarizing coefficient also preserves each two-use output spectrum: with \(R(X)=\operatorname{Tr}(X)I_2-X=\sigma_y X^{\mathsf T}\sigma_y\), composing a qubit depolarizing map with \(R\) reverses its coefficient, and \(R\otimes R\) is full transpose conjugated by \(\sigma_y\otimes\sigma_y\). This argument likewise preserves the reference spectrum, so the physical negative qubit case follows from the credited nonnegative qubit case. This dimension-two reduction does not apply to the higher-dimensional claim above.

King [3] treats the full physical range for output norm and entropy optimization; these inequalities do not themselves order every Ky Fan sum. Lami and Huber [4] study positivity and entanglement annihilation for a wider family of bipartite maps. The contribution here is the exact order of *all* spectral partial sums on the negative branch for \(d\ge3\): the reference has its long plateau at the top of the spectrum, and the two-sided operator estimates above yield the required high and low spectral bounds in that ordering.

## References

1. Z. Song, X. Wang, M. Tomamichel and K. Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, [arXiv:2609.37240v2](https://arxiv.org/abs/2609.37240v2), Introduction, Eq. (2) and discussion of the two-use case.
2. A. Fujiwara and T. Hashizumé, *Additivity of the capacity of depolarizing channels*, Physics Letters A **299** (2002), 469–475.
3. C. King, *The capacity of the quantum depolarizing channel*, [arXiv:quant-ph/0204172](https://arxiv.org/abs/quant-ph/0204172).
4. L. Lami and M. Huber, *Bipartite depolarizing maps*, [arXiv:1603.02158](https://arxiv.org/abs/1603.02158).
