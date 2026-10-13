# The first unresolved bounded Genocchi--Peano degree is \(D_b(9)=30\)
## Finding
Let \(D_b(n)\) be the least possible degree of the denominator of a bounded Genocchi--Peano example in \(n\) variables of the form
\[
g(x_1,\ldots,x_n)=\frac{x_1^{\alpha_1}\cdots x_n^{\alpha_n}}{x_1^{\beta_1}+\cdots+x_n^{\beta_n}},
\]
with positive integer exponents and \(g(0,\ldots,0)=0\). Then
\[
D_b(9)=30.
\]
A degree-\(30\) witness is given by
\[
(\beta_i)=(4,6,8,12,14,20,24,28,30),\qquad
(\alpha_i)=(1,1,1,1,1,1,1,5,1).
\]

## Assumptions and scope
The characterization used here is Ciesielski's bounded-GPE criterion: when the denominator exponents are positive even integers, a GPE is bounded exactly when the \(\beta_i\) are distinct and
\[
\sum_i\frac{\alpha_i}{\beta_i}=1.
\]
The same source explains that odd denominator exponents cannot occur in a GPE of this form. The claim concerns only this standard Genocchi--Peano family and the invariant \(D_b(n)\) defined for it.

## Proof
For the upper bound, take
\[
(\beta_i)=(4,6,8,12,14,20,24,28,30),
\quad
(\alpha_i)=(1,1,1,1,1,1,1,5,1).
\]
The \(\beta_i\) are distinct and even, and
\[
\frac14+\frac16+\frac18+\frac1{12}+\frac1{14}+\frac1{20}+\frac1{24}+\frac5{28}+\frac1{30}=1.
\]
Therefore the characterization gives a bounded GPE of degree \(30\), so \(D_b(9)\le30\).

For the lower bound, suppose a bounded nine-variable GPE had degree at most \(28\). Write \(\beta_i=2d_i\). Distinctness and evenness force the \(d_i\) to be nine distinct elements of \(\{1,\ldots,14\}\), while boundedness becomes
\[
\sum_{i=1}^9\frac{\alpha_i}{d_i}=2.
\]
Because all summands are positive, each \(\alpha_i/d_i<2\), hence
\[
1\le \alpha_i\le2d_i-1.
\]
Let
\[
L=\operatorname{lcm}(1,2,\ldots,14)=360360,
\quad
w_i=\frac L{d_i},
\quad
x_i=\alpha_i-1.
\]
Then \(0\le x_i\le2d_i-2\), and the equation is equivalent to
\[
\sum_i x_iw_i=2L-\sum_iw_i.
\]
This is a finite bounded subset-sum problem for each of the \(\binom{14}{9}=2002\) possible denominator sets. The bundled exact-integer verifier enumerates every set. In \(1228\) cases the right-hand side is already negative, so the contribution with all \(\alpha_i=1\) exceeds \(2\). For each of the remaining \(774\) sets, exact bitset dynamic programming over the allowed ranges \(0\le x_i\le2d_i-2\) proves the target unreachable. Hence no bounded nine-variable GPE has degree at most \(28\). Since every denominator exponent is even, degree \(29\) is impossible as well. Thus \(D_b(9)\ge30\), completing the proof.

## Verification
Run `python verify_db9.py`. The verifier uses only exact integer arithmetic and reports `VERIFY_OK`, together with \(2002\) denominator sets, \(1228\) immediate impossibilities, \(774\) residual exact checks, zero feasible candidates of degree at most \(28\), and the explicit degree-\(30\) witness. The included `verification.log` records the replay output.

## Relationship to prior work
Ciesielski's 2018 paper gives the boundedness characterization, proves general bounds for \(D_b(n)\), and explicitly asks for better information about these numbers. Its Table 3 lists exact \(D_b(n)\) values only through \(n=8\); the entry for \(n=9\) is blank. The 2017 predecessor treats the four-variable bounded case but does not determine the nine-variable invariant. The present result therefore supplies the first exact value immediately beyond the published table's bounded entries.

## Limitations
This result determines only \(D_b(9)\). It does not by itself give a general formula, monotonicity theorem, or asymptotic improvement for \(D_b(n)\). The lower bound is a complete finite certificate for nine variables rather than a uniform argument in \(n\).

## References
1. K. C. Ciesielski, *Minimal Degrees of Genocchi--Peano Functions: Calculus Motivated Number Theoretical Estimates*, Real Analysis Exchange 43(2) (2018), 281--292. DOI: 10.14321/realanalexch.43.2.0281. Author full text: https://math.wvu.edu/~kciesiel/prepF/135.OnDegreesOfGPEs.pdf
2. K. C. Ciesielski and D. A. Miller, *On a Genocchi--Peano Example*, College Mathematics Journal 48(3) (2017), 205--213. DOI: 10.4169/college.math.j.48.3.205.
3. MaRDI author record for K. C. Ciesielski, listing the 2018 paper with publication date 2018-08-24: https://portal.mardi4nfdi.de/wiki/Krzysztof_Chris_Ciesielski
