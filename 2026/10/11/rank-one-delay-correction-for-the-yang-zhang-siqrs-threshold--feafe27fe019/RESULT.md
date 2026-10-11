# Rank-one delay correction for the Yang–Zhang SIQRS threshold
## Finding
For the Yang–Zhang SIQRS computer-virus model, the numerical specialization used to verify the first-delay Hopf theorem contains two linked inconsistencies. Table 1 gives \(\eta=0.1\), \(d=0.1\), and \(\alpha_2=0.18\), hence the quarantine-removal coefficient in the model equation must be
\[
\eta+d+\alpha_2=0.38.
\]
System (5.1), however, prints
\[
\dot Q=0.14I-0.48Q.
\]
Taking the printed system (5.1) literally, its unique positive equilibrium is
\[
E_p=\left(\frac{{320}}{{197}},\frac{{1371240}}{{665663}},\frac{{399945}}{{665663}},\frac{{1313079}}{{665663}}\right)
\approx(1.6243654822,2.0599612717,0.6008220376,1.9725882316),
\]
not the reported point \(E^*=(1.6244,2.0598,0.7739,2.0011)\). The discrepancy cannot be explained by rounding: at the displayed coordinates, the quarantine residual of printed (5.1) is exactly \(-831/10000=-0.0831\), while changing both displayed \(I\) and \(Q\) by at most half a unit in the last printed decimal can change that residual by at most \(3.1\times10^{-5}\).

For the case \(\tau_2=0\), the delayed infection contribution to the \((S,I)\) equations is a rank-one matrix. Therefore the characteristic determinant is affine in \(z=e^{-\lambda\tau_1}\). After multiplication by the positive constant \(26398437500\), the exact characteristic equation of printed (5.1) at \(E_p\) is
\[
P(\lambda)+Q(\lambda)e^{-\lambda\tau_1}=0,
\]
where
\[
\begin{{aligned}}
P(\lambda)&=26398437500\lambda^4+53324843750\lambda^3+36831100000\lambda^2\\
&\quad+9663940000\lambda+648768000,\\
Q(\lambda)&=-3907775000\lambda^3+1620372000\lambda^2+4248671870\lambda+1106585331.
\end{{aligned}}
\]
In particular, the \(e^{-2\lambda\tau_1}\) term appearing in equation (3.4) of the source cannot occur for this printed system.

Writing \(u=\omega^2\), the condition \(|P(i\omega)|=|Q(i\omega)|\) is
\[
\begin{{aligned}}
F(u)={}&696877502441406250000u^4+883701272698789062500u^3\\
&+324295356339287500000u^2+31137005266996967100u\\
&-803631176960379561=0.
\end{{aligned}}
\]
Because \(F(0)<0\), \(F(u)\to\infty\), and every coefficient of \(F'(u)\) is positive, there is exactly one positive root. It gives
\[
\omega_*=0.144795075416724097\ldots,
\qquad
\tau_{{1,*}}=13.8796022360614596\ldots.
\]
The corresponding simple root crosses with
\[
\operatorname{{Re}}\frac{{d\lambda}}{{d\tau_1}}
=0.001746287897922014\ldots>0.
\]
Thus this is the first loss of linear stability as \(\tau_1\) increases from zero. The source's values \(\omega_{{10}}=0.0786\) and \(\tau_{{10}}=9.3985\) are not a characteristic-root crossing of the printed system.

## Assumptions and scope
The calculation concerns the system exactly as printed in equation (5.1), with \(\tau_2=0\) and the numerical coefficients printed in Section 5. It does not silently replace \(0.48\) by the Table 1 value \(0.38\). For comparison only, using the Table 1 specialization of the general model instead gives the distinct equilibrium
\[
\left(\frac{{320}}{{197}},\frac{{1085565}}{{516928}},\frac{{399945}}{{516928}},\frac{{32457}}{{16154}}\right)
\approx(1.6243654822,2.1000313390,0.7736957565,2.0092237217),
\]
which also does not equal the displayed \(E^*\) to the printed precision.

The finding is a linear spectral correction. It does not assert the direction or orbital stability of a nonlinear Hopf branch at the corrected crossing, because the first Lyapunov coefficient was not recomputed there.

## Proof
Let \(c=d+\alpha_1+\gamma+\varepsilon=0.64\), \(h=0.48\), and let
\[
g(S,I)=\frac{{0.65SI}}{{1+0.4S}}.
\]
At a positive equilibrium of printed (5.1), the infected equation gives \(g(S,I)=cI\), hence
\[
\frac{{0.65S}}{{1+0.4S}}=0.64,
\]
which has the unique positive solution \(S=320/197\). The quarantine and recovered equations then give \(Q=(7/24)I\) and a linear relation between \(R\) and \(I\). Substitution into the susceptible equation yields the displayed rational values of \(I,Q,R\). This proves uniqueness of the positive equilibrium for the printed coefficients.

At \(E_p\), set
\[
a=\frac{{0.65I_p}}{{(1+0.4S_p)^2}}=\frac{{1038978}}{{2111875}}.
\]
For \(\tau_2=0\), the delayed infection linearization in the first two equations is
\[
\begin{{pmatrix}}-a&-c\\a&c\end{{pmatrix}},
\]
whose determinant is zero. Hence its contribution to the full characteristic determinant is rank one and the determinant is affine in \(e^{-\lambda\tau_1}\). Direct block elimination gives
\[
D(\lambda,\tau_1)=P_0(\lambda)+Q_0(\lambda)e^{-\lambda\tau_1},
\]
with
\[
P_0=(\lambda+d)(\lambda+c)(\lambda+h)(\lambda+d+\delta)
\]
and
\[
Q_0=[a(\lambda+c)-c(\lambda+d)](\lambda+h)(\lambda+d+\delta)
-a\delta[\gamma(\lambda+h)+\eta\varepsilon].
\]
Clearing denominators yields the displayed integer polynomials \(P,Q\).

At \(\tau_1=0\), \(P+Q\) is the quartic
\[
26398437500\lambda^4+49417068750\lambda^3+38451472000\lambda^2+13912611870\lambda+1755353331.
\]
Its coefficients are positive and its nontrivial Hurwitz determinants are
\[
\Delta_2=1532887820450746875000>0,
\]
\[
\Delta_3=17039818505241533448549351562500>0,
\]
so \(E_p\) is linearly asymptotically stable at zero delay.

A purely imaginary root \(\lambda=i\omega\), \(\omega>0\), requires \(|P(i\omega)|=|Q(i\omega)|\). Squaring and putting \(u=\omega^2\) gives the displayed quartic \(F\). Its derivative is strictly positive for \(u>0\), so the positive root is unique. At that root,
\[
z_*=-\frac{{P(i\omega_*)}}{{Q(i\omega_*)}}
=-0.4249455429076618\ldots-0.9052189158225277\ldots i,
\]
with \(|z_*|=1\). Solving \(e^{-i\omega_*\tau_1}=z_*\) gives the smallest positive delay \(\tau_{{1,*}}=13.8796022360614596\ldots\). The next positive phase branch is larger by \(2\pi/\omega_*=43.39363952189956\ldots\), so no earlier imaginary crossing exists. Also \(D(0,\tau_1)=P(0)+Q(0)>0\) for every delay, so zero is never a characteristic root. Standard continuity of characteristic roots for retarded equations then shows that stability cannot change before \(\tau_{{1,*}}\). Implicit differentiation of \(D=0\) gives
\[
\frac{{d\lambda}}{{d\tau_1}}=
\frac{{\lambda Q(\lambda)e^{-\lambda\tau_1}}}
{{P'(\lambda)+(Q'(\lambda)-\tau_1Q(\lambda))e^{-\lambda\tau_1}}},
\]
whose real part at the crossing is positive as displayed.

Finally, the paper's reported frequency fails even the delay-independent modulus condition: for \(\omega=0.0786\), the exact rational value of \(F(\omega^2)\) is nonzero and negative. Therefore no choice of \(\tau_1\) can make \(i0.0786\) a root of the correct characteristic equation.

## Verification
The accompanying `verify.py` uses only the Python standard library. It reconstructs the rational equilibrium, checks the Table 1 coefficient mismatch, proves the displayed equilibrium residual cannot be a rounding artifact, reconstructs \(P,Q\), checks the zero-delay Hurwitz determinants, derives the exact modulus polynomial \(F\), certifies that the source frequency fails \(F=0\), brackets the unique positive root, reconstructs the first phase delay, and checks the positive transversality derivative. A successful replay prints `VERIFY_OK`.

The symbolic steps are exact rational arithmetic except for the final bisection, phase, and derivative evaluations, whose tolerances are explicitly tested. No trajectory simulation is needed.

## Relationship to prior work
Yang and Zhang formulate the general delayed SIQRS system, derive a characteristic equation, state a first-delay Hopf theorem, and in Section 5 report \(E^*=(1.6244,2.0598,0.7739,2.0011)\), \(\omega_{{10}}=0.0786\), and \(\tau_{{10}}=9.3985\) for system (5.1). The source itself does not state the rank-one cancellation, the corrected positive equilibrium of printed (5.1), or the corrected first characteristic crossing above.

A later SEIQRS article that cites this model reproduces the general quarantine equation with removal coefficient \(d+\alpha_2+\eta\); this supports reading Table 1 against the original general equation but does not supply the source-specific equilibrium and spectral correction proved here. Searches using the DOI, the displayed equilibrium, the two reported threshold numbers, and characteristic-equation aliases found no corrigendum or published result that implies this correction. Those searches reduce, but do not eliminate, the risk of an unindexed prior correction.

## Limitations
The analysis is tied to the printed system (5.1) and to the one-delay case \(\tau_2=0\). It does not repair the paper's other delay cases or recompute its nonlinear center-manifold coefficient. The corrected crossing is therefore called a first linear stability crossing rather than a fully re-established nonlinear Hopf theorem.

The literature comparison included the full original article and a related later SEIQRS paper, plus targeted searches for the exact numerical values and algebraic structure. It was not an exhaustive search of every non-indexed thesis, preprint, or commentary.

## References
1. F. Yang and Z. Zhang, “Dynamics of a nonlinear SIQRS computer virus spreading model with two delays,” *AIMS Mathematics* 6(4) (2021), 4083–4104, DOI: 10.3934/math.2021242. Published 04 February 2021; primary MSC 34C23.
2. Related SEIQRS analysis reproducing the general Yang–Zhang quarantine-removal structure: PMC12136457.
