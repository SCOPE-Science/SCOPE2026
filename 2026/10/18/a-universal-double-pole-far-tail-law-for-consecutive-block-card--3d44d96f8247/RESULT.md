# A universal double-pole far-tail law for consecutive-block card shuffling

## Finding

Let \(T_n\) be the number of shuffles needed to merge \(n\) consecutively numbered cards into one block under the random-permutation consecutive-successions merger defined below. For each fixed integer \(n\ge3\), there exist explicitly recursive rational constants \(\alpha_n>0\) and \(\beta_n\) such that, for integers \(t\to\infty\),
\[
\Pr(T_n>t)=2^{-t}(\alpha_n t+\beta_n)+O_n((11/24)^t).
\]
The \(11/24\) base is the largest nonleading eigenvalue for all \(n\ge4\), and it is attained with nonzero coefficient when \(n=4\). In particular, \(\Pr(T_3>t)=2^{-t}(1+2t/3)\) and
\[
\Pr(T_4>t)=(6t-60)2^{-t}+61(11/24)^t.
\]
The probability-generating function \(F_n(z)=\mathbb E[z^{T_n}]\) is rational, has a pole of order exactly two at \(z=2\) for \(n\ge3\), and has no pole of modulus smaller than two. Consequently, \(\mathbb E[e^{sT_n}]<\infty\) exactly when \(s<\log2\), for every \(n\ge2\). In contrast, \(T_2\) has a simple pole and \(\Pr(T_2>t)=2^{-t}\); \(T_1=0\).

## Assumptions and scope

Fix \(n\ge1\). At a step with \(j\) current blocks, place their \(j\) labels in a uniformly random permutation; adjacent increasing successive integers in that permutation are merged, with each maximal such string forming one block. Relabel the blocks in increasing original order and repeat with fresh independent permutations until one block remains. Write \(J_t\) for the current number of blocks, and \(T_n=\min\{t\ge0:J_t=1\}\), beginning with \(J_0=n\). The observed chain is decreasing in block count and absorbing at one.

Define \(A_0=A_1=1\) and, for \(m\ge2\), \(A_m=mA_{m-1}+(m-1)A_{m-2}\). The *known* one-step merger law is
\[
p_{j,k}:=\Pr(J_{t+1}=k\mid J_t=j)=\frac{\binom{j-1}{k-1}A_{k-1}}{j!},\qquad 1\le k\le j.
\]
It counts permutations with a specified number of increasing successions. Put \(q_j=p_{j,j}=A_{j-1}/j!\), so \(q_2=q_3=1/2\) and \(q_4=11/24\). The constants in the finding are specified by
\[
\begin{gathered}
\alpha_2=0,\quad\beta_2=1,\quad\alpha_3=2/3,\quad\beta_3=1,\\
\alpha_n=\frac{2\sum_{k=2}^{n-1}p_{n,k}\alpha_k}{1-2q_n},\qquad
\beta_n=\frac{2\sum_{k=2}^{n-1}p_{n,k}\beta_k-\alpha_n}{1-2q_n}\qquad(n\ge4).
\end{gathered}
\]
All statements concern *fixed* \(n\) as time grows, not the distinct simultaneous \(n\to\infty\) central-limit regime.

## Proof

**1. Transient spectrum.** For each \(n\), restrict the transition matrix to transient states \(2,\ldots,n\), ordered by state size. Since the number of blocks cannot increase, the resulting matrix \(Q_n\) is triangular and has eigenvalues \(q_2,\ldots,q_n\). The recurrence defining \(A_m\) gives, for \(j\ge3\),
\[
\frac{q_j}{q_{j-1}}=\frac{(j-1)+(j-2)A_{j-3}/A_{j-2}}j.
\]
For \(j\ge4\), \(A_{j-2}>(j-2)A_{j-3}\), hence \(q_j<q_{j-1}\). Thus exactly \(q_2=q_3=1/2\) are repeated and all other transient eigenvalues are distinct, positive, and at most \(q_4=11/24\).

**2. The double Jordan mode.** The \(3\to2\) transition has probability \(p_{3,2}=1/3>0\). In the \(2,3\) submatrix the off-diagonal entry therefore makes the repeated eigenvalue \(1/2\) a single Jordan block of size two, rather than two simple blocks. For the starting state \(3\), direct iteration of the \(2,3\) states gives \(S_3(t):=\Pr(T_3>t)=2^{-t}(1+2t/3)\); also \(S_2(t)=2^{-t}\). Since \(p_{n,3}>0\) for all \(n\ge3\), the Jordan mode is visible from every starting state \(n\ge3\). All other eigenvalues are smaller, so the survival sequence has the form asserted, with a remainder made of exponentials \(q_j^t\), \(4\le j\le n\). For \(n=3\), this remainder is identically zero.

**3. Exact coefficients.** For every integer \(t\ge0\), the Markov recursion reads
\[
S_n(t+1)=q_nS_n(t)+\sum_{k=2}^{n-1}p_{n,k}S_k(t).
\]
Substitute the inductive expansions \(S_k(t)=2^{-t}(\alpha_k t+\beta_k)+\text{faster exponentials}\), and equate the coefficients of \(t2^{-t}\) and \(2^{-t}\). For \(n\ge4\), the result is
\[
(1-2q_n)\alpha_n=2\sum_{k=2}^{n-1}p_{n,k}\alpha_k,
\quad (1-2q_n)\beta_n=2\sum_{k=2}^{n-1}p_{n,k}\beta_k-\alpha_n.
\]
All denominators are positive. Since \(p_{n,3}>0\) and \(\alpha_3=2/3\), each \(\alpha_n>0\). The distinct smaller eigenvalues produce the stated \(O_n((11/24)^t)\) remainder. Explicit substitution at \(n=4\) yields \(\alpha_4=6\), \(\beta_4=-60\); using \(S_4(0)=1\) fixes the remaining \((11/24)^t\) coefficient as \(61\). Thus this remainder exponent is sharp for the fourth state.

**4. Generating function and moment boundary.** Set \(F_1(z)=1\). First-step conditioning gives, for \(n\ge2\),
\[
F_n(z)=\frac{z\sum_{k=1}^{n-1}p_{n,k}F_k(z)}{1-zq_n}.
\]
In particular \(F_2(z)=z/(2-z)\). All poles of these rational functions lie among \(1/q_j\), and only \(q_2=q_3=1/2\) repeat. The positive coefficient of \(t2^{-t}\) in survival from each \(n\ge3\) rules out cancellation of its order-two pole at \(z=2\). The exact exponential-moment criterion follows from the nonnegative tail, its strictly positive leading coefficient, and \(\sum_t e^{st}t2^{-t}\) convergence exactly for \(s<\log2\). For \(n=2\), the same moment boundary holds with a simple pole. No assertion is made for \(n=1\), where the duration is zero.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic. It enumerates all permutations for initial block counts from two through seven and matches their transitions with the stated known kernel; independently propagates finite-state Markov distributions; checks the exact \(n=3,4\) survival formulas through fifty steps; and verifies annihilating-polynomial recurrences and the coefficient recursion through ten states. It prints `VERIFICATION_OK 1237 exact checks`. These finite checks corroborate the proof, rather than proving a statement quantified over all \(n\) by themselves. Run with `python3 verify.py` using Python's standard library.

## Relationship to prior work

Chern, Jiu and Simonelli (arXiv:2309.08841, public 2023-09-16) derive and analyze this card-merger problem and prove central-limit behavior in a growing-size regime. Their exact one-step merger kernel and recurrence are the input to the present analysis; neither the kernel nor the underlying shuffling process is asserted to be new. Rao, Zhang, Huang and Cheng (2016) previously considered its distribution and moments. The distinct contribution claimed here is the **fixed-size, long-time twofold spectral pole, its nonzero linear prefactor, explicit recursive constants and sharp universal secondary exponential scale**, which do not follow as a stated theorem in the inspected arXiv source. This relationship does not exclude an earlier algebraically equivalent formula.

## Limitations

The \(O_n\) constant depends on the fixed initial number of blocks. The finding does not estimate these constants uniformly when \(n\) grows, does not amend the prior central-limit theorem, and does not claim novelty for the one-step kernel or rationality of finite-state generating functions alone. The 2016 predecessor's full paper could not be inspected; its accessible abstract refers to distributions and Markov-chain properties and leaves a historical-coverage uncertainty, especially concerning implicit rational generating functions. No independent audit or independent historical-priority determination has been performed.

## References

- S. Chern, L. Jiu and I. Simonelli, *A central limit theorem for a card shuffling problem*, arXiv:2309.08841 (first posted 2023-09-16), https://arxiv.org/abs/2309.08841.
- M. Rao, X. Zhang, J. Huang and Y. Cheng, *A discrete probability problem in card shuffling*, Communications in Statistics—Theory and Methods 45 (2016), 612–620, DOI:10.1080/03610926.2013.834451. Full text not inspected.
