# Two-step three-cycle collapse in multipartite cyclic competition

## Finding
Let \(r\ge3\), let \(n_1,\ldots,n_r\ge1\), and let \(G=K_{n_1,\ldots,n_r}\) be the loopless, labelled complete multipartite graph. Consider the synchronous three-color cyclic cellular automaton \(F\): each vertex of color \(i\in\mathbb Z/3\mathbb Z\) moves to \(i+1\) if and only if a neighbor currently has color \(i+1\), and otherwise stays at \(i\).

**Theorem.** Every trajectory enters a fixed point or a primitive three-cycle within at most two steps; equivalently \(F^5=F^2\). Exactly three configurations are fixed, namely the three global monochromatic configurations. Every other periodic configuration advances **every vertex** by one color at each update, so has exact period three. The bound of two is sharp if some part contains at least two vertices; when every part is a singleton, the sharp bound is one.

For each nonempty \(S\subseteq\mathbb Z/3\mathbb Z\) put
\[
U_{|S|}(n)=\sum_{j=0}^{|S|}(-1)^j\binom{|S|}{j}(|S|-j)^n.
\]
Let \(\chi(S_1,\ldots,S_r)=1\) precisely when, for every part \(i\) and every \(c\in S_i\), there exists \(j\ne i\) with \(c+1\pmod3\in S_j\). Then the exact number of **labelled periodic configurations**, for all part sizes, is
\[
R(n_1,\ldots,n_r)=3+\sum_{S_1,\ldots,S_r\ne\varnothing}\chi(S_1,\ldots,S_r)\prod_{i=1}^r U_{|S_i|}(n_i).
\]
Thus the number of distinct primitive three-cycles is \((R-3)/3\), and the dynamical zeta function is
\[
\zeta_F(z)=(1-z)^{-3}(1-z^3)^{-(R-3)/3}.
\]

In particular, adding a **third nonempty part** eliminates the primitive period-four phenomenon that can occur in the three-color cyclic automaton on complete bipartite graphs. The conclusion holds uniformly for arbitrarily many additional parts and vertices.

## Assumptions and scope
All graph parts are nonempty, the graph has no edges within a part, and all edges across different parts are present. The alphabet is exactly \(\{0,1,2\}\), with cyclic successor addition modulo three. Updates are simultaneous, deterministic, and threshold one. Counts refer to labelled vertices, without quotienting graph automorphisms or color rotations. Nothing is claimed for two graph parts or for a larger alphabet.

## Proof
**Part supports and their exact factor.** Denote by \(S_i\subseteq\{0,1,2\}\) the nonempty support of colors present in part \(i\). For any color \(c\in S_i\), its vertices advance if and only if the successor of \(c\) belongs to \(\bigcup_{j\ne i}S_j\). Hence the evolution of the support tuple is deterministic and depends only on the supports, not on the part sizes or multiplicities of vertices within each color class.

There are seven possible nonempty color supports. Let \(m_A\) be the number of parts whose support is \(A\), and define the saturated signature \(p_A=\min(2,m_A)\in\{0,1,2\}\). For deciding whether the successor of a color is present in a different part, it suffices to know if that color occurs in zero, one, or at least two parts, and, in the one-part case, whether the current part itself contains it. Consequently the signature has an **exact deterministic induced update** \(T\): each occupied support type is mapped by the foregoing successor test and the multiplicity of each target support is again saturated at two.

The signatures realizable by at least three nonempty parts are precisely the vectors in \(\{0,1,2\}^7\) for which either the coordinate sum is at least three, or the only nonzero coordinate equals two. There are exactly \(2158\) such signatures. The supplied standalone checker enumerates these \(2158\) possibilities and computes \(T\) with integer and bit operations. The complete finite certificate verifies, for **every** such signature \(p\):

1. The signature \(T^2p\) is either a monochromatic signature or satisfies the all-advancing condition below.
2. If \(q=T^2p\), then \(T^3q=q\).
3. A signature is periodic precisely when it is monochromatic or all-advancing; the latter property is preserved by successor rotation.

This is an exhaustive verification of a size-independent finite quotient, **not** an inference from testing a finite number of graph sizes. The precise transition and exhaustive assertions are given in `verify.py` and the results are in `verification_output.txt`.

**Lifting from supports to labelled configurations.** Call a support tuple all-advancing if every color present in every part has its successor present in some other part; this is exactly the condition \(\chi=1\). If a support tuple is all-advancing, every labelled vertex advances in unison at every update. Since a simultaneous global rotation preserves the all-advancing condition, such a configuration is of exact period three. A monochromatic configuration is fixed. The complete quotient check proves that after two graph updates either condition holds, giving \(F^5=F^2\), and also that no additional periodic states exist.

**Enumeration.** For any prescribed nonempty support \(S_i\), inclusion-exclusion counts assignments of \(n_i\) labelled vertices realizing precisely those \(|S_i|\) colors as \(U_{|S_i|}(n_i)\). Multiply over parts and sum over all-advancing support tuples. The three monochromatic configurations are disjoint from this set. This gives the formula for \(R\), its period-three orbit count, and the zeta function.

**Sharpness.** If all graph parts are singletons, the graph is complete: a state containing all three colors rotates immediately, a monochromatic state is fixed, and any state with exactly two colors becomes monochromatic after one update. Thus the maximum first periodic-entry time is one. Otherwise select one part with at least two vertices, place at least one vertex in each of colors zero and one there, color any remaining vertices in that part zero, and color all other parts zero. After one step all other parts are entirely color one while the selected part still has both colors; after two steps all vertices are color one. The first periodic-entry time is exactly two.

## Verification
Run `python3 verify.py` with Python 3.8 or newer. The output file `verification_output.txt` records the exact signature census: \(2158\) realizable signatures, with first periodic-entry depths zero, one and two numbering \(1972,165,21\) **signature types**, respectively. This is a finite-quotient census, not a census of labelled configurations. Explicit direct support-vector updates were compared with the quotient for all \(7^3+7^4+7^5\) support tuples on three, four and five parts. A separately coded vertex-level update verified \(24246\) labelled configurations on ten representative parameter vectors (including part counts three and four), their complete period-one/period-three classification, and their exact periodic-state counts. The infinity of graph sizes is covered by the quotient proof, not by these labelled tests.

For three parts, setting \(u_i=U_2(n_i)\) and \(v_i=U_3(n_i)\), the general formula specializes to
\[
\begin{aligned}
R={}&9+6\sum_i u_i+9\sum_{i<j}u_i u_j+3\sum_{i\ne j}u_i v_j+3\sum_{i<j}v_i v_j\\
&+15u_1u_2u_3+6\sum_i v_i\prod_{j\ne i}u_j
+3\sum_i u_i\prod_{j\ne i}v_j+v_1v_2v_3.
\end{aligned}
\]
For example, \(R(1,1,1)=9\), \(R(1,1,2)=21\), and \(R(2,2,2)=273\).

## Relationship to prior work
Durrett and Griffeath (1993) study the cyclic and Greenberg–Hastings excitable automata primarily in lattice settings. Gravner, Lyu and Sivakoff (first posted 2016) prove a general finite-graph circulation test for synchronization and an asymptotic activity formula (Theorem 3). Their theorem applies to the present graphs but does not state the sharp global two-step first-entry bound, classify *all* periodic configurations, or give their exact labelled orbit enumeration.

The threshold-one **Greenberg–Hastings** automaton on complete multipartite graphs shares the same all-advancing support sum, but its other states and transient times differ: it has one monochromatic rest fixed point and may require four updates to enter recurrence. Here the three-color **cyclic** automaton has three monochromatic fixed points and a sharp two-step cutoff. The complete bipartite cyclic automaton can instead possess primitive period-four states; no such states survive once there are at least three nonempty parts. These are comparisons between update maps, not claims to have discovered the general circulation criterion or the inclusion-exclusion identity.

## Limitations
The exact finite quotient is specific to a three-color alphabet and complete multipartite graph topology with at least three parts. It does not classify basin sizes for individual periodic orbits or establish analogous results for larger alphabets. Novelty assessment remains bounded by accessible sources and search coverage; a mathematically equivalent unindexed treatment is possible. The 1993 foundational source was accessible in bibliographic form, whereas a material full-text inspection was made of the 2016 general graph theorem.

## References
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first posted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
- J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24; *Annals of Applied Probability* **28** (2018), 3324–3357. https://arxiv.org/abs/1610.07320
