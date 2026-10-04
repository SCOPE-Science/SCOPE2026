# Exact equilibrium census and unstable-index split for a sine-controlled multiscroll flow
## Finding
For the three-dimensional system
\[
\dot x_1=4.195x_1-4.295x_2+1.295x_3,
\]
\[
\dot x_2=3.1x_1-3.2x_2-6.1x_3,
\]
\[
\dot x_3=-7.605x_1+7.605x_2-1.905x_3+\frac{33}{10}\sin\!\left(\frac{47}{10}x_2\right),
\]
there are exactly 53 real equilibria. Every one is hyperbolic and unstable. Exactly 26 have unstable dimension two, while the other 27 have unstable dimension one.

More explicitly, put \(t=(47/10)x_2\). The equilibrium parameters are exactly the zeros of
\[
f(t)=t+\frac{231898}{2735}\sin t.
\]
There are exactly two positive zeros in each interval \(((2k-1)\pi,2k\pi)\), \(k=1,\ldots,13\), no other positive zeros, their 26 negatives, and \(t=0\). If a positive zero lies in the left half \(((2k-1)\pi,(2k-1/2)\pi)\), its equilibrium and the reflected equilibrium have unstable dimension two. If it lies in the right half \(((2k-1/2)\pi,2k\pi)\), both reflected equilibria have unstable dimension one. The origin also has unstable dimension one.

## Assumptions and scope
The statement concerns the vector field printed as Equation (3) by Ye and He at their principal chaotic parameter values \(\varepsilon_2=3.3\) and \(\sigma_2=4.7\). The decimal coefficients are interpreted exactly as the terminating decimals printed in the vector field; equivalently, they are the exact rational entries obtained from the matrices displayed immediately before Equation (3). The result classifies equilibria of this smooth autonomous ODE only. It does not assert a one-to-one relation between equilibria and scrolls, nor does it re-prove the source's horseshoe or chaotic-attractor claims.

## Proof
Let
\[
D=\begin{pmatrix}
4195/1000&-4295/1000&1295/1000\\
31/10&-32/10&-61/10\\
-7605/1000&7605/1000&-1905/1000
\end{pmatrix}.
\]
At an equilibrium, \(D(x_1,x_2,x_3)^T=(0,0,-(33/10)\sin((47/10)x_2))^T\). Exact elimination gives
\[
D^-1e_3=\left(-\frac{3065}{547},-\frac{98680}{18051},\frac{365}{18051}\right)^T,
\]
and hence, after setting \(t=(47/10)x_2\),
\[
t+\frac{231898}{2735}\sin t=0.
\]
The remaining coordinates are fixed by
\[
x_1=\frac{20229}{19736}x_2,
\qquad
x_3=-\frac{73}{19736}x_2.
\]
Thus the scalar equation gives the complete equilibrium set.

Set \(B=231898/2735\). The classical rational bounds \(333/106<\pi<22/7\) imply
\[
26\pi<B<27\pi.
\]
For a positive root, \(t=-B\sin t>0\), so \(\sin t<0\). Therefore every positive root lies in one of the negative-sine lobes \(((2k-1)\pi,2k\pi)\). Because \(t\le B<27\pi\), only \(k=1,\ldots,13\) are possible. On each such lobe,
\[
f''(t)=-B\sin t>0,
\]
so \(f\) is strictly convex. Its endpoint values are positive, while at the midpoint \(m_k=(2k-1/2)\pi\),
\[
f(m_k)=m_k-B<26\pi-B<0.
\]
Strict convexity therefore gives exactly two roots in each lobe, one on each side of the midpoint. Odd symmetry supplies their negatives, and \(t=0\) is the remaining root. Hence the exact count is \(2\cdot26+1=53\).

For stability, write
\[
q=\frac{1551}{100}\cos t.
\]
At the equilibrium corresponding to \(t\), direct determinant expansion gives
\[
p_q(\lambda)=\lambda^3+\frac{91}{100}\lambda^2+
\left(\frac{61}{10}q+\frac{27117}{500}\right)\lambda+
\frac{54153}{10000}-\frac{7401}{250}q.
\]
For every nonzero root, \(\sin t=-t/B\). Since every such root has \(0<|t|<26\pi\), the bound \(\pi<22/7\) gives
\[
|\cos t|=\sqrt{1-(t/B)^2}>\frac14.
\]
Thus \(|q|>1551/400\). On a left-half root, \(\cos t<0\), hence \(q<-1551/400\); on a right-half root, \(\cos t>0\), hence \(q>1551/400\).

The cubic Routh array has first column with signs determined by
\[
1,\qquad \frac{91}{100},\qquad
\frac{878875q+1098441}{22750},\qquad
\frac{54153}{10000}-\frac{7401}{250}q.
\]
The third entry changes sign only at \(q=-1098441/878875\), while the last changes sign only at \(q=18051/98680\). Since
\[
\frac{1551}{400}>\frac{1098441}{878875},
\qquad
\frac{1551}{400}>\frac{18051}{98680},
\]
a left-half root yields the sign pattern \((+,+,-,+)\), hence two right-half-plane eigenvalues; a right-half root yields \((+,+,+,-)\), hence one. No first-column entry vanishes, so these equilibria are hyperbolic. At the origin, \(q=1551/100\), giving the same one-unstable-direction pattern as the right-half roots. Reflection does not change \(q\), so the final unstable-index counts are 26 and 27.

## Verification
The bundled script `verify_equilibria.py` replays all rational matrix identities, the scalar reduction, the exact Routh thresholds, the rational inequalities used in the root count, and a high-precision numerical sanity check locating two roots in each of the 13 positive negative-sine lobes. It prints `VERIFY_OK` on success. The exact proof does not depend on the floating-point root locations.

## Relationship to prior work
Ye and He derive the equilibrium equation graphically, state that there are multiple nonzero equilibria, and list two nonzero examples together with their eigenvalues. Their article does not give the total number of equilibria at \(\varepsilon_2=3.3\), \(\sigma_2=4.7\), nor a complete unstable-index classification. The exact count above therefore strengthens the source's equilibrium analysis at the same parameter point.

Tang, Zhong, Chen, and Man earlier showed how a different sine-modified Chua system can be designed so that its equilibrium count is prescribed explicitly. That construction uses a different vector field and a piecewise continuation of the sine nonlinearity; its formula for the Chua-family equilibria does not imply the 53-point census or the Routh-index split for the Ye–He flow.

## Limitations
The classification is parameter-specific: changing the sine amplitude or frequency changes the scalar root equation and can change both the equilibrium count and the index pattern. The result does not establish how many of the 53 equilibria are dynamically visited by a particular attractor, does not equate equilibrium count with scroll count, and does not independently validate the source's computer-assisted horseshoe calculation.

## References
1. Y. Ye and J. He, “Constructing a New Multi-Scroll Chaotic System and Its Circuit Design,” *Mathematics* 12 (2024), 1931. DOI: 10.3390/math12131931. Published 2024-06-21.
2. W. K. S. Tang, G. Q. Zhong, G. Chen, and K. F. Man, “Generation of N-scroll attractors via sine function,” *IEEE Transactions on Circuits and Systems I* 48 (2001), 1369–1372.
