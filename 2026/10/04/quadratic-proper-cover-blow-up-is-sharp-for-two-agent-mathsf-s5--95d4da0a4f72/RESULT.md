# Quadratic proper-cover blow-up is sharp for two-agent \(\mathsf{S5}\)
## Finding

Let
\[
K_m=(W,R_1,R_2)
\]
be the two-agent \(\mathsf{S5}\) frame on
\[
|W|=m\ge1
\]
with
\[
R_1=R_2=W\times W.
\]

A two-agent frame
\[
\widetilde F=(\widetilde W,\widetilde R_1,\widetilde R_2)
\]
is **proper** when no two distinct worlds are related by both agents:
\[
x\ne y
\quad\Longrightarrow\quad
\neg(x\widetilde R_1y\ \text{and}\ x\widetilde R_2y).
\]
Assume \(\widetilde R_1,\widetilde R_2\) are equivalence relations and that there is a surjective bounded morphism
\[
\pi:\widetilde F\to K_m.
\]

Then
\[
|\widetilde W|\ge m^2.
\]
This lower bound is attained by the quadratic construction of Bjorndahl and Sink, so the exact minimum size is
\[
\boxed{m^2}.
\]

The equality case is rigid. If
\[
|\widetilde W|=m^2,
\]
then:

- each \(\widetilde R_1\)-class has exactly \(m\) worlds;
- each \(\widetilde R_2\)-class has exactly \(m\) worlds;
- there are exactly \(m\) classes for each relation;
- every \(\widetilde R_1\)-class meets every \(\widetilde R_2\)-class in exactly one world;
- the restriction of \(\pi\) to every relation class is a bijection onto \(W\).

After naming the \(\widetilde R_1\)-classes as rows and the \(\widetilde R_2\)-classes as columns, the array
\[
L(r,c)=\pi(r\cap c)
\]
is a Latin square of order \(m\): each target world occurs exactly once in each row and exactly once in each column.

Conversely, every Latin square \(L\) of order \(m\) gives an optimal proper cover. Take the cells of \(L\) as worlds, let the first agent identify cells in the same row, let the second identify cells in the same column, and map each cell to its symbol. The row and column relations are \(\mathsf{S5}\) equivalence relations, their common intersections are singletons, and each row and column maps bijectively onto \(W\). Hence the symbol map is a surjective bounded morphism onto \(K_m\).

Thus optimal proper covers of the complete two-agent \(\mathsf{S5}\) frame are exactly Latin-square grids after the relation classes are named.

## Assumptions and scope

The target has exactly two agents and both target accessibility relations are universal. The cover is required to remain an \(\mathsf{S5}\) frame, so its accessibility relations are equivalence relations, and the comparison map is a surjective bounded morphism.

The two-agent restriction is substantive. Properness forbids two distinct worlds from lying simultaneously in both equivalence classes, so pairwise class intersections are singletons or empty. With three or more agents, properness constrains the intersection of all agent classes rather than every pair, and the same quadratic lower-bound argument does not apply unchanged.

Valuations play no role in the frame-size lower bound. For models, any valuation on \(K_m\) can be pulled back along the bounded morphism, exactly as in the source construction.

## Proof

Fix any
\[
x\in\widetilde W.
\]
Because \(K_m\) has universal \(R_i\), the back condition for the bounded morphism says that for every target world
\[
w\in W
\]
and every agent \(i\in\{1,2\}\), there exists
\[
y\in\widetilde W
\]
such that
\[
x\widetilde R_i y
\qquad\text{and}\qquad
\pi(y)=w.
\]
Therefore every equivalence class
\[
[x]_i
\]
maps surjectively onto \(W\). In particular,
\[
|[x]_i|\ge m.
\]

Now fix one \(\widetilde R_1\)-class \(C\). Any two distinct points of \(C\) must lie in different \(\widetilde R_2\)-classes. Indeed, if distinct \(y,z\in C\) belonged to the same \(\widetilde R_2\)-class, then
\[
y\widetilde R_1z
\qquad\text{and}\qquad
y\widetilde R_2z,
\]
contradicting properness.

Since
\[
|C|\ge m,
\]
there are at least \(m\) distinct \(\widetilde R_2\)-classes. Every one of those classes has at least \(m\) elements by the bounded-morphism back condition. Equivalence classes are disjoint, hence
\[
|\widetilde W|\ge m\cdot m=m^2.
\]

Bjorndahl and Sink construct a proper cover with underlying set
\[
W\times W,
\]
hence with exactly \(m^2\) worlds, and prove that projection to the first coordinate is a surjective bounded morphism. When the target relations are equivalence relations, their construction preserves this property. Therefore the lower bound is sharp.

Now assume equality:
\[
|\widetilde W|=m^2.
\]
The preceding proof then forces the number of \(\widetilde R_2\)-classes to be exactly \(m\), and each such class must have exactly \(m\) points. Every \(\widetilde R_1\)-class meets each \(\widetilde R_2\)-class in at most one point, so its size is at most \(m\); the back condition gives the opposite inequality. Hence every \(\widetilde R_1\)-class also has exactly \(m\) points. There are therefore exactly \(m\) classes for each relation.

An \(\widetilde R_1\)-class has \(m\) points distributed among \(m\) \(\widetilde R_2\)-classes, with at most one point in each, so it meets every \(\widetilde R_2\)-class exactly once. The same statement is symmetric.

Each relation class maps surjectively to the \(m\)-element target and itself has \(m\) elements, so the restriction of \(\pi\) to each class is bijective. Consequently, after naming the first-agent classes as rows and the second-agent classes as columns, the unique point at their intersection carries one target label, and every target label occurs once in every row and column. This is precisely a Latin square.

For the converse, start from a Latin square \(L\) with row set \(R\), column set \(C\), and symbol set \(W\), all of size \(m\). Put
\[
\widetilde W=R\times C.
\]
Define
\[
(r,c)\widetilde R_1(r',c')
\quad\Longleftrightarrow\quad
r=r',
\]
and
\[
(r,c)\widetilde R_2(r',c')
\quad\Longleftrightarrow\quad
c=c'.
\]
The frame is proper because a common row and common column determine one cell. Define
\[
\pi(r,c)=L(r,c).
\]
Every row and column of a Latin square contains every symbol exactly once, so the back condition holds for both universal target relations; the forth condition is automatic because those target relations are universal. Thus \(\pi\) is a surjective bounded morphism and the cover has \(m^2\) worlds.

## Verification

The proof is exact and does not depend on finite experimentation.

The bundled checker performs three consistency tests.

First, for \(1\le m\le12\), it constructs the cyclic Latin-square cover, verifies properness, checks that both accessibility relations are equivalence relations, and checks the bounded-morphism forth and back conditions onto the complete \(m\)-world two-agent frame.

Second, for \(m=2,3\), it exhaustively generates set partitions of carriers of every size below \(m^2\). It verifies that no pair of equivalence partitions can simultaneously have all blocks of size at least \(m\) and pairwise block intersections of size at most one. These are the two combinatorial consequences forced respectively by the bounded-morphism back condition and properness.

Third, at the equality size \(m^2\) for \(m=2,3\), it checks the grid consequences for every admissible pair of partitions: both partitions have \(m\) blocks of size \(m\) and every cross-intersection is a singleton.

The finite enumeration corroborates the proof but is not used to justify the theorem for arbitrary \(m\).

## Relationship to prior work

Bjorndahl and Sink introduced a general properization construction for relational structures. In the finite case with \(m\) worlds, their construction replaces \(W\) by
\[
W\times W,
\]
uses one ordinary copy-partition for most agents and one skew copy-partition for a distinguished agent, proves properness, and proves that first-coordinate projection is a surjective bounded morphism. They also note that reflexivity, symmetry, transitivity, seriality, and Euclideanness are preserved.

Their later simplicial-belief paper reuses this construction and explicitly remarks that properization can create “substantial redundancy” by multiplying worlds and agential perspectives. The paper's displayed three-world example becomes a nine-world proper model.

The checked sources establish the quadratic upper bound but do not state a lower bound, an optimality theorem, or the Latin-square characterization of equality. The present theorem shows that, for the complete two-agent \(\mathsf{S5}\) frame, the quadratic blow-up is not an artifact of the cyclic construction: no smaller proper \(\mathsf{S5}\) bounded-morphic cover exists. It also identifies every extremal cover with a Latin-square grid.

## Limitations

The lower bound uses two-agent \(\mathsf{S5}\) equivalence classes essentially. It is not claimed for arbitrary non-equivalence relations, nor is \(m^2\) claimed to be optimal for three or more agents.

The Latin-square statement classifies optimal covers after the two families of equivalence classes are named. It does not count covers up to frame isomorphism or Latin-square isotopy.

The theorem concerns bounded-morphic properization, the comparison notion used in the source construction. Other semantic simulations, or richer structures such as simplicial sets, can avoid this exact size constraint.

## References

[1] Adam Bjorndahl and Philip Sink, “A Note on Proper Relational Structures,” arXiv:2506.17142, first posted 20 June 2025.

[2] Adam Bjorndahl and Philip Sink, “A Semantics for Belief in Simplicial Complexes,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 173–188. DOI:10.4204/EPTCS.447.10.

[3] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001.
