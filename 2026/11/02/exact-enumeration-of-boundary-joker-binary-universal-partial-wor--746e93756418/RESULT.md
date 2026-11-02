# Exact enumeration of boundary-joker binary universal partial words

## Finding
A **linear universal partial word** of order \(n\) over \(\{0,1\}\) is a finite word over \(\{0,1,\diamond\}\) in which each of the \(2^n\) binary words of length \(n\) is matched by exactly one consecutive window, with \(\diamond\) independently matching either bit. Here a *single-joker* word has exactly one occurrence of \(\diamond\). Let \(U_{n,k}\) count the distinct indexed single-joker universal partial words whose joker is the \(k\)-th symbol from the left. Words are not identified under complementation, reversal, or any rotation.

**Theorem.** For all \(n\ge 2\),
\[
U_{n,1}=2^{\,2^{n-1}-n+1}.
\]
For the second symbol,
\[
U_{2,2}=0,\qquad U_{3,2}=2,\qquad
U_{n,2}=\frac{2^{\,2^{n-1}-n}}{3}\left(1-\left(-\frac12\right)^{n-2}\right)
\quad(n\ge4).
\]
By reversal these counts also apply to a joker in the last or penultimate position, respectively (within the corresponding word length). In particular the exact ratio for the first two placements has a parity-dependent correction,
\[
\frac{U_{n,2}}{U_{n,1}}=\frac16\left(1-\left(-\frac12\right)^{n-2}\right)
\quad(n\ge4),
\]
and tends to \(1/6\).

| Order \(n\) | First-symbol joker | Second-symbol joker |
|---:|---:|---:|
| 2 | 2 | 0 |
| 3 | 4 | 2 |
| 4 | 32 | 4 |
| 5 | 4096 | 768 |
| 6 | 134217728 | 20971520 |

## Assumptions and scope
The alphabet is exactly binary, the wildcard occurs exactly once, and each ordinary binary length-\(n\) word must have one **matching window**, not merely appear somewhere among a union of possibilities. In particular, a window containing one joker represents two distinct binary words. All positions are indexed starting at one; no quotient by symmetry is taken. For \(k=1\) or \(2\), the joker belongs to exactly \(k\) length-\(n\) windows, so a valid partial word must have length \(2^n+n-k-1\). The theorem counts all valid words of these prescribed lengths, not only a chosen construction family.

## Proof
**1. The graph and its arborescences.** Put \(m=n-1\) and let \(B_m\) be the binary directed de Bruijn graph: vertices are binary \(m\)-words, while each binary length-\(n\) word \(x_1\cdots x_n\) labels the directed edge from \(x_1\cdots x_m\) to \(x_2\cdots x_n\). Each vertex has in- and outdegree two. If the first \(k\) length-\(n\) windows contain the joker, their \(2k\) expansions are precisely the deleted edges of \(B_m\); the remaining ordinary windows, in their order, are an Euler trail through the remaining directed edges. The start of this trail is the length-\(m\) block immediately following the joker. Conversely an Euler trail gives one and only one continuation of the indicated partial prefix.

Write \(T_n\) for the number of directed in-arborescences of \(B_m\) toward any specified root. The random-appended-bit transition matrix \(P\) on its \(N=2^m\) vertices satisfies \(P^m=\Pi\), with all entries of \(\Pi\) equal to \(1/N\). Thus the Laplacian \(2(I-P)\) has one zero eigenvalue and \(N-1\) eigenvalues equal to two, including algebraic multiplicities. Since the graph is Eulerian, the directed matrix-tree theorem makes all root cofactors equal. Their sum is the product of nonzero eigenvalues, giving
\[
T_n=\frac{2^{N-1}}{N}=2^{\,2^{n-1}-n}.
\]
For a remaining graph with an Euler trail from \(s\) to \(t\), the directed BEST/last-exit formula gives its number of ordered edge trails as
\[
\tau_t\prod_v\bigl(d^+(v)-1+\mathbf1_{v=t}\bigr)!,
\]
where \(\tau_t\) counts in-arborescences rooted at \(t\). In the graphs below every factorial is one. Edge labels are all distinct, so no division for edge multiplicities is necessary.

**2. Joker in position one.** Write the prefix as \(\diamond s\), with \(|s|=m\). The two removed edges are those labeled \(0s\) and \(1s\), both entering \(s\). Their origins are \(0s_1\cdots s_{m-1}\) and \(1s_1\cdots s_{m-1}\). In the remaining graph, the vertex \(s\) has excess outdegree two, except if it equals one of these origins. A single Euler trail beginning at \(s\) demands excess exactly one. Therefore \(s\) is constant, all zeros or all ones. These are distinct complementary cases.

For \(s=0^m\), the removed edges are the loop \(0^n\) at \(s\) and the edge from \(t=10^{m-1}\) to \(s\). In-arborescences rooted at \(t\) never use a loop or an edge leaving the root, hence all \(T_n\) original arborescences survive. Every retained vertex has positive outdegree and all BEST factors are one. Consequently exactly \(T_n\) trails complete this prefix, and complementation doubles the answer to \(2T_n\).

**3. The forced period-two prefix in position two.** The first \(n+1\) symbols have the form \(a\diamond s\) with \(|s|=m\). Their first two length-\(n\) windows expand to two two-edge walks, starting at \(a0s_1\cdots s_{m-2}\) and \(a1s_1\cdots s_{m-2}\), both ending at \(s\). For a single trail to cover all remaining edges beginning at \(s\), degree balance forces \(s\) to equal one of these two initial vertices. Hence \(s\) is two-periodic and begins with \(a\). If the first two bits of its period are equal, the two wildcard windows have a common binary expansion, which is forbidden. Thus its two period symbols are different. There are exactly two possible prefixes, exchanged by bit complementation: \(0\diamond 0101\cdots\) and \(1\diamond 1010\cdots\), truncated after \(m\) bits beyond the joker.

At \(n=2\) the two joker windows necessarily overlap in a binary expansion, so no word is possible. At \(n=3\), the two completions are \(0\diamond011100\) and \(1\diamond100011\). For the rest assume \(n\ge4\).

**4. Three-edge tree update.** Fix the prefix starting \(0\diamond\). Let \(s\) be the alternating length-\(m\) binary word starting with zero and \(b\) its bitwise complement. Put
\[
t=00s_1\cdots s_{m-2},\qquad c=00b_1\cdots b_{m-2}.
\]
Exactly four graph edges are removed:
\[
t\longrightarrow c,\qquad s\longrightarrow b,\qquad c\longrightarrow s,\qquad b\longrightarrow s.
\]
The remaining graph has Euler-trail imbalance \(+1\) at \(s\) and \(-1\) at \(t\). Its positive outdegrees are one or two, and its terminal vertex \(t\) has outdegree one. Therefore all last-exit factorials are one. Let \(L_t\) be the root-\(t\) cofactor of the original Laplacian and \(G=L_t^{-1}\). The removal of \(t\to c\) leaves this cofactor unchanged because the deleted edge leaves the root. For the other three edges set
\[
(u_1,v_1)=(s,b),\quad (u_2,v_2)=(c,s),\quad (u_3,v_3)=(b,s).
\]
By the matrix determinant lemma, the surviving in-arborescence count is
\[
\tau_t=T_n\det(I_3-K),\qquad
K_{ij}=(e_{u_i}-e_{v_i})^{\mathsf T}G e_{u_j},
\]
with all vector coordinates taken off the root.

**5. Exact evaluation of the three-by-three update.** For arbitrary nonroot vertices \(x,y\), the inverse Laplacian has the finite Green-function expression
\[
G_{xy}=\frac12\sum_{j=0}^{m-1}\left(P^j_{xy}-P^j_{ty}-P^j_{xt}+P^j_{tt}\right).
\]
Indeed \(P^m=\Pi\); telescoping \(2(I-P)G\) gives the identity in every nonroot row, and the displayed function vanishes at the root. Also, for \(0\le j<m\),
\[
P^j_{xy}=2^{-j}\mathbf1\{x_{j+1}\cdots x_m=y_1\cdots y_{m-j}\}.
\]
These formulas allow an overlap-only evaluation, without inversion of a large matrix. For the alternating words \(s,b\), the difference between the indicators of the overlaps \(s\to s\) and \(b\to s\) is \((-1)^j\); all overlaps of length at least two from \(s\) or \(b\) into \(c\) or \(t\) vanish because the latter begin with \(00\). Only the length-one terminal overlap needs its sign adjusted. Writing
\[
\rho=\left(-\frac12\right)^{m-1},\qquad
\alpha=\frac{1-\rho}{3},\qquad \beta=\frac{1+2\rho}{3},
\]
the six matrix entries affecting the determinant are, by these explicit finite geometric sums,
\[
\begin{aligned}
K_{11}&=\frac12\sum_{j=0}^{m-2}\left(-\frac12\right)^j=\alpha,&
K_{13}&=-\alpha+\frac{(-1)^m}{2^{m-1}}=-\beta,\\
K_{31}&=-\alpha,&
K_{33}&=\alpha+\frac{(-1)^{m-1}}{2^{m-1}}=\beta,\\
K_{12}&=K_{32}=0,& K_{22}&=\frac12.
\end{aligned}
\]
For the last identity, the only noncancelled overlap in the \(c\)-versus-\(t\) comparison is the length-\(m\) identity overlap at \(j=0\): no proper suffix of \(c\) of length at least two starts with \(00\), while the length-one overlaps cancel. Therefore
\[
K=\begin{pmatrix}\alpha&0&-\beta\\ *&1/2&*\\-\alpha&0&\beta\end{pmatrix},\qquad
\det(I_3-K)=\frac{1-\alpha-\beta}{2}=\frac\alpha2,
\]
because \(2\alpha+\beta=1\). Thus the fixed prefix has precisely \(T_n\alpha/2\) Euler-trail continuations. Complementation yields
\[
U_{n,2}=T_n\alpha=\frac{2^{\,2^{n-1}-n}}{3}\left(1-\left(-\frac12\right)^{n-2}\right),
\]
which completes the proof. Positivity of the displayed arborescence count, together with the degree conditions, also guarantees existence of an Euler trail in every claimed case.

## Verification
Run `python3 verify.py` with standard Python 3. The script independently enumerates all partial words for the feasible small cases through \(n=4\); counts Euler trails by exhaustive edge-subset recursion through \(n=5\); computes exact integer Laplacian cofactors through \(n=6\); and checks the rational overlap matrix and determinant formula for \(4\le n\le40\). It prints `VERIFY_OK` if every assertion passes. The finite checks corroborate the all-length analytical proof but do not replace its overlap summation and matrix-tree arguments.

## Relationship to prior work
Chen, Kitaev, Mütze and Sun's *On universal partial words*, initially public on 25 January 2016, proves existence of single-joker binary universal partial words at the first position (Theorem 9) and at positions two through \(n-1\) (Theorem 10 in the later full version); it does **not** give the exact all-length counts established here. Its explicit examples up to order five distinguish existence from complete enumeration. The original graph-removal strategy supplies the natural starting point for the present enumeration; the new count for the second position depends on a nontrivial rank-three arborescence ratio. The first-position count supplies a comparison baseline and is a direct simpler consequence of standard directed tree enumeration.

The 2018 *Universal Partial Words over Non-Binary Alphabets* identifies enumeration as an underexplored question, but chiefly studies alphabet sizes above two and cyclicity. The 2026 open-access *The existence and structure of universal partial cycles* studies cyclic partial words; its lift and perfect-necklace constructions do not provide counts for these indexed linear boundary-joker words. A standard de Bruijn count without joker is not itself a count for the stated partial-word classes.

## Limitations
The exact formulas cover one joker in the first or second position (and their reversals) only. They do not count all interior-joker words, multiple-joker words, cyclic partial words, or larger alphabets. Although the argument is a mathematical proof, a separately conducted independent scientific review and exhaustive historical-priority determination have not been performed. In particular, older unpublished or unindexed enumerative results could affect priority.

## References
1. H. Z. Q. Chen, S. Kitaev, T. Mütze and B. Y. Sun, *On universal partial words*, arXiv:1601.06456, first submission 2016-01-25; full text https://arxiv.org/html/1601.06456v4 ; journal DOI https://doi.org/10.23638/DMTCS-19-1-16 .
2. B. Goeckner et al., *Universal Partial Words over Non-Binary Alphabets*, arXiv:1611.03928, https://arxiv.org/abs/1611.03928 ; *Theoretical Computer Science* 713 (2018), 56–65.
3. D. Fillmore et al., *The existence and structure of universal partial cycles*, *Designs, Codes and Cryptography* 94 (2026), article 152, https://doi.org/10.1007/s10623-026-01841-x .
4. Standard results used in their usual directed-graph form: the directed matrix-tree theorem, the directed BEST/last-exit Euler-trail formula, and the matrix determinant lemma.
