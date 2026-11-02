# Superexponential weak mixing without the claimed uniform limit in F-stochastic Markov products

## Finding
Souissi and Mukhamedov's 2024 Theorem 3.5 claims uniform ergodicity of the reverse-ordered nonhomogeneous Markov chains obtained from their summably contracting \(F\)-stochastic operators. The following smooth, rational, simplex-linear family satisfies every hypothesis but fails to converge to the specified rank-one projection for **every** choice of strictly interior initial rows.

For each \(m\ge1\), let \(S^m=\{(x_0,\ldots,x_m):x_j\ge0,\ \sum_{j=0}^m x_j=1\}\) and define
\[
W(x_0,x_1,\ldots,x_m)=\left(1-\tfrac14\sum_{j=1}^m x_j,\tfrac14x_1,\ldots,\tfrac14x_m\right).
\]
For any \(m+1\) chosen points \(X=(x_1,\ldots,x_{m+1})\) of the relative interior, let \(P_n\) be the stochastic matrix with row \(i\) equal to \(W^n(x_i)\). Use the source's ordering
\[
B_{k,n}=P_nP_{n-1}\cdots P_{k+1},\qquad 0\le k<n.
\]
Put \(e_0=(1,0,\ldots,0)\) and \(P=\mathbf 1 e_0\), so all rows of \(P\) are \(e_0\). For every fixed \(k\), \(B_{k,n}\) converges to a rank-one stochastic matrix \(L_k\); however, for every \(j=1,\ldots,m\), its common row \(\pi_k\) satisfies
\[
4^{-(k+1)}\min_i(x_i)_j\ \le\ (\pi_k)_j\ \le\ 4^{-(k+1)}\max_i(x_i)_j.
\]
In particular, \(L_k\ne P\), even though \(\sum_{n\ge1}\lVert P_n-P\rVert<\infty\) and the reverse products mix rows at least superexponentially:
\[
\delta(B_{k,n})\le\delta(E)^{n-k}\,4^{-\frac{n(n+1)-k(k+1)}2},\qquad
E_{i\bullet}=x_i.
\]
Moreover \(L_k\to P\) as \(k\to\infty\), so there is no common limiting projection for all starting times. This contradicts the stated uniform-\(P\)-ergodicity assertion, not the weak-ergodicity result.

## Assumptions and scope
The source defines \(F\)-stochastic operators by continuous nonnegative coordinates \(f_j\), a positive-definite gauge \(\varphi\) on the nonnegative tail, and an increasing \(g:[0,1]\to[0,1]\) satisfying conditions (C1)–(C3). For the map above take
\[
f_j(x)=x_j/4,\qquad \varphi(y_1,\ldots,y_m)=\tfrac12\sum_j y_j,\qquad g(t)=3t/4.
\]
Then (C1) holds, \(\sum_jf_j=\frac14\sum_jx_j\le\varphi\), and
\[
\varphi(W(x))=\tfrac18\sum_{j\ge1}x_j\le\tfrac3{16}\sum_{j\ge1}x_j=g\bigl(1-(W(x))_0\bigr).
\]
Furthermore \(\sum_{r\ge1}g^{\circ r}(t)=3t<\infty\) for every \(t\in[0,1]\). The phenomenon occurs in every positive simplex dimension, with strictly positive initial rows, no discontinuity, and geometric convergence of each nonlinear trajectory to \(e_0\).

## Proof
**Exact row formula.** Set \(a=1/4\) and \(E_{i\bullet}=x_i\). Direct induction gives
\[
W^n(x)=e_0+a^n(x-e_0),\qquad P_n=P+a^n(E-P).
\]
Thus every \(P_n\) is row stochastic, \(P_nP=P\), and \(\lVert P_n-P\rVert=O(a^n)\). The converse identity \(PP_n=P\) fails for interior initial rows because the first row of \(P_n\) has positive tail.

**Persistent memory of the rightmost matrix.** Write \(B_{k,n}=Q_{k,n}P_{k+1}\), where \(Q_{k,n}=P_n\cdots P_{k+2}\) is stochastic (and is the identity if \(n=k+1\)). Each row of \(B_{k,n}\) is a convex combination of rows of \(P_{k+1}\). Since its tail-column entries are \(a^{k+1}(x_i)_j\), each entry lies between the announced positive lower and upper bounds, uniformly for all \(n>k\). Consequently convergence to \(P\) is impossible.

**Existence and rate of the actual limits.** The Dobrushin coefficient \(\delta(A)=\frac12\max_{i,r}\sum_j|A_{ij}-A_{rj}|\) obeys \(\delta(AB)\le\delta(A)\delta(B)\) for stochastic matrices. Here \(\delta(P_n)=a^n\delta(E)\). Multiplication gives exactly the displayed superexponential bound, which tends to zero for each fixed \(k\). For each column the minimum over rows of \(B_{k,n}\) increases with \(n\), and the maximum decreases: left multiplication by a stochastic matrix replaces each row by a convex combination of existing rows. Both sequences converge, and their difference tends to zero by \(\delta(B_{k,n})\to0\). Hence all rows of \(B_{k,n}\) converge to the same stochastic vector \(\pi_k\), proving rank-one convergence and the claimed coordinate bounds. As \(k\to\infty\), all positive-index coordinates tend to zero, so \(\pi_k\to e_0\), establishing \(L_k\to P\).

**Two-state rational witness.** For \(m=1\), choose \(X=((3/4,1/4),(1/4,3/4))\). Then
\[
P_n=\begin{pmatrix}1-4^{-n}/4&4^{-n}/4\\1-3\cdot4^{-n}/4&3\cdot4^{-n}/4\end{pmatrix},\quad
P_1=\begin{pmatrix}15/16&1/16\\13/16&3/16\end{pmatrix}.
\]
Every second-column entry of \(B_{0,n}\) lies in \([1/16,3/16]\); every such entry of \(B_{2,n}\) lies in \([1/256,3/256]\). The intervals are disjoint. The row-difference coefficient is even exact:
\[
\delta(B_{k,n})=2^{-(n-k)}4^{-\frac{n(n+1)-k(k+1)}2}.
\]
Thus the chain has superexponential weak mixing but no single fixed-start-time-independent uniform limit, and certainly not the claimed \(P\).

## Verification
A standalone `check.py` uses Python `fractions.Fraction` only. Running `python check.py` tests the two-state matrix formula, nonvanishing second-column bounds, preservation \(P_nP=P\), normalization, and exact Dobrushin products for 152 finite rational pairs \((k,n)\). These tests check implementation and specializations; the displayed general inequalities and infinite limits are proved analytically above.

## Relationship to prior work
Souissi and Mukhamedov, *Nonlinear Stochastic Operators and Associated Inhomogeneous Entangled Quantum Markov Chains* (2024), Section 3, define the **reverse-ordered** product in their displayed formula immediately before Theorem 3.4; Theorem 3.5 claims uniform ergodicity for every summably controlled \(F\)-stochastic operator. The counterexample satisfies its exact hypotheses and contradicts this specific conclusion. The authors' separate Theorem 3.6 asserts only weak ergodicity, which the construction confirms.

The perturbation result quoted as their Theorem 3.4 invokes earlier work of Mukhamedov and Al-Rawashdeh. In that work (arXiv:2001.07703, Theorem 6.6), the assumption \(T_n\in\Sigma_P\) expressly entails **commutation with** \(P\), in addition to \(T_nP=P\). The source's quoted version omits this commutation, and the matrices here violate it because \(PP_n\ne P\). Thus the counterexample does not contradict that earlier theorem as originally stated. The contemporaneous study by Jamilov et al. (2024) constructs the same kind of row matrices for questions about absolute continuity of Markov measures, rather than proving the disputed reversed-product uniform limit.

## Limitations
This establishes failure of the **uniform-\(P\)-ergodicity assertion with the source's explicit product convention**, not failure of single-trajectory convergence, weak ergodicity, or a corrected theorem with two-sided commutation. It does not by itself settle whether an entangled quantum-chain mixing conclusion could follow by a different argument. The construction uses rational linear dynamics and arbitrary relative-interior initial rows; claims of novelty concern their direct implication for the 2024 theorem, not the classical distinction between weak and strong nonhomogeneous Markov ergodicity. No independent validation has been carried out.

## References
1. A. Souissi and F. Mukhamedov, *Nonlinear Stochastic Operators and Associated Inhomogeneous Entangled Quantum Markov Chains*, Journal of Nonlinear Mathematical Physics **31**, article 11 (2024), first published 2024-02-26, https://doi.org/10.1007/s44198-024-00172-6 . See Definition 3.1, product definition, Theorems 3.4–3.6.
2. F. Mukhamedov and A. Al-Rawashdeh, *Generalized Dobrushin Ergodicity Coefficient and Ergodicities of Non-homogeneous Markov Chains*, arXiv:2001.07703 (2020), https://arxiv.org/abs/2001.07703 ; Banach Journal of Mathematical Analysis **16**, article 18 (2022). See definition of \(\Sigma_P\) and Theorem 6.6.
3. U. Jamilov, F. Mukhamedov, F. Mukhamedova, and A. Souissi, *Dynamics of nonlinear stochastic operators and associated Markov measures*, Mathematical Methods in the Applied Sciences **47**, 13300–13312 (2024), https://doi.org/10.1002/mma.10191 . See Section 4.
