# A sharp parity-monotonicity threshold for variance-one Student tails
## Finding
Let \(T_n\) have Student's \(t\)-distribution with integer degrees of freedom \(n\ge3\), and normalize it to variance one by
\[
Z_n=\sqrt{\frac{n-2}{n}}\,T_n.
\]
Write \(J_n(y)=\Pr\{|Z_n|<y\}\). Then
\[
J_{n+2}(y)<J_n(y)\qquad(n\ge3,\ 0<y\le\sqrt3).
\]
The endpoint \(\sqrt3\) is sharp uniformly in the degree: for every fixed \(y>\sqrt3\), the reverse inequality \(J_{n+2}(y)>J_n(y)\) holds for all sufficiently large \(n\).

On the same interval \(J_3(y)>J_4(y)\). Thus \(J_3(y)\) uniquely maximizes central mass over all integer degrees, and
\[
\inf_{n\ge3}\Pr\{|Z_n|\ge y\}
=1-\frac{2}{\pi}\left(\arctan y+\frac{y}{1+y^2}\right),
\qquad 0<y\le\sqrt3,
\]
with equality only for \(n=3\).

## Assumptions and scope
The degrees of freedom are integers \(n\ge3\), so the variance exists and equals \(n/(n-2)\) before standardization. The result concerns centered two-sided probabilities at a common variance. It does not claim monotonicity between consecutive degrees, nor a complete optimizer classification for \(y>\sqrt3\).

The lead source Hu--Song--Tan studies this same normalized Student anti-concentration problem. For \(0<y<\sqrt6/2\) its Theorem 2.4 reduces the answer to a finite maximization over degrees, and Remark 2.5 proves the same-parity inequality only for \(0<y\le1\). The finding here identifies the degree-three optimizer on a larger interval and locates the sharp uniform same-parity threshold.

## Proof
Put \(s=y^2\). The exact beta-density recurrence in Hu--Song--Tan gives
\[
J_{n+2}(y)<J_n(y)
\quad\Longleftrightarrow\quad
1<n\int_1^{L_n}R_{n,s}(t)\,dt,
\]
where
\[
L_n=\sqrt{\frac n{n-2}},
\qquad
R_{n,s}(t)=\left(\frac{n+s}{n+s t^2}\right)^{(n+1)/2}.
\]
For \(t>1\),
\[
\frac{\partial}{\partial s}\log R_{n,s}(t)
=\frac{n+1}{2}\frac{n(1-t^2)}{(n+s)(n+s t^2)}<0.
\]
Hence for \(0<s\le3\) it suffices to prove the integral inequality at \(s=3\).

For \(s=3\), \(t\mapsto R_{n,3}(t)\) is strictly convex on \(t\ge1\), because the sign factor in its second derivative is
\[
3(n+2)t^2-n>0.
\]
Jensen's inequality therefore yields
\[
n\int_1^{L_n}R_{n,3}(t)\,dt
\ge B_n:=n(L_n-1)R_{n,3}\!\left(\frac{1+L_n}{2}\right).
\]
We show \(B_n>1\).

For \(n\ge4\), set \(x=L_n\), so \(1<x\le\sqrt2\) and \(n=2x^2/(x^2-1)\). Write \(n(x-1)=1+u\) and
\[
R_{n,3}\!\left(\frac{1+x}{2}\right)=(1+d)^{-(n+1)/2},
\]
where
\[
u=\frac{(x-1)(2x+1)}{x+1},
\qquad
d=\frac{3(x-1)^2(x+1)(x+3)}{4(5x^2-3)}.
\]
Using \(\log(1+u)\ge2u/(2+u)\) and \(\log(1+d)\le d\), direct algebra gives
\[
\log B_n\ge
-\frac{(x-1)^2P(x)}{8(5x^2-3)(2x^2+x+1)},
\]
where
\[
P(x)=18x^4+81x^3-49x^2-123x-39.
\]
Now \(P''(x)=216x^2+486x-98>0\) for \(x\ge1\), and \(P'(1)=94>0\), so \(P\) increases on \([1,\sqrt2]\). Also
\[
P(\sqrt2)=-65+39\sqrt2<0,
\]
because \(\sqrt2<5/3\). Thus \(P(x)<0\) throughout that interval, giving \(B_n>1\).

For \(n=3\),
\[
B_3=\frac{48(\sqrt3-1)}{(\sqrt3+4)^2},
\qquad
B_3-1=\frac{-67+40\sqrt3}{(\sqrt3+4)^2}>0,
\]
since \(40\sqrt3>67\). This proves \(J_{n+2}(y)<J_n(y)\) for all claimed \(n\) and \(y\).

To compare the parity chains, direct integration gives
\[
J_3(y)=\frac2\pi\left(\arctan y+\frac{y}{1+y^2}\right),
\qquad
J_4(y)=\frac{y(y^2+3)}{(y^2+2)^{3/2}}.
\]
For \(D(y)=J_3(y)-J_4(y)\),
\[
D'(y)=\frac4{\pi(1+y^2)^2}-\frac6{(y^2+2)^{5/2}}.
\]
The condition \(D'(y)>0\) is equivalent to
\[
h(y^2)>\frac{3\pi}{2},
\qquad
h(q)=\frac{(q+2)^{5/2}}{(q+1)^2}.
\]
Since
\[
\frac d{dq}\log h(q)=\frac{q-3}{2(q+1)(q+2)},
\]
there is at most one sign change of \(D'\) on \(0<y<\sqrt3\), and it can only be from positive to negative. Also \(D'(0)>0\), while
\[
D(\sqrt3)=\frac23+\frac{\sqrt3}{2\pi}-\frac{6\sqrt{15}}{25}>0.
\]
For the final strict inequality, \(\pi<22/7\), \(\sqrt3>5/3\), and \(\sqrt{15}<31/8\) give the lower bound \(41/44-93/100=1/550\). Therefore \(D(y)>0\) throughout the interval.

Finally, the sharpness of \(\sqrt3\) follows from the large-degree expansion of the variance-one Student density. Uniformly for fixed bounded \(x\), Stirling's expansion and the Student kernel expansion through the next order give
\[
g_n(x)=\phi(x)\left[1+\frac{x^4-6x^2+3}{4n}+\frac{3x^8-52x^6+246x^4-396x^2+123}{96n^2}+O(n^{-3})\right].
\]
The first correction integrates using \(\frac d{dx}[(x^3-3x)\phi(x)]=-(x^4-6x^2+3)\phi(x)\). For the second correction, if
\[
Q(x)=-\frac{x^7}{32}+\frac{31x^5}{96}-\frac{91x^3}{96}+\frac{41x}{32},
\]
then \(Q'(x)-xQ(x)=(3x^8-52x^6+246x^4-396x^2+123)/96\). Hence
\[
J_n(y)=2\Phi(y)-1+\frac{y(3-y^2)\phi(y)}{2n}+\frac{2Q(y)\phi(y)}{n^2}+O_y(n^{-3}).
\]
Differencing this full expansion gives
\[
J_{n+2}(y)-J_n(y)
=\frac{y(y^2-3)\phi(y)}{n^2}+O_y(n^{-3}).
\]
For every fixed \(y>\sqrt3\), the leading coefficient is positive, so the same-parity inequality eventually reverses. This establishes sharpness of the endpoint.

## Verification
The accompanying `verify.py` checks the endpoint Jensen margin over thousands of degrees, verifies the closed forms for \(J_3\) and \(J_4\) against direct quadrature, stress-tests the same-parity inequalities through \(y=\sqrt3\), and confirms the predicted large-degree reversal above the threshold. These computations are supplementary checks; the infinite statements follow from the analytic proof.

## Relationship to prior work
Hu, Song and Tan, arXiv:2401.09998v1, formulate the same variance-normalized Student anti-concentration problem and derive the exact same-parity comparison used above. Their Theorem 2.4 gives a finite-degree maximization formula for \(0<y<\sqrt6/2\), and Remark 2.5 proves \(J_{n+2}(y)<J_n(y)\) for \(0<y\le1\). The inspected source does not state the extension through \(\sqrt3\), identify \(\sqrt3\) as the sharp threshold, or give the degree-three envelope on this larger interval.

Sun, Hu and Sun, arXiv:2304.11459v2, prove a variance-comparison inequality at one standard deviation for Student laws. That fixed-threshold result does not imply the phase boundary or the degree-three extremizer over the interval proved here.

## Limitations
The theorem is restricted to integer degrees \(n\ge3\). Above \(\sqrt3\), only eventual reversal within each parity chain is proved; the complete finite-degree optimizer map is not classified. The originality search was broad but cannot exclude an unindexed equivalent result.

## References
1. Z.-C. Hu, R. Song, Y. Tan, “On the anti-concentration functions of some familiar families of distributions,” arXiv:2401.09998v1, first public 2024-01-18; Mathematical Theory and Applications 44 (2024), 1–15.
2. P. Sun, Z.-C. Hu, W. Sun, “Variation comparison between infinitely divisible distributions and the normal distribution,” arXiv:2304.11459v2, first public 2023-04-22; Statistical Papers 65 (2024), 4405–4429.
