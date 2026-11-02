# Non-Gaussian centralizer fluctuations in complete bipartite incidence algebras

## Finding

For every prime power \(q\) and every \(n\ge1\), let \(P_n\) be the height-two poset with \(n\) labeled minimal vertices \(u_1,\ldots,u_n\), \(n\) labeled maximal vertices \(v_1,\ldots,v_n\), and all \(u_i<v_j\). Write \(A_n=I(P_n,\mathbb F_q)\). For \(a\in A_n\), write its diagonal entries as \(d_1,\ldots,d_n,e_1,\ldots,e_n\) and its strict comparable-pair entries as \(x_{ij}\). Define

\[
S(a)=\#\{(i,j):d_i=e_j\}.
\]

Let \(G(a)\) be the graph on the \(2n\) poset vertices with an edge \(u_iv_j\) precisely when \(d_i=e_j\) and \(x_{ij}\ne0\). Include isolated vertices in its number \(\kappa(a)\) of connected components. The exact centralizer identity is

\[
\boxed{\dim_{\mathbb F_q}C_{A_n}(a)=S(a)+\kappa(a),\qquad |C_{A_n}(a)|=q^{S(a)+\kappa(a)}.}
\]

For a uniformly random \(a\in A_n\) and **fixed** field size \(q\), the component count satisfies \(\Pr\{\kappa(a)=q\}=1-O_q(e^{-c_qn})\) for some \(c_q>0\). Moreover,

\[
\boxed{\frac{\log_q|C_{A_n}(a)|-n^2/q-q}{n}\ \xrightarrow{\mathrm d}\ Y_q=\frac1q\sum_{h=1}^{q-1}Z_hW_h,}
\]

where the \(2(q-1)\) random variables \(Z_h,W_h\) are independent standard real Gaussians. Thus the limiting characteristic function is

\[
\boxed{\mathbb E e^{itY_q}=(1+t^2/q^2)^{-(q-1)/2}}.
\]

The limit is non-Gaussian for each fixed \(q\ge2\). As finite identities, \(\mathbb E S(a)=n^2/q\) and \(\operatorname{Var}S(a)=n^2(q-1)/q^2\).

## Assumptions and scope

The algebra \(A_n\) is a unital, split-basic, radical-square-zero \(\mathbb F_q\)-algebra of vector-space dimension \(n^2+2n\); it is also the path algebra of the complete bipartite quiver with every arrow directed from minimal to maximal vertices. Its coordinates are independent and uniform when \(a\) is sampled uniformly. The centralizer \(C_{A_n}(a)\) is the entire \(\mathbb F_q\)-linear commutant \(\{b\in A_n:ab=ba\}\), including its center. The asymptotics take \(n\to\infty\) while \(q\) stays fixed; no assertion is made for fields growing with \(n\).

## Proof

**Exact centralizer formula.** Write a second element as \(b=(f_i,g_j,y_{ij})\) in the same diagonal/radical coordinates. Since the poset has height two, the \((i,j)\) entry of \(ab-ba\) is

\[
(d_i-e_j)y_{ij}-(f_i-g_j)x_{ij}.
\]

The diagonal entries of the commutator vanish identically. For each pair with \(d_i\ne e_j\), the commutator equation determines \(y_{ij}\) uniquely from the freely chosen diagonal coordinates \(f_i,g_j\). For every pair with \(d_i=e_j\), the coordinate \(y_{ij}\) is free, and if also \(x_{ij}\ne0\) the diagonal constraint is \(f_i=g_j\). The dimension of the space of vertex labels \((f_i,g_j)\) constant along every edge of \(G(a)\) is exactly its number of connected components \(\kappa(a)\). The independent free \(y\)-coordinates number \(S(a)\). This proves both finite centralizer identities, including isolated vertices and the cases \(n=1\) and characteristic two.

**The component event.** Conditional on the diagonal labels, let \(L_c\) and \(R_c\) count vertices of color \(c\in\mathbb F_q\) on each side. For each \(c\), the induced graph is an independent bipartite random graph on \(L_c,R_c\) vertices, with each cross-edge present with probability \(1-1/q\). There are no edges between different colors. For fixed \(q\), elementary binomial tail bounds give

\[
\Pr\{\min_c(L_c,R_c)<n/(2q)\}=O_q(e^{-c'_qn}).
\]

For bipartition sizes \(a,b\ge n/(2q)\), the probability of disconnection is bounded by the explicit cut union bound

\[
\sum_{\substack{0\le h\le a,\ 0\le k\le b\\1\le h+k\le(a+b)/2}}
\binom ah\binom bk q^{-h(b-k)-(a-h)k},
\]

where each disconnected graph has a component containing at most half of the vertices. On this summation range the crossing-edge count is at least \(\tfrac12\min(a,b)(h+k)\); hence the sum is \(O_q(e^{-c''_qn})\) uniformly over sizes between \(n/(2q)\) and \(n\). A union bound across the fixed \(q\) colors shows that all color graphs are connected with probability \(1-O_q(e^{-c_qn})\). Each color then contributes one component, proving \(\kappa(a)=q\) with this probability.

**Non-Gaussian scaling.** The left and right color-occupancy vectors \(L=(L_c)\) and \(R=(R_c)\) are independent multinomials with \(n\) trials and equiprobable \(q\) colors. Write

\[
U_n=\frac{L-(n/q)\mathbf1}{\sqrt n},\qquad V_n=\frac{R-(n/q)\mathbf1}{\sqrt n}.
\]

Their coordinate sums vanish exactly. Therefore, without an approximation,

\[
S(a)=\sum_c L_cR_c=\frac{n^2}{q}+n\langle U_n,V_n\rangle.
\]

The multinomial central limit theorem yields independent Gaussian vector limits with common covariance \(\Sigma=q^{-1}I-q^{-2}\mathbf1\mathbf1^T\). This covariance is zero on the constant vector and equals \(q^{-1}\) times the identity on its \((q-1)\)-dimensional orthogonal complement. Thus the continuous mapping theorem gives \(\langle U_n,V_n\rangle\Rightarrow q^{-1}\sum_{h=1}^{q-1}Z_hW_h\). The exponentially small component exception makes \((\kappa(a)-q)/n\to0\) in probability. Slutsky's theorem gives the displayed centralizer limit.

Conditioning on one Gaussian in each independent pair gives \(\mathbb E[e^{itZ_hW_h/q}]=(1+t^2/q^2)^{-1/2}\), proving the characteristic function. Its nonzero fourth cumulant \(6(q-1)/q^4\) distinguishes the limit from a Gaussian. Finally, \(S=\sum_{i,j}\mathbf1_{\{d_i=e_j\}}\) has \(n^2\) Bernoulli summands of mean \(1/q\) which are pairwise uncorrelated, including summands sharing one endpoint. This yields the exact mean and variance.

## Verification

The standalone `verify.py` implements multiplication in the algebra and independently reconstructs each commutant by finite-field Gaussian elimination of the actual commutator map. This is compared with a disjoint-set component count. Fully exhaustive checks cover \((q,n)=(2,1),(2,2),(3,1)\); in all cases the script additionally counts commuting partners directly, without using the dimension formula. Sampled direct-rank checks cover \((q,n)=(2,3),(3,2),(5,2)\). Separate exact enumeration of diagonal occupancies verifies the formulas for \(\mathbb ES\) and \(\operatorname{Var}S\) for \(q=2,3,5\) and \(n=1,2,3,4\). Run `python3 verify.py` and expect a final `VERIFY_OK` line. Finite tests corroborate the exact identity, not the infinite central limit argument, whose proof appears above.

## Relationship to prior work

Cheraghpour, Ghosseiri, Jafari and Seyfpour (arXiv:2402.12619v1, publicly posted 20 February 2024) determine centralizers and commuting-graph parameters of the \(2\times2\) upper triangular ring over a finite field. That case is \(A_1\) here, and is not claimed as new. Green and Schroll (arXiv:2302.08169) describe commuting algebras of quivers and their relation to incidence algebras; this gives background structural context, not a random-element centralizer limit. Can (arXiv:2105.09826) studies incidence monoid automorphisms and torus complexity, not these finite-field centralizer fluctuations. The published finite Kronecker-path-algebra commutator-fiber result treats a two-vertex family, rather than complete bipartite growing-vertex algebras. The present assertion is the graph-component centralizer identity for arbitrary \(n\) coupled to the non-Gaussian \(n\)-scale limit; it does not claim priority for elementary multinomial CLTs or Gaussian-product characteristic functions.

## Limitations

The large-\(n\) statement is for fixed finite field size. It concerns uniformly selected algebra elements, not units or idempotents and not the graph on noncentral elements alone. The exact centralizer formula is deterministic, while exponential connectivity and the limiting law are probabilistic. Priority remains subject to possible equivalent statements in the older incidence-algebra, random-graph, and random-commutant literature. No independent external audit is asserted.

## References

1. H. Cheraghpour, M. N. Ghosseiri, M. Jafari, F. Seyfpour, *On Commuting Graphs of Triangular Rings*, arXiv:2402.12619v1 (20 February 2024), https://arxiv.org/html/2402.12619v1.
2. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169v3 (first posted 16 February 2023), https://arxiv.org/html/2302.08169v3.
3. M. Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826 (first posted 20 May 2021), https://arxiv.org/abs/2105.09826.
