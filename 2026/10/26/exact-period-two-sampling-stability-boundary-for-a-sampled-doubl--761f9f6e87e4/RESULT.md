# Exact period-two sampling stability boundary for a sampled double integrator

## Finding

Consider the double integrator
\[
\dot q(t)=v(t),\qquad \dot v(t)=u(t),
\]
with sampled proportional-derivative feedback held constant between samples:
\[
u(t)=-k_p q(t_j)-k_d v(t_j),\qquad t\in[t_j,t_{j+1}),
\]
where \(k_p>0\), \(k_d>0\), and the sampling intervals alternate between two fixed values \(a,b>0\). Define
\[
h_*:=\min\!\left\{\frac{2}{k_d},\frac{2k_d}{k_p}\right\},
\qquad
\Phi(a,b;k_p,k_d):=k_p^2a^2b^2+4ab(k_d^2-k_p)-4k_d(a+b)+8.
\]
The constant-period sampled map is Schur stable exactly when \(0<h<h_*\). If both \(a,b\in(0,h_*)\), the two-step monodromy is Schur stable if and only if
\[
\boxed{\Phi(a,b;k_p,k_d)>0.}
\]
At \(\Phi=0\), the monodromy has a simple multiplier \(-1\); at \(\Phi<0\), it has a real multiplier strictly less than \(-1\). Thus stability at each of two fixed sampling intervals does not imply stability when those intervals alternate.

## Assumptions and scope

The plant is exactly \(\ddot q=u\), the state \((q,v)\) is sampled without delay, the controller uses fixed positive gains \(k_p,k_d\), and the input is held by a zero-order hold. The interval sequence is exactly period two, \(a,b,a,b,\ldots\), with \(a,b>0\). Stability means Schur stability of the sample-to-sample period map. No actuator saturation, measurement noise, transport delay, nonlinear plant term, or arbitrary aperiodic interval sequence is included.

## Proof

For an interval of length \(h\), integrating the constant input gives
\[
\begin{pmatrix}q_{j+1}\\v_{j+1}\end{pmatrix}
=M(h)\begin{pmatrix}q_j\\v_j\end{pmatrix},
\qquad
M(h)=\begin{pmatrix}
1-\frac{k_ph^2}{2}&h-\frac{k_dh^2}{2}\\
-k_ph&1-k_dh
\end{pmatrix}.
\]
Its trace and determinant are
\[
\operatorname{tr}M(h)=2-k_dh-\frac{k_ph^2}{2},\qquad
\det M(h)=1-k_dh+\frac{k_ph^2}{2}.
\]
For a real monic quadratic, the Schur--Jury conditions are \(|d|<1\), \(1-t+d>0\), and \(1+t+d>0\), where \(t\) and \(d\) are the trace and determinant of the corresponding two-by-two matrix. Here these expressions reduce to
\[
1-\operatorname{tr}M+\det M=k_ph^2>0,
\]
\[
1+\operatorname{tr}M+\det M=4-2k_dh,
\qquad
1-\det M=k_dh-\frac{k_ph^2}{2}.
\]
Also \(1+\det M=2-k_dh+k_ph^2/2>0\) whenever \(h<2/k_d\). Therefore \(M(h)\) is Schur stable exactly for \(0<h<h_*\).

For the alternating schedule the two-step matrix is \(P=M(b)M(a)\). Direct multiplication yields
\[
1-\operatorname{tr}P+\det P
=k_p(a+b)(a+b-k_dab),
\]
\[
2\bigl(1+\operatorname{tr}P+\det P\bigr)
=\Phi(a,b;k_p,k_d),
\]
and \(\det P=\det M(a)\det M(b)\). If \(a,b<h_*\), then \(|\det P|<1\). Moreover, \(a,b<2/k_d\) implies \(1/a+1/b>k_d\), hence \(a+b-k_dab>0\). Thus the first Schur--Jury inequality is strictly positive, and the only remaining nonautomatic condition is \(1+\operatorname{tr}P+\det P>0\), exactly \(\Phi>0\).

Let \(p(z)=z^2-\operatorname{tr}(P)z+\det P\). If \(\Phi=0\), then \(p(-1)=0\); its other root is \(-\det P\), which lies strictly inside the unit disk, so the multiplier \(-1\) is simple. If \(\Phi<0\), then \(p(-1)<0\) while \(p(z)\to+\infty\) as \(z\to-\infty\), so a real root lies below \(-1\).

An exact witness is \(k_p=2\), \(k_d=3/2\), \(a=1/10\), and \(b=13/10\). Here \(h_*=4/3\), so both fixed-period maps are Schur stable, but
\[
\Phi=-\frac{253}{1250}<0,\qquad
\operatorname{tr}P=-\frac{1086}{625},\qquad
\det P=\frac{1591}{2500}.
\]
The exact characteristic polynomial satisfies \(p(-2)=2903/2500>0\) and \(p(-1)=-253/2500<0\), proving a multiplier in \((-2,-1)\).

## Verification

The included `verify.py` reconstructs \(M(h)\) and \(P\) symbolically, checks the trace, determinant, and both Schur expressions, and replays the rational witness with exact arithmetic. Its output is recorded in `verification_output.txt`. The infinite-parameter criterion is proved algebraically above; finite computation is used only to check the displayed identities and witness.

## Relationship to prior work

Sampled-data control literature studies stability when sampling intervals vary and uses discrete-time lifting, quadratic Lyapunov inequalities, or robust sufficient conditions. Fujioka's 2008 IFAC paper explicitly notes that a constant interval can be checked through the spectral radius of its sampled map, while uncertain varying intervals require a condition holding over a range of interval values. Guo's work on nonequidistant sampling and Fujioka's later aperiodic sample-and-hold analysis address the broader stability problem. The present statement is a closed-form necessary-and-sufficient boundary for one fixed proportional-derivative law on the double integrator under a two-period interval sequence; it is not a claim that period-two monodromy or Schur--Jury theory is new.

## Limitations

The exact condition does not decide stability for general nonperiodic sequences, where products of more than two distinct sample maps matter. The result is specific to the double integrator and fixed positive proportional-derivative gains. It gives no performance or robustness margin for perturbations of the gains or interval lengths. A prior specialized calculation with the same four-parameter boundary may exist in literature not found in the inspected sources; the result is presented as a best-knowledge exact characterization, not a proof of global priority.

## References

1. H. Fujioka, “Stability Analysis for a Class of Networked/Embedded Control Systems: Output Feedback Case,” Proceedings of the 17th IFAC World Congress, 2008, pp. 4210–4215. DOI: 10.3182/20080706-5-KR-1001.2831.
2. G. Guo, “Systems with Nonequidistant Sampling: Controllable? Observable? Stable?,” Asian Journal of Control 7 (2005), 455–461; first published 22 October 2008. DOI: 10.1111/j.1934-6093.2005.tb00409.x.
3. H. Fujioka, “A Discrete-Time Approach to Stability Analysis of Systems With Aperiodic Sample-and-Hold Devices,” IEEE Transactions on Automatic Control 54(10) (2009), 2440–2445. DOI: 10.1109/TAC.2009.2029304.
4. M. G. Titton, J. M. Gomes da Silva Jr., G. Valmorbida, and M. Jungers, “Stability analysis of Lur'e systems under aperiodic sampled-data control,” International Journal of Robust and Nonlinear Control 33(12) (2023), 7130–7153. DOI: 10.1002/rnc.6744.
