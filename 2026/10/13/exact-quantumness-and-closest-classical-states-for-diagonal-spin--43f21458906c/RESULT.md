# Exact quantumness and closest classical states for diagonal spin-1 mixtures
## Finding
Consider the spin-1 state
\[\rho_{a,b,c}=a|1,1\rangle\langle1,1|+b|1,0\rangle\langle1,0|+c|1,-1\rangle\langle1,-1|,\qquad a,b,c\ge0,\quad a+b+c=1.\]
Write \(x=a-c\). Let \(\mathcal C\) be the convex hull of spin coherent states and define
\[Q(\rho)=\min_{\sigma\in\mathcal C}\|\rho-\sigma\|_2.\]
Then \(\rho_{a,b,c}\) is classical if and only if
\[x^2+2b\le1.\]
For every nonclassical state, so \(x^2+2b>1\), the cubic
\[3y^3+(6b-1)y-2x=0\]
has a unique real root \(y\in(-1,1)\). The unique closest classical state is
\[\sigma_y=\operatorname{diag}\!\left(\frac{(1+y)^2}4,\frac{1-y^2}2,\frac{(1-y)^2}4\right),\]
and
\[Q(\rho_{a,b,c})^2=\frac{(x-y)^2}2+\frac32\left(b-\frac{1-y^2}2\right)^2
=\frac32(1+3y^2)\left(b-\frac{1-y^2}2\right)^2.\]
If \(\theta=\arccos y\) and \(\phi_k=2\pi k/3\), then
\[\sigma_y=\frac13\sum_{k=0}^2|\theta,\phi_k\rangle\langle\theta,\phi_k|.\]
Because \(y\in(-1,1)\), all three diagonal entries of \(\sigma_y\) are positive, so \(\operatorname{rank}\sigma_y=3\). Hence every decomposition into pure states, and therefore every coherent-state decomposition, uses at least three terms; the displayed decomposition proves that the minimum coherent-state length is exactly three.

## Assumptions and scope
The basis \(|1,1\rangle,|1,0\rangle,|1,-1\rangle\) is any spin-projection basis. Rotation invariance therefore extends the statement to states diagonal in the eigenbasis of \(J_n\) for any spatial direction \(n\). The distance is the Hilbert--Schmidt norm used in the cited spin-quantumness literature. The theorem concerns the convex hull of spin coherent states, equivalently the symmetric separable two-qubit states; it is not a formula for distance to the larger set of all two-qubit separable states.

## Proof
Embed the spin-1 basis into the symmetric two-qubit subspace by
\[|1,1\rangle=|00\rangle,\qquad |1,0\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},\qquad |1,-1\rangle=|11\rangle.\]
The partial transpose of \(\rho_{a,b,c}\) is
\[\rho_{a,b,c}^\Gamma=
\begin{pmatrix}
a&0&0&b/2\\
0&b/2&0&0\\
0&0&b/2&0\\
b/2&0&0&c
\end{pmatrix}.\]
For symmetric two-qubit states, classicality of the spin-1 state is equivalent to separability, and for two qubits separability is equivalent to positivity of the partial transpose. Thus classicality is equivalent to \(b^2\le4ac\). Since \(4ac=(1-b)^2-x^2\), this is exactly \(x^2+2b\le1\).

Now suppose \(x^2+2b>1\). The state is invariant under rotations about the chosen spin axis. Average any classical competitor over those rotations. This averaging preserves classicality and is the Hilbert--Schmidt orthogonal projection onto the diagonal subspace. Because the target is already diagonal, Pythagoras gives a distance no larger than before averaging. Hence the unique metric projection onto the closed convex set \(\mathcal C\) is diagonal.

Write a diagonal competitor using coordinates \((y,b')\), where \(y=a'-c'\). The classicality condition just proved gives
\[-1\le y\le1,\qquad 0\le b'\le h(y):=\frac{1-y^2}2.\]
The Hilbert--Schmidt squared distance becomes
\[\frac12(x-y)^2+\frac32(b-b')^2.\]
A nearest point can be taken on the upper boundary \(b'=h(y)\): if \(b>h(y)\), increasing \(b'\) to \(h(y)\) strictly decreases the distance; if \(b\le h(y)\), then \(|y|\le\sqrt{1-2b}<|x|\), and moving \(y\) to the nearest endpoint of that interval reaches \(h(y)=b\) without increasing the horizontal distance. Consequently it suffices to minimize
\[F(y)=\frac12(x-y)^2+\frac32\left(b-\frac{1-y^2}2\right)^2,\qquad -1\le y\le1.\]
Its derivative is
\[F'(y)=\frac12\left(3y^3+(6b-1)y-2x\right).\]
Physicality gives \(|x|\le1-b\), and nonclassicality implies \(b>0\). Therefore the cubic \(g(y)=3y^3+(6b-1)y-2x\) obeys \(g(-1)<0<g(1)\). If \(b\ge1/6\), then \(g'(y)=9y^2+6b-1\ge0\), so the root is unique. If \(0<b<1/6\), nonclassicality gives \(x^2>1-2b\), while the discriminant of the depressed cubic is
\[\Delta=\frac{x^2}9-\frac{(1-6b)^3}{729}>0,\]
because \(81(1-2b)>(1-6b)^3\). Hence there is again exactly one real root. It lies in \((-1,1)\), and the sign change of \(F'\) makes it the global minimizer.

At the stationary point,
\[x-y=3y\left(b-\frac{1-y^2}2\right),\]
which gives the second displayed expression for \(Q^2\). The boundary state at this \(y\) is exactly the azimuthal three-point twirl of a coherent state: the third roots of unity cancel all off-diagonal phase factors of orders one and two. This proves both the closest-state formula and the three-term coherent decomposition.

## Verification
The standalone script `verify.py` checks the algebraic reduction \(b^2\le4ac\iff x^2+2b\le1\), reconstructs the cubic stationarity equation, verifies positivity of the cubic discriminant in representative nonclassical rational cases, checks the three-root-of-unity coherent decomposition numerically to machine precision, and compares the analytic minimizer against a dense direct scan of the whole diagonal classical region. It prints `VERIFY_OK`. These finite computations are supplementary checks; the theorem is proved by the analytic convex-projection argument above.

## Relationship to prior work
Giraud, Braun, and Braun introduced this Hilbert--Schmidt quantumness measure for finite-dimensional coherent-state classicality and solved the spin-1 Queen-of-Quantum problem. Their later parametrization paper describes the geometry of the complete spin-1 classical set. Bohnet-Waldraff, Braun, and Giraud then obtained an exact formula and closest classical states for all pure spin-1 states, but treated a general mixed state by random coherent-state sampling followed by quadratic programming. They explicitly state that a proof of their mixed-state upper bound is missing.

That 2015 paper also proves its mixed-state upper bound for states on a segment joining a pure state to that pure state's closest classical state. Within the present diagonal family, the nonclassical ray \(x=0\), \(b>1/2\), is such a previously covered segment, generated by the spin-1 Queen \(|1,0\rangle\). The new content is the exact two-parameter diagonal projection, especially the off-axis region \(x\ne0\), together with uniqueness and the minimum three-coherent-state representation of its closest classical state.

General Hilbert--Schmidt closest-separable-state results for two qubits minimize over all separable two-qubit states. That is a different and larger comparison set: the 2015 source itself notes that a closest separable state to a symmetric state need not be symmetric. Those results therefore do not imply the symmetric-classical projection derived here.

## Limitations
The theorem does not solve the arbitrary mixed spin-1 quantumness problem or the 2015 global mixed-state upper-bound conjecture. It is restricted to states diagonal in some spin-projection basis. The Hilbert--Schmidt distance is the historical quantumness definition used by the cited works; no claim is made that it is contractive under general quantum channels. A differently phrased later derivation of this exact diagonal projection could have escaped the searches described in the review material.

## References
1. O. Giraud, P. A. Braun, and D. Braun, “Quantifying Quantumness and the Quest for Queens of Quantum,” arXiv:1002.2158; DOI:10.1088/1367-2630/12/6/063005.
2. O. Giraud, P. Braun, and D. Braun, “Parametrization of spin-1 classical states,” arXiv:1110.0325; DOI:10.1103/PhysRevA.85.032101.
3. F. Bohnet-Waldraff, D. Braun, and O. Giraud, “Quantumness of spin-1 states,” arXiv:1510.07848; DOI:10.1103/PhysRevA.93.012104.
4. F. Verstraete, J. Dehaene, and B. De Moor, “On the geometry of entangled states,” arXiv:quant-ph/0107155; DOI:10.1080/09500340110115488.
5. P. Pandya and M. Wieśniak, “Minimum Hilbert-Schmidt distance and the Closest Separable state to arbitrary \(2\times2\) and \(2\times3\) states,” arXiv:2308.06245.
