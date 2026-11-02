# Review of the two-hub temporal epidemic scheduling theorem

## Correctness

**PASS (self-review).** On a tree each ordered seed-target pair has a unique route; infection reaches it precisely when edge-contact labels increase and all path transmissions succeed. Summing these exact probabilities yields a schedule-invariant distance-one and distance-two baseline, and a distance-three term equal to the number of opposing leaf contacts straddling the bridge contact. The two nonnegative forms \(M=x(b-y)+(a-x)y\) and \(ab-M=xy+(a-x)(b-y)\) prove global extrema with complete equality cases. Direct edge-order permutation counting proves the distribution; pairwise covariances conditioned on the central uniform contact mark prove its first two moments. The package checker reproduced `VERIFY_OK checks=75521`, including independent infection-event simulation for small trees. These tests are finite and do not certify the infinite theorem without its written proof.

## Originality

**PASS under inspected evidence, with historical risk.** The complete 2014/2015 Holme--Masuda temporal-epidemic text motivates the observable but studies empirical networks and does not give an exact diameter-three two-hub distribution. The 2015 De Silva et al. full paper, arXiv:1502.03146, proves increasing-path **length** bounds, not the sum of weighted increasing paths or its random-calendar variance on double stars. The accessible extended text of Deligkas--Potapov 2022 studies different temporal reachability controls (delays and merges); a complete independent comparison with every earlier graph-enumeration result has not been performed. The earlier one-contact path mean-outbreak theorem includes the \(a=b=1\) special case only and cannot furnish the full \((a,b)\) law or variance. Published mathematical-record semantic searches for exact double-star temporal outbreak timing, random edge-order path counts and temporal reachability yielded no identified implication covering the final theorem; a negative search alone is not proof of novelty. Equivalent unpublished or unlocated enumerations remain a risk.

## Value

**PASS.** A two-hub tree is the minimal topology supporting two sizeable communities connected by a single bridge, and precisely represents an interpretable contact-order intervention. The sharp, nonzero calendar effect \(abq^3/n\) is of order \(n\) for balanced hubs, and the exact distribution and variance quantify calendar robustness rather than merely producing an isolated toy example. This supplies a complete mathematical scheduling answer over every possible order, with a clear role for within-community contacts. It does not make clinical or field predictions without additional modeling and data.

## Closest sources and limitations

Holme and Masuda, arXiv:1407.6598 (2014); De Silva et al., arXiv:1502.03146 (2015; full text inspected); Deligkas and Potapov, *Information and Computation* (2022, relevant extended HTML material inspected, not the entire paper). The freely accessible PMC full manuscript of the first source was inspected through its abstract, introduction, data/results, methods, discussion and references. Its empirical finite-duration SIR experiments are distinct from the exact double-star calendar theorem. No complete historical-priority check or independent audit is claimed. Model limitations and the distinction between the calendar-mean variance and realized-outbreak variance are stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
