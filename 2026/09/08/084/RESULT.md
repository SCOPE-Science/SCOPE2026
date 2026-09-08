# Schur roots, bricks, and Kac q=2 counts for the wild 3-Kronecker quiver

## Context

The 3-arrow Kronecker quiver is the minimal wild quiver past the tame
2-Kronecker threshold. Gabriel's theorem is silent on its imaginary roots,
and Kac's root criterion guarantees indecomposables without deciding
Schur-ness (general representation a brick), Derksen-Weyman canonical
summands, or finite-field Kac counts. This record gives the evaluated
Schur/brick table for six small imaginary-root vectors plus exact
Kac evaluations at q=2 for the two smallest vectors.

## Definitions

- Quiver Q: vertices {1,2}, three parallel arrows 1 -> 2, over F2.
- Dimension vector d = (a,b) = (dim V1, dim V2).
- Euler form: <(a,b),(c,d)> = ac + bd - 3ad.
- Tits form: q(a,b) = a^2 + b^2 - 3ab.
- Committed list L = {(2,2),(2,3),(3,3),(3,4),(4,4),(2,4)}.
- A representation is a triple (A1,A2,A3) of b x a matrices over F2.
  Its endomorphism ring is pairs (X: a x a, Y: b x b) with Y A_k = A_k X.
  A brick has End = F2 (endomorphism dimension 1).
- d is a Schur root if the general representation of dimension d is a brick.
  Then its Derksen-Weyman canonical decomposition is the trivial one-term
  decomposition `d`.
- Kac polynomial A_d(q): number of absolutely indecomposable representations
  of dimension d over F_q up to isomorphism. A_d(2) is evaluated by
  F2-isomorphism enumeration plus separation of absolutely indecomposable
  from merely indecomposable classes.

## Result

1. Every d in L is an imaginary root, and every d in L is a Schur root.
   Hence the canonical decomposition of each d is the trivial one-term
   decomposition `d` itself.

2. Explicit F2-brick witnesses (matrix triples A1,A2,A3 of size b x a),
   each with certified endomorphism-ring dimension 1:

   - (2,2): A1=[[1,1],[1,0]], A2=[[1,1],[0,1]], A3=[[0,1],[1,0]]
   - (2,3): A1=[[1,0],[0,0],[0,0]], A2=[[1,1],[0,1],[1,0]], A3=[[0,1],[1,1],[0,1]]
   - (3,3): A1=[[0,1,0],[1,1,0],[0,0,1]], A2=[[0,0,0],[1,0,0],[1,1,0]], A3=[[1,1,1],[0,1,0],[0,0,0]]
   - (3,4): A1=[[0,1,0],[1,1,0],[0,1,1],[0,1,1]], A2=[[0,1,0],[0,1,1],[1,1,0],[1,1,0]], A3=[[0,1,1],[0,0,1],[0,1,0],[1,1,0]]
   - (4,4): A1=[[0,0,0,0],[1,0,0,0],[0,1,0,1],[0,1,1,1]], A2=[[0,0,1,0],[0,1,0,1],[0,1,0,1],[1,1,0,0]], A3=[[1,0,1,1],[1,0,1,0],[0,0,1,1],[1,1,1,0]]
   - (2,4): A1=[[1,1],[0,1],[0,1],[1,0]], A2=[[0,0],[0,0],[1,0],[0,1]], A3=[[1,0],[1,1],[1,1],[0,0]]

3. Exact Kac values at q=2:
   - A_(2,2)(2) = 91.
   - A_(2,3)(2) = 204.

## Proof / evidence

(a) Root status. Tits values: (2,2):-4, (2,3):-5, (3,3):-9, (3,4):-11,
(4,4):-16, (2,4):-4. All q <= -1, so not real (real needs q=1).
Fundamental-domain quantities c1=2a-3b, c2=2b-3a: five vectors satisfy
c1,c2 <= 0 (fundamental, hence imaginary roots); (2,4) has (-8,+2),
non-fundamental, but reflection s2(a,b)=(a,3a-b) sends (2,4)->(2,2)
with q preserved, so (2,4) is Weyl-equivalent to a fundamental imaginary
root, hence an imaginary root.

(b) Schur verdict. The stored triple for each d has dim End = 1 by the
GF(2) nullspace of the intertwining system Y A_k = A_k X
(independently recomputed 6/6). Since dim End >= 1 always and
endomorphism dimension is upper semicontinuous in the representation
entries, one brick forces the general representation to have End = F2,
i.e. d is a Schur root with trivial canonical decomposition.

(c) Exact (2,2) count. Representation space 2^12=4096 points; acting group
GL(2,F2)xGL(2,F2) has 6x6=36 elements. Orbit enumeration gives
148 isomorphism classes whose orbit sizes sum to 4096 exactly.
Exhaustive idempotent search in End (decomposable iff End contains a
nontrivial idempotent) gives 98 indecomposable classes.
End-dimension distribution: {1:70, 2:49, 3:14, 4:7, 5:7, 8:1}.
The 70 End-1 classes are bricks (automatically absolutely
indecomposable). The 28 End-2 indecomposable classes split by testing
whether every nonzero endomorphism is invertible: 21 are local
(dual-number type, absolutely indecomposable) and 7 are the field F4
(not absolutely indecomposable since End tensor Fbar splits).
Hence A_(2,2)(2) = 70 + 21 = 91.

(d) Exact (2,3) count. Representation space 2^18=262144; group
GL(2,F2)xGL(3,F2) has 6x168=1008 elements. Orbit enumeration gives
402 classes; orbit masses sum to 262144 exactly; spectrum
{1:1, 21:7, 42:14, 84:7, 126:28, 252:91, 504:43, 1008:211}.
End-dimension distribution: {1:183, 2:49, 3:22, 4:70, 5:49, 6:7, 7:14, 9:7, 13:1}.
Idempotent-End test: 204 indecomposable classes = 183 bricks (End 1)
+ 21 with End 2 (all other End>1 classes decomposable).
Field-vs-local test: all 21 are local, none is F4.
Hence A_(2,3)(2) = 183 + 21 = 204.

## Limitations

- No Kac q=2 values for (3,3),(3,4),(4,4),(2,4) beyond the >= 1 lower bound
  from the exhibited bricks; no closed Kac polynomials, only evaluations
  at q=2 for (2,2),(2,3).
- The admitted nontrivial-canonical-summand clause is dropped: all six
  vectors turned out Schur (trivial decomposition).
- Brick triples are certified but not asserted unique or minimal.
- Stored s1 JSON labels (2,4) as 'imag-fund' loosely; the correct statement
  is non-fundamental Weyl-equivalent to (2,2), as the stored reflection path
  shows. A superseded trace-based absolute-count file (nabs=77) is not used;
  the invertibility split giving 91 is the operative certificate.

## Reproducibility

All scripts use only the Python standard library with fixed seed 251 for
the brick search; (2,3) enumeration runs ~40 s. Replay from the committed
3-arrow Kronecker adjacency: recompute Tits form and Weyl path; recompute
dim End for each brick triple; recompute orbit enumerations with mass
balance; rerun idempotent and field-vs-local splits. Verification-critical
files are copied to output/artifacts/.

## References

- Derksen and Weyman, On the Canonical Decomposition of Quiver
  Representations, https://doi.org/10.1023/A:1020007100426
- Schofield, General Representations of Quivers,
  https://doi.org/10.1112/plms/s3-65.1.46
- Kac, Root systems, representations of quivers and invariant theory,
  https://doi.org/10.1007/BFb0063236
- Weist, Tree modules of the generalized Kronecker quiver,
  https://arxiv.org/abs/0901.1780
- Belmans, Franzen and Petrella, The QuiverTools package for SageMath
  and Julia, https://arxiv.org/abs/2506.19432
- Schiffmann, Kac polynomials and Lie algebras associated to quivers
  and curves (survey), https://arxiv.org/abs/1802.09760
