# A full first-order probability spectrum at every higher birthday threshold

## Finding

Fix an integer \(k\ge 2\) and a real constant \(c>0\). Let \(m_n\) be positive integers with \(m_n\sim c n^{k/(k-1)}\). Form a random finite structure \(\mathcal A_n\) in the signature \(\{R,C,E\}\): \(R\) and \(C\) are disjoint unary predicates partitioning the domain, with precisely \(m_n\) roots and \(n\) children; every child chooses independently one uniformly random root; \(E(x,y)\) holds exactly when child \(x\) chooses root \(y\). There are no other edges.

For a root \(v\), let its degree be the number of children assigned to it, and let \(X_{n,j}\) be the number of roots of degree \(j\). Put
\[
\lambda=\frac{1}{k!c^{k-1}}>0,\qquad
\mathcal S_{k,c}=
\left\{e^{-\lambda}\sum_{j\in F}\frac{\lambda^j}{j!}:
F\subseteq\mathbb N_0\ \text{is finite or cofinite}\right\}.
\]

**Theorem.** For every first-order sentence \(\varphi\) of the fixed signature, the limit \(\lim_{n\to\infty}\Pr(\mathcal A_n\models\varphi)\) exists, belongs to \(\mathcal S_{k,c}\), and is effectively computable from \(\varphi\), \(k\), and the symbolic parameter \(\lambda\). Conversely every number in \(\mathcal S_{k,c}\) is the limit of such a sentence. In particular
\[
X_{n,k}\ \xrightarrow{d}\ \operatorname{Poisson}(\lambda),
\]
the multiplicities \(X_{n,j}\) diverge in probability for every \(0\le j<k\), and \(\Pr(\exists v\in R:\deg(v)>k)\to0\).

The finite/cofinite qualification is essential: ordinary first-order logic has finite quantifier rank and cannot select a set of Poisson outcomes with infinitely many alternating membership decisions.

## Assumptions and scope

Only the two unary sorts and the binary edge are available. The two sorts are explicitly named; no natural order, arithmetic, numerical counting operators, or externally varying symbols are present. Quantification ranges over all roots and children. The parameter \(k\) is fixed before the limit \(n\to\infty\), and \(c\) is a fixed positive real. The theorem is a uniform mathematical assertion over all such fixed \(k,c\); effective computation of a limit returns a finite Poisson-polynomial expression with coefficient parameter \(\lambda\).

An \(j\)-star consists of one root and exactly \(j\) adjacent children. Every connected component of \(\mathcal A_n\) is an \(j\)-star. For fixed \(q\), two disjoint unions of these stars with no degrees exceeding \(k\) are \(q\)-equivalent if, for each \(0\le j\le k\), their \(j\)-star multiplicities are equal when below \(q\), and are both at least \(q\) otherwise.

## Proof

**Exact factorial moments.** The \(r\)-th falling-factorial moment of \(X_{n,j}\), for fixed integers \(j,r\ge0\) satisfying \(r\ge1\) and \(jr\le n\), is
\[
\mathbb E[(X_{n,j})_r]
=(m_n)_r\,\frac{(n)_{jr}}{(j!)^r m_n^{jr}}
\left(1-\frac r{m_n}\right)^{n-jr}.
\tag{1}
\]
Here \((a)_r=a(a-1)\cdots(a-r+1)\). Indeed, choose an ordered \(r\)-tuple of distinct roots, allocate to each exactly \(j\) children, and require all remaining children to avoid those \(r\) roots. Formula (1) includes \(j=0\) with the usual empty-product convention.

Because \(n/m_n\to0\), for fixed positive \(j,r\) the final factor is \(1+o(1)\), and
\[
\mathbb E X_{n,j}\sim\frac{n^j}{j!m_n^{j-1}}.
\tag{2}
\]
For \(1\le j<k\), the right side has order \(n^{(k-j)/(k-1)}\) and diverges, while formula (1) with \(r=2\) shows \(\operatorname{Var}(X_{n,j})=o((\mathbb EX_{n,j})^2)\). Consequently \(X_{n,j}\to\infty\) in probability. For \(j=0\), deterministically \(X_{n,0}\ge m_n-n\to\infty\).

For \(j=k\), formula (1) gives
\[
\mathbb E[(X_{n,k})_r]\longrightarrow\lambda^r
\quad\text{for every fixed }r\ge1.
\tag{3}
\]
The factorial-moment criterion for nonnegative integer random variables yields \(X_{n,k}\Rightarrow Z\), with \(Z\sim\operatorname{Poisson}(\lambda)\). Finally, using a union bound over subsets of \(k+1\) children, the expected number of roots with degree at least \(k+1\) is at most
\[
\frac{\binom n{k+1}}{m_n^k}
=O\!\left(n^{-1/(k-1)}\right)\longrightarrow0.
\tag{4}
\]

**Finite-rank structural reduction.** Fix a sentence \(\varphi\) of quantifier rank \(q\ge1\). With probability tending to one, there are no stars larger than \(k\), and for every \(j<k\) there are at least \(q\) stars of size \(j\). The standard \(q\)-round Ehrenfeucht–Fraïssé matching strategy proves that two unions of finite stars that agree on all star multiplicities truncated at \(q\) satisfy exactly the same rank-\(q\) sentences. Each time Spoiler enters a star not visited before, Duplicator chooses a fresh star of the same size, possible since fewer than \(q\) stars were previously visited; within already matched stars, Duplicator uses the fixed child-root isomorphism. The matching is a partial isomorphism after all \(q\) rounds. This argument is valid because there are no edges between components and the root/child predicates are respected.

On the high-probability event, the rank-\(q\) theory of \(\mathcal A_n\) therefore depends only on \(\min(X_{n,k},q)\). Let \(B_{q,z}\) be the canonical disjoint union with \(q\) copies of each \(j\)-star for \(0\le j<k\), and \(z\) copies of the \(k\)-star, for \(0\le z\le q\). Define
\[
F_\varphi=\{z<q:B_{q,z}\models\varphi\}
\ \cup\ \{z\ge q:B_{q,q}\models\varphi\}.
\tag{5}
\]
This is finite or cofinite. Equations (3)–(5) give
\[
\lim_{n\to\infty}\Pr(\mathcal A_n\models\varphi)
=\Pr(Z\in F_\varphi)
=e^{-\lambda}\sum_{j\in F_\varphi}\lambda^j/j!.
\tag{6}
\]
Thus every limit belongs to the displayed spectrum, and (5) is a terminating effective procedure, requiring evaluation of \(\varphi\) on \(q+1\) explicit finite structures.

**Realization.** For any fixed \(j\), the formula \(\operatorname{Deg}_j(v)\) states that \(v\) is a root incident with exactly \(j\) distinct children. It uses \(j\) existential witnesses followed by a universal clause excluding additional children; for \(j=0\), merely exclude all children. A sentence \(T_z\) can state that exactly \(z\) distinct roots satisfy \(\operatorname{Deg}_k\), by the same finite-witness construction. For a finite set \(F\subseteq\mathbb N_0\), the finite disjunction \(\bigvee_{z\in F}T_z\) expresses \(X_{n,k}\in F\); its negation expresses membership in the complement. Hence every finite or cofinite Poisson event is first-order definable, and the reverse inclusion holds. The case \(F=\varnothing\) uses a contradiction, and the case \(F=\mathbb N_0\) uses a tautology. This completes the proof.

## Verification

The included standalone program `verify.py` exhaustively compares the right side of (1) with the exact factorial moments enumerated over all allocations for small \(n,m,j,r\). It additionally checks finite-size critical-scale first moments and upper-tail bounds for \(k=2,3,4,5\) and several constants \(c\). The observed success marker is `CRITICAL_STAR_OCCUPANCY_EXACT_OK 184 checks`. Exhaustive finite tests corroborate the exact counting lemma; they cannot establish the weak limit, the first-order Ehrenfeucht–Fraïssé theorem, or historical novelty. Those steps are proved above.

Run with `python verify.py` using only the Python standard library.

## Relationship to prior work

Koponen's 2026 study of finite-model properties of \(\omega\)-categorical theories motivates examining first-order features of simple finite directed acyclic structures and their random expansions. The present model is a rooted height-two random allocation graph with a different, quantitatively explicit probabilistic question. The higher-birthday collision asymptotics underlying (1)–(4) belong to classical occupancy theory; they are not claimed as new in isolation. Larrauri–Perarnau's first-order convergence work on random graphs with given degree sequences treats a different sampling model and degree hypotheses, so its statements do not immediately furnish the exact complete spectrum (6). The 2026 first-order laws for random geometric graphs on a torus develop componentwise logical analysis and Poisson components, but assume a geometric graph process, not independent uniform child-to-root allocations with fixed named sorts and critical exponents \(k/(k-1)\). The contribution assessed here is the complete, effectively computable finite/cofinite Poisson-spectrum classification at **every** higher birthday threshold for this canonical random DAG family, including all fixed first-order sentences, not merely an example event.

## Limitations

The conclusion is for **fixed** \(k\ge2\) and positive \(c\), first-order logic without order or counting predicates, and \(m_n\sim c n^{k/(k-1)}\). It does not classify regimes where \(k\) grows with \(n\), random parent capacities, arithmetic enrichments, variable quantifier rank, or graphs allowing children multiple parents. It does not assert this method or the individual occupancy asymptotics are historically new. A broader general first-order random-component theorem may imply the instance, and specialized unpublished treatments may have priority; these are residual originality risks. No independent scientific audit has been performed.

## References

1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first posted 2026-10-12). https://arxiv.org/abs/2610.16163
2. *First-Order Laws for Random Geometric Graphs on the Torus*, arXiv:2609.26230v1 (2026). https://arxiv.org/abs/2609.26230
3. L. Larrauri and G. Perarnau, *First Order Logic of Sparse Graphs with Given Degree Sequences*, arXiv:2405.14836 (2024). https://arxiv.org/abs/2405.14836
4. Classical factorial-moment criterion for Poisson convergence and Ehrenfeucht–Fraïssé games for first-order finite structures; the needed special instances are proved or stated precisely above.
