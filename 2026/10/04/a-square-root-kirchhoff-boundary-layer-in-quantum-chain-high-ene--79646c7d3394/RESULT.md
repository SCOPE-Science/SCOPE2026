# A square-root Kirchhoff boundary layer in quantum-chain high-energy bands
## Finding
For the periodic chain graph of Exner and Pekař at the Kirchhoff endpoint parameter \(\gamma=0\), a simultaneous high-energy/interpolation limit has a critical scale that is not visible in the fixed-parameter asymptotics. Let \(\ell_1,\ell_2,\ell_3>0\) satisfy \(\ell_2+\ell_3=2\pi\), let \(\ell>0\), and put \(k_m=m\pi/\ell_1\). Consider a subsequence of fixed parity \(\varepsilon=(-1)^m\) such that
\[
a_m=k_m\ell_2\pmod{2\pi}\to a,\qquad b_m=k_m\ell_3\pmod{2\pi}\to b,
\]
with \(\sin a\sin b\ne0\). If \(t_m>0\) and \(\sqrt m\,t_m\to\tau\in(0,\infty)\), then the Bloch band issued from \(k_m\) has
\[
k_{m,\theta}=k_m+\frac{x_\infty(\theta)}m+o(m^{-1})
\]
uniformly for \(\theta\in[-\pi,\pi]\), where
\[
x_\infty(\theta)=\frac{24\ell_1}{\pi^4\ell^2\tau^2}
\frac{\sin(a+b)-\varepsilon(\sin a+\sin b)\cos\theta}{\sin a\sin b}.
\]
Therefore
\[
k_{m,\theta}^2-k_m^2\to E_\infty(\theta)
=\frac{48}{\pi^3\ell^2\tau^2}
\frac{\sin(a+b)-\varepsilon(\sin a+\sin b)\cos\theta}{\sin a\sin b},
\]
and the translated band converges in Hausdorff distance to the interval traced by \(E_\infty\). Its limiting energy width is
\[
W_\infty=\frac{96}{\pi^3\ell^2\tau^2}
\left|\frac{\sin a+\sin b}{\sin a\sin b}\right|.
\]
In particular, whenever \(\sin a+\sin b\ne0\), the scale \(t_m\asymp m^{-1/2}\) produces a finite nonzero high-energy band width.

## Assumptions and scope
The claim concerns only the \(\ell_1\)-centered Bloch band near \(k_m=m\pi/\ell_1\), at \(\gamma=0\), along a fixed-parity subsequence with nonresonant phase limits \(\sin a\sin b\ne0\). It does not assert a global density-of-states limit, does not cover subsequences approaching the other Dirichlet centers, and does not cover \(\tau=0\) or \(\tau=\infty\). The case \(\sin a+\sin b=0\) is included algebraically, but its leading limiting width is zero and a finer scale would be needed to resolve the band.

## Proof
At \(\gamma=0\), Appendix A of arXiv:2403.09457v1 gives an exact real secular equation of the form
\[
F(k,\theta,t)=k^6P_6+k^4P_4+k^2P_2+k^2\bigl(\sin\theta\,P_s+\cos\theta\,P_c\bigr)=0,
\]
with the odd polynomial coefficients absent. Write \(c=\cos(\pi t/3)\). The exact coefficients needed at leading order are
\[
P_6=72\ell^6(c-1)^2\sin(k\ell_1)\sin(k\ell_2)\sin(k\ell_3),
\]
\[
P_4=12\ell^4(c-1)(c+1)B_4(k),
\]
\[
P_c=-16\ell^2(c+1)\bigl(3k^2\ell^2(c-1)-(c+1)\bigr)
\bigl(\sin(k\ell_2)+\sin(k\ell_3)\bigr),
\]
where
\[
B_4(k)=-4\sin(k\ell_1)+3\sin(k(\ell_1+\ell_2+\ell_3))
+\sin(k(\ell_1+\ell_2-\ell_3))
+\sin(k(\ell_2+\ell_3-\ell_1))
+\sin(k(\ell_3+\ell_1-\ell_2)).
\]
The remaining terms satisfy \(k^2P_2=O(m^2)\) and \(k^2P_s=O(m^{5/2})\) on the scale below, uniformly in \(\theta\).

Set \(k=k_m+x/m\) with bounded \(x\). Since \(\sqrt m\,t_m\to\tau\),
\[
c-1=-\frac{\pi^2\tau^2}{18m}+o(m^{-1}),\qquad c+1=2+o(1).
\]
Uniformly for bounded \(x\),
\[
\sin(k\ell_1)=\varepsilon\frac{\ell_1x}m+O(m^{-3}),
\]
while \(\sin(k\ell_2)=\sin a_m+O(m^{-1})\) and similarly for \(\ell_3\). At \(k=k_m\), elementary angle identities give
\[
B_4(k_m)=4\varepsilon\sin(a_m+b_m).
\]
Dividing the exact secular equation by \(m^3\) and passing to the subsequence limit therefore yields a nonzero common factor times
\[
\frac{\pi^4\ell^2\tau^2}{24\ell_1}\varepsilon x\sin a\sin b
-\varepsilon\sin(a+b)+(\sin a+\sin b)\cos\theta.
\]
The coefficient of \(x\) is nonzero because \(\sin a\sin b\ne0\). Uniform convergence on bounded \(x\) and compact \(\theta\)-sets, together with this nonvanishing limiting derivative, gives a unique nearby zero and uniform convergence to the displayed \(x_\infty(\theta)\). Finally,
\[
k^2-k_m^2=\frac{2\pi}{\ell_1}x+o(1),
\]
which gives the energy profile. Its range over \(\cos\theta\in[-1,1]\) is an interval with the stated width.

## Verification
The accompanying `verify.py` evaluates the exact \(\gamma=0\) secular coefficients rather than the limiting formula alone. For the replay family \(\ell_1=2\pi\), \(\ell_2=2\pi/3\), \(\ell_3=4\pi/3\), \(\ell=1\), \(m\equiv1\pmod6\), and \(\tau=1.4\), the phase limits are \(a=\pi/3\), \(b=2\pi/3\), and \(\varepsilon=-1\). Bisection of the exact secular equation at \(\theta=0\) and \(\theta=\pi\) converges toward the predicted limiting width
\[
\frac{128\sqrt3}{\pi^3\tau^2}=3.648084653737707\ldots.
\]
The absolute width errors at \(m=121,241,481,961\) are respectively approximately \(0.3435,0.1821,0.0939,0.0477\). A separate nontrivial Bloch phase check confirms decay of the scaled exact secular residual at the predicted root. The program prints `VERIFY_OK`.

## Relationship to prior work
arXiv:2403.09457v1 derives the exact chain-graph secular equation and fixed-\(t\) high-energy asymptotics. Its high-energy width formula for the \(\ell_1\)-centered family is proportional to \(m^{-1}\cot^2(\pi t/6)\), and the paper treats the endpoint \(t=0\) separately. The simultaneous regime \(t=t_m\to0\) with \(\sqrt m\,t_m\to\tau\) and the resulting finite translated-energy profile are not stated there.

The earlier square-lattice interpolation paper, arXiv:1804.01414v1, analyzes a different periodic graph and a different high-energy singular balance. It does not imply the chain-graph formula above.

## Limitations
The proof is local to a nonresonant \(\ell_1\)-centered branch. Resonant phase subsequences with \(\sin a\sin b=0\) require a different balance because another Dirichlet center approaches simultaneously. The result does not classify the regimes \(t_m\sqrt m\to0\) or \(t_m\sqrt m\to\infty\), and it does not establish a global spectral-measure law. Originality searches cannot exclude an equivalent statement published under substantially different terminology.

## References
1. P. Exner and J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, arXiv:2403.09457v1 (first public version 2024-03-14), especially Section IV and Appendix A. Primary MSC: 81Q35.
2. P. Exner, J. Lipovský, and P. Tater, *A family of quantum graph vertex couplings interpolating between different symmetries*, arXiv:1804.01414v1 (2018), for the distinct square-lattice interpolation comparison.
