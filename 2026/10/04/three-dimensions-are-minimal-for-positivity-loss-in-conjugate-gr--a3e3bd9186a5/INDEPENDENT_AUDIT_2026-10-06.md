# Independent mathematical audit

## correctness

PASS

Sylvester's criterion gives positive definiteness of the displayed tridiagonal family exactly for a>2/3, and the stated inverse is entrywise positive there. Direct exact conjugate-gradient algebra gives the second-iterate first coordinate N_a(B)/Q_a(B), with Q_a(B)>0 because it is a positive scalar multiple of p_1^T A_a p_1. For 2/3<a<=4 every coefficient of N_a is nonnegative and its constant term is positive; for a>4 its leading coefficient is negative, so sufficiently large B makes the component negative and the limit is (4-a)/3. The exact witness a=5, B=7 gives x_2=(-5/751,1324/751,6881/1502) while the exact solution is strictly positive. One and two dimensions cannot exhibit the effect because the first CG iterate is a positive multiple of b and the method terminates at the exact inverse-positive solution by step two. The inspected exact-rational verifier and an independent recurrence replay reproduced the witness and formula checks.

## originality

PASS

Schmelzer--Stoll explicitly observe that ordinary CG on SPD systems need not preserve coordinatewise nonnegativity, but their accessible full text contains no Stieltjes or M-matrix specialization. Meijerink--van der Vorst are highly relevant because they study CG-based solution methods for symmetric M-matrices, but only abstract/bibliographic material was publicly accessible in this run; the permitted institutional retrieval returned no verified PDF and was not retried. Targeted Resultary search for Stieltjes/M-matrix positivity loss, minimal dimension and the a=4 threshold returned no implication-equivalent result. Best-of-knowledge originality therefore survives, with the inaccessible 1977 full text retained as an explicit priority risk rather than treated as failure.

## value

PASS

Inverse positivity is the canonical matrix property guaranteeing a nonnegative exact solution under nonnegative forcing, so leaving the positive cone inside this class is structurally meaningful. The result identifies the minimum dimension, gives a small exact witness, and supplies a sharp threshold within a natural tridiagonal Stieltjes family, making it useful for algorithms that rely on physically or optimization-motivated positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
