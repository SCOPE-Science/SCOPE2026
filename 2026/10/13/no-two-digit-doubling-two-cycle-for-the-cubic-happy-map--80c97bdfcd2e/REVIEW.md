# Independent mathematical audit

## correctness

PASS

Let X=ab+c with 1<=a<b,0<=c<b and b<=X<2X<b^2. In a no-carry doubling 2c<b, both digits double, so S3(2X)=8S3(X)=16X, contradicting required X. A carry forces c>=b/2 and a<b/2. From S3(X)=2X follows c^3<=b^2+b-2, whereas c^3>=b^3/8. The difference b^3-8b^2-8b+16 is positive at b=9 and increasing thereafter, so no b>=9. Independent enumeration of all 68 admissible digit pairs for 2<=b<=8 recovered exactly one satisfying first equation: (8,3,3,X=27), but S3,8(54)=432!=27. All bases and all two-digit cases exhausted; none beyond two digits claimed.

## originality

PASS

Scientific best-of-knowledge assessment after independently reading the frozen RESULT.md and recreating relevant proof/calculation, checking Resultary and named primary source statements. Wu--Dang--Zhang 2015 surveys cubic digit-map periodic points only for finitely many bases (up to 16) and Hargreaves--Siksek studies generalized happy functions and bounds, not this uniform arbitrary-base ratio-two exclusion. The square-digit doubling-cycle family in Goedhart--Gurtas--Harris differs in exponent; it motivates the contrast rather than implying this negative result.

## value

PASS

The exact ratio-two question is a mathematically motivated small-denominator dynamical rigidity test: the exponent-two map has an infinite two-digit doubling two-cycle construction, while cubic digit dynamics forbids that entire mechanism in every base. The all-base analytic cutoff plus exhaustive finite residual classification proves a genuine universal negative boundary, though it is narrow and not a census of all cubic cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
