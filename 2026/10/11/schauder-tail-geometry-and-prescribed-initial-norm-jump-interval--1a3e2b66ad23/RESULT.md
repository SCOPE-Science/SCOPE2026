# Schauder tail geometry and prescribed initial norm-jump intervals

## Finding
For an infinite Schauder decomposition of a complex Banach space, sufficiently separated diagonal decay scales make the short-time operator-norm defect recover exactly the asymptotic norms of the complementary partial-sum projections.

**Theorem.** Let \(X=\bigoplus_{n\ge1}X_n\), where each \(X_n\ne\{0\}\) is a closed subspace, and let \(P_n\) be the associated partial-sum projections, \(P_0=0\), and \(K=\sup_{n\ge1}\|P_n\|<\infty\). Suppose \(0<\lambda_1<\lambda_2<\cdots\) and \(\lambda_{n+1}/\lambda_n\to\infty\). Define
\[
T(0)=I,\qquad T(t)=\sum_{n\ge1}e^{-t\lambda_n}(P_n-P_{n-1})\quad(t>0).
\]
Then \(T\) is a bounded holomorphic \(C_0\)-semigroup with unbounded generator and
\[
\boxed{\limsup_{t\downarrow0}\|I-T(t)\|=\limsup_{n\to\infty}\|I-P_n\|.}
\]
For the canonical times \(t_n=(\lambda_n\lambda_{n+1})^{-1/2}\), a quantitative operator-norm cutoff estimate holds:
\[
\boxed{\|T(t_n)-P_n\|\le2K\left(\sqrt{\frac{\lambda_n}{\lambda_{n+1}}}+\exp\!\left[-\sqrt{\frac{\lambda_{n+1}}{\lambda_n}}\right]\right).}
\]
If all \(X_n\) are finite dimensional, the semigroup is immediately compact.

**Sharp realization.** For every \(c\in[1,2]\), one positive, contractive, exponentially stable and immediately compact holomorphic semigroup on the standard complex \(c_0\) has
\[
\liminf_{t\downarrow0}\|I-T(t)\|=1,\qquad
\limsup_{t\downarrow0}\|I-T(t)\|=c,
\]
and its full set of short-time norm-defect cluster values is precisely \([1,c]\). All these examples use the same superlacunary eigenvalue sequence \(\lambda_n=2^{2^n}\).

## Assumptions and scope
A Schauder decomposition means that each \(x\in X\) has a unique norm-convergent expansion \(x=\sum_{n\ge1}x_n\) with \(x_n\in X_n\). Consequently \(P_nx=\sum_{k\le n}x_k\) tends strongly to \(x\), and the projections are uniformly bounded. The scalar field is complex to state holomorphy without an additional complexification convention. The growth condition is \(\lambda_{n+1}/\lambda_n\to\infty\), not merely \(\lambda_n\to\infty\).

The positive assertion in the realization refers to the natural coordinate lattice order of \(c_0\). Its holomorphic extension is defined on the right half-plane; positivity is asserted for real \(t\ge0\). For a function \(F:(0,\infty)\to\mathbb R\), a cluster value at zero is a real limit of \(F(t_j)\) along some \(t_j\downarrow0\).

## Proof
**1. Construction and analytic control.** Write \(Q_n=P_n-P_{n-1}\) and \(a_n(z)=e^{-z\lambda_n}\). Abel summation gives, for \(\operatorname{Re}z>0\),
\[
T(z)=\sum_{n\ge1}(a_n(z)-a_{n+1}(z))P_n.
\]
The series converges in operator norm and satisfies
\[
\sum_{n\ge1}|a_n(z)-a_{n+1}(z)|
\le |z|\int_{\lambda_1}^{\infty}e^{-s\operatorname{Re}z}\,ds
=\frac{|z|}{\operatorname{Re}z}e^{-\lambda_1\operatorname{Re}z}.
\]
It is locally normally convergent on the right half-plane and uniformly bounded in any closed proper sector about the positive axis. Thus \(z\mapsto T(z)\) is holomorphic there. For real \(t>0\), its norm is at most \(Ke^{-t\lambda_1}\). Coordinatewise multiplication proves \(T(t+s)=T(t)T(s)\). The finite sums of decomposition vectors are dense, and on each such finite sum \(T(t)x\to x\) as \(t\downarrow0\). Uniform boundedness of \(T(t)\) transfers this convergence to all \(x\in X\). The generator restricts to the scalar \(-\lambda_n\) on each nonzero \(X_n\), hence is unbounded. If the blocks are finite dimensional, truncation at \(n=N\) leaves a tail with operator norm at most \(2Ke^{-t\lambda_{N+1}}\), proving immediate compactness.

**2. The general upper bound.** For real \(t>0\), put \(b_n(t)=1-e^{-t\lambda_n}\). These numbers increase from \(0\) toward \(1\) as \(n\to\infty\). The following norm-convergent identity follows by testing on each \(X_m\) and using density:
\[
I-T(t)=b_1(t)I+
\sum_{n\ge1}\bigl(b_{n+1}(t)-b_n(t)\bigr)(I-P_n).
\]
Every coefficient is nonnegative and their sum, including \(b_1(t)\), equals \(1\). Fix \(N\ge1\), let \(C_N=\max\{1,\max_{1\le n<N}\|I-P_n\|\}\), and set \(L_N=\sup_{n\ge N}\|I-P_n\|\). Splitting the convex combination yields
\[
\|I-T(t)\|\le b_N(t)C_N+(1-b_N(t))L_N.
\]
As \(t\downarrow0\), \(b_N(t)\to0\). Thus \(\limsup_{t\downarrow0}\|I-T(t)\|\le L_N\) for each \(N\), and letting \(N\to\infty\) gives the asserted upper bound.

**3. Exact cutoffs and the lower bound.** Define \(t_N=(\lambda_N\lambda_{N+1})^{-1/2}\). The hypothesis implies
\[
\lambda_Nt_N=\sqrt{\lambda_N/\lambda_{N+1}}\to0,
\qquad \lambda_{N+1}t_N=\sqrt{\lambda_{N+1}/\lambda_N}\to\infty.
\]
Separate \(T(t_N)-P_N\) into coordinates at most \(N\) and coordinates beyond \(N\). Abel summation for the low coefficients \(e^{-t_N\lambda_k}-1\) gives norm at most \(2K(1-e^{-t_N\lambda_N})\). The high-coefficient tail is at most \(2Ke^{-t_N\lambda_{N+1}}\). Therefore
\[
\|T(t_N)-P_N\|
\le2K\bigl(1-e^{-t_N\lambda_N}+e^{-t_N\lambda_{N+1}}\bigr)
\le2K\left(\sqrt{\lambda_N/\lambda_{N+1}}+e^{-\sqrt{\lambda_{N+1}/\lambda_N}}\right)\to0.
\]
The reverse triangle inequality shows that \(\big|\|I-T(t_N)\|-\|I-P_N\|\big|\to0\). Taking upper limits along \(N\) supplies the lower bound and completes the general equality.

**4. Every initial jump interval occurs on \(c_0\).** Fix \(c\in[1,2]\) and let \(\alpha=c-1\in[0,1]\). Identify standard complex \(c_0\) isometrically with the \(c_0\)-sum of copies of \((\mathbb C^2,\|\cdot\|_\infty)\). In block \(j\), use the ordered basis vectors \(u_j=(1,\alpha)\) and \(v_j=(0,1)\), enumerated \(u_1,v_1,u_2,v_2,\ldots\). For \((x,y)\) in one block, the odd partial sum maps it to \((x,\alpha x)\), a norm-one projection; even partial sums retain complete blocks. Hence every partial-sum projection has norm one. Its complement has norm \(1+\alpha=c\) after an odd index, and norm one after an even index. With \(\lambda_n=2^{2^n}\), the general formula already gives \(\limsup_{t\downarrow0}\|I-T(t)\|=c\).

For a direct endpoint analysis, let \(a_j(t)=e^{-t\lambda_{2j-1}}\) and \(d_j(t)=e^{-t\lambda_{2j}}\), with \(0<d_j(t)\le a_j(t)\). In standard block coordinates the multiplier matrix is exactly
\[
T_j(t)=\begin{pmatrix}
a_j(t)&0\\
\alpha(a_j(t)-d_j(t))&d_j(t)
\end{pmatrix}.
\]
Its entries are nonnegative. Since the maximum row sum is exactly \(a_j(t)\) for \(0\le\alpha\le1\), every \(T(t)\) is positive and contractive, with \(\|T(t)\|=\sup_j a_j(t)=e^{-4t}\). Each positive-time operator is compact, by the finite-block tail estimate from Step 1. For the defect, the exact norm is
\[
F_\alpha(t):=\|I-T(t)\|
=\sup_{j\ge1}\left\{1-d_j(t)+\alpha\bigl(a_j(t)-d_j(t)\bigr)\right\}.
\]
It obeys \(1\le F_\alpha(t)\le1+\alpha\) because the displayed block expression tends to \(1\) as \(j\to\infty\).

At the odd-index gaps \(t_{2j-1}\), one has \(a_j(t_{2j-1})\to1\) and \(d_j(t_{2j-1})\to0\), so \(F_\alpha(t_{2j-1})\to1+\alpha=c\). At the even-index gaps \(t_{2j}\), every block \(k\le j\) has a defect bounded by \((1+\alpha)\lambda_{2j}t_{2j}\to0\), whereas for every \(k\ge j+1\) the displayed expression is at most \(1+\alpha e^{-\lambda_{2j+1}t_{2j}}\to1\). Since always \(F_\alpha(t)\ge1\), this proves \(F_\alpha(t_{2j})\to1\). The analytic semigroup is norm-continuous on \((0,\infty)\), so the intermediate value theorem implies that all values between these two limiting endpoints, and no others, are attained as cluster values at zero. The exact cluster set is \([1,c]\), including both boundary cases \(c=1\) and \(c=2\).

## Verification
The key identities can be checked without a numerical approximation: the coefficient of \(Q_m\) in the convex-combination identity is exactly \(b_m(t)\), and the explicit block matrix is conjugate to the diagonal matrix with eigenvalues \(a_j(t)\), \(d_j(t)\) by the change-of-basis matrix with columns \(u_j,v_j\). Row-sum norms verify positivity, contractivity, and the exact defect expression. A supplementary finite-scale calculation for \(\alpha=0.65\) and \(\lambda_n=2^{2^n}\) yields defect values approximately \(1.610618\) at the gap following index \(3\), \(1.649990\) at the gap following index \(5\), and \(1.650000\) at the gap following index \(7\); the even-index gap values are \(1\) to the displayed precision for indices \(4,6,8\). The analytic proof, not these finite calculations, establishes all infinite-dimensional statements.

## Relationship to prior work
Araújo, Azevedo, Bezerra and Barbosa use diagonal Schauder-decomposition semigroups to establish a qualitative failure of the Lotz property for spaces with a Schauder decomposition. Their construction does not compute the short-time operator-norm defect, identify its exact projection-geometric coefficient, or produce the continuum of norm-jump cluster sets. Fackler proves the holomorphic-semigroup generation theorem for increasing positive Schauder multipliers and explores conditional bases through maximal-regularity obstructions, but does not state the spectral-cutoff norm law or the immediately compact positive contraction examples above. The 2026 diagonal \(C_0\)-semigroup literature using \(q\)-Riesz bases is limited by its unconditional coordinate geometry; it does not imply the conditional monotone-basis realization. Standard Abel summation is the computational ingredient, not a claimed new technique.

## Limitations
The general exact equality uses the superlacunary ratio condition; no claim is made for arbitrary increasing spectra, arbitrary positive semigroups, or arbitrary \(C_0\)-semigroups. The interval realization asserts existence for every \(c\in[1,2]\), not that all semigroup classes have only such intervals. The generator is unbounded; the semigroup is strongly continuous at zero but not norm-continuous there. Positivity applies for real time. Although the main primary results and relevant supporting sections were inspected, an older general spectral-cutoff principle could conceivably contain an implicit equivalent formulation; that originality risk is not eliminated by search alone.

## References
1. G. Araújo, M. Azevedo, F. Bezerra and A. Barbosa, *The Lotz Property in Weakly Compactly Generated Spaces*, arXiv:2609.38396v1 (public September 29, 2026), especially Proposition 2.4 and its proof.
2. S. Fackler, *The Kalton–Lancien Theorem Revisited: Maximal Regularity Does Not Extrapolate*, arXiv:1210.4333v2, especially Theorem 2.4 and Section 4.
3. *Laplace–Carleson embeddings and infinity-norm admissibility*, *Analysis and Mathematical Physics* (2026), DOI:10.1007/s13324-026-01203-9, especially Section 3.2.
