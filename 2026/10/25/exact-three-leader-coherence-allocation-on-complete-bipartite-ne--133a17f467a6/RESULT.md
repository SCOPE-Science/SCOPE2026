# Exact three-leader coherence allocation on complete bipartite networks

## Finding

For every pair of integers \(2\le p\le q\), consider the unit-conductance complete bipartite graph \(K_{p,q}\). Select exactly three *noise-free* leaders and minimize the trace of the followers' grounded Laplacian inverse. Write \(a\) for the number of leaders in the part of size \(p\); thus \(3-a\) leaders lie in the part of size \(q\). The following table gives **all** minimizing values of \(a\), including every tie:

| Parameters | All optimal values of \(a\) |
| --- | --- |
| \(p=2,q=2\) | \(1,2\) |
| \(p=2,3\le q\le5\) | \(0\) |
| \(p=2,q=6\) | \(0,1,2\) |
| \(p=2,q\ge7\) | \(1,2\) |
| \(p=3,q=3\) | \(0,3\) |
| \(p=3,4\le q\le5\) | \(0\) |
| \(p=3,q=6\) | \(0,3\) |
| \(p=3,q=7\) | \(2,3\) |
| \(p=3,q\ge8\) | \(2\) |
| \(p=4,4\le q\le5\) | \(0,3\) |
| \(p=4,6\le q\le12\) | \(3\) |
| \(p=4,q\ge13\) | \(2\) |
| \(p=5,q=5\) | \(0,3\) |
| \(p=5,6\le q\le29\) | \(3\) |
| \(p=5,q=30\) | \(2,3\) |
| \(p=5,q\ge31\) | \(2\) |
| \(p\ge6,q=p\) | \(0,3\) |
| \(p\ge6,q>p\) | \(3\) |

Every three-element subset with the indicated allocation is optimal, and no other subset is. In particular, for unequal part sizes and \(p\ge3\), allocating exactly one leader to the smaller part is never optimal. At fixed \(p\ge6\), even as \(q\to\infty\), all three optimal leaders remain in the smaller part; at fixed \(p=3,4,5\) and sufficiently large \(q\), exactly two do.

For any feasible \(a\in\{0,1,2,3\}\), put \(u=p-a\), \(v=q-3+a\). The exact coherence cost is
\[
J_a(p,q)=\frac{u-1}{q}+\frac{v-1}{p}+\frac{p+q}{pq-uv}.
\]
The minimum is this explicit rational expression evaluated at any allocation in the table. The number of optimal *unordered leader sets* is exactly
\[
\sum_{a\in\mathcal A_{p,q}}\binom pa\binom q{3-a},
\]
where \(\mathcal A_{p,q}\) is the corresponding set of optimal allocations displayed above.

## Assumptions and scope

The graph is finite, connected, simple, undirected, unweighted, with parts of sizes \(p,q\). All edges have conductance one; the graph Laplacian is the unnormalized combinatorial Laplacian. Three distinct leader vertices are pinned to a common noiseless reference. Every nonleader vertex is a follower subject to independent equal-intensity additive node noise, so its steady-state covariance is a common positive scalar multiple of the inverse grounded Laplacian. The optimized objective is specifically \(\operatorname{tr}(L_{FF}^{-1})\); for unit-variance Wiener perturbations its steady-state total variance is half this value. Weighted edges, noisy leaders, heterogeneous disturbances, a different leader budget, and objectives involving the *smallest eigenvalue* of the grounded Laplacian are not included.

## Proof

**1. Exact objective for every allocation.** Choose \(a\) leaders from the \(p\)-part and \(3-a\) from the \(q\)-part. Every such choice is equivalent under graph automorphisms. The remaining follower counts are \(u=p-a\) and \(v=q-3+a\). In an ordering by parts, the grounded Laplacian is
\[
L_{FF}=\begin{pmatrix}
qI_u&-\mathbf1_u\mathbf1_v^{\mathsf T}\\
-\mathbf1_v\mathbf1_u^{\mathsf T}&pI_v
\end{pmatrix}.
\]
When both follower groups are nonempty, the subspaces perpendicular to their constant vectors have eigenvalues \(q\) and \(p\) with multiplicities \(u-1\) and \(v-1\). The remaining two-dimensional block is \(\left(\begin{smallmatrix}q&-\sqrt{uv}\\-\sqrt{uv}&p\end{smallmatrix}\right)\), whose inverse has trace \((p+q)/(pq-uv)\). Since three vertices are grounded and the graph is connected, \(pq-uv>0\). Summing inverse eigenvalues gives the claimed formula for \(J_a\). If either follower group is empty, direct diagonal inversion gives the same expression after cancellation of the formally absent one-dimensional contribution. This also establishes all boundary cases.

**2. Algebraic comparisons.** For \(p\le q\) and whenever the allocations compared are feasible, elementary fraction reduction gives
\[
J_1-J_2=\frac{(p-2)(q-p)(q-2)(p+q-1)}{pq(p+2q-2)(2p+q-2)},
\]
\[
J_0-J_3=\frac{(q-p)(p+q-9)}{3pq},
\]
\[
J_3-J_2=\frac{(6-p)q^2-(5p+6)q+p(p-2)(p-3)}{3pq(p+2q-2)}.
\]
All denominators are positive in their stated domains. Thus for \(p\ge3\), the \(a=1\) option is dominated by \(a=2\); if \(p<q\), it is strictly dominated. For \(p=2\), the two allocations \(a=1,2\) tie identically, and
\[
J_0-J_1=\frac{(q-6)(q-1)}{6q}
\]
whenever \(a=0\) is feasible. This gives every row for \(p=2\).

For \(p\ge3\), only \(a=0,2,3\) can minimize. The second comparison ranks \(a=0\) versus \(a=3\). The numerator of the third comparison reduces at the small possible \(p\) to
\[
\begin{array}{c|c}
p&3pq(p+2q-2)(J_3-J_2)\\\hline
3&3q(q-7)\\
4&2(q^2-13q+4)\\
5&(q-30)(q-1)
\end{array}.
\]
For integer \(q\ge4\), the middle polynomial is negative through \(q=12\) and positive from \(q=13\) onward: its positive root lies strictly between twelve and thirteen. For \(p\ge6\), writing \(q=p+k\) with integer \(k\ge0\) transforms the numerator into
\[
(6-p)k^2+(-2p^2+7p-6)k-4p^2<0.
\]
Indeed, for all \(p\ge6\) every coefficient is nonpositive and the constant is strictly negative. Finally \(J_0-J_3\) changes sign only at \(q=p\) or \(p+q=9\). Combining these three *exhaustive* pairwise comparisons yields precisely the table, including the ties at \((p,q)=(2,6),(3,6),(3,7),(4,5),(5,30)\) and balanced graphs. All feasible three-leader placements belong to exactly one of the four allocations, so the classification is global. The count of optimal sets follows from independent choices of vertices inside the two parts.

## Verification

The standalone Python program `verify.py` uses SymPy for five exact symbolic identity checks, tests the complete allocation table with rational arithmetic on 16,170 parameter pairs, and independently computes 1,876 traces by exact rational Gauss–Jordan inversion of actual grounded Laplacian matrices. Its recorded successful output is `VERIFY_OK symbolic_identities=5 exact_phase_cases=16170 dense_grounded_inverse_cases=1876`. Execute from a directory containing the supplied `verify.py` with `python verify.py` after installing the stated `requirements.txt`. The infinite-family result is proved by the algebraic argument above; finite checks neither establish uniqueness outside the theorem's assumptions nor replace proof.

## Relationship to prior work

Clark, Bushnell and Poovendran (first publicly posted 4 August 2012, arXiv:1208.0946) developed general supermodular and noisy leader-selection methods. Their optimization algorithms do not provide a closed three-leader allocation classification for complete bipartite graphs. Fitch and Leonard (first publicly posted 7 July 2014, arXiv:1407.1569) established the general joint-centrality formulation of noise-free leader selection and explicit placements on paths and cycles. Their general objective formula applies to the present graphs after specialization; the exact integer phase diagram, including all discrete ties and the two-versus-three leaders transition at the smaller part size six, requires the additional comparisons above. We do not claim the grounded-inverse objective, Schur-complement method, or generic leader-selection framework as new.

## Limitations

No unrestricted claim is made for more or fewer than three leaders, directed or weighted bipartite networks, noisy pinning, or other performance objectives. The formula holds for ordinary equal edge weights and combinatorial-Laplacian normalization only. The literature comparison is based on the identified primary papers and relevant indexed searches, not a proof that no equivalent specialized treatment exists. Independent mathematical review has not been performed.

## References

1. A. Clark, L. Bushnell, and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946, first submitted 2012-08-04. https://arxiv.org/abs/1208.0946
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submitted 2014-07-07; subsequently IEEE Transactions on Control of Network Systems 3(4), 366–378 (2016). https://arxiv.org/abs/1407.1569
