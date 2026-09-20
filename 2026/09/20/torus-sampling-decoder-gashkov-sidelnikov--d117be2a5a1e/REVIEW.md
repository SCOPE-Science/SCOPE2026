# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof starts from the exact length-two criterion and signed-column
torus model in Shi--Li--Xia--Helleseth--Ozbudak.  For a weight-three syndrome
\(S\), every residual norm \(a=N(S-\beta)\) avoids \(0\) and \(1\), so the
success indicator is exactly \((1-\chi(a(a-1)))/2\).  The norm equation is a
quadratic in \(\beta\), and its torus-fiber cardinality is
\(1-\chi((N(S)+1-a)^2-N(S))\).  Summing over fibers converts the success count
into a quartic character sum.

For \(n=N(S)\ne0,1\), the quartic
\(X(X-1)((n+1-X)^2-n)\) is squarefree.  Its smooth projective model has genus one
and two rational points at infinity.  The affine character-sum point count then
gives \(\#C_n(\mathbb F_q)=2M(S)\) exactly, and Hasse's theorem yields the
claimed \(\sqrt q\) error term.  The expected-probe bound is the geometric mean
waiting time for independent uniform torus probes.

The leader-multiplicity identity uses two facts already established in the source
paper: a length-two residual has a unique unordered two-term decomposition, and a
minimum three-term decomposition has no equal or opposite summands.  Hence every
weight-three error vector is counted exactly three times by successful choices of
its first torus summand.

Adversarial checks included the characteristic-three identity \(4=1\), the two
points at infinity on a monic quartic model, possible collisions of the quadratic
factor with \(0\) or \(1\), double discriminant roots, and the conversion from
signed torus elements to distinct ternary coordinate positions.  The only
collision case for the quartic is \(N(S)=1\), which is excluded because then the
syndrome already has additive length one.

The finite verification artifact constructs the fields and quadratic extensions
without external algebra packages.  For \(q=9,27,81\) it enumerates every exact
length-three syndrome, verifies the exact character-sum identity and Hasse bound,
and independently enumerates unordered torus triples to check the factor of three
in the coset-leader count.  It reports PASS.  These computations are supporting
checks rather than a substitute for the proof.

## Originality

**PASS, to the best of our knowledge, with material near-simultaneous and folklore risk.**

The closest source inspected in full is Shi et al., arXiv:2609.20402.  It proves
the signed-column torus model, the additive-length classification, uniqueness of
length-two decompositions, and a direct weight-three search over \(\mathcal T\).
Its Remark 2.9 states that the direct construction may test all \(q+1\) torus
elements in the worst case.  The paper then develops structured conic searches and
proves an asymptotic admissible-parameter density \(1/4\), corresponding to
\(4+o(1)\) expected uniform parameter trials.  The paper does not state a success
density for uniform sampling in the direct torus search, an elliptic-curve point
count for that density, or a formula for the number of minimum-weight leaders in a
weight-three coset.

The 2025 generalized-Zetterberg covering-radius paper was checked because it uses
algebraic curves over finite fields in a closely related family.  Its stated focus
is covering radius and existence, not the direct randomized torus-probe count or
coset-leader multiplicity considered here.  Searches using the source identifier
and combinations of “Gashkov-Sidel'nikov”, “norm-one torus”, “randomized decoder”,
“three-term representation”, “coset leader multiplicity”, “elliptic curve”, and
“Zetterberg decoding” did not surface an equivalent theorem.

Older Zetterberg decoding literature remains the main residual originality risk.
Dodunekov--Nilsson (IEEE Trans. Inf. Theory 38(5), 1992) and the 1989 Kallquist
decoder are bibliographically relevant, but the full text of the former was not
available from the repository inspected and the latter was only located through
secondary bibliographic descriptions.  The 2026 source paper itself distinguishes
these older Zetterberg decoders from its new complete constructive description of
the original ternary Gashkov-Sidel'nikov families.  No available statement from
the older sources matched the exact torus-sampling or leader-count theorem here,
but incomplete inspection leaves a nonzero residual risk.

The current public SCOPE archive was checked by the source identifier, torus
decoding terminology, elliptic-curve formulation, and coset-leader terminology;
no accepted record covering this claim was found.

## Value

**PASS.** The result turns the recent paper's worst-case \(q+1\)-probe direct
construction into a syndrome-uniform Las Vegas decoder requiring only
\(2+O(q^{-1/2})\) expected candidate probes.  It also identifies the exact source
of the half-density as an elliptic-curve point count and yields a new quantitative
statement about the number of maximum-likelihood error patterns in every hard
coset.  These are direct refinements of the constructive decoding problem rather
than routine parameter changes.

## Scope and limitations

The theorem is specific to the characteristic-three norm-one-torus model of the
original Gashkov-Sidel'nikov families.  The expected-probe statement does not
claim constant bit complexity: character evaluation, field arithmetic, quadratic
solving, and coordinate recovery still have their usual costs.  No closed formula
for the varying elliptic Frobenius trace is proved, and no extension to all
generalized Zetterberg codes or other odd characteristics is claimed.
