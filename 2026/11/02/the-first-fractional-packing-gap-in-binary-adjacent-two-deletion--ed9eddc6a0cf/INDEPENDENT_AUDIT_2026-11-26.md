# Independent mathematical audit

## correctness

PASS

The stated integral program is exactly disjointness of the distinct output sets after deleting one adjacent pair, with no wraparound. An independent exact replay rebuilt those sets from binary strings and checked the listed codes and all rational primal and dual inequalities for n=2,...,8. Their respective objectives certify (1,2,4,4,8,13,21) for the LP, and the exhibited codes match the LP through n=7. At n=8 every one of the 77 weighted families was checked pairwise for conflict; the minimum coverage of a word is 1 and the total weight is 482/23. Each code meets a family at most once, so its integral size is at most floor(482/23)=20, achieved by the displayed code. This proves the first gap, not optimality of the clique-augmented relaxation or any assertion for n>8.

## originality

PASS

The specifically supported distinct claim is the first integral/fractional separation for the exact adjacent-pair shadow LP, with A_2(8)=20, F_2(8)=21 and the explicit clique bound. The length-six integral optimum 8 is already covered, and neither the model nor the LP framework is new. No inspected comparable statement gives or implies the claimed separation.

## value

PASS

The length cutoff is dictated by the first failure of a standard relaxation, not an arbitrary range of computations. The exact equality through seven followed by failure at eight is a usable benchmark for burst-deletion bounds; the clique certificate shows that pairwise conflicts can tighten the output-star constraints enough to certify the true optimum by rounding. This value does not depend on re-establishing the known n=6 result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
