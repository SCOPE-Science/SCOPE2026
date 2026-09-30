# Same-matrix cubic Pisot pair: the balanced-block algorithm terminates in 9 blocks

## Context

Let beta>1 be the real root of x^3-2x^2-1 and let

- sigma: 1->2, 2->3, 3->133,
- sigma': 1->2, 2->3, 3->313.

Both substitutions have incidence matrix
M=[[0,0,1],[1,0,0],[0,1,2]].  For a balanced pair (U,V), split at every
common prefix abelianization; breadth-first closure from the diagonal seeds
(1,1), (2,2), (3,3) defines the balanced-block substitution Phi when the
closure is finite.

## Result

The balanced-block algorithm for this concrete pair terminates in exactly nine
minimal blocks, of maximum word length seven:

- B0=(1,1),       Phi(B0)=B1
- B1=(2,2),       Phi(B1)=B2
- B2=(3,3),       Phi(B2)=B3 B2
- B3=(13,31),     Phi(B3)=B7
- B4=(32,23),     Phi(B4)=B5 B2
- B5=(133,331),   Phi(B5)=B8
- B6=(213,132),   Phi(B6)=B4 B0 B2 B2
- B7=(2133,3132), Phi(B7)=B2 B6 B2 B0 B2 B2
- B8=(2133133,3133132),
  Phi(B8)=B2 B6 B2 B0 B2 B2 B6 B2 B0 B2 B2.

With columns indexed by B0,...,B8, the incidence matrix is

N = [[0,0,0,0,0,0,1,1,2],
     [1,0,0,0,0,0,0,0,0],
     [0,1,1,0,1,0,2,4,7],
     [0,0,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,0],
     [0,0,0,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,1,2],
     [0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,1,0,0,0]].

N^8 is strictly positive (minimum entry 1), so Phi is primitive.  Phi^3(B2)
starts with B2, providing the stated prolongability witness.  The normalized
block frequencies are approximately

(0.072095, 0.032688, 0.487231, 0.220910, 0.022491,
 0.010197, 0.049605, 0.100160, 0.004623).

The exact density of diagonal length-one blocks per projected letter is

(-3-9 beta+7 beta^2)/32 = 0.350051...,

and the diagonal-block density among blocks is

(-3-104 beta+90 beta^2)/347 = 0.592015....

Every non-diagonal block reaches a diagonal block within two Phi-steps.

These statements are the claimed finite common-block computation.  They do
not, by themselves, assert that the common-point set is a regular model set or
has pure-point diffraction.  Published balanced-pair/Rauzy-fractal and overlap
criteria impose additional geometric or dynamical hypotheses; those hypotheses
are not established here.

## Proof / evidence

The shared incidence matrix follows by abelianizing the two substitutions.
The characteristic polynomial of M is x^3-2x^2-1.  It has one real root
2.2<beta<2.21; because det(M)=1, the two non-real conjugates have modulus
1/sqrt(beta)<1, so beta is Pisot.  M^4 is strictly positive.

`artifacts/verify_blocks.py` reconstructs the breadth-first closure, checks
that each of the nine blocks is balanced and has no interior common cut,
re-splits every Phi-image, verifies the matrix N, and checks M^4>0, N^8>0
and the prolongability witness.  `artifacts/exact_freq.py` solves
(N-beta I)v=0 exactly in Q(beta), proves positivity on beta in (2.2,2.21),
and derives the two displayed coincidence densities.  `artifacts/blocks.json`
stores the block list, Phi-images and N.

## Originality and scope

Balanced-block methods for common dynamics of same-matrix Pisot substitutions
are established in work of Sellami and subsequent authors.  The contribution
here is the exact finite closure and frequency data for this particular pair.
No priority claim is made from literature non-detection.

## Limitations

The computation does not verify all hypotheses of any theorem that would turn
finite balanced-block closure into a regular-model-set or pure-point-diffraction
conclusion.  The intersection matrix N is not itself Pisot.  Decimal
frequencies are only roundings of exact Q(beta) expressions.

## Reproducibility

Run:

- `python3 artifacts/verify_blocks.py`
- `python3 artifacts/exact_freq.py`

Both scripts use only the Python standard library.

## References

- T. Sellami, *Common dynamics of two Pisot substitutions with the same
  incidence matrix*, arXiv:1002.3559.
- T. Sellami, *Balanced pair algorithm for a class of cubic substitutions*,
  Turk. J. Math. 39 (2015), DOI 10.3906/mat-1407-3.
- K. Scheicher, V. F. Sirvent, P. Surer, *Measure-wise disjoint Rauzy
  fractals with the same incidence matrix*, Monatsh. Math. 194 (2021),
  DOI 10.1007/s00605-021-01515-x.
- V. F. Sirvent, S. Starosta, *On a conjecture about the absence of an
  initial balanced pair for Pisot substitutions*, arXiv:1711.10167.
