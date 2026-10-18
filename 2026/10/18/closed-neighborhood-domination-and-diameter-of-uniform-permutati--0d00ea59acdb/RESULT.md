# Closed-neighborhood domination and diameter of uniform permutation trees: a joint Gaussian law

## Finding

Let \(T_n\) be uniform among permutation inversion graphs on \(n\ge3\) vertices that are trees. Let \(\gamma_n\) be its *ordinary closed-neighborhood domination number*: the smallest cardinality of a set \(D\subseteq V(T_n)\) such that every vertex belongs to \(D\) or has a neighbor in \(D\). Let \(\Delta_n\) be the graph diameter. Then

\[
\mathbb E\gamma_n=\frac{2n}{7}+O(1),\qquad
\operatorname{Var}(\gamma_n)=\frac{18n}{343}+o(n),\qquad
\operatorname{Cov}(\gamma_n,\Delta_n)=\frac{3n}{49}+o(n).
\]

More precisely,

\[
\frac{1}{\sqrt n}
\begin{pmatrix}\gamma_n-2n/7\\\Delta_n-n/2\end{pmatrix}
\xrightarrow{d}
N_2\!\left(0,
\begin{pmatrix}18/343&3/49\\3/49&1/4\end{pmatrix}\right).
\]

The limit has correlation \(\sqrt{2/7}\), and its covariance matrix is positive definite, with determinant \(45/4802\). The known exact diameter law is \(\Delta_n\overset d=2+\operatorname{Bin}(n-3,1/2)\); the contribution here is the genuine vertex-domination statistic, its constants and its joint dependence on diameter.

## Assumptions and scope

The inversion graph of a permutation \(\pi\) has vertices its symbols and joins a pair whenever its symbols occur in inverted order. The tree is chosen uniformly among the \(2^{n-2}\) different tree permutation graphs. The Acan–Hitczenko bijection encodes each such tree by a uniform independent fair-bit word of length \(n-2\). Suppose the word has consecutive equal-bit run lengths \(b_1,\ldots,b_m\), so \(\sum_i b_i=n-2\). Its caterpillar spine has \(m\) vertices in order; the two endpoints support pendant leaves, and an interior spine vertex supports at least one pendant leaf precisely when its associated run has length at least two. The spine diameter is \(m+1\).

Put

\[
F=\{1,m\}\cup\{i:1<i<m,\ b_i\ge2\},
\]

with duplicates removed. If \(f_1<\cdots<f_t\) list \(F\), then the exact finite-word identity is

\[
\boxed{\gamma_n=t+\sum_{j=1}^{t-1}
\left\lfloor\frac{f_{j+1}-f_j-1}{3}\right\rfloor.}
\]

When \(m=1\), the tree is a star and the formula gives one. All assertions concern ordinary *vertex* domination; edge coverage (minimum vertex cover) is a different optimization problem.

## Proof

**1. Exact domination formula.** On any caterpillar, every spine vertex adjacent to a pendant leaf can be included in some minimum dominating set: replacing a selected pendant leaf by its unique spine neighbor cannot reduce domination of any vertex. These replacements can be made simultaneously, and can only improve domination elsewhere. For the run-coded tree these forced spine vertices are exactly \(F\). Between two consecutive forced vertices separated by \(k\) unforced degree-two vertices, the two endpoint vertices already dominate the adjacent interior vertices. The residual internal path has \(\max(k-2,0)\) vertices and requires \(\lceil\max(k-2,0)/3\rceil=\lfloor k/3\rfloor\) selected vertices. Different gaps cannot dominate one another, because forced vertices separate them. Summation proves the boxed exact identity. The one-spine-vertex case is immediate.

**2. Independent regeneration.** Extend the unbiased bit word indefinitely. Its complete equal-bit run lengths are independent and have geometric law \(\Pr\{L=j\}=2^{-j}\), for integers \(j\ge1\). Take one cycle to consist of \(K\) successive singleton runs followed by one long run \(J\ge2\). Then \(K\) and \(G=J-2\) are independent with

\[
\Pr\{K=k\}=\Pr\{G=k\}=2^{-(k+1)},\qquad k\ge0.
\]

The cycle consumes \(M=K+J=K+G+2\) word positions, contributes \(R=1+\lfloor K/3\rfloor\) to the interior domination formula, and contributes \(C=K+1\) to the number of spine vertices. Successive cycles are independent. Cutting at a deterministic word length changes each actual statistic, compared to complete-cycle rewards, by a boundary term with uniformly bounded moments of every fixed order: the initial forced endpoint changes the first gap contribution by at most one, and the final residual cycle has a geometrically decaying size. The additional \(2\) symbols that turn word length into vertex count and the extra \(1\) in diameter also affect only bounded terms.

In particular \(\mathbb E M=4\), \(\mathbb E R=8/7\), \(\mathbb E C=2\); the renewal-reward rates are \(\alpha=2/7\) and \(\beta=1/2\). The span of \(M\) is one and the cycles have exponential moments. The arithmetic renewal theorem and the exponentially bounded end corrections give \(\mathbb E\gamma_n=\alpha n+O(1)\).

**3. Exact centered cycle covariance.** Write \(K=3W+B\). Geometric memorylessness makes \(W\) and \(B\) independent, with

\[
\Pr\{W=w\}=\frac78\left(\frac18\right)^w\ (w\ge0),
\quad \Pr\{B=0,1,2\}=\left(\frac47,\frac27,\frac17\right).
\]

The independent variables have \(\operatorname{Var}W=8/49\), \(\operatorname{Var}B=26/49\), and \(\operatorname{Var}G=2\). The zero-mean, centered cycle-reward vector is exactly

\[
U=R-\alpha M=\frac{3+W-2B-2G}{7},\qquad
V=C-\beta M=\frac{3W+B-G}{2}.
\]

Independence gives

\[
\mathbb E U^2=\frac{72}{343},\qquad
\mathbb E UV=\frac{12}{49},\qquad
\mathbb E V^2=1.
\]

**4. Two-dimensional limit and moment constants.** Let \(N(t)\) count complete cycles consuming at most \(t\) word positions. By the renewal law of large numbers, \(N(t)/t\to1/4\) in probability. The multivariate iid partial-sum central limit theorem, followed by the random-time-change theorem, applies to sums of the centered pairs \((U,V)\). The age and overshoot and first/last boundary corrections are \(O_{L^q}(1)\) for every fixed \(q\), because the renewal interarrival lengths have exponential tails. Consequently those corrections vanish on division by \(\sqrt{n}\). This establishes the displayed bivariate normal law, with covariance \(\mathbb E[(U,V)^\top(U,V)]/4\), giving the stated matrix.

The same moment assumptions yield uniform integrability of squares via a fourth-moment bound for centered renewal-reward sums (or the standard renewal-reward second-moment theorem). Thus the variance and covariance limits hold as asserted, rather than being inferred merely from convergence in distribution. The determinant is positive, completing the argument.

## Verification

The standalone `verify.py` builds each tree from the independent binary insertion encoding and independently computes domination by brute-force search over all vertex subsets. It compares the result, and the graph diameter computed by independent breadth-first searches, against the exact run formula for every one of \(1{,}022\) words at orders \(3\le n\le11\). It also checks the centered renewal moments and the positive covariance determinant with exact rational arithmetic. Running `python verify.py` completed successfully. Enumeration is corroboration only; the all-size statements follow from the spine argument and renewal theory.

## Relationship to prior work

Acan and Hitczenko, *On random trees obtained from permutation graphs* (first posted 2014-06-16, arXiv:1406.3958), established the canonical binary-word correspondence, caterpillar structure and exact diameter law. Their Section 3.4 explicitly uses an *edge-incidence* condition for its stated “dominating set” (i.e. vertex cover), and their gap contribution is \(\lfloor k/2\rfloor\). The present claim uses the usual closed-neighborhood condition; its gap cost is \(\lfloor k/3\rfloor\), giving distinct linear-scale expectations and fluctuations. Neither their Theorem 20 nor their diameter law implies the present bivariate covariance constants.

Baren, Cory, Friedberg, Gardner, Hammer, Harrington, McGinnis, Waechter and Wong, *On the Domination Number of Permutation Graphs and an Application to Strong Fixed Points* (arXiv:1810.03409), explicitly studies ordinary closed-neighborhood domination of permutation graphs, but their inspected text treats extremal sizes, connected graph enumerations and algorithms, not the uniform tree-permutation model's limiting joint law. Related random-tree domination studies on recursive or search trees concern different probability measures. A semantic survey of published related work did not identify an implication establishing this exact law; absence of a search hit alone is not evidence of uniqueness.

## Limitations

The exact finite-tree identity concerns only inversion graphs that are trees; it makes no assertion about uniformly labeled Cayley trees or all permutation graphs. The renewal limit describes first- and second-order asymptotics; an all-order local limit or finite-sample distribution is not established. Literature priority beyond the primary texts inspected may contain an implicit equivalent renewal decomposition, especially in general random-caterpillar studies. This is a self-contained proof and finite computational corroboration, not independent certification or a proof of historical uniqueness.

## References

1. H. Acan and P. Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958, first posted 16 June 2014. See §§2–3.4, particularly Lemma 8, Lemma 12, Eq. (3.8) and Theorem 20.
2. T. Baren, M. Cory, M. Friedberg, P. Gardner, J. Hammer, J. Harrington, D. McGinnis, R. Waechter and T. W. H. Wong, *On the Domination Number of Permutation Graphs and an Application to Strong Fixed Points*, arXiv:1810.03409, first posted 8 October 2018. See §1 and §§2–7.
3. Standard lattice renewal-reward central limit and second-moment theorems for iid cycles with exponential moments; the required centered cycle variables and all parameters are calculated explicitly above.
