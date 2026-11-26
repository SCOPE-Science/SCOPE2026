# Independent mathematical audit

## correctness

PASS

Each unit chore adds one to load and total share, hence the discrepancies sum to zero, and Prop1 is exactly max discrepancy <=1. An empty bundle has nonpositive discrepancy; a singleton eligibility simply leaves the discrepancy vector unchanged. An independent Fraction-based enumeration on permutation orbits (python /workspace/checks/1.py, output /workspace/checks/1.txt) constructs the closed greedy class for n=1,2,3, checks every entry of the three-agent transition table, and includes every eligible subset and tied choice. Closure starting at zero proves the all-horizon result. At n=4 the depth 0–4 nonsingleton orbit counts 1,3,14,43,87 give labeled counts 1,28,187,617,1405 by permutation multiplicities and maxima 0,3/4,3/4,1,1. Deleting singleton chores transfers this to every four-arrival prefix. In units of 1/12 the adaptive obstruction forces sorted states (-3,-3,-3,9) and (-7,-7,5,9), then either immediate failure with 13 or (-11,1,1,9); choosing the equal pair forces (-11,-5,7,9), then choosing the two positive agents forces a 13 or 15. The all-response minimax calculation independently confirms the first loss at 5 for four agents. For n>=5 two full sets either overload the same recipient or produce two distinct recipients, whose subsequent pair share is 2/n+1/2<1. No n can be forced to fail in two arrivals: use a different recipient when possible; otherwise the first recipient's singleton share alone pays for load minus one. The textual 'self-review' in RESULT.md line 74 is a typo for 'same agent', unambiguous from the stated load and the next sentence. The packaged checker was inspected, not executed.

## originality

PASS

Supported distinct contribution at the frozen October 26 publication is the sharp four-agent cutoff together with the all-horizon three-agent guarantee, not the discrepancy-greedy ordering itself or the general targeted-adversary idea. There IS a separately indexed record stating the same complete theorem, with a November 8 publication date. It is equivalent coverage in the present catalogue, not evidence of earlier publication than the frozen record. No order of derivation or independence is established. The verified earlier primary literature and earlier restricted-family catalogue result do not imply the two exceptional small-population cases.

## value

PASS

The exact population threshold and the four-agent failure at five rather than three pin down when a natural exact fairness benchmark can be promised at every prefix. The finite cutoff separates a genuinely perpetual guarantee from delayed impossibility and provides a useful test of stronger eligibility-aware online fairness claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
