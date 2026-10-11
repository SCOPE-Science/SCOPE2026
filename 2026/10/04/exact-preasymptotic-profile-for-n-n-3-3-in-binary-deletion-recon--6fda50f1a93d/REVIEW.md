# Independent mathematical audit

## correctness

PASS

For equal-length binary words, \(d_L(x,y)\ge3\) is equivalent to disjoint two-deletion balls: a common subsequence using at most two deletions can always be shortened to length \(n-2\), and conversely a common length-\(n-2\) word witnesses distance at most two. Thus exhaustive enumeration of all unordered word pairs is an exact proof for each finite length. A fresh independent implementation regenerated the complete values \(2,4,6,8,11,15\) for \(n=4,5,6,7,8,9\), with numbers of maximizing pairs \(2,1,4,7,4,2\) and total eligible-pair count 94949, matching the package. The published diagonal theorem supplies the universal upper bound twenty and a matching construction for every \(n\ge4t-2=10\); the stated length-ten witness also directly has twenty common three-deletion outputs. Hence the finite exhaustive prefix and published infinite tail meet exactly at ten.

## originality

PASS

Pham, Goyal and Kiah define exactly \(N(n,\ell,t)\), state that before their work exact values were known only for \(\ell\in\{1,2\}\), and prove the diagonal value \(\binom{2t}{t}\) once \(n\ge4t-2\). For \(t=3\) that gives the prior tail \(20\) from length ten onward but says nothing about the six shorter values. Their paper gives a conjectural general exact framework rather than the audited finite table. Current Resultary and web searches for \(N(n,3,3)\), the values eleven/fifteen and preasymptotic deletion-ball intersections did not reveal a published table filling lengths four through nine. The finite prefix therefore survives the closest full-text comparison.

## value

PASS

This finite computation sits exactly below the first published stabilization threshold for the first previously unknown diagonal case \(\ell=t=3\). Completing all six missing lengths establishes that the sufficient threshold ten is sharp and gives a complete all-length profile. That is a meaningful finite cutoff problem, not an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
