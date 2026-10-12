# Exact equilateral crossover from positive band density to logarithmic momentum measure
## Finding
For the periodic ring-chain model with \(\gamma=0\), \(\ell_1=\ell_2=\ell_3=\pi\), coupling length \(\ell>0\), and interpolation parameter \(t\in[0,1]\), let
\[
\Sigma_t:=\{k\ge0:k^2\in\sigma(H_{0,t})\},\qquad
b_t:=\ell\tan\!\left(\frac{\pi t}6\right),
\]
and
\[
A(y):=\frac{2\sqrt2}3\,\frac{\sqrt{3y+1}}{y+1}.
\]
Every positive integer \(m\) is a flat-band momentum. For each noninteger \(k>0\),
\[
k\in\Sigma_t
\quad\Longleftrightarrow\quad
|\sin(\pi k)|\le A(b_t^2k^2).
\]
The threshold satisfies
\[
1-A(y)^2=\frac{(3y-1)^2}{9(y+1)^2},
\]
so \(A(y)\le1\), with equality exactly at \(y=1/3\).

For fixed \(t>0\),
\[
|\Sigma_t\cap[0,K]|
=
\frac{4\sqrt6}{3\pi b_t}\log K+O(1).
\]
If instead \(t=t_K=\tau/K\) for a fixed \(\tau\ge0\), then
\[
\frac{|\Sigma_{t_K}\cap[0,K]|}{K}
\longrightarrow
\Phi_\ell(\tau):=
\int_0^1\frac2\pi\arcsin\!\left[
A\!\left(\left(\frac{\pi\ell\tau x}6\right)^2\right)
\right]\,dx.
\]
In particular,
\[
\Phi_\ell(0)=\frac2\pi\arcsin\!\left(\frac{2\sqrt2}3\right)
=0.7836531040\ldots,
\]
while
\[
\Phi_\ell(\tau)=
\frac{8\sqrt6}{\pi^2\ell\tau}
\log\!\left(\frac{\pi\ell\tau}6\right)
+O(\tau^{-1})
\qquad(\tau\to\infty).
\]

## Assumptions and scope
The graph and vertex conditions are those of Exner--Pekař's interpolation family. The specialization is \(\gamma=0\) and \(\ell_1=\ell_2=\ell_3=\pi\); their normalization \(\ell_2+\ell_3=2\pi\) is therefore respected. The symbol \(\ell\) denotes the length scale in the vertex condition, not an edge length. The statement concerns the nonnegative spectrum and its momentum image. Flat-band points have zero Lebesgue measure and therefore do not alter the measure asymptotics.

The fixed-\(t\) asymptotic is asserted only for \(t>0\). The scaled limit uses \(t_K=\tau/K\), which lies in \([0,1]\) for all sufficiently large \(K\). No statement is made about negative bands.

## Proof
For \(\gamma=0\), the source gives \(P_5=P_3=P_1=P_0=0\) and explicit formulas for \(P_6,P_4,P_2,P_c,P_s\). Under \(\ell_1=\ell_2=\ell_3=\pi\), put
\[
s:=\sin(\pi k),\qquad c:=\cos\!\left(\frac{\pi t}3\right).
\]
Then \(P_s=0\), while the remaining coefficients reduce exactly to
\[
P_6=72\ell^6(c-1)^2s^3,
\]
\[
P_4=48\ell^4(c^2-1)s(2-3s^2),
\]
\[
P_2=8\ell^2(c+1)^2s(-4+9s^2),
\]
and
\[
P_c=-32\ell^2(c+1)
\left[3k^2\ell^2(c-1)-(c+1)\right]s.
\]
The source's exact secular equation
\[
k^6P_6+k^4P_4+k^2P_2+k^2P_c\cos\theta=0
\]
therefore has an overall factor \(s\). The case \(s=0\), i.e. \(k\in\mathbb N\), is the flat-band branch already identified by the source.

For \(s\ne0\), divide by \(8k^2\ell^2(c+1)^2s\) and use
\[
q:=\frac{1-c}{1+c}=\tan^2\!\left(\frac{\pi t}6\right),
\qquad y:=k^2\ell^2q=b_t^2k^2.
\]
The secular equation becomes
\[
9(y+1)^2\sin^2(\pi k)
=
8(3y+1)\sin^2\!\left(\frac\theta2\right).
\]
Because \(\sin^2(\theta/2)\) ranges over \([0,1]\), a real Floquet phase exists exactly when
\[
|\sin(\pi k)|
\le
\frac{2\sqrt2}3\frac{\sqrt{3y+1}}{y+1}
=A(y).
\]
Also
\[
1-A(y)^2
=
\frac{9(y+1)^2-8(3y+1)}{9(y+1)^2}
=
\frac{(3y-1)^2}{9(y+1)^2},
\]
proving the sharp bound on \(A\).

For the measure asymptotics, on one unit cell the periodic function \(|\sin(\pi k)|\) spends the fraction
\[
p(y):=\frac2\pi\arcsin A(y)
\]
below a frozen threshold \(A(y)\). For fixed \(t>0\),
\[
A(b_t^2k^2)=\frac{2\sqrt6}{3b_tk}+O(k^{-3}),
\]
and its variation across a unit cell is \(O(k^{-2})\). Hence the actual spectral measure of \([n,n+1]\) is
\[
\frac{4\sqrt6}{3\pi b_t}\frac1n+O(n^{-2}).
\]
Summation gives the logarithmic law with an \(O(1)\) remainder.

For \(t_K=\tau/K\),
\[
K\tan\!\left(\frac{\pi t_K}6\right)\longrightarrow\frac{\pi\tau}6.
\]
Partition \([0,K]\) into unit cells. On the cell with \(k/K\to x\), the threshold converges uniformly to
\[
A\!\left(\left(\frac{\pi\ell\tau x}6\right)^2\right).
\]
The same one-cell phase average and a Riemann-sum argument yield the formula for \(\Phi_\ell(\tau)\).

Finally, with \(a=\pi\ell\tau/6\),
\[
\Phi_\ell(\tau)=\frac1a\int_0^a p(z^2)\,dz.
\]
Since
\[
p(z^2)=\frac{4\sqrt6}{3\pi z}+O(z^{-3})
\qquad(z\to\infty),
\]
integration gives
\[
\Phi_\ell(\tau)
=
\frac{4\sqrt6}{3\pi}\frac{\log a}{a}+O(a^{-1}),
\]
which is the stated large-\(\tau\) asymptotic.

## Verification
The bundled `verify.py` evaluates the source's unsimplified \(\gamma=0\) equilateral coefficients and the reduced secular expression on a deterministic grid of \((k,t,\theta,\ell)\) values, checking agreement to floating-point tolerance. It separately checks the identity for \(1-A(y)^2\), the coefficient of the \(k^{-1}\) phase fraction, and numerical convergence of the scaled density integral. These computations corroborate the algebra; the proof above is analytic and does not infer an infinite statement from finite sampling.

## Relationship to prior work
Exner and Pekař derive the exact general secular equation, give the simplified \(\gamma=0\) coefficients used above, identify the corresponding flat bands, and prove that a degree-three chain has zero limiting band probability for every fixed \(t\in(0,1]\). They also emphasize that the \(t\to0^+\) spectral convergence is uniform only on bounded energy intervals, because the \(t=0\) momentum-band probability is nonzero whereas it vanishes at every fixed positive \(t\). The exact equilateral reduction above is not stated there, nor is the logarithmic fixed-\(t\) momentum measure or the \(t\asymp K^{-1}\) crossover function.

Band and Berkolaiko introduced momentum band density as the asymptotic fraction of momenta lying in the spectrum. Their framework motivates the observable used here but does not supply this interpolation-dependent crossover.

## Limitations
The exact reduction uses the maximally symmetric edge choice \(\ell_1=\ell_2=\ell_3=\pi\) and \(\gamma=0\). It does not classify the analogous crossover for unequal or incommensurate lengths, for \(\gamma\ne0\), or for negative spectrum. The \(O(1)\) remainder in the fixed-\(t\) measure law is not evaluated in closed form. The result concerns Lebesgue measure of the momentum spectrum, not integrated density of states.

## References
1. P. Exner and J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, arXiv:2403.09457v1 (2024); Journal of Mathematical Physics 65, 092102 (2024), doi:10.1063/5.0208361.
2. R. Band and G. Berkolaiko, *Universality of the momentum band density of periodic networks*, arXiv:1304.6028; Physical Review Letters 111, 130404 (2013).
