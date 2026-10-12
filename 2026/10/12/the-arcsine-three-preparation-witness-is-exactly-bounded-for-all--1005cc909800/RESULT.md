# The arcsine three-preparation witness is exactly bounded for all qubit POVMs
## Finding
Consider three qubit preparations \(\rho_1,\rho_2,\rho_3\), two binary measurements, and correlations \(E_{xy}=P(+1\mid x,y)-P(-1\mid x,y)\). For arbitrary density operators and arbitrary binary POVMs,
\[
J_3=\left|\arcsin(E_{11})+\arcsin(E_{12})+\arcsin(E_{21})-\arcsin(E_{22})-\arcsin(E_{31})\right|\le \frac{3\pi}{2}.
\]
The constant is attained by qubits. This proves the nonlinear qubit witness proposed, on the basis of strong numerical evidence, in Gallego, Brunner, Hadley and Acín.

## Assumptions and scope
For measurement \(y\), write the binary observable as
\[
O_y=M^y_{+}-M^y_{-}=a_y I+b_y\cdot\sigma,
\]
where \(O_y\) is Hermitian with spectrum in \([-1,1]\). Put \(t_y=\lVert b_y\rVert\). The contraction condition is exactly \(\lvert a_y\rvert+t_y\le 1\). A state has Bloch form \(\rho=(I+r\cdot\sigma)/2\), with \(\lVert r\rVert\le 1\), and therefore \(E=a_y+b_y\cdot r\).

Only the two vectors \(b_1,b_2\) enter the correlations of preparations \(1,2\). Their span has dimension at most two, so any Bloch vector \(r\) can be replaced by a unit Bloch vector with the same projection onto that span. This preserves both correlations. Preparation \(3\) can likewise be replaced by a pure state without changing \(E_{31}\). Hence it is enough to prove the inequality on the Bloch sphere, even though the claim allows mixed states and nonprojective binary POVMs.

## Proof
Fix one binary qubit observable \(O=aI+t n\cdot\sigma\), where \(t\ge0\), \(\lVert n\rVert=1\), and \(\lvert a\rvert+t\le1\), and define
\[
f(r)=\arcsin\!\left(a+t\,n\cdot r\right),\qquad r\in S^2.
\]
Let \(\theta\) be the polar angle from \(n\). Along a meridian,
\[
\left|\frac{df}{d\theta}\right|=
\frac{t\sqrt{1-\cos^2\theta}}{\sqrt{1-(a+t\cos\theta)^2}}\le1,
\]
because the squared inequality is equivalent to
\[
t^2\le 1-a^2-2at\cos\theta,
\]
and its smallest right-hand side is \(1-a^2-2\lvert a\rvert t\ge t^2\), which is exactly \((\lvert a\rvert+t)^2\le1\). By rotational symmetry this is the spherical gradient norm, so \(f\) is one-Lipschitz for geodesic distance \(d\).

We next prove the key three-point inequality
\[
f(r)+f(s)-\min_{u\in S^2}f(u)+d(r,s)\le\frac{3\pi}{2}.
\]
Write the polar angles of \(r,s\) as \(\theta_1,\theta_2\), and set \(h(\theta)=\arcsin(a+t\cos\theta)\). The largest possible distance for fixed polar angles is
\[
d(r,s)\le \min\{\theta_1+\theta_2,\;2\pi-\theta_1-\theta_2\}.
\]
Since \(-1\le h'(\theta)\le0\), if \(\theta_1+\theta_2\le\pi\), increasing either angle toward the boundary \(\theta_1+\theta_2=\pi\) cannot decrease \(h(\theta_1)+h(\theta_2)+\theta_1+\theta_2\). If \(\theta_1+\theta_2\ge\pi\), decreasing either angle toward the same boundary cannot decrease \(h(\theta_1)+h(\theta_2)+2\pi-\theta_1-\theta_2\). Thus the maximum occurs with \(\theta_2=\pi-\theta_1\).

Writing \(c=\cos\theta_1\) and using symmetry to take \(c\ge0\), it remains to show
\[
\arcsin(a+tc)+\arcsin(a-tc)\le \frac{\pi}{2}+\arcsin(a-t).
\]
For \(a\ge0\), the left side is increasing in \(c\), so its maximum is at \(c=1\), where the claim reduces to \(\arcsin(a+t)\le\pi/2\). For \(a\le0\), the left side is decreasing in \(c\), so its maximum is \(2\arcsin(a)\le0\), while the right side is nonnegative. This proves the three-point inequality.

Now let \(f\) correspond to measurement \(1\) and \(g\) to measurement \(2\), and choose pure Bloch representatives \(r_1,r_2,r_3\) as above. Without the outer absolute value, the witness expression is
\[
Q=f(r_1)+g(r_1)+f(r_2)-g(r_2)-f(r_3).
\]
The one-Lipschitz property gives \(g(r_1)-g(r_2)\le d(r_1,r_2)\), and \(-f(r_3)\le-\min f\). Therefore the three-point inequality yields \(Q\le3\pi/2\). Replacing both observables by their negatives replaces \(Q\) by \(-Q\) and preserves all assumptions, hence \(-Q\le3\pi/2\) as well. Thus \(J_3=\lvert Q\rvert\le3\pi/2\).

Sharpness is explicit. Take pure Bloch vectors \(r_1=(1,0,0)\), \(r_2=(0,1,0)\), measurement axes \(s_1=(r_1+r_2)/\sqrt2\), \(s_2=(r_1-r_2)/\sqrt2\), and \(r_3=-s_1\). Then
\[
(E_{11},E_{12},E_{21},E_{22},E_{31})=(2^{-1/2},2^{-1/2},2^{-1/2},-2^{-1/2},-1),
\]
so the five arcsine terms sum to \(3\pi/2\).

## Verification
The proof is analytic and covers arbitrary binary qubit POVMs, including biased observables and mixed preparations. The accompanying `verify_j3.py` independently checks the contraction-to-Lipschitz algebra on a deterministic parameter grid, checks the scalar boundary inequality, and verifies the exact saturating correlation pattern numerically to floating-point precision. These computations are sanity checks; finite sampling is not used as proof of the universal inequality.

## Relationship to prior work
Gallego, Brunner, Hadley and Acín introduced \(J_3\) and stated that they had strong numerical evidence for the qubit bound \(3\pi/2\), while noting that the bound is attained. Their paper did not supply an analytic proof. Brunner, Navascués and Vértesi subsequently described the earlier prepare-and-measure approach as one whose quantum-witness validity generally had to be tested numerically and developed a different state-discrimination family. Bowles, Quintino and Brunner later developed determinant-based nonlinear witnesses under an independence assumption; their witness and assumptions differ from the arcsine inequality here.

Targeted searches using the exact five-term arcsine expression, the label \(J_3\), the constant \(3\pi/2\), and angular/Bloch reformulations did not locate a published implication-equivalent analytic proof. The closest inspected papers use different witness families and do not imply this inequality.

## Limitations
No claim is made about a complete characterization of the full qubit correlation set, about higher-dimensional analogues, or about robustness margins under finite statistics. The originality conclusion is limited by ordinary literature-indexing coverage: a poorly indexed later proof could exist. The numerical checker is not a certificate for the universal quantifier; universality comes from the analytic argument above.

## References
1. R. Gallego, N. Brunner, C. Hadley, A. Acín, “Device-independent tests of classical and quantum dimensions,” arXiv:1010.5064v1 (25 October 2010), later Phys. Rev. Lett. 105, 230501 (2010), DOI: 10.1103/PhysRevLett.105.230501.
2. N. Brunner, M. Navascués, T. Vértesi, “Dimension witnesses and quantum state discrimination,” arXiv:1209.5643 (2012), later Phys. Rev. Lett. 110, 150501 (2013), DOI: 10.1103/PhysRevLett.110.150501.
3. J. Bowles, M. T. Quintino, N. Brunner, “Certifying the dimension of classical and quantum systems in a prepare-and-measure scenario with independent devices,” arXiv:1311.1525 (2013), later Phys. Rev. Lett. 112, 140407 (2014), DOI: 10.1103/PhysRevLett.112.140407.
4. Mathematics Subject Classification 2020, class 81P15: “Quantum measurement theory, state operations, state preparations,” American Mathematical Society / MathSciNet MSC2020 database.
