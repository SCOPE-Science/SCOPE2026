# A mod-four census of optimal general three-position sets on cycles

## Finding

Let \(C_n\) be the simple cycle with named vertices \(\mathbb Z/n\mathbb Z\), where \(n\ge6\). A subset \(S\) is in **general three-position** if no geodesic of length at most three contains three vertices of \(S\). Write \(N_n\) for the number of subsets of maximum possible cardinality, with the cycle vertices distinguished. Then the maximum cardinality is \(\lfloor n/2\rfloor\) and

\[
N_n=\begin{cases}
6,&n\equiv0\pmod4,\\
\dfrac{n(n+3)}4,&n\equiv1\pmod4,\\
2,&n\equiv2\pmod4,\\
\dfrac{n(n+1)}4,&n\equiv3\pmod4.
\end{cases}
\]

The number \(R_n\) of these optimal sets up to cyclic rotation is

\[
R_n=\begin{cases}
2,&n\equiv0\pmod4,\\
1,&n\equiv2\pmod4,\\
\lfloor(n+3)/4\rfloor,&n\text{ odd}.
\end{cases}
\]

In particular, for every odd \(n\ge7\) there are growing numbers of rotation-inequivalent optimal sets, whereas the standard maximally even construction supplies only one rotational class. Both formulas count *all* optimal sets, not only maximally even ones.

## Assumptions and scope

All graphs are finite, simple, undirected, and vertex-labeled by their displayed cyclic coordinates. A geodesic is a shortest path between its endpoints. Distinct sets of labeled vertices count separately even if one is a rotation of another; the separate orbit count identifies rotation-equivalent sets. The condition concerns at most three edges, not unrestricted geodesics. The range \(n\ge6\) ensures that every arc of three consecutive edges of the cycle is a geodesic. No assertion is made for smaller cycles or for longer path-length limits.

## Proof

**1. A cyclic-window criterion and the optimum size.** For \(n\ge6\), a set is in general three-position exactly when each cyclic block of four successive vertices contains at most two selected vertices. Indeed, every such block induces a length-three geodesic, and any shorter geodesic is contained in a length-three block. Summing the \(n\) block inequalities counts every selected vertex four times and yields \(4|S|\le2n\). Conversely, the alternating selection of \(\lfloor n/2\rfloor\) positions, with a double zero at the wrap-around for odd \(n\), satisfies every block condition. Thus the optimum is \(m=\lfloor n/2\rfloor\).

**2. Cyclic gaps.** Fix an optimal \(S\) and order its \(m\) selected positions around the cycle. Let \(g_0,\ldots,g_{m-1}\) be the positive cyclic distances from one selected vertex to the next, so that \(\sum_i g_i=n\). The block criterion is equivalent to

\[
g_i+g_{i+1}\ge4\qquad(i\in\mathbb Z/m\mathbb Z).
\]

Set \(h_i=g_i-2\ge-1\) and \(s_i=h_i+h_{i+1}\ge0\). Then

\[
\sum_i h_i=n-2m,\qquad \sum_i s_i=2(n-2m).
\]

For each valid cyclic gap tuple, there are \(n\) choices of a named starting selected vertex; each resulting labeled set is represented exactly \(m\) times. Hence

\[
N_n=\frac{n}{m}\,\#\{\text{valid ordered cyclic gap tuples}\}.
\]

This identity remains valid for cyclic-periodic gap tuples: the double count is of pairs consisting of a labeled set and a distinguished selected starting vertex.

**3. Even cycle order.** If \(n\) is even, then \(\sum_i s_i=0\), so every \(s_i=0\) and \(h_{i+1}=-h_i\). When \(m\) is odd, cyclic consistency forces \(h_i=0\) for every \(i\), giving one gap tuple. When \(m\) is even, all gap tuples have alternating values \(h_i=a,-a\), and positivity of the gaps is exactly \(a\in\{-1,0,1\}\), giving three tuples. Since \(n/m=2\), this yields respectively \(N_n=2\) for \(n\equiv2\pmod4\) and \(N_n=6\) for \(n\equiv0\pmod4\).

**4. Odd cycle order, odd number of selected vertices.** Now \(n=2m+1\) and \(\sum_i s_i=2\). If \(m\) is odd, the cyclic linear system \(h_i+h_{i+1}=s_i\) has the unique solution

\[
2h_i=s_i-s_{i+1}+s_{i+2}-\cdots+s_{i+m-1}.
\]

Since the nonnegative integer entries of \(s\) sum to two, the alternating sum is even and lies between minus two and two. Thus every such \(s\) yields integral \(h_i\in\{-1,0,1\}\), hence positive gaps. Conversely each feasible gap tuple produces one such \(s\). There are \(m\) placements of a single entry two, and \(\binom m2\) placements of two entries one. Therefore the number of gap tuples is \(m(m+1)/2\), giving \(N_n=n(m+1)/2=n(n+1)/4\) when \(n\equiv3\pmod4\).

**5. Odd cycle order, even number of selected vertices.** Let \(m\ge4\) be even. Since the \(m/2\) equations \(s_i=h_i+h_{i+1}\) over the even positions partition the \(m\) entries of \(h\), and the odd equations also partition them, both parity sums of \(s\) equal \(\sum h_i=1\). Hence \(s\) has exactly one unit at an even index and exactly one unit at an odd index, all other entries zero. There are \(m^2/4\) possible unordered pairs of occupied indices, exactly \(m\) of which are adjacent on the cyclic index graph.

For completeness, fix an occupied index at zero and the other at an odd index \(r\in\{1,3,\ldots,m-1\}\). All solutions of \(h_i+h_{i+1}=s_i\), before imposing positivity, are determined by \(h_0=a\) and have the explicit form

\[
h_t=\begin{cases}
a,&t=0,\\
1-a,&1\le t\le r,\ t\text{ odd},\\
a-1,&2\le t\le r,\ t\text{ even},\\
a,&r+1\le t<m,\ t\text{ even},\\
-a,&r+1\le t<m,\ t\text{ odd}.
\end{cases}
\]

The wrap-around equation holds because \(m\) is even and \(r\) is odd. The condition \(h_t\ge-1\) for every index gives exactly three integer values of \(a\) when \(r=1\) (namely \(-1,0,1\)), exactly three when \(r=m-1\) (namely \(0,1,2\)), and exactly two when \(3\le r\le m-3\) (namely \(0,1\)). Consequently the total number of gap tuples is

\[
3m+2\left(\frac{m^2}{4}-m\right)=\frac{m^2}{2}+m.
\]

Multiplying by \(n/m\) gives \(N_n=n(m+2)/2=n(n+3)/4\) when \(n\equiv1\pmod4\). Together with the preceding cases this proves the first formula.

**6. Rotation classes.** If \(n\) is odd, \(\gcd(n,m)=\gcd(2m+1,m)=1\). A selected subset fixed by a nontrivial rotation would be a union of equal-size rotational cycles, so its cardinality would share a nontrivial divisor with \(n\), impossible. Every optimal set therefore has an orbit of size \(n\), giving \(R_n=N_n/n=\lfloor(n+3)/4\rfloor\). For even \(n\), the gap classification above gives either only the alternating pattern (one orbit) or both the alternating pattern and the recurring \(1,3\)-gap pattern (two orbits), proving the second formula.

## Verification

A standalone standard-library Python program, `verify.py`, tests the original shortest-path condition independently of cyclic windows for all candidate optimum-size sets on cycles through order \(15\). It separately exhausts all candidate optimum-size subsets for orders \(6\) through \(23\), checks rotation classes through order \(18\), and counts optimum-size configurations using a separate closed-walk eight-state transfer method through order \(120\).

The execution produced: `VERIFICATION_OK orders=6..23 candidate_subsets=2786632 direct_distance_cases=13472 orbit_orders=6..18 transfer_orders=6..120`.

These finite tests are not a substitute for the unrestricted arguments in the Proof section. The explicit four-step gap recurrences and parity cases are the essential infinite proof.

## Relationship to prior work

Klavžar, Rall, and Yero introduced general distance-limited position sets and determined their maximum cardinalities on cycles; they also gave a structural characterization for arbitrary graphs (arXiv:2005.08095, first public 2020-05-16). Cody and Moore extended the problem to general multiplicities of selected vertices on short geodesics and proved that maximally even subsets attain the maximum size on cycles (arXiv:2409.05644, first public 2024-09-09). Bushaw, Cody, Freeman, and Whitaker studied maximal evenness and energy optimization on graph cycles (arXiv:2407.18768, first public 2024-07-26).

The scalar maximum \(\lfloor n/2\rfloor\) is not claimed as new. Nor is the existence or construction of maximally even optimal sets. The added result is the closed count and rotation-orbit classification of *all* optimal sets for this geodesic restriction, including non-maximally-even ones. These counts do not follow simply by counting maximally even rotations. Published general structural characterizations supply membership tests, but do not state the displayed mod-four census.

## Limitations

Only cycles of order \(n\ge6\) with the stated length-three geodesic threshold are covered. The theorem does not enumerate suboptimal feasible sets or other length thresholds. While targeted source comparisons found no explicit matching census, classical constrained-circular-word enumerations may express an equivalent result under different terminology. Full independent mathematical and bibliographic review has not been performed.

## References

1. S. Klavžar, D. F. Rall, and I. G. Yero, *General d-position sets*, arXiv:2005.08095 (first public 2020-05-16), Ars Mathematica Contemporanea 21 (2021), article P1.03. https://arxiv.org/abs/2005.08095
2. B. Cody and G. Moore, *The k-general d-position problem for graphs*, arXiv:2409.05644 (first public 2024-09-09). https://arxiv.org/abs/2409.05644
3. N. Bushaw, B. Cody, L. Freeman, and T. Whitaker, *The Music and Mathematics of Maximal Evenness in Graphs*, arXiv:2407.18768 (first public 2024-07-26). https://arxiv.org/abs/2407.18768
