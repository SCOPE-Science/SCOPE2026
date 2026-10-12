# W states make the block-product relaxation loss order-one-over-q sharp
## Finding
For integers \(2\le q\le n\) with \(q\mid n\), consider the \(n\)-qubit W state
\[
|W_n\rangle=\frac1{\sqrt n}\sum_{i=1}^n |0\cdots010\cdots0\rangle.
\]
For a partition \(\Pi=(B_1,\ldots,B_q)\) into \(q\) nonempty blocks, let \(F_\Pi^2(W_n)\) be the largest squared overlap with a state that is product across the blocks, while \(F_{\mathrm{prod}}^2(W_n)\) denotes the largest squared overlap with a fully product state. Put
\[
A_m=\left(\frac{m-1}{m}\right)^{m-1}.
\]
Then
\[
\min_{\Pi:\,|\Pi|=q}F_\Pi^2(W_n)=A_q,
\qquad
F_{\mathrm{prod}}^2(W_n)=A_n.
\]
The first equality is attained exactly by equal block sizes. Hence the exact best-partition relaxation loss is
\[
\Delta_{n,q}=A_q-A_n.
\]
For fixed \(q\) and \(n=mq\to\infty\),
\[
\Delta_{n,q}\to A_q-e^{-1},
\]
and as \(q\to\infty\),
\[
A_q-e^{-1}=\frac{1}{2e\,q}+\frac{7}{24e\,q^2}+O(q^{-3}).
\]
Thus the additive \(O(1/q)\) scale in the random-coloring block-product approximation of arXiv:2610.01979v1 is optimal in order over arbitrary states.

## Assumptions and scope
A block-product state for \(\Pi\) is an arbitrary tensor product of one state on each block; entanglement inside a block is allowed. The theorem concerns pure qubit W states, which are valid inputs to the arbitrary-state statement of the recent product-state-testing work. The exact equal-block statement assumes \(q\mid n\). The asymptotic lower bound concerns the best partition, so it applies a fortiori to any rule that selects one \(q\)-block partition.

The result is a sharpness statement for the partition-relaxation step. It does not claim that the constant implicit in the recent paper's upper bound is optimal, and it does not give a sample-complexity lower bound for the full testing or learning algorithms.

## Proof
Let \(s_j=|B_j|\) and \(p_j=s_j/n\), so \(p_j>0\) and \(\sum_jp_j=1\). Inside block \(B_j\), let \(|0_j\rangle\) be the all-zero state and let \(|1_j\rangle\) be the normalized one-excitation W state on that block. Relative to these two-dimensional local subspaces,
\[
|W_n\rangle=\sum_{j=1}^q\sqrt{p_j}\,|1_j\rangle\!\bigotimes_{k\ne j}|0_k\rangle.
\]
Thus the partition only changes the W coefficients from equal single-qubit weights to \(\sqrt{p_j}\).

For any \(\alpha>0\), choose the block-product vector
\[
|u(\alpha)\rangle=\bigotimes_{j=1}^q
\frac{|0_j\rangle+\alpha\sqrt{p_j}|1_j\rangle}{\sqrt{1+\alpha^2p_j}}.
\]
Its squared overlap is exactly
\[
|\langle u(\alpha)|W_n\rangle|^2
=\frac{\alpha^2}{\prod_{j=1}^q(1+\alpha^2p_j)}.
\]
Because \(p\mapsto\log(1+\alpha^2p)\) is strictly concave,
\[
\prod_{j=1}^q(1+\alpha^2p_j)
\le
\left(1+\frac{\alpha^2}q\right)^q,
\]
with equality exactly when every \(p_j=1/q\). Taking \(\alpha^2=q/(q-1)\) gives
\[
F_\Pi^2(W_n)\ge\left(\frac{q-1}q\right)^{q-1}=A_q,
\]
with strict inequality from this explicit witness whenever the block sizes are not equal.

For equal block sizes, the grouped state is locally isometric to the symmetric \(q\)-qubit W state. Its exact maximal product overlap is the standard value \(A_q\), so the lower bound is attained. The same formula with singleton blocks gives \(F_{\mathrm{prod}}^2(W_n)=A_n\). The symmetric-W overlap formula is independently established in the geometric-entanglement literature cited below.

Finally,
\[
\log A_q=(q-1)\log\left(1-\frac1q\right)
=-1+\frac1{2q}+\frac1{6q^2}+O(q^{-3}),
\]
so exponentiation yields
\[
A_q=e^{-1}\left(1+\frac1{2q}+\frac7{24q^2}+O(q^{-3})\right).
\]
This proves the asymptotic sharpness claim.

## Verification
The proof uses an explicit block-product witness, strict Jensen concavity, and the established exact product fidelity of symmetric W states. No finite enumeration or numerical experiment is used to infer an infinite statement. The accompanying script checks the algebraic witness numerically on representative partitions and checks the asymptotic constant; those calculations are corroborative only.

## Relationship to prior work
Bao, Helsen, and Nguyen (arXiv:2610.01979v1) introduce the random-coloring reduction and state that one can choose \(q\) blocks whose squared closest-product overlap exceeds the fully product optimum by only \(O(1/q)\). The result here supplies a matching order lower bound for that relaxation: W states force a best-partition loss asymptotic to \(1/(2e\,q)\) after the large-system limit.

Older geometric-entanglement work computes the nearest product states of W-type states and, in particular, the exact symmetric-W product fidelity \(A_m\). Those results provide the endpoint values used here but do not compare full product fidelity with the best \(q\)-block relaxation arising in the recent random-coloring reduction.

## Limitations
The sharpness is in asymptotic order, not in the constant of the recent upper bound. The exact finite formula above assumes \(q\mid n\); for general \(n\), the same witness argument still gives the universal lower bound \(A_q\), but this report does not optimize the integer imbalance correction. The conclusion concerns arbitrary input states and does not preclude better rates on restricted state classes.

## References
1. Z. Bao, J. Helsen, and T. Nguyen, *Fully tolerant product state testing and closest product state learning*, arXiv:2610.01979v1 (2026).
2. L. Tamaryan, H. Kim, E. Jung, M.-R. Hwang, D. K. Park, and S. Tamaryan, *Toward an understanding of entanglement for generalized n-qubit W-states*, arXiv:0806.1314v1 (2008), J. Phys. A 42 (2009) 475303.
3. S. Tamaryan, A. Sudbery, and L. Tamaryan, *Duality and the geometric measure of entanglement of general multiqubit W states*, arXiv:1002.3049v1 (2010).
4. A. Bakshi, J. Bostanci, W. Kretschmer, Z. Landau, J. Li, A. Liu, R. O'Donnell, and E. Tang, *Learning the closest product state*, arXiv:2411.04283v1 (2024).
