# Independent mathematical audit

## correctness

PASS

For positive (a,b,c,d,e) and word 0^a1^b0^c1^d0^e, reconstructed exhaustive classification by number of transitions in a square root. A nonunary root has either one transition, giving only (0^c1^b)^2 if c<=a,b<=d or (1^d0^c)^2 if c<=e,d<=b, or two transitions, giving (0^i1^b0^(c-i))^2 when b=d and max(1,c-e)<=i<=min(a,c-1). Unary squares add floor(P/2)+floor(Q/2), P=max(a,c,e), Q=max(b,d); these root categories are distinct. Thus S=floor(P/2)+floor(Q/2)+alpha+beta+H and all mixed squares have the one length 2(c+min(b,d)). The case inequalities bound S<=floor(n/2), mixed T<=floor((n+1)/3), with witnesses for every n>=5. Counting b,i,k and nonnegative outer extensions gives H expectation GF z^6/((1-z)^2(1-z^2)^3); counting H>0 gives z^6(1+z+z^2)/((1-z)^4(1+z)^3). Dominant poles yield E[H]->1/8 and P(H>0)~3/(2n); normalized uniform five-compositions converge to Dirichlet(1,1,1,1,1), with limiting square density half of max of zero-run proportions plus max of one-run proportions, mean 1/3. Independent direct substring-set enumeration for all 5^5=3125 positive tuples in [1,5]^5 matched the complete list, counts and upper bounds. Finite testing corroborates the all-length transition/counted-composition arguments.

## originality

PASS

Best-of-knowledge PASS for the complete run-parameter square-factor classification, common mixed-square length, sharp fixed-five-run bounds and rare synchronization generating functions, not for general linear bounds on distinct squares. Inspected Brlek–Li and Shuo Li original texts: their unrestricted and binary-frequency inequalities do not determine the exact five-run set or event law. The closely related Jonoska–Manea–Seki 2014 SOFSEM paper could only be checked by abstract and related presentation references, not the full proceedings article; exact-coverage risk remains material. Resultary search found unrelated binary-word extremal records, no exact same classification.

## value

PASS

PASS: five alternating runs mark the first possibility of linearly many distinct mixed-symbol square factors; with fewer runs there is at most one. Synchronization of the two one-runs forces equal mixed-square lengths yet creates rare O(n)-sized families, quantified by exact generating functions and asymptotics. This explains meaningful new combinatorics and probability of a natural contiguous-factor invariant, not a new unrestricted word-length bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
