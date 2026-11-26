# Independent mathematical audit

## correctness

PASS

Reproduced the full 44,100-pair complex vanishing census with independently written subset dynamic programming in the integral group ring of a cyclic group of order five. Put t=−ζ, a primitive fifth root. Each matrix entry is represented by (−1)^(rc) t^(rc mod 5). A subset state is the determinant for the first |S| rows and chosen column positions S in increasing order. Appending an unused position j in the next row multiplies by the corresponding entry and the sign (−1)^(number of positions in S larger than j), so Laplace expansion proves the DP. The final five integer coefficients evaluate to zero precisely when all are equal, by 1+t+t²+t³+t⁴ being the minimal polynomial. Integers are exact in the replay: each determinant has at most 24 signed terms. The independent result was (degree,count)=(0,20),(10,100),(20,50),(30,20),(110,10),(130,10), totaling 5000 of 44100; it also verified bitwise transpose symmetry. The affine orbit representatives, sizes and degrees from the run were (0123,20,0), (0124,40,10), (0125,40,10), (0126,20,30), (0134,10,20), (0135,40,20), (0138,20,10), (0156,10,110), (0246,10,130). All counts agree and 5000/44100 reduces to 50/441. The frozen cyclotomic coefficient recurrence is valid as written; its recorded modular digests agree but are not used to infer complex vanishing.

## originality

PASS

Pass for the full degree distribution and singular-pair probability at four rows and four columns of F_10. Do not credit the zero class, one complete affine orbit at degree 10, or the existence of singular minors as new. The closest same-order census found for a different cardinality is not equivalent.

## value

PASS

Order ten with four rows is the classical concrete obstruction to sufficiency of divisor-uniformity. At that motivated finite boundary, the degree gives the exact failure probability of recovering coefficients on a fixed Fourier support from four sample sites chosen uniformly. The earlier full-spark comparison only distinguishes zero risk from positive risk, while the six-level distribution distinguishes, for example, 10 failures from 130 among the same 210 choices and fixes the probability for uniformly chosen supports and samples. This is a natural complete incidence invariant at that boundary, not an arbitrary computer census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
