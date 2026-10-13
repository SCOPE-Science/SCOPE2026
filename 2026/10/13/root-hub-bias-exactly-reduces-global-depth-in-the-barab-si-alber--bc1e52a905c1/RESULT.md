# Root-hub bias exactly reduces global depth in the Barabási–Albert tree

## Finding

Consider the standard Barabási–Albert preferential-attachment tree \(T_n\) started from the single edge on vertices \(1,2\). When the tree has \(n\ge2\) vertices, vertex \(n+1\) attaches to an existing vertex with probability proportional to its current degree.

Root the tree at vertex \(1\). Let
\[
R_n=\deg_{T_n}(1)
\]
be the root degree, and let
\[
P_n=\sum_{v=1}^n d(v)
\]
be the total root-to-vertex path length, where \(d(v)\) is the graph distance from the root. Write
\[
H_m=\sum_{j=1}^m\frac1j,
\qquad H_0=0.
\]

For every \(n\ge3\),
\[
\boxed{
\operatorname{Cov}(R_n,P_n)
=
-\mathbb E R_n\,B_n,
}
\tag{1}
\]
where
\[
\mathbb E R_n
=
\frac{2\Gamma(n-\tfrac12)}
{\sqrt{\pi}\,\Gamma(n-1)}
\tag{2}
\]
and
\[
\boxed{
B_n
=
\frac{2n-1}{2}
\bigl(1+H_{n-2}-H_{2n-3}\bigr)
-\frac14H_{n-2}.
}
\tag{3}
\]

The same quantity has the manifestly positive representation
\[
\boxed{
B_n
=
\frac{2n-1}{2}
\sum_{k=2}^{n-1}
\frac{H_{k-1}}{(2k-1)(2k+1)}
>0.
}
\tag{4}
\]
Thus
\[
\operatorname{Cov}(R_n,P_n)<0
\qquad(n\ge3).
\]

There is also a direct size-bias interpretation. Define the root-degree-biased law by
\[
\mathbb P_n^\star(A)
=
\frac{\mathbb E\!\left[R_n\mathbf1_A\right]}
{\mathbb E R_n}.
\]
Then
\[
\boxed{
\mathbb E_n^\star P_n-\mathbb E P_n
=
-B_n.
}
\tag{5}
\]
So favoring trees in proportion to the size of the root hub reduces expected global root depth by exactly \(B_n\).

The ordinary mean path length is
\[
\mathbb E P_n
=
\frac{n-1}{2}\bigl(H_{n-1}+1\bigr).
\tag{6}
\]

Finally,
\[
B_n\sim(1-\log2)n
\tag{7}
\]
and
\[
\boxed{
\operatorname{Cov}(R_n,P_n)
\sim
-\frac{2(1-\log2)}{\sqrt{\pi}}\,
n^{3/2}.
}
\tag{8}
\]

Thus the early hub and global depth are not merely negatively related: root-degree size bias produces a linear asymptotic reduction
\[
(1-\log2)n
\]
in expected total depth.

## Assumptions and scope

The initial tree is the single edge joining vertices \(1\) and \(2\). The root is vertex \(1\). At every step, the attachment probability of an existing vertex \(v\) is
\[
\frac{\deg(v)}{2(n-1)}
\]
when the current tree has \(n\) vertices.

The result is exact for this linear preferential-attachment model. It is not asserted for affine attachment with nonzero offset, different seeds, multiple attachments per new vertex, or for total pairwise path length.

Equation (1) is a mixed finite-size identity. Equation (8) is a consequence of (1), the standard gamma-ratio asymptotic, and the harmonic-number limit in (3).

## Proof

Grow \(T_n\) to \(T_{n+1}\). Let \(V_n\) be the chosen parent, let
\[
A_n=\mathbf1\{V_n=1\},
\]
and let
\[
D_n=d(V_n).
\]

The two statistics evolve as
\[
R_{n+1}=R_n+A_n
\tag{9}
\]
and
\[
P_{n+1}=P_n+D_n+1.
\tag{10}
\]

Conditional on \(T_n\),
\[
\mathbb E[A_n\mid T_n]
=
\frac{R_n}{2(n-1)}.
\tag{11}
\]

A deterministic tree identity supplies the crucial depth average:
\[
\sum_{v=1}^n\deg(v)d(v)
=
2P_n-(n-1).
\tag{12}
\]
Indeed, summing \(d(\text{parent})+d(\text{child})\) over all edges gives \(P_n-(n-1)+P_n\). Hence
\[
\mathbb E[D_n\mid T_n]
=
\frac{P_n}{n-1}-\frac12.
\tag{13}
\]

Since the root has depth zero,
\[
A_nD_n=0
\tag{14}
\]
identically.

Put
\[
m_n=\mathbb E R_n,
\qquad
p_n=\mathbb E P_n,
\qquad
c_n=\operatorname{Cov}(R_n,P_n).
\]

Taking expectations in (9) gives
\[
m_{n+1}
=
m_n\left(1+\frac1{2(n-1)}\right),
\qquad
m_2=1,
\]
which solves to (2).

Taking expectations in (10) and using (13) gives
\[
p_{n+1}
=
\frac n{n-1}p_n+\frac12,
\qquad
p_2=1.
\]
After division by \(n\), this telescopes to (6). In particular,
\[
\mathbb E D_n
=
\frac12H_{n-1}.
\tag{15}
\]

Now expand the covariance in (9)--(10). Equations (11)--(13) give
\[
\operatorname{Cov}(R_n,D_n)
=
\frac{c_n}{n-1},
\tag{16}
\]
and
\[
\operatorname{Cov}(A_n,P_n)
=
\frac{c_n}{2(n-1)}.
\tag{17}
\]
By (14)--(15),
\[
\operatorname{Cov}(A_n,D_n)
=
-\frac{m_nH_{n-1}}{4(n-1)}.
\tag{18}
\]

Therefore
\[
c_{n+1}
=
\left(1+\frac{3}{2(n-1)}\right)c_n
-
\frac{m_nH_{n-1}}{4(n-1)},
\qquad
c_2=0.
\tag{19}
\]

Normalize by the root-degree mean:
\[
d_n=\frac{c_n}{m_n}.
\]
Using the recurrence for \(m_n\), equation (19) becomes
\[
d_{n+1}
=
\frac{2n+1}{2n-1}d_n
-
\frac{H_{n-1}}{2(2n-1)}.
\tag{20}
\]
Consequently
\[
\frac{d_{n+1}}{2n+1}
=
\frac{d_n}{2n-1}
-
\frac{H_{n-1}}{2(2n-1)(2n+1)}.
\tag{21}
\]

Since \(d_2=0\), telescoping yields
\[
d_n
=
-\frac{2n-1}{2}
\sum_{k=2}^{n-1}
\frac{H_{k-1}}{(2k-1)(2k+1)}.
\tag{22}
\]
This proves (1) and (4).

For the closed form, use
\[
\frac1{(2k-1)(2k+1)}
=
\frac12
\left(
\frac1{2k-1}-\frac1{2k+1}
\right)
\]
and summation by parts to obtain
\[
\sum_{k=2}^{n-1}
\frac{H_{k-1}}{(2k-1)(2k+1)}
=
1+H_{n-2}-H_{2n-3}
-\frac{H_{n-2}}{2(2n-1)}.
\tag{23}
\]
Equations (22)--(23) give (3).

Equation (5) is simply the defining identity for size bias:
\[
\mathbb E_n^\star P_n
=
\frac{\mathbb E[R_nP_n]}{\mathbb E R_n}.
\]

Finally,
\[
H_{n-2}-H_{2n-3}\longrightarrow-\log2,
\]
so (3) gives (7). Also,
\[
\frac{\Gamma(n-\tfrac12)}{\Gamma(n-1)}
\sim n^{1/2},
\]
and (2) together with (1) gives (8).

## Verification

The accompanying exact checker enumerates every preferential-attachment parent history through \(n=9\). Each history is weighted by its exact rational attachment probability, not counted uniformly.

Across
\[
\sum_{m=1}^{8}m!=46233
\]
weighted histories, the checker recomputes depths and degrees directly and verifies the exact formulas for \(\mathbb E R_n\), \(\mathbb E P_n\), and \(\operatorname{Cov}(R_n,P_n)\).

It also checks the covariance recurrence (19), the normalized telescoping recurrence (20), and the equivalence of the positive-sum and harmonic closed forms through \(n=300\) using exact rational arithmetic.

These finite checks are supplementary. The all-\(n\) result follows from the deterministic identity (12) and the conditional recurrences above.

## Relationship to prior work

Móri studied the maximum degree in the Barabási–Albert random tree and related one-parameter preferential-attachment trees. That work supplies archive-era degree-side context, but its stated object is the maximal degree rather than a mixed root-degree/path-length law.

Feng and Hu studied topological indices of scale-free trees in the same linear preferential-attachment setting. Their full paper explicitly notes that large-degree vertices shorten average path length and proposes the Zagreb index as a bridge between degree distribution and the small-world property. The paper develops Zagreb and Randić indices and average-path-length motivation, but targeted full-text inspection found no covariance statement connecting root degree to total root-to-vertex path length.

Katona studied levels of the Barabási–Albert tree and the degree distribution on sufficiently high levels. That level-profile perspective is related to depth, but the accessible statement does not give the finite mixed identity (1) or the root-degree size-bias shift (5).

The present result gives a direct finite quantitative bridge between a distinguished early hub and a canonical global depth functional. Its exact size-bias form makes the hub-versus-depth relation operational rather than only qualitative.

## Limitations

The statistic \(P_n\) is total depth from the distinguished root, not average pairwise path length. Therefore the result should not be read as an exact formula for the average-path-length statistic discussed in small-world studies.

The initial edge and zero-offset linear attachment rule are part of the theorem. Different seeds or affine attachment rules change the conditional recurrences.

Negative covariance does not imply a full stochastic ordering or negative association between root degree and path length.

Preferential-attachment literature is extensive. The strongest same-model full source treating degree/path-length interaction was inspected in full, but an equivalent older formula under different terminology remains a residual bibliographic risk.

## References

1. T. F. Móri, “The Maximum Degree of the Barabási–Albert Random Tree,” *Combinatorics, Probability and Computing* 14 (2005), 339–348, DOI 10.1017/S0963548304006133. Published online 2005-04-11.
2. Q. Feng and Z. Hu, “Phase Changes in the Topological Indices of Scale-Free Trees,” *Journal of Applied Probability* 50 (2013), 516–532, DOI 10.1239/jap/1371648958. Primary MSC \(60C05\) among the paper's primary classifications.
3. Z. Katona, “Levels of a scale-free tree,” *Random Structures & Algorithms* 29 (2006), 194–207, DOI 10.1002/rsa.20106. First published 2005-12-27.
