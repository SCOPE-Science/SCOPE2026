# Independent mathematical audit

## correctness

PASS

Reconstructed the universal proof, not just the low-prime enumeration. Split the six distinct low-index cyclotomic factors into A from (X−1,X+1,X²+1) and B from (U,U_−,V). The ℓ¹ norm of every A is ≤4, and the residue-slice norm of AB is bounded by a convolution with |A|'s coefficient weights. Six B-products (including 1) have at most one coefficient ±1 per residue, using UU_−=ΣX^(2j), UU_−V=ΣX^(4j) and odd q. X→−X reduces the other choices to B=UV. Factors X−1 and X²+1, when present, telescope with U and V respectively, giving the stated slice bound (in the both-present case four terms in residue zero, with an optional disjoint copy in residue one). UV itself is flat by the alternating consecutive-index coefficient formula, with at most three slots per residue. For W=(1+X)UV and q=2k+1, each middle-block coefficient (q≤n≤2q−1) has k+1 alternating summands with exactly one endpoint of weight one and all other weights two. Its absolute value is 1. In the low block n<q, the magnitude is 1 at even n and at most 2 at odd n. Reciprocity about degree 3q−2 pairs the outer coefficients of residue r≤q−2 with low indices r and q−2−r, of opposite parity, proving 4; the final residue has only two slots. The argument includes q=3. The three q²-index factors are precisely U,U_−,V evaluated at X^q by cyclotomic factorization; their subset products are flat before substitution. In each output coefficient the lifted factor can then draw only from a single slice of F, proving height ≤4. The proposed witness divides as the specified four distinct factors, and its coefficient of X³ is 4. Inspected verify.py and VERIFICATION.md but did not execute the frozen script; the finite checks are not needed to establish the quantified bound.

## originality

PASS

The established lower bound and proposed witness are prior work. The all-prime upper bound in the p=2 specialization and the uniform residue-slice lemma are the distinct contributions supported by the comparison. Neither a different exponent family nor a degree statistic at the same exponent constitutes coverage of height. The bounded search does not certify priority.

## value

PASS

Resolves a uniform specialization of a concrete maximal-divisor-height conjecture, rather than adding instances to its table. The slice inequality is motivated by the q-dilation of the remaining factors and controls precisely the coefficient mass that can combine at a single exponent. It supplies the missing upper bound and is stronger than knowing a height bound for the factors alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
