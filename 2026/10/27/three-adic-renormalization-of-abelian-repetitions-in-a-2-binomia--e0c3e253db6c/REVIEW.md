# Independent mathematical audit

## correctness

PASS

For every k, the repeated central choice is the unique residue p=(3^k-1)/2 not fixed by the last k ternary digits. The other residues pair by digit complementation and contribute p ones in every length-3^k interval, aligned or not. The central position has index 3^k ceil((i-p)/3^k)+p, and shifting the start by j*3^k adds j to the decoded index. Any three consecutive decoded letters include a fixed 0 and a fixed 1. The equality coding is (1-z_r,z_r,0), so each aligned triple of indicators contributes exactly one square. Repeating each decoded index 3^k times apart from bounded ends preserves its density for fixed k. For the letter density, D(N)=2 sum_{a<N} z_a-N satisfies D(3r)=D(r), D(3r+1)=D(r)-1, D(3r+2)=D(r)+2z_r-2, giving D(N)=O(log(N+1)). The k=0 case is the letter-level identity. This proves the all-start and all-scale claims. The supplied checker was inspected, not executed; its bounded tests do not prove the density or the universal claims.

## originality

PASS

The word and its 2-binomial-cube avoidance are prior. The supported distinct contribution is the arbitrary-offset exact Parikh-window law and its Abelian repetition and frequency consequences at substitution scales, not the construction or any unrestricted Abelian-cube claim.

## value

PASS

This is a naturally motivated exact invariant of an established avoidance word: an arbitrary-offset renormalization specifies both possible Parikh classes, all square positions at infinitely many natural scales and their frequency, and excludes every triple at those scales. It answers a weaker-equivalence question left open by the stricter avoidance theorem, rather than just enumerating a prefix or treating a hand-picked scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
