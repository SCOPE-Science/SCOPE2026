# Exact periodic-orbit census for tie-retaining majority on complete tripartite graphs

## Finding
Let \(a,b,c\) be arbitrary positive integers and let \(G=K_{a,b,c}\) be the **labelled**, loopless complete tripartite graph. Under synchronous binary majority dynamics, every vertex adopts the strict majority of its neighbors, retaining its previous value when they tie. Write \(F\) for the resulting deterministic map on \(\{0,1\}^{a+b+c}\), and \((n_1,n_2,n_3)=(a,b,c)\).

For positive integers \(s,r\), define the central binomial band
\[
B(s,r)=\sum_{\substack{0\le j\le r\\|2j-r|<s}}\binom rj.
\]
Let \(U=1\) if exactly one of \(a,b,c\) is strictly larger than both the others, and let \(U=0\) otherwise. Then the number \(P_1\) of fixed configurations and the number \(P_2\) of *primitive two-cycles (unoriented pairs of configurations)* are exactly
\[
P_1=2+\mathbf1_{\{2\mid a,\ 2\mid b,\ 2\mid c\}}
\binom a{a/2}\binom b{b/2}\binom c{c/2},
\]
\[
P_2=U+\sum_{\substack{1\le i<j\le3\\ n_i=n_j}} B(n_i,n_k),
\qquad\text{where }\{k\}=\{1,2,3\}\setminus\{i,j\}.
\]
(The binomial-product term is understood to be zero unless all three sizes are even.) Every trajectory eventually reaches a fixed point or two-cycle. Thus for every positive integer \(t\),
\[
\#\operatorname{Fix}(F^t)=\begin{cases}P_1,&t\text{ odd},\\P_1+2P_2,&t\text{ even},\end{cases}
\qquad
\zeta_F(z)=\frac1{(1-z)^{P_1}(1-z^2)^{P_2}}.
\]
The zeta function is the Artin–Mazur generating function of periodic-point counts, as a formal series.

The classification has a sharp size-equality effect. When \(a,b,c\) are pairwise distinct, there is **exactly one** primitive two-cycle: all three parts flip, with the uniquely largest part opposite the other two. If all sizes are equal to \(m\), then \(P_2=3(2^m-2)\); these cycles have exactly two oscillating parts and one unchanged part. For \(m=1\) there are no such cycles.

## Assumptions and scope
All three parts are nonempty and all vertices inside a given part have the same neighbors, namely every vertex outside that part. Updates are simultaneous. A tied local neighborhood causes the vertex to *keep its own bit*, rather than preferring either bit or randomizing. States are distinct according to their labelled individual vertices, not identified under graph automorphisms. A fixed point is a configuration \(x\) with \(F(x)=x\); a primitive two-cycle is an unordered pair \(\{x,y\}\) with \(x\ne y\), \(F(x)=y\), \(F(y)=x\).

## Proof
**1. Eventually only periods one and two occur.** Write every bit as a spin \(\sigma_v\in\{-1,1\}\). Let \(A\) be the symmetric adjacency matrix of \(G\), and let \(B=A+\tfrac12 I\). Since every neighbor sum is an integer, the update is exactly
\[
\sigma_v(t+1)=\operatorname{sgn}((B\sigma(t))_v),
\]
with no zero arguments. Define the two-time energy \(E_t=-\sigma(t+1)^TB\sigma(t)\). Using the symmetry of \(B\),
\[
E_{t+1}-E_t=\sum_v[\sigma_v(t)-\sigma_v(t+2)](B\sigma(t+1))_v.
\]
Each summand is zero when the two spins match, and equals \(-2|(B\sigma(t+1))_v|<0\) when they differ. The energy has only finitely many possible values; consequently there is a time beyond which \(\sigma(t+2)=\sigma(t)\). This self-contained energy argument is the standard symmetric-threshold mechanism.

**2. Fixed configurations.** Write \(x_i\) for the number of ones in part \(i\). In a fixed configuration any part containing both bits must see a tie: for such \(i\),
\[
2\sum_{j\ne i}x_j=\sum_{j\ne i}n_j.
\]
With all three parts mixed, these three equations force \(x_i=n_i/2\) for every \(i\), possible exactly when all sizes are even. Each part then admits \(\binom{n_i}{n_i/2}\) independent label choices.

Exactly two mixed parts cannot be fixed: if the third part is all zeros, the other two tie equations make its neighboring one-count strictly above half; if it is all ones, they make that count strictly below half. Exactly one mixed part is also impossible: its two homogeneous neighboring parts must have equal sizes and opposite bits to provide a tie, but then the zero homogeneous part and the one homogeneous part impose incompatible inequalities on the mixed part's one-count. If all parts are homogeneous, any nonunanimous triple has either a single one-part whose neighbors are all zero, or a single zero-part whose neighbors are all one; in either case it changes. Hence the two unanimous states and the possible three-way half-split states are the only fixed configurations.

**3. Primitive two-cycles.** A nonuniform part can never be generated from a homogeneous one: one update either preserves its existing bit pattern on a tie or replaces the entire part by one bit. Hence on a two-cycle each part is either unchanged vertex by vertex, or oscillates completely between all zeros and all ones. A single oscillating part is impossible because its neighbors would remain unchanged. Two oscillating parts must oscillate in opposite directions, for otherwise each would see its neighbors change in the wrong direction for reversal.

Suppose parts \(i,j\) oscillate oppositely, while part \(k\) is unchanged. Its outside-neighbor one-count alternates between \(n_i\) and \(n_j\). An unchanged part, whether homogeneous or mixed, can survive both phases only if \(n_i=n_j=s\): if the counts differ, one is strictly above and one strictly below their midpoint. For equal sizes, part \(k\) always sees a tie and therefore can retain an arbitrary pattern with \(b\) ones. The strict flip conditions on parts \(i,j\) reduce exactly to
\[
\frac{n_k-s}{2}<b<\frac{n_k+s}{2}
\quad\Longleftrightarrow\quad |2b-n_k|<s.
\]
Every such pattern produces one distinct unoriented two-cycle. Its number is \(B(s,n_k)\).

If all three parts oscillate, not all can move in the same direction. After possibly exchanging the two phases, two parts start all zero and the third starts all one. The first two flip to one and the third flips to zero precisely when the third part is strictly larger than **each** of the first two. This gives one two-cycle exactly if the largest part is unique, and none otherwise. The cases of two or three oscillating parts are disjoint and exhaustive, establishing \(P_2\).

**4. Periodic-point and zeta counts.** Step 1 excludes primitive periods beyond two. Every fixed point contributes one point to \(\operatorname{Fix}(F^t)\) for every \(t\); each primitive two-cycle contributes two points if and only if \(t\) is even. The product zeta formula follows from the standard decomposition by primitive orbit lengths.

## Verification
The standalone script `verify.py` uses two independent finite enumerations: (i) all \(12^3=1728\) ordered positive part-size triples with each size at most \(12\), tracking all part-count triples weighted by products of binomial coefficients; (ii) all \(220\) ordered positive part-size triples with total size at most \(12\), evolving every one of their combined \(376824\) labelled configurations using explicit per-vertex neighbors. In each test the observed fixed-point and unoriented two-cycle totals agree with the formulas. Run `python verify.py` with Python 3 (standard library only). These finite tests corroborate, but do not replace, the proof for arbitrary part sizes.

## Relationship to prior work
Goles and Olivos (1980) established the general eventual period-at-most-two theorem for symmetric threshold networks; this proof invokes the same classical energy mechanism but explicitly derives new size-dependent fixed-state and primitive-two-cycle counts. Goles and Tchuente (1983) investigated generalized majority rules and algebraic invariants; full text was not available for detailed comparison. Mossel, Neeman and Tamuz (2012) analyze information aggregation under majority updates. Tamuz and Tessler (2013) analyze information retention. Kaaser, Mallmann-Trenn and Natale (2015) examine majority convergence time, including contraction bounds for Turán graphs, but do not give the stated enumeration of all recurrent configurations on arbitrary three-part complete multipartite graphs. Parity automata on complete multipartite graphs use a different linear update and do not imply the present nonlinear majority census.

## Limitations
The theorem counts and classifies periodic states and periodic orbits but does not count their attraction basins or determine the exact transient length of each initial state. Results depend on the tie-retention convention. Historical priority is not independently certified; older generalized-majority full texts were not fully accessible during the comparison, and a broader prior enumeration cannot be ruled out solely from available abstracts.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
- E. Goles and M. Tchuente, *Iterative behaviour of generalized majority functions*, Mathematical Social Sciences 4 (1983), 197–204, DOI: 10.1016/0165-4896(83)90023-9.
- E. Mossel, J. Neeman, O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1 (first public 2012-07-04).
- O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035v1 (first public 2013-07-15).
- D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (first public 2015-08-14).
