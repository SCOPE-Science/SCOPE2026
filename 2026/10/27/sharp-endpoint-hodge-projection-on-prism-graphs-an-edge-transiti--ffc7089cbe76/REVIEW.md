# Independent mathematical audit

## correctness

PASS

Reconstructed the rail-swap decomposition: the symmetric and antisymmetric Laplacians are L_C and L_C+2I, and the cyclic geometric kernel satisfies the normalized recurrence and sums to 1/2. Applying incidence again gives the two rail blocks I−J/(2n)−G and G−J/(2n), mixed blocks ±DG and rung block 2G. At zero offset 1/(2n)<g_0≤3/10 makes both rail coefficients nonnegative. Away from zero their absolute sum is max(1/n,2g_j), and cyclic variation gives 2(g_0−g_m). The rung norm is 1+4(g_0−g_m). Independent grounded-incidence arithmetic gave (H,V)=(26/15,9/5),(2,2),(202/95,39/19) at n=3,4,5 by forming U(UᵀU)⁻¹Uᵀ after deleting one vertex column. The symbolic inequality H−V≥1−2/n−2(g_0−g_m)>0 holds for every n≥5 and the sign row test attains the operator norm. Rechecked the corrected all-size positive defect 2/n+2g_m+Σ_{j>0} min(1/n,2g_j), then summed its geometric tail beyond the cutoff. The cutoff is floor(β_n) or one larger, and the latter implies phase approaching 1; the phase function matches at the endpoints and gives uniform o(1) error through that rounding. Convexity and the density of logarithmic phases on the circle give the two limits; independent formula evaluation returned 1.89784624322142 and 1.57624426657283. The submitted Python file was inspected but not executed; independent small-size arithmetic is corroboration only. The repaired proof supplies the previously implicit finite-size bound and states the subsequence argument on the circle, so it does not assume convergence of fractional parts to 0 for every choice of nearest integer.

## originality

PASS

For the narrowed explicit phase correction and rail/rung transition. Exact projector entries and finite norms can be recovered from Cinkir's earlier resistance formulas; the repaired result credits this instead of presenting the finite reconstruction as independent novelty. An earlier exact Möbius-ladder rim formula is exponentially close to the prism rail sum and already gives the leading logarithmic term. The corrected full text states the strong overlap and supplies the uniform cutoff analysis, nonconstant phase and its extrema and the specific small-order change of edge orbit. These are the supported distinct parts, not the leading defect or the underlying transfer-current data.

## value

PASS

The contribution identifies which edge types set the worst amplification and resolves the full 1/n scale of its convergence, where just quoting an O(1/n) error hides a genuine oscillation. The sharp limsup and liminf show that no constant second coefficient can replace the phase. This is exact size-sensitive information for a natural graph projection, beyond recovering known resistance entries or reporting the leading logarithmic coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
