# Sharp heterogeneous two-agent gradient-tracking stability frontier

## Finding

Let \(0<s<1\), \(0\le\eta<1\), \(\bar h>0\), and consider two strictly positive scalar quadratic curvatures \(h_1=\bar h(1+\eta)\), \(h_2=\bar h(1-\eta)\). Use the symmetric doubly-stochastic communication matrix
\[
W=\frac12\begin{pmatrix}1+s&1-s\\1-s&1+s\end{pmatrix}.
\]
For the standard constant-step distributed gradient-tracking iteration specified below, the exact asymptotic convergence condition is
\[
0<\beta<\beta_*(s,\eta),\qquad \beta=\alpha\bar h,
\]
where
\[
L=s^2+6s+1,\qquad
\boxed{\beta_*(s,\eta)=\frac{4(1+s)^2}{L+\sqrt{L^2-16s(1-\eta^2)(1+s)^2}}}.
\]
At \(\beta=\beta_*\) the reduced iteration has an eigenvalue \(-1\); no larger positive step yields a Schur-stable reduced iteration. For fixed \(s\), \(\beta_*\) decreases strictly as the nonzero curvature dispersion \(\eta\) increases, while \(\beta_*(s,0)=2\) and
\[
\lim_{\eta\uparrow1}\beta_*(s,\eta)=\frac{2(1+s)^2}{s^2+6s+1}<2.
\]
Thus a non-complete two-agent network loses a definite portion of its allowable step interval under heterogeneous local curvatures, even though full averaging \(s=0\) retains the ceiling \(\beta<2\).

## Assumptions and scope

The two local objectives are \(f_i(x)=h_i(x-b_i)^2/2+c_i\), with arbitrary real \(b_i,c_i\). Each agent uses the common step \(\alpha>0\) and the standard gradient-tracking recursion
\[
x_{k+1}=W(x_k-\alpha y_k),\qquad
 y_{k+1}=Wy_k+H(x_{k+1}-x_k),\qquad
 H=\operatorname{diag}(h_1,h_2),
\]
with the usual consistent initial gradient tracker (after subtracting the optimizer, \(y_{i,0}=h_i(x_{i,0}-b_i)\)). Convergence is measured by the spectral radius of the three-dimensional reduced error state after removing the constant, unexcited conservation mode; this is the standard linear convergence criterion for the consistently initialized recursion. All calculations are in exact real arithmetic. No claim is made about nonidentical or time-varying step sizes, directed communication, or nonlinear losses.

## Proof

Take the orthonormal consensus/disagreement basis \(v=(1,1)^\mathsf T/\sqrt2\), \(u=(1,-1)^\mathsf T/\sqrt2\). In the source's reduced coordinates, the disagreement eigenvalue is \(s\), the normalized curvature cross-coupling is \(\eta\), and the reduced error matrix is exactly
\[
A_\beta=\begin{pmatrix}
1-\beta&\beta\eta(s-1)&-\beta\eta s\\
0&s&-s\\
-\beta\eta&\beta(s-1)&s(1-\beta)
\end{pmatrix}.
\]
Its characteristic polynomial \(P(z)=z^3+a z^2+b z+c\) has coefficients
\[
\begin{aligned}
a&=\beta(1+s)-1-2s,\\
b&=s\bigl((1-\eta^2)\beta^2-4\beta+s+2\bigr),\\
c&=s\bigl(-(1-\eta^2)\beta^2+(1+s)\beta-s\bigr).
\end{aligned}
\]
Write \(v_0=1-\eta^2\in(0,1]\) (distinct from the consensus basis vector), and \(L=s^2+6s+1\). Direct substitution yields
\[
P(1)=\beta(1-s)^2>0,\qquad
-P(-1)=F(\beta):=2s v_0\beta^2-L\beta+2(1+s)^2.
\]
The two positive roots of \(F\) are \(\beta_*<\beta_+\), with the displayed formula for the smaller root. The discriminant is \((1-s)^4+16s(1-v_0)(1+s)^2>0\). At \(v_0=1\) the roots are \(2\) and \((1+s)^2/(2s)\ge2\), so \(\beta_*\le2\le\beta_+\); for \(v_0<1\) the first root is strictly below \(2\) and the second strictly above \(2\).

For a real monic cubic, the strict Schur--Jury conditions are \(|c|<1\), \(P(1)>0\), \(-P(-1)>0\), and \(J:=1-b+ac-c^2>0\). We establish the two non-obvious inequalities for every \(0<\beta<\beta_*\).

First, \(c\ge s[-\beta^2+(1+s)\beta-s]>-1\): the latter quadratic is concave on \([0,2]\), and its values at \(0\) and \(2\) are respectively \(-s^2\) and \(s(s-2)\), both strictly greater than \(-1\). To show \(c<1\), let \(B_0=2(1+s)^2/L\). If \(\beta\le B_0\), use \(c\le s[(1+s)\beta-s]\le s[(1+s)B_0-s]<1\); indeed
\[
1-s[(1+s)B_0-s]=\frac{(1-s)(s^3+s^2+5s+1)}{L}>0.
\]
If \(\beta>B_0\), the inequality \(F(\beta)>0\) implies \(s v_0\beta^2>(L\beta-2(1+s)^2)/2\), hence
\[
c<1+2s-\frac{s^2+4s+1}{2}\beta\le 1+2s-\frac{s^2+4s+1}{2}B_0<1.
\]
(The last expression equals the preceding upper bound at \(B_0\).)

Next, write the final Jury expression as the quadratic polynomial in \(v_0\)
\[
\begin{aligned}
J(\beta,v_0)={}&(1-s)^3(1+s)+\beta s(1-s)^2(2s+3)\\
&+\beta^2s(1-s)(1+s)^2\\
&+v_0\bigl(2\beta^2s^2(1-s)+\beta^3s(1+s)(2s-1)\bigr)
-\beta^4s^2v_0^2.
\end{aligned}
\]
It is concave in \(v_0\in[0,1]\); the minimum is at an endpoint. For \(v_0=0\), all displayed surviving terms are strictly positive. For \(v_0=1\), as a polynomial in \(\beta\), the coefficients in descending degree have signs \((-,-,+,+,+)\) if \(s<1/2\) and \((-,+,+,+,+)\) if \(s\ge1/2\) (ignoring zero coefficients). Thus Descartes' rule gives exactly one positive root. Since \(J(0,1)=(1-s)^3(1+s)>0\) and \(J(2,1)=(1-s)^2(1+2s-s^2)>0\), that root lies beyond \(2\). Therefore \(J>0\) throughout \(0<\beta\le2\) and \(0\le v_0\le1\). All four Schur inequalities now hold precisely throughout \((0,\beta_*)\).

For \(\beta_*\le\beta\le\beta_+\), the characteristic polynomial has \(P(-1)=0\) at the endpoints and \(-P(-1)<0\) in between; none is Schur stable. For \(\beta>\beta_+\), we prove \(c<-1\), also excluding stability. At the upper root, \(F(\beta_+)=0\) gives
\[
c(\beta_+)=1+2s-\frac{s^2+4s+1}{2}\beta_+.
\]
The upper root is no smaller than its \(v_0=1\) value \((1+s)^2/(2s)\). The elementary identity
\[
(1+s)(s^2+4s+1)-8s=(1-s)^3+2s^2(1+s)>0
\]
therefore implies \(c(\beta_+)<-1\). Finally, \(\beta_+> (1+s)/(2v_0)\), so \(c'(\beta)=s[(1+s)-2v_0\beta]<0\) thereafter, proving \(c<-1\) for all \(\beta>\beta_+\). This completes the global classification. The formula itself gives strict decrease of \(\beta_*\) in \(\eta>0\) and the endpoint statements.

## Verification

Run `python3 verify.py` in the package directory. It checks the polynomial coefficient identities and the sign/boundary formulas using exact rational arithmetic on a parameter grid, together with numerical eigenvalue tests above, at and below the predicted boundary. The infinite parameter classification rests on the symbolic proof above; numerical grids are not treated as an exhaustive proof.

## Relationship to prior work

Wang, Ballotta, Carli, Iannelli, Cao, and Schenato (2026) establish a certified distributed-gradient-tracking framework and explicit optima in the complete-graph or homogeneous-curvature regimes. Their general heterogeneous-network construction is a conservative certification, not this exact two-agent stability region. Earlier homogeneous graph-specific tuning does not imply the heterogeneous classification: the cross-coupling \(\eta\) destroys the modal factorization. The present result resolves the simplest missing joint regime \(s>0\), \(\eta>0\) and gives its sharp full-step boundary rather than a sufficient bound. General Schur--Jury stability theory is used as a tool, not claimed as new.

## Limitations

The theorem concerns two agents, positive disagreement eigenvalue, positive scalar curvatures and identical constant steps. For negative disagreement eigenvalues, three or more agents, heterogeneous step sizes, nonquadratic costs or inexact communication, neither the threshold nor the monotonicity conclusion is asserted. The exact discovery's historical priority beyond the inspected literature is not independently certified.

## References

- Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao, L. Schenato, *Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*, arXiv:2608.03548v1 (first public 2026-08-04), Sections II--IV, VII, https://arxiv.org/abs/2608.03548.
- Standard real-polynomial Schur--Jury criterion for discrete-time linear systems (classical criterion; no novel priority claimed).
