# Scientific review: exact worst-mixing shuffle enumeration

## Correctness — PASS

The claimed domain is all odd integers \(N\ge3\), with equal-interval translations after the doubling map. The existing transfer-matrix reduction is taken from Byott--Holland--Zhang and its specific \(m=2\) conjugacy is independently calculated in the proof. On the mean-zero space the symmetric circulant has a unique top singular Fourier plane, and equality in the spectral norm forces a permutation eigenvector to lie in that plane. The proof then exhausts nonreal, fixed, and sign-reversed Fourier eigenvectors. Regular-polygon rigidity, the exact sampled-cosine equality classes, and an odd-moment power sum exclude other cases. The pair-swap stabilizers intersect only in the identity, establishing the full count. This is an analytic all-odd-\(N\) proof, not an inference from finite enumeration.

The actual included `verify.py` was run and returned `VERIFY_OK`. It checked all \(3!+5!+7!\) permutations at those sizes and 500 further seeded samples at \(N=9\), including the explicit similarity of the two matrices and agreement of the extremal classifications. Floating-point eigenvalue comparisons have a stated tolerance and are corroboration only.

## Originality — PASS

The original 2012-03-22 source (arXiv:1203.5145) explicitly provides the sharp **value** of the worst mixing rate, the Markov matrix reduction, and examples realizing the extremal eigenvalue locations; its Conjecture 2.4.1 asks for restrictions on the outer-circle spectrum. The inspected full paper's main statements and extremal-value proof do not classify/count all maximizing permutations. Its 2014 sequel (arXiv:1405.0481) extends the sharp value to non-coprime slopes and other branch orientations but its inspected statements/proofs likewise do not present the equality-case count. The new result is strictly finer than the known maximum value and includes a special-case resolution of the conjectured outer-circle locations.

The searchable mathematical-results database was queried for the object, exact optimizer count, Fourier aliases, and the outer-circle conjecture; no equivalent implication or stronger encompassing result was recovered. Accessible own earlier claims were compared and no matching shuffle-optimizer theorem was found. Such a search does not certify priority. A possible unindexed counting argument is the residual originality risk.

## Mathematical value — PASS

Complete classification of **all** worst-mixing protocols, not merely existence of one, is a natural structural refinement of a sharp spectral-mixing theorem and of an explicit conjecture about the associated eigenvalue geometry. The quantity \(N2^{(N-1)/2}\) is the exact natural count across an infinite family, exposing non-dihedral partial reflection symmetries missed by the standard circulant extremizers. It also gives the exact probability that a uniformly chosen shuffle is worst-mixing. This is a nontrivial equality-case theorem, not a routine parameter substitution or a numerical gain.

## Closest sources and limitations

The closest scientific antecedents are Byott--Holland--Zhang, *On the mixing properties of piecewise expanding maps under composition with permutations*, arXiv:1203.5145 (2012), particularly Theorem 2 and Conjecture 2.4.1; and Byott--Lin--Zhang, *On the mixing properties ... II*, arXiv:1405.0481 (2014), particularly Theorem 4. The transfer spectral reduction and maximal mixing-rate magnitude remain credited to those works. The new proof only covers the doubling slope with odd cell count and does not resolve the general higher-slope conjecture or rule out unindexed earlier priority.

Self-review: passed. Independent audit: not yet performed.
