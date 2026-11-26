# Independent mathematical audit

## correctness

PASS

At fixed n and weight three, (a,b,c) are precisely the ordered counts of zeros before each one. Directly counting the patterns with one selected one gives 001=Q, 010=(z-1)S-2Q, and 100=3 binom(z,2)-(z-1)S+Q. Counting those with two selected ones gives 011=T, 101=2(c-a)=2(S-T), and 110=3z-2S+T. The single-symbol counts and pure patterns are fixed, and S is 01; indeed the exact length-three deck also determines S via S=011+101/2 in this layer. Fixing S,T leaves b=T-2a, c=S-T+a; equality of Q requires equality of the sum of squares, a quadratic with nonzero leading coefficient 6. Its other root shifts a by (u-v)/3 for gaps u=b-a and v=c-b, swapping the gaps. Unequal gaps, integrality and the endpoints give the unique orientation v=u+3t, with t>=1, a>=t, a+2u+3t<=n-3; zero gaps are allowed and equal gaps give no distinct partner. Writing a=t+j and allowing the remaining endpoint slack h>=0 gives n=7+2u+4(t-1)+j+h, yielding the stated count and generating function. Its pole at 1 gives n^3/48+O(n^2), and it is the fraction of words in doubletons, 2C(n)/binom(n,3), that tends to 1/4. The author-recorded finite dynamic program was inspected but not executed; it is not needed for the all-length proof.

## originality

PASS

The distinct contribution is the proof of the all-length formula and the exact singleton/doubleton classification, not proposing the formula, identifying the first collision, or finding the nullspace direction. The frozen literature discussion misses a direct antecedent: Chrisnata et al. explicitly analyze weight-three gaps and conjecture the exact profile-count generating function in §5.3, Conjecture 1. That attribution should be corrected in any public exposition. Their published conjecture and initial coefficients do not establish the classification or the all-length formula. Several later indexed records prove the same result; their catalog dates do not show priority over the frozen record.

## value

PASS

The theorem settles a specific published fixed-weight deck-enumeration conjecture and shows exactly which sparse inputs fail unique reconstruction, not just how many decks exist. Weight three is the first potentially ambiguous layer, and the quarter-density result quantifies its ambiguity in a natural low-depth observation model. These are substantive consequences of the classification, not claims about arbitrary weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
