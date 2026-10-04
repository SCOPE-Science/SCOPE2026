# Exact mixed contact-tracing threshold curve and a strict partial-compliance synergy law
## Finding
## Finding
Consider the fast-variable epidemic-threshold system of de Meijere et al. for simultaneous pairwise and triplewise contact tracing. Define
\[
R_0=\\tau(n-2),\qquad \\kappa=\\frac{n-1}n,\qquad \\delta=\\frac{n-2}n,\qquad \\widehat\\kappa=\\kappa\\delta,
\]
and assume \\(n>2\\), \\(R_0>1\\), \\(a>0\\), and
\[
q_{\\min}^t=\\frac{2(R_0-1)}{R_0n-2}<q\\le1.
\]
Then the entire nonnegative mixed critical branch joining the pure pairwise and pure triplewise thresholds has the exact parameterization, for \\(0\\le t\\le1\\),
\[
B(t)=(1-t)\\frac{R_0-1}\\kappa+t\\frac{R_0-1}\\delta,
\]
\[
z(t)=\\frac{1-(1-q)(B(t)+1)/R_0}{a+R_0},
\]
\[
c_p(t)=\\frac{(1-t)(R_0-1)}{\\kappa z(t)},\qquad
c_t(t)=\\frac{t(R_0-1)}{\\widehat\\kappa z(t)^2}.
\]
At \\(t=0\\) and \\(t=1\\) these reduce exactly to the source's pure pairwise and pure triplewise critical levels \\(c_p^*\\) and \\(c_t^*\\), respectively.

More strongly, let \\(r=z(1)/z(0)\\) and \\(D(t)=1-t+tr\\). Then
\[
\\frac{c_p(t)}{c_p^*}+\\frac{c_t(t)}{c_t^*}
=1-\\frac{t(1-t)r(1-r)}{D(t)^2}.
\]
For \\(q_{\\min}^t<q<1\\), one has \\(0<r<1\\), so every interior mixture \\(0<t<1\\) lies strictly below the straight chord joining the two pure thresholds. At full compliance \\(q=1\\), one has \\(r=1\\), and the normalized mixed threshold is exactly the straight chord. Thus the slight reinforcement reported numerically for combined tracing has an exact threshold-level form: strict synergy occurs precisely under partial compliance in this parameter regime.

## Assumptions and scope
The object is the algebraic threshold system obtained from the source's early-time fast-variable closure, with \\(x=[SI]/[I]\\), \\(y=[II]/[I]\\), and \\(z=[IT]/[I]\\). The claim concerns the connected nonnegative critical branch between the two pure-intervention thresholds. The strict statement assumes \\(q_{\\min}^t<q<1\\); the endpoint \\(q=q_{\\min}^t\\) is excluded because the pure triplewise threshold diverges, while \\(q=1\\) is treated separately and gives equality. No assertion is made for \\(R_0\\le1\\), negative intervention rates, or for the full stochastic network process independently of the moment closure.

## Proof
Write \\(A=R_0-1\\), \\(P=c_pz\\), and \\(T=c_tz^2\\). The second threshold equation, after dividing by the positive variable \\(x\\), is
\[
\\kappa P+\\widehat\\kappa T=A. \tag{1}
\]
The first equation gives \\(\\tau x=1+P+\\kappa T\\). Define
\[
B=P+\\kappa T.
\]
The third threshold equation and (1) imply
\[
\\tau x=y(1+\\kappa P+\\widehat\\kappa T)=R_0y,
\]
so
\[
R_0y=1+B. \tag{2}
\]

The fourth threshold equation contains the positive tracing terms \\(y(\\kappa P+\\widehat\\kappa T)=Ay\\). Its negative tracing terms combine as
\[
-z(\\kappa P+\\widehat\\kappa T)-(P+\\kappa T)=-Az-B.
\]
Using (2), the fourth equation therefore reduces exactly to
\[
1-(a+R_0)z+(q-1)y=0,
\]
or
\[
z=\\frac{1-(1-q)(B+1)/R_0}{a+R_0}. \tag{3}
\]

Now solve the two linear equations
\[
P+\\kappa T=B,\qquad \\kappa P+\\widehat\\kappa T=A.
\]
Since \\(\\widehat\\kappa=\\kappa\\delta\\) and \\(\\kappa-\\delta=1/n\\),
\[
P=n(A-\\delta B),\qquad T=n\\left(B-\\frac A\\kappa\\right). \tag{4}
\]
Nonnegativity \\(P,T\\ge0\\) is therefore equivalent to
\[
\\frac A\\kappa\\le B\\le\\frac A\\delta.
\]
Parameterize this interval affinely by
\[
B(t)=(1-t)\\frac A\\kappa+t\\frac A\\delta,\qquad 0\\le t\\le1.
\]
Equation (4) becomes
\[
P(t)=(1-t)\\frac A\\kappa,\qquad T(t)=t\\frac A{\\widehat\\kappa}.
\]
Together with (3), this yields the asserted formulas for \\(c_p=P/z\\) and \\(c_t=T/z^2\\). Because \\(q>q_{\\min}^t\\), the triplewise endpoint has \\(z(1)>0\\); hence the whole affine function \\(z(t)\\) is positive. The remaining fast variables are positive because \\(R_0y=1+B>0\\) and \\(\\tau x=R_0y\\).

At \\(t=0\\) and \\(t=1\\), direct simplification gives precisely the source formulas
\[
c_p^*=(a+R_0)\\frac{R_0-1}{F_p},\qquad
c_t^*=(a+R_0)^2\\frac{R_0-1}{F_t}.
\]
This endpoint identity is checked symbolically in the bundled verifier.

Finally, (3) makes \\(z(t)\\) affine. Put \\(z_p=z(0)\\), \\(z_t=z(1)\\), \\(r=z_t/z_p\\), and \\(D(t)=z(t)/z_p=1-t+tr\\). Then
\[
\\frac{c_p(t)}{c_p^*}=\\frac{1-t}{D(t)},\qquad
\\frac{c_t(t)}{c_t^*}=\\frac{tr^2}{D(t)^2}.
\]
Their sum satisfies
\[
1-\\left(\\frac{1-t}{D(t)}+\\frac{tr^2}{D(t)^2}\\right)
=\\frac{t(1-t)r(1-r)}{D(t)^2}. \tag{5}
\]
For \\(q<1\\), equation (3) and \\(B(1)>B(0)\\) give \\(0<z_t<z_p\\), hence \\(0<r<1\\); (5) is then strictly positive for every \\(0<t<1\\). For \\(q=1\\), equation (3) gives \\(z(t)=1/(a+R_0)\\) for all \\(t\\), so \\(r=1\\) and (5) vanishes identically.

## Verification
The bundled `verify.py` reconstructs all four threshold equations symbolically from the displayed parameterization, verifies that each simplifies to zero, checks algebraic equality with the source's pure-threshold formulas, proves the normalized chord identity by exact symbolic simplification, and checks the source's Figure 5(b) parameter regime as a rational example. The verifier was executed from the packaged path after writing the files and returned `VERIFY_OK`.

For the source's Figure 5(b) parameters \\(n=5\\), \\(\\tau=7/10\\), \\(a=1\\), and \\(q=3/5\\), the assumptions hold because \\(R_0=21/10\\) and \\(q_{\\min}^t=22/85<3/5\\). At \\(t=1/2\\), the verifier confirms that the normalized threshold sum is strictly less than one.

## Relationship to prior work
De Meijere et al. derive explicit critical rates for pure pairwise and pure triplewise tracing and then study simultaneous tracing numerically. Their Figure 5(b) compares the numerically observed mixed threshold against the straight line joining the two pure thresholds and reports a slight reinforcement at intermediate mixtures. The exact mixed critical parameterization and the identity (5), including the sharp distinction between partial and full compliance, are not stated in the article.

Earlier pairwise contact-tracing work of Eames and Keeling derives a threshold relation for pairwise tracing but has no triplewise intervention parameter. Barnard et al. develop the fast-variable threshold method for clustered pairwise epidemic models, not the simultaneous pairwise/triplewise contact-tracing system. De Meijere and Castellano analyze forward contact tracing with partial adherence in a different SIS-based model; the inspected abstract does not contain a mixed pairwise/triplewise threshold curve. These works motivate or precede parts of the framework but do not imply the algebraic mixed-intervention geometry proved here.

## Limitations
This result is exact only for the source's fast-variable mean-field closure and its threshold equations. It does not establish a threshold theorem for the underlying finite stochastic network, does not quantify final epidemic size away from threshold, and does not claim that every possible path in intervention-parameter space exhibits synergy. The strict chord inequality is for the natural endpoint-normalized mixed critical branch and requires \\(q_{\\min}^t<q<1\\). At \\(q=1\\), the effect disappears exactly; at \\(q=q_{\\min}^t\\), the triplewise endpoint is singular and is outside the stated branch.

## References
1. G. de Meijere, A. Pugliese, G. Iñiguez, P. L. Simon, I. Z. Kiss, “To trace or not to trace: analytical insights from network-based contact-tracing models,” *Journal of Mathematical Biology* 93, 45 (2026), DOI 10.1007/s00285-026-02455-6; first public preprint arXiv:2603.04059 (2026-03-04).
2. K. T. D. Eames, M. J. Keeling, “Contact tracing and disease control,” *Proceedings of the Royal Society B* 270 (2003), 2565–2571, DOI 10.1098/rspb.2003.2554.
3. R. C. Barnard, L. Berthouze, P. L. Simon, I. Z. Kiss, “Epidemic threshold in pairwise models for clustered networks: closures and fast correlations,” *Journal of Mathematical Biology* 79 (2019), 823–860, DOI 10.1007/s00285-019-01380-1.
4. G. de Meijere, C. Castellano, “Limited efficacy of forward contact tracing in epidemics,” *Physical Review E* 108 (2023), 054305, DOI 10.1103/PhysRevE.108.054305.
