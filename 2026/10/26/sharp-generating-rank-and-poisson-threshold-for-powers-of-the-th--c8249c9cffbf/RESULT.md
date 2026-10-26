# Sharp generating rank and Poisson threshold for powers of the three-valued Boolean semialgebra

## Finding

Let \(\mathbf K_3=\{0,u,1\}\) be the three-valued Kleene Boolean semialgebra, where \(0<u<1\), \(\neg0=1\), \(\neg u=u\), \(\neg1=0\), conjunction and disjunction are minimum and maximum, and implication is \(x\to y=\neg x\vee y\). The named constants are \(0,1\); **\(u\) is not a named constant**. Let \(m,k\ge1\), and consider the coordinate-labelled direct power \(\mathbf K_3^m\).

Choose \(k\) prospective generators \(g_1,\ldots,g_k\in\mathbf K_3^m\). The word in coordinate \(i\) is \(a_i=(g_1(i),\ldots,g_k(i))\in\{0,u,1\}^k\). Define its associated Boolean subcube
\[
F(a_i)=\bigl\{z\in\{0,1\}^k:z_j=a_i(j)\text{ whenever }a_i(j)\ne u\bigr\}.
\]

**Theorem (generation, extremal rank, and random transition).** The tuple \((g_1,\ldots,g_k)\) generates the full direct power \(\mathbf K_3^m\) if and only if **every** \(a_i\) contains at least one \(u\), and the \(m\) Boolean subcubes \(F(a_i)\) are pairwise disjoint. In particular, a generating \(k\)-tuple exists precisely when \(m\le 2^{k-1}\), and the minimum number of algebra generators is
\[
\operatorname{rk}(\mathbf K_3^m)=1+\lceil\log_2 m\rceil.
\]
At the maximum size \(m=2^{k-1}\), every subcube must be an edge of the \(k\)-cube, and these edges constitute a perfect matching. Conversely every perfect matching, with an assignment of its edges to the \(m\) labelled algebra coordinates, gives a generating \(k\)-tuple. Thus the exact number of ordered generating \(k\)-tuples at maximum size is
\[
(2^{k-1})!\,\operatorname{pm}(Q_k),
\]
where \(\operatorname{pm}(Q_k)\) denotes the number of perfect matchings of the \(k\)-dimensional Boolean-cube graph.

For an independent uniformly sampled \(k\)-tuple of elements of \(\mathbf K_3^{m_k}\), let \(W_k\) count unordered pairs of coordinate words with intersecting Boolean subcubes. If \(k\to\infty\) and
\[
\frac{m_k}{(9/7)^{k/2}}\longrightarrow\lambda\in(0,\infty),
\]
then
\[
W_k\xrightarrow{d}\operatorname{Poisson}(\lambda^2/2),\qquad
\Pr\bigl(\langle g_1,\ldots,g_k\rangle=\mathbf K_3^{m_k}\bigr)\longrightarrow e^{-\lambda^2/2}.
\]
For \(m_k/(9/7)^{k/2}\to0\), the generation probability tends to \(1\); for \(m_k/(9/7)^{k/2}\to\infty\), it tends to \(0\), whenever \(m_k\ge1\).

## Assumptions and scope

The algebra signature comprises the two designated constants \(0,1\), binary \(\wedge,\vee,\to\), and unary \(\neg\). Implication introduces no extra term functions because \(x\to y=\neg x\vee y\). The constant \(u\) is deliberately *not* part of the signature. Generated means equality of the smallest subalgebra containing the displayed generators with the full labelled direct product. Boolean subcubes are defined in \(\{0,1\}^k\) without probabilistic independence assumptions; their intersection is the ordinary set-theoretic one. In the probability statement, each of the \(km_k\) entries is independent and uniformly distributed among \(0,u,1\). All asymptotics use integer sequences \(m_k\ge1\) and \(k\to\infty\).

## Proof

**Step 1: information monotonicity.** Give \(\{0,u,1\}\) the *information order* \(u\preceq 0\) and \(u\preceq1\), with \(0,1\) incomparable. Each primitive operation \(\wedge,\vee,\neg\) is monotone in its arguments for this order, and constants are monotone; hence every term function \(t:\mathbf K_3^k\to\mathbf K_3\) is information-monotone. This is readily checked on the two cover relations \(u\preceq0\) and \(u\preceq1\), using the ordinary strong-Kleene truth tables. Implication is a definitional abbreviation and likewise monotone in the information order.

Suppose \(F(a_i)\cap F(a_j)\ne\varnothing\). A common total Boolean completion \(z\in\{0,1\}^k\) satisfies \(a_i\preceq z\) and \(a_j\preceq z\). If a term were \(0\) at \(a_i\) and \(1\) at \(a_j\), then both \(0,1\preceq t(z)\), impossible. The full direct power contains a vector with coordinate values \(0\) and \(1\) at these two distinct coordinates, so such a compatible pair cannot occur in a generating tuple. If some \(a_i\) has no \(u\), it is a Boolean word, and all terms at \(a_i\) evaluate in \(\{0,1\}\) (the Boolean values form a subalgebra). The full power contains a vector with \(u\) there. Thus both conditions are necessary.

**Step 2: constructive sufficiency.** Now assume every \(a_i\) has a \(u\), and each pair of subcubes is disjoint. For each ordered pair \(i\ne j\) there is an index \(s=s(i,j)\) at which \(a_i(s),a_j(s)\) are the opposite definite values \(0,1\). Choose a literal \(\ell_{ij}\) from the generator variable \(X_s\) and its negation which equals \(1\) at \(a_i\) and \(0\) at \(a_j\). Let
\[
e_i=\bigwedge_{j\ne i}\ell_{ij},\]
with the empty meet interpreted as named constant \(1\). Then \(e_i(a_i)=1\), while \(e_i(a_j)=0\) for every \(j\ne i\). Choose any position \(s_i\) where \(a_i(s_i)=u\), and put \(h_i=e_i\wedge X_{s_i}\). This term is \(u\) on column \(i\) and \(0\) on all other columns. For any desired vector \(v\in\{0,u,1\}^m\), the term
\[
T_v=\bigvee_{i:v_i=1} e_i\;\vee\!\bigvee_{i:v_i=u} h_i
\]
(with empty joins interpreted as \(0\)) evaluates to \(v\) on \((a_1,\ldots,a_m)\). Therefore all \(3^m\) vectors occur in the generated subalgebra.

**Step 3: sharp rank and perfect matchings.** Each nondegenerate Boolean subcube has at least two vertices; disjointness gives \(2m\le 2^k\), or \(m\le2^{k-1}\). Conversely, partition \(\{0,1\}^k\) into its \(2^{k-1}\) parallel coordinate edges (fix the last \(k-1\) bits). Any \(m\le2^{k-1}\) of them produce the required words. This proves the generator rank. If equality holds in the volume bound, every selected subcube has exactly two vertices, hence is an edge, and the edges partition the cube: a perfect matching. There are \(m!\) ways to assign a fixed matching to the \(m\) labelled columns and exactly one ternary word per edge. This establishes the stated exact matching multiplier.

**Step 4: Poisson pair counts.** For two independent uniform ternary symbols, exactly \(7\) of the \(9\) ordered pairs are compatible as partial Boolean assignments. Thus two words have intersecting subcubes with probability \(p_k=(7/9)^k\). For three independent symbols \(A,B,C\), exactly \(17\) of the \(27\) triples satisfy simultaneous compatibility of \((A,B)\) and \((A,C)\). Hence two edge indicators sharing one endpoint have joint probability \(q_k=(17/27)^k\). Indicators based on disjoint index pairs are independent. Put \(\mu_k=\binom{m_k}{2}p_k\). The standard dependency-neighbourhood Chen–Stein Poisson bound (Arratia–Goldstein–Gordon) gives
\[
d_{\mathrm{TV}}\bigl(\mathcal L(W_k),\operatorname{Pois}(\mu_k)\bigr)
\le C\bigl(m_k^3 p_k^2+m_k^3q_k\bigr)
\]
for an absolute constant \(C\) when \(\mu_k\) is bounded. For \(m_k/(9/7)^{k/2}\to\lambda\), the first term tends to zero and the second does too because
\[
(9/7)^{3/2}(17/27)=0.917913720165\ldots<1.
\]
Furthermore \(\mu_k\to\lambda^2/2\). It follows that \(W_k\) converges to the stated Poisson law.

An independent uniform ternary column has no \(u\) with probability \((2/3)^k\). By the union bound the chance any of the \(m_k\) columns is completely Boolean is at most \(m_k(2/3)^k=o(1)\) because \((9/7)^{1/2}(2/3)<1\). By Steps 1–2 generation occurs exactly when this obstruction and \(W_k\) are both absent, proving the displayed generation probability. If the normalizing ratio tends to zero, the same union bounds for nongeneration give success with probability tending to one. If it tends to infinity, retaining an arbitrary fixed \(\lambda(9/7)^{k/2}\) columns bounds the original success probability above by \(e^{-\lambda^2/2}+o(1)\); let \(\lambda\to\infty\) to obtain zero. This proves all assertions.

## Verification

A standalone standard-library Python checker accompanies this statement. It implements the original strong-Kleene truth tables and computes generated subalgebras by repeated closure under both named constants, negation, conjunction and disjunction. For all \(m,k\in\{1,2,3\}\) it exhaustively compares actual generation of \(\mathbf K_3^m\) with the disjoint-subcube criterion for every ordered tuple. The passing generator-tuple totals, ordered by \(k=1,2,3\), are: \(m=1\): \(1,5,19\); \(m=2\): \(0,4,138\); \(m=3\): \(0,0,336\). An independent subcube-only enumerator checks the totals, and a hypercube matching recursion verifies perfect-matching counts \(1,2,9,272\) for \(k=1,2,3,4\). Direct enumeration independently gives the crucial single-digit probabilities \(7/9\) and \(17/27\). The checker reports `ALL_CHECKS_OK` when successful. These finite checks are corroboration, not proofs for unbounded \(m,k\) or the asymptotic limit; those depend on the arguments above and the stated standard Poisson approximation theorem.

## Relationship to prior work

Abou El Wafa and Platzer (2026), Examples 12–13, establish the finite Kleene Boolean semialgebra and its direct powers as the algebra of partial two-valued functions. Those definitions motivate the algebraic-generation problem; their paper does not provide the present generating-tuple criterion or random-generation theorem in the inspected material. Classical work on free Kleene algebras and fuzzy switching functions studies the cardinalities and representations of term-function algebras, rather than the particular random surjectivity problem studied here.

Falgas-Ravry and Markström (2016) study the **same subcube-intersection random graph model**, with uniform ternary labels corresponding to their binomial parameter \(p=1/3\). Their clique-appearance threshold includes the exponential scale at which the first edge appears. Thus that scale is acknowledged as prior mathematics. Their Theorem 1 and Corollary 2 give a zero-one threshold outside a shrinking critical window, but do not state the exact Poisson edge-count law \(\operatorname{Pois}(\lambda^2/2)\) at the critical window or its equivalence to generation of a finite Boolean semialgebra. The latter algebraic application and sharp finite-rank characterization form the combined contribution here. Standard Chen–Stein Poisson approximation is used as a known theorem, not claimed as new.

## Limitations

The random model samples every entry independently with the **uniform** ternary distribution. Biased sampling, nonindependent generators, other algebra signatures (especially a named constant \(u\)), and arbitrary Boolean semialgebras are not covered. The matching formula at maximal capacity invokes the known perfect-matching number and is not a closed-form evaluation of that number for general \(k\). The result gives a Poisson limit for compatible pairs, not full convergence of the resulting graph to an Erdős–Rényi random graph in every regime. An older equivalent characterization of Kleene term functions or a prior special-case Poisson theorem under different terminology remains a priority risk. No independent scientific audit is claimed.

## References

1. N. Abou El Wafa and A. Platzer, *Subreflexive Logic: Completeness without Identity* (first publicly posted July 27, 2026), arXiv:2607.24623, https://arxiv.org/abs/2607.24623, Examples 12–13.
2. V. Falgas-Ravry and K. Markström, *Random Subcube Intersection Graphs I: Cliques and Covering*, Electronic Journal of Combinatorics 23(3), P3.43 (2016), doi:10.37236/5472, arXiv:1309.7375, Section 2, Theorem 1 and Corollary 2.
3. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25.
4. J. Berman and M. Mukaidono, *Enumerating fuzzy switching functions and free Kleene algebras*, Computers & Mathematics with Applications 10 (1984), 25–35, doi:10.1016/0898-1221(84)90083-X.
