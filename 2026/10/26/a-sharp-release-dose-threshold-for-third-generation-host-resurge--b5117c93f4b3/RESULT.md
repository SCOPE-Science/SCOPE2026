# A sharp release-dose threshold for third-generation host resurgence in the Nicholson–Bailey model

## Finding
For the classical Nicholson–Bailey host–parasitoid recurrence, one positive initial parasitoid release always reduces host abundance after one and two generations, but can **increase** host abundance after three. The third-generation release-dose curve admits an exact parameter-uniform classification: it has at most two positive stationary doses, and two occur if and only if an explicit host-production threshold is exceeded and the starting parasitoid density is sufficiently low.

Fix \(R,a,c,H_0,P_0>0\), and apply **exactly one** parasitoid introduction of \(q\geq0\) just before the first update, replacing \(P_0\) by \(P_0+q\). Write
\[
W=acH_0,\quad Y_0=W e^{-aP_0},\quad Y(q)=Y_0e^{-aq}.
\]
If \(R\leq1\), the resulting third-generation host abundance \(H_3(q)\) is strictly decreasing in \(q\). If \(R>1\), put \(b=R-1\), let \(y_c>1/b\) be the **unique** positive solution in that range of
\[
b y_c^2(y_c+2)=y_c^2+3y_c+1,
\]
and define
\[
W_c(R)=y_c+\log\frac{R y_c(1+y_c)}{b y_c-1}.
\]
When \(W\leq W_c(R)\), \(H_3(q)\) is strictly decreasing on \([0,\infty)\). When \(W>W_c(R)\), the equation
\[
G_{R,W}(y)=-1+(R-1)y-Ry(1+y)e^{y-W}=0
\]
has exactly two roots \(0<y_-<y_+<W\). The complete shape classification is:

* If \(Y_0\leq y_-\), the dose curve is strictly decreasing, apart from a possible zero derivative at the starting point.
* If \(y_-<Y_0\leq y_+\), it increases strictly until \(q=a^{-1}\log(Y_0/y_-)\), then decreases strictly; the unique positive local maximum is attained at that dose.
* If \(Y_0>y_+\), it decreases strictly to a local minimum at \(q=a^{-1}\log(Y_0/y_+)\), rises strictly to a local maximum at \(q=a^{-1}\log(Y_0/y_-)\), and then decreases strictly. Both turning points are genuine and positive.

At \(W=W_c(R)\), the derivative may vanish at one isolated dose, but the host response is still strictly decreasing. Thus \(W_c(R)\) is the **sharp onset threshold** for a locally counterproductive parasitoid release at generation three, and generation three is the earliest such response horizon in this model.

## Assumptions and scope
For each integer generation \(j\geq0\), the baseline recurrence is
\[
H_{j+1}=R H_j e^{-aP_j},\qquad
P_{j+1}=cH_j(1-e^{-aP_j}).
\]
All parameters and initial abundances are strictly positive; \(R\) need not exceed one. The intervention is a nonnegative **additive** release only at the initial generation. No parasitoid survival carryover, competing hosts, density regulation, or further interventions are assumed. The comparison observes host abundance after exactly one, two, or three complete population updates; no claim concerns the infinite-time limit or field efficacy.

## Proof
Introduce the dimensionless original parasitoid exposure \(p=aP_0\), intervention exposure \(z=aq\), initial host-production parameter \(W=acH_0\), and \(Y=W e^{-p-z}\). Direct substitution gives
\[
H_1=RH_0e^{-p-z},\quad aP_1=W-Y,
\]
\[
H_2=R^2H_0e^{-p-z-W+Y},\quad aP_2=RY(1-e^{-W+Y}).
\]
The exact three-generation expression is therefore
\[
H_3(q)=R^3H_0\exp\!\left[-p-z-W+(1-R)Y+RYe^{Y-W}\right].
\]
The first two log-derivatives with respect to \(z\) are \(-1\) and \(-1-Y\), both negative. Since \(dY/dz=-Y\), differentiation of the third expression yields
\[
\frac{d}{dz}\log H_3=G_{R,W}(Y)
=-1+(R-1)Y-RY(1+Y)e^{Y-W}.
\]
For \(R\leq1\), this is always negative. For \(R>1\), its derivative and second derivative in \(y\) are
\[
G_{R,W}'(y)=(R-1)-Re^{y-W}(1+3y+y^2),
\]
\[
G_{R,W}''(y)=-Re^{y-W}(4+5y+y^2)<0.
\]
Moreover, \(G_{R,W}(0)=-1\), while \(G_{R,W}(W)=-1-W-RW^2<0\). Thus any positive segment of \(G\) consists of one interval between exactly two simple roots.

For \(b=R-1>0\), positivity of \(G(y)\) requires \(y>1/b\) and is equivalent to
\[
W>F_R(y):=y+\log\frac{Ry(1+y)}{by-1}.
\]
Note \(F_R(y)>y\), so such a \(y\) lies within \((0,W)\). The function \(F_R\) diverges at both ends of \((1/b,\infty)\); differentiating gives
\[
F_R'(y)=\frac{by^3+(2b-1)y^2-3y-1}{y(1+y)(by-1)}.
\]
The cubic numerator is negative at \(y=1/b\). Its first derivative there is \(1+1/b>0\), and its second derivative is \(6by+4b-2>0\) for \(y\geq1/b\). Hence the cubic increases strictly and crosses zero exactly once. This unique minimizer \(y_c\) solves \(b y_c^2(y_c+2)=y_c^2+3y_c+1\), and \(W_c(R)=F_R(y_c)\). If \(W<W_c\), \(G<0\). If \(W=W_c\), \(G\leq0\), with a single zero. If \(W>W_c\), strict concavity and the negative endpoint values imply exactly two roots \(y_-<y_+\), positive precisely between them. As \(q\) increases, \(Y(q)\) decreases continuously and strictly from \(Y_0\) to zero; crossing these roots gives the stated exhaustive dose-curve classification. At equality \(W=W_c\), one isolated derivative zero does not prevent strict decrease.

For a fully exact counterexample, choose \(R=3\), \(a=c=1\), \(H_0=6\), and \(P_0=\log3\). A release \(q=\log2\) changes the first-generation host population from \(6\) to \(3\), and the second-generation host population from \(18e^{-4}\) to \(9e^{-5}\). Yet
\[
\frac{H_3(\log2)}{H_3(0)}
=\exp\!\left(2-\log2+3e^{-5}-6e^{-4}\right)>1,
\]
because \(\log2<1\) and \(6e^{-4}<1\). Thus the third-generation reversal occurs despite strict suppression in the first two generations. Finally, the exact expression shows \(H_3(q)\to0\) as \(q\to\infty\): this is a finite-dose, finite-horizon reversal, not a claim that arbitrarily large releases worsen outcomes.

## Verification
Run `python -m pip install -r requirements.txt` followed by `python verify.py` from the directory containing both files. The independent checker evaluates the original recurrence directly, compares it with the closed three-generation expression, checks the analytic dose derivative numerically and verifies strict one- and two-generation suppression for 5,000 randomized admissible parameter tuples. It also checks critical tangencies and the sign changes on 48 parameter settings and verifies the explicit counterexample. Numerical checks supplement, but do not establish, the theorem for all parameters; the proof above handles all positive real parameters.

## Relationship to prior work
The Nicholson–Bailey model is the classical discrete-generation host–parasitoid framework. Hassell's 2000 review (online publication 2001) establishes the ecological interpretation and the delayed feedback mechanism. Tang, Xiao and Cheke's model, available publicly online in December 2007, treats parasitoid releases and integrated pest management, including fixed and state-dependent interventions; its principal results concern asymptotic eradication thresholds, periodic attractors, and combined interventions. Wang, Qin and Tang (2019) analyze resource-limited periodic pulses and the optimal range of a release rate for an asymptotic threshold in a different map. Those are not the present claim, which is a complete **finite-three-generation, one-additive-release dose-response phase diagram in the unmodified Nicholson–Bailey map**. A general sensitivity or parametric-bifurcation framework could subsume the derivation; no claim of historical priority is made without independent verification.

## Limitations
The original classical model does not capture density-limited host growth, parasitoid carryover, field stochasticity, host age structure, resource limitations, or spatial heterogeneity. The parameter boundary predicts a model effect, not a management recommendation. Only a single initial additive pulse and exactly three generations are classified. The finding does not optimize total intervention cost, prove long-run population suppression, or establish mathematical independence from more general dynamical-systems results. The full breadth of earlier biological-control literature has not been ruled out; the especially close 1982 Barclay equilibrium study concerns a different response quantity, but was not fully inspected.

## References
1. M. P. Hassell, *Host–parasitoid population dynamics*, Journal of Animal Ecology 69 (2000), 543–566. DOI: 10.1046/j.1365-2656.2000.00445.x. Full text: https://besjournals.onlinelibrary.wiley.com/doi/10.1046/j.1365-2656.2000.00445.x . First-online date displayed as 2001-12-25.
2. S. Tang, Y. Xiao, and R. A. Cheke, *Multiple attractors of host–parasitoid models with integrated pest management strategies: Eradication, persistence and outbreak*, Theoretical Population Biology 73 (2008), 181–197. DOI: 10.1016/j.tpb.2007.12.001. Author repository: https://gala.gre.ac.uk/id/eprint/2162/ . First public online: 2007-12-08.
3. P. Wang, W. Qin, and G. Tang, *Modelling and Analysis of a Host-Parasitoid Impulsive Ecosystem under Resource Limitation*, Complexity (2019), 9365293. DOI: 10.1155/2019/9365293. Full text: https://onlinelibrary.wiley.com/doi/10.1155/2019/9365293 .
4. H. J. Barclay, *Models for pest control using predator release, habitat management and pesticide release in combination*, Journal of Applied Ecology 19 (1982), 337–348. DOI: 10.2307/2403471. The complete text was not inspected; literature-overlap risk is explicitly retained.
