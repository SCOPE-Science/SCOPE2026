# Independent mathematical audit

## correctness

PASS

For the stated reciprocal two-agent, unit-self-weight and no-rate-multiplier model, the gap obeys d'=-2wφ(d)d/(1+w); the mean is conserved. Dividing the logistic equation by 1−w² gives exactly F'(d)d', so C=artanh(w)−F(d) is constant. Positivity and strict finite-time bounds follow from the multiplicative ODE factors; d=2 is inward-pointing, not an invariant face as the blanket wording in the proof suggests. The decreasing gap has a limit, and the weight has a limit because its derivative changes sign at most once. A positive limiting gap forces w→0; d→0 forces w→1 by logistic comparison. F decreases to its unique minimum 0 at r, increases thereafter, and diverges at zero. For d0>r, C<0 forces stagnation at the unique right-branch root F(d∞)=−C, C=0 forces approach to r from above, and C>0 forces a crossing below r and hence consensus. For d0≤r the tie increases once d<r, so consensus follows. Writing a=−φ'(r)>0 gives F(r+z)=(a/r)z²+O(z³) and z'=−az²+O(z³), so (1/z)'→a; the two critical limits and both logarithmic off-critical rates follow by time averaging. The exponential example also differentiates correctly. The rational-kernel checker comment at line 66 misstates F''(1), which is 1/2, not 1/4; the latter is the quadratic Taylor coefficient and the checked formula and theorem use the correct value.

## originality

PASS

Pass for the exact initial-data basin partition and critical coefficients in the frozen general-kernel model, as of its recorded publication. The closest primary antecedents establish the same model and a qualitative clustering alternative, not the invariant, phase boundary, or rates. There is demonstrably equivalent indexed content in a distinct subsequent general-kernel entry, and substantial special-case coverage in another subsequent entry. Neither supplies evidence of earlier coverage of this frozen record; these comparisons do not establish independent discovery, lineage, or absolute priority.

## value

PASS

In the motivating minimal reciprocal network, the instantaneous sign of the tie derivative does not determine whether initially disagreeing agents ever establish consensus. The exact initial-trust criterion, limiting positive gap and anomalous critical rates answer that model question and give a benchmark for simulations and network approximations. This is more than asserting that a separable planar reduction exists; the parameter-uniform limits are the useful result. No value is claimed for a larger-network inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
