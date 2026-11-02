# Independent mathematical audit

## correctness

PASS

A mutual-inverse pair in O_n has equal rank and each image is a transversal to the other kernel. For rank two, alpha=(a;b,c), beta=(d;e,f) are inverse iff b<=d<c and e<=a<f; the piecewise swaps of nonidempotents are involutive and fix exactly binom(n+1,3) idempotents, leaving binom(n,3) transpositions. Corank-one maps (a;b) similarly invert precisely when missing image values hit the doubled kernel block, giving 2(n-1) fixed idempotents and binom(n-1,2) transpositions. This yields all-idempotent-fixing inverse involutions for n<=4. At n=5 rank three contains 60 maps and 21 idempotents, hence 39 nonidempotents of which none can be a fixed point of an inverse involution; parity forbids fixing every idempotent. The actual twenty-pair certificate was independently decoded and checked: 40 distinct maps, every pair mutually inverse, one moved idempotent, and twenty remaining unpaired idempotents. Independently checked 3,000 parameter cases n=3..12 for the two extremal-rank formulas; zero violations.

## originality

PASS

Higgins 2026 proves an inverse-valued permutation matching exists on O_n, but does not require a two-cycle involution or the idempotent-fixing property. Rank-stratified explicit involutions, the sharp O5 parity obstruction, and the one-moved-idempotent certificate are additional statements. Earlier involution-matching work concerns orientation preserving/reversing maps of a cycle and does not force these assertions on isotone chain transformations.

## value

PASS

The smallest obstruction to idempotent-fixed inverse involutions is a natural refinement of a recently settled matching-existence question. The sharp n=5 construction and explicit extremal strata supply precise nontrivial semigroup matching geometry, not only a parity sanity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
