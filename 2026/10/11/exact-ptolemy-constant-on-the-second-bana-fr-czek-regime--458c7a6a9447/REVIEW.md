# Independent mathematical audit

## correctness

PASS

For every real lambda>sqrt(2), the branch norms E(v)=sqrt(v_1^2+v_2^2), F(v)=lambda|v_1| give N=max(E,F). Put c=lambda^2/2>1 and d=lambda^2/[2(lambda^2-1)] in (1/2,1), and H(v)^2=c v_1^2+d v_2^2. When F>=E, v_2^2<=(lambda^2-1)v_1^2 yields H^2<=lambda^2 v_1^2=F^2; when E>=F, the signs of c-1 and d-1 give H^2<=E^2. Therefore H<=N for all vectors. The four numerator active-branch pairs EE, FF, EF, FE are exhaustive, ties included. EE and FF obey Hilbert/one-dimensional Ptolemy with factor 1 (the FF seminorm is valid for the inequality); EF and FE obey E(a)F(b)<=lambda H(a)H(b)/sqrt(cd), and lambda/sqrt(cd)=2sqrt(1-lambda^-2). Hilbert Ptolemy followed by H<=N bounds ALL denominator terms by C=2sqrt(1-lambda^-2). For t=sqrt(lambda^2-1) and x=(1,t), y=(1,-t), z=(2,0), the four denominator-side norms are lambda, N(x-y)=2t, N(z)=2lambda, so the ratio is exactly 2t/lambda. Nonzero pairwise-distinctness holds throughout lambda>sqrt(2). The proof is uniform in the unbounded parameter and treats the endpoint only as a limit; no computational experiment is elevated to an infinite proof. Independent symbolic check with L=lambda^2 simplified (lambda/sqrt(cd))^2 to 4-4/L and evaluated exact witness cases lambda=3/2,2,4.

## originality

PASS

Best-of-knowledge originality for the exact Ptolemy value on lambda>sqrt(2). Full relevant primary texts of the same-object 1993 and 2016 papers, Zuo 2012/2018 exactness criteria, and published first-regime Ptolemy and Zbaganu records were compared by definitions and implication. The earlier same-invariant formula is restricted to the complementary interval. The same second-branch expression for C_Z does not by itself give an upper bound for C_Pt. The inspected general criteria require midpoint or coordinate symmetry absent here. A highly plausible 2015 article could not be read, so priority is not certified and its coverage remains a specific risk, not an automatic fail.

## value

PASS

This is a motivated exact invariant of the classical Banaś--Frączek clipped-disk plane, not an arbitrary parameter slice or renaming. It supplies the missing natural second half of the Ptolemy phase diagram beyond the lambda=sqrt(2) switch, a sharp new mixed-active-branch Hilbert certificate, and a concrete attaining triple. The exact value differs from the first-regime lambda upper envelope and approaches the square-plane constant 2 as lambda grows; this is a reusable benchmark for comparing four-point geometry with Zbaganu, James, and NJ invariants. Its mathematical value does not depend on an unclaimed general p-family extension or a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
