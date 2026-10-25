# A sharp non-completeness obstruction to symmetric Markov mixing

## Finding

Let \(n\ge3\), and let \(G\) be any simple undirected graph on \(n\) labeled vertices that is **not complete**. All vertices may carry holding probabilities. Among real symmetric, entrywise nonnegative, row-stochastic \(n\)-by-\(n\) matrices \(P\) with \(P_{ij}=0\) at each nonedge \(\{i,j\}\) of \(G\), define
\[
\mu_*(G)=\min_P\left\|P-\frac1n\mathbf1\mathbf1^{\mathsf T}\right\|_2.
\]
The norm equals the second-largest eigenvalue modulus (SLEM). The sharp graph-universal bound and *complete equality classification* are
\[
\boxed{\mu_*(G)\ge\frac1{n-1},\qquad
\mu_*(G)=\frac1{n-1}\ \Longleftrightarrow\ \overline G\text{ is a nonempty matching.}}
\]
Here a matching is a set of vertex-disjoint edges; isolated vertices in the complement are permitted. Hence every graph whose complement has two edges sharing a vertex has a **strictly** larger optimum than \(1/(n-1)\), whereas deletion of any number of mutually disjoint edges from a complete graph incurs exactly the same optimal mixing penalty as deletion of a single edge. These statements concern the exact SLEM, not a bound on total-variation mixing time with a universal prefactor.

## Assumptions and scope

An admissible transition matrix satisfies \(P=P^{\mathsf T}\), \(P\mathbf1=\mathbf1\), \(P_{ij}\ge0\), and \(P_{ij}=0\) for distinct nonadjacent vertices. All diagonal entries are allowed to be nonzero; admissible edge probabilities may vanish. The matrix \(J=\mathbf1\mathbf1^{\mathsf T}/n\) is the orthogonal projection onto constants, so \(\|P-J\|_2\) is the maximum absolute value of nonconstant eigenvalues, even if there is a repeated eigenvalue \(1\). The finite feasible set of such matrices is compact, so the minimum exists. The result covers every noncomplete simple graph of order at least three, whether connected or not; the equality graphs are connected for these orders. No claim is made for directed, nonreversible, nonuniform-stationary, or time-varying chains.

## Proof

**Step 1: every missing edge gives the sharp lower bound.** Let \(H=P-J\), \(\mu=\|H\|_2\), and \(w_i=e_i-\mathbf1/n\), where \(e_i\) is the \(i\)-th standard coordinate vector. Then \(H\mathbf1=0\), \(\|w_i\|^2=(n-1)/n\). Choose any nonedge \(\{u,v\}\). Since \(P_{uv}=0\),
\[
-\frac1n=H_{uv}=\langle w_u,Hw_v\rangle.
\]
The operator-norm inequality yields
\[
\frac1n\le\|w_u\|\,\|H\|_2\,\|w_v\|=\frac{n-1}{n}\mu,
\]
so \(\mu\ge1/(n-1)\) for every admissible \(P\).

**Step 2: equality forces missing edges to be disjoint.** Suppose \(\mu=1/(n-1)\). Equality holds simultaneously in Cauchy–Schwarz and the operator-norm bound for each missing edge. Its negative sign forces
\[
Hw_v=-\mu w_u.
\]
Indeed, the inner product with \(w_u\) equals \(-\mu\|w_u\|^2\), and \(\|Hw_v\|\le\mu\|w_v\|=\mu\|w_u\|\), so equality implies exactly the displayed vector identity. If \(\{u,v\}\) and \(\{u',v\}\) were distinct missing edges with \(u\ne u'\), they would force \(Hw_v=-\mu w_u=-\mu w_{u'}\), hence \(w_u=w_{u'}\), impossible. Thus every vertex is incident to at most one missing edge: \(\overline G\) is a matching. This argument holds for arbitrary feasible matrices, with no symmetry reduction or assumption of their uniqueness.

**Step 3: every deleted matching attains the bound.** Write the \(k\ge1\) missing edges as \(\{1,2\},\{3,4\},\ldots,\{2k-1,2k\}\), and let \(m=n-2k\ge0\) denote the number of unmatched vertices. Put \(a=1/(n-1)\). Define \(P\) by the explicit rule
\[
P_{ij}=\begin{cases}
0,&\{i,j\}\text{ is one of the missing pairs},\\
a,&\text{at least one of }i,j\text{ is matched, and the pair is not missing},\\
(m-1)/(m(n-1)),&i,j\text{ are both unmatched and }m\ge1.
\end{cases}
\]
The missing-edge case always has \(i\ne j\). For \(m=0\) the last case is absent; for \(m=1\) its value is zero. Matched rows contain exactly \(n-1\) entries of value \(a\), hence sum to one. An unmatched row contains \(2k\) entries of value \(a\) and \(m\) entries of value \((m-1)/(m(n-1))\), totaling \(\bigl(2k+m-1\bigr)/(n-1)=1\). Therefore \(P\) is feasible and nonnegative.

An exact invariant-space decomposition computes its entire spectrum. Each matched-pair difference \(e_{2j-1}-e_{2j}\) is an eigenvector of eigenvalue \(+a\), giving multiplicity \(k\). Pair-symmetric contrasts with total pair coefficient zero have eigenvalue \(-a\), giving multiplicity \(k-1\). When \(m\ge2\), unmatched-coordinate contrasts with sum zero have eigenvalue \(0\), giving multiplicity \(m-1\). If \(m\ge1\), the two-dimensional space constant on the matched class and on the unmatched class has quotient transition matrix
\[
\begin{pmatrix}(2k-1)/(n-1)&m/(n-1)\\2k/(n-1)&(m-1)/(n-1)\end{pmatrix},
\]
whose eigenvalues are \(1\) and \(-a\). If \(m=0\), only the constant eigenvalue \(1\) remains beyond the pairwise difference and contrast spaces. These spaces together have dimension \(n\). Thus every nonconstant eigenvalue belongs to \(\{+a,-a,0\}\); since \(k\ge1\), \(+a\) occurs, so \(\mu(P)=a=1/(n-1)\).

Together Steps 1–3 prove both directions and the strict claim for graphs whose complements contain adjacent edges. The strictness follows because the feasible matrices form a compact set and no minimizer can attain the universal bound in that case.

## Verification

Run `python3 verify.py` using only the Python standard library. The script constructs \(P\) over all \(224\) pairs \((n,k)\) with \(3\le n\le30\) and \(1\le k\le\lfloor n/2\rfloor\). It checks, in exact rational arithmetic, symmetry, entrywise nonnegativity, row sums, and each of the \(n\) explicitly exhibited eigenvectors and eigenvalues. Successful output is `EXACT_REPLAY_OK 224`. This finite replay checks the construction and spectral formulas but is not a replacement for the all-\(n\) analytic argument.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduce precisely the symmetric, loop-permitting fastest-mixing Markov-chain optimization and its semidefinite formulation. The present claim uses their objective, not a new mixing definition. Boyd, Diaconis, Parrilo and Xiao (2009, available as a 2007 preprint) derive a closed optimum for all *edge-transitive* graphs in terms of extremal Laplacian eigenvalues. In particular, their result already implies the optimal value for the cocktail-party graphs (complete graphs with a **perfect** matching deleted); that special case is **not** being claimed as new. Their formula does not classify equality among **all noncomplete graphs**, or directly handle a partial deleted matching with unmatched vertices via edge transitivity. The new claim is the graph-universal sharp nonedge obstruction **together with necessity and sufficiency of matching complements**, deduced from saturation of the centered-coordinate spectral norm. The much broader general FMMC SDP formulation can of course determine any finite instance numerically, but an algorithmic formulation is not an implication-equivalent uniform sharp extremal classification.

A 2025 treatment of clique-lifted graphs and graph subgraphs (Jafarizadeh) develops reductions and topology-specific solutions for broader reversible-chain settings. The accessible full text was compared for matching-deleted complete graphs and a universal noncomplete-graph SLEM equality classification; neither was located. This comparison does not assert that a search failure proves novelty; see the limitation below.

## Limitations

This is a complete graph-family **extremal characterization**, not an enumeration of all transition matrices attaining equality for a given matching-deleted graph. A structural equality classification can potentially be implicit in the dual SDP or in broader graph spectral extremality literature; the cited papers' generally applicable optimization techniques and the absence of a specific indexed theorem do not logically exclude that possibility. All arguments are exact for real symmetric stochastic matrices with holding allowed; modifying the holding constraint, imposing positive transitions on every edge, or allowing directed chains changes the optimization. The sharp objective is the SLEM; it does not alone fix preasymptotic total-variation mixing constants.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264, public PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (first verified public online release 2004-10-29).
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, DOI 10.1137/070689413, preprint arXiv:0709.0955 (2007-09-06), public PDF: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421 (2025-01-05), https://arxiv.org/abs/2501.02421.
