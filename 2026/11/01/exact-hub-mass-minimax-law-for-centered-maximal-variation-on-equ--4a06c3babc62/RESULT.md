# Exact hub-mass minimax law for centered maximal variation on equimass-leaf stars

## Finding
For every integer \(m\ge 3\), let \(S_{m+1}\) be a star with hub mass \(h>0\) and \(m\) equal leaf masses \(w>0\). Write \(q=h/w\). If \(M_q\) is centered Hardy–Littlewood maximal averaging over graph balls with these vertex masses, and \(\operatorname{Var}(f)=\sum_{i=1}^{m}|f(v_i)-f(o)|\) is **unweighted edge variation**, then the exact attained sharp constant is
\[
C_m(q):=\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(M_q f)}{\operatorname{Var}(f)}
=\max\left\{1-\frac{1}{m+q},\frac{1}{1+q}\right\}.
\]
The first branch is attained by the indicator of any leaf. The second is attained by the indicator of the hub. Consequently, \(C_m(q)\) has the unique global minimizer
\[
q_m=\frac{\sqrt{(m-1)^2+4}-(m-1)}{2},\qquad
\min_{q>0} C_m(q)=\frac{1}{1+q_m}.
\]
For three leaves \(q_3=\sqrt2-1\) and the minimum is \(1/\sqrt2\). As \(m\to\infty\), \(q_m\sim 1/(m-1)\). The uniform counting-mass specialization \(q=1\) is the previously known \(m/(m+1)\); the new statement concerns the complete nonconstant hub-mass profile and its minimax tuning for every \(m\ge3\).

## Assumptions and scope
The graph has one hub \(o\) joined to exactly \(m\) leaves \(v_i\), and no other edges. All leaf masses equal \(w>0\); the hub mass is \(h=qw\). For each vertex \(v\),
\[
(M_q f)(v)=\max_{r\in\{0,1,2\}}
\frac{\sum_{u:d(u,v)\le r}\mu(u)|f(u)|}{\sum_{u:d(u,v)\le r}\mu(u)}.
\]
Here \(d\) is graph distance and \(\mu(o)=h\), \(\mu(v_i)=w\). The variation has no vertex or edge weights. Inputs are arbitrary real vertex functions. The ratio is taken only when the input variation is positive; constant inputs yield zero output variation.

## Proof
First, replacing \(f\) by \(|f|\) does not increase variation, and does not change \(M_qf\). Thus it suffices to prove the inequality for nonnegative input \(g\). Because every average of \(g+c\) equals the corresponding average of \(g\) plus \(c\), the centered maximal operator on nonnegative inputs commutes with a common additive shift. Put \(x_i=g(v_i)-g(o)\); the \(x_i\) can have either sign. Write
\[
D=m+q>2,\qquad t=\frac1{1+q},\qquad A=\frac{\sum_i x_i}{D}.
\]
After subtracting the common value \(g(o)\), the maximal value at the hub is \(z_0=\max\{0,A\}\), and at leaf \(i\) is \(z_i=\max\{x_i,t x_i,A\}\). This follows directly by listing the radius-zero, radius-one and whole-star ball averages. The original variation is \(\sum_i|x_i|\), while the output variation is \(\sum_i|z_i-z_0|\).

Write \(P=\sum_{x_i>0}x_i\) and \(N=\sum_{x_i<0}(-x_i)\). **Case \(A\ge0\).** Every leaf difference is \((x_i-A)_+\), so the output variation is \(\sum_i(x_i-A)_+\). If any term is positive, the contributing index set has size at least one. Since \(A=(P-N)/D\ge0\),
\[
\sum_i(x_i-A)_+\le P-A
=\left(1-\frac1D\right)P+\frac ND
\le\left(1-\frac1D\right)(P+N).
\]
The last inequality uses \(D>2\). If there are no positive contributions, the claim is immediate.

**Case \(A<0\).** Then \(N>P\) and \(z_0=0\). Each positive deviation contributes exactly \(x_i\); each negative deviation \(x_i=-v_i\) contributes \(\min\{t v_i,(N-P)/D\}\). If \(P=0\), the variation is at most \(tN\). If \(P>0\), let \(k\) be the number of negative deviations. Because at least one deviation has each sign, \(1\le k\le m-1\). Hence
\[
\operatorname{Var}(M_qg)
\le P+\frac{k(N-P)}D
=\left(1-\frac{k}{D}\right)P+\frac{k}{D}N
\le\left(1-\frac1D\right)(P+N).
\]
For the last inequality, \(k\ge1\) and \(k\le m-1<D-1\). Together the cases give the asserted upper bound.

For the leaf indicator, only the chosen leaf differs from the hub, and the output difference across that leaf edge is \(1-1/D\), all others being zero. For the hub indicator, the output at the hub is \(1\) and each leaf output is \(q/(q+1)\), because this exceeds the whole-star average \(q/(m+q)\). Consequently the variation ratio is \(t\). Thus both branches are exact and attained.

Finally, \(1-1/(m+q)\) is strictly increasing in \(q\), whereas \(1/(1+q)\) is strictly decreasing. Their unique crossing solves \(q^2+(m-1)q-1=0\). That crossing is the unique minimizer. The displayed asymptotic is immediate from the positive quadratic root.

## Verification
The standalone `verify.py` independently computes each graph-ball maximal value from the original weighted definition using exact rational arithmetic, checks the sharp inequality on exhaustive small integer samples for \(m=3,4,5,6\) and six rational hub masses, checks both exact extremizer families, and checks the unique balance relation numerically for \(3\le m\le40\). The run reported 19,568 successful assertions. This is supplementary evidence: the unrestricted theorem follows from the preceding analytic case proof, not from finite tests.

## Relationship to prior work
Soria and Tradacete (2014 preprint) study graph maximal-operator \(\ell^p\) bounds with counting measure, not sharp variation dependence on nonuniform vertex masses. Madrid (2015 preprint) addresses variation bounds on \(\mathbb Z^d\), not a weighted finite star. González-Riquelme and Madrid (2020) prove the sharp **counting-measure** \(1\)-variation constant \(m/(m+1)\) on \(S_{m+1}\); this is exactly the \(q=1\) specialization here and is not claimed as new. Their 2020 sequel studies other \(p\)-variation and strong-norm problems with counting measure. The new dependence on the hub-to-leaf mass ratio, the two competing weighted extremal modes and the unique mass-design minimizer do not follow from the cited displayed results. Earlier uncatalogued weighted-star treatments remain a novelty risk.

## Limitations
Only centered graph-ball averages and finite stars with equal leaf masses are covered. No statement is made for independently unequal leaf masses, weighted edge variation, \(p\)-variation for \(p\ne1\), other graph classes, or uncentered maximal operators. The minimizer varies the hub mass while keeping a common leaf mass; it is not a global minimizer over all possible leaf-mass vectors. The claim is mathematically proved but has not received independent scientific validation.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first submitted 2014-10-22), subsequently J. Math. Anal. Appl. 436 (2016), 661–682.
2. J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112 (first submitted 2015-12-13).
3. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first submitted 2020-05-06), Theorem 2(ii) and Section 2.2.
4. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (first submitted 2020-11-05), Sections 1 and 4.
