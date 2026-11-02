# A two-parameter Poisson–Gaussian threshold for idempotent generation of random Rees semigroups

## Finding

Let \(p\) be a fixed prime. Form an \(N\)-by-\(N\) Rees zero-matrix semigroup over the additive elementary abelian group \(G_N=\mathbb F_p^{d_N}\). Independently retain each potential nonzero sandwich entry with probability
\[
\theta_N=\frac{\log N+c}{N},
\]
and give each retained entry an independent uniform value in \(G_N\). Here \(c,t\in\mathbb R\) are fixed, \(N\) tends to infinity, and
\[
\mu_N=N^2\theta_N,\qquad
\sigma_N=\sqrt{N^2\theta_N(1-\theta_N)},\qquad
 d_N=\left\lfloor\mu_N-2N+1+t\sigma_N\right\rfloor.
\]
For sufficiently large \(N\), the specified probability and group dimension are admissible. Let \(S_N\) be this finite Rees zero-matrix semigroup, including its absorbing zero, and let \(E(S_N)\) be its idempotents. Then
\[
\boxed{\lim_{N\to\infty}\Pr\bigl(\langle E(S_N)\rangle=S_N\bigr)
=\exp(-2e^{-c})\,[1-\Phi(t)]},
\]
where \(\Phi\) denotes the standard normal distribution function. The two factors arise independently: a Poisson obstruction from isolated vertices of the random bipartite support, and a Gaussian obstruction from fluctuations in its cycle-space dimension. This limit is independent of the fixed prime \(p\).

An exact finite structural law underlies this limit. For arbitrary nonempty finite index sets \(I,\Lambda\), a fixed bipartite support graph \(\Gamma\) on \(I\sqcup\Lambda\), and independent uniform labels in \(\mathbb F_p^d\), let \(C\) range over its connected components containing at least one edge. Write \(a_C=|C\cap I|\), \(b_C=|C\cap\Lambda|\), and \(\beta_C=|E(C)|-|V(C)|+1\). Independently for these components, let \(\rho_C\) have the rank of a uniform \(d\)-by-\(\beta_C\) matrix over \(\mathbb F_p\). Then the size of the idempotent-generated subsemigroup has the exact conditional distribution
\[
\boxed{|\langle E(S)\rangle|\ \stackrel{\mathrm d}{=}\ 1+\sum_C a_C b_C p^{\rho_C}}.
\]
In particular, if \(\Gamma\) has no isolated vertices, \(S\) is idempotent-generated precisely when \(\Gamma\) is connected and the cycle-label map is surjective. The same criterion holds for arbitrary supports, because isolated index vertices prevent generation of all nonzero triples. Given a connected support of cycle rank \(\beta\), the success probability is exactly
\[
F_{p,d}(\beta)=
\begin{cases}
\displaystyle\prod_{j=0}^{d-1}(1-p^{j-\beta}),&\beta\ge d,\\
0,&\beta<d.
\end{cases}
\]
For \(0\le k\le\min(d,\beta)\), the component-rank probabilities are
\[
\Pr(\rho_C=k)=p^{-d\beta_C}
\frac{\displaystyle\prod_{j=0}^{k-1}(p^d-p^j)(p^{\beta_C}-p^j)}
{\displaystyle\prod_{j=0}^{k-1}(p^k-p^j)}.
\]
Empty products equal one, including when \(\beta_C=0\). Thus, for independent Bernoulli support with retention parameter \(\theta\), the exact generation probability is the finite sum
\[
\sum_{\substack{B\subseteq K_{a,b}\\B\text{ connected}}}
\theta^{|E(B)|}(1-\theta)^{ab-|E(B)|}
F_{p,d}(|E(B)|-a-b+1).
\]
This formula includes nonregular Rees zero-matrix realizations in the ambient ensemble, but only connected—and hence regular—realizations can contribute.

## Assumptions and scope

A Rees zero-matrix semigroup \(S=\mathcal M^0[G;I,\Lambda;P]\) has underlying set \((I\times G\times\Lambda)\sqcup\{0\}\). Its multiplication, using additive notation for \(G\), is
\[
(i,g,\lambda)(j,h,\mu)=
\begin{cases}
(i,g+P_{\lambda j}+h,\mu),&P_{\lambda j}\in G,\\
0,&P_{\lambda j}\text{ is the structural zero}.
\end{cases}
\]
The absorbing zero is distinct from the zero vector of \(G\). The support is the bipartite graph whose edge \((j,\lambda)\) exists exactly when \(P_{\lambda j}\in G\). All results are for finite index sets, finite elementary abelian \(p\)-groups, independently uniform retained-edge labels, and the specified probability distribution on supports. The limiting result fixes \(p,c,t\); its internal group dimension grows with \(N\). No assertion is made for nonabelian groups or nonuniform labels.

## Proof

**1. Idempotents and cycle gains.** An edge \((i,\lambda)\) supports the unique nonzero idempotent \((i,-P_{\lambda i},\lambda)\). Products of such idempotents follow walks in the bipartite support. Fix a spanning forest. Gauge changes obtained by adding vertex potentials send every forest-edge group label to zero without changing the semigroup's isomorphism type or the cardinality of its idempotent-generated subsemigroup. Each remaining edge gives a fundamental cycle gain, and the linear span \(H_C\) of those gains is the subgroup of cycle values in its component. For any choice of \(i\in I\cap C\) and \(\lambda\in\Lambda\cap C\), products of idempotents with these outside indices have as group-coordinate set an affine coset of \(H_C\): a path from \(i\) to \(\lambda\) gives one value, and inserting closed walks gives the entire coset. There is no nonzero product between different components, and isolated vertices are never outside indices of nonzero idempotent products. Consequently
\[
|\langle E(S)\rangle|=1+\sum_C a_Cb_C|H_C|.
\]
This is the finite path-value/Graham–Howie description specialized to elementary abelian labels, not an independently claimed new deterministic semigroup theorem.

**2. Exact conditional distribution.** On a fixed component with \(v_C\) vertices and \(e_C\) edges, a spanning tree has \(v_C-1\) edges; there are \(\beta_C=e_C-v_C+1\) remaining edges. Gauge normalization is an invertible linear coordinate transformation of the full edge-label space, so their residual labels are independent and uniform in \(\mathbb F_p^d\), also independently between components. Thus \(\dim H_C=\rho_C\) has exactly the rank distribution of a uniform \(d\)-by-\(\beta_C\) matrix. Counting ordered bases for rank-\(k\) linear maps gives the displayed product formula. In a connected support, every outside index pair occurs, so \(\langle E(S)\rangle=S\) is equivalent to \(\dim H_C=d\), yielding \(F_{p,d}(\beta)\). An isolated support vertex cannot occur in any nonzero idempotent product, proving the same equivalence in the unrestricted support ensemble. Summing over connected Bernoulli supports yields the exact finite probability formula.

**3. Isolated-vertex Poisson law and connectivity.** In the balanced random support put \(Y_L\) and \(Y_R\) for the numbers of isolated vertices on each side, and \(M_N\) for the number of retained edges. Let
\[
Z_N=(M_N-\mu_N)/\sigma_N.
\]
For fixed nonnegative integers \(l,r\), the event that specified \(l\) left and \(r\) right vertices are isolated forbids exactly \(N(l+r)-lr\) independent edges. Consequently
\[
\mathbb E[(Y_L)_l(Y_R)_r]
=(N)_l(N)_r(1-\theta_N)^{N(l+r)-lr}
\longrightarrow e^{-c(l+r)}.
\]
Here \((y)_k\) denotes a falling factorial. Hence \((Y_L,Y_R)\) converges to a pair of independent \(\operatorname{Pois}(e^{-c})\) variables.

For completeness, with probability tending to one there is no disconnected component containing an edge unless an isolated vertex also exists. Indeed, if a disconnected graph has no isolates, it has a component with \(l\ge1\) left vertices and \(r\ge1\) right vertices, \(s=l+r\le N\). A connected bipartite component contains a spanning tree, and \(K_{l,r}\) has \(l^{r-1}r^{l-1}\le s^{s-2}\) spanning trees. The union bound gives
\[
\sum_{s=2}^N\ \sum_{l+r=s}
\binom Nl\binom Nr s^{s-2}\theta_N^{s-1}
(1-\theta_N)^{Ns-2lr}.
\]
Since \(\binom Nl\binom Nr\le(2eN/s)^s\), \(2lr\le s^2/2\), and \(N\theta_N=\log N+c\), the sum is \(o(1)\). More explicitly, for \(s\le N/4\) it is bounded by a geometric series with base \(O((\log N)N^{-7/8})\), multiplied by \(O(N/\log N)\); for \(s>N/4\) its base is \(O((\log N)N^{-1/2})\). Thus connectivity and the absence of isolates are asymptotically equivalent events.

**4. Independence of the Poisson and Gaussian obstructions.** Ordinary binomial central-limit theory gives \(Z_N\Rightarrow Z\sim\mathcal N(0,1)\). Conditional on any prescribed \(l+r\) isolated vertices, the remaining edge count is binomial on \((N-l)(N-r)\) possible edges. Its mean differs from \(\mu_N\) by at most \(O_{l,r}(\log N)\), which is \(o(\sigma_N)\); its variance is asymptotic to \(\sigma_N^2\). Therefore, for every real \(u\),
\[
\mathbb E[(Y_L)_l(Y_R)_r e^{iuZ_N}]
\longrightarrow e^{-c(l+r)}e^{-u^2/2}.
\]
The mixed factorial-moment/characteristic-function criterion implies joint convergence of \((Y_L,Y_R,Z_N)\) to the two independent Poisson variables and an independent standard Gaussian \(Z\). In particular,
\[
\lim_{N\to\infty}\Pr(\Gamma_N\text{ connected},Z_N>t)
=e^{-2e^{-c}}[1-\Phi(t)].
\]

**5. The group-generation threshold.** On connected supports, the cycle rank is exactly \(\beta_N=M_N-2N+1\). By construction \(d_N=\lfloor\mu_N-2N+1+t\sigma_N\rfloor\), so \((\beta_N-d_N)/\sigma_N=Z_N-t+o(1)\). When \(\beta_N<d_N\), surjectivity is impossible. When \(\beta_N\ge d_N\), the union bound on deficient random-matrix ranks gives
\[
1-F_{p,d_N}(\beta_N)
\le\sum_{j=0}^{d_N-1}p^{j-\beta_N}
\le\frac{p^{d_N-\beta_N}}{p-1}.
\]
Away from \(|Z_N-t|\le\varepsilon\), this failure probability tends uniformly to zero whenever \(Z_N>t+\varepsilon\), and success is impossible whenever \(Z_N<t-\varepsilon\). The boundary probability tends to \(\Phi(t+\varepsilon)-\Phi(t-\varepsilon)\), which vanishes as \(\varepsilon\downarrow0\). Combining this with Step 4 proves the stated Poisson–Gaussian product limit.

## Verification

The accompanying Python file `verify.py` constructs Rees multiplication directly and enumerates the subsemigroup generated by all idempotents, without using the claimed size or rank formula in the closure computation. It exhaustively checks every zero-support/edge-label configuration for \(2\)-by-\(2\) and \(2\)-by-\(3\) matrices over \(\mathbb F_2\) in dimensions one and two, and independently tests \(\mathbb F_3\) and \(\mathbb F_5\) in dimension one. For example, with a full \(2\)-by-\(3\) support over \(\mathbb F_2^2\), the cycle rank is two; exactly \(1536\) of the \(4^6\) edge assignments generate the full semigroup, consistent with the uniform-matrix rank formula and the three tree-edge gauge degrees of freedom. This finite enumeration verifies finite cases only. The infinite-N probability limit follows from the mathematical argument above, not from simulation.

## Relationship to prior work

Graham's structural theorem, Howie's 1978 path-value theorem, and Houghton's 1978 cycle-space/cohomology classification already provide the deterministic component and cycle-gain mechanism; the exact conditional rank probabilities further use the standard finite-field random-matrix rank count. These are **inputs**, not newly claimed deterministic discoveries. Quinn-Gregson's 2019 preprint and the 2020 elementary Graham-theorem treatment give modern algebraic contexts for the same Rees machinery. The specific conclusion assessed here is the **jointly tuned sparse-support, growing-group limit**, which puts the isolated-vertex Poisson obstruction and the surplus-cycle Gaussian obstruction on the same nontrivial probability scale. None of the inspected source statements gives this two-parameter joint limit. A more general random gain-graph or random-cocycle theorem could subsume it and remains a priority risk.

## Limitations

The asymptotic law fixes the prime and the two real window parameters and uses balanced bipartite supports, independent Bernoulli edges, and independent uniform vector labels. The result is about the chance that *all elements* are generated by idempotents, not the minimal number of idempotent generators. Although the ambient random Rees semigroup can be nonregular when an isolated support vertex appears, successful instances are regular. The exact conditional description extends to arbitrary finite bipartite supports, including isolated vertices. Publication priority requires independent literature review; the result has not undergone independent mathematical validation.

## References

1. T. Quinn-Gregson, *Homogeneous completely simple semigroups*, arXiv:1908.10665, first public version 28 August 2019, https://arxiv.org/abs/1908.10665.
2. J. M. Howie, *Idempotents in completely 0-simple semigroups*, Glasgow Mathematical Journal 19 (1978), 109–113, https://doi.org/10.1017/S0017089500003475.
3. C. H. Houghton, *Finite zero-simple semigroups over an elementary abelian group*, Bulletin of the Australian Mathematical Society 18 (1978), 211–220, https://doi.org/10.1017/S0004972700008029.
4. A. Ballester-Bolinches and V. Pérez-Calabuig, *An elementary proof of a theorem of Graham on finite semigroups*, Mathematics 8 (2020), 105, https://doi.org/10.3390/math8010105.
5. R. D. Gray, *The minimal number of generators of a finite semigroup*, arXiv:1307.8280, first public version 31 July 2013, https://arxiv.org/abs/1307.8280.
