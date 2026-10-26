# Review of the balanced multipartite majority recurrence formula

## Correctness

PASS. The graph neighbourhood of every vertex in a part is identical. With \(t_i\) ones in part \(i\), \(T\) ones globally, and half-degree \(h=(r-1)s/2\), the three possible updates of that part depend only on the sign of \(T-t_i-h\). On a periodic state every nonhomogeneous part must tie at every step, and all such parts therefore have a common count \(t\). Since all homogeneous groups flip under \(0<t<s\) and global one-count remains constant, their full and empty numbers must be equal; the residual equation is \((k-1)(2t-s)=0\). This exhausts the recurrent states, giving the labelled coefficient and the one-mixed-part correction. The two unanimous states and the fully mixed half-filled states are exactly the fixed configurations. A separate complete case argument establishes \(\(F^5=F^3\)\), and the stated example shows that entry time three is attainable. Standard Stirling and Laplace estimates supply the asymptotics. Two computational formulations independently checked 167,116 labelled states for 20 parameter pairs and the time-three identity on each; this does not replace the proof.

## Originality

PASS, bounded by available sources. Goles–Olivos established only the generic at-most-two eventual period, which is acknowledged. Benjamini et al. (arXiv:1405.2486v1) study majority dynamics on infinite and random graphs, and their accessible full paper contains no balanced multipartite all-parameter census. Turau (arXiv:2202.01580) gives tree-specific fixed and two-cycle classifications. An existing exact complete-tripartite note covers the case of three parts, which the formula reproduces and does not claim as independently new. A published static majority-C-coloring result already identifies the central-binomial fixed-state family but does not, on the accessible summary, cover the dynamic two-cycle census. The general even/odd number-of-parts correction, its asymptotics, and the sharp uniform transient bound require a genuinely additional argument. No available source was found to imply the entire result. The classical 1980 full text and the static C-coloring full record were unavailable in this check, and an unindexed equivalent remains possible. Absence from an index is not a guarantee of novelty.

## Mathematical value

PASS. The attractor census is a natural invariant of parallel opinion dynamics on the symmetric regular multipartite family. Complete two-parameter formulas and a sharp global entry bound identify precisely how tie-retained mixed parts store information or support oscillation. For odd part size \(s\ge3\), switching the parity of the number of parts changes the power of \(r\) multiplying \(2^r\); for even part size the leading exponential base increases to \(C_s+2\). This qualitative phase mechanism is not a mere evaluation of a small table, and allows exact comparisons of persistence and recurrence density across infinitely many networks.

## Boundaries and sources

The proof excludes unequal part sizes, randomized/asynchronous updating and alternative tie rules. It does not derive attraction-basin counts or a sharp entry bound separately for every parameter pair. The closest sources are Goles and Olivos (1980), DOI:10.1016/0012-365X(80)90121-1; Benjamini et al., arXiv:1405.2486v1; Turau, arXiv:2202.01580; a documented earlier exact tripartite claim; and the published static majority-C-coloring record (2026-10-04). The latter two have partial substantive coverage, expressly excluded from the novelty claim. Independent specialist verification and publication-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
