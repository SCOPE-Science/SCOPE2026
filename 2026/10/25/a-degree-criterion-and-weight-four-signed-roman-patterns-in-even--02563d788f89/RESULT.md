# A degree criterion and weight-four signed Roman patterns in even Kneser graphs

## Finding

Let \(n\ge12\) be even. On the Kneser graph \(K_{n,2}\), whose vertices are the two-element subsets of \([n]\) and whose edges join disjoint subsets, a signed Roman dominating function takes values in \(\{-1,1,2\}\), has closed-neighborhood sum at least one at every vertex, and gives every \(-1\)-labeled vertex a neighboring \(2\)-labeled vertex. Its minimum weight is denoted \(\gamma_{sR}(K_{n,2})\).

**Theorem.** For every even \(n\ge12\),
\[
2\le \gamma_{sR}(K_{n,2})\le4.
\]
There is an explicit family of signed Roman dominating functions of weight exactly \(4\), with the following precise structural properties.

Put \(a=n/2-1\) and \(b=n/2+1\), and partition \([n]\) into labeled sets \(A,B\) of these orders. For graphs \(H_A\subseteq\binom A2\) and \(H_B\subseteq\binom B2\), give a Kneser vertex \(uv\) label \(-1\) when \(u\) and \(v\) lie on opposite sides, label \(2\) when \(uv\) belongs to \(H_A\cup H_B\), and label \(1\) otherwise. An exact necessary-and-sufficient degree criterion for this class of labelings is proved below; **the least feasible weight within this entire fixed-size cut-pattern class is \(4\)** (not necessarily the least weight among all signed Roman functions).

More concretely, set
\[
s=\lfloor b/2\rfloor,\qquad r=n/2+2-s.
\]
Choose \(H_B\) to be any matching of size \(s\) in \(B\); for \(n=12\), choose \(H_A\) to be a cycle on the five vertices of \(A\); for even \(n\ge14\), choose \(H_A\) to be any path with \(r\) edges on \(r+1\) vertices of \(A\). Every such choice yields a valid signed Roman function of weight \(4\). The number of distinct functions given by this designated construction is exactly
\[
\binom na\frac{b!}{2^s s!(b-2s)!}\,Q_{a,r},\qquad
Q_{a,r}=\begin{cases}
(a-1)!/2,& n=12,\\
\binom{a}{r+1}(r+1)!/2,& n\ge14.
\end{cases}
\]
This is a count of a constructive **subfamily**, not a count of all weight-four functions. It equals \(997{,}920\) when \(n=12\) and \(113{,}513{,}400\) when \(n=14\).

## Assumptions and scope

All graphs are finite, simple, and labeled. The denominator and factorial expressions are ordinary integer combinatorial counts. A graph \(H_A\) or \(H_B\) has vertex set \(A\) or \(B\), including isolated vertices. Write \(d_A(u)=\deg_{H_A}(u)\), \(d_B(v)=\deg_{H_B}(v)\), \(\Delta_A=\max_{u\in A}d_A(u)\), \(\Delta_B=\max_{v\in B}d_B(v)\), and \(t=|E(H_A)|+|E(H_B)|\). The weight of the resulting function is
\[
T=2-\frac n2+t.
\]

The claim is a bound and a structural result **for even \(n\ge12\)**; no assertion of equality \(\gamma_{sR}=4\) for unrestricted functions is made. The previously published lower bound \(2\) is used as prior work.

## Proof

**Incidence identity.** Write \(f_{uv}\) for the label on Kneser vertex \(\{u,v\}\), let \(T=\sum_{u<v}f_{uv}\), and let \(S_u=\sum_{v\ne u}f_{uv}\). The closed neighborhood of Kneser vertex \(\{u,v\}\) comprises that vertex together with all pairs disjoint from \(\{u,v\}\). Therefore its label sum is exactly
\[
T-S_u-S_v+2f_{uv}.
\tag{1}
\]
The two sums \(S_u,S_v\) count the edge \(uv\) twice; excluding all incident pairs and restoring the vertex itself produces the coefficient \(2\) in (1).

**Exact cut-pattern criterion.** For the partition and labels of the theorem,
\[
S_u=-3+d_A(u)\quad(u\in A),\qquad
S_v=1+d_B(v)\quad(v\in B).
\]
For a cross-pair \(uv\), (1) is \(T-d_A(u)-d_B(v)\). For an internal pair \(uv\) in \(A\), it is \(T+8-d_A(u)-d_A(v)+2\mathbf1_{uv\in E(H_A)}\); for an internal pair in \(B\), it is \(T-d_B(u)-d_B(v)+2\mathbf1_{uv\in E(H_B)}\). Finally, the number of label-\(2\) neighbors of a cross-pair \(uv\) equals \(t-d_A(u)-d_B(v)\). Thus the cut-pattern function is signed Roman dominating **if and only if** all four conditions hold:
\[
\begin{aligned}
&T\ge1+\Delta_A+\Delta_B,\\
&t\ge1+\Delta_A+\Delta_B,\\
&T+8-d_A(u)-d_A(v)+2\mathbf1_{uv\in E(H_A)}\ge1 && (uv\in\tbinom A2),\\
&T-d_B(u)-d_B(v)+2\mathbf1_{uv\in E(H_B)}\ge1 && (uv\in\tbinom B2).
\end{aligned}
\tag{2}
\]
These conditions check every closed neighborhood and every \(-1\) defender; vertices with label \(1\) or \(2\) require no separate defender condition.

**Existence at weight four.** Put \(s=\lfloor b/2\rfloor\) and \(r=n/2+2-s\). At \(n=12\), \(a=r=5\), so a cycle exists on \(A\). For every even \(n\ge14\), \(s\ge4\), whence \(r\le a-1\); the specified \(r\)-edge path fits in \(A\). Also \(r\ge5\) throughout. The matching in \(B\) exists by its definition. Their edge counts give \(t=r+s=n/2+2\), hence \(T=4\). We have \(\Delta_A\le2\) and \(\Delta_B\le1\), so the first condition in (2) holds and the second follows from \(t\ge8\). For internal pairs in \(A\), the third left-hand side is at least \(4+8-2-2=8\). For internal pairs in \(B\), the fourth is at least \(4-1-1=2\). Therefore (2) is satisfied and the constructed function is signed Roman dominating.

**Optimality within the cut-pattern class.** For any cut-pattern signed Roman function, the first condition in (2) implies \(T\ge1+\Delta_A+\Delta_B\). Suppose \(T\le3\). Since \(T=2-n/2+t\), the three integer possibilities \(T=1,2,3\) require, respectively, \(t=a,b-1,b\). At \(T=1\), the degree-sum bound forces no selected internal edges, contradicting \(t=a>0\). At \(T=2\), it forces \(\Delta_A+\Delta_B\le1\); all selected edges lie in a matching on one side, hence \(t\le\lfloor b/2\rfloor<b-1\), a contradiction. At \(T=3\), it forces \(\Delta_A+\Delta_B\le2\). If both maximum degrees are positive, each is at most one, so \(t\le\lfloor a/2\rfloor+\lfloor b/2\rfloor\le n/2<b\). If \(\Delta_B=0\), then \(t\le a<b\), because a maximum-degree-two graph on \(a\) vertices has at most \(a\) edges. In the remaining case \(\Delta_A=0\), we must have \(t=b\) with \(\Delta_B\le2\), forcing every vertex of \(H_B\) to have degree two. Since \(b\ge7\), some internal pair \(uv\) in \(B\) is absent from \(H_B\); for it the last expression of (2) is \(3-2-2=-1\), a contradiction. Thus no cut-pattern signed Roman function has weight below four.

**Counting the designated family.** There are \(\binom na\) choices for the smaller side \(A\); \(b!/(2^s s!(b-2s)!)\) matchings of size \(s\) in \(B\); \((a-1)!/2\) cycles on five labeled vertices in the boundary case; and \(\binom a{r+1}(r+1)!/2\) unoriented simple paths on \(r+1\) distinct vertices otherwise. The negative-labeled pairs recover the complete bipartite cut uniquely because \(a\ne b\). The label-\(2\) pairs recover both internal graphs. Hence no two counted choices give the same function, proving the count.

The published inequality \(\gamma_{sR}(K_{n,2})\ge2\) supplies the lower bound in the theorem.

## Verification

The reproducible scripts `verify_kn_signed_roman.py` and `check_criterion.py` use only Python's standard library. The first constructs the stated functions, independently evaluates *every* closed neighborhood by graph disjointness for fifteen even sizes from \(12\) through \(40\), and checks the incidence identity for fifty-nine even sizes through \(128\). It also checks the displayed family-count values. The second compares the criterion (2) against the original graph definition for all \(8{,}320\) cut-pattern subgraph choices on the two small illustrative orders \(6,8\), as well as \(300\) seeded random choices at order \(12\). These finite tests support error detection; the preceding proof covers the infinite statement.

## Relationship to prior work

Zec and Grbić, in *Several Roman domination graph invariants on Kneser graphs* (arXiv:2204.05664, initial public version dated 12 April 2022; DMTCS 25, 2023), proved for even \(n\ge12\) that \(2\le\gamma_{sR}(K_{n,2})\le5\), while for odd \(n\ge12\) their upper bound is \(3\). Their Theorem 3 gives weight-five even constructions; their Remark 3 determines the even case \(n=10\) exactly as \(4\). Their conclusion explicitly identifies tighter bounds on this Kneser parameter as a possible direction. The present construction reduces the published even upper bound by one for every even \(n\ge12\), while deriving a degree test, optimality inside a natural cut-based subclass, and a sizable counted family. The 2025 survey *Varieties of Roman domination IV* repeats the upper bound \(5\) rather than establishing the stronger inequality. These are statement-level comparisons, not a claim of exhaustive bibliographic priority.

## Limitations

It remains unproved here whether unrestricted signed Roman functions of weight \(2\) or \(3\) exist for any even \(n\ge12\); in particular **the exact signed Roman domination number is not determined**. The counted family is not asserted exhaustive among weight-four functions. The characterization (2) holds specifically for the chosen cut-pattern class. Possible unindexed or inaccessible stronger prior statements remain a priority risk. Self-review do not constitute independent mathematical validation.

## References

1. T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, arXiv:2204.05664v3 (first submitted 2022-04-12), *Discrete Mathematics & Theoretical Computer Science* 25 (2023), article 14. https://arxiv.org/html/2204.05664v3 ; https://doi.org/10.46298/dmtcs.10506 .
2. H. Abdollahzadeh Ahangar, M. A. Henning, C. Löwenstein, Y. Zhao, and V. Samodivkin, *Signed Roman domination in graphs*, *Journal of Combinatorial Optimization* 27 (2014), 241–255. https://doi.org/10.1007/s10878-012-9500-0 .
3. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, and L. Volkmann, *Varieties of Roman domination IV*, *AKCE International Journal of Graphs and Combinatorics* (online 2025). https://doi.org/10.1080/09728600.2025.2598772 .
