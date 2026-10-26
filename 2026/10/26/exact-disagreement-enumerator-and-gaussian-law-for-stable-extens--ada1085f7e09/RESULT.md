# Exact disagreement enumerator and Gaussian law for stable extensions of symmetric cycles

## Finding

Fix an integer \(n\ge3\). Let \(F_n\) be the abstract argumentation framework on vertices \(\mathbb Z/n\mathbb Z\) with exactly the two opposite attacks along each edge of the undirected cycle \(C_n\). Write \(\operatorname{Stab}(F_n)\) for its stable extensions, and define the **ordered-pair disagreement polynomial**
\[
D_n(t)=\sum_{A,B\in\operatorname{Stab}(F_n)}t^{|A\triangle B|}.
\]
For formal variables \(z,t\), let
\[
\begin{aligned}
P(z,t)&=1+tz-t^2z^3,\\
Q(z,t)&=1-tz-z^2+(t-1-t^2)z^3+tz^4-t^2z^5+t^2z^6.
\end{aligned}
\]
The complete distance distribution of stable-extension pairs has the **factored rational generating function**
\[
\boxed{\displaystyle \sum_{n\ge3}D_n(t)z^n
=-z\frac{\partial}{\partial z}\log(P(z,t)Q(z,t))-2(1+t^2)z^2.}
\]
This is interpreted as a formal power series about \(z=0\). The correction subtracts the length-two closed walks (there are no length-one closed walks), for which the simple cycle \(C_2\) is not defined. In particular, writing \(p_3=3,p_4=2,p_5=5\), and \(p_n=p_{n-2}+p_{n-3}\), one has \(D_n(0)=p_n\) and \(D_n(1)=p_n^2\).

For every \(n\ge3\), the maximum disagreement of two stable extensions equals \(n\) when \(n\) is even and \(n-1\) when \(n\) is odd. Exactly **two ordered pairs** achieve it for even \(n\), and exactly **\(2n\) ordered pairs** achieve it for odd \(n\).

Let \(A_n,B_n\) be independent uniform stable extensions, and \(H_n=|A_n\triangle B_n|\). If \(\rho\) is the unique positive root of \(\rho^3=\rho+1\), define
\[
\mu=\frac{12+2\rho-2\rho^2}{23}=0.4843339383\ldots,
\qquad
\sigma^2=\frac{2(1683\rho^2+385\rho-294)}{12167}=0.5209954016\ldots .
\]
Then \(\sigma^2>0\),
\[
\mathbb E H_n=\mu n+O(1),\qquad
\operatorname{Var}(H_n)=\sigma^2 n+O(1),
\]
and
\[
\boxed{\displaystyle \frac{H_n-\mu n}{\sqrt{\sigma^2 n}}
\ \xrightarrow[n\to\infty]{\rm distribution}\ \mathcal N(0,1).}
\]
All asymptotic statements concern the fixed bidirected cycle family and independent uniformly selected stable extensions, not arbitrary attack graphs.

## Assumptions and scope

There are \(n\ge3\) *labelled, cyclically ordered* vertices with a mutual attack in each cycle edge and no self-attacks or additional attacks. A stable extension is conflict-free and attacks every vertex not in it. For a symmetric irreflexive attack graph, this is precisely a maximal independent set. Pairs are ordered and may coincide. The coefficient of \(t^d\) in \(D_n\) is therefore a nonnegative integer counting pairs at symmetric-difference distance \(d\). In the probabilistic assertion the pair is chosen uniformly from the Cartesian square of the extension set. The constants \(\mu,\sigma^2\) are absolute; there is no moving graph or parameter regime.

## Proof

**1. Local coding.** Encode an extension \(A\) by cyclic bits \(a_i=\mathbf1_{i\in A}\). Independence means that \(11\) never occurs at consecutive positions. Maximality means each absent vertex has a present neighbor, equivalently \(000\) never occurs at three consecutive cyclic positions. Conversely these two local prohibitions suffice. Consequently an ordered pair \((A,B)\) corresponds bijectively to a cyclic word \(c_i=(a_i,b_i)\) over \(\{0,1\}^2\) with the two prohibitions separately in each coordinate, weighted \(\prod_i t^{a_i\oplus b_i}\).

**2. Transfer and exact denominator.** Index sixteen states by \(((a,b),(c,d))\), where each displayed pair is a symbol of two bits. Place an edge from state \((u,v)\) to \((v,w)\) precisely when, for each coordinate \(j\in\{1,2\}\), neither \(u_j=v_j=1\) nor \(u_j=v_j=w_j=0\). Give it weight \(t\) if \(w_1\ne w_2\), and weight \(1\) otherwise. Let \(T(t)\) be the resulting sixteen-by-sixteen integer-polynomial matrix. The closed length-\(n\) walks encode exactly the labelled cyclic pair words and include each once (the starting state is fixed by the entries indexed at positions \(0,1\)). Therefore
\[
D_n(t)=\operatorname{tr}(T(t)^n)\qquad(n\ge3).
\]
The finite polynomial identity, verifiable by exact matrix algebra, is
\[
\det(I-zT(t))=P(z,t)Q(z,t).
\]
For completeness, a reproducible derivation uses the sixteen trace polynomials \(s_j(t)=\operatorname{tr}(T(t)^j)\) and the Newton identities \(kd_k=-\sum_{j=1}^ks_jd_{k-j}\), starting at \(d_0=1\): the resulting characteristic coefficients coincide term-for-term with the product above, and all coefficients of \(z^{10}\) through \(z^{16}\) vanish. This calculation uses only integer addition and multiplication, with exact divisions guaranteed by the identity. Taking the formal logarithmic derivative of the determinant yields
\[
-z\partial_z\log\det(I-zT)=\sum_{n\ge1}\operatorname{tr}(T^n)z^n.
\]
There are no length-one closed walks and there are exactly \(2+2t^2\) weighted length-two closed walks. Removing these gives the displayed generating function. At \(t=0\), the determinant specializes to \(1-z^2-z^3\), giving the known Perrin recurrence for maximal independent sets. At \(t=1\), independence of the two unweighted choices gives \(p_n^2\).

**3. Maximum and its multiplicity.** Always \(H_n\le n\). Equality means every vertex lies in exactly one of the two independent sets, hence gives a proper two-coloring of the connected cycle. This exists if and only if \(n\) is even, with exactly two color assignments and therefore two ordered extremal pairs. If \(n\) is odd, a pair of distance \(n-1\) is made by leaving one vertex in neither set and alternately assigning its remaining \(n-1\) path vertices to the two sets. Each set is independent; the omitted vertex is adjacent to one vertex in each set because the path has even length, so both sets dominate the omitted vertex and are maximal. There are \(n\) choices of omitted vertex and two alternating assignments, yielding \(2n\) ordered pairs. Any distance-\(n-1\) pair on an odd cycle must be of this form since exactly one vertex is outside their symmetric difference; if that vertex belonged to both sets, the rest would alternate, and both its neighbors would have to be absent from both sets by independence, contradicting the distance. Hence that vertex belongs to neither, forcing the described alternating path. This also proves optimality for odd \(n\).

**4. Limit law.** At \(t=1\), the recurrent part of the one-coordinate memory-two shift is the three-state directed graph \(00\to01\to10\to\{00,01\}\); its closed walks have lengths two and three, so it is irreducible and aperiodic. The recurrent part of \(T(1)\) is its synchronous tensor square, hence primitive. The other seven states are transient. Perron--Frobenius theory therefore supplies a unique simple dominant eigenvalue \(\lambda(1)=\rho^2\), since the one-coordinate Perrin recurrence has growth root \(\rho\). The same entry pattern and positivity for \(t>0\) imply a simple dominant eigenvalue \(\lambda(t)\), analytic for \(t\) near \(1\). If \(z(t)=1/\lambda(t)\), then \(Q(z(t),t)=0\), \(z(1)=\rho^{-2}\), and \(P(\rho^{-2},1)\ne0\). Uniform spectral separation in a neighborhood of \(t=1\) gives
\[
\mathbb E e^{sH_n}=\frac{D_n(e^s)}{D_n(1)}
=\left(\frac{\lambda(e^s)}{\lambda(1)}\right)^n(1+O(\theta^n))
\]
for complex \(s\) sufficiently close to zero and some \(\theta<1\). Let \(E=t\partial_t\) and \(Z=z\partial_z\). Implicit differentiation of \(Q(z(t),t)=0\) yields
\[
\mu=\left.\frac{EQ}{ZQ}\right|_{(\rho^{-2},1)},\qquad
\sigma^2=\left.\left(E-\mu Z\right)\frac{EQ}{ZQ}\right|_{(\rho^{-2},1)}.
\]
Reducing powers of \(\rho\) with \(\rho^3=\rho+1\) gives exactly the two displayed algebraic constants; in particular \(\sigma^2>0\). Differentiating the analytic log moment generating function gives the stated mean and variance. Substituting \(s=iu/\sqrt{\sigma^2 n}\) and expanding its logarithm to second order shows convergence of characteristic functions to \(e^{-u^2/2}\), proving the central limit theorem. The bounded exponential spectral remainder controls the derivatives needed for the \(O(1)\) assertions.

## Verification

The included standalone `checker.py` constructs the transfer matrix from the stated local prohibitions, computes its first sixteen trace polynomials with integer arithmetic, recovers its determinant via Newton identities, and verifies exactly the factored polynomial identity. Independently it enumerates all maximal independent subsets and ordered pairs on each cycle from length \(3\) through \(16\), checking every distance coefficient, diagonal Perrin counts, and the extremal multiplicities. Execution with Python 3 standard library produced `ALL_CHECKS_OK`. These finite tests corroborate, but do not replace, the arbitrary-length transfer proof or the analytic Perron--Frobenius argument.

For example,
\[
\begin{aligned}
D_3(t)&=3+6t^2,\\
D_4(t)&=2+2t^4,\\
D_5(t)&=5+10t^2+10t^4,\\
D_6(t)&=5+12t^3+6t^4+2t^6.
\end{aligned}
\]

## Relationship to prior work

Fichte, Hecher, Mahmood, and Wang (2026) introduced and studied distance-based diversity of extensions, including stable extensions and computational-complexity classifications. Their definitions and motivating problem are prior work; their main theorems do not state the cycle-specific ordered-pair enumerator or Gaussian fluctuations. Bisdorff and Marichal (2007/2008) give the Perrin enumeration and orbit formulas for single maximal independent sets of cycles. Jou and Lin (2018) give a constructive algorithm enumerating those sets. The local binary-word encoding and the identity \(D_n(1)=p_n^2\) are thus rooted in known results. The distinguishing assertion here is the factorized two-replica distance polynomial for every cycle length together with explicit variance and the normal law of disagreement. An exhaustive enumeration of single extensions is not itself a formula for their pair-distance distribution or its asymptotic fluctuations.

## Limitations

The formula is not claimed for directed one-way cycles, paths, chorded cycles, general symmetric graphs, more than two sampled extensions, or other argumentation semantics. The Gaussian statement concerns fixed unweighted cycles as their length tends to infinity. The method is a standard transfer-matrix method, not a new general counting paradigm. Priority is limited by the possibility of a previously published two-replica or independent-dominating-set overlap generating function under another name; this cannot be excluded solely by the reported searches. No external independent audit is claimed.

## References

1. J. K. Fichte, M. Hecher, Y. Mahmood, Z. Wang, *Diversity of Extensions in Abstract Argumentation*, arXiv:2605.13332v1, first submitted 2026-05-13, https://arxiv.org/abs/2605.13332 .
2. R. Bisdorff, J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647v2 (2008), https://arxiv.org/html/math/0701647v2 .
3. M.-J. Jou, J.-J. Lin, *Algorithms for Generating All the Maximal Independent Sets of Some Graphs*, International Journal of Contemporary Mathematical Sciences 13 (2018), 95--101, https://doi.org/10.12988/ijcms.2018.826 .
4. S. Coste-Marquis, C. Devred, P. Marquis, *Symmetric Argumentation Frameworks*, ECSQARU 2005, https://www.cril.univ-artois.fr/~marquis/coste-devred-marquis-ecsqaru05.pdf .
