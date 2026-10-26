# Sharp half-density Gabor frame bounds for asymmetric two-sided exponentials

## Finding

For arbitrary rates \(a,b>0\), let
\[
g_{a,b}(x)=\begin{cases}e^{-ax},&x\geq0,\\ e^{bx},&x<0.\end{cases}
\]
The lattice Gabor system \(\{e^{\pi i m x}g_{a,b}(x-n):m,n\in\mathbb Z\}\) has the following *optimal* lower and upper frame bounds, including the locations of every extremizing Zak fiber.

Put \(u=e^{-a}\), \(v=e^{-b}\), and
\[
\alpha=\frac1{1+u^2},\qquad
\beta=\frac{v^2}{1+v^2},\qquad
\gamma=\frac{v(u+v)}{(1+u^2)(1+v^2)}.
\]
Define
\[
y_* = \frac{(b-a)\gamma+\sqrt{(b-a)^2\gamma^2+4ab\alpha\beta}}{2b\beta},
\qquad x_* = \frac{\log y_*}{a+b}.
\]
Then \(0<x_*<1\), and the sharp lower bound is
\[
\boxed{A_{a,b}=2\left(\alpha e^{-2ax_*}+\beta e^{2bx_*}-2\gamma e^{(b-a)x_*}\right).}
\]
The sharp upper bound is
\[
\boxed{B_{a,b}=2\left[\left(\frac1{1-u^2}+\frac{v^2}{1-v^2}\right)^2+
\left(\frac{u}{1-u^2}+\frac{v}{1-v^2}\right)^2\right].}
\]
With the Zak convention below, the lower bound occurs precisely at \(x\equiv x_*\pmod 1\) and \(\omega\equiv1/4\pmod{1/2}\), while the upper bound occurs precisely at \(x\equiv0\pmod 1\) and \(\omega\equiv0\pmod{1/2}\). Consequently the exact spectral condition number is \(B_{a,b}/A_{a,b}\). Interchanging \(a,b\) reflects the lower-fiber position: \(x_*(b,a)=1-x_*(a,b)\).

## Assumptions and scope

All rates are strictly positive, without an equality-of-rates restriction. The generator is *not* \(L^2\)-normalized; multiplying it by a scalar multiplies both bounds by the squared modulus. The lattice has translation step one and modulation step one-half, hence redundancy two. Frame bounds are the optimal constants in the usual squared-coefficient frame inequality on \(L^2(\mathbb R)\). No assertion is made for other lattice densities, generators, or for sharp bounds under perturbations of the window.

The Zak transform is defined for \(0\leq x<1\) by
\[
Zg(x,\omega)=\sum_{k\in\mathbb Z}g(x+k)e^{-2\pi i k\omega}.
\]
For redundancy two, Zak diagonalization gives
\[
A_{a,b}=\mathop{\rm ess\,inf}_{0\le x,\omega<1} S(x,\omega),\quad
B_{a,b}=\mathop{\rm ess\,sup}_{0\le x,\omega<1} S(x,\omega),
\quad S=|Zg(x,\omega)|^2+|Zg(x,\omega+1/2)|^2.
\]
The window is continuous and exponentially decaying, so the fiber function is continuous and these extrema are attained.

## Proof

**1. Explicit fiber.** For \(0\le x<1\), write \(P=e^{-ax}\), \(Q=e^{bx}\), and \(t=e^{2\pi i\omega}\). Summing both exponential tails gives the absolutely convergent identity
\[
Zg(x,\omega)=\frac{P}{1-u/t}+\frac{Qvt}{1-vt}.
\]
Splitting lattice indices into even and odd classes, let \(q=t^2\). Then \(Zg=E+O\), \(Zg(x,\omega+1/2)=E-O\), where
\[
E=\frac{q(C_e+D_eq)}{(q-u^2)(1-v^2q)},\quad
O=\frac{t(C_o+D_oq)}{(q-u^2)(1-v^2q)},
\]
\[
C_e=P-Qu^2v^2,\quad D_e=v^2(Q-P),\quad
C_o=u(P-Quv),\quad D_o=v(Q-Puv).
\]
For \(0\le x\le1\), \(u\le P\le1\), \(1\le Q\le1/v\), and \(Q\ge P\). Hence all four coefficients are nonnegative; in fact \(C_e>0\) and \(D_o>0\), and at least one of the two products \(C_eD_e\), \(C_oD_o\) is strictly positive.

**2. Rigidity of the frequency extremes.** Writing \(c=\cos(4\pi\omega)\), the parity identity yields
\[
S(x,\omega)=\frac{2\bigl(C_e^2+D_e^2+C_o^2+D_o^2+2(C_eD_e+C_oD_o)c\bigr)}{(1+u^4-2u^2c)(1+v^4-2v^2c)}.
\]
For each fixed \(x\), the numerator is positive and strictly increasing in \(c\), and each positive denominator factor strictly decreases in \(c\in[-1,1]\). Thus \(S\) is strictly increasing in \(c\), which proves the unique frequency classes of the minimum and maximum.

**3. Spatial minimum.** Substituting \(c=-1\) simplifies the fiber to
\[
S_-(x)=2\left[\alpha e^{-2ax}+\beta e^{2bx}-2\gamma e^{(b-a)x}\right].
\]
Its derivative has the sign of \(Q_0(y)=-a\alpha+b\beta y^2-(b-a)\gamma y\), where \(y=e^{(a+b)x}\). The quadratic has exactly one positive zero \(y_*\), given above; its other zero is negative. With \(D=(1+u^2)(1+v^2)\), direct simplification gives
\[
Q_0(1)=-\frac{(1-uv)(a+buv)}D<0,
\qquad Q_0((uv)^{-1})=\frac{(1-uv)(auv+b)}{u^2D}>0.
\]
Therefore \(1<y_*<(uv)^{-1}\), so \(x_*\in(0,1)\), and \(S_-\) strictly decreases before and strictly increases after \(x_*\). This proves both the lower bound and its complete equality set.

**4. Spatial maximum.** At \(c=1\),
\[
S_+(x)=2\left[\left(\frac{P}{1-u^2}+\frac{Qv^2}{1-v^2}\right)^2+
\left(\frac{Pu}{1-u^2}+\frac{Qv}{1-v^2}\right)^2\right].
\]
Its expansion is a positive linear combination of \(e^{-2ax}\), \(e^{2bx}\), and \(e^{(b-a)x}\). The second derivative is strictly positive for every \(x\in[0,1]\), hence the maximum is attained only at an endpoint. Zak quasi-periodicity gives \(S_+(1)=S_+(0)\), and evaluating the latter gives the stated upper bound. Since the lower bound is strictly positive, the system is a frame.

**5. Reflection of rates.** The identity \(g_{a,b}(-x)=g_{b,a}(x)\) sends the Zak spatial coordinate \(x\) to \(1-x\), preserving the entire frame-symbol range, and proves the reflected minimizer formula.

## Verification

The standalone `check.py` uses exact symbolic rational identities to reconstruct the parity numerators, the \(c=-1\) formula, and the left-endpoint derivative sign. It also evaluates 72 deterministically sampled positive rate pairs, comparing 864 fiber values from the geometric formula against direct 601-term Zak sums, and tests the claimed extrema. Execute `python check.py` with Python 3, SymPy, and NumPy. `check_output.txt` is the recorded output. These finite checks are diagnostic only; the all-parameter statement follows from the proof above.

For \(a=1\), \(b=3\), the formulas yield \(x_*=0.65315441967\), \(A_{1,3}=0.456191869778\), and \(B_{1,3}=3.13852682883\). The equality-of-rates case \(a=b=1\) instead gives \(x_*=1/2\).

## Relationship to prior work

The Zak characterization of frame bounds and the single fundamental-domain Zak zero for totally positive windows are classical. Kloos and Stöckler (2013) prove the frame property for all totally positive finite-type windows and give lower bounds for **even** two-sided exponentials; their Section 5 does not claim these exact two-parameter asymmetric optimum formulas. Kloos (2014) gives global Zak zero uniqueness, not the full oversampled fiber extrema. The present result concerns the nonsymmetric two-rate family and determines both sharp bounds and every extremizing fiber at redundancy two, rather than merely frame existence or the symmetry-restricted case. An independently established equivalence from the general Gabor-frame literature could reduce its historical novelty, and publication priority is not certified.

## Limitations

The formula is specific to a translation step of one and modulation step of one-half. It is not an optimal-lattice theorem over varying lattice aspect ratios, nor a characterization of dual Gabor windows. The exactness is mathematical; the computations are consistency checks, not independent validation. Exhaustive historical coverage and independent mathematical audit have not been performed.

## References

- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, first posted 2013-11-28, https://arxiv.org/abs/1311.7359 .
- T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539, first posted 2014-11-06, https://arxiv.org/abs/1411.1539 .
