# Independent mathematical audit

## correctness

PASS

For an arbitrary F_q-linear algebra isomorphism, mixed products of different source basis vectors vanish. Independence of the nonzero target basis squares then forces the products of distinct entries of each isomorphism-matrix row to vanish. Invertibility makes the matrix monomial. The permutation satisfies sigma(i+1)=sigma(i)+1, leaving rotations. At rotation k the recurrence lambda_{i+1}=lambda_i^2 d_{i+k}/c_i closes exactly when lambda_0^N=Theta(c)/Theta(rot_k d), so necessity and sufficiency hold in every characteristic. In the quotient by N-th powers, Theta(rot_1 d)=Theta(d)^2 since their ratio differs by d_0^N. Every quotient class is realized (vary a single coefficient), and squaring is invertible and has m-th power the identity. The fixed set of squaring^k has gcd(g,2^k-1) elements, including g for k=0. Burnside counts the classes; separately each of h admissible rotations has exactly g scalar lifts, giving gh automorphisms. If g>1 the identity orbit cannot include any other class, proving the collapse criterion. Read the frozen verifier as consistency evidence; fresh exact checks with python3 /workspace/review_evidence/5_gf4_witness.py tested 180 invertible maps on each of the 81 ordered weight pairs and recovered two classes and automorphism-order histogram {3:6,6:3} on the nine tuples. The theorem is the symbolic recurrence, not an inference from those examples. It treats algebras given by one directed cycle over the base field, not all descent forms of the scalar-extended algebra or all perfect evolution algebras.

## originality

PASS

The distinct earlier-record contribution is the explicit all-q, all-m arithmetic resolution on a fixed single-cycle support: the power-class invariant with its rotation action, reduced class count and exact rational lift count. Monomiality and the abstract orbit/counting framework are prior. A later dated indexed result contains the entire classification and goes further; this is demonstrable equivalent coverage in the later record, not evidence of an earlier publication or of provenance between the two. The strongest earlier sources do not resolve the all-dimension restricted orbit problem by a parameter substitution.

## value

PASS

A single cycle is the basic nonzero permutation support. The arithmetic obstruction determines exactly when the familiar unit-weight normalization fails, enumerates the resulting nonisomorphic forms in every dimension, and tells when graph rotations lift to rational automorphisms. The explicit all-dimension answer replaces an unrestricted matrix orbit search; it is not simply the F_4 example or a low-dimensional recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
