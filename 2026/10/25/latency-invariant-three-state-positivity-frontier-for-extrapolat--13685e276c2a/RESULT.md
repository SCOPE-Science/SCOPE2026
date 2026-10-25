# Latency-invariant three-state positivity frontier for extrapolated Strang splitting

## Finding

Let \(A,B\) be arbitrary row-conservative finite-state continuous-time Markov generators, and put
\[
S_h=e^{hA/2}e^{hB}e^{hA/2},\qquad
X_h=S_h,\qquad Y_h=S_{h/2}^{2},\qquad
M_{h,p}=\frac{4Y_h^p-X_h^p}{3}
\]
for \(h>0\) and each integer \(p\ge1\). This is a fourth-order two-level multi-product extrapolation of a symmetric second-order splitting, with aggregation delayed for \(p\) substeps. The output is row-conservative for all \(p\), but need not be entrywise nonnegative.

**Theorem.** In every dimension \(n\le2\), for every \(A,B,h,p\) as above, \(M_{h,p}\) is stochastic. More strongly,
\[
\boxed{M_{h,p}=M_{h,1}^{p}\quad(n\le2).}
\]
This exact identity is not asserted in higher dimensions.

Three states are the sharp universal dimension boundary. For \(\lambda>0\), set
\[
A=\lambda\begin{pmatrix}-1&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
B=\lambda\begin{pmatrix}0&0&0\\0&-1&1\\0&0&0\end{pmatrix}.
\]
For *every* positive integer \(p\), this directed pure-birth splitting has the exact positivity classification
\[
\boxed{M_{h,p}\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
0<h\le h_*(\lambda)=\frac4\lambda\log(4+\sqrt{15}).}
\]
In particular, the threshold in the per-substep length \(h\) is completely independent of the aggregation delay \(p\); the associated block spans physical time \(ph\). The first deficient entry is the transition from state 0 to state 1, which is strictly negative for every \(h>h_*(\lambda)\), no matter how large \(p\) is.

## Assumptions and scope

All matrices and computations are real and exact. A row Markov generator has nonnegative off-diagonal entries and zero row sums; its exponentials are row-stochastic. Matrix products act on row-distributed probabilities on the right. The nonnegativity statement includes reducible generators, vanishing individual generators, every positive step, and every finite integer delay. For \(n=1\), the matrices equal \(1\). The sharp three-state classification refers to the displayed equal-rate directed pure-birth split, not all possible three-state decompositions.

## Proof

**Two-state reduction.** Write the two generator rates as \(\alpha,\beta\ge0\). If \(\alpha>0\), the Markov exponential of \(A\) takes the form
\[
P(q,w)=\begin{pmatrix}1-w(1-q)&w(1-q)\\(1-w)(1-q)&w+(1-w)q\end{pmatrix},\quad
q=e^{-\alpha t},\quad 0\le w\le1.
\]
Here \(w=A_{01}/\alpha\); the second split has an analogous weight \(v\). Zero-rate generators follow by continuity. Set
\[q=e^{-\alpha h/4},\qquad r=e^{-\beta h/4},\qquad
w=\frac{A_{01}}\alpha,\qquad v=\frac{B_{01}}\beta.\]
Direct multiplication of the two Strang products yields
\[
(M_{h,1})_{01}=w F_A(q,r)+v F_B(q,r),\quad
(M_{h,1})_{10}=(1-w)F_A(q,r)+(1-v)F_B(q,r),
\]
where
\[
\begin{aligned}
F_A(q,r)&=\frac{1-q}{3}\bigl[q^2r^4(3q-1)+4qr^2(q+1)+3-q\bigr],\\
F_B(q,r)&=\frac{q(1-r^2)}{3}\bigl[4q^2r^2-qr^2-q+4\bigr].
\end{aligned}
\]
For \(q,r\in[0,1]\), both bracketed expressions are strictly positive: the first is at least \(3-q-q^2\ge1\), and the second at least \(4-q-qr^2\ge2\). Therefore both off-diagonal entries of \(M_{h,1}\) are nonnegative. Since \(X_h,Y_h\) are two-state stochastic matrices with the same determinant \(\theta=e^{-(\alpha+\beta)h}\), their traces both equal \(1+\theta\). Consequently \(M_{h,1}\) also has trace \(1+\theta\), so its off-diagonal entries sum to \(1-\theta\). This proves its diagonal entries are nonnegative.

For any stochastic \(2\times2\) matrix \(Z\) with determinant \(\theta\), Cayley–Hamilton gives
\[
Z^p=I+H_p(\theta)(Z-I),\qquad
H_p(\theta)=\sum_{j=0}^{p-1}\theta^j.
\]
Apply this identity to \(X_h,Y_h,M_{h,1}\), which all have determinant \(\theta\). Since \(M_{h,1}=(4Y_h-X_h)/3\), one obtains
\[
M_{h,p}=I+H_p(\theta)(M_{h,1}-I)=M_{h,1}^p.
\]
As powers of a stochastic matrix are stochastic, the dimension-two result holds for every delay. The zero-generator and \(\theta=1\) cases follow without division from the polynomial expression for \(H_p\).

**The three-state threshold.** For the displayed directed pure-birth generators put \(q=e^{-\lambda h/4}\in(0,1)\). Exact products of the upper-triangular exponentials show that \(X_h\) and \(Y_h\) both have diagonal \((q^4,q^4,1)\). The undelayed combination has
\[
\begin{aligned}
(M_{h,1})_{01}&=\frac{q^2(1-q^2)(8q-q^2-1)}3,\\
(M_{h,1})_{02}&=\frac{(1-q)^2(1+q)(-q^3+7q^2+3q+3)}3,\\
(M_{h,1})_{00}&=(M_{h,1})_{11}=q^4,\qquad
(M_{h,1})_{12}=1-q^4.
\end{aligned}
\]
The second displayed entry is strictly positive because \(-q^3+7q^2+3q+3>0\) on \((0,1)\).

For any upper-triangular matrix whose first two diagonal elements both equal \(d\), its \((0,1)\) entry after the \(p\)-th power equals \(p d^{p-1}\) times the original \((0,1)\) entry. Using this for \(X_h\) and \(Y_h\) gives
\[
\boxed{(M_{h,p})_{01}=\frac{p q^{4p-2}(1-q^2)(8q-q^2-1)}3.}
\]
Moreover \((M_{h,p})_{00}=(M_{h,p})_{11}=q^{4p}\), \((M_{h,p})_{12}=1-q^{4p}\), and row conservation forces \((M_{h,p})_{02}=1-q^{4p}-(M_{h,p})_{01}\). If \((M_{h,1})_{01}\ge0\), its positive companion \((M_{h,1})_{02}\) implies \((M_{h,1})_{01}\le1-q^4\), and hence
\[
0\le(M_{h,p})_{01}\le p q^{4(p-1)}(1-q^4)
\le(1-q^4)\sum_{j=0}^{p-1}q^{4j}=1-q^{4p}.
\]
So every entry is nonnegative in this case. If \((M_{h,1})_{01}<0\), the displayed exact formula makes the same entry negative for every delay \(p\).

Finally, \(8q-q^2-1\ge0\) precisely when \(q\ge4-\sqrt{15}\), since the other root is \(4+\sqrt{15}>1\). Substituting \(q=e^{-\lambda h/4}\) and \((4-\sqrt{15})(4+\sqrt{15})=1\) proves the threshold. This also shows strict loss for all larger \(h\), rather than just an isolated counterexample. A one-state stochastic map is the identity, so dimension three is minimal.

## Verification

The self-contained `verify.py` reconstructs two-state Strang matrices symbolically, checks the exact coefficient identities and shared determinant, verifies the delayed-power identity for integers \(1\le p\le7\), and reconstructs all relevant three-state entries and row sums for \(1\le p\le8\), plus rational threshold tests. Run `python verify.py` with SymPy at least version 1.10. These finitely many symbolic checks are reproducibility safeguards; the proofs above quantify over every integer delay and all admissible rates.

## Relationship to prior work

Blanes, Casas and Shaw [1] study fourth-order two-level multi-product extrapolation and delayed linear-combination aggregation, particularly equations (1.4)–(1.5), and analyze other qualitative properties and efficiency. Earlier multi-product constructions are credited therein to Chin and Geiser [2]. The present work does not propose a new integrator or the negative extrapolation coefficient. Its distinct result is the exact two-state identity for arbitrary Markov splittings, together with a sharp minimal three-state positivity boundary that remains independent of the aggregation delay.

The broad splitting review [3] presents Strang splitting, multi-product expansions, general order/positivity issues and positive-flow constructions, but not the above exact Markov-state classification or its delay invariance. General obstructions from negative weights do not imply a dimension-minimal threshold, nor that delay leaves the witness's per-step boundary unchanged. The earlier symmetric affine Lie–Trotter construction [4] has a different base map and does not identify this Strang-extrapolation result.

## Limitations

The exact nonnegativity boundary in three states applies to the displayed equal-rate *two-edge pure-birth split*; other three-state decompositions need not share it. The two-state assertion is universal for row-conservative continuous-time Markov generators but not for arbitrary non-Markov real matrices. The matrix \(M_{h,p}\) is a delayed block approximation, not generally the \(p\)-fold power of \(M_{h,1}\) in three or more dimensions. All statements concern exact matrix exponentials and exact arithmetic, not roundoff, stochastic simulation, or independent numerical validation. Literature coverage is a best-knowledge comparison; an equivalent earlier formula under other terminology is not ruled out.

## References

[1] S. Blanes, F. Casas, L. Shaw, *Generalized extrapolation methods based on compositions of a basic 2nd-order scheme*, arXiv:2311.11581 (first public version 2023-11-20), especially equations (1.4), (1.5), sections 3 and 5. https://arxiv.org/abs/2311.11581

[2] S. A. Chin and J. Geiser, *Multi-product operator splitting as a general method of solving autonomous and nonautonomous equations*, IMA Journal of Numerical Analysis **31** (2011), 1552–1577.

[3] S. Blanes, F. Casas, A. Murua, *Splitting methods for differential equations*, Acta Numerica (2024), arXiv:2401.01722, sections 1, 9.1.2, and 9.2.1. https://arxiv.org/abs/2401.01722

[4] M. De Leo, D. Rial, C. Sanchez de la Vega, *High-order time-splitting methods for irreversible equations*, arXiv:1310.3664 (2013). https://arxiv.org/abs/1310.3664
