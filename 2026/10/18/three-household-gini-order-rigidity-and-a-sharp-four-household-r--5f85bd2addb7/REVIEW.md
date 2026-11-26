# Independent mathematical audit

## correctness

PASS

Write G=N/(nS) in the sorted convention with N=sum_{i<j}(z_j-z_i). At n=1 N=0; at n=2 and 3 N is the extreme gap multiplied by 1 and 2, respectively, by cancellation of all intermediate terms. Original majorization with equal totals gives x_1<=y_1 and x_n>=y_n (use the prefix of length n-1 and subtract from the common total). The common monotone map preserves these comparisons, enlarging the gap in f(x) relative to f(y). Concave Karamata gives S(f(x))<=S(f(y)), both strictly positive. Thus the numerator and denominator changes both favor the stated ratio, with ties and flat f allowed. For n=4 the sorted prefix totals of x and y are (1,2,3,6) and (1,2,4,6); raw (N,S) are (6,6) and (4,6), and after the top-code they are (3,5) and (4,6). The resulting reversal is 3/20 versus 1/6. For f(t)=1-8^(-t), f is positive and f'>0>f'' on t>0. From the exact three transformed values, using denominators 512 for x and 64 for y, the (N,S) pairs are (189,1855)/512 and (28,238)/64. The Ginis are 27/1060 and 1/34, with difference -71/18020. This algebra independently checks the exact witnesses; universal preservation does not rely on finite enumeration. The supplied exact-arithmetic checker and recorded verification output were read, not executed. The claim requires original equal totals and the majorization comparison of profiles, not just their untransformed Gini ranking.

## originality

PASS

The credited result is the combined sharp boundary for a single relative Gini coefficient comparing two initially majorized profiles after a common positive nondecreasing concave map. Endpoint cancellation at n<=3 and Karamata are existing ingredients. Impact of top-coding on ordinal inequality rankings is also documented, but the checked evidence does not establish the universal small-n theorem or the sharp first strict reversal under these matched hypotheses. Same-input comparisons, different indices, and data-dependent Winsorization are distinguished below. This judgment is limited by the unavailable full text of the 1994 empirical paper.

## value

PASS

A common top-code or saturating concave rescaling is a natural way to modify incomes. The result identifies exactly when a reversal first becomes possible even with initial Lorenz dominance, and demonstrates it with a strict smooth witness rather than an artifact of a flat cap or noncomparable originals. The mechanistic distinction is useful: an endpoint gap controls the low-dimensional numerator, while at four households interior ranks matter and can overcome the favorable denominator comparison. No empirical prevalence or maximal size is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
