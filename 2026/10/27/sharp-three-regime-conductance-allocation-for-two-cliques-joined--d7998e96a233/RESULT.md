# Sharp three-regime conductance allocation for two cliques joined by a partial matching

## Finding

Let \(G_{k,m}\) consist of two copies of \(K_{k+m}\), with \(k\ge2\) designated gateways and \(m\ge1\) nongateways per clique. Join the gateways of opposing cliques by the \(k\) edges of a matching. Nonnegative conductances on all allowed edges have a single total budget \(B>0\). We compute the maximum of the second eigenvalue of the unnormalized weighted Laplacian. The low-ratio regime also follows from the earlier complete-biclique gateway optimum and a feasibility check, as explained below. The transitions and the allocation in the higher-ratio regimes require the matching-specific spectral constraint.

Write \(r=k/m\) and \(s_k=1+\sqrt{k/[2(k+1)]}\), and set
\[
t_* = \begin{cases}
3/2,&r\le3/2,\\
r,&3/2<r<s_k,\\
s_k,&r\ge s_k.
\end{cases}
\]
The maximum is \(\Lambda_{k,m}(B)=B/C_{k,m}\), where
\[
\begin{aligned}
C_{k,m}&=\frac{k+m}{2}+2mt_*+\frac{m}{2(t_*-1)}+(k-1)\max\{0,1-mt_*/k\}\\
&=\begin{cases}
(k+9m)/2,&r\le3/2,\\
(k+m)/2+2k+m^2/[2(k-m)],&3/2<r<s_k,\\
3k/2-1+m\bigl(3/2+1/k+\sqrt{2(k+1)/k}\bigr),&r\ge s_k.
\end{cases}
\end{aligned}
\]
The formulas agree at the boundaries. The optimizer invariant under exchange of cliques, simultaneous permutation of matched gateway pairs and independent permutations of nongateways in each clique is unique as an assignment to the actual edges. With \(\lambda_*=B/C_{k,m}\), its rates are \(\lambda_*\) times the following unit-gap rates:

| Edge class | Unit-gap rate |
| --- | --- |
| Gateway–gateway within either clique | \(a_* = \max\{0,1-mt_*/k\}/k\) |
| Gateway–nongateway within either clique | \(c_*=t_*/k\) |
| Matched interclique gateway links | \(b_*=((k+m)t_*-k)/[2k(t_*-1)]\) |
| Nongateway–nongateway within either clique | \(d_*=0\) |

Every optimum, symmetric or not, assigns zero to each nongateway–nongateway edge. Every optimum also assigns zero to each intracluster gateway–gateway edge if \(r\le s_k\), and assigns positive *total* conductance to that class if \(r>s_k\). For \(m=1\) the nongateway–nongateway class is empty. For example, \((k,m)=(8,5)\) is in the intermediate regime and \((2,1)\) in the last.

## Assumptions and scope

For an undirected edge \(ij\), the Laplacian contribution of weight \(w_{ij}\) is \(w_{ij}(e_i-e_j)(e_i-e_j)^\top\); the budget counts that edge once. We maximize \(\lambda_2\) on the full nonnegative edge-weight simplex, not only among invariant allocations. This is a continuous-time spectral-gap objective without degree normalization or stochastic row constraints. There is no general uniqueness claim outside the symmetry-invariant class. We make no claim for unequal clique orders, full matching \(m=0\), or \(k=1\).

## Proof

**Symmetry and spectrum.** On \(\mathbf1^\perp\), the smallest Rayleigh quotient of the Laplacian is the minimum of linear functions of its weights, so it is concave in the weights. Averaging an arbitrary optimum over the indicated automorphisms produces an invariant optimum with the same budget. Use rates \(a,b,c,d\) for the intracluster gateway, bridge, gateway–nongateway and intracluster nongateway classes, respectively. Their total weight is
\[
W=k(k-1)a+kb+2kmc+m(m-1)d.
\]
The zero-sum gateway coordinates have eigenvalues \(ka+mc\) and \(ka+mc+2b\), each of multiplicity \(k-1\), according as their patterns in the two cliques agree or are negatives under the matching. On zero-sum nongateway coordinates the eigenvalue is \(kc+md\), with multiplicity \(2(m-1)\). Among vectors constant on the vertex classes, the even sector has eigenvalues \(0,(k+m)c\); the odd sector is represented in gateway and nongateway coordinates by
\[
Q=\begin{pmatrix}mc+2b&-mc\\-kc&kc\end{pmatrix}.
\]
The odd block is symmetric after conjugation by \(\operatorname{diag}(\sqrt{k},\sqrt m)\), and the dimensions of the sectors sum to \(2(k+m)\).

**Minimum unit-gap budget.** Homogeneity reduces the problem to minimizing \(W\) with \(\lambda_2\ge1\). Necessarily \(c>0\) for connectivity; since the odd block has a nonzero off-diagonal entry in its symmetric coordinates, its smaller eigenvalue is strictly less than \(kc\). Thus \(t=kc>1\). The lower-right entry of \(Q-I\) in symmetric coordinates is then positive, so positive semidefiniteness is equivalent to
\[
\det(Q-I)=1-(k+m)c+2b(kc-1)\ge0,
\qquad b\ge \frac{(k+m)t-k}{2k(t-1)}.
\]
The other effective constraint is \(ka+mc\ge1\), or \(a\ge k^{-1}\max\{0,1-mt/k\}\); all remaining nonconstant eigenvalues are at least one under these two bounds and nonnegativity. At fixed \(t\), the least cost comes from equality in the bounds on \(a,b\) and setting \(d=0\) for any nongateway–nongateway edges. Substitution yields the first displayed formula for \(C_{k,m}\) with \(t_*\) replaced by \(t\). This function of \(t>1\) is strictly convex, since \(m/[2(t-1)]\) is strictly convex and the positive part is convex. For \(t\ge r\) its smooth-branch derivative is \(2m-m/[2(t-1)^2]\), vanishing at \(3/2\); for \(1<t\le r\) it is \(m(1+1/k)-m/[2(t-1)^2]\), vanishing at \(s_k\). Comparing these points with the kink at \(r\) proves the regimes and uniqueness of \(t_*\). Equality in the cost bounds then fixes every invariant rate. Scaling the unit-gap optimum gives the claimed result at budget \(B\).

**Support without symmetry.** Averaging any optimizer must give the unique invariant optimum. A class whose average rate is zero has every original rate zero by nonnegativity; a class whose average is positive has positive original total. This proves the support assertions.

## Verification

The companion `verify_spectral.py` can be run with Python and NumPy. It assembles the full Laplacian for 156 pairs \(2\le k\le13,1\le m\le13\) and checks the unit gap, equivalent cost expressions in the code, trace-to-budget identity, and nearby scalar perturbations. These numerical tests are supplementary; the block decomposition and strict-convexity argument prove the complete parameter range.

## Relationship to prior work and limitations

The continuous-time optimization framework is established by Sun, Boyd, Xiao and Diaconis [1] and Göring, Helmberg and Wappler [2]; symmetry reduction is also standard in fastest-mixing problems. The closely related complete-biclique gateway theorem [3] replaces the matching by all \(k^2\) interclique gateway edges. Its odd orbit-constant block is the same after matching each gateway's total cross conductance, but a zero-sum gateway fluctuation in each clique gets a positive cross-degree contribution there. For the matching, that contribution is zero in the equal-across-layers sector. This changes the feasible design precisely where the missing contribution matters.

In particular, for \(r\le3/2\), the complete-biclique budget optimum is \(2B/(k+9m)\) by [3] (its low-ratio case is \(m/k\ge1/6\)). It is an upper bound for any subgraph allocation. Moving the biclique optimal cross weight onto the matching, preserving each gateway's cross degree, leaves the orbit-constant eigenvalues unchanged. The other potentially binding matching eigenvalue, in unit-gap scaling, is \(mc_*=3m/(2k)\ge1\), so this upper bound is attainable. Thus the low-ratio branch is also a corollary of [3] with this feasibility check. In contrast, already at \((k,m)=(2,1)\) the matching cost is \(4+\sqrt3\), strictly greater than the biclique cost \(11/2\). The two higher-ratio regimes and the matching-specific gateway activation threshold are not the biclique thresholds.

The later indexed partial-matching result [4] has the same graph on its domain but optimizes the second-largest eigenvalue modulus over symmetric row-stochastic matrices. Its local row constraints and treatment of the negative spectrum differ from the single conductance budget here. The available publisher description of Allison–Shader [5] identifies a fastest-mixing Markov chain for a union of two cliques; its full text was not inspected, so a finer comparison of its graph and constraints is unresolved. No claim of exhaustive priority is made.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, [DOI 10.1137/S0036144504443821](https://doi.org/10.1137/S0036144504443821).
2. F. Göring, C. Helmberg and M. Wappler, *Embedded in the Shadow of the Separator*, [public preprint](https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf).
3. *Sharp three-regime spectral-gap allocation for two cliques with a biclique gateway*, [Resultary record 901311831846](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-three-regime-spectral-gap-allocation-for-two-cliques-with--901311831846/RESULT.md), Finding and Proof §§2–3.
4. *Exact fastest symmetric mixing through a partial matching between two cliques*, [Resultary record 18bf18376a63](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-fastest-symmetric-mixing-through-a-partial-matching-betwee--18bf18376a63/RESULT.md), Finding and Assumptions.
5. M. Allison and B. Shader, *Fastest Mixing Markov Chain Problem for the Union of Two Cliques*, Linear and Multilinear Algebra 59 (2011), 801–823, [DOI 10.1080/03081087.2010.538690](https://doi.org/10.1080/03081087.2010.538690), publisher description only.
