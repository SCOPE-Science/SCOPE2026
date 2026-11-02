# A disagreement-graph trichotomy for essential norms of discrete composition differences

## Finding
Let \(X\) be a countably infinite set and let \(\phi,\psi:X\to X\). On scalar \(\ell_\infty(X)\) (real or complex), set \(T=C_\phi-C_\psi\), where \((C_\phi f)(v)=f(\phi(v))\). Define the **disagreement graph** \(G_{\phi,\psi}\) on vertex set \(X\): its distinct, unordered edges are precisely
\[
E=\{\{\phi(v),\psi(v)\}:v\in X,\ \phi(v)\ne\psi(v)\}.
\]
Then the distance to compact operators is exactly
\[
\boxed{\|T\|_{\mathrm e}=\begin{cases}
0,&E\text{ finite},\\
1,&E\text{ infinite and has a finite vertex cover},\\
2,&E\text{ has no finite vertex cover}.
\end{cases}}
\]
Equivalently, the last case is exactly when \(E\) contains an infinite matching. All three values occur, and \(\|T\|=2\) whenever \(E\ne\varnothing\). Thus noncompact differences can have either half or all of the maximal norm as their essential norm.

For the corresponding composition operators on \(c_0(X)\), assume **both** symbols are proper (preimages of finite sets are finite). Then
\[
\boxed{\|C_\phi-C_\psi\|_{\mathrm e,c_0}=0\quad\text{if }E\text{ is finite},\qquad
\|C_\phi-C_\psi\|_{\mathrm e,c_0}=2\quad\text{if }E\text{ is infinite}.}
\]
The intermediate value \(1\) is therefore excluded on \(c_0\) for proper symbols.

The trichotomy extends to approximation numbers \(a_r(T)=\inf\{\|T-R\|:\operatorname{rank}R<r\}\): if \(E\) contains an infinite matching then \(a_r(T)=2\) for every \(r\ge1\); if \(E\) is infinite with a vertex cover \(F\) of \(k\) vertices then \(a_r(T)=1\) for every \(r\ge k+1\); and if \(E\) has \(s\) distinct edges then \(a_r(T)=0\) for \(r\ge s+1\). In the proper-\(c_0\) case with infinite \(E\), \(a_r(T)=2\) for all \(r\ge1\).

A useful weighted form identifies the underlying operator-norm mechanism. For positive weights \(\mu,\nu:X\to(0,\infty)\), put
\[
\mathcal B_\mu(X)=\{f:X\to\mathbb K:\|f\|_\mu=\sup_{u\in X}\mu(u)|f(u)|<\infty\}.
\]
Suppose \(C_\phi,C_\psi:\mathcal B_\mu(X)\to\mathcal B_\nu(X)\) are bounded. For each finite \(F\subset X\), put
\[
H(F)=\sup_{v:\phi(v)\ne\psi(v)}\nu(v)
\left(\frac{\mathbf1_{\phi(v)\notin F}}{\mu(\phi(v))}
+\frac{\mathbf1_{\psi(v)\notin F}}{\mu(\psi(v))}\right),
\]
with the supremum of the empty set equal to \(0\). The **exact weighted essential-norm identity** is
\[
\boxed{\|C_\phi-C_\psi\|_{\mathrm e,\,\mathcal B_\mu\to\mathcal B_\nu}=\inf_{F\subset X\text{ finite}}H(F).}
\]
The graph trichotomy follows from this identity with \(\mu=\nu=1\).

## Assumptions and scope
The index set is countably infinite and no metric structure is required. All scalar fields in the theorem may be \(\mathbb R\) or \(\mathbb C\). The essential norm is the infimum of operator-norm distances to all compact (not only finite-rank) operators. Weighted symbols are assumed separately bounded; equivalently
\[
\sup_v\frac{\nu(v)}{\mu(\phi(v))}<\infty,\qquad
\sup_v\frac{\nu(v)}{\mu(\psi(v))}<\infty.
\]
A vertex cover meets every edge. A matching consists of pairwise vertex-disjoint edges. Statements about \(c_0\) require the two composition operators separately preserve \(c_0(X)\), guaranteed by properness of their symbols. No statement is made for a difference that acts on \(c_0\) only through cancellation of two individually undefined maps.

## Proof
**1. Exact tail norm.** Let \(P_F\) be the input-coordinate projection onto a finite set \(F\subset X\), and let \(T=C_\phi-C_\psi\). Each output row of \(T(I-P_F)\) is either zero or consists of two evaluations on distinct input coordinates with coefficients of opposite sign. Each input coordinate \(u\) has norm-one normalized point mass \(\mathbf1_{\{u\}}/\mu(u)\). Hence the \(\ell_\infty\)-row norm is the sum of the absolute coefficient magnitudes, namely
\[
\|T(I-P_F)\|=H(F).
\]
For the lower inequality in this equality, choose the signs of the two surviving evaluations to agree after subtraction. Since \(TP_F\) is finite rank, this yields
\[
\|T\|_{\mathrm e}\le\inf_{F\text{ finite}}H(F)=:L.
\]

**2. All compact perturbations obey the opposite bound.** Take any compact \(K:\mathcal B_\mu\to\mathcal B_\nu\). If \(L=0\), the lower bound is automatic. Otherwise choose an increasing sequence of finite sets \(F_n\) containing each support selected at earlier stages. Since \(H(F_n)\ge L\), choose an output index \(v_n\) with the row mass outside \(F_n\) at least \(L-1/n\). Construct \(f_n\) supported precisely on the one or two coordinates of \(\{\phi(v_n),\psi(v_n)\}\setminus F_n\), with phases yielding the positive row mass and \(\|f_n\|_\mu=1\). Enlarge \(F_{n+1}\) to include this support. The normalized \(f_n\) have pairwise disjoint finite supports.

Every bounded disjoint-support sequence in scalar \(\ell_\infty(X)\) is weakly null. Indeed, for any continuous linear functional \(\Lambda\) and disjointly supported vectors \(g_n\) of sup norm at most one, any finite set of indices admits unit phases \(\zeta_n\) with
\[
\sum_n|\Lambda(g_n)|=\left|\Lambda\left(\sum_n\zeta_n g_n\right)\right|\le\|\Lambda\|,
\]
so the scalar sequence \(\Lambda(g_n)\) tends to zero. Multiplication by \(\mu\) is an isometry from \(\mathcal B_\mu\) to \(\ell_\infty(X)\), so \(f_n\rightharpoonup0\). Compact operators send weakly null sequences to norm-null sequences; therefore \(\|Kf_n\|_\nu\to0\). By construction,
\[
\|(T-K)f_n\|_\nu\ge L-1/n-\|Kf_n\|_\nu.
\]
Consequently \(\|T-K\|\ge L\). Taking the infimum over all compact \(K\) proves the weighted identity.

**3. Graph trichotomy.** When \(\mu=\nu=1\), the quantity \(H(F)\) is the maximum number of endpoints outside \(F\) among the distinct disagreement edges. This number is in \(\{0,1,2\}\). It equals zero for some finite \(F\) exactly when \(E\) itself is finite; it is at most one for some finite \(F\) exactly when \(F\) is a vertex cover. If \(E\) is infinite, even a finite cover leaves an endpoint outside it, so the infimum cannot be zero. If there is no finite cover, every finite \(F\) misses both endpoints of an edge, so \(H(F)=2\).

A graph has no finite vertex cover if and only if it has an infinite matching. To see this, greedily select disjoint edges. Either the selection continues indefinitely, producing an infinite matching, or the finitely many selected edges form a maximal matching, whose finite set of endpoints covers every edge. This establishes the equivalent graph formulation.

**4. The vanishing-at-infinity space.** Properness of \(\phi\) and \(\psi\) makes each composition operator bounded on \(c_0(X)\). The finite-coordinate truncations and the disjoint-support compactness argument above remain valid in \(c_0\), giving the same infimum formula. Moreover each graph vertex \(u\) belongs to at most \(|\phi^{-1}(\{u\})|+|\psi^{-1}(\{u\})|\) disagreement edges, hence has finite graph degree. An infinite locally finite graph cannot possess a finite vertex cover. Thus every infinite \(E\) has essential norm two, while finite \(E\) makes \(T\) finite rank.

**5. Approximation numbers and attainment of all phases.** For any finite cover \(F\) of cardinality \(k\), \(TP_F\) has rank at most \(k\), and \(\|T-TP_F\|\le1\). This gives \(a_{k+1}\le1\), while the essential norm lower bound forces \(a_r\ge1\) for every \(r\). For no finite cover the essential norm and the operator norm both equal two, forcing all approximation numbers to equal two. For finite \(E\), all rows use one of \(|E|\) difference functionals, so \(\operatorname{rank}T\le|E|\).

Three examples on \(X=\mathbb N_0\) demonstrate sharpness. Finite disagreement between \(\phi\) and \(\psi\) gives essential norm zero even if both have infinite range. Taking \(\phi(n)=0\), \(\psi(n)=n\) for all positive \(n\), and \(\phi(0)=\psi(0)=0\), gives the infinite star and essential norm one. Taking \(\phi(2n)=2n\), \(\psi(2n)=2n+1\), and \(\phi(2n+1)=\psi(2n+1)=2n+1\) gives an infinite matching and essential norm two on both \(\ell_\infty\) and \(c_0\). In the star example the constant symbol is not proper, consistent with the \(c_0\) dichotomy.

## Verification
The self-contained `checker.py` uses exact rational arithmetic and exhaustive sign choices on finite coordinate sets. It compares the weighted row-sum tail formula with direct \(\ell_\infty\)-operator maximization, checks the greedy-matching endpoint-cover argument for all small finite graphs, and checks finite-prefix star and matching patterns. Execute `python checker.py` in a Python 3 environment; the recorded run reported 1,857 passing finite checks. Infinite compactness and full graph statements are proven above, not inferred from enumeration.

## Relationship to prior work
Allen and Pons established boundedness, compactness, operator norms, and essential norms for **individual** composition operators on weighted supremum Banach spaces of infinite trees (2022; arXiv:2207.09001). The present statement concerns differences of two composition operators and the combinatorics of the unordered disagreement pairs. Their single-operator essential-norm formula does not itself identify the finite-cover versus infinite-matching alternatives.

Lindström and Wolf studied differences of weighted composition operators between spaces of **holomorphic** functions (2008); related papers address bounded analytic, Hardy, and Bloch settings. These spaces lack the freely assignable point-mass evaluations used here, so a holomorphic-space formula is not automatically the stated discrete graph law. Standard absolute-row-sum and coordinate truncation methods are background ingredients, not asserted to be new independently. Published results on individual weighted composition s-numbers concern a different operator class from a general difference of two such operators.

## Limitations
This is a discrete, scalar-valued statement. For the unweighted trichotomy, no restriction on symbols is imposed on \(\ell_\infty\), while the \(c_0\) conclusion explicitly requires properness. The weighted formula assumes separate boundedness. The work does not classify essential norms of arbitrary sums of more than two composition operators or operators on holomorphic function spaces. The graph formulation is an application of general coordinate-tail techniques and could occur as an implicit corollary of older matrix-operator literature; the novelty assessment is therefore qualified. Independent expert validation and exhaustive historical verification are outstanding.

## References
1. R. F. Allen and M. A. Pons, *Composition operators on weighted Banach spaces of a tree*, arXiv:2207.09001, first posted 2022-07-19, https://arxiv.org/abs/2207.09001.
2. M. Lindström and E. Wolf, *Essential norm of the difference of weighted composition operators*, Monatsh. Math. 153 (2008), 133–143, DOI:10.1007/s00605-007-0493-1.
3. A. A. Albanese and C. Mele, *On composition operators between weighted (LF)- and (PLB)-spaces of continuous functions*, Math. Nachr. (2023), DOI:10.1002/mana.202200171.
4. Z. Fang and Z. Zhou, *Difference of composition operators in the polydiscs*, arXiv:0709.1430 (2007), https://arxiv.org/abs/0709.1430.
