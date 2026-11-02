# Scientific assessment of exact Abelian-border multiplicities

## Correctness (C): PASS

The domain comprises labeled linear words over a uniform fixed alphabet of size \(q\ge2\), with one Abelian-border count per proper positive length. Opposite positions form independent ordered symbol pairs. Prefix/suffix Parikh equality is *equivalent* to a zero sum of their difference vectors at the corresponding paired step. The multinomial-squared coefficient counts all walks ending at zero. Every finite walk has a unique sequence of first-return excursions followed by a possibly empty return-free tail; distinguishing terminal returns from nonterminal returns yields the even/odd generating functions with no missing center or odd-middle factors. The normalization at \(v=1\) reproduces exactly \(q^{2m}\) and \(q^{2m+1}\) words.

The local limit uses the explicitly computed determinant \(q^{-q}\) of the multinomial covariance restricted to \(q-1\) coordinates. The associated return probability decays as \(j^{-(q-1)/2}\), giving recurrence at \(q=2,3\) and transience at \(q\ge4\). The factorial-moment formula and harmonic bounds prove the ternary exponential limit; a Gaussian simplex integral proves the binary benchmark; the renewal escape probability yields the geometric higher-alphabet law. The paired-step representation shows the full proper-border count differs from twice the short-border count by at most one.

The independent finite checker `verify.py` exhaustively enumerated the binary, ternary and quaternary instances specified in `VERIFICATION.md`, independently comparing complete border-length multiplicity distributions against integer coefficient recurrences and returning `VERIFY_OK`. The finite checks do not prove infinite claims; those are established analytically in the proof.

## Originality (O): PASS with explicit priority risk

The closest primary paper, Blanchet-Sadri–Chen–Hawes (arXiv:1708.06461v1, first public 2017-08-22), Theorem 3 on page 8 of the PDF, already gives the complete binary border-multiplicity distribution. That result has been excluded from the originality claim: its \(q=2\) formulas are a benchmark. Goč–Rampersad–Rigo–Salimov (2014 original) provides general-alphabet lattice path encodings (Propositions 11–16) and zero-border enumerations, but not an exact positive-border multiplicity generating function for \(q\ge3\), nor the logarithmic-to-geometric limit-law change. The Fici–Puzynina 2022 survey in Section 6 discusses Abelian borders and earlier exact binary shortest-border enumeration, with no such nonbinary full multiplicity spectrum.

Statement-level comparisons with indexed research records and the available prior work on border-array alphabet ranks show no result entailing the new full \(q\ge3\) formulas. Existing generic random-walk first-return principles are acknowledged as a proof ingredient, not presented as novel. A separate unpublished or unindexed derivation of the same q-ary enumerator or its limits cannot be excluded; this is a material priority risk but no decisive conflicting source was located.

## Value (V): PASS

This completes the natural higher-alphabet extension of an established exact binary border-multiplicity enumeration, for **every word length and every multiplicity**, without restricting to zero borders or finite tables. It exposes a sharp and otherwise hidden dimension threshold: a three-letter word has an unbounded logarithmic number of short Abelian borders with a nondegenerate exponential limit, whereas every fixed alphabet of at least four letters has a geometric limiting border count. This distinguishes two qualitatively different random word models that are not distinguished by binary enumeration or by merely knowing the existence of an Abelian border. It supplies a reusable exact integer-coefficient method and a precise probabilistic law; it is not an arbitrary parameter slice, and does not claim a new general random-walk principle.

## Closest sources and remaining limitations

- Blanchet-Sadri, Chen, Hawes, *Dyck Words, Lattice Paths, and Abelian Borders* (2017), Theorem 3, https://arxiv.org/abs/1708.06461 — exact binary multiplicity law; not the new higher-alphabet result.
- Goč, Rampersad, Rigo, Salimov, *On the Number of Abelian Bordered Words* (original 2014), Propositions 11–16, https://orbi.uliege.be/bitstream/2268/178701/1/numberAbelianBorder.pdf — general-alphabet walk mapping and no-return counts; not a complete all-multiplicity law.
- Fici, Puzynina, *Abelian Combinatorics on Words: A Survey* (2022), Section 6, https://arxiv.org/abs/2207.09937 — background and coverage check.

The result assumes independent uniformly distributed symbols. The exact series need not reduce to a finite product for general \(q\), and unknown unindexed equivalent computations remain possible. Independent mathematical validation is not supplied here.

Self-review: passed. Independent audit: not yet performed.
