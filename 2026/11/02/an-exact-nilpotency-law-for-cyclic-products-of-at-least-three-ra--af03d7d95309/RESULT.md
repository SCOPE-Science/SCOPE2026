# An exact nilpotency law for cyclic products of at least three random finite-field matrices

## Finding
For every finite field \(\mathbb F_q\), every integer \(t\ge3\), and all positive integers \(n_0,\ldots,n_{t-1}\), independently sample uniformly random linear maps
\[
A_i:\mathbb F_q^{n_{i-1}}\longrightarrow\mathbb F_q^{n_i}\quad(1\le i\le t),\qquad n_t=n_0.
\]
The cyclic product \(T=A_tA_{t-1}\cdots A_1\) is an endomorphism of \(\mathbb F_q^{n_0}\). Its nilpotency probability is exactly
\[
\boxed{\Pr(T\text{ nilpotent})=1-\prod_{i=0}^{t-1}(1-q^{-n_i}).}
\]
In particular, for \(t\ge3\) independent uniform square matrices of order \(n\), the probability is \(1-(1-q^{-n})^t\). The formula depends only on the multiset of dimensions, regardless of their ordering around the cycle.

## Assumptions and scope
All spaces are over the *same* finite field \(\mathbb F_q\), the dimensions are strictly positive, and all matrices are chosen independently with each entry uniformly distributed. Nilpotent means \(T^j=0\) for some positive integer \(j\), equivalently \(T^{n_0}=0\). The theorem includes arbitrary rectangular intermediate maps and no invertibility assumptions. The claimed new range is \(t\ge3\); the cases \(t=1\) and \(t=2\) were already known.

## Proof
**1. A rank-conditioned lemma.** Let \(P:V\to W\) be a fixed linear map of rank \(r\) and let \(B:W\to V\) be uniformly random. Write \(U=\operatorname{im}P\). The random restriction
\[
(PB)|_U:U\longrightarrow U
\]
is uniformly distributed among all endomorphisms of \(U\). Indeed, \(B|_U\) is uniformly distributed among maps \(U\to V\), while the linear map \(\operatorname{Hom}(U,V)\to\operatorname{End}(U)\), \(C\mapsto P\circ C\), is surjective, with fibers of equal size because \(P:V\to U\) is onto. The image of \(PB\) lies in \(U\), hence \(PB\) is nilpotent exactly when its restriction to \(U\) is nilpotent. Furthermore \(BP\) is nilpotent exactly when \(PB\) is nilpotent, by the power identities
\[
(BP)^{j+1}=B(PB)^jP,\qquad (PB)^{j+1}=P(BP)^jB.
\]
The Fine–Herstein–Hall nilpotent-matrix counting theorem gives \(\Pr(S\in\operatorname{End}(U)\text{ nilpotent})=q^{-r}\), including \(r=0\). Therefore
\[
\boxed{\Pr(BP\text{ nilpotent}\mid P)=q^{-\operatorname{rank}P}.}
\]

**2. A kernel moment.** Let \(P=A_{t-1}\cdots A_1:V_0\to V_{t-1}\) and write \(V_i=\mathbb F_q^{n_i}\). For every linear map \(P\),
\[
q^{-\operatorname{rank}P}=q^{-n_0}|\ker P|.
\]
For any fixed nonzero vector \(v\in V_0\), the conditional distribution of \(A_i u\), given any nonzero \(u\in V_{i-1}\), is uniform on \(V_i\). Thus the probability that the prefix trajectory stays nonzero is
\[
\Pr(Pv\ne0)=\prod_{i=1}^{t-1}(1-q^{-n_i})=:s.
\]
By summing the indicators of membership in the kernel (including the zero vector),
\[
\mathbb E|\ker P|=1+(q^{n_0}-1)(1-s)
=q^{n_0}-(q^{n_0}-1)s.
\]

**3. Complete the probability.** Conditional on the prefix \(P\), the last independent map \(A_t:V_{t-1}\to V_0\) is uniform. Apply Step 1 and average:
\[
\begin{aligned}
\Pr(A_tP\text{ nilpotent})
&=\mathbb E[q^{-\operatorname{rank}P}]\\
&=q^{-n_0}\mathbb E|\ker P|\\
&=1-(1-q^{-n_0})\prod_{i=1}^{t-1}(1-q^{-n_i}),
\end{aligned}
\]
which is the claimed identity for all \(t\ge3\) and completes the proof.

## Verification
A standalone enumeration is supplied in `verify.py`; run `python3 verify.py` using ordinary Python 3. This verifier enumerates *all* matrices in the indicated small cases, composes the prescribed maps, checks nilpotency by actual matrix powers, and compares rational probabilities exactly using fractions. Sample exhaustive results include \(112/256=7/16\) for a two-factor binary square case (a known test), \(2368/4096=37/64\) for a three-factor binary square case, \(1376/2048=43/64\) for a three-factor binary rectangular dimension cycle \((1,2,3)\), and \(1377/6561=17/81\) for the ternary two-factor square case. Further checks exhaust the rank-conditioned lemma. The executable prints `VERIFY_OK` on success. Finite enumerations do not establish the theorem for arbitrary dimensions or fields; Steps 1–3 provide the universal proof.

## Relationship to prior work
The 2026 paper of Sarma and Subedi introduced nilpotent product probability as a statistic for finite rings and examined commutative and triangular rings. The original motivation here is to understand that statistic for arbitrary-length products of independently sampled full finite-field matrices. The Fine–Herstein nilpotent count, discussed and reproved by Leinster, already gives the single-factor case. More importantly, **Wästlund's 2020 Proposition 14 gives exactly the two-factor rectangular formula**
\[
q^{-m}+q^{-n}-q^{-(m+n)}.
\]
That two-factor result, including its square specialization for full matrix rings, is prior work and is not claimed as new. The present claim is the uniform identity for every cyclic length \(t\ge3\), including independently varying rectangular dimensions, proven by a rank-conditioned transfer and a kernel-moment computation. The older two-factor argument via a bipartite martingale motivates possible further generalization, but does not state the arbitrary-length identity. The multi-row material elsewhere in Wästlund's paper concerns a different key-placement model, so an implicit extension cannot be excluded and is a priority limitation.

## Limitations
No result is claimed for dependent or nonuniform matrix factors, different base fields, fixed-rank sampling, or the distribution of nilpotency indices or Jordan types. The identity is a probability statement, not a complete description of the matrix-product distribution. A closely related martingale proof may be implicit in older literature, especially Wästlund's paper; absolute priority cannot be inferred from unsuccessful database searches. The proof uses the established Fine–Herstein–Hall nilpotent count as an input.

## References
1. D. Sarma and T. Subedi, *Nilpotent product probability of finite rings*, arXiv:2610.07892v1 (2026-10-06), https://arxiv.org/html/2610.07892v1.
2. J. Wästlund, *Padlock Solitaire: A martingale trick for combinatorial enumeration*, arXiv:2008.13017v1 (2020-08-29), Section 15, Proposition 14, https://arxiv.org/pdf/2008.13017.
3. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562 (2019-12-29), https://arxiv.org/abs/1912.12562.
4. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois J. Math. 2 (1958), 499–504.
