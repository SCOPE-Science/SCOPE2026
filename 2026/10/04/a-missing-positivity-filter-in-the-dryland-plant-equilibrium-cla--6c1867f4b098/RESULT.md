# A missing positivity filter in the dryland plant equilibrium classification

## Finding
Consider the temporal system
\[
\dot u=u\big((a+mu-u^2)v-1\big),\qquad
\dot v=1-(b+cu+du^2)v,
\]
under the parameter domain stated in the source, namely \(a,b,d>0\) and \(m,c\in\mathbb{R}\). A state with \(u>0\) is a positive equilibrium if and only if
\[
F(u)=(1+d)u^2+(c-m)u+b-a=0
\]
and
\[
0<u<\tau:=\frac{m+\sqrt{m^2+4a}}{2}.
\]
For every such root, the second coordinate is uniquely
\[
v=\frac{1}{a+mu-u^2}>0.
\]
Thus a quadratic root is not by itself enough: it must also lie below the positive zero \(\tau\) of \(a+mu-u^2\).

In particular, the source's case \(b=a\), \(m>c\) proposes the nonzero branch
\[
u=\frac{m-c}{1+d}.
\]
On that branch,
\[
a+mu-u^2=\frac{a(1+d)^2+(m-c)(md+c)}{(1+d)^2},
\]
so positivity of \(v\) is equivalent to the additional sharp condition
\[
a(1+d)^2+(m-c)(md+c)>0.
\]
The exact parameter choice \(a=b=d=m=1\), \(c=-3\) satisfies \(b=a\) and \(m>c\), but the proposed branch is \(u=2\) with
\[
a+mu-u^2=-1,
\]
therefore \(v=-1\). Since the quadratic equation then has only roots \(u=0\) and \(u=2\), the system has no positive equilibrium despite meeting the source theorem's case (ii).

## Assumptions and scope
The statement concerns the non-diffusive equilibrium equations of the dimensionless dryland vegetation model in arXiv:2411.07255v1. The source explicitly takes \(a,b,d>0\) and \(m,c\in\mathbb{R}\). Positive means both ecological state variables satisfy \(u>0\) and \(v>0\).

The correction is about equilibrium feasibility, not local stability, global attraction, or existence of spatial patterns after a feasible equilibrium has been selected. It does not assert that numerical examples in parameter subregions with \(c\ge 0\) are affected.

## Proof
At an equilibrium with \(u>0\), the first equation can be divided by \(u\), giving
\[
(a+mu-u^2)v=1.
\]
The second equilibrium equation gives
\[
(b+cu+du^2)v=1.
\]
Hence both denominators are equal and nonzero, and subtraction yields
\[
(1+d)u^2+(c-m)u+b-a=0.
\]
Conversely, if \(u>0\) solves this quadratic and \(a+mu-u^2>0\), then setting \(v=1/(a+mu-u^2)\) makes both equilibrium equations hold and gives \(v>0\).

Because \(a>0\), the polynomial \(p(u)=a+mu-u^2\) has one negative and one positive real zero. Its positive zero is
\[
\tau=\frac{m+\sqrt{m^2+4a}}{2},
\]
and the concave quadratic satisfies \(p(u)>0\) for positive \(u\) exactly when \(0<u<\tau\). This proves the necessary-and-sufficient filter.

For \(b=a\), \(m>c\), the nonzero root is \(u=(m-c)/(1+d)\). Direct substitution gives
\[
(1+d)^2p(u)=a(1+d)^2+(m-c)(md+c),
\]
which proves the stated branch condition because \(1+d>0\).

For \(a=b=d=m=1\), \(c=-3\), the quadratic becomes \(2u^2-4u=2u(u-2)\). Its only positive root is \(u=2\), for which \(p(2)=1+2-4=-1\), so \(v=-1\). Hence no root survives the positivity filter.

## Verification
The bundled `verifier.py` uses exact rational arithmetic from Python's standard library. It checks the source case assumptions for the counterexample, reconstructs the quadratic root, verifies both equilibrium residuals exactly at \((u,v)=(2,-1)\), checks the branch numerator equals \(-4\), and confirms that no positive quadratic root has positive \(v\). It prints `VERIFY_OK` only after all checks pass.

The general filter is proved symbolically above and does not depend on finite sampling or numerical root finding.

## Relationship to prior work
Xia, Xiao, and Yu derive the same two equilibrium equations and then classify positive equilibria by the roots of the resulting quadratic. Their stated parameter domain allows \(c\) and \(m\) to be real, but Theorem 2.1 does not separately require positivity of \(a+mu-u^2\), even though their displayed formula for \(v\) divides by that quantity.

The antecedent reduced dryland model of Jaibi, Doelman, Chirilus-Bruckner, and Meron also emphasizes that the coefficient corresponding to the linear biomass contribution in the water-loss factor may have either sign. This makes a negative linear coefficient part of the model family's intended sign structure rather than an algebraic extension introduced only for the counterexample.

Searches for the exact source identifier, the missing feasibility inequality, the branch numerator, and equivalent positive-equilibrium corrections found no prior source-specific correction. The closest published dryland-model result located in the internal comparison set concerned parameter identifiability in a Klausmeier model and neither contains nor implies this equilibrium-feasibility statement.

## Limitations
This finding corrects the literal equilibrium classification over the source's stated parameter domain. It does not establish that every later theorem in the paper fails: several later results explicitly impose \(c\ge 0\), and any later argument restricted to a genuinely positive equilibrium must be assessed separately. No claim is made about nonlinear pattern selection, ecological calibration of the specific counterexample, or the existence of a journal-version erratum not retrieved in the searches performed here.

## References
1. Y. Xia, J. Xiao, J. Yu, *Pattern formation and global analysis of a systematically reduced plant model in dryland environment*, arXiv:2411.07255v1, 30 October 2024.
2. O. Jaibi, A. Doelman, M. Chirilus-Bruckner, E. Meron, *The existence of localized vegetation patterns in a systematically reduced model for dryland vegetation*, Physica D 412 (2020), 132637, DOI 10.1016/j.physd.2020.132637; arXiv:2001.11804v1.
