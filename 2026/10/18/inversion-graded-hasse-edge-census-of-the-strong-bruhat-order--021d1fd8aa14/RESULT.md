# Inversion-graded Hasse-edge census of the strong Bruhat order

## Finding

Let \(n\ge2\) and put \(N=\binom n2\). In the full strong Bruhat order on \(\mathfrak S_n\), weight an upward cover \(\pi\lessdot\sigma\) by \(q^{\ell(\pi)}\), where \(\ell\) is inversion number. Let \(E_{n,d}(q)\) count these covers by the rank of the lower endpoint, restricted to those swapping positions at gap \(d=j-i\) (not a difference of values). Set \([j]_q=1+q+\cdots+q^{j-1}\), \([n]_q!=\prod_{j=1}^n[j]_q\), \([0]_q!=1\). Then
\[
E_{n,d}(q)=(n-d)dq^{d-1}\frac{[n]_q!}{[d]_q[d+1]_q},\quad 1\le d\le n-1,
\qquad E_n(q)=\sum_{d=1}^{n-1} E_{n,d}(q).
\]
The total \(E_n\) is reciprocal of degree \(N-1\). For every gap, rank reflection gives \(E_{n,d}(q)=q^{N-1}E_{n,d}(1/q)\); the actual degree of \(E_{n,d}\) is \(N-d\), and its lowest exponent is \(d-1\). Equivalently \(q^{-(d-1)}E_{n,d}(q)\) is reciprocal of degree \(N-2d+1\).

For the Mallows law \(\Pr_q(\Pi=\pi)=q^{\ell(\pi)}/[n]_q!\) at \(q>0\), extended to the sorted permutation at \(q=0\), the expected upward degree is
\[
\mu_n(q)=\sum_{d=1}^{n-1}(n-d)\frac{d q^{d-1}}{[d]_q[d+1]_q}.
\]
For every \(n\ge4\) this function has a global maximizer over \(q\ge0\), and every global maximizer is strictly between zero and one. For each fixed \(q>0\), \(q\ne1\), one has \(\mu_n(q)=\Theta_q(n)\); at \(q=1\), \(\mu_n(1)\sim n\log n\).

## Proof

For \(i<j\) and \(\pi_i<\pi_j\), interchanging the entries increases inversion number by \(1+2\#\{k:i<k<j,\ \pi_i<\pi_k<\pi_j\}\). Hence the up-cover condition is precisely the boxed \(12\) pattern [1,2]. Fix a pair at gap \(d\) and examine its consecutive block of size \(d+1\), conditioning on the set of values in the block and the ordered outside entries. All inversions that do not have both positions in the block are independent of the ordering within the block, so the standardized order inside has Mallows law with normalizer \([d+1]_q!\).

For an up-cover the increasing endpoints must be consecutively ranked within the block, say \(a,a+1\), giving \(d\) choices. They contribute exactly \((a-1)+(d-a)=d-1\) inversions against the interior. The \(d-1\) interior entries are unconstrained and contribute \([d-1]_q!\). Thus the up-cover probability for a specified pair is \(p_d(q)=d q^{d-1}/([d]_q[d+1]_q)\). Summing over the \(n-d\) pairs and multiplying by the full Mallows partition function proves the two rank-count formulas as polynomial identities. The quotient in \(E_{n,d}\) removes the factors \([d]_q\) and \([d+1]_q\) from \([n]_q!\), proving the actual degree and the initial exponent. The formula \([j]_{1/q}=q^{1-j}[j]_q\) yields \(p_d(1/q)=q p_d(q)\); it gives rank reflection with grade \(N-1\) in every gap, and degree \(N-1\) for the total (the \(d=1\) contribution reaches that degree).

The sum of the gap probabilities gives the Mallows mean. It satisfies \(\mu_n(1/q)=q\mu_n(q)\), so positive \(q>1\) is strictly dominated by its reciprocal, and \(\mu_n(q)\to0\) as \(q\to\infty\). For \(n\ge4\), expansion at zero gives \(p_1(q)=1-q+O(q^2)\), \(p_2(q)=2q+O(q^2)\) and \(p_d(q)=O(q^2)\) for \(d\ge3\). Thus \(\mu_n(q)=(n-1)+(n-3)q+O_n(q^2)\). At one, differentiating the reciprocal identity gives \(\mu_n'(1)=-\mu_n(1)/2<0\). Continuity on \([0,1]\) gives a maximum, both endpoints are excluded by the derivative signs, and domination excludes every \(q>1\).

At \(q=1\) the prior uniform gap probability is \(p_d(1)=1/(d+1)\) [2, Remark 8.6]; summing gives \(\mu_n(1)=(n+1)H_n-2n\), where \(H_n=\sum_{j=1}^n1/j\). For fixed \(q\ne1\), let \(\rho=\min(q,1/q)<1\); the formula and reciprocity give \(p_d(q)\le C_q d\rho^{d-1}\). Then \(A(q)=\sum_{d\ge1}p_d(q)>0\) and \(B(q)=\sum_{d\ge1}d p_d(q)\) converge. The tail \(\sum_{d\ge n}(d-n)p_d(q)\) is \(O_q(n\rho^n)\), so \(\mu_n(q)=nA(q)-B(q)+O_q(n\rho^n)\), proving the growth distinction.

## Reproducibility

The standalone standard-library `verify.py` enumerates all permutations for \(2\le n\le8\), tests covers by actual swaps and inversion-number changes, and compares the cross-multiplied gap formulas coefficient by coefficient. It tests rank reflection using coefficients through grade \(N-1\), including padding with zeros for gaps at least two. It also checks the uniform mean and covariance consistency. The accompanying `verification_output.txt` reports the finite check of 1,246,964 candidate pair incidences. These are diagnostics; the formula is proved above for all \(n\).

## Relationship to prior work and scope

Adin and Roichman [1] give the cover criterion and the uniform mean. Kitaev, Qiu and Xu [2] identify boxed \(12\) with up-covers and give the **uniform** probability at every positional gap, not merely the uniform aggregate. The contribution here is the lower-inversion-rank refinement at each gap, its resulting nonuniform Mallows response, and the proofs that all maximizing parameters lie in \((0,1)\) and that fixed-parameter growth differs at \(q=1\). Mallows positive association for strong Bruhat up-sets [3] concerns a different property. The single-statistic degree enumerator \(\sum_\pi z^{d_+(\pi)}\) and its low-degree layers also concern a different distribution; they do not record inversion rank by position gap. Rank reflection itself is consistent with the known rank-reversing symmetry and is not a separate novelty claim.

The theorem does not treat weak order, arbitrary Bruhat intervals, parabolic quotients, the full degree distribution under Mallows weighting, or uniqueness of the maximizing \(q\). Scaling with varying \(q=q_n\), including the window near \(q=1\), is not asserted. The position-gap formula is a polynomial identity in formal \(q\), while the degree expectation and optimization are over real nonnegative parameters.

## References

1. R. M. Adin and Y. Roichman, *On Degrees in the Hasse Diagram of the Strong Bruhat Order*, arXiv:math/0505020 (2005).
2. S. Kitaev, D. Qiu and C. Xu, *Coincidences and Growth of Boxed Mesh Patterns*, arXiv:2609.13764 (2026), §8, Proposition 8.1 and Remark 8.6.
3. J. R. Johnson, I. Leader and E. Long, *Correlation for permutations*, arXiv:1909.03770 (2019).
