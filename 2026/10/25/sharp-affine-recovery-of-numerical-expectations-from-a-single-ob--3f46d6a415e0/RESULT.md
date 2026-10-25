# Sharp affine recovery of numerical expectations from a single observable

## Finding
Let \(H\) be a nonzero complex Hilbert space. For a bounded self-adjoint observable \(A\) and any bounded operator \(T\), write \(m_B(x)=\langle Bx,x\rangle\) for every unit vector \(x\). Define the *worst-case scalar-response prediction error*
\[
E_A(T):=\inf_{f:W(A)\to\mathbb C}\sup_{\|x\|=1}|m_T(x)-f(m_A(x))|,
\]
where \(W(A)=\{m_A(x):\|x\|=1\}\subset\mathbb R\) and no regularity whatsoever is required of \(f\). Define the operator-norm distance to affine functions of this observable by
\[
d_A(T):=\inf_{a,b\in\mathbb C}\|T-aA-bI\|.
\]
Then
\[
\boxed{E_A(T)\le d_A(T)\le 2E_A(T).}
\]
The factor \(2\) cannot be replaced by any smaller universal constant, even on \(\mathbb C^2\). If \(T=T^*\), the stronger *exact* formula is
\[
\boxed{E_A(T)=d_A(T)=\frac12\sup_{\substack{\|x\|=\|y\|=1\\ m_A(x)=m_A(y)}}|m_T(x)-m_T(y)|.}
\]
Thus optimal nonlinear recovery from a single expectation is already affine for a real target. For a complex target, its optimal affine operator approximation costs at most twice the optimal arbitrary scalar-response error, and this loss is sharp.

## Assumptions and scope
The Hilbert space may be finite- or infinite-dimensional; only nonemptiness is needed. The predictor observes one *real* expectation \(m_A(x)\) for a self-adjoint \(A\). The target \(T\) may be nonnormal. All supremums range over *pure unit-vector states*. No assertion concerns joint observations of multiple noncommuting observables, estimation from noisy samples, or trace-class mixed-state statistics. The infimum over predictors includes discontinuous functions. The affine approximation uses arbitrary complex \(a,b\), and \(I\) denotes the identity on \(H\).

## Proof
**1. Self-adjoint reduction and fiber lower bound.** First take \(T=T^*\). For every \(t\in W(A)\), the set \(F_t=\{m_T(x):\|x\|=1,\ m_A(x)=t\}\) is a real interval, because \(\{(m_A(x),m_T(x)):\|x\|=1\}=W(A+iT)\) is convex by the Toeplitz--Hausdorff theorem. Its radius as a subset of \(\mathbb R\) is half its diameter, possibly with unattained endpoints. Arbitrary complex-valued predictors cannot reduce this radius. Choosing the midpoint between its infimum and supremum therefore proves
\[
E_A(T)=\tfrac12 D_0,\quad D_0=\sup\{|m_T(x)-m_T(y)|:m_A(x)=m_A(y),\ \|x\|=\|y\|=1\}.
\]

**2. Uniform affine approximation.** Put \(K=\overline{W(A+iT)}\subset\mathbb R^2\), and \(L=K-K\); these sets are compact and convex in the usual plane, and \(L=-L\). Let \(D=\max\{v:(0,v)\in L\}\), with coordinates \((u,v)\). Since \(W(A+iT)-W(A+iT)\) is convex, \(D=D_0\): only the nontrivial direction needs explanation. For any sequence \((u_n,v_n)\in W(A+iT)-W(A+iT)\) converging to \((0,D)\), choose a fixed point \((u',v')\) of the same convex difference set with \(u'\) of sign opposite to \(u_n\) and nonzero; such positive and negative points exist whenever \(A\) is not scalar. Mixing them with coefficient \(|u_n|/(|u_n|+|u'|)\to0\) produces points in the difference set with *exactly zero* first coordinate and second coordinate tending to \(D\). If \(u_n=0\), no mixing is needed. The case of scalar \(A\) follows immediately from the spectral width of \(T\).

For nonscalar \(A\), the projection of \(L\) onto the horizontal axis contains an open interval about \(0\). The upper profile \(g(u)=\max\{v:(u,v)\in L\}\) is a finite concave function on this interval. It has a finite supporting supergradient at \(0\): there exists a real \(a\) such that \(g(u)\le g(0)+au=D+au\) for all projected \(u\) (the supporting inequality extends to the endpoints by concavity). Hence
\[
(m_T(x)-a m_A(x))-(m_T(y)-a m_A(y))\le D
\]
for every pair of unit vectors. Therefore the numerical range of the self-adjoint operator \(T-aA\) has total width at most \(D\). Centering its spectral interval at \(b\in\mathbb R\) gives \(\|T-aA-bI\|\le D/2=E_A(T)\). The reverse bound follows from using any affine predictor \(f(t)=at+b\) and the elementary inequality \(|m_B(x)|\le\|B\|\). Complex affine coefficients cannot improve this minimum in the self-adjoint case, since taking the real part of an approximation contracts the operator norm. This completes the exact formula.

**3. Complex target.** For arbitrary \(T\), put \(X=(T+T^*)/2\) and \(Y=(T-T^*)/(2i)\), which are self-adjoint. If any predictor has uniform complex error \(e\), its real and imaginary parts predict \(m_X\) and \(m_Y\) with error at most \(e\). Thus \(E_A(X),E_A(Y)\le E_A(T)\). By Step 2, each has a real affine approximation at distance at most its prediction error. Adding their respective affine approximants with coefficient \(i\) gives
\[
d_A(T)\le d_A(X)+d_A(Y)=E_A(X)+E_A(Y)\le 2E_A(T).
\]
The reverse inequality \(E_A(T)\le d_A(T)\) follows by taking \(f(t)=at+b\) for any complex affine pencil, then infimizing.

**4. Sharpness in dimension two.** Take
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad T=\begin{pmatrix}0&2\\0&0\end{pmatrix}.
\]
For a unit vector \(x=(x_1,x_2)\), the observed value is \(t=|x_1|^2-|x_2|^2\), while \(m_T(x)=2\overline{x_1}x_2\). At each fixed \(t\in[-1,1]\), the possible target values form the entire circle of radius \(\sqrt{1-t^2}\). The optimal prediction error is therefore \(E_A(T)=\max_t\sqrt{1-t^2}=1\), achieved by the constant-zero predictor. Meanwhile the upper-right matrix entry of \(T-aA-bI\) is always \(2\), hence \(\|T-aA-bI\|\ge2\); equality is achieved by \(a=b=0\). Therefore \(d_A(T)=2=2E_A(T)\).

## Verification
The proof is analytic and uses the standard convexity of the numerical range of one bounded operator, elementary finite-dimensional convex separation, and spectral width for self-adjoint operators. A standalone checker tests the two-by-two extremal family and its fixed-observation circle on a deterministic grid; the off-diagonal obstruction is exact. These finite tests are **not** used to establish the universal theorem. Reproduction: run `python3 verify.py` with Python's standard library; the checker requires no network access.

## Relationship to prior work
Stephan Weis, *Matrix systems, algebras, and open maps* (arXiv:2502.01761, first posted 2025-02-03; later published in *Advances in Operator Theory*), studies numerical expectation maps and the topology of state restrictions. The accessible complete article was inspected, including its numerical-range-map analysis in Section 4 and matrix-system results. Its openness conclusions do not supply the present uniform prediction error or quantitative comparison with operator-norm affine distance. B. Lins and I. M. Spitkovsky, *Inverse continuity of the numerical range map for Hilbert space operators*, *Operators and Matrices* 14 (2020), 77--90, examine inverse continuity and numerical-range fibers for general Hilbert-space operators, not this sharp affine approximation estimate. The standard Toeplitz--Hausdorff convexity theorem and the supporting-hyperplane theorem are used, not claimed as new. A closely related manuscript concerning exact numerical information, arXiv:2610.29826 (first posted 2026-10-21), is chronologically later than the source-date scope used here and treats qualitative factorization; its complete text was inaccessible in this review and remains an explicit priority caveat.

## Limitations
The exact constant one is restricted to self-adjoint targets; for nonselfadjoint targets the best uniform two factor is optimal, though individual pairs can do better. The statement concerns one self-adjoint observable and pure unit vectors; it is not a theorem about multiple observables, noise, or general Banach spaces. Its proof does not imply the existence of a best arbitrary predictor for nonselfadjoint targets, although the infimum is defined. Earlier or inaccessible sources may contain equivalent approximation principles; the claim is not an assertion of independently certified publication priority. Independent scientific audit has not been carried out.

## References
1. S. Weis, *Matrix systems, algebras, and open maps*, arXiv:2502.01761 (version 1 posted 2025-02-03); *Advances in Operator Theory* **10** (2025), article 62. https://doi.org/10.1007/s43036-025-00448-8
2. B. Lins and I. M. Spitkovsky, *Inverse continuity of the numerical range map for Hilbert space operators*, *Operators and Matrices* **14** (2020), 77--90. https://doi.org/10.7153/oam-2020-14-06
3. D. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826 (first posted 2026-10-21; qualitative nearby result, full-text comparison outstanding).
4. O. Toeplitz, *Das algebraische Analogon zu einem Satze von Fejér*, *Mathematische Zeitschrift* **2** (1918), 187--197; F. Hausdorff, *Der Wertvorrat einer Bilinearform*, *Mathematische Zeitschrift* **3** (1919), 314--316.
