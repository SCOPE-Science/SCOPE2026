# First three-step gap between adaptive and static shattering for finite divisibility

## Finding
For each integer \(N\geq1\), set \(X_N=\{1,\ldots,N\}\) and let \(\mathcal H_N=\{h_y:y\in X_N\}\) where the Boolean hypothesis \(h_y(x)=1\) precisely when \(x\mid y\). Write \(L_N\) for its Littlestone dimension and \(V_N\) for its Vapnik–Chervonenkis dimension, with \(L_1=V_1=0\).

**Theorem.** The least integers \(N\) such that \(L_N\geq d\), for \(d=1,2,3,4,5,6,7\) in this order, are exactly
\[
2,\quad4,\quad9,\quad27,\quad81,\quad320,\quad1280.
\]
Moreover, for every \(N\ge1\), the exact VC dimension is
\[
V_N=\max\{k\ge0:p_1\cdots p_k\le N\},
\]
where \(p_i\) denotes the \(i\)-th prime and the empty product is one. Hence \(L_{1280}=7\) and \(V_{1280}=4\), and **\(1280\) is the least positive integer \(N\) for which \(L_N-V_N\ge3\)**.

## Assumptions and scope
The instance space and the hypothesis index set are both the *same* initial interval \(X_N\); positive examples are queries \(x\) that divide the hidden hypothesis integer \(y\). Queries may be selected adaptively in a complete binary mistake tree. Each leaf must be realized by at least one hypothesis in \(\mathcal H_N\). This is the ordinary deterministic realizable online-learning Littlestone dimension, not the worst-case number of oracle queries required to identify the integer. The theorem includes all positive \(N\) for the VC formula, and the first seven **finite** threshold levels for Littlestone dimension; it makes no general claim about the eighth or later thresholds.

## Proof
### The exact VC-dimension formula
Suppose \(S=\{x_1,\ldots,x_k\}\subseteq X_N\) is shattered. The all-positive labeling supplies \(y\le N\) divisible by every \(x_i\). For each \(i\), the labeling positive on the other \(k-1\) points but negative on \(x_i\) supplies a multiple of \(\operatorname{lcm}(S\setminus\{x_i\})\) that is not divisible by \(x_i\). Consequently \(x_i\) fails to divide that least common multiple. Some prime \(q_i\) therefore satisfies
\[
\nu_{q_i}(x_i)>\max_{j\ne i}\nu_{q_i}(x_j).
\]
The primes \(q_i\) are pairwise distinct, as one prime cannot have two different strictly maximal exponents. All \(q_i\) divide \(y\). Hence \(N\ge y\ge\prod_i q_i\ge p_1\cdots p_k\). Conversely, if \(p_1\cdots p_k\le N\), choose \(S=\{p_1,\ldots,p_k\}\); each Boolean labeling is realized by the product of its positive primes, with the empty product equal to one. This proves the formula.

### Exact finite Littlestone threshold recurrence
For fixed \(N\), a *version space* is a subset \(H\subseteq X_N\) of the surviving hypothesis indices. Define the Boolean predicate \(W_N(H,d)\) to mean that a complete depth-\(d\) mistake tree can be shattered using exactly these hypotheses. At depth zero, \(W_N(H,0)\) holds if and only if \(H\ne\varnothing\). For \(d\ge1\) the exact recursion is
\[
W_N(H,d)\Longleftrightarrow\exists x\in\{2,\ldots,N\}\ \bigl[W_N(H_x^+,d-1)\land W_N(H_x^-,d-1)\bigr],
\]
where \(H_x^+=\{y\in H:x\mid y\}\) and \(H_x^-=H\setminus H_x^+\). The query \(x=1\) is constant and cannot support a nonempty full binary split. The recurrence follows by taking the query at the root and then its two independent subtrees; conversely, two subtree witnesses attach to that root. The pruning rule \(|H|<2^d\implies\neg W_N(H,d)\) is sound because a hypothesis realizes at most one depth-\(d\) root-to-leaf bit sequence. The stronger prerequisite \(|H_x^\pm|\ge 2^{d-1}\) is likewise exact as a necessary condition; failing it cannot conceal a witness.

The accompanying `verify.py` enumerates *every* candidate root query \(2\le x\le N\) and evaluates this recurrence with memoization using exact integer bitsets (no approximations or random tests). Replaying it verifies, for each of the seven claimed thresholds \(t_d\), both \(\neg W_{t_d-1}(X_{t_d-1},d)\) and \(W_{t_d}(X_{t_d},d)\). This exhausts all smaller initial segments because the class embeds monotonically as \(N\) increases. In addition, the script verifies \(\neg W_{1280}(X_{1280},8)\); thus \(L_{1280}=7\) exactly. The bundled `witness.json` is a *standalone explicit* depth-seven full decision tree with 128 distinct leaf hypotheses from \(X_{1280}\), checked separately against integer divisibility along every path.

### First gap of size three
By the threshold calculation, \(L_N\) is respectively \(0,1,2,3,4,5,6\) on the consecutive intervals with endpoints \(1,2,4,9,27,81,320,1280\). By the exact VC formula, the VC thresholds through \(1280\) occur at \(2,6,30,210\), with the next at \(2310\). Comparing these intervals shows \(L_N-V_N\le2\) for every \(1\le N\le1279\), while at \(1280\) it is \(7-4=3\).

## Verification
Run `python3 verify.py` and `python3 verify_secondary.py` in the directory containing this document, the script, and `witness.json`. The script checks 14 threshold boundary values, absence of depth eight at \(N=1280\), the VC formula, and all 128 leaf paths of the supplied depth-seven tree. The two separately coded recurrences print `CERTIFIED` and `SECONDARY_OK` only if the required exact assertions pass. The transcript in `CHECKS.txt` records one actual replay; the scripts and witness, not that transcript alone, form the reproducible evidence. The exhaustive negative tests apply only to the stated finite values and are not proofs of impossibility in any infinite extension.

## Relationship to prior work
Malliaris and Moran (2021) treat Littlestone classes and model-theoretic stability in general, including full binary mistake trees, without an exact finite-divisibility threshold sequence. Walker (2022) gives the general tree-dimension/Sauer–Shelah framework; it bounds shatter functions but does not evaluate the divisibility predicate at a particular \(N\). A separate query-efficiency literature studies richer divisibility oracles for recovering unknown periods, a different measurement from adversarial online mistake trees. The present result supplies an exact arithmetic **first-gap cutoff**, not a competing general Sauer–Shelah theorem.

## Limitations
The Littlestone thresholds are verified only through depth seven. This does not classify the next threshold, infinite-dimensional behavior, randomized learning, noisy labels, or arbitrary number-theoretic predicates. The first-gap cutoff depends on the exact rule that both queries and hidden integers lie in \(\{1,\ldots,N\}\). Literature-priority risk remains for synonymous descriptions such as thicket dimension of divisibility posets; a negative search is not proof of global novelty.

## References
1. Maryanthe Malliaris and Shay Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first posted August 12, 2021. https://arxiv.org/abs/2108.05569
2. Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted March 23, 2022. https://arxiv.org/abs/2203.12211
3. David García-Soriano, *Query-Efficient Computation in Property Testing and Learning Theory*, PhD thesis (2012), §9.3.1 (different divisibility oracle model). https://ir.cwi.nl/pub/20273
