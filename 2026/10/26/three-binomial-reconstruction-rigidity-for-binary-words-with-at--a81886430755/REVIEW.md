# Independent mathematical audit

## correctness

PASS

The alternating triples distinguish four runs (both present), three (one, fixing the start), and at most two (neither); letter totals and ordered pairs recover these shorter cases. For four runs starting in zero, the deck supplies Z=a+c, O=b+d, P=N10=bc, N010=aP and N101=dP, which recover all four exponents at fixed orientation. For a same-deck word starting in one, put Q=N01 and rho=P/Q. Pair balance gives P+Q=ZO and the alternating triples give opposite end exponents rho*d,rho*a. The product of its two middle exponents is (Z-rho*a)(O-rho*d)=Q+rho(rho-1)ad since Zd+Oa=Q+ad. As that product must equal Q, rho=1 and the word is the reversal. Counting zeros before and after individual ones (and vice versa) gives the two triple-difference identities, so the reversal is equivalent precisely when N01=N10, or 2bc=ZO. Dividing b(c-a)=d(a+c) by gcd(c-a,c+a) gives the positive solutions, with c>a. Each labeled unordered reversal pair has a unique zero-start representative, so the listed parameters are nonredundant for labeled pairs; complement is an involution on the family, not an additional nonredundant list if one further quotients by complement. Independent direct enumeration of all 510 binary words of lengths 1–8 found zero collisions through length 6, exactly two reversal pairs at 7, and eight nonreversal pairs at 8. The specified witness has the stated deck and run counts 4 and 5. Thus the theorem is sharp in both stated senses, not a claim that the first collision of any kind has length 8.

## originality

PASS

The supported contribution is the complete four-run rigidity and reversal criterion for scattered multiplicity decks, with a verified five-run boundary. The later indexed record contains the same central classification as well as a census; this is real duplication of scope, not evidence of independent priority or a prior source for the frozen theorem. The small length threshold is supporting sharpness, not the basis for the originality pass.

## value

PASS

Reconstruction from subsequence multiplicities has a natural restriction by the number of symbol changes. The proof delineates the last bound with uniqueness up to reversal, classifies exactly which reversals it cannot distinguish, and shows by a minimal nonreversal witness what fails when the run bound is increased. The arbitrary-length classification, not the small finite enumeration alone, is the substantive contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
