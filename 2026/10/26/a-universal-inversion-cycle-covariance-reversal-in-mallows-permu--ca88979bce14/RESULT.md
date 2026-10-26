# A universal inversion–cycle covariance reversal in Mallows permutations
## Finding
Let \(\Pi_{n,q}\) have the Mallows distribution on the symmetric group \(S_n\), with probability proportional to \(q^{\operatorname{inv}(\pi)}\) for \(q>0\). Write \(C\) for the total number of cycles (including fixed points), \(I=\operatorname{inv}(\Pi_{n,q})\), and \(V_n(q)=\operatorname{Cov}_q(C,I)\). Then for every integer \(n\ge3\),
\[
V_n(1)=-\frac{2n-1}{12}<0,
\qquad
V_n(q)=-\,(n-1)q+O_n(q^2)\quad(q\downarrow0),
\]
and
\[
V_n(q)=\frac{a_n}{q}+O_n(q^{-2})\quad(q\to\infty),
\quad a_n=\begin{cases} n-1,&n\text{ odd},\\ n-3,&n\text{ even}.\end{cases}
\]
In particular, \(a_n>0\) for all \(n\ge3\): there are parameters above \(1\) where cycles and inversions are positively covariant, and there is at least one \(q_n>1\) with \(V_n(q_n)=0\). Hence the expected number of cycles has an interior local minimum above \(1\). The cutoff is sharp: for \(n=2\), \(V_2(q)=-q/(1+q)^2<0\) for every \(q>0\), while for \(n=1\) it is identically zero.

The first nontrivial size, \(n=3\), has precisely one positive covariance-zero parameter: it is the unique positive root of \(2q^4-7q^2-8q-2=0\), approximately \(2.3249635241\). No uniqueness claim is made for general \(n\).

## Assumptions and scope
Throughout, \(S_n\) is the permutation group on \(\{1,\ldots,n\}\), \(\operatorname{inv}(\pi)=\sum_{1\le i<j\le n}\mathbf 1\{\pi(i)>\pi(j)\}\), and the total cycle count \(C(\pi)\) includes one-cycles. The finite partition function is \(Z_n(q)=\sum_{\pi\in S_n}q^{\operatorname{inv}(\pi)}\), so every derivative in \(q>0\) is of a rational function with strictly positive denominator. Asymptotic constants in \(O_n(\cdot)\) are allowed to depend on fixed \(n\). The assertion of a local minimum does not imply that it is unique.

## Proof
**1. A derivative identity.** Put \(\mu_n(q)=\mathbb E_q C\). Differentiating finite sums gives the exact identity
\[
q\mu_n'(q)=\mathbb E_q[CI]-\mathbb E_q[C]\mathbb E_q[I]=V_n(q).
\]
Thus the sign of covariance is exactly the sign of the response of expected cycle count to increasing \(q\).

**2. The uniform-point sign, independently calculated.** For \(n\ge2\), fix positions \(1\le i<j\le n\), let \(d=j-i\), and put \(J_{ij}=\mathbf 1\{\Pi(i)>\Pi(j)\}\) for uniform \(\Pi\). Its probability is \(1/2\). Condition on the two distinct prescribed images \(\Pi(i)=a\) and \(\Pi(j)=b\) with \(a>b\). Any partial permutation made of these two prescribed directed arcs has some already closed directed cycles and exactly \(n-2\) remaining directed paths (isolated vertices included). Completing the permutation is equivalent to a uniform bijection of those path endpoints, so the conditional expected total number of cycles equals \(H_{n-2}\) plus the number of cycles already forced by the two arcs; use \(H_0=0\).

A forced cycle occurs precisely when \(a=i\), or \(b=j\), or \((a,b)=(j,i)\). Among the \(\binom n2\) equally likely ordered image pairs satisfying \(a>b\), these events have respectively \(i-1\), \(n-j\), and \(1\) possibilities. Their total count is \(n-d\). Therefore
\[
\mathbb E[C\mid J_{ij}=1]
=H_{n-2}+\frac{n-d}{\binom n2}
=H_n-\frac{2d-1}{n(n-1)},
\]
where \(\mathbb E C=H_n\) for a uniform permutation (the same path-completion argument with no fixed arcs, or the classical insertion decomposition). Hence
\[
\operatorname{Cov}(C,J_{ij})
=-\frac{2d-1}{2n(n-1)}.
\]
By summing over all pairs, and using \(\sum_{d=1}^{n-1}(n-d)(2d-1)=n(n-1)(2n-1)/6\), we obtain \(V_n(1)=-(2n-1)/12\). This proves strict negativity at \(q=1\) without assuming a monotonicity result.

**3. The identity-neighbor coefficient.** There is exactly one permutation with zero inversions (the identity); it has \(n\) cycles. Exactly \(n-1\) permutations have one inversion: the adjacent transpositions, each with \(n-1\) cycles. Consequently
\[
Z_n(q)=1+(n-1)q+O_n(q^2),\quad
\sum_{\pi}C(\pi)q^{\operatorname{inv}(\pi)}
=n+(n-1)^2q+O_n(q^2).
\]
Their quotient is \(\mu_n(q)=n-(n-1)q+O_n(q^2)\), and Step 1 yields the stated negative small-\(q\) covariance.

**4. The reverse-permutation-neighbor coefficient.** Let \(N=\binom n2\) and let \(w_0(i)=n+1-i\), the unique permutation with \(N\) inversions. It has \(c_0=\lceil n/2\rceil\) cycles. Exactly \(n-1\) permutations have \(N-1\) inversions, obtained by swapping two adjacent positions of \(w_0\): this follows, for example, by composing with \(w_0\), which complements inversion count, and using the one-inversion classification from Step 3.

Composing a permutation with a transposition merges two distinct cycles, decreasing cycle count by one, or splits one cycle, increasing cycle count by one. For odd \(n\), no adjacent pair of positions belongs to the same cycle of \(w_0\), so all \(n-1\) swaps decrease cycle count by one. For even \(n\), exactly the central adjacent pair \((n/2,n/2+1)\) lies in the same cycle; that one swap increases the count, while the remaining \(n-2\) swaps decrease it. The aggregate change relative to \(c_0\) is therefore
\[
\Delta_n=\begin{cases}-(n-1),&n\text{ odd},\\3-n,&n\text{ even}.\end{cases}
\]
Dividing numerator and denominator in \(\mu_n(q)\) by \(q^N\), then expanding in \(t=1/q\) at \(t=0\), gives \(\mu_n(q)=c_0+\Delta_n/q+O_n(q^{-2})\). By Step 1,
\[
V_n(q)=-\frac{\Delta_n}{q}+O_n(q^{-2}).
\]
For \(n\ge3\), \(-\Delta_n=a_n>0\), proving the positive large-\(q\) sign. For \(n=2\), the two-point law directly gives the stated strictly negative covariance; the case \(n=1\) is deterministic.

**5. Existence and the first threshold.** Because \(V_n(q)\) is continuous, is strictly negative at \(1\), and is strictly positive for all sufficiently large \(q\), it has a zero in \((1,\infty)\). The differentiable function \(\mu_n\) decreases immediately to the right of \(1\) and increases eventually, so it has an interior local minimum in that interval. For \(n=3\), direct enumeration gives \(Z_3(q)=1+2q+2q^2+q^3\) and cycle-weighted numerator \(G_3(q)=3+4q+2q^2+2q^3\). The numerator of \(\mu_3'(q)\) is \(G_3'(q)Z_3(q)-G_3(q)Z_3'(q)=2q^4-7q^2-8q-2\). Its nonzero descending coefficients have exactly one sign change, so Descartes' rule and opposite signs at zero and infinity give a unique positive root. Since \(Z_3(q)>0\), this is the unique zero of \(V_3\).

## Verification
Run `python verify.py` with Python 3 and no nonstandard dependencies. It enumerates every permutation for \(2\le n\le8\), checks exact inversion-level enumerators and both endpoint coefficients, independently recomputes uniform-point covariance using rational arithmetic, and checks the \(n=3\) derivative polynomial. The included `checker_output.txt` records its output. Enumeration is a finite consistency check; the all-\(n\) assertion follows from Steps 1–5.

## Relationship to prior work
The Mallows inversion-weighted model originates in Mallows' ranking model (1957). Gladkich and Peled, *On the Cycle Structure of Mallows Permutations* (first public arXiv version 2016-01-26), establish order bounds for expected cycle count for \(0<q<1\), and discuss the reflected regime \(q>1\) in their Section 5. Those results do not supply a finite-\(n\) covariance-sign reversal across the parameter range. He, Müller, and Verstraaten, *Cycles in Mallows random permutations* (arXiv 2022), obtain large-\(n\) asymptotics for cycle counts for fixed \(q<1\) and \(q>1\); this differs from the present exact all-\(n\) endpoint coefficient and crossing statement. A published published-finding corpus finding, *Linear inversion-gap profile for cycle count in a uniform random permutation* (2026), gives the uniform-point covariance and is acknowledged as prior coverage for Step 2, not as a new discovery here. The new statement is the positive high-bias sign and consequent universal reversal, including its parity-dependent coefficient and sharp \(n=2\) boundary.

## Limitations
No uniqueness, exact location, or monotonic dependence on \(n\) of the positive covariance zero is proved for \(n\ge4\). The two endpoint expansions are for each fixed \(n\), not uniform when \(n\) and \(q\) vary together. These results do not characterize the full joint law of inversion number and cycle count. Literature searches and focused inspection of related primary work cannot conclusively exclude an earlier equivalent result under alternative ranking-model terminology.

## References
1. C. L. Mallows, *Non-null ranking models. I*, Biometrika 44 (1957), 114–130.
2. A. Gladkich and R. Peled, *On the Cycle Structure of Mallows Permutations*, arXiv:1601.06991 (first public version 2016-01-26), later Annals of Probability 46 (2018), 1114–1169. https://arxiv.org/abs/1601.06991
3. J. He, T. Müller, and T. W. Verstraaten, *Cycles in Mallows random permutations*, arXiv:2201.11610 (first public version 2022-01-27), later Random Structures & Algorithms 63 (2023), 1054–1099. https://arxiv.org/abs/2201.11610
4. *Linear inversion-gap profile for cycle count in a uniform random permutation*, published-finding corpus record `2026/10/4/SCOPE-linear-inversion-gap-profile-for-cycle-count-in-a-uniform-random--efaa92233051` (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-linear-inversion-gap-profile-for-cycle-count-in-a-uniform-random--efaa92233051
