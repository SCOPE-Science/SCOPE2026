# Exact renewal-protocol optimum for first detection on the fully connected quantum model
## Finding
For the fully connected quantum Hamiltonian \(H=-J\sum_{x,y=1}^N |x\rangle\langle y|\) with \(J>0\), target subspace \(A=\operatorname{span}\{|m+1\rangle,\ldots,|N\rangle\}\), and initial uniform survivor state \(|b\rangle=m^{-1/2}\sum_{x=1}^m|x\rangle\), consider projective detection attempts separated by i.i.d. waiting times \(\tau\ge0\) with finite positive mean. Put \(\omega=NJ\), \(\beta=4m(N-m)/N^2\), and let \(x_*\in(\pi/2,\pi)\) be the unique root of \(\tan(x_*/2)=x_*\). Then every renewal waiting-time law with finite mean first-detection time satisfies
\[
T\ge \frac{2}{\beta\omega\sin x_*}=\frac{N}{2m(N-m)J\sin x_*},
\]
where \(x_*=2.331122370414422\ldots\) and \(\sin x_*=0.724611353776708\ldots\). Equality is attained by the deterministic protocol \(\tau=x_*/(NJ)\); if zero waiting times are allowed, arbitrary extra mass at \(0\) preserves equality. Among exponential waiting laws the optimum is instead at rate \(r=NJ\) with \(T_{\mathrm{Pois}}^{\min}=N/[m(N-m)J]\), so the globally optimal renewal protocol has the exact ratio \(T_{\min}/T_{\mathrm{Pois}}^{\min}=1/(2\sin x_*)=0.690025069844650\ldots\), a \(30.9975\%\) reduction.

This optimizes the entire i.i.d. renewal waiting-time law for the canonical bright state supported uniformly on the unmeasured sites. The recent fully connected model was solved in detail for Poissonian probing and explicitly left comparison of different measurement protocols as a future direction.

## Assumptions and scope
Let \(N\ge2\), \(1\le m\le N-1\), and \(J>0\). The target is
\[
A=\operatorname{span}\{|m+1\rangle,\ldots,|N\rangle\},
\]
and its orthogonal complement is supported on the first \(m\) sites. The initial state is
\[
|b\rangle=\frac1{\sqrt m}\sum_{x=1}^m|x\rangle.
\]
Measurement attempts use the projectors onto \(A\) and \(A^\perp\). Waiting times are independent and identically distributed on \([0,\infty)\) with \(0<\mathbb E\tau<\infty\). The theorem concerns the mean elapsed time to the first successful detection. It does not optimize non-renewal, history-dependent, weak-measurement, or adaptive protocols.

## Proof
Write \(|u\rangle=N^-0.5\sum_{x=1}^N|x\rangle\). Then
\[
H=-NJ|u\rangle\langle u|,
\qquad
U_\tau=I+(e^{i\omega\tau}-1)|u\rangle\langle u|,
\qquad \omega=NJ.
\]
Since \(\langle u|b\rangle=\sqrt{m/N}\), one attempt after a waiting time \(\tau\) succeeds with probability
\[
p(\tau)=\|P_AU_\tau|b\rangle\|^2
=\frac{4m(N-m)}{N^2}\sin^2\!\left(\frac{\omega\tau}2\right)
=\frac\beta2(1-\cos(\omega\tau)),
\]
where \(\beta=4m(N-m)/N^2\). More importantly,
\[
P_{A^\perp}U_\tau|b\rangle
=\left[1+\frac mN(e^{i\omega\tau}-1)\right]|b\rangle.
\]
Thus every failed measurement resets the normalized state exactly to \(|b\rangle\), up to a phase. The successive trials are therefore identically distributed. If \(\bar p=\mathbb E[p(\tau)]>0\), the attempt number is geometric. Moreover, the event that attempt \(i\) is reached depends only on earlier waiting times and outcomes, so it is independent of the current \(\tau_i\). Consequently
\[
T=\sum_{i\ge1}\mathbb E[\tau_i\mathbf 1_{\{K\ge i\}}]
=\mathbb E\tau\sum_{i\ge1}(1-\bar p)^{i-1}
=\frac{\mathbb E\tau}{\bar p}.
\]
If \(\bar p=0\), the mean detection time is infinite and the claimed lower bound is automatic.

Put \(X=\omega\tau\). For \(X\) with finite positive mean,
\[
T=\frac2{\beta\omega}\frac{\mathbb E X}{\mathbb E(1-\cos X)}.
\]
Define \(g(x)=(1-\cos x)/x\) for \(x>0\). Its derivative has the sign of
\[
x\sin x-(1-\cos x)
=2\sin(x/2)\bigl(x\cos(x/2)-\sin(x/2)\bigr).
\]
On \((0,\pi)\), stationary points therefore satisfy \(\tan(x/2)=x\). The function \(h(x)=\tan(x/2)-x\) decreases up to \(\pi/2\), has \(h(\pi/2)=1-\pi/2<0\), and then increases strictly to \(+\infty\) as \(x\uparrow\pi\). Hence there is a unique root \(x_*\in(\pi/2,\pi)\). At that root,
\[
\frac{1-\cos x_*}{x_*}=\sin x_*.
\]
For \(x\ge\pi\), \(g(x)\le2/x\le2/\pi<\sin x_*\), so \(x_*\) is the unique positive global maximizer. Therefore
\[
\mathbb E(1-\cos X)=\mathbb E[Xg(X)]\le \sin x_*\,\mathbb E X,
\]
which gives the stated lower bound. Equality requires positive \(X\)-mass only at maximizers of \(g\), hence at \(x_*\); mass at \(X=0\) is harmless because it contributes zero to both expectations. In particular, \(\tau=x_*/\omega\) attains the optimum.

For an exponential waiting law of rate \(r\),
\[
\mathbb E\cos(\omega\tau)=\frac{r^2}{r^2+\omega^2},
\]
so
\[
T_{\mathrm{Pois}}(r)=\frac2{\beta\omega}\left(\frac r\omega+\frac\omega r\right).
\]
This is minimized at \(r=\omega\), yielding \(4/(\beta\omega)=N/[m(N-m)J]\). Dividing the global renewal optimum by this value gives \(1/(2\sin x_*)\).

## Verification
The proof is analytic and does not rely on finite sampling. The bundled script `artifacts/verify.py` independently checks the root and constants, the exact one-step transition formula and failed-state reset on several finite systems, the Poissonian optimum, and the renewal inequality on a deterministic grid of finite-support waiting laws. Those computations corroborate, but do not replace, the global maximization argument above.

## Relationship to prior work
Del Vecchio Del Vecchio and Majumdar introduced and solved the same fully connected extended-target model for Poissonian projective measurements and explicitly identified comparison of different measurement protocols as future work. Their general setup already allows i.i.d. intervals, but their exact optimization is carried out for the Poissonian family. The present result uses the special reset structure of the uniform survivor state to optimize over all i.i.d. waiting-time laws, and it quantifies the strict gap to the best Poissonian law.

Kessler, Barkai, and Ziegler proved for finite-dimensional systems under i.i.d. random probing that mean first-detection time equals mean attempt number times mean waiting time, and studied how Gamma-distributed waiting times interpolate between deterministic and exponential probing. That general identity is consistent with the renewal step used here, but it does not supply the complete-graph extended-subspace success law, the global waiting-law optimizer, or the universal constant \(x_*\). Kulkarni and Majumdar treated general renewal measurement intervals in a resetting framework and derived universal short-time behavior; their result likewise does not give this exact all-laws optimum for the fully connected extended-target model.

## Limitations
The theorem is for the distinguished uniform state on \(A^\perp\), for which a failed measurement returns exactly to the same ray. It does not claim that deterministic probing is globally optimal for arbitrary initial bright states, arbitrary graphs, dependent intervals, adaptive schedules, weak measurements, or protocols with an external reset operation. The literature search found no equivalent all-renewal optimization for this model, but older work could conceivably contain the same scalar extremal reduction under different terminology.

## References
1. G. Del Vecchio Del Vecchio and S. N. Majumdar, “Optimal detection of quantum states via projective measurements,” arXiv:2509.08556; J. Phys. A: Math. Theor. 59 (2026) 035001, doi:10.1088/1751-8121/ae34fe.
2. D. A. Kessler, E. Barkai, and K. Ziegler, “The first detection time of a quantum state under random probing,” arXiv:2012.01763; Phys. Rev. A 103 (2021) 022222.
3. M. Kulkarni and S. N. Majumdar, “First detection probability in quantum resetting via random projective measurements,” arXiv:2305.15123.
