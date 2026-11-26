# All-size ordinary zero forcing and propagation on the degree-five Clebsch graph

## Finding

Let \(G\) be the five-regular Clebsch graph, not its degree-ten complement. The ordinary zero-forcing polynomial, counting labeled initial black sets, is
\[
\mathcal Z_G(z)=3872z^{10}+3632z^{11}+1760z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\]
There are \(9961\) successful initial sets. Every inclusion-minimal successful set has cardinality ten; in particular, merely being inclusion-minimal rather than of minimum cardinality adds no other sets. The following table refines the full polynomial by the number of synchronous rounds until all vertices are black:

| Initial black size | 0 rounds | 1 round | 2 rounds |
|---:|---:|---:|---:|
| 10 | 0 | 0 | 3872 |
| 11 | 0 | 272 | 3360 |
| 12 | 0 | 1280 | 480 |
| 13 | 0 | 560 | 0 |
| 14 | 0 | 120 | 0 |
| 15 | 0 | 16 | 0 |
| 16 | 1 | 0 | 0 |

There are no other cardinalities or propagation times for successful sets. In particular the minimum and maximum propagation times over minimum-cardinality sets are both two. The result concerns the entire forcing family and its synchronous dynamics, rather than only the known minimum cardinality and family of optimum sets. For reference, the seven orbits of optimum sets have respective sizes \(960,960,480,480,480,320,192\); their white complements are represented by bit masks \(303,363,287,399,873,407,857\). The accompanying CSV records all eighteen six-white orbits, successful or not.

## Assumptions and scope

Vertices are integers from 0 to 15 representing \(\mathbb F_2^4\). Distinct vertices \(x,y\) are adjacent if \(x\oplus y\in\{1,2,4,8,15\}\), where \(\oplus\) is bitwise XOR. Initially the vertices of a chosen set are black and all others are white. In a synchronous round, each white vertex adjacent to a black vertex with just one white neighbor becomes black; the conditions are tested before changing any colours. An inclusion-minimal successful set has no successful proper subset. Masks encode labels, not isomorphism types. Real maximum nullity refers to real symmetric matrices with nonzero off-diagonal entries precisely on graph edges and with unrestricted diagonals.

## Proof

**Forcing number and real maximum nullity.** The adjacency eigenvalue for the character with index \(a\in\mathbb F_2^4\) of Hamming weight \(w\) is \(4-2w+(-1)^w\), by summing the character over the generators. Thus the eigenvalues are \(5,1,-3\), with respective multiplicities \(1,10,5\), and the real matrix \(A-I\) has nullity ten. For any real symmetric matrix with the stated pattern, a kernel vector that is zero on a forcing set vanishes everywhere: at each force, the row for the black vertex has just one white neighbor, whose coefficient is nonzero. Consequently maximum nullity is at most the zero-forcing number. A witness with initially white vertices \(0,1,2,3,5,8\), of mask 303, forces in two rounds: \(15,14,6,11\) can force \(0,1,2,3\), respectively, and then \(1,0\) can force \(5,8\). Together these facts give \(Z(G)=M(G)=10\). The equality is included as a check and normalization, not a priority claim.

**Full automorphism group.** The five generators sum to zero and any four form a basis. Their permutations therefore extend uniquely to linear automorphisms, and all sixteen translations act. Conversely the stabilizer of zero embeds in the permutations of its five neighbors: each of the remaining ten vertices is the XOR of a distinct pair of generators and is their unique common neighbor other than zero. Thus the full group has \(16\cdot 5!=1920\) elements.

**Exhaustive counting.** For each initial white mask \(W\) in \([0,2^{16})\), compute the union of all singleton sets \(N(v)\cap W\) over black \(v\) for which this intersection has size one. If the union is nonempty, subtract it from \(W\) and add one to the round count; if it is empty at a nonempty white mask, the process has stalled. This reproduces the literal synchronous rule. The white mask strictly shrinks at every non-stalling round. For every mask that reaches zero, count the initial black cardinality and the recorded round count. This gives the table by the included exact implementations, so summing rows proves the polynomial and total.

Forcing is monotone: from a larger black set, a force from the smaller-set process remains legal unless the target has already become black. Hence testing every single deletion suffices to determine inclusion-minimality. Scanning all successful masks by that test finds exactly the \(3872\) size-ten sets and none larger. The independent set-based program also applies the full group to all \(\binom{16}{6}=8008\) six-white masks. Taking the least unassigned mask as the representative of each orbit and removing its full orbit checks all eighteen rows in the CSV. The table and inclusion-minimality rely on the exhaustive all-size check, not on the six-white count alone.

## Verification

With the unchanged `verify_white.cpp`, `verify_group.py`, and `six_white_orbit_certificate.csv` in the package directory, run `g++ -O2 -std=c++17 -Wall -Wextra -o verify_white verify_white.cpp && ./verify_white` and `python3 verify_group.py`. Each verifier exhausts the 65,536 initial sets. The C++ program checks the complete cardinality and round table and all one-vertex deletions from successful sets; the Python program independently checks the forcing counts and inclusion-minimality, generates and tests the full automorphism group, and compares every CSV row. These are finite graph checks, not a classification for other folded cubes.

## Relationship to prior work

The zero-forcing rule and the nullity bound are due to the AIM Minimum Rank–Special Graphs Work Group, [DOI 10.1016/j.laa.2007.10.009](https://doi.org/10.1016/j.laa.2007.10.009), Proposition 2.4. Boyer et al., [arXiv:1801.08910](https://arxiv.org/abs/1801.08910), define the polynomial; Grood et al., [arXiv:2312.14298](https://arxiv.org/abs/2312.14298), study well-forced graphs; Hogben et al., [arXiv:1410.4191](https://arxiv.org/abs/1410.4191), define extremal propagation times. These general concepts are not new here.

For this exact graph, the published [binary-information-set comparison](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-unique-fort-orbit-separating-clebsch-zero-forcing-from-binar--64ea619489d7/RESULT.md) characterizes successful six-white complements by binary column independence with a single induced-graph exception, and records the minimum ten, the 3872 optimum sets and their seven orbits. The minimum-family data are therefore supporting context in the present account, not a new minimum-set classification. Characterizing the minimum family alone does not say whether every larger forcing set contains an optimum, and does not give synchronous propagation times. Here the contribution is the complete ordinary all-cardinality polynomial, the proof of well-forcedness on this graph, and the joint size/round census, without a claim of discovery priority. Results on skew forcing, on powers of the graph, or on its degree-ten complement concern different objects or rules.
