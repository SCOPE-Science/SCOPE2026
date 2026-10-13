# Optimal odd-party Pauli-parity total-correlation envelope
## Finding
Let \(n\ge 3\) be odd and work on \((\mathbb C^2)^{\otimes n}\). Write
\[
P_x=X^{\otimes n},\qquad P_y=Y^{\otimes n},\qquad P_z=Z^{\otimes n},
\]
and for a state \(\rho\) define its three full-parity correlations by
\[
c(\rho)=\bigl(\operatorname{Tr}(\rho P_x),\operatorname{Tr}(\rho P_y),\operatorname{Tr}(\rho P_z)\bigr)\in\mathbb R^3.
\]
Let
\[
\mathbb B_1=\{u\in\mathbb R^3:\|u\|_1\le 1\}.
\]
Then the total correlation, using natural logarithm,
\[
I_{\mathrm{tot}}(\rho)=D\!\left(\rho\middle\|\rho_1\otimes\cdots\otimes\rho_n\right),
\]
satisfies the geometric lower bound
\[
\boxed{\;I_{\mathrm{tot}}(\rho)\ge \frac12\operatorname{dist}_2\!\bigl(c(\rho),\mathbb B_1\bigr)^2\;}.
\]
Moreover this is exactly the strongest lower bound obtainable from the full real weighted family
\[
B_w=w_xP_x+w_yP_y+w_zP_z
\]
through the trace-norm/Pinsker witness mechanism used in the anchor paper.

For the equal-rate local depolarizing semigroup in the anchor, the three correlations scale as \(c(\rho_t)=e^{-nt}c(\rho_0)\). Therefore the optimized certificate is nonzero exactly for
\[
0\le t<\frac1n\log\|c(\rho_0)\|_1
\]
when \(\|c(\rho_0)\|_1>1\), and is zero for every \(t\ge0\) when \(\|c(\rho_0)\|_1\le1\). This is a statement about the optimized certificate, not a claim that the physical total correlation itself vanishes at that time.

## Assumptions and scope
The claim is restricted to odd \(n\ge3\). The oddness assumption is essential for the Euclidean form because \(P_x,P_y,P_z\) then pairwise anticommute. The state is otherwise arbitrary. All logarithms in \(I_{\mathrm{tot}}\) are natural, matching the anchor. The optimization is over real weight vectors \(w\in\mathbb R^3\); the zero vector is irrelevant.

The octahedron \(\mathbb B_1\) is also the product/separable threshold region seen by these three parity coordinates: for every product state the weighted support function is \(\|w\|_\infty\). A 2026 many-particle parity-witness paper independently records the associated absolute-correlation separability condition \(|c_x|+|c_y|+|c_z|\le1\). The finding here is the quantitative total-correlation envelope and its exact optimization over all weights, not the separability inequality itself.

## Proof
Fix \(w=(w_x,w_y,w_z)\in\mathbb R^3\) and set \(B_w=w_xP_x+w_yP_y+w_zP_z\).

First compute the product threshold. For a product state \(\sigma=\sigma^{(1)}\otimes\cdots\otimes\sigma^{(n)}\), let \(v_r=(v_{r,x},v_{r,y},v_{r,z})\) be the Bloch vector of \(\sigma^{(r)}\), so \(\|v_r\|_2\le1\). Then
\[
\operatorname{Tr}(\sigma B_w)=\sum_{j\in\{x,y,z\}}w_j\prod_{r=1}^n v_{r,j}.
\]
For \(n\ge2\),
\[
\left|\operatorname{Tr}(\sigma B_w)\right|
\le \|w\|_\infty\sum_j|v_{1,j}v_{2,j}|\prod_{r=3}^n|v_{r,j}|
\le \|w\|_\infty\sum_j|v_{1,j}v_{2,j}|
\le \|w\|_\infty.
\]
Equality is attained by choosing every site to be a Pauli eigenstate along an index where \(|w_j|=\|w\|_\infty\), with local eigenvalue signs chosen so that their product agrees with the sign of \(w_j\). Hence
\[
\Gamma_{\mathrm{prod}}(B_w)=\|w\|_\infty.
\]

Next compute the operator norm. Because \(n\) is odd, distinct full Pauli strings anticommute. For example,
\[
P_xP_y=i^nP_z=-P_yP_x,
\]
and similarly for the other pairs. Each \(P_j^2=I\), so
\[
B_w^2=(w_x^2+w_y^2+w_z^2)I
\]
and therefore
\[
\|B_w\|=\|w\|_2.
\]

The proof mechanism behind the anchor's Theorem 3.1 gives, before replacing the exact operator norm by its parity-defect upper bound, the following general witness inequality. If \(\rho_*:=\rho_1\otimes\cdots\otimes\rho_n\), then \(\operatorname{Tr}(\rho_*B_w)\le\Gamma_{\mathrm{prod}}(B_w)\), hence
\[
\bigl(\operatorname{Tr}(\rho B_w)-\Gamma_{\mathrm{prod}}(B_w)\bigr)_+
\le \|B_w\|\,\|\rho-\rho_*\|_1.
\]
Quantum Pinsker with natural logarithm gives
\[
I_{\mathrm{tot}}(\rho)\ge\frac12\|\rho-\rho_*\|_1^2,
\]
so for every nonzero \(w\)
\[
I_{\mathrm{tot}}(\rho)
\ge\frac12
\frac{\bigl(w\cdot c(\rho)-\|w\|_\infty\bigr)_+^2}{\|w\|_2^2}.
\]

Now use convex duality. The support function of \(\mathbb B_1\) is
\[
h_{\mathbb B_1}(w)=\|w\|_\infty.
\]
For any closed convex set \(K\subset\mathbb R^3\), Euclidean projection gives
\[
\operatorname{dist}_2(c,K)
=\sup_{\|w\|_2\le1}\bigl(w\cdot c-h_K(w)\bigr).
\]
Applying this to \(K=\mathbb B_1\), and using homogeneity of the preceding witness inequality, yields
\[
\sup_{w\ne0}
\frac{\bigl(w\cdot c-\|w\|_\infty\bigr)_+}{\|w\|_2}
=\operatorname{dist}_2(c,\mathbb B_1).
\]
Squaring proves the claimed bound and proves its optimality within this weighted witness mechanism.

For explicit evaluation, let \(a_j=|c_j|\). If \(\sum_j a_j\le1\), the distance is zero. Otherwise choose the unique \(\tau>0\) such that
\[
\sum_{j\in\{x,y,z\}}\max\{a_j-\tau,0\}=1.
\]
Then the Euclidean projection onto \(\mathbb B_1\) is coordinatewise soft-thresholding and
\[
\operatorname{dist}_2(c,\mathbb B_1)^2
=\sum_j\min\{a_j,\tau\}^2.
\]

Finally, in the anchor's equal-rate local depolarizing model, each centered one-site Pauli operator acquires a factor \(e^{-t}\), so each full parity string acquires \(e^{-nt}\). Thus \(c(\rho_t)=e^{-nt}c(\rho_0)\). The distance is positive exactly when \(\|e^{-nt}c(\rho_0)\|_1>1\), which gives the stated certificate lifetime.

## Verification
The algebraic steps are exact and do not rely on numerical enumeration. Pairwise anticommutation for odd \(n\) gives the exact norm \(\|B_w\|=\|w\|_2\), while the product-threshold proof is a direct Cauchy--Schwarz estimate with an explicit saturating product state. The convex-duality step is the standard Euclidean distance/support-function identity, applied to the \(\ell_1\) unit ball whose support function is \(\ell_\infty\).

The improvement over the equal-weight witness is strict on physical states. For odd \(n\), define
\[
\rho_a=2^{-n}\bigl(I+aP_x+aP_y\bigr),\qquad \frac12<a\le\frac1{\sqrt2}.
\]
Since \(P_x\) and \(P_y\) anticommute, \(\rho_a\ge0\), and its parity vector is \((a,a,0)\). The optimized result gives
\[
I_{\mathrm{tot}}(\rho_a)\ge\frac{(2a-1)^2}{4},
\]
whereas the anchor's equal-weight odd-\(n\) bound gives only
\[
I_{\mathrm{tot}}(\rho_a)\ge\frac{(2a-1)^2}{6}.
\]
Thus the envelope improves that bound by a factor \(3/2\) on this natural one-parameter family. The packaged checker verifies the Pauli anticommutation/norm identities, the soft-threshold distance formula on representative points, and this strict-factor example for small odd system sizes. Those finite checks are corroborative only.

## Relationship to prior work
The anchor, arXiv:2603.01105v1, proves a general total-correlation witness bound and specializes it to the fixed observable \(X^{\otimes n}+Y^{\otimes n}+Z^{\otimes n}\), obtaining denominator \(3\) for odd \(n\) and \(9\) for even \(n\). Its introduction explicitly says that it does not optimize a fixed family of multipartite correlation inequalities. The inspected text contains no weighted-Pauli optimization, Euclidean projection formula, or \(\ell_1\)-ball envelope.

Quensen et al., DOI 10.1038/s41567-026-03302-7, prove the absolute-parity separability criterion \(|\langle P_x\rangle|+|\langle P_y\rangle|+|\langle P_z\rangle|\le1\). That establishes the same octahedral boundary as an entanglement witness, but it does not turn Euclidean distance from that octahedron into a lower bound on multipartite total correlation, nor does it identify the full weighted witness optimization above.

Older two-qubit Bell-diagonal geometry, including DOI 10.1103/PhysRevA.81.052325, uses an octahedral separable region in correlation coordinates when discussing relative entropy of entanglement. That setting is bipartite, uses a different information quantity, and does not imply the odd-party total-correlation theorem here.

## Limitations
The Euclidean envelope is proved only for odd \(n\). For even \(n\), the three full Pauli strings commute and the exact weighted operator norm is polyhedral rather than Euclidean; no even-party optimized formula is claimed here. The result quantifies total correlation, not entanglement itself, and it uses only three full-body parity correlators, so states whose correlation lies inside \(\mathbb B_1\) can still possess substantial total correlation. The depolarizing lifetime concerns positivity of this optimized certificate only.

## References
1. J. Tian, "Multipartite parity bounds and total correlation," arXiv:2603.01105v1 (2026).
2. M. Quensen et al., "Hong--Ou--Mandel interference of more than ten indistinguishable atoms," Nature Physics (2026), DOI 10.1038/s41567-026-03302-7.
3. H. Kim, M.-R. Hwang, E. Jung, and D. K. Park, "Difficulties in analytic computation for relative entropy of entanglement," Physical Review A 81, 052325 (2010), DOI 10.1103/PhysRevA.81.052325.
