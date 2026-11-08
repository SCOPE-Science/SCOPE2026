# Independent mathematical audit

## correctness

PASS

Two pair-read errors require cyclic pair distance at least five between codewords of different information weight. The exact pair-shadow identity d_pair(x,y)=|T∪(T−1)| for difference support T handles ≥4 changed message bits immediately (n≥5). For three changed message bits, suffix difference 101 or 111 gives two additional fresh suffix edges; for two, different weights force ±2 and suffix 010 supplies two fresh edges; for one, suffix 101 or 111 touches four suffix-adjacent cyclic edges and at least one changed prefix edge is outside that set when k≥2. These cases exhaust all pairs. Any r≤2 suffix fails comparing 0^k with a 1 in last information position: all differences lie in ≤3 consecutive positions and touch ≤4 pair reads; k=1 needs total block length ≥5 and 00000/11111 attains it. An independent cyclic pair-distance enumerator checked all unequal-weight message pairs for k=2..9 (106,762 pairs at k=9), with exact minimum five. The infinite-length guarantee rests on the edge argument.

## originality

PASS

Different exact metrics/functions must be distinguished: Ge et al 2025 study ordinary Hamming weight but Hamming channel, Singh–Singh–Yaakobi 2025 study b-symbol read channels with b-symbol weight; Xia–Liu–Chen 2023 develop general pair function correcting codes. A prior general construction COULD imply this ordinary-weight cyclic-pair r=3 special case, but no such implication was established in the inspected full 2023 and 2025 texts. Singh–Singh 2026 full text inaccessible (VPN disconnected), leaving a material priority risk; only abstract available. Best-of-knowledge originality qualified.

## value

PASS

Exact constant redundancy for a basic information statistic under overlapping-read errors is a natural coding-theory design target; three check bits are proven both necessary and sufficient for every k≥2, with an explicit four-periodic systematic encoder. It is a sharp structural guarantee distinct from full-message recovery, not an isolated numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
