# Review of Affine lifting law for zeros of dual quaternionic polynomials

## Correctness

PASS. The recent source proves, for every dual slice regular polynomial,
\[
P(x_1+\epsilon x_2)
=
g(x_1)+
\epsilon\left(h(x_1)+dg_{x_1}(x_2)\right)
\]
throughout the full dual quaternion algebra. Vanishing is therefore exactly the conjunction of a primal-zero condition and one real-linear equation.

The affine-fiber description is elementary linear algebra once that source identity is fixed. The possible fiber dimensions follow from the source's differential-rank theorem for quaternionic slice regular functions.

For
\[
P_*(x)=x^2+1+\epsilon i,
\]
the primal zeros are \(J^2=-1\), and
\[
dg_J(v)=Jv+vJ.
\]
This map has image \(\mathbb C_J\) and kernel \(\mathbb C_J^\perp\). Solving against \(-i\) leaves only \(J=\pm i\) and gives the two claimed affine planes. Their dual parts have nonzero real component, so they are outside the quadratic cone.

## Originality

PASS with a named access risk. The 2026 source constructs the whole-algebra extension and explicitly says that systematic study of its zero sets is deferred. It does not state the affine lifting theorem or the off-cone example.

The earlier 2021 zero theory is identified by the fresh source as a theory on the quadratic cone. The accepted example has no zeros on that cone at all.

The open 2021 factorization paper studies right zeros through linear factors and quadratic norm factors. It contains no differential lifting formula and its principal generic extraction theorem does not cover the real primal factor in the explicit example.

Targeted database and public-literature searches for affine fibers, derivative lifting, the explicit polynomial, and Hensel-type formulations found no covering result. The inaccessible complete 2021 zero-set paper remains a residual risk and is not used for a whole-document noncoverage assertion.

## Value

PASS. The source presents full-space dual slice functions specifically as a new tool for understanding zeros and factorization of dual quaternionic polynomials, and announces systematic zero analysis as future work.

The accepted theorem supplies an immediate structural part of that program: every full-space zero fiber is completely determined by the primal differential, with a unique-lift criterion at nondegenerate zeros and exact dimension alternatives at degenerate ones.

The explicit polynomial shows that the new ambient space is not a cosmetic extension. It has two complete affine zero planes that are entirely invisible on the quadratic cone. This gives a concrete geometric phenomenon and a reusable lifting criterion for future factorization and zero-set arguments.

Same-model review: passed. Independent audit: not yet performed.
