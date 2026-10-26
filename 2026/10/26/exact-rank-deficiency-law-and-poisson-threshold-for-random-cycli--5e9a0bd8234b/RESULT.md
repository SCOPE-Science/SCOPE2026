# Exact rank-deficiency law and Poisson threshold for random cyclic actuator schedules

## Finding

For each integer \(n\ge 2\), choose \(1\le r<n\), and write \(g=\gcd(n,r)\) and \(d=n/g\). Consider the cyclic shift \(P_n e_j=e_{j+1\bmod n}\) on \(\mathbb R^n\), with the two distinct actuator columns \(B=[e_0,e_r]\). At each of \(h=qn\) steps, for an integer \(q\ge1\), activate exactly one actuator, independently and uniformly from these two. Define the scheduled finite-horizon reachability matrix
\[
\Phi_h=[P_n^{h-1}b_0,P_n^{h-2}b_1,\ldots,b_{h-1}],\qquad b_k\in\{e_0,e_r\},
\]
and the rank deficiency \(X=n-\operatorname{rank}\Phi_h\). Let \(p=4^{-q}\). Then its **entire probability-generating polynomial** is
\[
\boxed{\mathbb E[z^X]=J_d\bigl(p(z-1)\bigr)^g,\quad
J_d(t)=\sum_{j=0}^{\lfloor d/2\rfloor}
\frac{d}{d-j}\binom{d-j}{j}t^j.}
\]
For \(d\ge2\), equivalently,
\[
J_d(t)=\left(\frac{1+\sqrt{1+4t}}2\right)^d+
\left(\frac{1-\sqrt{1+4t}}2\right)^d;
\]
its right side is a polynomial, independent of the choice of square-root branch. In particular, **the exact probability of complete reachability** is
\[
\boxed{\Pr\{\operatorname{rank}\Phi_h=n\}=
\left[\left(\frac{1+\sqrt{1-4^{1-q}}}2\right)^d+
\left(\frac{1-\sqrt{1-4^{1-q}}}2\right)^d\right]^g.}
\]
At the information-theoretically shortest possible horizon \(h=n\), **exactly \(2^g\) of the \(2^n\) distinct schedules are controllable**, and hence the success probability is \(2^{g-n}\). This can be exponentially small even though the constant schedule activating \(e_0\) is always controllable.

The probability law has a uniform, offset-independent asymptotic transition. For any sequences \(n\to\infty\), \(1\le r_n<n\), and integers \(q_n\ge1\), set \(\lambda_n=n4^{-q_n}\). If \(\lambda_n\to\lambda\in[0,\infty)\), then
\[
\boxed{X_n\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}(\lambda),\qquad
\Pr\{X_n=0\}\to e^{-\lambda}.}
\]
If \(\lambda_n\to\infty\), then \(\Pr\{X_n=0\}\to0\). Thus the transition occurs at a repeated-cycle count \(q\) near \(\log_4 n\), or horizon \(h\) near \(n\log_4 n\), on its inherent integer lattice. In particular, along \(n=4^k\), \(q=k+c\) for fixed integer \(c\), the limit is \(\exp(-4^{-c})\), uniformly in the allowed offset.

## Assumptions and scope

All ranks are over \(\mathbb R\) in exact arithmetic. Indices lie in the cyclic group \(\mathbb Z/n\mathbb Z\). Inputs are scalar at each time, with a single selected input column \(b_k\), so pointwise sparsity is exactly one. The selections are independent fair two-way choices; they are **not** the output distribution of a rank-constrained scheduling optimizer. The horizon is an exact positive integer multiple \(qn\) of the cycle length. The matrix \(P_n\) is invertible and \(B\) contains two distinct coordinate actuators. The theorem concerns the resulting finite-time algebraic reachability rank; it makes no claim about energy-optimal control, nonuniform sampling, feedback, stochastic disturbances, or mixing of a scheduling Markov chain.

## Proof

**1. Reduction to uncovered target coordinates.** Put \(s\equiv h-1-k\pmod n\). At each of the \(q\) time indices with this residue, the corresponding reachability column is either \(e_s\) (first actuator) or \(e_{s+r}\) (second actuator). Let \(C_s\) count the choices of the second actuator among those \(q\) times. The random counts \((C_s)_{s\in\mathbb Z/n\mathbb Z}\) are independent \(\operatorname{Binomial}(q,1/2)\). Since all columns of \(\Phi_h\) are standard basis vectors, its rank equals the number of distinct target coordinates reached. Coordinate \(s\) is absent precisely when the first-actuator count at residue \(s\) is zero and the second-actuator count at residue \(s-r\) is zero, namely
\[
E_s=\{C_s=q\}\cap\{C_{s-r}=0\}.
\]
As \(r\not\equiv0\pmod n\), the counts in this event are independent and \(\Pr(E_s)=2^{-2q}=p\), and
\(X=\sum_{s\in\mathbb Z/n\mathbb Z}\mathbf 1_{E_s}\).

**2. Exact joint-event formula.** If two distinct residues \(s,t\) are adjacent in the undirected step-\(r\) graph (that is, \(t=s+r\) or \(t=s-r\)), the joint event \(E_s\cap E_t\) is impossible, because one binomial count would have to equal both zero and \(q\). If a set \(S\) has no adjacent vertices in this graph, all the random binomial counts on which \(\{E_s:s\in S\}\) depend are disjoint, so
\[
\Pr\Bigl(\bigcap_{s\in S} E_s\Bigr)=p^{|S|}.
\]
The graph decomposes into \(g=\gcd(n,r)\) disjoint cycles of length \(d=n/g\). When \(d=2\), interpret the two opposite cyclic steps as the single edge of \(K_2\); the same counting formulas hold. Expanding
\(z^X=\prod_s(1+(z-1)\mathbf1_{E_s})\)
and taking expectations yields the independence polynomial of this disjoint union evaluated at \(t=p(z-1)\).

**3. Cycle polynomial and exact finite probability.** For a cycle on \(d\ge2\) vertices, the number of independent vertex subsets of cardinality \(j\) is
\(\frac{d}{d-j}\binom{d-j}{j}\) for \(0\le j\le\lfloor d/2\rfloor\). For example, count nonadjacent chosen positions by distributing the \(d-j\) unchosen positions into \(j\) positive circular gaps, and account for the choice of starting marked vertex. The cycle independence polynomials satisfy
\(J_0(t)=2\), \(J_1(t)=1\), and \(J_d(t)=J_{d-1}(t)+tJ_{d-2}(t)\). The quadratic characteristic roots are \((1\pm\sqrt{1+4t})/2\), proving the stated expression. Independence of the \(g\) cycles yields the generating polynomial and its evaluation at \(z=0\). For \(q=1\) one has \(t=-1/4\), so \(J_d(-1/4)=2^{1-d}\). The full-rank probability equals \(2^{g-n}\), hence exactly \(2^g\) of \(2^n\) schedules succeed. The constant first-actuator schedule attains rank \(n\), and rank \(n\) is impossible with fewer than \(n\) scalar-column time steps, showing sharp minimal horizon.

**4. Offset-uniform Poisson limit.** For any fixed integer \(k\ge1\), expand the falling factorial \((X)_k\) over ordered, distinct \(k\)-tuples of residues. Tuples containing a step-\(r\) adjacent pair contribute zero; all other tuples contribute \(p^k\). The dependency graph has maximum degree two for every \(n,r\), so the number of excluded distinct tuples is \(O_k(n^{k-1})\), uniformly in the offset. Therefore
\[
\mathbb E[(X)_k]=\bigl(n^k+O_k(n^{k-1})\bigr)p^k.
\]
When \(np\to\lambda\in(0,\infty)\), these factorial moments tend to \(\lambda^k\) for every fixed \(k\), and the usual factorial-moment characterization of the Poisson distribution gives the claimed weak convergence. When \(np\to0\), the union bound \(\Pr(X>0)\le np\) gives convergence to zero. When \(np\to\infty\), covariances between nonadjacent events vanish and between distinct adjacent events equal \(-p^2\); hence \(\operatorname{Var}(X)\le np\), and Chebyshev gives
\(\Pr(X=0)\le\operatorname{Var}(X)/(\mathbb E X)^2\le1/(np)\to0\).

For \(\lambda>0\), the assertion \(\Pr(X_n=0)\to e^{-\lambda}\) additionally follows from weak convergence because integer-valued random variables can be tested on the continuity interval \((-1/2,1/2)\). All estimates hold independently of the offset sequence.

## Verification

A standalone Python-standard-library checker is provided as `verify.py`. It directly enumerates all \(2^{qn}\) selection vectors for **74 distinct** cases with \(2\le n\le9\), \(1\le r<n\), \(q\in\{1,2,3\}\), and \(qn\le17\). For each vector it constructs the set of actual reached coordinates and the resulting rank deficiency, then compares the entire exact rational empirical distribution with an independently implemented recurrence for \(J_d(p(z-1))^g\). It also checks the exact minimal-horizon count and compares selected probability evaluations with the characteristic-root expression, along with critical-window examples \(n=4^k\). The successful reproducibility message begins `VERIFY_OK exact rank-deficiency distributions for 74 independent enumeration cases`. This finite enumeration is neither a proof of the all-dimension theorem nor a proof of the limiting law; the analytical proof above supplies both.

To reproduce with standard Python 3, place `verify.py` in any folder and execute `python verify.py`. No third-party package or input file is needed.

## Relationship to prior work

Ballotta, Joseph, and Thete [1] motivate the precise issue of selecting few actuators at each time while retaining finite-horizon controllability. Their reachable-column formula matches the definition used here; they analyze guaranteed-feasible greedy schedules and stochastic cost optimization instead of the **exact probability law for an unguided independently sampled schedule** on a cyclic permutation system. Their rank-preserving MCMC method should not be identified with the independent fair law here. Kondapi et al. [2] treat sparse scheduling design and numerical guarantees rather than this probability distribution. Siami, Olshevsky, and Jadbabaie [3] develop deterministic and randomized actuator schedules for performance bounds, using a different sampling/design framework. Jiao et al. [4] optimize finite-horizon LQG actuator schedules, including one-actuator choices, and compare algorithms with random selection; their Riccati-cost comparison does not provide a cyclic rank-deficiency generating function or the Poisson limit.

The cycle independence polynomial, its quadratic recurrence, and the factorial-moment method are classical combinatorial/probabilistic tools; the contribution asserted here is their exact synthesis into an all-parameter **scheduled-controllability rank law**, minimal-horizon arithmetic count, and offset-uniform sharp random-horizon transition. Unidentified prior results under equivalent occupancy or cyclic-cover terminology remain a genuine originality risk.

## Limitations

The distribution and threshold concern unbiased independent actuator draws over exactly \(qn\) time steps for a cyclic permutation matrix and two coordinate actuators. No claim is made about other horizons, other dynamics, nonuniform or adaptive choices, the output of the motivating rank-constrained algorithms, control costs, robust reachability, or the numerical conditioning of the controllability matrix. Standard-basis columns give rank directly but say nothing about optimal control energy. The asymptotic threshold is a lattice effect in \(q\), not a continuous limiting curve for arbitrary real horizon. The derivation is analytic and self-contained; its external originality beyond the inspected literature has not been independently certified.

## References

1. L. Ballotta, G. Joseph, and I. R. Thete, *Pointwise-Sparse Actuator Scheduling for Linear Systems with Controllability Guarantee*, arXiv:2407.12125v1 (first public submission 2024-07-16), https://arxiv.org/abs/2407.12125.
2. R. Kondapi et al., *Sparse Actuator Scheduling for Discrete-Time Linear Dynamical Systems*, arXiv:2407.00385v1 (2024), https://arxiv.org/abs/2407.00385.
3. M. Siami, A. Olshevsky, and A. Jadbabaie, *Deterministic and Randomized Actuator Scheduling with Guaranteed Performance Bounds*, arXiv:1805.00606 (2018), https://arxiv.org/abs/1805.00606.
4. J. Jiao, D. Maity, J. S. Baras, and S. Hirche, *Actuator Scheduling for Linear Systems: A Convex Relaxation Approach*, arXiv:2203.02321v2 (2022), https://arxiv.org/abs/2203.02321.
