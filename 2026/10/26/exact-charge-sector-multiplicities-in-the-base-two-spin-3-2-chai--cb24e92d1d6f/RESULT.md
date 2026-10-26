# Exact charge-sector multiplicities in the base-two spin-\(3/2\) chain

## Finding

For the open-boundary exponential-symmetry spin chain with base \(q=2\), on-site spin \(S=3/2\), and length \(L\ge1\), the dimension of each charge eigenspace has an exact piecewise-linear formula. Define
\[
Q_L=\sum_{j=1}^{L}2^{L-j}S_j^z,\qquad r=Q_L+\frac32(2^L-1).
\]
The possible shifted charges are the integers \(0\le r\le3(2^L-1)\). Their multiplicities are
\[
d_L(r)=
\begin{cases}
\lfloor r/2\rfloor+1,&0\le r\le2^L-3,\\
2^{L-1},&2^L-2\le r\le2^{L+1}-1,\\
3\cdot2^{L-1}-\lfloor r/2\rfloor-1,&2^{L+1}\le r\le3\cdot2^L-3,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus the dimensions rise linearly, plateau at \(2^{L-1}\), and fall symmetrically. Their sum is \(4^L\), and every physical charge is half-odd-integer, so no neutral sector occurs.

## Assumptions and scope

The chain has open boundaries, \(L\ge1\) sites, and local spin \(S=3/2\), so each \(S_j^z\) eigenvalue lies in \(\{-3/2,-1/2,1/2,3/2\}\). This is a count of charge eigenspaces in the microscopic Hilbert space, not a count of energy levels. The result is specific to base \(q=2\) and does not assert the same piecewise law for other bases or spins.

## Proof

Set \(n_j=S_j^z+3/2\in\{0,1,2,3\}\). Then
\[
r=\sum_{j=1}^{L}2^{L-j}n_j,
\qquad
P_L(x)=\sum_r d_L(r)x^r
=\prod_{k=0}^{L-1}(1+x^{2^k}+x^{2^{k+1}}+x^{3\cdot2^k}).
\]
Each factor is \((1-x^{4\cdot2^k})/(1-x^{2^k})\). Telescoping gives
\[
P_L(x)=\frac{(1-x^{2^L})(1-x^{2^{L+1}})}{(1-x)(1-x^2)}.
\]
For \(L=1\) the identity follows directly; for \(L\ge2\), cancel the common powers. The coefficient of \(x^r\) in \(1/((1-x)(1-x^2))\) is \(a_r=\lfloor r/2\rfloor+1\) for \(r\ge0\), and zero for negative indices. Hence
\[
d_L(r)=a_r-a_{r-2^L}-a_{r-2^{L+1}}+a_{r-3\cdot2^L}.
\]
Evaluating this expression on the stated ranges yields the piecewise formula. Also \(P_L(1)=4^L\), and the coefficient sequence is symmetric under \(r\mapsto3(2^L-1)-r\), equivalently \(Q_L\mapsto-Q_L\).

## Verification

The generating-function argument proves the formula for every \(L\ge1\). The accompanying standard-library Python script compares the formula with direct integer convolution for \(L=1,\ldots,12\), checks reflection symmetry, and checks the total dimension \(4^L\). These finite checks supplement, but do not replace, the proof.

## Relationship to prior work

*Spin Chain with Continuous Exponential Symmetry: Topological Phase and Beyond* (arXiv:2610.10682v1; inspected full text arXiv:2610.10682v2) defines the weighted charge and studies the \(q=2,S=3/2\) half-SPT example, including the absence of a neutral charge sector and symmetry-paired open-chain levels. The inspected text does not state the exact charge-sector dimension law above. *Spin-spin correlation functions of the q-VBS state of an integer spin model* (arXiv:1009.4018v3) studies a different family with a real quantum-group deformation parameter and integer physical spin; it is not this base-two half-integer-spin model. The claim is limited to the finite-volume multiplicity formula, not a broader phase classification.

## Limitations

The result concerns open-boundary charge-sector dimensions for \(q=2,S=3/2\). It gives no energy spectrum, dynamical conclusion, or extension to other bases. Literature coverage is not exhaustive, and independent audit has not been performed.

## References

- *Spin Chain with Continuous Exponential Symmetry: Topological Phase and Beyond*, arXiv:2610.10682v1 (first public version, 2026-10-07); inspected full text arXiv:2610.10682v2.
- *Spin-spin correlation functions of the q-VBS state of an integer spin model*, arXiv:1009.4018v3 (2012).
