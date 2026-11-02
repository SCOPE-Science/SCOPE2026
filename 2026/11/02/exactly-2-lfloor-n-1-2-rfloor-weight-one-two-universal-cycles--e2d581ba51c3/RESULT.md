# Exactly \(2^{\lfloor(n-1)/2\rfloor}\) weight-one/two universal cycles

## Finding
For every integer \(n\ge 2\), the set of binary cyclic words whose length-\(n\) cyclic windows each occur once and are precisely the binary words of Hamming weight one or two has cardinality
\[
N_n=2^{\lfloor(n-1)/2\rfloor}.
\]
Words are identified only under cyclic rotation of *the entire word*, not under reversal, letter interchange, or arbitrary permutation of the windows. Each counted word has length \(\binom{n+1}{2}\) and necessarily has primitive period of that length. Equivalently, the first nontrivial two-adjacent-weight shorthand universal cycles for subsets have exactly this many cyclic realizations.

## Assumptions and scope
Fix \(n\in\mathbb Z\) with \(n\ge2\), and put \(m=n-1\). Denote by \(w(x)\) the number of ones in a binary word \(x\). Define \(G_n\) to have as vertices the binary words of length \(m\) with weights zero, one or two. Each length-\(n\) word \(a_1\ldots a_n\) of weight one or two labels a **distinct directed edge** from \(a_1\ldots a_m\) to \(a_2\ldots a_n\). The all-zero vertex is the root \(z=0^m\). A rooted directed in-arborescence is a spanning selection of one outgoing edge at every nonroot vertex, and none at the root, with a unique directed path from every vertex to the root.

Vertices of weights zero and two have in- and out-degree one. Vertices of weight one have in- and out-degree two. For the (possibly parallel) directed edges, distinct length-\(n\) labels remain distinguished. There are precisely \(\binom n1+\binom n2=\binom{n+1}{2}\) edges.

## Proof
**1. Reduce Euler tours to in-arborescences.** Each cyclic word described above lists every directed edge of \(G_n\) exactly once in a consistent order, hence corresponds bijectively to an Euler circuit considered up to cyclic shift of its edge labels. Conversely any Euler circuit gives a word with the required exact window set. The edge \(e_0=0^m1\) is unique and leaves the root \(z\), whose out-degree is one; it therefore provides a canonical first edge in each cyclic circuit. By the directed BEST enumeration formula, the number of circuits beginning with this fixed edge is
\[
\tau_z(G_n)\prod_{v\in V(G_n)}(\deg^+(v)-1)!=\tau_z(G_n),
\]
provided the graph is Eulerian, where \(\tau_z(G_n)\) counts in-arborescences rooted at \(z\). The product is one since every out-degree is at most two. An explicit in-arborescence is constructed in step 3. The graph is balanced; a balanced finite digraph with every vertex able to reach \(z\) is strongly connected, so Eulerian existence and the BEST formula apply.

**2. Forced states and an index reduction.** Every weight-two vertex has only one outgoing edge, namely the edge appending zero. Successive forced zero-appends eventually remove one of its ones and reach a weight-one state. Thus the choice of an in-arborescence amounts exactly to choosing one of the two outgoing edges at each weight-one vertex and forbidding cycles in the resulting functional digraph. Index weight-one states by \(i\in\{0,1,\ldots,m-1\}\), where state \(i\) has its sole one at the bit position \(i\) from the right. Following an outgoing edge appending zero gives the reduced transition \(i\to i+1\) for \(i<m-1\), and \(m-1\to z\). Following the edge appending one and then all forced weight-two transitions gives the reduced transition \(i\to m-1-i\) for all indices, including \(i=m-1\) (where this is an immediate transition). These two choices are different labeled original edges, even if their reduced targets coincide.

**3. Classify all valid choices.** Suppose a vertex with index \(i\ge(m-1)/2\) chose the append-one edge. Consider the nonempty index interval \(I_i=\{m-1-i,m-i,\ldots,i\}\). Every reduced append-one transition from \(I_i\) stays inside \(I_i\), and every append-zero transition does too, except at the upper endpoint \(i\), whose append-one choice has already been fixed. In particular, even for \(i=m-1\), the append-zero transition to \(z\) is unavailable because index \(i\) chooses append one. Thus \(I_i\) is forward-closed and disjoint from the root, contradicting the required path to \(z\). All such upper-half indices must choose append zero.

For every index \(i<(m-1)/2\), both possible reduced destinations strictly exceed \(i\): they are \(i+1\) and \(m-1-i\). At all other indices the forced append-zero transition increases the index, except at \(m-1\) where it reaches the root. Consequently **any** independent choices at the lower-half indices produce paths with strictly increasing indices, which all terminate at the root. This yields an in-arborescence. There are exactly
\[
\#\{i\in\{0,\ldots,m-1\}:i<(m-1)/2\}=\lfloor m/2\rfloor
\]
such free indices, and two different selections give distinct arborescences. Therefore \(\tau_z(G_n)=2^{\lfloor m/2\rfloor}\). Substituting \(m=n-1\) in step 1 proves the formula for every \(n\ge2\).

**4. Rotation normalization and primitivity.** Every edge label is used exactly once, in particular the edge label \(0^m1\) occurs at exactly one cyclic window position. This distinguishes a unique rotation of each counted cyclic word and precludes any proper rotational period. Hence no further division by the word length occurs, including when \(n=2\).

## Verification
Two standalone pure-Python verification programs are included. Running `python3 verify_euler.py` independently enumerates all edge-distinct Euler circuits with the unique root edge fixed and checks counts for \(2\le n\le11\). Running `python3 verify_trees.py` builds the directed Laplacian and checks its root cofactor using exact integer fraction-free elimination for the same lengths. Outputs are stored in `verify_euler_output.txt` and `verify_trees_output.txt`. Their checks are finite corroboration; the all-\(n\) conclusion follows from the proof above.

## Relationship to prior work
Ruskey, Sawada and Williams (2012) proved existence and developed a constructive algorithm for binary fixed-weight shorthand de Bruijn sequences, a formulation equivalent to the present two-consecutive-weight case. Sawada, Williams and Wong (2013) constructed weight-range universal cycles efficiently. Sawada and Gabrić (2025) studied uniform random generation via Eulerian arborescences. Mitchell and Wild (first public version 2026-07-24) extended weight-constrained existence to other alphabets and weight functions. The distinguishing claim here is the **closed-form total number** of cyclic sequences for weights one and two at every span, obtained by fully classifying the arborescences, not merely their existence or efficient construction. The enumeration is not asserted for other weight pairs or nonbinary alphabets.

## Limitations
Equivalence excludes reversal and complementation. The result covers only binary words and the adjacent weight pair one/two. The exact enumeration could also occur implicitly in earlier work on shorthand universal cycles or spanning-tree cofactors; this is a residual priority risk, not a mathematical limitation of the proof. No claim is made about algorithms for other weight intervals, or about independently audited publication priority.

## References
1. F. Ruskey, J. Sawada and A. Williams, “De Bruijn Sequences for Fixed-Weight Binary Strings”, *SIAM Journal on Discrete Mathematics* 26(2) (2012), 605–617. https://doi.org/10.1137/100808782
2. J. Sawada, A. Williams and D. Wong, “Universal Cycles for Weight-Range Binary Strings” (2013), https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf
3. J. Sawada and D. Gabrić, “Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random” (2025), https://arxiv.org/abs/2510.16545
4. C. J. Mitchell and P. R. Wild, “Weight-Constrained Cut-Down de Bruijn Sequences”, first public version 2026-07-24, https://arxiv.org/abs/2607.22350
5. The BEST theorem for directed Euler-circuit counting and the directed matrix-tree theorem; classical graph-theoretic results.
