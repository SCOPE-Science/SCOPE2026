# Independent mathematical audit

## correctness

PASS

For any one unmarked position its rank in the k+1 values consisting of that position and the marks stays uniform after conditioning on the relative order at the marks. If it lies after j of the marks, its total expected comparisons contributing inversions with the marks are [j(j+1)+(k−j)(k−j+1)]/[2(k+1)]=k/2−j(k−j)/(k+1). Unmarked pairs remain fair and marked pairs lose precisely 1/2 each. This gives the claimed gap law including exterior gaps (j=0,k). All k+1 gap sizes form a weak composition of n−k, so linear optimization gives the exact central-gap equality cases, including the coincident endpoints for k=n. For uniform marks each gap has mean (n−k)/(k+1); the weight sum is k(k−1)(k+1)/6. Averaging produces (3), and tilting by Z/EZ then gives (4). As a separate bounded check, enumeration of all 40320 permutations and all 70 marked sets for n=8,k=4 yielded minimum 39/5 only at (1,2,7,8), maximum 11, and mixture mean 47/5; the counts were exact integers before division. The rank and gap arguments establish the arbitrary-size formulas.

## originality

PASS

The distinct content is the complete dependence of the inversion mean on prescribed marks, with sharp optimal placement and equality conditions. The uniform marked mixture and size-bias identity were already in Pinsky. General mixed-pattern moment methods are relevant to the covariance; the covariance is not treated as a separate novelty claim or as evidence for the sharper positional law.

## value

PASS

Inversions quantify how much ordering remains when a selected subsequence is forced to increase in a permutation otherwise sampled uniformly. The exact all-size formula answers how every forced-position layout changes that observable; all unused positions go in a middle gap to maximize the reduction, while moving them outside the marked interval eliminates their contribution. Pinsky's natural mixture motivates the averaged diagnostic, but cannot substitute for this placement information. The result also works for k growing with n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
