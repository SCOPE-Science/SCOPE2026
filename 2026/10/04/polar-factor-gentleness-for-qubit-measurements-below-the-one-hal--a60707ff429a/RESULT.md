# Polar-factor gentleness for qubit measurements below the one-half disturbance threshold
## Finding
Let \(M=(M_y)_y\) be a measurement on a qubit and suppose it is \(\alpha\)-gentle on all qubit states for some \(0\le\alpha<1/2\), in the sense that every possible outcome satisfies
\[
D\!\left(\rho,\frac{M_y\rho M_y^*}{\operatorname{Tr}(M_y\rho M_y^*)}\right)\le\alpha,
\qquad D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\]
For each nonzero outcome write \(M_y=U_yA_y\) with \(A_y=|M_y|=(M_y^*M_y)^{1/2}\). Then \((A_y)_y\) is again a valid measurement, has exactly the same outcome probabilities, and is \(\alpha\)-gentle.

More quantitatively, for a nonzero qubit operator \(T\) define
\[
G(T)=\sup_\rho D\!\left(\rho,\frac{T\rho T^*}{\operatorname{Tr}(T\rho T^*)}\right),
\]
where the supremum is taken over states for which the displayed denominator is nonzero. If the singular values of \(T\) are \(a\ge b>0\) and
\[
g=\frac{a-b}{a+b},
\]
then
\[
G(|T|)=g,
\]
and
\[
G(T)\ge g\quad\text{when }g\le\frac1{\sqrt3},
\qquad
G(T)\ge\frac12\quad\text{when }g\ge\frac1{\sqrt3}.
\]
Hence
\[
G(T)<\frac12\quad\Longrightarrow\quad G(|T|)\le G(T).
\]
This proves the positive-polar-factor gentleness conjecture for qubits throughout the strict \(\alpha<1/2\) regime used in the gentle-measurement data-processing theory. Combining it with the positive-operator result of Butucea, Johannes, and Stein also yields, for arbitrary qubit measurement operators in this regime, the same quantum-differential-privacy parameter
\[
\delta=2\log\!\left(\frac{1+\alpha}{1-\alpha}\right).
\]

## Assumptions and scope
The Hilbert space is \(\mathbb C^2\). A zero measurement outcome can be deleted. If a nonzero qubit operator \(T\) is singular, then its normalized postselected output is a fixed pure state and states with nonzero outcome probability can approach an orthogonal input, so \(G(T)=1\). Thus every outcome of an \(\alpha\)-gentle measurement with \(\alpha<1/2\) is automatically invertible, and its polar factor is unitary.

The statement concerns worst-case trace-distance disturbance of the normalized post-measurement state, not average disturbance and not a distance between channels. It proves the conjectured comparison in the operational regime \(\alpha<1/2\); it does not claim the comparison for arbitrary disturbance above that threshold or in dimensions larger than two.

## Proof
Fix an invertible qubit operator \(T=UA\), with \(A=|T|\), and diagonalize \(A\) so that its eigenvalues are \(a\ge b>0\). Scaling \(T\) does not change normalized postselection. Put
\[
g=\frac{a-b}{a+b},\qquad
c=\frac{a^2-b^2}{a^2+b^2}=\frac{2g}{1+g^2},\qquad
d=\frac{2ab}{a^2+b^2}=\frac{1-g^2}{1+g^2}.
\]
For a Bloch vector \(r=(x,y,z)\), the normalized positive filtering map induced by \(A\) is
\[
h_A(r)=\left(\frac{dx}{1+cz},\frac{dy}{1+cz},\frac{c+z}{1+cz}\right).
\]
For fixed \(z\), the squared Euclidean displacement \(\|h_A(r)-r\|_2^2\) is affine with nonnegative coefficient in \(x^2+y^2\). Therefore its maximum over the Bloch ball at that \(z\) occurs on the sphere. On a pure state whose squared amplitude on the \(a\)-eigenvector is \(p\), one has
\[
D^2=1-\frac{(pa+(1-p)b)^2}{pa^2+(1-p)b^2}
=\frac{p(1-p)(a-b)^2}{pa^2+(1-p)b^2}.
\]
Differentiation gives the unique interior maximizer \(p=b/(a+b)\), at which \(D=g\). Hence \(G(A)=g\).

It remains to lower-bound the disturbance of \(T=UA\). On pure states the left unitary \(U\) acts as a rotation \(R\in SO(3)\) of the output Bloch vector, and
\[
D^2=\frac{1-r\cdot Rh_A(r)}2.
\]
First suppose \(g\le1/\sqrt3\). Let \(s=\sqrt{1-g^2}\) and consider the circle
\[
r_\phi=(s\cos\phi,s\sin\phi,-g).
\]
The positive filter sends it exactly to
\[
h_A(r_\phi)=(s\cos\phi,s\sin\phi,g).
\]
Averaging the Bloch inner product over \(\phi\) gives
\[
\frac1{2\pi}\int_0^{2\pi} r_\phi\cdot Rh_A(r_\phi)\,d\phi
=x(R_{11}+R_{22})-yR_{33},
\]
where \(x=(1-g^2)/2\) and \(y=g^2\). Here \(y\le x\). Write a rotation as angle \(\theta\) about a unit axis with third coordinate \(n_3\). With \(q=\cos\theta\),
\[
R_{33}=q+(1-q)n_3^2,
\]
and therefore
\[
x(R_{11}+R_{22})-yR_{33}
=x+(x-y)q-(x+y)(1-q)n_3^2
\le 2x-y=1-2g^2.
\]
At least one point on the circle thus satisfies \(r_\phi\cdot Rh_A(r_\phi)\le1-2g^2\), which implies \(D\ge g\). Hence \(G(T)\ge g\).

Now suppose \(g\ge1/\sqrt3\). On the equator \(r_\phi=(\cos\phi,\sin\phi,0)\),
\[
h_A(r_\phi)=(d\cos\phi,d\sin\phi,c).
\]
Averaging gives
\[
\frac1{2\pi}\int_0^{2\pi}r_\phi\cdot Rh_A(r_\phi)\,d\phi
=\frac d2(R_{11}+R_{22})\le d.
\]
Thus some equatorial input has
\[
D^2\ge\frac{1-d}{2}=\frac{g^2}{1+g^2}\ge\frac14,
\]
so \(G(T)\ge1/2\).

If \(G(T)<1/2\), the second case is impossible. Therefore \(g<1/\sqrt3\), the first case applies, and
\[
G(|T|)=g\le G(T).
\]
For an \(\alpha\)-gentle qubit measurement with \(\alpha<1/2\), each outcome operator satisfies \(G(M_y)\le\alpha\), so \(G(|M_y|)\le\alpha\). Finally,
\[
\sum_y |M_y|^2=\sum_y M_y^*M_y=I,
\]
so the positive polar factors form a valid measurement and have the same outcome law.

## Verification
The proof above is analytic. The accompanying `artifacts/verify.py` checks the Bloch-map formulas at the maximizing latitude, the two circle-average inequalities for random rotations, and the threshold algebra for representative values of \(g\). It prints `VERIFY_OK` when all checks pass. These finite checks corroborate the algebra but are not used as an infinite proof.

## Relationship to prior work
Butucea, Johannes, and Stein explicitly observed that replacing measurement operators by their positive factors preserves outcome probabilities, conjectured that the positive factors have at least the same gentleness, and stated that the qubit case was strongly supported by numerical simulations. Their positive-operator Lemma 2 gives the sharper differential-privacy parameter \(2\log((1+\alpha)/(1-\alpha))\). The theorem above proves their conjectured comparison for qubits whenever the original worst-case disturbance is below \(1/2\), exactly covering the strict \(\alpha<1/2\) regime used by their strong data-processing result, and thereby removes the positivity restriction from that qubit differential-privacy conclusion.

Classical antieigenvalue and operator-angle theory gives the positive-matrix extremum corresponding to \(G(A)=(a-b)/(a+b)\). The new step needed here is the uniform comparison against an arbitrary left polar unitary in the qubit postselection geometry. Searches for the claim under gentle-measurement, polar-factor, operator-angle, and antieigenvalue terminology did not locate a published implication that resolves the cited qubit conjecture.

## Limitations
The comparison \(G(|T|)\le G(T)\) is proved only under the hypothesis \(G(T)<1/2\). The argument supplies the weaker universal lower bound \(G(T)\ge1/2\) once \((a-b)/(a+b)\ge1/\sqrt3\), but does not determine the exact minimum disturbance over left-unitary polar factors in that large-anisotropy regime. No claim is made for dimensions larger than two. The literature search cannot rule out an equivalent statement hidden in older operator-angle terminology.

## References
1. C. Butucea, J. Johannes, H. Stein, “Sample-optimal learning of quantum states using gentle measurements,” arXiv:2505.24587, first public 2025-05-30; Electronic Journal of Statistics 20 (2026), 3423–3459, DOI 10.1214/26-EJS2562.
2. K. Gustafson, “The angle of an operator and positive operator products,” Bulletin of the American Mathematical Society 74 (1968), 488–492, DOI 10.1090/S0002-9904-1968-11974-3.
3. S. M. Hossein, K. C. Das, L. Debnath, K. Paul, “Bounds for total antieigenvalue of a normal operator,” International Journal of Mathematics and Mathematical Sciences (2004), DOI 10.1155/S0161171204401409.
