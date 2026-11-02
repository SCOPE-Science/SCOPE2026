# Uniform-to-lattice transition for mutually annihilating tuples in finite chain rings

## Finding
For fixed \(q\) and \(r\), sample \(r\) independent, uniformly random ring elements, conditioning on every pairwise product vanishing. The case \(r=2\) exhibits a *macroscopic uniform valuation split*, whereas each fixed \(r\ge3\) has a *tight, parity-dependent lattice law* centered at half the ring length. Both conclusions, their exact probability normalizations, and their error limits are independent of the particular finite chain ring.

Write \(a=1-q^{-1}\). For \(r=2\),
\[
\Pr(E_{2,m})=q^{-m}(1+ma).
\]
Let \(v_m(0)=m\), and define \(T_m=v_m(X_1)+v_m(X_2)-m\). Under conditioning on \(E_{2,m}\),
\[
\bigl(v_m(X_1)/m,v_m(X_2)/m,T_m\bigr)
\ \Longrightarrow\ (U,1-U,G),
\]
where \(U\) is uniform on \([0,1]\), \(G\) has \(\Pr(G=t)=a q^{-t}\) for nonnegative integers \(t\), and \(U,G\) are independent.

For fixed \(r\ge3\), write \(m=2h+\epsilon\), \(\epsilon\in\{0,1\}\), and set
\[
D_{r,\epsilon}=\{(u_1,\ldots,u_r)\in\mathbb Z^r:\ u_i+u_j\ge\epsilon\ \text{for all}\ i<j\}.
\]
Put
\[
Z_{r,q,0}=a^{-r}+\frac{r q^{-(r-2)}}{1-q^{-(r-2)}}a^{-(r-1)},
\qquad
Z_{r,q,1}=q^{-r}a^{-r}+\frac{r q^{-(r-1)}}{1-q^{-(r-2)}}a^{-(r-1)}.
\]
Then the conditional law of the entire integer vector \((v_m(X_i)-h)_{i=1}^r\) converges in **total variation** to
\[
\mu_{r,q,\epsilon}(u)=Z_{r,q,\epsilon}^{-1}\,
q^{-\sum_{i=1}^r u_i}\,\mathbf1_{\{u\in D_{r,\epsilon}\}}.
\]
Moreover,
\[
\Pr(E_{r,2h+\epsilon})=a^r q^{-rh}\left(Z_{r,q,\epsilon}+o(1)\right).
\]
For fixed \(r\ge3\), a conditioned tuple comprises distinct nonzero zero divisors with probability tending to one. Hence the lattice law also governs ordered cliques in the ordinary zero-divisor graph, after this asymptotically negligible exclusion.

## Assumptions and scope
A finite commutative *chain ring* means a finite commutative unital local ring \(R_m\) whose ideals are \(R_m\supset\mathfrak m\supset\cdots\supset\mathfrak m^m=0\), with nonzero consecutive quotients and \(\mathfrak m=(\pi)\). The residue field \(R_m/\mathfrak m\) has \(q\) elements. Existence is exemplified by \(\mathbb F_q[t]/(t^m)\). Other examples include \(\mathbb Z/p^m\mathbb Z\) when \(q=p\). The length \(m\) tends to infinity, the residue-field order \(q\) and tuple size \(r\) remain fixed, and the ring structure may change with \(m\). Sampled tuples are ordered, and zero entries or repeated entries are allowed in the conditioning event \(E_{r,m}\). The graph transfer follows by removing them after taking the limit. Valuation is defined by \(v_m(x)=j\) for \(x\in\mathfrak m^j\setminus\mathfrak m^{j+1}\), with \(v_m(0)=m\).

## Proof
**Finite valuation reduction.** Chain-ring ideal sizes are \(|\mathfrak m^j|=q^{m-j}\). Consequently, for \(0\le j<m\),
\[
\Pr(v_m(X)=j)=a q^{-j},\qquad \Pr(v_m(X)=m)=q^{-m}.
\]
Since nonzero elements of valuation \(j\) are units times \(\pi^j\), every pair obeys
\[
XY=0\quad\Longleftrightarrow\quad v_m(X)+v_m(Y)\ge m.
\]
These observations prove the stated uniformity over all finite chain rings and give the exact finite event probability as a finite sum over valuation vectors satisfying the inequalities.

**Pairs.** Given \(v_m(X_1)=j<m\), the annihilator of \(X_1\) is \(\mathfrak m^{m-j}\), of size \(q^j\). Thus for every \(0\le j<m\),
\[
\Pr(v_m(X_1)=j,E_{2,m})=a q^{-m},
\]
while \(\Pr(v_m(X_1)=m,E_{2,m})=q^{-m}\). This proves \(\Pr(E_{2,m})=q^{-m}(1+ma)\). For \(0\le j<m\), conditional on \(v_m(X_1)=j,E_{2,m}\), the second variable is uniform on \(\mathfrak m^{m-j}\). Therefore its excess valuation \(T_m\) satisfies
\[
\Pr(T_m=t\mid v_m(X_1)=j,E_{2,m})=a q^{-t}\quad(0\le t<j),
\qquad
\Pr(T_m=j\mid v_m(X_1)=j,E_{2,m})=q^{-j}.
\]
The first valuation is asymptotically uniform over \(\{0,\ldots,m-1\}\), with vanishing exceptional mass at \(m\). The geometric tail bound above is uniform, and \(j\) tends to infinity in probability; hence \((j/m,T_m)\Rightarrow(U,G)\) with independence. Since \(v_m(X_2)=m-j+T_m\), the three-coordinate weak limit follows.

**The centered lattice normalizations.** Let \(m=2h+\epsilon\) and write \(u_i=v_m(X_i)-h\). For the even case \(\epsilon=0\), every feasible lattice vector either has all coordinates nonnegative or has a unique negative coordinate \(-t\), \(t\ge1\), with all others at least \(t\). The two disjoint sums of \(q^{-\sum u_i}\) are \(a^{-r}\) and \(r a^{-(r-1)}\sum_{t\ge1}q^{-(r-2)t}\). For the odd case \(\epsilon=1\), either all coordinates are at least \(1\), or exactly one coordinate is \(-t\), \(t\ge0\), and the others are at least \(t+1\). The two sums are \(q^{-r}a^{-r}\) and \(r a^{-(r-1)}\sum_{t\ge0}q^{-(r-1)-(r-2)t}\). Evaluating the geometric series proves both displayed formulas for \(Z_{r,q,\epsilon}\). Finiteness is equivalent to \(r>2\): precisely the mechanism that distinguishes pairs from higher tuples.

**Total variation and exact leading probability.** For a fixed feasible centered vector \(u\), all \(v_i=h+u_i\) lie strictly below \(m\) when \(h\) is large, so its *unconditional* mass is exactly \(a^r q^{-rh}q^{-\sum u_i}\). For boundary vectors containing \(v_i=m\), the actual shell factor differs from this expression by \(a^{-1}\) per such coordinate. Extend finite-dimensional masses by zero to \(\mathbb Z^r\). They are bounded by \(a^{-r}q^{-\sum u_i}\mathbf1_{D_{r,\epsilon}}\), a summable majorant by the preceding calculation. Dominated convergence proves convergence of the rescaled normalizing constants and convergence in \(\ell^1(\mathbb Z^r)\) of the conditional probability mass functions, equivalent to total variation convergence.

**Graph interpretation.** For every fixed centered valuation vector, each nonzero shell contains \(a q^{h+\epsilon-u_i}\) elements, tending to infinity. Conditionally on the valuation vector, distinct coordinates are independently uniform on their shells, so the collision probability of two coordinates is at most the reciprocal of the smaller shell cardinality (and zero if the shells differ). Tightness of the centered vector, together with \(v_i\to\infty\) and \(m-v_i\to\infty\), implies conditioned zero entries, units, and repeated elements have probability tending to zero. On the remaining event, all entries are distinct nonzero zero divisors pairwise adjacent in the usual graph.

## Verification
Run the standalone standard-library program `python3 verify.py`. It independently enumerates tuples using actual multiplication in \(\mathbb Z/p^m\mathbb Z\) and in the truncated polynomial ring \(\mathbb F_p[t]/(t^m)\), compares their all-zero pairwise products with an independently computed valuation-shell count, checks the exact two-variable normalization and conditional flatness, and checks finite approximations to the parity-specific constants. The recorded result is `VERIFY_OK: exhaustive_ring_models=22; shell_and_limit_checks=128; pair_flatness=42`. Exhaustive finite instances corroborate finite claims but do not replace the dominated-convergence proof.

## Relationship to prior work
Khasraw's 2018 preprint establishes the scalar probability of a zero product of **two** ring elements, including \(\mathbb Z/p^m\mathbb Z\); that scalar formula is explicitly acknowledged as prior work. Salih's 2023 work studies zero-product probabilities of pairs in finite group algebras, including related modular cases. Arunkumar–Cameron–Kavaskar–Tamizh Chelvam (2022) identify the threshold-graph structure of zero-divisor graphs of local principal-ideal rings and the valuation criterion for adjacency. This structural criterion is also prior work. The present contribution is the *joint conditional law* and its qualitative change from two to three or more mutually annihilating sampled entries, including the entire parity-dependent lattice law and total-variation convergence for arbitrary finite chain rings. The literature comparison does not rule out an unlocated equivalent result in studies of random cliques, tropical valuations, or conditioned zero products.

## Limitations
The theorem holds for fixed \(q\) and fixed \(r\) as the nilpotency length grows; no joint limit with increasing \(q\) or \(r\) is claimed. The pair limit is weak, whereas the higher-tuple lattice limit is total variation. The error term in the asymptotic probability is not assigned an explicit convergence rate. Publication priority is not conclusively established, and the result has not undergone independent review.

## References
1. S. M. S. Khasraw, *What is the probability that two elements of a finite ring have product zero?*, arXiv:1810.13312 (public preprint 31 October 2018), https://arxiv.org/abs/1810.13312.
2. G. Arunkumar, P. J. Cameron, T. Kavaskar and T. Tamizh Chelvam, *Induced subgraphs of zero-divisor graphs*, arXiv:2207.11741 (public preprint 24 July 2022), https://arxiv.org/abs/2207.11741.
3. H. M. Mohammed Salih, *The probability that the product of two elements of finite group algebra is zero*, arXiv:2306.16416 (2023), https://arxiv.org/abs/2306.16416.
