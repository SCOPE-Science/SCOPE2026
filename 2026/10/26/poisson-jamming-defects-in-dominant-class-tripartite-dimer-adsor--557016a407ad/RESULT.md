# Poisson jamming defects in dominant-class tripartite dimer adsorption

## Finding

Let \(K_{M_n,B_n,C_n}\) be the complete tripartite graph with vertex classes \(A,B,C\). Each edge independently attempts permanent dimer adsorption at rate one, and an attempt succeeds if and only if both endpoints are vacant. Suppose \(B_n/n\to\alpha>0\), \(C_n/n\to\beta>0\), and \(M_n/n\to\infty\). Write \(J_n\) for the number of successfully adsorbed \(B\)-to-\(C\) dimers and \(\lambda_n=B_nC_n/(2M_n)\). Then:

1. Every minority vertex eventually becomes covered, and the terminal number of uncovered vertices is exactly \(M_n-B_n-C_n+2J_n\), all in the dominant class.
2. Whenever \(\lambda_n\to\lambda\in[0,\infty)\), the law of \(J_n\) converges in total variation to \(\mathrm{Poisson}(\lambda)\).
3. Whenever \(\lambda_n\to\infty\), one has \(J_n/\lambda_n\to1\) in probability.

In particular, if \(M_n/n^2\to\kappa\in(0,\infty)\), then \(J_n\) converges in total variation to a Poisson law with mean \(\alpha\beta/(2\kappa)\), and the random correction to the terminal vacancy count is precisely \(2J_n\). The scale \(M_n\asymp n^2\) separates vanishing from diverging minority–minority deposition counts.

## Assumptions and scope

The three part sizes are positive integers; the dominant part eventually exceeds the sum of the two minority parts. Distinct edges carry independent rate-one Poisson attempt processes. Once a vertex is occupied, it remains occupied. The process is run until no eligible edge remains. The analysis concerns the count of successful edges between the two minority classes, not the time required for deposition or the number of failed attempts. Both minority sizes grow linearly with the common parameter \(n\), and the dominant size grows superlinearly. All stochastic limits are under the adsorption randomness; no independence of successful edges is assumed.

## Proof

**Step 1: exact embedded chain.** Write \((a,b,c)\) for the vacant populations. After ignoring unsuccessful Poisson attempts, the next accepted dimer joins classes \(A\!B\), \(A\!C\), or \(B\!C\) with probabilities proportional to \(ab\), \(ac\), and \(bc\). In particular the conditional probability of a minority–minority event is
\[
p=\frac{bc}{a(b+c)+bc}.
\]
Set \(S=B_n+C_n\). Since \(M_n>S\) for all sufficiently large \(n\), the dominant class remains vacant throughout minority depletion. Every accepted edge removes one or two minority vertices, so the process ends precisely when \(b=c=0\). Exactly \(S-2J_n\) successful dimers join the dominant part; its uncovered population is \(M_n-S+2J_n\).

**Step 2: small-event bounds.** Let \(s=b+c\) and \(\theta=b/s\) when \(s>0\). At each step the dominant vacancy count satisfies \(M_n-S\le a\le M_n\), giving
\[
0\le p\le\frac{bc}{as}\le\frac{s}{4(M_n-S)}\le\frac{S}{4(M_n-S)}.
\]
There are at most \(S\) successful steps. Consequently
\[
\mathbb E J_n\le\frac{S^2}{4(M_n-S)},\qquad
J_n/S\xrightarrow{\mathbb P}0.
\]
The estimate also proves \(J_n\to0\) in probability when \(\lambda_n\to0\), since \(S^2/M_n\) and \(\lambda_n\) have asymptotically positive constant ratio under the hypotheses.

**Step 3: minority composition is nearly constant.** Index accepted dimers by \(k\), and let \(s_k,\theta_k\) denote the minority total and its \(B\)-fraction immediately before the next accepted dimer. Conditional on an event involving the dominant class, the minority vertex is selected from \(B\) with probability \(\theta_k\), so its contribution to the conditional drift of \(\theta_k\) is zero. For \(s_k\ge4\), the only drift comes from a minority–minority event, and is exactly
\[
\mathbb E[\theta_{k+1}-\theta_k\mid\mathcal F_k]
=p_k\,\frac{b_k-c_k}{s_k(s_k-2)}.
\]
Its magnitude is bounded by \(1/[2(M_n-S)]\). Stop when \(s_k<\varepsilon S\), for any fixed \(\varepsilon>0\). Before this time, each increment is at most \(2/(\varepsilon S)\) in absolute value for large \(n\); the compensated martingale therefore has maximal variance \(O_\varepsilon(S^{-1})\). Its total predictable drift is \(O(S/M_n)=o(1)\). By the martingale maximal inequality,
\[
\sup_{k:s_k\ge\varepsilon S}
\left|\theta_k-\frac{B_n}{S}\right|
\xrightarrow{\mathbb P}0.
\]
The last \(\varepsilon S\) minority sites contribute at most \(O(\varepsilon^2S^2/M_n)\) to the total conditional probability of minority–minority events, using the bound in Step 2 and the fact that \(s\) decreases at least once each step.

**Step 4: deterministic rare-event approximation.** Let \(\tau\le S\) be the number of accepted dimers and extend \(p_k=0\) for \(k\ge\tau\). Define deterministic probabilities
\[
q_{n,k}=\frac{B_nC_n}{S^2}\frac{S-k}{M_n},\qquad 0\le k<S.
\]
At step \(k<\tau\), the identity \(s_k=S-k-J_k\) holds, where \(J_k\) is the number of minority–minority dimers among the first \(k\) accepted edges. Using \(a_k=M_n-S+s_k+2J_k\), we have uniformly
\[
p_k=\frac{s_k}{M_n}\theta_k(1-\theta_k)\left(1+O(S/M_n)\right).
\]
Step 3 controls the composition on \(s_k\ge\varepsilon S\); Step 2 controls the remaining stages. Together with \(J_n/S\to0\), these imply
\[
\sum_{k=0}^{S-1}|p_k-q_{n,k}|
=o_{\mathbb P}(S^2/M_n).
\]
Since the sum is deterministically bounded by a constant times \(S^2/(M_n-S)\), its expectation tends to zero whenever \(S^2/M_n\) stays bounded. Furthermore,
\[
\sum_{k=0}^{S-1}q_{n,k}=
\frac{B_nC_n}{2M_n}\frac{S+1}{S}=\lambda_n(1+S^{-1}),
\quad\max_k q_{n,k}=O(S/M_n)\to0.
\]

**Step 5: the Poisson limit and diverging regime.** The accepted-edge process can be realized with independent uniforms \(U_k\): its minority–minority indicator is \(\mathbf1_{\{U_k\le p_k\}}\), with any remaining choice performed using auxiliary randomness. Couple it to the independent deterministic-probability indicators \(\mathbf1_{\{U_k\le q_{n,k}\}}\). Their total mismatch probability is at most \(\mathbb E\sum_k|p_k-q_{n,k}|\). When \(\lambda_n\) is bounded this tends to zero, and the sum of the independent indicators has total-variation distance at most \(\sum_k q_{n,k}^2\to0\) from the Poisson law of its mean. This proves the first limit, including \(\lambda=0\).

For \(\lambda_n\to\infty\), Step 4 implies \(A_n/\lambda_n\to1\) in probability, where \(A_n=\sum_k p_k\) is the compensator of \(J_n\). The martingale \(J_n-A_n\) has second moment bounded by \(\mathbb E A_n\le S^2/[4(M_n-S)]=O(\lambda_n)\). Chebyshev's inequality therefore gives \((J_n-A_n)/\lambda_n\to0\) in probability, proving the second limit.

## Verification

The accompanying `verification.py` uses only the Python standard library. It computes exact rational distributions via the three admissible transitions, checks mass conservation, class interchange, nonnegativity and support size for 112 finite part-size triples satisfying \(M>B+C\), and checks the terminal vacancy identity in independent adsorption simulations. It also compares simulated rare-event counts for four sequences of part sizes to the Poisson prediction. Run `python3 verification.py`. These finite computations corroborate, but do not establish, the asymptotic limit theorems.

## Relationship to prior work

Haji-Akbari, Haji-Akbari and Ziff study geometric dimer coverings and percolation of two-dimensional lattice substrates [1]. Turban studies random sequential \(k\)-mer adsorption on a homogeneous fully connected lattice and obtains a Poisson law for **failed attempts** in a low-coverage limit [2]. In contrast, this result gives a Poisson law for **successful edges between two minority vertex classes** in an imbalanced complete tripartite graph, coupled to an exact terminal vacancy-count correction. The processes, random observables and asymptotic regimes differ. Related general randomized greedy matching or adsorption theorems may provide broader coverage; no exhaustive historical-priority claim is made.

## Limitations

The result concerns equal Poisson attempt rates for all edges, one initially vacant complete tripartite graph, two linear-sized minority classes and one superlinear-sized dominant class. It does not give limiting deposition times, general multipartite rates, spatially sparse substrates, or universal laws for all random greedy matchings. Total-variation convergence applies only to the bounded-parameter regime; the diverging-parameter regime establishes a law of large numbers, not a central limit theorem.

## References

[1] A. Haji-Akbari, N. Haji-Akbari and R. M. Ziff, *Dimer Covering and Percolation Frustration*, arXiv:1507.04411 (first posted 15 July 2015), https://arxiv.org/abs/1507.04411.

[2] L. Turban, *Random sequential adsorption of k-mers on the fully-connected lattice: probability distributions of the covering time and extreme value statistics*, arXiv:1908.00940 (first posted 2 August 2019), https://arxiv.org/abs/1908.00940.
