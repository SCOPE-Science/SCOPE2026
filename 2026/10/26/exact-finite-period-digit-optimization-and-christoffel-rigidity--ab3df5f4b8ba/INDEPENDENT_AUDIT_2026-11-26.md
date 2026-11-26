# Independent mathematical audit

## correctness

PASS

Huang–Jenkinson–Xu–Zhang's bound S_n≤nα+1 applies to the same lexicographic shift. For a q-periodic point, taking n=Nq and then N→∞ bounds its q-block count by floor(qα). For r=floor(qα)/q, the upper mechanical repetition has q-block count qr, and any shifted prefix of length k has at most ceil(kr)≤ceil(kα) ones by the ceiling difference. At a first lexicographic exceedance the prefix count would instead be greater, so every shift is admissible. For rigidity, the needed fixed-content cyclic comparison can also be derived directly: for a word of weight p rotate after a minimum of the periodic cumulative deviation S(j)=number of ones in the first j digits−jp/q. All resulting prefix counts are at least ceil(kp/q), making that rotation lexicographically at least U(p,q); equality of the q-word means that the original word is a rotation of U. In the strict lower approximation window the ceilings at k=1,…,q−1 are unchanged because their next integer is at distance at least 1/q and k(α−p/q)<1/q. A strictly greater equal-weight rotation must differ before the last symbol, so it exceeds the irrational cap, a contradiction. Coprimality gives least period q and q distinct rotations; the infinitely many lower convergents eventually satisfy all hypotheses. For q=1 or p=0, the all-period optimum is the zero fixed point. The frozen bounded verifier was inspected, not executed; its finite prefix tests are not used as an infinite admissibility certificate.

## originality

PASS

The prior discrepancy bound, the existence and defect of selected return loops, and fixed-content Christoffel order are already known. Credit the all-q optimizing construction together with the exact dynamical rigidity criterion, not those ingredients. The strongest inspected same-system work does not supply both the optimizing orbit at arbitrary lengths and exclusion of every competing maximizing orbit in the lower-rational window.

## value

PASS

Fixed-period optimization for the same observable studied in global ergodic optimization is a natural constraint. The answer gives the exact unavoidable deficit at every q and constructs an attaining orbit even at lengths not supplied by the known first-return calculation. The rigidity theorem identifies when approximation by a short rational word forces uniqueness, and gives infinitely many such periods for each slope. That is a useful dynamical conclusion beyond the classical cyclic ordering or the known limiting optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
