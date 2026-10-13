# Sharp ten-coordinate rigidity for a four-weighted quadratic norm equation

## Finding
Let \(\mathbb N=\{1,2,3,\ldots\}\) and \(E_4=\{x^2+4y^2:x,y\in\mathbb N\}\). Every pair of functions \(G:\mathbb N\to\mathbb C\) and \(F:E_4\to\mathbb C\) satisfying
\[
F(x^2+4y^2)=G(x)+4G(y)\qquad(x,y\in\mathbb N)
\]
is **exactly** of the form
\[
G(n)=An^2+B\quad(n\ge1),\qquad F(t)=At+5B\quad(t\in E_4),
\]
for unique \(A,B\in\mathbb C\). Conversely, every \(A,B\in\mathbb C\) defines such a pair.

There is a sharp finite rigidity threshold: suppose the equation is enforced only for \(1\le x,y\le N\) and \(F\) is defined on the resulting represented integers. For every \(N\ge10\), the values \(G(1),\ldots,G(N)\) necessarily lie on a quadratic \(Ak^2+B\). For every \(3\le N\le9\), nonquadratic assignments of these values satisfy all corresponding representation collisions. Thus \(10\) is the least nontrivial truncation forcing the quadratic form.

## Assumptions and scope
All variables \(x,y,n\) are positive integers. There is no boundedness, reality, multiplicativity, continuity, or positivity condition on either function. The claimed description of \(F\) is **only** on the represented set \(E_4\); values outside that set are not prescribed. The coefficient on the second term is exactly \(4\), matching the quadratic norm \(x^2+4y^2\). For finite truncation, the only consequence of the existence of \(F\) is equality of weighted \(G\)-sums between pairs representing the same integer.

## Proof
**Eight finite collision witnesses.** Put \(s_j=G(j)\). The following are equalities of integers; each row gives \(x^2+4y^2=u^2+4v^2\), and therefore the linear relation \(s_x+4s_y-s_u-4s_v=0\):

| Common integer | \((x,y)\) | \((u,v)\) |
| ---: | :---: | :---: |
| \(65\) | \((1,4)\) | \((7,2)\) |
| \(145\) | \((1,6)\) | \((9,4)\) |
| \(20\) | \((2,2)\) | \((4,1)\) |
| \(40\) | \((2,3)\) | \((6,1)\) |
| \(68\) | \((2,4)\) | \((8,1)\) |
| \(104\) | \((2,5)\) | \((10,1)\) |
| \(200\) | \((2,7)\) | \((10,5)\) |
| \(85\) | \((7,3)\) | \((9,1)\) |

In column order \(s_1,\ldots,s_{10}\), their coefficient matrix is
```
 1 -4  0  4  0  0 -1  0  0  0
 1  0  0 -4  0  4  0  0 -1  0
-4  5  0 -1  0  0  0  0  0  0
-4  1  4  0  0 -1  0  0  0  0
-4  1  0  4  0  0  0 -1  0  0
-4  1  0  0  4  0  0  0  0 -1
 0  1  0  0 -4  0  4  0  0 -1
-4  0  4  0  0  0  1  0 -1  0
```
The determinant of the submatrix consisting of the first eight columns is exactly \(-608\). This is verified by fraction-free integer elimination in `verify.py`; hence this matrix has row rank \(8\). Both the constant vector \((1,\ldots,1)\) and the square vector \((1^2,\ldots,10^2)\) lie in its kernel, and are linearly independent. The kernel therefore consists **precisely** of their span. Consequently, there exist unique \(A,B\in\mathbb C\) such that \(G(j)=Aj^2+B\) for every \(1\le j\le10\).

**Infinite propagation.** For all \(n\ge1\), the exact identity
\[
(n+8)^2+4(n+3)^2=n^2+4(n+5)^2
\]
gives
\[
G(n+8)=G(n)+4G(n+5)-4G(n+3).
\]
The constant sequence and the square sequence separately satisfy this recurrence. Given the first ten quadratic values, induction starting at \(n=3\) proves \(G(j)=Aj^2+B\) for every \(j\ge11\) (the right side then involves only earlier indices). The original equation now gives \(F(t)=At+5B\) for every \(t\in E_4\), since each such \(t\) has a positive representation. Conversely, substitution proves the equation for every pair. This also proves uniqueness of \(A,B\).

**Sharpness.** For a fixed \(N\), collect every representation \((x,y)\) with \(1\le x,y\le N\), group the pairs by \(x^2+4y^2\), choose one base pair per group, and form the integer collision rows \(s_x+4s_y-s_u-4s_v=0\) against every remaining pair. This spans **all** collision constraints, with no assumption on the unrepresented values of \(F\). Exact rational elimination gives the ranks below:

| \(N\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) | \(9\) | \(10\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| rank | \(0\) | \(1\) | \(1\) | \(2\) | \(3\) | \(4\) | \(6\) | \(8\) |
| nullity | \(3\) | \(3\) | \(4\) | \(4\) | \(4\) | \(4\) | \(3\) | \(2\) |

Since the two-dimensional space of quadratic sequences is always contained in the kernel, nullity at least \(3\) means a nonquadratic assignment exists for each \(3\le N\le9\). In fact, when \(N=9\) the assignment \(G(5)=1\) with \(G(k)=0\) for \(k\ne5\) within \(1\le k\le9\) satisfies every collision and is not quadratic. For \(N\ge10\), the same eight witnesses already force every first-ten value to be quadratic, and the propagation identity forces the remaining values up to \(N\). This proves the threshold claim.

## Verification
Run the standalone standard-library script with `python3 verify.py`. It reconstructs the eight witnesses, checks their equal norms, computes the \(8\)-row matrix rank and the exact minor determinant \(-608\), enumerates **every** pair collision at each cutoff \(3\le N\le10\), checks all listed ranks, checks the nonquadratic ninth-cutoff witness, verifies the propagation polynomial identity coefficient by coefficient, and checks sample converse evaluations. The recorded output is:

`EXACT_CERTIFICATE_OK finite_threshold=10 minor_det=-608 rank10=8 rank9=6 witness_count=8 propagation_step=8`

The finite computations establish only their stated exact rank identities; the recurrence plus induction, not any finite search, supplies the infinite conclusion.

## Relationship to prior work
Kátai and Phong (2014, *The functional equation f(A+B)=g(A)+h(B*, Theorem 1) study arbitrary additive decompositions on a sumset and identify possible periodic residues under an \(8\mathbb N\)-difference hypothesis. Their theorem does **not** apply directly here: taking \(A=\{4m^2:m\ge1\}\) leaves \(8\notin A-A\), and our two summands are constrained to be one linked function. Kátai and Phong (2015, Problem 2) explicitly ask when an affine sumset decomposition is the only possibility; Problem 5 separately concerns the nonlinear identity below.

You, Chen, Yuan, and Shen (arXiv:1606.05039v1, first public 2016-06-16) resolve \(D=4\) for the **different nonlinear one-function** equation \(f(x^2+4y^2)=f(x)^2+4f(y)^2\). Khanh (2017, Lemmas 1–2 and main theorem) later proves the general nonlinear equation for all positive \(D\), and establishes that the auxiliary linear identity \(F(x^2+Dy^2)=G(x)+UG(y)\) allows, *as a necessary condition*, a quadratic term plus several periodic-character terms. You et al. explicitly use several of the same quadratic-norm collisions in their Section 5 and prove a pattern for \(f(n)^2\) using, among other inputs, \(11\); this overlap is substantial. The distinct, newly isolated assertion here is the **sharp ten-coordinate collision threshold**, proved by a complete rank calculation and by the nonquadratic nine-coordinate witness. Neither cited paper states this minimal finite threshold or proves its optimality. The unrestricted two-function formulation is a useful corollary of the same finite-rank theorem, not a claim to have first solved the previously resolved nonlinear \(f\)-equation.

## Limitations
The result is specific to the natural weighted norm \(x^2+4y^2\) with a matching coefficient \(4\). It gives no characterization for general \(D\) or independent summand functions, and none for \(F\) outside \(E_4\). The originality assessment is literature-dependent: unindexed equivalent arguments might exist. The finite rank computation is fully checkable, but no external independent audit has been performed.

## References
1. I. Kátai and B. M. Phong, “The functional equation \(f(A+B)=g(A)+h(B)\),” *Annales Univ. Sci. Budapest., Sect. Comp.* **43** (2014), 287–301. https://ac.inf.elte.hu/Vol_043_2014/287_43.pdf ; DOI: 10.71352/ac.43.287.
2. I. Kátai and B. M. Phong, “Some unsolved problems on arithmetical functions,” *Annales Univ. Sci. Budapest., Sect. Comp.* **44** (2015), 233–235, especially Problems 2 and 5. https://ac.inf.elte.hu/Vol_044_2015/233_44.pdf.
3. L. You, Y. Chen, P. Yuan, J. Shen, “A characterization of arithmetic functions satisfying \(f(u^2+kv^2)=f^2(u)+kf^2(v)\),” arXiv:1606.05039v1, posted 2016-06-16. https://arxiv.org/pdf/1606.05039.
4. B. M. M. Khanh, “On conjecture concerning the functional equation,” *Annales Univ. Sci. Budapest., Sect. Comp.* **46** (2017), 123–135, especially Lemmas 1–2. https://ac.inf.elte.hu/Vol_046_2017/123_46.pdf.
