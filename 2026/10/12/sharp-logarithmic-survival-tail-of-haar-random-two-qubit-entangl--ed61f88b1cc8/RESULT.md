# Sharp logarithmic survival tail of Haar-random two-qubit entanglement under independent dephasing

## Finding
Let \(|\psi\rangle=a|00\rangle+b|01\rangle+c|10\rangle+d|11\rangle\) be Haar distributed on the unit sphere of \(\mathbb C^4\). Apply \(\mathcal D_s\otimes\mathcal D_s\), where \(\mathcal D_s\) multiplies each single-qubit computational-basis off-diagonal entry by \(s\) and leaves the diagonal unchanged. The probability \(p(s)\) of retaining two-qubit entanglement obeys the sharp two-term endpoint law
\[
p(s)=8s^4\log(1/s)-2s^4+O(s^6\log(1/s)),\qquad s\downarrow0.
\]
The coefficient of the logarithmic term is exactly \(8\), and the next nonlogarithmic coefficient is exactly \(-2\). For every \(0<s<\sqrt2-1\), define
\[
e=\frac{s}{1-s^2},\qquad v_- = \frac{\sqrt{1+4e^2}-1}{2e},\qquad v_+ = \frac{1-\sqrt{1-4e^2}}{2e},
\]
and \(F(h)=h\log(1/h)/(1-h)^2-h/(1-h)\) for \(0<h<1\). Then the fully explicit nonasymptotic enclosure holds:
\[
2F(v_-^4)\le p(s)\le 2F(v_+^4).
\]
With Markovian visibility \(s=e^{-\gamma t}\) for \(\gamma>0\), this is equivalently
\[
p(e^{-\gamma t})=(8\gamma t-2)e^{-4\gamma t}+O(t e^{-6\gamma t})\quad(t\to\infty).
\]
The same leading mass arises from two disjoint, equally probable asymptotic mechanisms: \(|ad|\ll|bc|\) or \(|bc|\ll|ad|\).

## Assumptions and scope
The initial state is a *complex* Haar-uniform normalized pure state; its four coordinates are not independent after normalization. The noise comprises two identical, independent local, zero-temperature-free pure-dephasing channels in the stated computational basis; no unitary coupling or population relaxation occurs. For \(s>0\), entanglement means nonseparability, equivalently negative partial transpose (NPT) for two qubits. At \(s=0\), every output is diagonal and separable. The asymptotic describes \(s\downarrow0\) through strictly positive values; it does not claim entanglement survives at \(s=0\). The constants in the \(O\)-term are absolute for sufficiently small positive \(s\).

## Proof
**1. Exact statewise threshold.** Put \(P=ad\), \(Q=bc\), \(A=|P|\), \(B=|Q|\), and \(X=|P-Q|\). The exact concurrence for independent identical phase damping, given by Fonseca-Romero, Martínez-Rincón, and Viviescas (2012, Eq. (8)) in the convention with residual coherence \(s=1-q\), is
\[
C_s=\left[-(1-s^2)(A+B)+\sqrt{(1-s^2)^2(A-B)^2+4s^2X^2}\right]_+.
\]
The positive part is \([y]_+=\max\{0,y\}\). Since \((A+B)^2-(A-B)^2=4AB\), elementary squaring of nonnegative terms shows, for \(0<s<1\),
\[
C_s>0\quad\Longleftrightarrow\quad sX>(1-s^2)\sqrt{AB}.
\]
This is a strict inequality except for a null boundary under the Haar measure. The exact concurrence formula follows from the two-qubit spin-flip criterion (Wootters, 1997) and was independently checked against direct \(4\times4\) output partial-transpose eigenvalues in the accompanying verifier. This is the sole quantum-theoretic input; all subsequent calculations are elementary probability and inequalities.

**2. Independent Gaussian products.** Generate Haar measure by \((a,b,c,d)=G/\|G\|_2\), where the four entries of \(G\) are independent standard circular complex Gaussians. Homogeneity removes \(\|G\|_2\) from the concurrence threshold. Thus \(U=|a|^2|d|^2\) and \(V=|b|^2|c|^2\), evaluated in the unnormalized Gaussian coordinates, are independent products of two independent unit-exponential variables. Their positive square roots are \(A=\sqrt U\) and \(B=\sqrt V\). The relative phase of \(P,Q\) is independent and uniform on the circle.

For independent unit exponentials \(E,E'\), the ratio \(E/E'\) has cumulative distribution \(h/(1+h)\), \(h>0\), and density \((1+h)^{-2}\). Consequently \(U/V\) has the distribution of a product of two independent such ratios. For \(0<h<1\), direct conditioning gives the *exact* cumulative distribution
\[
\begin{aligned}
F(h)&=\Pr\{U/V<h\}
=\int_0^\infty\frac{h\,\mathrm du}{(u+h)(1+u)^2}\\
&=\frac{h\log(1/h)}{(1-h)^2}-\frac{h}{1-h}
=h\log(1/h)-h+O(h^2\log(1/h)).
\end{aligned}
\]
The equality is verified by splitting the integrand into elementary partial fractions. By exchange symmetry, for \(0<h<1\), the two events \(U<hV\) and \(V<hU\) are disjoint and each has probability \(F(h)\).

**3. Sharp phase-independent sandwich.** Define \(e=s/(1-s^2)\). By step 1, survival requires \(\sqrt{AB}/|P-Q|<e\). On the event \(A\le B\), put \(t=\sqrt{A/B}\in[0,1]\). The reverse triangle inequality and the triangle inequality give
\[
\frac{t}{1+t^2}\le\frac{\sqrt{AB}}{|P-Q|}\le\frac{t}{1-t^2},
\]
where the final quotient is understood as infinite at \(t=1\). Suppose \(e<1/2\), equivalent to \(s<\sqrt2-1\). The two scalar functions are strictly increasing on \([0,1]\). The equation \(t/(1-t^2)=e\) has positive root \(v_-=(\sqrt{1+4e^2}-1)/(2e)\); the equation \(t/(1+t^2)=e\) has its first root \(v_+=(1-\sqrt{1-4e^2})/(2e)\) in \((0,1)\). Therefore every state with \(t<v_-\) survives, while no state with \(t>v_+\) survives. Since \(t^4=U/V\), and swapping \(U,V\) handles \(A>B\), step 2 proves
\[
2F(v_-^4)\le p(s)\le2F(v_+^4).
\]
No approximation to the relative phase has been made.

**4. Endpoint extraction, including the constant term.** Taylor expansions of the explicit radicals yield \(v_-=e+O(e^3)\) and \(v_+=e+O(e^3)\), hence \(v_\pm^4=e^4(1+O(e^2))\). The exact formula for \(F\) gives, uniformly for those endpoints,
\[
2F(v_\pm^4)=8e^4\log(1/e)-2e^4+O(e^6\log(1/e)).
\]
The sandwich forces the same two-term expansion for \(p(s)\). Finally \(e=s/(1-s^2)=s(1+O(s^2))\), so substitution changes the expansion only by \(O(s^6\log(1/s))\). The Markovian-time expression follows by putting \(s=e^{-\gamma t}\). Symmetry of \(U,V\) proves equal contributions from the two extremal amplitude-ratio mechanisms. This completes the proof.

## Verification
The self-contained script `verify.py` (with dependencies in `requirements.txt`) constructs Haar states by normalized independent complex Gaussians, independently implements both local dephasing channels on their \(4\times4\) density matrices, and tests the NPT criterion against the statewise scalar threshold. It also computes the survival probability by an independent one-dimensional angular integral of the exact ratio density and compares it with the analytic two-sided enclosure and asymptotic. Run `python verify.py` after installing `requirements.txt`. Numerical checks are finite consistency tests; the proof for all states and the exact limit are the inequalities in steps 1–4.

## Relationship to prior work
Wootters (arXiv:quant-ph/9709029, first posted 1997-09-12) supplies the concurrence test for arbitrary two-qubit states. Fonseca-Romero, Martínez-Rincón, and Viviescas, *A statistical portrait of the entanglement decay of two-qubit memories* (arXiv:1210.5645, first posted 2012-10-20), derive the general statewise phase-damping concurrence and express the phase-damping separation-time density as an unevaluated joint-parameter integral (their Eqs. (5), (8) and Sec. III/VI). In particular their work already establishes that almost every input loses entanglement at a finite dephasing time. This result does **not** re-claim that distribution or the statewise criterion: it derives the previously unstated sharp two-term near-complete-dephasing tail and rigorous explicit finite-visibility bounds by reducing the Haar endpoint to an exact product-ratio distribution. Datta (arXiv:1004.1317) treats a different Haar observable, the negativity of initial pure states, without an environmental dephasing tail.

## Limitations
The expansion is only for independent *identical* phase damping and complex-Haar initial pure states. It says nothing about the average concurrence magnitude, mixed initial states, unequal residual coherences, quantum channels with population relaxation, or fixed-size finite-s experiments outside the displayed bound range. An exact integral for the whole phase-damping separation-time distribution was known; the contribution is an explicit singular endpoint extraction with a sharp constant and next term. Equivalent endpoint asymptotics in other literature have not been conclusively excluded; no independent audit or priority certification has been performed.

## References
1. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, arXiv:quant-ph/9709029, first posted 1997-09-12, https://arxiv.org/abs/quant-ph/9709029.
2. A. Datta, *On the negativity of random pure states*, arXiv:1004.1317, first posted 2010-04-08, https://arxiv.org/abs/1004.1317.
3. K. M. Fonseca-Romero, J. Martínez-Rincón, C. Viviescas, *A statistical portrait of the entanglement decay of two-qubit memories*, arXiv:1210.5645, first posted 2012-10-20, https://arxiv.org/abs/1210.5645.
