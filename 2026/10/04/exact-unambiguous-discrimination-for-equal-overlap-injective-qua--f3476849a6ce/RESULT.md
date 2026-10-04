# Exact unambiguous discrimination for equal-overlap injective quantum sequences
## Finding
Let \(N\ge 3\), \(2\le k\le N\), and \(0<s<1\). Let \(\mathcal S_N=\{\lvert\psi_1\rangle,\ldots,\lvert\psi_N\rangle\}\) be pure states satisfying
\[
\langle\psi_i\mid\psi_j\rangle=s\qquad(i\ne j),
\]
and let \(\mathcal E_{N,k}\) be the uniform ensemble whose members are the product states
\[
\lvert\Psi_{\mathbf a}\rangle=\lvert\psi_{a_1}\rangle\otimes\cdots\otimes\lvert\psi_{a_k}\rangle
\]
indexed by ordered injective tuples \(\mathbf a=(a_1,\ldots,a_k)\) of distinct labels in \(\{1,\ldots,N\}\).

The exact global and LOCC unambiguous-discrimination probabilities are
\[
p_{\mathrm{LOCC}}^{\mathrm{ud}}(\mathcal E_{N,k})
=
p_{\mathrm G}^{\mathrm{ud}}(\mathcal E_{N,k})
=
\begin{cases}
(1-s)^k,&k<N,\\[3pt]
(1-s)^{N-1}\bigl(1+(N-1)s\bigr),&k=N.
\end{cases}
\]
Thus the unambiguous-discrimination part of Conjecture 14 of Murshid, Gupta, Russo, and Bandyopadhyay holds for every parameter in its stated domain.

## Assumptions and scope
The local states are exactly the equidistant family used in the source: their mutual inner products are the same real number \(s\in(0,1)\). The tuples are sampled uniformly without replacement and retain their order. The result concerns exact, zero-error unambiguous discrimination, with an inconclusive outcome allowed. It makes no claim about the minimum-error half of Conjecture 14.

Because the one-system Gram matrix is
\[
B=(1-s)I_N+sJ_N,
\]
its eigenvalues are \(1-s\) with multiplicity \(N-1\) and \(1+(N-1)s\) with multiplicity one. Hence \(B\) is positive definite and the \(N\) local states are linearly independent. The product states indexed by injective tuples are therefore linearly independent as a subset of the full tensor-product basis.

## Proof
Write \(G_{N,k}\) for the Gram matrix of the injective tuple ensemble. For injective tuples \(\mathbf a,\mathbf b\),
\[
(G_{N,k})_{\mathbf a,\mathbf b}=s^{d_H(\mathbf a,\mathbf b)},
\]
where \(d_H\) is Hamming distance.

For linearly independent pure states, unambiguous discrimination with conclusive probabilities \(p_{\mathbf a}\) is feasible exactly when
\[
G_{N,k}-\operatorname{diag}(p_{\mathbf a})\succeq0.
\]
Simultaneously relabeling all symbols by any permutation of \(\{1,\ldots,N\}\) acts transitively on the injective tuples and leaves \(G_{N,k}\) invariant. Averaging any feasible vector \((p_{\mathbf a})\) over this action preserves its average success probability and gives a uniform feasible value \(p\). Therefore
\[
p_{\mathrm G}^{\mathrm{ud}}(\mathcal E_{N,k})=\lambda_{\min}(G_{N,k}).
\]

Suppose first that \(k<N\). The full Gram matrix on all ordered \(k\)-tuples, repetitions allowed, is \(B^{\otimes k}\). Since \(G_{N,k}\) is its principal submatrix on injective tuples, the variational principle gives
\[
\lambda_{\min}(G_{N,k})\ge\lambda_{\min}(B^{\otimes k})=(1-s)^k.
\]
To attain this lower bound, choose any \(k+1\) labels and let \(\varepsilon\) be the alternating tensor on those labels. Define
\[
f(i_1,\ldots,i_k)=\sum_r\varepsilon_{i_1\cdots i_k r}.
\]
The tensor \(f\) is nonzero and vanishes whenever two coordinates coincide, so it is supported entirely on injective tuples. For every coordinate, summing \(f\) over that coordinate gives zero: after the other \(k-1\) distinct labels are fixed, the two possible remaining labels contribute with opposite signs. Hence
\[
f\in(\mathbf 1^\perp)^{\otimes k}
\]
and consequently
\[
B^{\otimes k}f=(1-s)^k f.
\]
Because \(f\) has no support outside the injective tuples, restricting this equation gives
\[
G_{N,k}f=(1-s)^k f.
\]
Thus \(\lambda_{\min}(G_{N,k})=(1-s)^k\) for \(k<N\).

Now let \(k=N\), so the tuple labels are permutations \(\pi\in S_N\). For \(T\subseteq\{1,\ldots,N\}\), define
\[
(A_T)_{\pi,\sigma}=\mathbf 1\{\pi(r)=\sigma(r)\text{ for every }r\in T\}.
\]
Each \(A_T\) is positive semidefinite: it is the Gram matrix obtained by assigning to a permutation the standard basis vector indexed by its restriction to \(T\). Expanding each factor \(s+(1-s)\mathbf 1\{\pi(r)=\sigma(r)\}\) gives
\[
G_{N,N}=\sum_{T\subseteq[N]}s^{N-|T|}(1-s)^{|T|}A_T.
\]
If \(|T|\ge N-1\), agreement on \(T\) forces two permutations to be equal, so \(A_T=I\). Dropping all other positive semidefinite summands yields
\[
G_{N,N}\succeq
\Bigl((1-s)^N+Ns(1-s)^{N-1}\Bigr)I
=(1-s)^{N-1}\bigl(1+(N-1)s\bigr)I.
\]

This bound is sharp. Let \(v_\pi=\operatorname{sgn}(\pi)\). If \(|T|\le N-2\), then every fiber of permutations agreeing on \(T\) leaves at least two symbols free, and a transposition of two free symbols pairs its even and odd completions. Therefore \(A_Tv=0\). For \(|T|\ge N-1\), \(A_Tv=v\). Hence
\[
G_{N,N}v=(1-s)^{N-1}\bigl(1+(N-1)s\bigr)v,
\]
which proves the claimed minimum eigenvalue.

It remains to attain the same values by LOCC. The one-system equal-overlap ensemble has exact optimal unambiguous success probability \(1-s\); a fixed reciprocal-state measurement attains this probability for every label. Let every party perform this same local measurement. If \(k<N\), the joint tuple is certainly identified whenever all \(k\) local measurements are conclusive, which occurs with probability \((1-s)^k\). If \(k=N\), the tuple is a permutation of all labels and is identified whenever zero or one local measurements are inconclusive. Thus the success probability is
\[
(1-s)^N+Ns(1-s)^{N-1}
=(1-s)^{N-1}\bigl(1+(N-1)s\bigr).
\]
These probabilities equal the global upper bounds above.

## Verification
The proof uses two exact spectral witnesses rather than finite enumeration: an alternating \((k+1)\)-label tensor for \(k<N\), and the sign representation of \(S_N\) for \(k=N\). The lower bounds come respectively from principal-submatrix interlacing and from an explicit positive-semidefinite decomposition.

The bundled script `artifacts/verify.py` checks, with exact rational arithmetic at \(s=2/5\), the alternating-tensor eigenvector identity for every \(3\le N\le6\) and \(2\le k<N\), the sign-vector identity for every \(3\le N\le6\), and the closed-form success expressions. These finite checks corroborate the algebra but are not used as a substitute for the universal proof.

## Relationship to prior work
Murshid, Gupta, Russo, and Bandyopadhyay define the same injective ensembles, prove the base \(N=3,k=2\) case, calculate the additional cases \((N,k)=(3,3),(4,2),(4,3)\), exhibit matching local protocols there, and state the formula above as Conjecture 14. Their discussion explicitly moves from those examples to the all-\(N,k\) conjecture rather than supplying a general spectrum calculation.

Earlier quantum-sequence discrimination results of Gupta, Murshid, Bandyopadhyay and collaborators treat sequences whose members are drawn independently, equivalently the full Cartesian product of local ensembles. That hypothesis excludes the present without-replacement prior. The distinction is substantive: at \(k=N\), the injective constraint makes one local inconclusive outcome recoverable from the missing label and raises the optimum from the independent-product value \((1-s)^N\) to \((1-s)^{N-1}(1+(N-1)s)\).

Targeted searches also considered the permutation-kernel formulation in which the full-length Gram matrix is a class-function kernel determined by fixed points or Hamming distance on \(S_N\). No source inspected supplied the stated minimum-eigenvalue formula for this quantum-discrimination problem.

## Limitations
The theorem requires the exact common real overlap \(s\in(0,1)\), a uniform prior over ordered injective tuples, and exact unambiguous discrimination. It does not address unequal overlaps, nonuniform tuple priors, noisy or approximate discrimination, maximum-confidence discrimination, or the minimum-error conjecture from the motivating paper.

A residual originality risk is that the \(k=N\) sign-eigenvector identity may have an equivalent formulation in older symmetric-group or association-scheme literature under terminology not recovered by the searches. No such source was located, and the inspected quantum-sequence literature does not cover the without-replacement ensemble.

## References
1. S. Murshid, T. Gupta, V. Russo, and S. Bandyopadhyay, “Quantum nonlocality without entanglement and state discrimination measures,” arXiv:2506.20560v1 (2025); Quantum 10, 2174 (2026), DOI: 10.22331/q-2026-07-23-2174.
2. T. Gupta, S. Murshid, and S. Bandyopadhyay, “Unambiguous discrimination of sequences of quantum states,” Physical Review A 109, 052222 (2024), arXiv:2402.06365.
3. T. Gupta, S. Murshid, V. Russo, and S. Bandyopadhyay, “Optimal discrimination of quantum sequences,” arXiv:2409.08705 (2024).
4. L. Roa, C. Hermann-Avigliano, R. Salazar, and A. Klimov, “Conclusive discrimination among \(N\) equidistant pure states,” Physical Review A 84, 014302 (2011), DOI: 10.1103/PhysRevA.84.014302.
5. Y. C. Eldar, “A semidefinite programming approach to optimal unambiguous discrimination of quantum states,” IEEE Transactions on Information Theory 49, 446–456 (2003).
