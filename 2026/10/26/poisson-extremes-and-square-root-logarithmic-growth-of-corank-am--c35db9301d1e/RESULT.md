# Poisson extremes and square-root logarithmic growth of corank among nested Haar finite-field matrices

## Finding
Fix any prime power \(q\ge2\). Let \(A=(A_{ij})_{i,j\ge1}\) have independent uniform entries in \(\mathbb F_q\), let \(A_n\) be its upper-left \(n\times n\) submatrix, and let \(C_n=n-\operatorname{rank}_{\mathbb F_q}(A_n)\), with \(C_0=0\). Write \(M_N=\max_{0\le n\le N}C_n\) and \(P_\infty(q)=\prod_{j=1}^{\infty}(1-q^{-j})\).

**Exact extremal limit.** For every integer sequence \(k\to\infty\) and every sequence of nonnegative integers \(N_k\) such that \(N_kq^{-k^2}\to t\in[0,\infty)\),
\[
\Pr(M_{N_k}<k)\longrightarrow\exp\!\left(-\frac{t}{P_\infty(q)}\right).
\]
In particular, at time \(\lfloor tq^{k^2}\rfloor\) the number of completed zero-to-zero excursions attaining corank \(k\) has an asymptotic Poisson law of mean \(t/P_\infty(q)\).

**Almost-sure growth.** The sequence of maximum coranks satisfies
\[
\lim_{N\to\infty}\frac{M_N}{\sqrt{\log_q N}}=1\qquad\text{almost surely}.
\]
A finite exact formula underlying both conclusions is the excursion hitting probability
\[
h_k=\Pr_1(\tau_k<\tau_0)=\left[\sum_{j=0}^{k-1}q^{j(j+2)}\prod_{i=1}^{j}(1-q^{-i})^2\right]^{-1},\qquad k\ge2,
\]
and its sharp asymptotic \(h_k\sim q^{1-k^2}/P_\infty(q)^2\).

## Assumptions and scope
The field is a fixed finite field of prime-power cardinality \(q\), the matrix entries are independent and exactly Haar-uniform, and the principal blocks are *nested upper-left blocks* (not all subsets of principal minors). The time parameter counts successive block sizes, not independent matrix samples. Write \(P_m(q)=\prod_{j=1}^{m}(1-q^{-j})\) and \(P_0(q)=1\). The positive constant \(P_\infty(q)\) is well defined because \(\sum_{j\ge1}q^{-j}<\infty\). Passage to \(t=0\) is included, while no claim is made for a finite nontrivial limit when \(N_kq^{-k^2}\to\infty\). The Poisson assertion refers to complete regenerative excursions; the maximum assertion needs no excursion-label choice.

## Proof
**1. Transition kernel.** Conditional on the old block having corank \(j\), invertible row and column operations reduce it to \(\operatorname{diag}(I_{n-j},0_j)\). Since the appended row, column, and corner entry are independent uniform elements, elimination reduces the rank increment to the rank of a residual bordered \((j+1)\times(j+1)\) block
\[
\begin{pmatrix}0_{j\times j}&v\\w^T&a\end{pmatrix},
\]
where \(v,w\) are independent uniform \(j\)-vectors and \(a\) is an independent uniform scalar. This residual block has rank two exactly if \(v\ne0\) and \(w\ne0\), and rank zero exactly if \(v=w=0\) and \(a=0\); all other cases have rank one. Therefore the time-homogeneous corank chain has probabilities
\[
d_j=\Pr(C_{n+1}=j-1\mid C_n=j)=(1-q^{-j})^2,\qquad
u_j=\Pr(C_{n+1}=j+1\mid C_n=j)=q^{-(2j+1)},
\]
for \(j\ge1\), with \(d_0=0\), \(u_0=q^{-1}\), and holding probability \(1-d_j-u_j\). In particular the chain is irreducible, aperiodic, and nearest-neighbor.

**2. Recurrence and normalization.** For \(j\ge1\), \(u_j\le1/8\) and \(d_j\ge1/4\) (uniformly over prime powers \(q\ge2\)), so the conditional drift is at most \(-1/8\) away from zero. The bounded-increment Foster argument shows finite mean return to zero and positive recurrence. Independently, elementary counting of rank-\((n-j)\) finite matrices gives
\[
\Pr(C_n=j)=q^{-j^2}\frac{P_n(q)^2}{P_j(q)^2P_{n-j}(q)}\quad(0\le j\le n).
\]
The marginal limit gives the stationary law
\[
\pi_j=P_\infty(q)\frac{q^{-j^2}}{P_j(q)^2},\qquad\pi_0=P_\infty(q),
\]
whose uniqueness follows from positive recurrence. One may check detailed balance directly using \(\pi_j u_j=\pi_{j+1}d_{j+1}\).

**3. Hitting probability.** For \(k\ge2\), let \(f_j=\Pr_j(\tau_k<\tau_0)\), with \(f_0=0\), \(f_k=1\). The harmonic recurrence gives \(u_j(f_{j+1}-f_j)=d_j(f_j-f_{j-1})\). Consequently the successive increments are proportional to \(s_j=\prod_{i=1}^{j}d_i/u_i=q^{j(j+2)}P_j(q)^2\) for \(j\ge1\), with \(s_0=1\). Normalization \(\sum_{j=0}^{k-1}(f_{j+1}-f_j)=1\) yields the claimed exact formula \(h_k=f_1=(\sum_{j=0}^{k-1}s_j)^{-1}\).

Because \(s_{j-1}/s_j=u_j/d_j\to0\) exponentially fast, the sum is asymptotic to its final summand, \(s_{k-1}=q^{k^2-1}P_{k-1}(q)^2\). Thus \(h_k\sim q^{1-k^2}/P_\infty(q)^2\).

**4. Renewal intensity and Poisson limit.** Form independent cycles by waiting at state zero until the next exit to state one, and then following the walk until its next return to zero. The waiting time at zero is geometric with mean \(q\). If \(L\) denotes a cycle length, the regenerative renewal reward identity for time spent at zero gives \(\pi_0=q/\mathbb EL\), hence
\[
\mathbb EL=\mu=q/P_\infty(q).
\]
The cycle maxima are independent identically distributed; each reaches \(k\) with probability \(h_k\). By the renewal strong law, the number \(R_N\) of completed cycles by step \(N\) obeys \(R_N/N\to1/\mu\) almost surely. For every fixed \(\varepsilon>0\), with probability tending to one, the number of cycles started by \(N_k\) lies between \((1-\varepsilon)N_k/\mu\) and \((1+\varepsilon)N_k/\mu+1\). The event that no completed cycle has reached \(k\) is therefore sandwiched between the corresponding no-success events for these deterministic numbers of independent cycle marks (the single possibly incomplete cycle is absorbed into the upper deterministic count). Their probabilities are powers of \(1-h_k\). Since
\[
N_k h_k/\mu\longrightarrow t/P_\infty(q),
\]
the two bounds converge, after \(\varepsilon\downarrow0\), to \(\exp[-t/P_\infty(q)]\). The same binomial rare-event argument proves Poisson convergence for the number of completed cycles marked as hitting \(k\). For \(t=0\) the upper bound and \(N_kh_k\to0\) suffice.

**5. Strong law for maxima.** Let \(H_i\) be the maximum corank in cycle \(i\). Then \(\Pr(H_i\ge k)=h_k\), so \(\log_q h_k=-k^2+O(1)\). Fix \(\varepsilon>0\). For integer \(m=2^j\), a union bound at \(\lceil(1+\varepsilon)\sqrt{\log_qm}\rceil\) is summable over \(j\). The probability that all \(m\) cycles stay below \(\lfloor(1-\varepsilon)\sqrt{\log_qm}\rfloor\) is at most \(\exp(-mh_k)\), also summable along the dyadic subsequence. Borel--Cantelli, monotonicity between dyadic values, and then \(\varepsilon\downarrow0\) yield \(\max_{1\le i\le m}H_i/\sqrt{\log_qm}\to1\) almost surely. Finally \(R_N/N\to1/\mu\), and one unfinished cycle changes the index between \(R_N\) and \(R_N+1\), proving the stated assertion for \(M_N\).

## Verification
The independent finite-state arithmetic checker in `verify.py` enumerates the residual-block rank cases over small fields, verifies exact finite-dimensional corank probabilities against recursive evolution, and checks all gambler's-ruin harmonic equations. It also propagates killed transition matrices to compute finite-time no-hit probabilities, illustrating convergence to the stated constant. Its recorded output is in `verification_output.txt`. These finite checks are not used to infer infinite-time claims: the proof above supplies the recurrence, renewal and Borel--Cantelli arguments.

## Relationship to prior work
Lvov [1] explicitly identifies the nested principal-block corank as a recurrent reversible nearest-neighbor Markov chain and proves the corresponding Markov and stationary structure in a broader setting. Those statements provide background, not the present rare-level excursion asymptotic or maximum-over-time law. Lvov [2] gives a related operator approach and spectral results for cokernels over \(p\)-adic rings, again with a different stated target. Cooper [3] establishes finite-field rank-distribution background. Arratia and Earnest [4] use a countdown process to approximate one-time random-matrix rank distributions, rather than treating the maximum over a nested sequence of square principal blocks. No source inspected supplied the displayed Poisson extreme limit and its sharp intensity for this nested corank statistic.

## Limitations
The conclusions require independent uniform entries and fixed field size. They do not address symmetric ensembles, sparse or biased matrices, all non-nested principal minors, or growing fields. The proof supplies the leading extreme-scale intensity but not finer second-order corrections or a continuous Gumbel limit; the scale remains intrinsically lattice-valued. A historical statement in unsearched terminology might subsume the asymptotic; the identified literature comparison is not a mathematical proof of global novelty. No independent scientific audit has been performed.

## References
[1] Nikita Lvov, *Markov chains arising in the study of random matrices over pro-finite rings*, arXiv:2610.00134v1 (first submitted 2026-09-09), https://arxiv.org/html/2610.00134v1.
[2] Nikita Lvov, *A Random Walk on the Category of Finite Abelian p-groups*, arXiv:2408.06492v1 (2024), https://arxiv.org/html/2408.06492v1.
[3] C. Cooper, *On the distribution of rank of a random matrix over a finite field*, Random Structures & Algorithms 17 (2000), 197–212; DOI:10.1002/1098-2418(200010/12)17:3/4<197::AID-RSA2>3.0.CO;2-K.
[4] Richard Arratia and Michael Earnest, *A countdown process, with application to the rank of random matrices over \(\mathbb F_q(n)\)*, arXiv:1605.04352 (2016), https://arxiv.org/abs/1605.04352.
