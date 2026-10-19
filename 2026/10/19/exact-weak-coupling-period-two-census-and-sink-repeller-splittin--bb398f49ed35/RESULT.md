# Exact weak-coupling period-two census and sink–repeller splitting in a memristive Lozi map

## Finding

Consider the Wang–Gu–Rong–Xu–Zhang three-dimensional memristive Lozi map restricted to its physically used corner parameter \(a=1\):
\[
F_{b,k}(x,y,z)=\bigl(1-|x|+y,\; bx+ky\sin z,\; z+y\bigr).
\]
For every \(b>0\) and \(0<k<1/3\), the complete number of primitive period-two **orbits modulo** simultaneous phase translation \(z\mapsto z+2\pi m\), \(m\in\mathbb Z\), is
\[
N_2(b,k)=\begin{cases}
0,&|b-1|>k,\\
1,&|b-1|=k,\\
2,&|b-1|<k.
\end{cases}
\]
This counts all real period-two orbits, not just those in a selected numerical basin; every counted orbit has infinitely many distinct copies on the full real phase space under \(2\pi\) translation. The two phase solutions merge into one at each boundary \(b=1\pm k\).

Every orbit admits an explicit one-variable characterization. For each solution \(z\in\mathbb R/(2\pi\mathbb Z)\) of
\[
\sin z=(b-1)/k,
\]
there is exactly one \(t>0\) solving
\[
t\bigl(1+k\sin(z+t)\bigr)=b.
\]
Its two states, in their canonical time ordering, are
\[
p=(-t,t,z),\qquad q=(1,-t,z+t),\qquad F_{b,k}(p)=q,\quad F_{b,k}(q)=p.
\]
On the central line \(b=1\), the phase \(z=\pi\) cycle is a hyperbolic **attractor**, whereas the phase \(z=0\) cycle is a hyperbolic **repeller**, for every sufficiently small \(k>0\). Thus an open set of positive parameters has coexistence of a stable and a fully repelling primitive two-cycle in a map with no fixed point.

## Assumptions and scope

The domain is all of \(\mathbb R^3\). The map parameter \(a\) from the originating paper is set to \(1\); the other parameters satisfy \(b>0\) and \(0<k<1/3\). The count identifies orbits under cyclic re-ordering of their two states and under the exact symmetry \((x,y,z)\mapsto(x,y,z+2\pi m)\). Without this quotient, every orbit has countably infinitely many vertical translates. No claim is made about periods greater than two, attractors elsewhere, the high-gain regime, or global basin sizes. The hyperbolicity assertion along \(b=1\) is for sufficiently small positive coupling, not for the entire \(0<k<1/3\) range.

## Proof

**1. All periodic pairs have opposite signed inputs.** Suppose \(F_{b,k}^2(x_0,y_0,z_0)=(x_0,y_0,z_0)\). The third coordinate yields \(y_0+y_1=0\). If \(y_0=0\), both \(y\)-coordinates vanish, and the second equation (using \(b>0\)) makes both \(x\)-coordinates zero; the first equation then requires \(0=1\), a contradiction. Reorder the two states so that \(y_0=t>0\) and \(y_1=-t\). The second recurrence at the first state gives \(b x_0=-t(1+k\sin z_0)<0\), while the second recurrence at the second state gives \(b x_1=t(1+k\sin(z_0+t))>0\). Hence \(x_0<0<x_1\); this step uses \(0<k<1\).

**2. Exact reduction.** In the sign sectors just determined, the first-coordinate recurrences are \(x_1=1+x_0+t\) and \(x_0=1-x_1-t\). Solving gives \(x_0=-t\) and \(x_1=1\). Substituting into the second-coordinate recurrences gives precisely
\[
\sin z_0=(b-1)/k,\qquad t(1+k\sin(z_0+t))=b.
\]
Conversely, any phase–amplitude pair solving these two equations produces exactly the two states displayed above, and direct substitution proves both recurrences. In particular, all these cycles are primitive because the system has no fixed point: a fixed point would have \(y=0\), then \(x=0\) from \(b>0\), contrary to the first equation.

**3. Exhaustive phase count and amplitude uniqueness.** Necessarily \(|b-1|\le k\), proving nonexistence outside that closed wedge. Inside the wedge, the sine equation has exactly two solutions modulo \(2\pi\) for strict inequality and one at equality. For a fixed allowed phase, set \(g(t)=t(1+k\sin(z+t))\). Any positive solution \(g(t)=b\) obeys
\[
\frac{b}{1+k}\le t\le\frac{b}{1-k}.
\]
On the full interval from \(0\) to \(b/(1-k)\),
\[
g'(t)=1+k\sin(z+t)+kt\cos(z+t)
\ge 1-k-\frac{kb}{1-k}.
\]
Since \(|b-1|\le k\), we have \(b\le1+k\). Therefore
\[
(1-k)g'(t)\ge(1-k)^2-k(1+k)=1-3k>0.
\]
Furthermore \(g(0)=0<b\) and \(g(b/(1-k))\ge b\). Thus exactly one positive amplitude exists for each phase; values beyond \(b/(1-k)\) cannot solve the equation. The phase count is the complete orbit count.

**4. The two weak-coupling stability types.** On \(b=1\), the two phases are exactly \(z=0\) and \(z=\pi\). Write \(\eta=\cos z\in\{+1,-1\}\). The corresponding amplitude solves \(t(1+\eta k\sin t)=1\); by the implicit function theorem at \((t,k)=(1,0)\),
\[
t=1-\eta k\sin1+O(k^2).
\]
All orbit points stay in differentiable sign sectors. With the Jacobian ordered as \((x,y,z)\), the one-step matrices at \(p\) and \(q\) are
\[
J_p=\begin{pmatrix}1&1&0\\1&0&\eta kt\\0&1&1\end{pmatrix},\qquad
J_q=\begin{pmatrix}-1&1&0\\1&\eta k\sin t&-\eta kt\cos t\\0&1&1\end{pmatrix}.
\]
The return matrix is \(M=J_qJ_p\). Its characteristic polynomial has the explicit first-order expansion
\[
\begin{split}
\det(\lambda I-M)={}&(\lambda-1)(\lambda^2-\lambda+1)\\
&+\eta k\bigl[(\cos1-1)\lambda^2+(\sin1)\lambda-(\cos1+\sin1+1)\bigr]+O(k^2).
\end{split}
\]
The three unperturbed multipliers \(1\) and \((1\pm i\sqrt3)/2\) are simple, so their analytic continuations obey
\[
\lambda_{\mathrm{real}}=1+2\eta k+O(k^2),\qquad
|\lambda_{\mathrm{pair}}|=1+\frac{\eta}{2}(\sin1+\cos1-1)k+O(k^2).
\]
Here the second expression denotes the common modulus of the nonreal pair. Because \(\sin1+\cos1>1\), the branch \(\eta=-1\) has all three multipliers strictly inside the unit disk for sufficiently small \(k>0\); the \(\eta=+1\) branch has all three strictly outside. The first is a hyperbolic sink and the second a hyperbolic repeller for the period-two return. Hyperbolic continuation preserves this coexistence on an open neighborhood of each sufficiently small central-line parameter pair.

## Verification

The standalone `verify.py` contains exact symbolic checks of the two Jacobians, the return characteristic expansion, the real-multiplier derivative, and the complex-pair radial derivative. Its finite sample checks independently reconstruct 2-cycles for couplings up to \(3/10\), including both wedge edges, and confirm their recurrences. Running `python verify.py` with SymPy and NumPy returned `PASS: 640 finite symbolic/numerical checks`.

The infinitely many parameter statements, completeness of the orbit count, and small-coupling hyperbolicity are established analytically above, not inferred from those finite tests.

## Relationship to prior work

Wang, Gu, Rong, Xu and Zhang introduced this three-dimensional map in their 2022 article (their equation (4)); section 2.3 establishes the absence of fixed points when \(b\ne0\). Their sections 3–4 numerically display period-two and higher-period regions and hidden multistability, primarily at coupling gains between approximately \(1.4\) and \(1.9\). They do not give the exact low-gain parameter wedge, exhaustive period-two orbit count, or the analytic sink–repeller splitting derived here. The general theory of the two-dimensional Lozi map and its known bisecting bifurcations does not imply the phase equation or return-multiplier splitting in this three-dimensional memristive extension. The present result concerns a different, weak-coupling parameter regime and makes no claim to classify the source's high-gain hyperchaos.

## Limitations

The uniform count relies on the tractable sufficient condition \(k<1/3\); outside it the scalar amplitude equation need not be monotone and extra orbits are not excluded. The existence of a sink and a repeller is proved for sufficiently small positive coupling on \(b=1\) and nearby positive parameters, without providing a numerically sharp stability endpoint. There may be invariant sets or other attracting orbits not considered. Priority is not exhaustively established against every historical or unindexed publication; the checked literature covers the original map, an accessible Lozi survey, and related but different period-two classifications. Independent mathematical review has not occurred.

## References

1. J. Wang, Y. Gu, K. Rong, Q. Xu, X. Zhang, “Memristor-Based Lozi Map with Hidden Hyperchaos,” *Mathematics* **10** (2022), 3426, DOI: 10.3390/math10193426, first verified public date 2022-09-21. Original full text: https://pdfs.semanticscholar.org/a374/c56a2f55a893c2110b7b90c3a85e288a64fc.pdf.
2. R. Lozi and related studies surveyed in “Survey of Recent Applications of the Chaotic Lozi Map,” *Algorithms* **16** (2023), 491, DOI: 10.3390/a16100491; comparison limited to its discussion of the classical Lozi map, bisecting bifurcations, and memristive variant.
