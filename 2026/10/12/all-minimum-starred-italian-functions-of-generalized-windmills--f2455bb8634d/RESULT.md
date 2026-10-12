# All minimum starred Italian functions of generalized windmills
## Finding
Let
\[
W_{m,r}=K_1\vee mK_r
\]
with
\[
m\ge3,\qquad r\ge1.
\]
Write \(c\) for the universal center, and let
\[
B_1,\ldots,B_m
\]
be the \(m\) pairwise anticomplete clique blades, each of order \(r\).

Every minimum starred Italian dominating function \(f\) is obtained by choosing exactly one blade \(B_i\) and setting
\[
f(c)=2,
\]
\[
f(v)=1\qquad(v\in B_i),
\]
and
\[
f(v)=0\qquad(v\notin B_i\cup\{c\}).
\]

Therefore
\[
\gamma_I^*(W_{m,r})=r+2,
\]
and the exact number of minimum functions is
\[
m.
\]

The scalar equality is already implied by the published universal-join theorem for starred Italian domination. The complete optimizer classification and multiplicity are the content established here.

## Assumptions and scope
A starred Italian dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every zero-labeled vertex \(v\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2,
\]
and the zero set
\[
V_0=\{v:f(v)=0\}
\]
is not a dominating set of \(G\).

Equivalently, in addition to the Italian condition, some positive vertex has no zero-labeled neighbor.

The generalized windmill \(W_{m,r}\) consists of one universal center joined to \(m\) disjoint copies of \(K_r\). The theorem assumes \(m\ge3\). The two-blade case has additional minimum-function types and is intentionally excluded.

## Proof
Let \(f\) be a minimum starred Italian dominating function on \(W_{m,r}\).

First, the zero set is nonempty. Indeed, the all-positive labeling has weight at least
\[
1+mr>r+2
\]
when \(m\ge3\), while the construction given below has weight \(r+2\).

Since \(V_0\) is not dominating, there exists a positive vertex having no zero neighbor. The center \(c\) cannot be such a vertex because \(c\) is adjacent to every zero vertex. Hence some outer vertex
\[
x\in B_i
\]
has no zero neighbor.

The neighbors of \(x\) are exactly the center together with the other vertices of \(B_i\). Therefore
\[
f(c)>0
\]
and every vertex of \(B_i\) is positive. This already gives
\[
\omega(f)\ge r+1.
\tag{1}
\]

Equality in (1) is impossible. If the total weight were \(r+1\), then necessarily
\[
f(c)=1
\]
and every vertex of \(B_i\) would have label \(1\), while all remaining blades would be zero. Any zero vertex in another blade would then see total neighboring weight only
\[
f(c)=1,
\]
contradicting the Italian requirement. Thus
\[
\omega(f)\ge r+2.
\tag{2}
\]

Conversely, choose one blade \(B_i\), assign label \(2\) to \(c\), label \(1\) to every vertex of \(B_i\), and label \(0\) on all other blades. Every zero vertex has the center as a neighbor of weight \(2\), so the Italian condition holds. Every vertex of \(B_i\) has no zero neighbor because its neighborhood consists only of \(c\) and the rest of \(B_i\). Thus the zero set is not dominating. Hence
\[
\gamma_I^*(W_{m,r})=r+2.
\]

It remains to classify equality in (2). Suppose
\[
\omega(f)=r+2.
\]
We already know that some blade \(B_i\) is entirely positive and that \(c\) is positive.

Assume first that
\[
f(c)=1.
\]
The center and the positive blade consume at least \(r+1\) units of weight, leaving only one additional unit. At most one further blade can therefore contain a positive label. Because \(m\ge3\), there is another blade \(B_j\) that is entirely zero. A zero vertex of \(B_j\) then receives neighboring weight only \(1\) from the center, again contradicting the Italian condition.

Therefore
\[
f(c)=2.
\]
The remaining weight is exactly \(r\). Since every vertex of \(B_i\) is positive and there are \(r\) such vertices, each must have label \(1\), and every vertex outside \(B_i\cup\{c\}\) must have label \(0\).

Hence the minimum functions are exactly the \(m\) functions obtained by choosing the unique all-positive blade.

## Verification
The included checker constructs \(W_{m,r}\) directly and exhausts every ternary labeling for nine parameter pairs:
\[
(m,r)\in
\{(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)\}.
\]

For every labeling it tests the Italian neighborhood inequality and tests directly that the zero set is not dominating. For every parameter pair it compares the complete minimum-function family with the theorem.

## Relationship to prior work
The foundational paper on starred Italian domination proves the universal-join formula
\[
\gamma_I^*(N_1+G)=
\begin{cases}
\delta(G)+2,&N_{\delta,\gamma}(G)\ne\varnothing,\\
\delta(G)+3,&N_{\delta,\gamma}(G)=\varnothing.
\end{cases}
\]
For
\[
G=mK_r,\qquad m\ge2,
\]
we have
\[
\delta(G)=r-1
\]
and
\[
N_{\delta,\gamma}(G)=\varnothing,
\]
because the closed neighborhood of a vertex is confined to its own clique component. Thus the published theorem already yields
\[
\gamma_I^*(W_{m,r})=r+2.
\]

That scalar equality is therefore not an originality claim here.

The same primary paper gives exact values for paths, cycles, complete bipartite graphs, wheels, joins of two nontrivial graphs, and corona products. Its searchable full text contains no occurrence of “friendship” or “windmill,” and its universal-join theorem determines only the minimum weight in the present family. It does not state which functions attain that weight or how many there are.

The present classification identifies the equality mechanism: for at least three blades, optimum forces center weight \(2\) and forces all remaining positive weight onto one entire blade. This yields exactly \(m\) optima.

## Limitations
The theorem assumes at least three blades. For \(m=2\), additional minimum-function types occur, so the stated rigidity fails.

The result classifies minimum functions only; it does not enumerate all starred Italian dominating functions by weight.

The exhaustive computation is finite corroboration only. The arbitrary-parameter result follows from the proof.

A differently phrased or non-indexed minimum-function classification may exist despite the targeted searches.

## References
1. A. Cabrera Martínez, “Starred Italian domination in graphs,” Contributions to Discrete Mathematics 16(3) (2021), 139–152, DOI 10.55016/ojs/cdm.v16i3.71109; article page dated 31 December 2021.
