# Cyclically symmetric minimum-genus orientable embedding of K(4,10)

## Context

The complete bipartite graph K(4,10) has bipartition sizes 4 and 10, hence 14
vertices and 40 edges. Its minimum orientable genus is
ceil((4-2)(10-2)/4) = 4, a classical formula of Ringel and Bouchet. The
admitted target question asks whether this bound can be realized by a cellular
orientable embedding with a cyclic symmetry permuting the 10 vertices of the
large part: either exhibit such a rotation system with an explicit cyclic
symmetry of order 10 (or a divisor acting semiregularly on the 10-side)
verified to have genus 4, or rigorously prove that no minimum-genus rotation
system admits such symmetry.

## Definitions

Let A = {a0,a1,a2,a3} be the 4-side and B = Z_10 = {b0,...,b9} the 10-side.
An orientable cellular embedding is encoded by a rotation system: a cyclic
ordering rot(v) of the neighbours of each vertex v. Faces are traced by the
standard successor rule: crossing a dart (a,b) continues from b with the
successor of a in rot(b), and vice versa. If V, E, F are the numbers of
vertices, edges, and faces, Euler's formula V - E + F = 2 - 2g gives the
orientable genus g. An orientation-preserving embedding automorphism is a
graph automorphism mapping rotation systems to rotation systems up to cyclic
rotation at each vertex.

## Result

Yes. K(4,10) admits a minimum-genus (genus 4) orientable cellular embedding
whose orientation-preserving automorphism group contains an element g of
order 10 acting as the 10-cycle i -> i+1 on the large part B.

Witness rotation system (arithmetic mod 10 on B indices). Let
phi = transposition (a0 a1) on A and g(a_j) = a_{phi(j)}, g(b_i) = b_{i+1}.
Then:

- rot(b_0) = (a0, a2, a1, a3); rot(b_i) = phi^i applied to rot(b_0), i.e.
  (a0,a2,a1,a3) for even i and (a1,a2,a0,a3) for odd i.
- rot(a0) = (0,1,2,3,4,5,6,7,8,9).
- rot(a1) = (1,2,3,4,5,6,7,8,9,0), i.e. rot(a0) shifted by +1.
- rot(a2) = rot(a3) = (0,9,8,7,6,5,4,3,2,1).

Face-tracing gives F = 20 faces, every face of length 4 (a quadrangulation).
Hence V - E + F = 14 - 40 + 20 = -6 = 2 - 2g, so g = 4, the known minimum.
The map g preserves the rotation system up to cyclic rotation at each vertex,
acts as a 10-cycle on B, and has order 10 as a permutation of directed edges.

## Proof / evidence

Rotations are well-formed: each rot(a) permutes all 10 vertices of B and each
rot(b) permutes all 4 vertices of A. Symmetry holds in the cyclic-order
sense: phi(rot(b_i)) is cyclically equal to rot(b_{i+1}) for every i, and
rot(a_j) shifted by +1 is cyclically equal to rot(a_{phi(j)}) for every j,
which is exactly the condition for g = (phi, +1) to be an
orientation-preserving rotation-system automorphism. The B-action
i -> i+1 is a 10-cycle and the induced dart permutation has order
lcm(2,10) = 10, confirmed by direct orbit computation. An independent
from-scratch face tracer yields 20 faces each with 4 dart-states (boundary
length 4), dart-sum 80 = 2E, and Euler genus 4. The tracer was validated on
K(2,2) (planar 4-cycle recovered) and K(4,4) (torus quadrangulations found in
random search), with the identity sum of face lengths = 2E holding on every
censused system. Exhaustive enumeration of all 5896 rotation systems
symmetric under g = (phi,+1) across all five S_4 conjugacy classes of phi
found 24 minimum-genus systems for transposition phi and 16 for
double-transposition phi, each of dart-order exactly 10; the witness above is
one of the 24.

## Limitations

The result is an existence proof by explicit symmetric rotation system plus
supporting exhaustive computer enumeration of the symmetric slice; the
nonexistence half of the target disjunction is not claimed since the
affirmative half holds. No claim is made about uniqueness, classification of
all symmetric embeddings, asymmetric embeddings, or non-orientable
embeddings.

## Reproducibility

Rebuild rotA and rotB as above, form successor tables, trace faces from every
unvisited dart (0,j,b), count faces and face lengths, evaluate V - E + F and
the genus, and compute the order of g on the 80 darts via
(0,j,b) -> (0,phi(j),b+1), (1,i,j) -> (1,i+1,phi(j)). Scripts
output/artifacts/verify_witness.py and output/artifacts/enumerate.py perform
these steps; output/artifacts/verification.json records the witness data and
checks.

## References

- A. Bouchet, Orientable and nonorientable genus of the complete bipartite
  graph, J. Combin. Theory Ser. B 24 (1978), 24-33 (minimum-genus formula).
- E. Flapan et al., Symmetries of embedded complete bipartite graphs,
  arXiv:1205.4052 (spatial S^3 symmetries; different category).
- J. H. Kwak and Y. S. Kwon; G. A. Jones; S. Du et al.: regular and
  reflexible embeddings of K_{n,n} (require equal parts, inapplicable here).
- Standard rotation-system face-tracing and Euler genus computation.
