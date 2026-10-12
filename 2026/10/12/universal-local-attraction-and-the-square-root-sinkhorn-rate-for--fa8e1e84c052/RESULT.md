# Universal local attraction and the square-root Sinkhorn rate for Bregman Douglas–Rachford matrix scaling

## Finding

**Theorem (exact local spectral law).** Let \(m,n\geq1\), let \(M\in(0,\infty)^{m\times n}\), and let \(r\in(0,\infty)^m\) and \(c\in(0,\infty)^n\) satisfy \(\sum_i r_i=\sum_j c_j=1\). All vector products, divisions, and squares below are coordinatewise. Define the positive Sinkhorn map
\[
S_M(q)=\frac{c}{M^{\mathsf T}(r/(Mq))},\qquad q>0.
\]
Let \(q_*\) be its positive fixed point (unique up to scaling), put \(p_*=r/(Mq_*)\), and set
\[
P=\operatorname{diag}(p_*)M\operatorname{diag}(q_*),\qquad
W=\operatorname{diag}(r)^{-1/2}P\operatorname{diag}(c)^{-1/2}.
\]
Let \(s_2\) be the second largest singular value of \(W\), with \(s_2=0\) when \(W\) has only one column. Consider the two-step *cumulative-column* Bregman Douglas–Rachford scaling recurrence
\[
q^{k+1}=S_M\!\left(\frac{(q^k)^2}{q^{k-1}}\right),\qquad k\geq1.
\]
It is the recurrence of the matrix-scaling algorithm in Ma (2026); the dynamic is considered on positive **projective** column vectors, so each \(q^k\) is identified under multiplication by an arbitrary positive scalar.

The projective equilibrium \(([q_*],[q_*])\) is locally exponentially attracting **for every such positive matrix**, irrespective of its cross-ratio/projective diameter. More precisely, \(0\leq s_2<1\), its projective two-step Jacobian has spectral radius exactly \(s_2\), and for every \(\rho\) with \(s_2<\rho<1\), there are a neighborhood and a constant \(C_\rho\) such that sufficiently nearby initialized trajectories obey
\[
\left\| (e^{k-1},e^k)\right\|\leq C_\rho\rho^k
\left\|(e^0,e^1)\right\|,\qquad k\geq1,
\]
where \(e^k\) is the coordinatewise logarithmic error \(\log(q^k/q_*)\) with its \(c\)-weighted mean subtracted, and any fixed finite-dimensional norm may be used. The corresponding column-feasible matrices reconstructed by the BDRS multiplicative iteration also converge locally to \(P\) at every rate \(\rho>s_2\).

When \(s_2>0\), no smaller rate is valid as a **uniform local linearized bound**, either for the two-step projective state or for the reconstructed matrix output. Ordinary Sinkhorn scaling has exact projective Jacobian spectral radius \(s_2^2\); thus the BDRS local rate is its square root, not an improvement. For the explicit positive family
\[
M_t=\begin{pmatrix}t&1\\1&t\end{pmatrix},\qquad
r=c=(1/2,1/2)^{\mathsf T},\qquad t>1,
\]
these two radii are respectively \((t-1)/(t+1)\) and \(((t-1)/(t+1))^2\). In particular the BDRS rate can approach one from below, even though its equilibrium remains locally attractive. The theorem is strictly local and makes **no global convergence assertion**.

## Assumptions and scope

The matrix and every marginal component must be strictly positive; the two marginal vectors have equal total mass normalized to one. The dynamics are exact-arithmetic projective recurrences, not finite-precision implementations. The initialization consists of two consecutive cumulative column factors near the fixed projective class, not an arbitrary distant start. A BDRS matrix-scaling orbit produces this recurrence after its initial update. The result neither asserts that all allowed initial conditions lie in the local basin nor implies that any globally nonconvergent orbit is impossible.

The weighted-centered error subspace is
\[
E=\{h\in\mathbb R^n:\sum_jc_jh_j=0\}.
\]
It is a coordinate chart for the positive projective cone near \([q_*]\). When \(n=1\), this space is zero-dimensional and the projective assertion is immediate. When \(\operatorname{rank}(M)=1\), the Sinkhorn projective map is constant, and projective settling is finite-step; the displayed local spectral radius is then zero.

## Proof

**1. Reduction from multiplicative scaling.** The BDRS matrix-scaling steps are
\[
u^k=\frac{r}{X^kv^{k-1}},\quad v^k=\frac{c}{(X^k)^{\mathsf T}u^k},\quad X^{k+1}=\operatorname{diag}(u^k)X^k\operatorname{diag}(v^k).
\]
Writing \(X^k=\operatorname{diag}(p^k)M\operatorname{diag}(q^k)\) for cumulative row and column factors gives \(q^{k+1}=q^k\odot v^k\), and the row update yields
\[
p^{k+1}=\frac{r}{M(q^k\odot v^{k-1})}.
\]
For \(k\geq1\), \(v^{k-1}=q^k/q^{k-1}\); the ensuing column update is exactly the stated two-step recurrence. The reconstructed coupling is
\[
X^{k+1}=\operatorname{diag}\!\left(\frac{r}{My^k}\right)M\operatorname{diag}(S_M(y^k)),
\quad y^k=\frac{(q^k)^2}{q^{k-1}}.
\]
It has column sums \(c\) exactly, and the reconstruction is invariant if \(y^k\) is rescaled. The formula works in any local projective coordinate representatives.

**2. Exact derivative of the Sinkhorn map.** Differentiate in logarithmic coordinates at \(q_*\). Define \(A=\operatorname{diag}(r)^{-1}P\), so \(A\) is row-stochastic. The row scaling \(r/(Mq)\) has logarithmic derivative \(-Ah\) for a logarithmic column perturbation \(h\). A second division by the corresponding column sums reverses the sign, giving
\[
J=D(\log S_M)(\log q_*)
=\operatorname{diag}(c)^{-1}P^{\mathsf T}\operatorname{diag}(r)^{-1}P.
\]
One has \(J\mathbf1=\mathbf1\), \(c^{\mathsf T}J=c^{\mathsf T}\), and \(J\) is self-adjoint and nonnegative in the weighted inner product \(\langle a,b\rangle_c=a^{\mathsf T}\operatorname{diag}(c)b\). It preserves \(E\) and is similar to \(W^{\mathsf T}W\), whose eigenvalues are the squared singular values of \(W\).

**3. Strict spectral separation.** Weighted Cauchy–Schwarz gives, for all \(z\in\mathbb R^n\),
\[
\sum_i\frac{(\sum_jP_{ij}z_j/\sqrt{c_j})^2}{r_i}\leq\sum_jz_j^2.
\]
Equality holds at \(z=\sqrt c\), proving that the largest singular value of \(W\) is one. Because \(P\) is strictly positive, \(W^{\mathsf T}W\) is strictly entrywise positive; its Perron eigenvalue one is simple. Therefore every eigenvalue \(\sigma\) of \(J|_E\) belongs to \([0,1)\), and the largest equals \(s_2^2\) (zero if the quotient dimension is zero).

**4. Linearization and local attraction.** Write each projective class as \([q_*\odot\exp(e)]\) with \(e\in E\). The induced logarithmic Sinkhorn map \(H:E\to E\) is real analytic, fixes zero, and satisfies \(DH(0)=J|_E\). On \(E\times E\) the two-step state map is
\[
F(a,b)=(b,H(2b-a)),\qquad
DF(0,0)=\begin{pmatrix}0&I\\-J&2J\end{pmatrix}\bigg|_{E\times E}.
\]
For each eigenvector of \(J|_E\) with eigenvalue \(\sigma\), its invariant two-dimensional block has characteristic polynomial
\[
\lambda^2-2\sigma\lambda+\sigma=0.
\]
For \(0<\sigma<1\), the roots are \(\sigma\pm i\sqrt{\sigma(1-\sigma)}\), with modulus \(\sqrt\sigma\); for \(\sigma=0\), the block is nilpotent. Consequently \(\rho(DF(0,0))=s_2<1\). For any \(\rho\in(s_2,1)\), choose an equivalent norm in which the derivative norm is strictly less than \(\rho\), and shrink the neighborhood so continuity of the derivative keeps the map contractive there. Iteration proves the stated local exponential bound. The smooth reconstruction in Step 1 transfers it to \(X^k\to P\).

**5. Sharpness for the matrix output.** If \(s_2>0\), a nonconstant eigenvector \(h\in E\) with \(Jh=s_2^2h\) gives a Jacobian eigenvalue of modulus \(s_2\), so no uniform local estimate with an exponent smaller than \(s_2\) can hold: differentiate such an estimate at the fixed point and take iterates. The logarithmic derivative of the reconstructed output with respect to the extrapolated column argument is
\[
(DX[h])_{ij}=P_{ij}\bigl((Jh)_j-(Ah)_i\bigr).
\]
This is nonzero for the nonconstant \(h\), because otherwise positivity of \(P\) would force all components of \(Jh=s_2^2h\) to coincide. Along a two-step eigenmode \(\lambda\), the argument perturbation is \((2\lambda-1)h\); the characteristic polynomial excludes \(2\lambda-1=0\). Hence the same maximal rate occurs in the matrix-output linearization; the bound cannot be made uniformly faster by observing couplings instead of scaling factors.

**6. Exact two-by-two witness.** For \(M_t\) the scaled coupling is \(P=M_t/[2(t+1)]\), and \(W=M_t/(t+1)\) has singular values \(1\) and \((t-1)/(t+1)\). This proves the two exact local factors and their near-one limiting behavior. Standard Sinkhorn has state derivative \(J|_E\), hence rate \(s_2^2\). The BDRS two-step derivative has rate \(s_2\). 

## Verification

The companion standalone Python checker `verify.py` uses only the standard library. It exactly reconstructs six BDRS multiplicative updates with rational data and verifies equality to the cumulative-column recurrence, exact column feasibility at every step, weighted detailed balance and stochastic invariance of the Sinkhorn Jacobian on a nonsquare rational coupling, and the symbolic two-by-two eigenvalue formula at seven rational parameter choices. Three floating-point finite-difference checks separately confirm the logarithmic Jacobian; they are diagnostic only. A successful run prints `VERIFY_OK`. The proof above, not the finite checks, establishes the universal statement.

## Relationship to prior work

Ma's *Convergence of BDRS as a Matrix Scaling Algorithm* (May 2026) proves **global** convergence only under a strict projective-diameter bound \(\tanh^2(\Delta(M)/4)<1/3\). Its error comparison has a scalar recurrence with polynomial \(\lambda^2-2\kappa\lambda-\kappa\); this upper envelope is different from the **actual local derivative** polynomial \(\lambda^2-2\sigma\lambda+\sigma\). The opposite constant-term sign permits complex, stable roots for every \(0\le\sigma<1\). Ma's September 2026 paper shows an explicit positive-matrix six-cycle, ruling out unconditional global convergence while giving the cumulative recurrence used here. The present local theorem does not contradict that counterexample.

Ma, Xiao and Zhao (2025) introduce Bregman Douglas–Rachford splitting and discuss its optimal-transport formulation, without the matrix-scaling local spectral classification. Lehmann, von Renesse, Sambale and Uschmajew (2021) identify the squared-singular-value rate for ordinary and overrelaxed **Sinkhorn** updates; their first-order/SOR recurrences differ from BDRS's second-order cumulative recurrence. Classical Euclidean Douglas–Rachford local tangent-angle results (Liang, Fadili and Peyré, 2017) supply related geometric intuition but do not state the entropy-Bregman matrix-scaling recurrence or its all-positive-data local rate. The exact BDRS-specific local rate and the coexistence with its global cycles are the scope of this result.

## Limitations

This is local exponential stability on a projective neighborhood, not global convergence from arbitrary initial matrices or auxiliary scaling vectors. A positive six-cycle outside that neighborhood is consistent with the theorem. The analysis assumes strictly positive entries and exact arithmetic, and offers no explicit general lower bound on basin size or guaranteed complexity from arbitrary initialization. The sharpness concerns the uniform local linearized exponent; individual special initializations may decay faster. The source *Annealed Sinkhorn with Momentum* (arXiv:2609.33814) shares BDRS logarithmic-momentum structure, but its complete text could not be obtained during the comparison; equivalent local statements there remain a specific originality risk. Broader nonlinear Bregman-splitting equivalences in unindexed literature are an additional residual risk. Independent external validation has not been performed.

## References

1. Shiqian Ma, *BDRS Can Fail for Matrix Scaling and Optimal Transport*, publicly posted September 30, 2026, https://optimization-online.org/2026/09/bdrs-can-fail-for-matrix-scaling-and-optimal-transport/ , especially §2 equations (2.2)–(2.6) and §6.
2. Shiqian Ma, *Convergence of BDRS as a Matrix Scaling Algorithm*, publicly posted May 30, 2026, https://optimization-online.org/2026/05/convergence-of-bdrs-as-a-matrix-scaling-algorithm/ , Theorem 4.1 and its proof.
3. Shiqian Ma, Lin Xiao and Renbo Zhao, *Bregman Douglas-Rachford Splitting Method*, arXiv:2509.08739, https://arxiv.org/abs/2509.08739 .
4. Tobias Lehmann, Max-K. von Renesse, Alexander Sambale and André Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm*, Optimization Letters 16 (2022), https://doi.org/10.1007/s11590-021-01830-0 , §1 and Theorem 1.
5. Jingwei Liang, Jalal Fadili and Gabriel Peyré, *Local Linear Convergence Analysis of Primal–Dual Splitting Methods*, Optimization Online, 2017, https://optimization-online.org/2017/05/5995/ , §§1–4.
6. Samuel J. K. Chin and Maximilian Schiffer, *Annealed Sinkhorn with Momentum: Certified Unregularized Optimal Transport in Linear Memory*, arXiv:2609.33814, https://arxiv.org/abs/2609.33814 (abstract available; full text not inspected).
