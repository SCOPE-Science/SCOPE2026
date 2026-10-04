# Exact odds parametrization of the confidential Blackwell Pareto frontier
## Finding
For the Blackwell broadcast channel \(0\mapsto(0,0),\ 1\mapsto(0,1),\ 2\mapsto(1,0)\), let \(p_0=a\), \(p_1=b\), and \(p_2=c\). Write \(A=(a+c)h_2(c/(a+c))\) and \(B=(a+b)h_2(b/(a+b))\), so the mutually confidential classical capacity region of arXiv:2609.26750v1 is the downward closure of the union of the points \((A,B)\). Its entire non-axis Pareto frontier is exactly parameterized as follows. Choose \(x\in(0,1)\), let \(y\in(0,1)\) be the unique solution of \(\psi(x)\psi(y)=1\), where \(\psi(t)=-\ln t/\ln(1+t)\), and set \(a=(1+x+y)^{-1}\), \(b=ax\), \(c=ay\). Then the corresponding frontier point is \(R_1=\frac{1+y}{1+x+y}h_2(\frac{y}{1+y})\) and \(R_2=\frac{1+x}{1+x+y}h_2(\frac{x}{1+x})\). Conversely every non-axis Pareto point arises uniquely this way, with unique supporting weight \(w=\frac{-\ln x}{-\ln x+\ln(1+y)}\in(0,1)\). The two endpoint limits are \((1,0)\) and \((0,1)\), while the symmetry fixed point is \(x=y=\varphi^{-1}\), giving \((R_1,R_2)=(\log_2\varphi,\log_2\varphi)\).

## Assumptions and scope
The channel is the deterministic Blackwell broadcast map \(0\mapsto(0,0)\), \(1\mapsto(0,1)\), \(2\mapsto(1,0)\). The capacity notion is the mutually confidential classical-message capacity studied in Belzig, Ghosal, Salek, and Smith, with conditional strong secrecy. Their deterministic-channel formula specializes to
\[
\mathcal C_{\mathrm{conf}}=\bigcup_{a,b,c\ge 0,\ a+b+c=1}[0,A(a,c)]\times[0,B(a,b)],
\]
where
\[
A(a,c)=(a+c)h_2\!\left(\frac{c}{a+c}\right),\qquad
B(a,b)=(a+b)h_2\!\left(\frac{b}{a+b}\right).
\]
The statement concerns the Pareto frontier of this region. It does not alter the coding theorem, secrecy model, or quantum-capacity comparison in the source paper.

## Proof
Fix a supporting weight \(w\in(0,1)\) and maximize
\[
F_w(a,b,c)=wA(a,c)+(1-w)B(a,b)
\]
over the probability simplex. Using natural logarithms only to differentiate, the entropy factors contribute an overall positive factor \(1/\ln 2\), which does not affect the optimizer.

For a tangent perturbation \(u=(u_a,u_b,u_c)\), the second variations of the two conditional-entropy terms are
\[
D^2A[u,u]=-
\frac{(c u_a-a u_c)^2}{\ln 2\,a c(a+c)},
\qquad
D^2B[u,u]=-
\frac{(b u_a-a u_b)^2}{\ln 2\,a b(a+b)}.
\]
Hence \(F_w\) is strictly concave on the interior of the simplex: equality in both quadratic forms forces \(u_b/b=u_a/a=u_c/c\), so \(u\) is proportional to \((a,b,c)\); the tangent condition \(u_a+u_b+u_c=0\) then gives \(u=0\).

The unique maximizer is interior. If \(b=0\) and \(1-w>0\), introducing an infinitesimal positive \(b\) produces the usual \(-b\log b\) gain in \(B\), which dominates the finite first-order change in \(A\); similarly \(c=0\) is impossible when \(w>0\). If \(a=0\), then both conditional entropies vanish, while interior inputs give a positive objective.

At the interior maximizer, the Lagrange equations are
\[
\begin{aligned}
w\ln\frac{a+c}{a}+(1-w)\ln\frac{a+b}{a}&=\lambda,\\
(1-w)\ln\frac{a+b}{b}&=\lambda,\\
w\ln\frac{a+c}{c}&=\lambda.
\end{aligned}
\]
Put \(x=b/a\) and \(y=c/a\). Subtracting the second and third equations from the first gives
\[
w\ln(1+y)+(1-w)\ln x=0,
\qquad
(1-w)\ln(1+x)+w\ln y=0.
\]
Thus \(0<x,y<1\), and multiplication yields
\[
\ln x\,\ln y=\ln(1+x)\,\ln(1+y),
\]
which is equivalent to \(\psi(x)\psi(y)=1\) for \(\psi(t)=-\ln t/\ln(1+t)\).

Conversely, let \(x,y\in(0,1)\) satisfy \(\psi(x)\psi(y)=1\) and define
\[
w=\frac{-\ln x}{-\ln x+\ln(1+y)}.
\]
Then the first stationary equation holds by construction, and the product relation implies the second. Strict concavity makes the associated probability vector \((1,x,y)/(1+x+y)\) the unique global maximizer of \(F_w\). Because the capacity region is compact, convex, and downward closed, every non-axis Pareto point has a supporting normal with both coordinates positive, and hence is obtained from exactly one such maximizer.

It remains to show that the parametrization itself is single-valued. On \(0<t<1\),
\[
\psi'(t)=\frac{-\ln(1+t)/t+\ln t/(1+t)}{\ln^2(1+t)}<0,
\]
so \(\psi\) decreases continuously from \(+\infty\) to \(0\). Therefore for every \(x\in(0,1)\) there is a unique \(y\in(0,1)\) with \(\psi(x)\psi(y)=1\). The map is an involution. Its fixed point satisfies \(-\ln x=\ln(1+x)\), equivalently \(x(1+x)=1\), so \(x=\varphi^{-1}\). Substituting gives \(a=1/\sqrt5\), \(b=c=(1-1/\sqrt5)/2\), and \(R_1=R_2=\log_2\varphi\), agreeing with the source's maximum-sum point. Finally, \(x\downarrow0\) forces \(y\uparrow1\), while \(x\uparrow1\) forces \(y\downarrow0\), giving the endpoint limits \((1,0)\) and \((0,1)\).

## Verification
The accompanying `verify.py` independently evaluates the involution relation, the supporting-weight equations, the symmetric golden-ratio point, endpoint limits, and numerical weighted optimizations on representative weights. These computations are checks of the analytic proof, not substitutes for it.

## Relationship to prior work
Belzig, Ghosal, Salek, and Smith give the exact union-of-rectangles capacity formula for the confidential Blackwell channel, prove the symmetric maximum-sum value \(2\log_2\varphi\), and state that the curved boundary in their figure is sampled numerically by maximizing weighted conditional entropies. The present result keeps their capacity theorem unchanged and eliminates that remaining weighted two-dimensional optimization: the whole Pareto frontier and every optimal input distribution are characterized by a one-dimensional odds involution.

The ordinary Blackwell broadcast capacity without mutual secrecy has a different classical rate region and does not imply this confidential frontier. Searches for the exact confidential frontier, weighted conditional-entropy boundary, odds-ratio formulation, and the source identifier found no equivalent published statement. A residual risk remains that an equivalent KKT parametrization exists under different information-geometric terminology.

## Limitations
The result is specific to the Blackwell deterministic map and the mutually confidential classical-message capacity formula in the cited source. It does not characterize the Platypus example, general deterministic broadcast channels, or the quantum-capacity frontier. The parametrization is implicit through the monotone involution \(\psi(x)\psi(y)=1\); except at the symmetric point and endpoints, no elementary closed form for \(y\) is claimed.

## References
1. P. Belzig, S. Ghosal, F. Salek, and G. Smith, "Quantum Broadcast Channels with Mutually Confidential Messages," arXiv:2609.26750v1, first public 2026-09-22. Sections 6.3 and 8.1 contain the Blackwell capacity formulas and comparison.
2. Z. Goldfeld, G. Kramer, H. H. Permuter, and P. Cuff, "Strong secrecy for cooperative broadcast channels," IEEE Transactions on Information Theory 63 (2017), 469--495. This is a different cooperative secrecy model and is cited only as nearby literature.
