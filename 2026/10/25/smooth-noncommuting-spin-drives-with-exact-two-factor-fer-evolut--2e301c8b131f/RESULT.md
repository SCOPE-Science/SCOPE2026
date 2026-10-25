# Smooth noncommuting spin drives with exact two-factor Fer evolution at unbounded pulse area

## Finding

The Fer exponential-product expansion for a time-dependent spin Hamiltonian can terminate **exactly after its second factor**, even though the Hamiltonian does not commute with itself at different times. This occurs for an infinite sequence of explicit resonant spin-control amplitudes and a continuously parametrized family of compactly supported \(C^\infty\) pulses. For a qubit, their integrated operator norm can be made arbitrarily large, notwithstanding the general sufficient convergence threshold near \(2.6058\) established by Bagnasacco and Giovannetti [1].

Precisely, let \(r_n>0\) be the unique root of
\[
\tan(2r_n)=2r_n,\qquad n\pi<2r_n<(n+\tfrac12)\pi,\quad n=1,2,\ldots.
\]
Define the nonzero coefficient
\[
A_n=\frac{1-(-1)^n\sqrt{1+4r_n^2}}{2}.
\]
For every such \(n\) and every \(\Theta>0\), the compactly supported smooth noncommuting Hamiltonian constructed below has, in every nontrivial finite-dimensional unitary spin representation, the **exact all-time propagator**
\[
U(t)=\exp\bigl(-i\mathbf f(t)\cdot\mathbf T\bigr)
       \exp\bigl(-i A_n\Theta S(t-1)T_z\bigr),\qquad t\ge0,
\]
where the displayed exponentials are **the first and second factors of the usual Fer recursion**, the second factor is not identically the identity on the angular segment, and the third effective Hamiltonian vanishes identically. For Pauli matrices \(\mathbf T=\boldsymbol\sigma\),
\[
\int_0^\infty\|H(t)\|_{\mathrm{op}}\,dt=r_n(1+\Theta),
\]
which is unbounded as \(\Theta\to\infty\) at fixed \(n\). This does not assert that a universal convergence radius can be increased: it exhibits exactly solvable trajectories outside that sufficient domain.

## Assumptions and scope

Let \(T_x,T_y,T_z\) be any nontrivial finite-dimensional Hermitian unitary representation satisfying \([T_a,T_b]=2i\sum_c\epsilon_{abc}T_c\). The qubit choice is \(T_a=\sigma_a\); the spin-\(j\) choice is \(T_a=2J_a\). Let \(S:\mathbb R\to[0,1]\) be the standard smooth switch
\[
\eta(u)=\begin{cases}e^{-1/u},&u>0,\\0,&u\le0,\end{cases}
\qquad
S(u)=\frac{\eta(u)}{\eta(u)+\eta(1-u)}.
\]
Thus \(S=0\) on \(( -\infty,0]\), \(S=1\) on \([1,\infty)\), all endpoint jets vanish, and \(S'(u)>0\) for \(0<u<1\).

For an integer \(n\ge1\), let \(r=r_n\). For arbitrary \(\Theta>0\) define
\[
\mathbf f(t)=\begin{cases}
 rS(t)(1,0,0),&t\le1,\\
 r\bigl(\cos\vartheta(t),\sin\vartheta(t),0\bigr),&t\ge1,
\end{cases}
\quad \vartheta(t)=\Theta S(t-1),\qquad H(t)=\dot{\mathbf f}(t)\cdot\mathbf T.
\]
These branches agree to every derivative at \(t=1\), and \(H\) vanishes outside \((0,2)\). The Schrödinger equation is \(\dot U(t)=-iH(t)U(t)\), \(U(0)=I\). Throughout, \(\hbar=1\). The pulse is not real analytic at its support boundaries.

For definiteness, the standard Fer recursion is
\[
F_j(t)=-i\int_0^t H_j(u)\,du,\qquad H_1=H,
\]
\[
H_{j+1}(t)=e^{-F_j(t)}H_j(t)e^{F_j(t)}
 -\int_0^1e^{-sF_j(t)}H_j(t)e^{sF_j(t)}\,ds.
\]
The expansion is \(U=e^{F_1}e^{F_2}\cdots\), with an exact remainder after every finite number of factors [1,2].

## Proof

**1. Resonances.** Write \(x=2r\). In each interval \((n\pi,(n+\tfrac12)\pi)\), \(\tan x-x\) increases strictly from a negative value to \(+\infty\), since its derivative is \(\tan^2x>0\) in the interior. There are no other strictly positive roots: \(\tan x>x\) on \((0,\pi/2)\), while on the intervening negative-tangent intervals \(\tan x<0<x\). At each root, \(\cos x=(-1)^n/\sqrt{1+x^2}\). In particular all \(r_n\) are nonzero and discrete.

**2. Closed one-step map.** At a time where \(\mathbf f(t)\ne0\), put \(r=\|\mathbf f(t)\|\) and \(\mathbf h=\dot{\mathbf f}(t)\). The Pauli/spin commutator identity, or its Rodrigues-conjugation form, applied to the Fer recursion gives
\[
\mathbf h_2
=\alpha(r)(\mathbf f\times\mathbf h)
 +\beta(r)((\mathbf f\times\mathbf h)\times\mathbf f),
\]
where \(H_2=\mathbf h_2\cdot\mathbf T\) and
\[
\alpha(r)=\frac{1-\cos(2r)}{2r^2}-\frac{\sin(2r)}r,
\qquad
\beta(r)=\frac{\cos(2r)}{r^2}-\frac{\sin(2r)}{2r^3}.
\]
For completeness, decompose \(\mathbf h\) into components parallel and perpendicular to \(\mathbf f\), use
\[
e^{i\mathbf f\cdot\mathbf T}(\mathbf h\cdot\mathbf T)e^{-i\mathbf f\cdot\mathbf T}
=\biggl(\mathbf h_{\parallel}+\cos(2r)\mathbf h_{\perp}
 -\frac{\sin(2r)}r\mathbf f\times\mathbf h\biggr)\cdot\mathbf T,
\]
and subtract the average of the same conjugation with \(\mathbf f\) replaced by \(s\mathbf f\), integrated over \(0\le s\le1\). The transverse coefficient is \(\cos(2r)-\sin(2r)/(2r)=r^2\beta(r)\); the cross-product coefficient is \(\alpha(r)\). At \(\mathbf f=0\) the formula follows by continuity.

**3. Exact two-stage geometry.** For \(t\le1\), both \(\mathbf f\) and \(\dot{\mathbf f}\) lie on the \(x\)-axis, so their cross product vanishes and \(H_2(t)=0\). For \(t>1\), set \(\vartheta=\Theta S(t-1)\). We have
\[
\mathbf f\times\dot{\mathbf f}=r_n^2\dot\vartheta\,(0,0,1),
\quad
(\mathbf f\times\dot{\mathbf f})\times\mathbf f=r_n^2\dot{\mathbf f}.
\]
The resonant identity \(\sin(2r_n)=2r_n\cos(2r_n)\) makes \(\beta(r_n)=0\). Therefore
\[
H_2(t)=A_n\dot\vartheta(t)T_z,
\qquad A_n=r_n^2\alpha(r_n).
\]
Using the root and the sign of its cosine yields
\[
A_n=\tfrac12\bigl(1-(1+4r_n^2)\cos(2r_n)\bigr)
=\tfrac12\bigl(1-(-1)^n\sqrt{1+4r_n^2}\bigr)\ne0.
\]
As \(\vartheta(0)=0\), this integrates to \(F_2(t)=-iA_n\vartheta(t)T_z\). Hence \([F_2(t),H_2(t)]=0\) at every \(t\). Substitution into the Fer recursion gives \(H_3\equiv0\), so the exact remainder after two factors is the identity and
\[
U(t)=e^{F_1(t)}e^{F_2(t)},\qquad F_1(t)=-i\mathbf f(t)\cdot\mathbf T.
\]
Since \(A_n\ne0\), \(H_2\not\equiv0\) for \(\Theta>0\). Thus the first Fer factor alone is not exact. For one time in \((0,1)\), the driving vector is proportional to the \(x\)-axis, whereas at a time just after \(1\) the angular derivative has a nonzero \(y\)-component. Their matrix commutator is nonzero in every nontrivial spin representation, proving noncommutation.

**4. Unbounded integrated norm.** In the Pauli representation \(\|\mathbf h\cdot\boldsymbol\sigma\|_{\mathrm{op}}=\|\mathbf h\|\). The radial segment has path length \(r_n\int_0^1 S'(t)\,dt=r_n\). The angular segment has path length \(r_n\int_1^2\Theta S'(t-1)\,dt=r_n\Theta\). Their sum is \(r_n(1+\Theta)\), arbitrarily large with fixed resonant \(r_n\). For instance \(n=1\), \(\Theta=\pi/2\) gives \(r_1\simeq2.24670472895\), \(A_1\simeq2.80166942438\), and pulse area \(5.77582026459\), already above the published sufficient threshold \(2.6058\).

## Verification

The fully standalone `fer_two_factor_verify.py` computes resonances by bracketing \(\tan(2r)=2r\); tests the derived trigonometric expression for \(A_n\); evaluates the first Fer remainder against \(A_n\dot\vartheta\,T_z\); and independently integrates the Schrödinger equation with high-accuracy adaptive ODE integration. It then compares the resulting propagator with the claimed two-exponential product in the qubit, spin-one, and spin-three-halves representations. Executing the bundled script with NumPy and SciPy passed **3256 numerical assertions**; the largest reported matrix-norm discrepancy in the eight test cases was below \(10^{-9}\). These finite numerical tests do not prove the all-parameter claim, which follows analytically from the previous section.

## Relationship to prior work

Bagnasacco and Giovannetti [1], first public on 2026-09-23, establish a sufficient operator-norm pulse-area radius of approximately \(2.6058\) for the general Hermitian Fer recursion and the exact recursion used here. Their guarantee is universal and sufficient, not a criterion excluding convergence outside the radius. Blanes, Casas, Oteo and Ros [2] establish earlier convergence bounds and use the same recursive factorization; their convergence theorems do not settle finite termination for the present noncommuting smooth pulses.

Bagnasacco, Burgarth, Giovannetti and Yuasa [3] subsequently prove rigidity of finite termination for **real-analytic** spin driving functions, and derive an equivalent \(\mathfrak{su}(2)\) closed Fer map. Their theorem requires real analyticity; the present compactly supported nonzero smooth pulse has flat, nonanalytic transition points and therefore lies outside that theorem. The examples here do not contradict the analytic rigidity result. The new contribution is the explicit countable resonance family, exact nontrivial two-factor termination throughout the smooth pulse, and unbounded accumulated norm at fixed resonance.

## Limitations

The result constructs a special family of smooth, compactly supported spin drives. It does not show that generic smooth pulses terminate, provide a radius of convergence improved for all Hermitian drives, or imply universal advantages over direct numerical integration. The published analytic rigidity result [3] is not challenged on its stated assumptions. Exact termination relies on the resonant equality \(\tan(2r_n)=2r_n\), with no claim of stability of exact termination under amplitude detuning. The finding's priority has not been independently certified; a broader existing construction of finitely terminating nonanalytic Fer products may exist.

## References

[1] L. Bagnasacco and V. Giovannetti, *Improved convergence radius of the Fer expansion for Hermitian generators*, arXiv:2609.28302v1 (first submitted 2026-09-23), https://arxiv.org/abs/2609.28302.

[2] S. Blanes, F. Casas, J. A. Oteo and J. Ros, *Magnus and Fer expansions for matrix differential equations: the convergence problem*, Journal of Physics A 31 (1998), 259–268, DOI:10.1088/0305-4470/31/1/023.

[3] L. Bagnasacco, D. Burgarth, V. Giovannetti and K. Yuasa, *The Fer expansion of a driven spin under su(2) operations cannot terminate beyond first order*, arXiv:2610.27979v1 (first submitted 2026-10-20), https://arxiv.org/html/2610.27979v1.
