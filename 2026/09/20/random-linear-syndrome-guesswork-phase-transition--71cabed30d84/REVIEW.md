# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The core statement reduces, for each fixed source word, to moments of the
number of earlier likelihood-ranked words that collide under a random linear map.
For independent-entry matrices, a d-dimensional tuple span is annihilated with
probability exactly q^{-md}. Counting rank-d tuples gives uniform integer-moment
bounds. Jensen/Lyapunov cover rho >= 1, while a rank-one/pairwise second-moment
bound plus Paley--Zygmund covers 0 < rho < 1. The full-row-rank version follows
from the exact probability that a uniform kernel contains a fixed d-subspace.

The exponent step uses Arıkan's one-shot Rényi guesswork inequality. A separate
cellwise application of the same inequality plus convexity gives the matching
converse for every encoder with at most M labels, so the claimed linear-encoder
exponent is also optimal among arbitrary encoders. The typical-matrix statement
then follows from the deterministic lower bound, the ensemble upper bound, and
Markov's inequality. No step uses IID source structure.

Adversarial checks included the endpoints m=0 and m=n, dependent difference
vectors over q>2, rank-deficient random matrices, tie handling in the likelihood
order, and the regime where the formal unconstrained-minus-syndrome exponent is
negative. The baseline G >= 1 is precisely what creates the positive part.

The finite verification artifact exhaustively enumerates small q=2 and q=3
instances and reproduces both exact first-moment formulas; it also checks the
binary second-moment identity and several fractional/integer moments. It reports
PASS. These computations support but do not replace the general proof.

## Originality

**PASS, to the best of our knowledge, with material adjacent-literature risk.**

The closest recent source inspected in full is Tavakoli, arXiv:2607.00205. Its
binary exact-exponent theorem assumes the stated subcriticality conditions
h_b(delta*) > 1-R and h_b(p) > 1-R, and its q-ary theorem assumes the analogous
conditions. Thus its theorem does not cover the low-rate side where the affine
formula would become nonpositive. The present theorem agrees with that result
inside its hypothesis range but gives the all-rate positive-part continuation and
works for arbitrary source sequences.

Older Rényi task-encoding and guessing literature was explicitly checked because
it is the strongest source of possible prior coverage. Arıkan (1996) supplies the
one-shot unconstrained guessing inequality. Bunte--Lapidoth (2014) establishes the
Rényi threshold for arbitrary task encoders. Bracher--Lapidoth--Pfister (2019)
characterizes distributed guessing rates and describes achievability by random
binning. Bracher--Hof--Lapidoth (2017) relates guessing to task encoding in a
storage setting. These works make the arbitrary-encoder exponent and unstructured
random-binning achievability prior art, not part of the novelty claim.

Targeted searches were made for the combinations "random linear syndrome
+ guesswork", "linear binning + guesswork/Rényi", "parity-check + guesswork +
Rényi", "random linear encoder + guessing", and equivalent universal-hashing
formulations. No source surfaced that states the finite constant-factor law
E_H G_H(x)^rho asymp (1+q^{-m}(G_0(x)-1))^rho, its exact one-shot first moment,
or the resulting all-rate optimality of uniform random linear syndromes.

Residual risk remains because the proof is short once the collision-count
viewpoint is adopted, and universal hashing/random-binning literature is broad.
The Bunte--Lapidoth paper was checked through its accessible arXiv metadata and
abstract rather than every theorem in its full published text, and the
Bracher--Hof--Lapidoth source was inspected at abstract level. These are the
sources most plausibly capable of containing an equivalent structured-linear
specialization. No such specialization was found in the material inspected.

A search of the current SCOPE archive by guesswork, random-linear-syndrome,
relevant source identifier, and equivalent claim terminology found no prior SCOPE
record covering this result.

## Value

**PASS.** The result resolves a concrete gap left by the hypothesis range of a
recent exact coset-guesswork theorem, and does so with a source-independent
finite-length structural identity rather than another weight-enumerator
calculation. It identifies the exact all-rate moment transition, proves that a
highly structured linear encoder is exponent-optimal against arbitrary encoders,
and exposes a moment-cascade regime in which mean and higher-moment decoding
complexities have different exponential behavior.

## Scope and limitations

The field size is fixed. The result is about optimal likelihood-ordered syndrome
search and does not imply an efficient implementation of that order. It gives the
leading exponential rate, not the sharp logarithmic second-order term. No claim is
made that random linear binning itself is new; the novelty claim is restricted to
the structured-linear constant-factor law and its all-rate consequences.
