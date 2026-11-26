# Independent mathematical audit

## correctness

PASS

Condition on T and write x_v=2^(-d_v). Distinct nonadjacent indicators have product probability x_u x_v. On an edge a source–sink pair has probability 2x_u x_v, a same-type pair has probability zero, and no vertex can be both. The Prüfer word gives means a_n/2 and distinct-pair weights b_n/4. To check the incidence factor, use product edge weights z_i z_j, equivalent to the Prüfer tilt up to a common factor. In trees containing uv, contract it: incident connections from the merged vertex have combined weight (z_u+z_v)z_j and the forced edge contributes z_u z_v. The weighted tree totals before and after contraction give ratio (z_u+z_v)/∑z_i, or 1/(n−1) at the two half-weights. Ordered-pair summation gives n²b_n/4 for the mixed moment and n(n−2)b_n/4 for the factorial moment. At n=2 both counts are one; otherwise the base for a_n² exceeds that for b_n by 1/(4n²). The covariance and variance per n from the expansions are −1/(16e) and (8√e−9)/(16e); finite variances are nonzero for n≥3. On the path, the diagonal sum is 1/2+(n−2)/16 and the unordered edge sum is 1/4+(n−3)/16, giving (n−4)/16. The finite checker was inspected, not rerun; it is supplementary to these identities.

## originality

PASS

The supported distinct claim is the explicit joint-moment and sign/correlation comparison for independently fair orientations of uniform Cayley trees versus a fixed path, not the Cayley enumerator or generic edge-pair calculation. The inspected literature did not establish earlier equivalent aggregate coverage. Later indexed statements materially overlap, and their dates warrant no inference of independent discovery or authorship.

## value

PASS

In a canonical random directed tree, the exact joint moments determine both a strict finite-size aggregate sign and a nonzero limiting correlation. The positive covariance on every sufficiently long path is a motivated contrasting fixed-shape family and prevents interpreting the aggregate sign as a local or shape-independent rule. The precise effect is useful beyond a finite check without requiring a full joint law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
