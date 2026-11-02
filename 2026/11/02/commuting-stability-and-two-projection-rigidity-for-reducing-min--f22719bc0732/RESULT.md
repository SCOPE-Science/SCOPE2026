# Commuting stability and two-projection rigidity for reducing-minimum operators

## Finding

Let \(H\) be a separable complex Hilbert space, and let \(\mathcal M_r^+(H)\) consist of the bounded positive operators whose restrictions to every nonzero reducing subspace attain their minimum modulus. The following three statements constitute one stability-and-obstruction theorem.

**Finite commuting calculus.** If \(A_1,\ldots,A_d\in\mathcal M_r^+(H)\) commute pairwise, \(d\) is finite, and \(F:[0,R]^d\to[0,\infty)\) is bounded, Borel measurable, and nondecreasing separately in each variable, where \(R\ge\max_i\|A_i\|\), then
\[
F(A_1,\ldots,A_d)\in\mathcal M_r^+(H).
\]
In particular, the class is closed under finite sums and products of commuting positive members and under nonnegative-coefficient multivariate polynomial calculus. No continuity of \(F\) is required.

**Exact two-projection boundary.** For any orthogonal projections \(P,Q\) on \(H\) and any \(0<t<1\), put \(A_t=tP+(1-t)Q\). The following are equivalent:
\[
A_t\in\mathcal M_r^+(H)
\quad\Longleftrightarrow\quad
\sigma(PQP)\text{ is finite}
\quad\Longleftrightarrow\quad
\sigma(A_t)\text{ is finite}
\quad\Longleftrightarrow\quad
C^*(I,P,Q)\text{ is finite-dimensional}.
\]
In particular, membership is independent of the choice of \(t\in(0,1)\). The finite-spectrum criterion is an exact condition on the pair, not a demand that \(P\) and \(Q\) commute.

**Infinitesimal obstruction.** On the separable space \(\ell^2(\mathbb N;\mathbb C^2)\), for every \(\varepsilon>0\) there exist projections \(P,Q\) such that
\[
0<\|P-Q\|<\varepsilon,
\qquad P-Q\in\bigcap_{p>0}\mathcal S_p,
\]
yet every \(A_t\), \(0<t<1\), is injective with minimum modulus zero. Consequently no such \(A_t\) is minimum attaining even on the whole space. The trace norm \(\|P-Q\|_{\mathcal S_1}\) and the norm of the commutator \([P,Q]\) can both be made arbitrarily small.

## Assumptions and scope

Throughout, the Hilbert space is complex and separable; infinite dimensionality is needed only for the counterexample. A reducing subspace means a closed subspace invariant under an operator and its adjoint. For a positive operator, attaining the minimum modulus means that its infimum of \(\|Ax\|\) over unit vectors is attained. The joint functional calculus is the bounded Borel calculus of a finite commuting self-adjoint family. \(\mathcal S_p\) denotes the Schatten ideal for \(p>0\), including its quasi-normed range \(0<p<1\).

The foundational spectral characterization used here is the following established theorem: a bounded positive operator on a separable Hilbert space belongs to \(\mathcal M_r^+\) if and only if it admits an orthogonal eigenbasis and its set of distinct eigenvalues is well ordered in the ordinary increasing order on the real line [1]. The present result concerns operations on such operators and the complete two-projection boundary; it does not reprove or claim the foundational characterization.

## Proof

**Step 1: finite products of spectral orders.** Let \(\Lambda_i\) be the well-ordered, countable eigenvalue set of \(A_i\). Pairwise commuting pure-point self-adjoint operators admit a common orthonormal eigenbasis: each eigenspace of the first operator reduces all remaining operators; repeat inside these eigenspaces. Thus every joint eigenvalue lies in \(J\subseteq\Lambda_1\times\cdots\times\Lambda_d\), and the values of \(F(A_1,\ldots,A_d)\) are precisely \(F(J)\).

Every infinite sequence in a well-ordered linear set has an infinite nondecreasing subsequence: recursively choose the least value occurring in each remaining infinite tail. Applying this extraction successively to each coordinate yields a subsequence of any infinite sequence in the finite product on which every coordinate is nondecreasing. If \(F(J)\) contained an infinite strictly decreasing sequence, representatives of its values in \(J\) would admit a coordinatewise nondecreasing subsequence, contradicting the separate monotonicity of \(F\). Hence \(F(J)\) is well ordered. It is countable because \(J\) is countable. The established spectral characterization [1] now proves the commuting-calculus assertion.

**Step 2: canonical two-projection decomposition.** Use the classical Halmos decomposition [2,3] into four commuting intersection pieces and a generic piece \(K\oplus K\). On the generic piece, for commuting positive contractions \(C,S\) with \(C^2+S^2=I\) and trivial kernels, the projections take the form
\[
P=\begin{pmatrix}I&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}C^2&CS\\CS&S^2\end{pmatrix}.
\]
The positive operator \(B=C^2\) has spectrum in \([0,1]\). The four intersection pieces contribute only the scalar values \(0,1,t,1-t\) to the spectrum of \(A_t\). On \(K\oplus K\), the spectral branches of \(A_t\), parametrized by \(x\in\sigma(B)\), are
\[
\lambda_{\pm}(x)=\frac{1\pm\sqrt{1-4t(1-t)(1-x)}}{2}.
\]
The branch \(\lambda_+\) is strictly increasing and \(\lambda_-\) is strictly decreasing in \(x\in[0,1]\). Also,
\[
A_t^2-A_t=-t(1-t)(P-Q)^2,
\qquad (P-Q)^2|_{K\oplus K}=(I-B)\oplus(I-B).
\]
Finally \(PQP|_{K\oplus K}=B\oplus0\); outside the generic piece, \(PQP\) has only the spectral values zero or one.

**Step 3: necessity and sufficiency.** If \(\sigma(B)\) is finite, the preceding canonical form makes \(\sigma(A_t)\) finite. Its positive finite-spectral functional calculus shows that the minimum on every reducing subspace is attained. Moreover, all functions of \(B\) involved in \(P,Q\) belong to the finite-dimensional span of its spectral projections; the generated unital \(C^*\)-algebra is finite-dimensional.

Conversely, suppose \(A_t\in\mathcal M_r^+(H)\). By [1], its restriction to the generic reducing piece has a complete eigenbasis and a well-ordered set of eigenvalues. Since \(B\oplus B\) is a polynomial in that restriction, \(B\) has an orthogonal eigenbasis. If \(B\) had infinitely many distinct eigenvalues, a strictly increasing or strictly decreasing infinite sequence of them could be selected. Each eigenvalue \(x\) of \(B\) produces *both* eigenvalues \(\lambda_+(x)\) and \(\lambda_-(x)\) of \(A_t\) on the corresponding two-dimensional fiber. A strictly increasing sequence of \(x\) produces strictly decreasing \(\lambda_-(x)\); a strictly decreasing sequence produces strictly decreasing \(\lambda_+(x)\). Either contradicts the well-order property. Thus \(\sigma(B)\) is finite. The formulas for \(PQP\) and the canonical algebra then give the claimed equivalences. If the generic space is zero, the argument reduces to the four scalar pieces.

**Step 4: quantitatively small counterexample.** Let \(\tau=\min\{\varepsilon/2,1/4\}\) and \(\theta_n=\tau2^{-n}\) for integers \(n\ge1\). On each copy of \(\mathbb C^2\), set
\[
P_n=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q_n=\begin{pmatrix}\cos^2\theta_n&\cos\theta_n\sin\theta_n\\\cos\theta_n\sin\theta_n&\sin^2\theta_n\end{pmatrix},
\]
and take their orthogonal direct sums. The eigenvalues of \(P_n-Q_n\) are \(\pm\sin\theta_n\), so
\[
\|P-Q\|=\sin(\tau/2)<\varepsilon,
\qquad \|P-Q\|_{\mathcal S_p}^p
=2\sum_{n\ge1}\sin^p\theta_n
\le\frac{2\tau^p}{2^p-1}<\infty
\]
for every fixed \(p>0\). In particular, \(\|P-Q\|_{\mathcal S_1}\le2\tau\), and \(\|[P,Q]\|\le\|P-Q\|\). The two positive eigenvalues of the \(n\)-th block of \(A_t\) are \(\lambda_\pm(\cos^2\theta_n)\). Its smaller eigenvalue is strictly positive for every \(n\), but tends to zero as \(n\to\infty\). Thus the direct-sum operator is injective and has unattained minimum modulus zero, simultaneously for every \(t\in(0,1)\).

## Verification

The standalone Python file `verify.py` checks exact rational \(2\times2\) projection matrices, the quadratic spectral and polynomial identities, and numerical monotonicity of the small spectral branch for finitely many geometric angles. Run with `python3 verify.py`; no third-party package is required. The finite checks are corroboration only: the infinite-dimensional assertions and Schatten bounds follow from the displayed analytic arguments.

## Relationship to prior work

Nag and Ramesh [1] introduced the reducing-minimum class and proved its positive spectral characterization. The commuting closure and projection-mixture classification proved here use that result as an input, not as a claimed contribution. Halmos' two-projection representation is classical [2]. Böttcher and Spitkovsky [3] provide exact norm-attainment criteria for general functions of two projections, but ordinary norm attainment does not entail minimum attainment on every reducing subspace; their criteria do not state the finite-angle-spectrum equivalence above. Klaja [4] studies spectra and numerical ranges of products of projections, without the present reducing-minimum criterion. The special case of a commuting pair is subsumed by the finite commuting calculus; the two-projection theorem identifies what survives without commutativity and what fails even under arbitrarily small Schatten perturbations.

## Limitations

The claims concern positive operators on separable complex Hilbert spaces, finite families in the joint monotone calculus, and convex mixtures of precisely two orthogonal projections. No assertion is made for infinitely many commuting factors, nonmonotone Borel functions, or arbitrary noncommuting positive pairs. The proof uses existing spectral characterization and projection decomposition theorems. Full publication priority remains subject to further historical comparison, including possible reformulations in the established two-projections and order-theoretic literature. Independent mathematical review has not been performed.

## References

[1] P. Nag and G. Ramesh, *Minimum attaining operators on reducing subspaces: Spectral structure and density*, arXiv:2608.19286, first submitted 2026-08-19, https://arxiv.org/abs/2608.19286.

[2] P. R. Halmos, *Two subspaces*, Transactions of the American Mathematical Society **144** (1969), 381–389.

[3] A. Böttcher and I. M. Spitkovsky, *The norm attainment problem for functions of projections*, Archiv der Mathematik **117** (2021), 397–403, https://doi.org/10.1007/s00013-021-01628-7.

[4] H. Klaja, *The numerical range and the spectrum of a product of two orthogonal projections*, Journal of Mathematical Analysis and Applications **411** (2014), 177–195, https://arxiv.org/abs/1212.1996.
