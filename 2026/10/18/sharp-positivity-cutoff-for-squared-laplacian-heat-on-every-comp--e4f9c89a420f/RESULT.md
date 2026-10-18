# Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph

## Finding
Let \(G=K_{m_1,\ldots,m_r}\) be a finite, simple, unweighted complete multipartite graph, with \(r\ge2\), \(m_i\ge1\), and \(n=\sum_i m_i\). Write \(L=D-A\) for its combinatorial Laplacian, and put \(T(t)=e^{-tL^2}\) for \(t\ge0\). Its sharp complex or real endpoint operator norm is
\[
\boxed{\|T(t)\|_{\ell^\infty\to\ell^\infty}=1+2\max_i\frac{m_i-1}{m_i}\left[e^{-(n-m_i)^2t}-\frac{m_i}{n}-\frac{n-m_i}{n}e^{-n^2t}\right]_+.}
\]
Here \([z]_+=\max\{0,z\}\). Since \(T(t)\) fixes constants, entrywise nonnegativity is equivalent to contraction in \(\ell^\infty\) and to preserving every interval of input values.

If \(m=\max_i m_i=1\), the graph is complete and \(T(t)\) is nonnegative at every \(t\ge0\). If \(m\ge2\), put \(x=(n-m)/n\in(0,1)\). For every \(0<x<1\), define \(u(x)>0\) as the unique strictly positive solution to
\[
e^{-x^2u}=1-x+xe^{-u}.
\]
Then the *complete* positivity-time set is
\[
\boxed{\{t\ge0:T(t)\ge0\text{ entrywise}\}=\{0\}\cup[\tau(G),\infty),\qquad \tau(G)=\frac{u((n-m)/n)}{n^2}.}
\]
At \(t=\tau(G)\), the only vanishing off-diagonal entries are pairs of distinct vertices inside largest parts; all entries are strictly positive for \(t>\tau(G)\). The function \(u\) is strictly decreasing throughout \((0,1)\); thus \(\tau(G)\) depends only on \(n\) and the largest part size, and increases strictly with that size.

For fixed \(n\ge4\), the smallest and largest positive cutoffs among all noncomplete complete multipartite graphs belong respectively to \(K_{2,1,\ldots,1}\) (one deleted edge from a clique) and \(K_{n-1,1}\) (a star). Let \(u_0=1.2564312086261696\ldots\) denote the unique positive root of \(e^{u_0}=1+2u_0\). Their asymptotics are
\[
\lim_{n\to\infty}n^2\tau(K_{2,1,\ldots,1})=u_0,\qquad
\lim_{n\to\infty}n\tau(K_{n-1,1})=1.
\]
In contrast, both graph families have exactly the same initial bounded-input amplification coefficient:
\[
\|T(t)\|_{\infty\to\infty}=1+2(n-2)t+O_n(t^2)\quad(t\downarrow0).
\]
Hence equal first-order departure from positivity need not predict the duration of the positivity failure: the ratio of the two sharp recovery times grows as \(n/u_0\).

## Assumptions and scope
Counting-measure \(\ell^p\) norms and the **unnormalized** Laplacian are used. The generator is the negative square \(-L^2\), not the ordinary Markov generator \(-L\), the resolvent \((I+tL^2)^{-1}\), or a normalized graph bi-Laplacian. A graph may have singleton parts. For \(t=0\), \(T(0)=I\); every assertion about strictly positive off-diagonal entries refers to \(t>0\). The graph is connected because \(r\ge2\). The case \(m=1\) is handled separately: no within-part distinct pair exists.

## Proof
**1. Orthogonal decomposition and exact matrix entries.** Let \(V_i\) be the \(i\)-th part. Split \(\mathbb R^n\) orthogonally into the constants, the subspace of vectors constant on each part with total sum zero, and the within-part zero-sum subspaces \(E_i=\{v:\operatorname{supp}v\subseteq V_i,\ \sum_{a\in V_i}v_a=0\}\). Their \(L\)-eigenvalues are respectively \(0\), \(n\), and \(n-m_i\) on \(E_i\). Let \(J\) be the all-ones matrix, and \(J_i\), \(I_i\) the all-ones and identity blocks on \(V_i\), padded by zero. Therefore
\[
T(t)=\frac1nJ+e^{-n^2t}\left(\sum_i\frac1{m_i}J_i-\frac1nJ\right)
+\sum_i e^{-(n-m_i)^2t}\left(I_i-\frac1{m_i}J_i\right).
\]
For two distinct vertices in different parts the entry is \(c(t)=(1-e^{-n^2t})/n\), strictly positive for \(t>0\). Within a part of size \(s=m_i\), the common *off-diagonal* entry and diagonal entry are
\[
w_s(t)=\frac1s\left[\frac sn+\left(1-\frac sn\right)e^{-n^2t}-e^{-(n-s)^2t}\right],
\]
\[
d_s(t)=\frac1n+\left(\frac1s-\frac1n\right)e^{-n^2t}+\left(1-\frac1s\right)e^{-(n-s)^2t}>0.
\]
The strict diagonal inequality follows since all three displayed coefficients are nonnegative and the constant coefficient \(1/n\) is positive. Since \(T(t)\mathbf1=\mathbf1\), the absolute row sum at a vertex in a part of size \(s\) is exactly \(1+2(s-1)[-w_s(t)]_+\). Taking the largest row proves the displayed sharp operator-norm identity (the same for real and complex \(\ell^\infty\)).

**2. A unique recovery time for each part.** Put \(u=n^2t\), \(x=(n-s)/n\), and
\[
F(x,u)=e^{-x^2u}-(1-x+xe^{-u}),\qquad w_s(t)=-\frac1sF(x,n^2t).
\]
For fixed \(x\in(0,1)\), one has \(F(x,0)=0\), \(\partial_uF(x,0)=x(1-x)>0\), and \(F(x,u)\to-(1-x)<0\) as \(u\to\infty\). Moreover,
\[
\partial_uF(x,u)=-x^2e^{-x^2u}+xe^{-u},
\]
which has precisely one positive zero, \(u=\log(1/x)/(1-x^2)\), with derivative changing from positive to negative. Hence \(F(x,u)>0\) for \(0<u<u(x)\), equals zero exactly at \(u=u(x)\), and is negative for \(u>u(x)\).

**3. The nontrivial strict root-ordering lemma.** Let \(u_0>0\) be the unique positive solution to \(e^u=1+2u\). For any fixed \(u>0\),
\[
F(0,u)=F(1,u)=0,\quad
\partial_xF(0,u)=1-e^{-u}>0,\quad
\partial_xF(1,u)=1-(1+2u)e^{-u},
\]
\[
\partial_x^2F(x,u)=2u(2ux^2-1)e^{-ux^2}.
\]
This last derivative is initially negative and thereafter positive, with at most one change of sign. If \(0<u\le u_0\), the right endpoint derivative is nonpositive; the derivative \(\partial_xF\) crosses from positive to nonpositive at most once, so \(F(x,u)>0\) for all \(x\in(0,1)\). If \(u>u_0\), both endpoint derivatives are positive. The condition \(\int_0^1\partial_xF\,dx=0\) forces its single minimum to be negative. Therefore \(\partial_xF\) has exactly two interior zeros, and \(F\) changes sign precisely once within \((0,1)\), from positive to negative. Thus \(u(x)>u_0\) for every \(x<1\). At \(u=u(x_2)>u_0\), the unique interior sign-change point is \(x_2\); for \(0<x_1<x_2\) one has \(F(x_1,u)>0\), so \(u(x_1)>u(x_2)\). This proves strict decrease of \(u(x)\) without relying on numerical observations.

**4. Global positivity and equality cases.** A part with \(s\ge2\) has nonnegative internal off-diagonal entries precisely for \(t\ge u((n-s)/n)/n^2\), aside from \(t=0\). Since this cutoff increases strictly with \(s\), the largest part determines the full matrix cutoff. At equality its internal off-diagonal entries vanish; smaller parts have strictly positive internal entries and cross-part entries are strictly positive. For every \(t\in(0,\tau(G))\), the largest part still has strictly negative off-diagonal entries, and the endpoint norm exceeds one. If all \(m_i=1\), the internal off-diagonal obstruction is absent and the cross-part kernel is positive at positive times.

**5. Sharp extremizers over graph shapes and timescale contrast.** For a noncomplete graph \(2\le m\le n-1\). These extremes are attained by the near-complete graph and the star, respectively, so the strict monotonicity proved above gives the fixed-\(n\) minimax claim. Since \(u(x)\) decreases and is bounded below by \(u_0\), it has a limit as \(x\uparrow1\). Put \(x=1-\varepsilon\) into \(F(x,u(x))=0\), divide by \(\varepsilon\), and pass to the limit to obtain \((1+2u)e^{-u}=1\). The nonzero lower bound forces \(u=u_0\). Thus the near-complete family, with \(x=1-2/n\), has \(n^2\tau\to u_0\). As \(x\downarrow0\), for every fixed positive \(v\), \(F(x,v)/x\to1-e^{-v}>0\), so \(u(x)\to\infty\). The root identity becomes \(x^2u(x)=-\log(1-x+xe^{-u(x)})=x(1+o(1))\); consequently \(xu(x)\to1\). For a star, \(x=1/n\), giving \(n\tau\to1\).

Finally, \(w_s(t)=-(n-s)t+O_n(t^2)\). The exact norm identity yields
\[
\|T(t)\|_{\infty\to\infty}=1+2t\max_i(m_i-1)(n-m_i)+O_n(t^2).
\]
This maximand equals \(n-2\) both for part sizes \((n-1,1)\) and for \((2,1,\ldots,1)\), proving the shared first-order growth and unequal sharp recovery times.

## Verification
The self-contained file `verify_biheat_multipartite.py` independently builds each graph Laplacian and its square from the edge relation, exponentiates the resulting matrix by scaling-and-squaring Taylor series, and compares the matrix entries and norms against the formulas above. In the recorded execution it passed 43,847 numerical equalities across 82 graph designs, together with exact-sign/limit checks. The proof above establishes the universal claims; finite numerical calculations are consistency tests rather than proofs of all parameter ranges. The complete mathematical derivation does not depend on this script.

## Relationship to prior work
Daners, Glück, and Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices* [1], develop eventual positivity and asymptotic positivity for operator semigroups, including squared Laplacians, but do not give a complete-multipartite kernel, sharp cutoff, or largest-part classification. Their *Eventually Positive Semigroups of Linear Operators* [2], Sections 6.1 and 6.3, treats finite-dimensional eventual positivity and squares of generators, without quantifying the exact positivity-time set of the family here. A published general three-spectral-value barrier [3] rules out positivity-time gaps under a three-level spectrum, but complete multipartite graphs with several distinct part sizes have more than three spectral levels; moreover [3] does not produce the exact cutoff or its graph-extremal asymptotics. No new claim is made about the abstract eventual-positivity criterion or the known Laplacian spectral decomposition itself.

## Limitations
This is a theorem specifically for simple, unweighted complete multipartite graphs and the counting-measure squared combinatorial Laplacian. It does not apply unchanged to weighted graphs, normalized graph Laplacians, arbitrary graphs, or fourth-order continuum differential operators. The threshold is defined through a unique transcendental root; no elementary closed form is asserted. Equivalence to an older unpublished or differently named exact multipartite matrix-exponential computation remains a residual bibliographic risk.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first submitted 2015-11-17, https://arxiv.org/abs/1511.05294 .

[2] D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020, first submitted 2015-11-29, https://arxiv.org/abs/1511.09020 .

[3] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-spectral-value-barrier-for-gaps-in-positivity-times-of-s--da21753d4271 .

