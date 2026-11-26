# Independent mathematical audit

## correctness

PASS

The state (a_n,a_(n+1),a_(n+2)) advances by the stated integral matrix M of determinant one, so back substitution reaches w_(−4)=(−1,0,1). Multiplication gives M^7=I+2C and M^14=I+4B as displayed, with first coordinates of Cw_(−4) and Bw_(−4) equal to 1 and 5. For n=7s−4, odd s gives (a_n+1)≡2s mod 4. For s=2m>0, the j≥2 terms in (I+4B)^m are divisible by 2^(ν₂(m)+3) since binom(m,j)=(m/j)binom(m−1,j−1) and 2j−ν₂(j)≥3. Thus the leading 20m fixes the exact valuation. For all other branches the period of the state modulo 4 divides 14; the extra residue 5 mod 14 has valuation 2 because the first coordinate of Bw_5 is the even integer 148, fixing a_n+1≡4 mod 8. This exhausts all n≥0 and gives the stated counting classes: periods 14,14,28 at 0,1,2 and one progression of modulus 7·2^t at each t≥3. A single class has error strictly less than one. Enumerating the three short prefix periods gives ranges [−5/7,4/7], [−3/7,9/7], [−15/28,6/7]; the witness N=4,t=1 attains 9/7. Independently computed 4001 exact terms, valuations and prefixes confirm these checks (python -I /workspace/branches/independent_checks.py 1). Frozen VERIFICATION.md and verify.py were inspected, not executed. The infinite result rests on the matrix congruence and complete period argument, not on the diagnostics.

## originality

PASS

The same shifted terms have a prior prime-three theorem, and the same prime has prior unshifted lower bounds and a same-day exact unshifted law. These do not cover the shifted binary valuation. A later same-normalization isometry does imply the nonperiodic branch after centering it using the reversible recurrence, as shown below; it is not prior coverage, and does not state the sharp shifted prefix count. The exact level law and its joint sharp discrepancy survive the statement-level comparisons. This judgment is relative to the inspected evidence.

## value

PASS

Shifted p-adic laws for this particular natural recurrence are motivated by the known prime-three case and by Diophantine applications of valuations. The infinite binary law reveals a unique index branch supporting arbitrarily high levels, establishes exact level frequencies, and gives the optimal uniform prefix error over all levels and cutoffs. The last conclusion is exact distributional information rather than a tightening of a fitted finite estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
