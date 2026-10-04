# Local maxima determine temporal zero forcing on injectively timed paths
## Finding
Let \(\mathcal P\) be the temporal path \(v_0v_1\cdots v_{n-1}\), where \(n\ge2\). Edge \(e_i=v_{i-1}v_i\) is active in exactly one snapshot, and the \(n-1\) activation times are pairwise distinct. Because only their order matters, write \(t_i\in\{1,\ldots,n-1\}\) for the rank of the activation time of \(e_i\).

Define the strict-peak set
\[
M=\{i:2\le i\le n-2,\ t_{i-1}<t_i>t_{i+1}\}.
\]
Split \(M\) into maximal chains in which consecutive indices differ by \(2\), and let their lengths be \(r_1,\ldots,r_q\). Then
\[
\operatorname{TZ}(\mathcal P)=1+\sum_{j=1}^q\left\lceil\frac{r_j}{2}\right\rceil.
\]
Equivalently,
\[
\operatorname{TZ}(\mathcal P)=1+\min\Bigl\{|C|:C\subseteq\{1,\ldots,n-1\},\ C\cap\{i-1,i,i+1\}\ne\varnothing\text{ for every }i\in M\Bigr\}.
\]
In particular,
\[
\max_{(t_1,\ldots,t_{n-1})}\operatorname{TZ}(\mathcal P)=\left\lfloor\frac{n+2}{3}\right\rfloor,
\]
where the maximum is over all permutations of \(1,\ldots,n-1\). One extremal timing is obtained by concatenating the rank blocks \((1,3,2),(4,6,5),(7,9,8),\ldots\) and then appending any remaining one or two ranks increasingly.

## Assumptions and scope
Temporal zero forcing is the synchronous snapshot process of Baste, Dreyer, Marcille, Rabie, and Toullec-Streicher: in each snapshot, every already corrupted vertex having exactly one uncorrupted neighbor in that snapshot corrupts that neighbor, and vertices corrupted in one snapshot can act only in later snapshots. The theorem is restricted to paths in which every underlying edge has exactly one activation and no two edges share an activation time. It makes no claim for repeated activations, tied activation times, or other temporal-zero-forcing conventions.

## Proof
Because every snapshot contains one edge, an active edge transmits precisely when exactly one of its endpoints is corrupted before that snapshot. Suppose a forcing set has \(s\) seeds. Every one of the \(n-s\) nonseed vertices must be newly corrupted across a distinct one-shot edge. Hence exactly \(n-s\) path edges transmit, leaving exactly \(s-1\) unused edges. Deleting those unused edges partitions the underlying path into exactly \(s\) components. Every such component must contain a seed, and there are exactly \(s\) seeds, so each component contains exactly one seed.

Consider one retained path component. If its unique seed is an internal vertex, the edge times must increase strictly while moving away from the seed in either direction: an edge farther from the seed cannot transmit before the nearer edge has corrupted its inward endpoint. Reading the component from left to right, its retained edge-time word therefore strictly decreases to the seed and then strictly increases. The endpoint-seed cases are the two monotone degeneracies. Conversely, any such valley-shaped word is forced completely from its valley vertex, or from the appropriate endpoint in a monotone component. Thus a cut set \(C\) of unused edge positions is feasible exactly when every resulting edge-time block has no strict interior local maximum.

A strict peak at position \(i\) remains an interior peak unless one cuts at \(i-1\), \(i\), or \(i+1\). Therefore feasible cut sets are exactly the hitting sets of the integer intervals \(\{i-1,i,i+1\}\) for \(i\in M\), and \(\operatorname{TZ}=1+|C|\) for a minimum such hitting set.

Two strict peaks cannot be adjacent. Their three-position neighborhoods intersect exactly when their indices differ by \(2\). Hence the overlap graph of the peak neighborhoods is a disjoint union of chains. In a chain of \(r\) peaks, one cut can hit at most two consecutive peak neighborhoods, while cutting at the shared position of each consecutive pair, plus one endpoint-neighborhood position when \(r\) is odd, hits them all. Its exact contribution is therefore \(\lceil r/2\rceil\), proving the formula.

For the extremal statement, interval stabbing on a line shows that the minimum hitting-set size equals the maximum number of pairwise disjoint peak neighborhoods. Such neighborhoods have centers at least \(3\) apart and their centers lie among \(2,\ldots,n-2\), so at most \(\lfloor(n-1)/3\rfloor\) can be disjoint. The block timing \((1,3,2),(4,6,5),\ldots\) has peaks at positions \(2,5,8,\ldots\), whose neighborhoods are pairwise disjoint, attaining that number. Adding the single initial seed gives \(1+\lfloor(n-1)/3\rfloor=\lfloor(n+2)/3\rfloor\).

## Verification
The proof above is symbolic and does not rely on computation. The accompanying verifier independently simulates the snapshot process for every permutation of edge times for paths with \(2\le n\le9\). For every timing it exhaustively searches seed sets by cardinality, independently computes the minimum three-position peak-hitting set, and compares both values with the closed formula. It checks all \(46,233\) timing permutations and also verifies the extremal value and an explicit block witness at every tested order. The recorded output is:

```text
ALL CHECKS PASSED
permutations=46233
seed_sets_tested=1992563
maxima=n=2:TZ=1:witness=1;n=3:TZ=1:witness=1,2;n=4:TZ=2:witness=1,3,2;n=5:TZ=2:witness=1,3,2,4;n=6:TZ=2:witness=1,3,2,4,5;n=7:TZ=3:witness=1,3,2,4,6,5;n=8:TZ=3:witness=1,3,2,4,6,5,7;n=9:TZ=3:witness=1,3,2,4,6,5,7,8
```

## Relationship to prior work
Baste et al. introduced the synchronous temporal-zero-forcing problem used here and established hardness and algorithmic results, including polynomial solvability on bounded-degree temporal trees. Their inspected paper does not state an exact formula for one-shot injectively timed paths. The present theorem specializes their model to the sparsest connected underlying graph and converts the process into an exact local-maximum hitting formula.

A separate public project by Krishna Harish describes layer-local and footprint-constrained temporal-zero-forcing variants and advertises exact values for alternating paths and even cycles. Its publicly indexed README is therefore a directly relevant comparison. The statement proved here concerns the synchronous model of Baste et al. and arbitrary injective one-shot timings, not only an alternating-path schedule. The complete project manuscript was not available from the inspected public endpoint, so overlap on that advertised special family remains a stated literature risk rather than being inferred away.

## Limitations
The theorem does not cover simultaneous edge activations, edges that reappear, temporal walks with waiting conventions different from the synchronous corruption rule, or nonpath underlying graphs. The finite verifier is only a stress test through \(n=9\); the all-order statement rests on the cut-and-valley proof. The closest inaccessible manuscript may contain additional path statements beyond what its public README advertises, so a later full-text comparison could refine the originality assessment.

## References
1. Julien Baste, Simon Dreyer, Clara Marcille, Mikaël Rabie, and Ronan Toullec-Streicher, “Zero Forcing Sets in Temporal Graphs,” arXiv:2609.29054, first public version 2026-09-24.
2. Krishna Harish, “Zero forcing on temporal graphs: Layer-local and footprint-constrained dynamics,” public software/manuscript project, version DOI 10.5281/zenodo.21347118; public README advertises exact values for alternating paths and even cycles.
