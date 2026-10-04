# The Oropouche threshold criterion has a missing supercritical branch
## Finding
For the autonomous Oropouche transmission system studied by Peterson et al., define
\[
A=R_{FA},\qquad B=R_{FH},\qquad C=R_{CH},\qquad S=A+B+C,\qquad P=AC.
\]
The published basic reproduction number satisfies
\[
q:=\mathcal R_0^2=rac{S+\sqrt{S^2-4P}}2,
\]
so \(q\) is the larger root of \(x^2-Sx+P=0\). The exact threshold is
\[
\mathcal R_0>1
\quad\Longleftrightarrow\quad
S>2\ 	ext{ or }\ P<S-1.
\]
The Appendix instead identifies \(S>P+1\), equivalently \(P<S-1\), as *the* condition for \(\mathcal R_0>1\). That condition is sufficient but not necessary: it omits every supercritical point with \(S>2\) and \(P\ge S-1\).

An exact parameter witness satisfying the paper's transmission parametrization is
\[
N_A=N_H=N_F=N_C=1,\quad b=4,\quad \pi_{VH}=1,\quad \pi_{HV}=	frac12,
\]
\[
k=p=	frac12,\quad \mu_V=1,\quad \gamma_A=\gamma_H=	frac14,\quad
\mu_A=	frac34,\quad \mu_H=	frac{11}4.
\]
For these values, Eq. (2) gives
\[
eta_{FA}=2,\ eta_{FH}=2,\ eta_{CH}=4,\ eta_{AF}=1,\ eta_{HF}=1,\ eta_{HC}=2,
\]
and hence
\[
A=2,\qquad B=	frac23,\qquad C=	frac83,\qquad S=P=	frac{16}3.
\]
Thus \(\mathcal R_0^2=4\), so \(\mathcal R_0=2\), while the Appendix factor is
\[
S-P-1=-1<0.
\]
Moreover,
\[
I_A^*=I_F^*=I_H^*=I_C^*=	frac12
\]
is an exact positive equilibrium of the reduced autonomous system. Therefore the negative Appendix constant-term factor does not imply \(\mathcal R_0<1\), and the printed endemic-equilibrium argument misses a genuine supercritical endemic regime.

## Assumptions and scope
The result concerns the autonomous reduction obtained from the paper by setting the seasonal factors to one and treating host and vector totals as fixed, exactly as in its qualitative-analysis section. All parameters in the witness are nonnegative, both transmission probabilities lie in \([0,1]\), the two host recovery rates are equal, and the six transmission rates are generated from the paper's Eq. (2), rather than chosen independently.

No claim is made about the seasonal data-fitting conclusions, about global stability of the endemic equilibrium, or about uniqueness of endemic equilibria for arbitrary parameters. The result is an algebraic correction to the stated threshold equivalence in Appendix A, plus an exact admissible witness showing that the omitted branch is dynamically nonempty.

## Proof
Write \(q=\mathcal R_0^2\). The paper gives
\[
q=rac{S+\sqrt{S^2-4P}}2,
\]
so \(q\) is the larger root of
\[
f(x)=x^2-Sx+P.
\]
Because \(A,B,C\ge0\),
\[
S^2-4P=(A-C)^2+2B(A+C)+B^2\ge0.
\]
If \(S>2\), then \(q\ge S/2>1\). If \(S\le2\), the two roots cannot both exceed one, because their sum is \(S\). Hence in this case the larger root exceeds one exactly when \(1\) lies strictly between the roots, that is exactly when
\[
f(1)=1-S+P<0,
\]
or equivalently \(P<S-1\). This proves
\[
\mathcal R_0>1\Longleftrightarrow S>2\ 	ext{or}\ P<S-1.
\]
Similarly,
\[
\mathcal R_0=1\Longleftrightarrow S\le2\ 	ext{and}\ P=S-1,
\]
and
\[
\mathcal R_0<1\Longleftrightarrow S<2\ 	ext{and}\ P>S-1.
\]

For the witness, the forest bite fractions are both \(1/2\), since
\[
rac{kN_A}{kN_A+(1-p)N_H}=rac{(1-p)N_H}{kN_A+(1-p)N_H}=	frac12.
\]
The stated six \(eta\)-values follow directly from Eq. (2). Since
\[
\mu_A+\gamma_A=1,\qquad \mu_H+\gamma_H=3,
\]
the three cycle quantities are exactly
\[
R_{FA}=1\cdot2=2,
\]
\[
R_{FH}=1\cdotrac23=rac23,
\]
\[
R_{CH}=rac43\cdot2=rac83.
\]
Therefore \(S=P=16/3\). The discriminant is \(64/9\), so
\[
q=rac{16/3+8/3}2=4,
\]
and \(\mathcal R_0=2\). The Appendix factor is \(S-P-1=-1\).

Finally, substitute \(I_A=I_F=I_H=I_C=1/2\) into the four equations of the reduced system. Their right-hand sides are respectively
\[
2\cdot	frac12\cdot	frac12-1\cdot	frac12=0,
\]
\[
(1\cdot	frac12+1\cdot	frac12)	frac12-1\cdot	frac12=0,
\]
\[
(2\cdot	frac12+4\cdot	frac12)	frac12-3\cdot	frac12=0,
\]
and
\[
2\cdot	frac12\cdot	frac12-1\cdot	frac12=0.
\]
Thus the omitted supercritical branch contains an exact positive endemic equilibrium.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic. It reconstructs the transmission rates from the primitive parameters, recomputes \(R_{FA},R_{FH},R_{CH}\), verifies \(S=P=16/3\), verifies the perfect-square discriminant and \(\mathcal R_0^2=4\), checks that the published Appendix factor is negative, and substitutes the proposed equilibrium into all four autonomous equations. A successful run prints `VERIFY_OK`.

## Relationship to prior work
Peterson et al. derive the displayed formula for \(\mathcal R_0\) from the next-generation matrix and, in Appendix A, rewrite a quartic constant term as a positive prefactor times
\[
R_{FA}+R_{CH}+R_{FH}-R_{CH}R_{FA}-1.
\]
They then state that positivity of this expression is the condition \(\mathcal R_0>1\), and that negativity is the condition \(\mathcal R_0<1\). The exact root analysis above shows that this is only valid on the \(S\le2\) side of parameter space. The general next-generation framework of van den Driessche and Watmough establishes the local disease-free threshold once \(\mathcal R_0\) is correctly computed; it does not supply the source-specific algebraic equivalence asserted in Appendix A.

Searches of the exact article title, DOI, the three cycle labels, the claimed threshold expression, and correction/erratum aliases found no published correction or prior result stating this missing branch. Semantic searches of published mathematical findings returned only different threshold problems, with no implication of this source-specific claim.

## Limitations
The counterexample uses an admissible exact parameter set chosen to expose the algebraic branch structure; it is not claimed to be a calibrated Amazonas parameter set. The result does not show that every point on the missing branch possesses a unique endemic equilibrium, and it does not invalidate the paper's formula for \(\mathcal R_0\) itself. It shows that the Appendix's equivalence between the sign of its constant-term factor and the sign of \(\mathcal R_0-1\) is false without an additional restriction such as \(S\le2\).

## References
1. C. Peterson, D. Gandhi, E. Slack, E. Rubio, A. Claxton, and C. M. Kribs, “A novel mathematical model of seasonality in Oropouche virus transmission in Amazonas, Brazil,” *Journal of Mathematical Biology* 93 (2026), article 21. DOI: 10.1007/s00285-026-02422-1.
2. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
