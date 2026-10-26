# Two distinct rank-reversal thresholds for finite-recovery Arps decline curves

## Finding

For two hyperbolically declining oil or gas wells whose decline exponents and initial decline rates are both ordered, **instantaneous production-rate rankings and cumulative-production rankings have different, sharp two-crossing thresholds**. In particular, a well with strictly lower initial rate and strictly lower lifetime recovery can nonetheless exceed the other well in cumulative output over one bounded interval, with two cumulative-ranking reversals. This occurs even though both individual rates decline strictly at every positive time and both lifetime recoveries are finite.

More precisely, choose \(0<b_1<b_2<1\), \(0<D_1<D_2\) and define
\[
 f_i(t)=(1+b_iD_it)^{-1/b_i},\qquad
 F_i(t)=\frac{1-(1+b_iD_it)^{-(1-b_i)/b_i}}{D_i(1-b_i)},\quad t\geq0.
\]
The wells have instantaneous rates \(q_1(t)=r f_1(t)\), \(q_2(t)=f_2(t)\) and cumulative volumes \(C_1(t)=rF_1(t)\), \(C_2(t)=F_2(t)\). Set
\[
 \rho_\infty=\frac{D_1(1-b_1)}{D_2(1-b_2)},\qquad
 r_{\max}=\min\{1,\rho_\infty\},\qquad 0<r<r_{\max}.
\]
Thus the first well starts at a strictly lower rate and has strictly lower lifetime recovery. Let \(k(t)=f_2(t)/f_1(t)\) and \(G(t)=F_2(t)/F_1(t)\) for \(t>0\). Define
\[
 t_R=\frac{D_2-D_1}{D_1D_2(b_2-b_1)},\quad
 r_R=k(t_R),\quad
 t_C=\text{the unique positive minimizer of }G,\quad r_C=G(t_C).
\]
Then \(0<r_R<r_C<r_{\max}\), and the five exhaustive cases are:

1. For \(0<r<r_R\), both the rate and cumulative output of well 1 are strictly smaller for every \(t>0\).
2. At \(r=r_R\), rates tie only at \(t_R\), tangentially, while cumulative output is strictly smaller for all \(t>0\).
3. For \(r_R<r<r_C\), rates reverse ranking exactly twice, but cumulative output is strictly smaller at all positive times.
4. At \(r=r_C\), rates reverse twice and cumulative production has exactly one tangential equality at \(t_C\), without reversing its sign.
5. For \(r_C<r<r_{\max}\), **both** rates and cumulative output reverse ranking exactly twice. Writing the respective positive crossing times \(u_1<u_2\) and \(v_1<v_2\), their strict order is \(u_1<v_1<u_2<v_2\).

Both pair-creation events have square-root onset: if \(r=r_R+\varepsilon\), the separation of the two rate crossings is \(2\sqrt{2\varepsilon/k''(t_R)}+o(\sqrt\varepsilon)\); if \(r=r_C+\varepsilon\), the two cumulative crossings are separated by \(2\sqrt{2\varepsilon/G''(t_C)}+o(\sqrt\varepsilon)\), with \(\varepsilon\downarrow0\) and the stated parameter restrictions maintained.

## Assumptions and scope

This is a pairwise mathematical comparison of independently declining *Arps hyperbolic* production-rate curves with constant parameters. All times are \(t\geq0\); \(0<b_i<1\) guarantees finite lifetime cumulative production. Initial rates are normalized to \((r,1)\); multiplying both by an arbitrary common positive rate does not change comparisons. Strict inequalities \(b_1<b_2\), \(D_1<D_2\), and \(r<\min\{1,\rho_\infty\}\) are essential to the five-case classification. No empirical calibration, interaction, or field-wide reservoir dynamics are assumed.

## Proof

First, differentiation of \(\log k\) yields
\[
 \frac{k'(t)}{k(t)}=\frac{D_1}{1+b_1D_1t}-\frac{D_2}{1+b_2D_2t}
 =\frac{D_1-D_2+D_1D_2(b_2-b_1)t}{(1+b_1D_1t)(1+b_2D_2t)}.
\]
Hence \(k\) strictly decreases on \((0,t_R)\), strictly increases on \((t_R,\infty)\), and has a nondegenerate strict minimum \(r_R<k(0)=1\). Since \(b_2>b_1\), its tail is asymptotically a positive constant times \(t^{1/b_1-1/b_2}\), so \(k(t)\to\infty\). Every horizontal level \(r\in(r_R,1)\) has precisely two transverse intersections, and its equality at \(r_R\) is tangential.

Next, \(F_i'=f_i\) and \(F_i(0)=0\). Set \(H(t)=F_1(t)k(t)-F_2(t)\) for \(t\geq0\), with its continuous value \(H(0)=0\). The cancellation \(f_1k=f_2\) yields the exact identity
\[
 H'(t)=F_1(t)k'(t),\qquad
 G'(t)=\frac{f_1(t)}{F_1(t)^2}H(t).
\]
Thus \(H\) decreases strictly from zero until \(t_R\), where \(H(t_R)<0\), then increases strictly. Its limit is \(+\infty\): \(F_1\to1/[D_1(1-b_1)]>0\), \(F_2\to1/[D_2(1-b_2)]<\infty\), and \(k\to\infty\). Hence exactly one zero \(t_C>t_R\) exists. Accordingly \(G\) decreases strictly until \(t_C\) and increases strictly afterwards, with one nondegenerate minimum because \(G''(t_C)=f_1(t_C)H'(t_C)/F_1(t_C)^2>0\). Its endpoint limits are \(G(0+)=1\) and \(G(\infty)=\rho_\infty\), so \(r_C=G(t_C)<\min\{1,\rho_\infty\}=r_{\max}\). Since \(H(t_C)=0\), \(r_C=k(t_C)>k(t_R)=r_R\).

The rate and cumulative differences are respectively \(f_1(t)[r-k(t)]\) and \(F_1(t)[r-G(t)]\). Their signs, the endpoint inequalities, and the strictly unimodal shapes of \(k\) and \(G\) establish all five cases including boundaries. When \(r_C<r<r_{\max}\), the cumulative difference starts negative, becomes positive, then becomes negative. At a cumulative upward crossing its derivative equals the instantaneous difference and is positive; at the downward crossing its derivative is negative. Since there are exactly two rate crossings, each cumulative upcrossing follows the first rate upcrossing, and each cumulative downcrossing follows the second rate downcrossing. Thus \(u_1<v_1<u_2<v_2\). Taylor expansion of \(k\) at its nondegenerate minimum and \(G\) at its nondegenerate minimum proves the two square-root separation laws, with no approximation elsewhere.

For an exact nonempty witness take \(b_1=1/2\), \(b_2=3/4\), \(D_1=1\), \(D_2=2\), \(r=4/5\). Here \(\rho_\infty=1\), \(t_R=2\), \(r_R=4^{-1/3}\), and on setting \(z=(1+3t/2)^{1/3}\) one has
\[
 G(t)=\frac{z^3+2}{z(z^2+z+1)},\qquad
 \frac{dG}{dz}=\frac{z^4+2z^3-6z^2-4z-2}{z^2(z^2+z+1)^2}.
\]
The numerator polynomial has exactly one positive root greater than 1 (one sign change in descending coefficients and a sign change from \(z=1\) to sufficiently large \(z\)). This supplies an algebraic characterization \(r_C\approx0.7139563503876054\). At \(t=2\),
\[
 C_1(2)-C_2(2)=2\,4^{-1/3}-\frac65>0,
\]
since \(4<125/27\). Yet the difference is negative immediately after zero and tends to \(-2/5\), proving exactly two nontrivial cumulative rank reversals. The four crossings are approximately \(u_1=0.31443330\), \(v_1=0.88552900\), \(u_2=7.52685607\), and \(v_2=55.82675519\).

## Verification

The companion `verify.py` checks the symbolic rational-parameter reduction, computes the algebraic threshold and all four crossings at high precision, proves the witness signs with exact rational inequalities, and tests 160 seeded admissible generic parameter sets for threshold order and sampled ratio monotonicity near both minima, and verifies four-crossing interlacing in the explicit witness. All tests completed successfully when run against this package. The proof above, not the finite tests, justifies all parameter quantifiers.

## Relationship to prior work

Arps (1945) introduces exponential, hyperbolic, and harmonic decline curves; the functional forms and finite-recovery integrals used here are standard. The 2010 Fekete decline-curve manual discusses rate-time/rate-cumulative plots and their differences, including cumulative asymptotes. Adeboye, Ubani and Oribayo (2011), inspected across its model, examples, conclusions and appendix, analyzes multiwell performance using a modified hyperbolic model. It does not explicitly classify the ordered-independent-well pairwise rate and cumulative rank reversals or the separate thresholds here. Pinelis (2006) develops abstract monotonicity theorems for quotient functions; those general principles may supply alternative proofs of the qualitative quotient shape, which is not independently claimed as a new mathematical method. The specialized sharp Arps production ranking and its exact two-stage phase diagram are the claim assessed here.

## Limitations

The original Arps 1945 primary full text was not accessible for direct inspection. More general published monotonicity or petroleum reservoir ranking results may subsume part or all of the specialized classification; this is residual historical-priority risk rather than a proof of novelty. Two well trajectories are assumed to have no interaction or changes in operating conditions. Finite ultimate extrapolation with constant decline parameters need not fit real reservoirs. The result is a deterministic mathematical comparison, not an oilfield performance or recovery forecast.

## References

1. J. J. Arps, “Analysis of Decline Curves,” *Transactions of the AIME*, 160 (1945), 228–247. DOI: https://doi.org/10.2118/945228-G. First public date used: 1945-12-01.
2. Y. B. Adeboye, C. E. Ubani and O. Oribayo, “Prediction of reservoir performance in multi-well systems using modified hyperbolic model,” *Journal of Petroleum Exploration and Production Technology* (2011), DOI: https://doi.org/10.1007/s13202-011-0009-3.
3. Fekete Associates, “Decline Curve Analysis,” technical manual (2010), https://www.pandai.com/faq/decline_curve_analysis.fekete.pdf.
4. I. Pinelis, “Non-strict l'Hospital-Type Rules for Monotonicity: Intervals of Constancy,” 2006, https://arxiv.org/abs/math/0611662.
