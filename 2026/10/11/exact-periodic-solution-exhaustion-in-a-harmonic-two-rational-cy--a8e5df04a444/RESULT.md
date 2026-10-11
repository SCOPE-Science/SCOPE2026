# Exact periodic-solution exhaustion in a harmonic two-rational-cycle Abel family

## Finding
For every choice of real parameters \(g>v>0\), \(w>s>0\), and \(k>0\), let
\[
G(t)=g+v\cos t,\qquad S(t)=w+s\sin t,
\]
and define the trigonometric polynomials
\[
A(t)=G(t)S(t)(S(t)+k)G'(t),\qquad
B(t)=-G(t)S'(t)-(2S(t)+k)G'(t).
\]
Then the Abel equation
\[
x'(t)=A(t)x(t)^3+B(t)x(t)^2
\]
has exactly three real \(2\pi\)-periodic solutions, all defined on the whole real line:
\[
x_0(t)=0,\qquad x_-(t)=\frac1{G(t)(S(t)+k)},\qquad
x_+(t)=\frac1{G(t)S(t)}.
\]
There are no other positive, negative, or nonrational \(2\pi\)-periodic solutions. The two nonzero solutions are hyperbolic: \(x_-\) is attracting and \(x_+\) is repelling. Their exact Floquet exponents are
\[
\Lambda_+=kJ(w)>0,\qquad \Lambda_-=-kJ(w+k)<0,
\]
where, for \(c>s\),
\[
J(c)=2sv\int_0^\pi\frac{\sin^2t}{(g+v\cos t)(c^2-s^2\sin^2t)}\,dt>0.
\]
The zero solution is nonhyperbolic and isolated, with local \(2\pi\)-return displacement
\[
\Pi(u)-u=\pi vs\,u^2+O(u^3)\qquad (u\to0).
\]
There are also no distinct periodic solutions with a period equal to an integer multiple of \(2\pi\): the scalar return map is strictly increasing wherever defined.

## Assumptions and scope
Parameters are fixed positive real numbers satisfying the strict inequalities above. Time is physical time and has forcing period \(2\pi\); \(\Pi(u)\) is the return value at \(2\pi\) of the solution starting at \(x(0)=u\), when it exists through that interval. Here a Floquet exponent means \(\int_0^{2\pi}\partial_x(A(t)x^3+B(t)x^2)\,dt\) computed along the periodic solution, and the multiplier is its exponential. Solutions are real classical solutions. The classification is for \(2\pi\)-periodic solutions and integer-multiple subharmonics, not a statement about arbitrary quasiperiodic forcing or unbounded solutions.

## Proof
**1. Two explicit solutions.** Write \(P_0=GS\) and \(P_1=G(S+k)\). Direct differentiation yields
\[
-P'_0=B+A/P_0,\qquad -P'_1=B+A/P_1.
\]
Therefore \(x=1/P_j\) satisfies the Abel equation. Both denominators are strictly positive. The zero function is also a solution. These algebraic invariant curves specialize the construction of Bravo, Calderón, and Ojeda [1, Proposition 2.10]; their existence is not a new assertion.

**2. Exclusion of all other periodic solutions.** Let \(x\) be a nonzero entire \(2\pi\)-periodic solution. By uniqueness, \(x\) has constant sign. Put \(W=1/x\) and \(z=W/G-S\). The equation and the definitions give the exact identity
\[
z'(t)=-\frac{G'(t)}{G(t)}\frac{z(t)(z(t)-k)}{S(t)+z(t)}.\tag{1}
\]
Since \(S+z=W/G\ne0\), this equation holds along the entire solution. The constant solutions \(z=0\) and \(z=k\) correspond exactly to \(x_+\) and \(x_-\). Uniqueness implies that, if \(z\) is neither, then \(z(t)\ne0,k\) for every \(t\), so \(z(t)(z(t)-k)\) has one fixed nonzero sign.

Set \(\xi=\log G(t)\), \(\xi_0=\log(g-v)\), and \(\xi_1=\log(g+v)\). For each \(\xi\) strictly between these values, the two times with \(\log G(t)=\xi\) are
\[
t_+(\xi)=\arccos((e^\xi-g)/v)\in(0,\pi),\quad
 t_-(\xi)=2\pi-t_+(\xi)\in(\pi,2\pi).
\]
Let \(q(\xi)=\sqrt{1-((e^\xi-g)/v)^2}\). The two values of the forcing are
\[
S_+(\xi)=w+s q(\xi),\qquad S_-(\xi)=w-s q(\xi),\qquad S_+>S_-.
\]
Define \(z_\pm(\xi)=z(t_\pm(\xi))\). Because \(d\xi/dt=G'/G\), equation (1) becomes on each half-period
\[
\frac{dz_\pm}{d\xi}=F_\pm(\xi,z_\pm),\qquad
F_\pm(\xi,z)=-\frac{z(z-k)}{S_\pm(\xi)+z}.\tag{2}
\]
The two curves share their values at both endpoints: \(z_+(\xi_0)=z_-(\xi_0)=z(\pi)\), and periodicity would imply \(z_+(\xi_1)=z_-(\xi_1)=z(0)=z(2\pi)\).

At any interior intersection \(z_+(\xi)=z_-(\xi)=z\), the two denominators \(S_\pm+z=W(t_\pm)/G(t_\pm)\) have the same nonzero sign, because \(x\) retains its sign. Hence
\[
F_-(\xi,z)-F_+(\xi,z)
=-\frac{(S_+-S_-)z(z-k)}{(S_-+z)(S_++z)}\ne0,\tag{3}
\]
whose sign \(\sigma=-\operatorname{sgn}(z(z-k))\) is independent of \(\xi\) and of the intersection. Near \(\xi_0\), integration of (2) from the common endpoint, using (3) and local Lipschitz continuity away from the nonzero denominators, gives \(\operatorname{sgn}(z_--z_+)=\sigma\) immediately to the right. Near \(\xi_1\), integration backward from the other common endpoint instead gives \(\operatorname{sgn}(z_--z_+)=-\sigma\) immediately to the left. A continuous difference cannot change between these signs without an interior zero; but at any such zero, (3) says the difference crosses zero only with derivative sign \(\sigma\), so it cannot pass from sign \(\sigma\) to sign \(-\sigma\). This contradiction excludes every other nonzero periodic solution, on both the positive and the negative half-lines. No assumption of rationality of the hypothetical solution entered this argument.

**3. Multipliers and stability.** For a nonzero periodic solution \(x=1/P\), using the periodic logarithmic derivative \(x'/x=A/P^2+B/P\) gives
\[
\int_0^{2\pi}\partial_x(Ax^3+Bx^2)\,dt
=\int_0^{2\pi}\frac{A(t)}{P(t)^2}\,dt.
\]
For \(P=P_0=GS\), this is \(k\int_0^{2\pi}G'/(GS)\,dt\), since \(\int_0^{2\pi}G'/G\,dt=0\). For \(P=P_1=G(S+k)\), it is \(-k\int_0^{2\pi}G'/(G(S+k))\,dt\). Pairing \(t\) and \(2\pi-t\) gives exactly \(\int_0^{2\pi}G'/(G(c+s\sin t))\,dt=J(c)>0\), with the displayed integral. This proves the exponents, strict hyperbolicity, and opposite stability types.

**4. The origin and subharmonics.** Since the vector field is \(B(t)x^2+O(x^3)\) near zero, standard finite-time smooth dependence yields \(\Pi(u)-u=u^2\int_0^{2\pi}B(t)\,dt+O(u^3)\). Integration using \(\int_0^{2\pi}GS'\,dt=\pi vs\) and \(\int_0^{2\pi}(2S+k)G'\,dt=-2\pi vs\) gives \(\int B=\pi vs>0\). Thus the origin is parabolic but isolated. Finally scalar uniqueness makes \(\Pi\) strictly increasing on each interval of initial data with existence through a period. An increasing map cannot have any periodic point of least period greater than one. Hence no additional integer-multiple subharmonic orbits exist.

## Verification
All identities in the proof are symbolic and apply to continuous parameter ranges. The accompanying standalone `verify.py` evaluates the exact invariant-curve residuals, return-map displacement, and Floquet exponents for several admissible parameter sets. It prints `CHECK_OK` if the numerical consistency tests pass. These finite tests do not replace the analytic comparison lemma or prove an infinite-dimensional claim.

For example, at \((g,v,w,s,k)=(3,1,2,1/2,1)\), the two nonzero initial values are \(1/12\) and \(1/8\); numerical quadrature gives exponents approximately \(-0.0611548687\) and \(+0.1413504910\), respectively.

## Relationship to prior work
Bravo, Calderón, and Ojeda [1, Proposition 2.10] give the source parameterization of two rational invariant curves. They establish rational-cycle bounds, not an exhaustive count of *all* real periodic solutions for the positive first-harmonic subfamily above. Bravo, Fernández, and Ojeda [2] study stability of singular positive cycles and provide bounds under other hypotheses. Huang, Tian, and Zhao [3] establish a Chebyshev criterion for at most two nonzero cycles subject to an extended-Chebyshev condition and prove results for linear-trigonometric and quadratic-polynomial coefficients; the displayed \(A\) generally has trigonometric degree greater than one, and the conditional bound does not itself supply the full uniform count and exact hyperbolic exponents here. The present assertion is the parameter-uniform negative/nonrational exhaustion and explicit stability ordering, not the earlier algebraic two-cycle construction.

## Limitations
The strict assumptions \(g>v>0\), \(w>s>0\), \(k>0\) are essential to the stated proof. Boundary cases such as \(s=0\), \(v=0\), or \(k=0\) are excluded. The result does not assert a classification for arbitrary trigonometric \(G,S\) or for general Abel coefficients. The priority comparison remains subject to the possibility of an equivalent but differently formulated earlier theorem, particularly general uniqueness criteria; this statement has not undergone independent audit.

## References
[1] J. L. Bravo, L. A. Calderón, I. Ojeda, *Rational Limit Cycles of Abel Differential Equations*, arXiv:2302.10743v1 (first posted 2023-02-21), Proposition 2.10, https://arxiv.org/abs/2302.10743.

[2] J. L. Bravo, M. Fernández, I. Ojeda, *Stability of Singular Limit Cycles for Abel Equations Revisited*, arXiv:2302.13642v1 (2023), https://arxiv.org/abs/2302.13642.

[3] J. Huang, R. Tian, Y. Zhao, *A Chebyshev Criterion for at Most Two Non-zero Limit Cycles in Abel Equations*, arXiv:2506.14091v1 (2025), https://arxiv.org/abs/2506.14091.

[4] A. Gasull, J. Llibre, *Limit Cycles for a Class of Abel Equations*, SIAM Journal on Mathematical Analysis 21 (1990), 1235–1244, DOI 10.1137/0521068.
