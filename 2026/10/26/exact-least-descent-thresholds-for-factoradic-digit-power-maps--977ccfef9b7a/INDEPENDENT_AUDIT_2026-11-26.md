# Independent mathematical audit

## correctness

PASS

For i<j=j_r the maximal digit i makes i^r−i·i!≥0; convexity of the excess d^r−d·i! makes this endpoint a maximizer. Therefore every block with j-th digit a and no higher digits has maximum excess exactly P_r+a^r−a·j!, attained with all lower digits maximal, at (a+1)j!−1. The case a=0 ensures a_r exists, and only the largest a with nonnegative maximum is needed (no monotonicity in a is assumed). Thus C_r−1 is a witness and all later numbers below (j+1)! descend. When a_r=j that intermediate range is empty. I checked that Sánchez Garza–Treviño, Theorem 1, covers the entire range n≥(j+1)! with the same crossing index and digit convention; starting its crossing search at i=1 makes no difference. The arithmetic proof of the cited bound was also checked: the last integrality sentence of their Proposition 11 would not by itself imply a strict inequality, but their displayed bound has positive margin when r≥2168 and the finite range through 2167 was independently checked. Separately, an independent proof of the needed high-range bound is as follows. Since r−1<j and j≥3, for every i≥j the ratio i!/i^(r−1) grows by a factor greater than (i+1)/e each step. For i≥j+1 we have i^(r−1)/i!<e/(j+1), so the loss d·i!−d^r is, for positive d≤i, at least i!−1: by concavity minimize at d=1 or i, and at d=i the loss exceeds (j+1−e)i!>i!. Thus a single high nonzero digit suffices if P_r<(j+1)!−1. For j≥100, applying the integral lower bound for log((j−1)!) and minimality of j gives r−1≥(j−1)(1−1/log(j−1))>3j/4. Hence Σ_{i<j}i^r≤j^r Σ_{k≥1}exp(−3k/4)<j^r<j·j!, which bounds P_r as needed. For each 3≤j<100 my exact script checked P_r<(j+1)!−1 at the largest integer r allowed by j^(r−1)<j!; this bounds P_r for all smaller r with that same j. The script also reproduced all eight example cutoffs and exhaustively recovered the last failure below (j+1)! for r=2…6.

## originality

PASS

The covered result is a uniform sufficient upper threshold at (j_r+1)!, including the lower-digit sum used in the earlier inequality proving that bound. The distinct claim computes the least bound and supplies the actual last witness for every exponent, using an attained maximum conditional on the top digit rather than just an estimate above the sufficient threshold. The strongest available prior statements did not give that optimization.

## value

PASS

Least universal one-step descent is a natural invariant of these maps: it gives the exact maximum range that must be retained when reducing large inputs by descent. The endpoint witness proves no smaller such range is valid; the loss from using the previous sufficient cutoff is real even at r=3 (120 versus 24). The formula applies to every integer exponent and reduces a search over inputs to finitely many top digits with exact maxima, rather than reporting a numerical table or a bounded experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
