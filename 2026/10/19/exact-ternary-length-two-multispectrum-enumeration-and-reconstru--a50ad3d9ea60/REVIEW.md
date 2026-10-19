# Scientific review

## Correctness — PASS

The object is the complete directed 2-gram multiplicity matrix of a linear ternary word. The Euler-trail existence criterion requires connected active support and either zero degree imbalances or a unique +1/-1 ordered endpoint pair. The proof partitions matrices by one, two, or three incident symbols, then enumerates the balanced and open three-symbol cases using oriented triangle differences. Precisely enumerated disconnected cases are removed before free loop insertions. Algebra gives the rational function for every length; a direct integer recurrence, direct word-set enumeration for all lengths 1–11, and independent exhaustive matrix feasibility testing for edge counts 0–12 agree. No finite census is used to justify the infinite formula. Boundary at length one is addressed separately.

## Originality — PASS

The closest published work is Jacquet–Knessl–Szpankowski (2010/2012), which derives exact balanced-matrix generating functions and asymptotic numbers of cyclic and noncyclic Markov types. The relevant 2012 journal paper and Drmota–Szpankowski's Chapter 11 §11.2.2 were inspected: their noncyclic result is an exact decomposition followed by bounds and an asymptotic theorem, not an exact all-length ternary series. Chang–Chrisnata–Ezerman–Kiah (2016) give exact profile numbers when read length is \(\ell\) and \(\ell\le n<2\ell\), which for \(\ell=2\) covers only \(n=2,3\). Gabrys–Milenkovic (2018) work in logarithmic read-length coding regimes. Related circular ternary and binary linear count statements do not imply the displayed finite ternary linear answer without the new open-endpoint and disconnected-support enumeration. A literature-index omission remains a documented risk.

## Mathematical value — PASS

The finding gives the complete length-uniform observation-capacity function for the first genuinely three-symbol order-one reconstruction channel, a natural case in Markov-type counting and DNA substring profiles. It resolves finite-length values left undetermined by the principal asymptotic theory, identifies a six-period correction, and supplies an exact optimal noiseless code-size formula. The leading coefficient is known from prior asymptotics; it is not presented as a new improvement. No efficient encoder, noisy decoding, or larger-alphabet result is asserted.

## Limitations and closest comparisons

Potential equivalent but unindexed enumerations of noncyclic three-state Markov types are the main originality risk. The result also does not count the number of words per profile or specify canonical code representatives. Verification is reproducible with `python3 verify.py`.

Self-review: passed. Independent audit: not yet performed.
