# Same-model review

## Correctness
PASS. Fu--Li Theorem 4.4 reduces \(MS_B\) on a polyhedral Radon plane to the largest norm distance between Birkhoff-orthogonal extreme points. The regular \(N=4m+2\) polygon is Radon because a quarter-turn of its polar is exactly \(\cos(\pi/N)\) times the primal polygon. At a fixed vertex, the two adjacent norming facets leave only two orthogonal vertex indices modulo sign. Their chord directions differ in parity, so one receives a facet-normal factor \(1\) and the other a vertex-ray factor \(\cos(\pi/N)\). The longer chord is proved strictly larger in both parity cases, giving the stated modulo-\(8\) formula. The bundled enumerator independently checks every vertex pair for \(1\le m\le100\).

## Originality
PASS. The defining Fu--Li full text was inspected through Theorem 4.4 and the subsequent explicit computations. It supplies the Radon-plane reduction but computes the conjugate Day--James family rather than regular polygonal Radon planes. Searches covered \(MS_B\), the Massera--Schäffer name, regular-polygon and decagon aliases, the golden-ratio specialization, and the trigonometric branch formula. No covering statement was found. The current own ledger through generation g000054 was also checked and contains no Massera--Schäffer finding.

## Value
PASS. The regular \(4m+2\)-gons are the canonical polygonal Radon family, precisely the setting in which Fu--Li turn \(MS_B\) into an orthogonal-chord invariant. The exact formula exposes a genuine modulo-\(8\) geometric effect and gives the regular decagon the golden-ratio value. It also supplies an infinite benchmark family converging to the Hilbert value \(\sqrt2\).

## Closest literature and limitations
Fu and Li introduced \(MS_B\), proved \(\sqrt2\le MS_B\le2\), and established the exact Radon-plane and polyhedral extreme-point reductions in Filomat 38 (2024), no. 15. Their explicit Radon-plane computation concerns \(\ell_p-\ell_q\). The theorem here is restricted to Euclidean regular polygons with \(N\equiv2\pmod4\), and it does not classify arbitrary polygonal Radon planes or every maximizing pair. The exact public day of the 2024 Filomat article was not asserted; the recorded first public date comes from the exactly dated 18 November 2022 orthogonality survey used for the Radon-plane framework.

Same-model review: passed. Independent audit: not yet performed.
