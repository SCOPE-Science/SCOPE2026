# Morse–Lyapunov existence is invisible to the full Taylor jet
## Finding
Let \(\varepsilon>0\) and consider the planar polynomial vector field
\[
f_\varepsilon(x_1,x_2)=\bigl(-\varepsilon x_1^3+x_2,-x_1^3-x_2^3\bigr).
\]
Jongeneel proves that the origin is globally asymptotically stable for this field and that no smooth Morse Lyapunov function exists. Introduce the standard flat scalar
\[
a(x)=\begin{cases}\exp(-1/\|x\|^2),&x\ne0,\\0,&x=0,\end{cases}
\]
and define
\[
F_-(x)=a(x)f_\varepsilon(x),\qquad F_+(x)=-a(x)x.
\]
Both fields are smooth and globally asymptotically stable at the origin. They have exactly the same complete Taylor jet at the origin—indeed every derivative of both fields at \(0\) is zero—but their Morse–Lyapunov behavior is opposite: \(F_+\) admits a smooth Morse Lyapunov function and \(F_-\) does not. Therefore the full Taylor jet of a smooth globally asymptotically stable planar vector field does not determine whether a smooth Morse Lyapunov function exists.

## Assumptions and scope
The statement is in the \(C^\infty\) category on \(\mathbb{R}^2\). A smooth Lyapunov function is understood in the sense used by Jongeneel: it is coercive, vanishes only at the equilibrium, has no other critical points, and decreases strictly along every non-equilibrium trajectory. A Morse Lyapunov function additionally has positive-definite Hessian at the equilibrium.

The conclusion concerns determination from the complete Taylor jet at one equilibrium. It does not assert that Morse–Lyapunov existence is invisible to the full local germ, to orbit data away from the equilibrium, or in the real-analytic category.

## Proof
Jongeneel's Proposition 3.5 supplies the field \(f_\varepsilon\) above for every \(\varepsilon>0\). The origin is globally asymptotically stable, with the smooth strict Lyapunov function
\[
V_0(x_1,x_2)=\frac{x_1^4}{4}+\frac{x_2^2}{2},
\]
and the proposition proves that no smooth Morse Lyapunov function can exist.

The function \(a\) is smooth, positive on \(\mathbb{R}^2\setminus\{0\}\), and flat at the origin. A flat smooth scalar multiplied by any smooth vector field is flat, so every derivative of \(F_-\) and \(F_+\) at the origin vanishes. Thus the two vector fields have identical complete Taylor jets.

For \(F_+\), take
\[
V_+(x)=\|x\|^2.
\]
Its Hessian at the origin is \(2I\), and for every \(x\ne0\),
\[
\langle\nabla V_+(x),F_+(x)\rangle=-2a(x)\|x\|^2<0.
\]
Moreover, along a nonzero radial trajectory with radius \(r\), one has \(\dot r=-a(r)r<0\). Hence the radius is nonincreasing and cannot converge to a positive limit; therefore every trajectory converges to the origin. This also gives Lyapunov stability. Thus \(F_+\) is globally asymptotically stable and \(V_+\) is a smooth Morse Lyapunov function.

For \(F_-\), multiplication by the positive scalar \(a\) away from the origin changes only the speed along each non-equilibrium orbit of \(f_\varepsilon\). More explicitly, if \(\phi_s\) is the flow of \(f_\varepsilon\), a trajectory of \(F_-\) through \(x_0\ne0\) can be written as \(x(t)=\phi_{s(t)}(x_0)\), where
\[
\dot s(t)=a(\phi_{s(t)}(x_0))>0.
\]
Since \(a\le1\), finite \(t\) gives finite \(s(t)\). If \(s(t)\) approached a finite limit as \(t\to\infty\), the corresponding point on the nonstationary \(f_\varepsilon\)-orbit would remain away from the origin and \(a\) would be bounded below there, contradicting boundedness of \(s(t)\). Hence \(s(t)\to\infty\), and global attractivity follows from that of \(f_\varepsilon\). Lyapunov stability is inherited because the same oriented orbits are traversed more slowly. Thus \(F_-\) is globally asymptotically stable.

Finally, suppose that \(W\) were a smooth Morse Lyapunov function for \(F_-\). For every \(x\ne0\), positivity of \(a(x)\) gives
\[
\langle\nabla W(x),f_\varepsilon(x)\rangle
=a(x)^{-1}\langle\nabla W(x),F_-(x)\rangle<0.
\]
Coercivity, the unique zero, the critical-point condition, and the positive-definite Hessian are properties of \(W\) itself and are unchanged. Therefore \(W\) would be a smooth Morse Lyapunov function for \(f_\varepsilon\), contradicting Proposition 3.5. Hence none exists for \(F_-\).

## Verification
The motivating preprint was inspected at the definition of smooth and Morse Lyapunov functions, the full statement and proof of Proposition 3.5, and Corollary 3.9. Proposition 3.5 gives the exact polynomial field, proves global asymptotic stability, and derives the Morse obstruction from its linearization. Corollary 3.9 states only a necessary semisimplicity condition and explicitly leaves the influence of higher-order terms unresolved.

The new argument uses no numerical experiment. Flatness of \(a\), the orbit-preserving positive time change on the punctured plane, the strict derivative identity for a hypothetical Lyapunov function, and the radial proof for \(F_+\) are all exact. The time-change argument also verifies forward completeness: \(a\le1\) prevents the reparameterized source time from reaching infinity at finite physical time.

## Relationship to prior work
Jongeneel's preprint establishes that Morse Lyapunov functions need not exist and gives a necessary condition on the non-hyperbolic part of the linearization. It notes that examples with zero linearization satisfy that necessary condition and that the effect of higher-order terms remains unclear. The construction here goes further in a different direction: it produces two globally asymptotically stable smooth vector fields with identical complete Taylor jets but opposite answers to the Morse–Lyapunov existence question. Consequently, no criterion depending only on any finite jet, or even on the entire formal Taylor series, can characterize this property in the smooth category.

Algaba, García, and Giné prove preservation of Lyapunov functions under their notion of smooth orbital equivalence, where the time multiplier satisfies \(\mu(0)=1\) and is therefore positive near the singular point. That result supports the general time-rescaling mechanism but does not imply the present construction: the flat multiplier used here vanishes at the origin, deliberately erasing every Taylor coefficient while preserving strict Lyapunov inequalities away from the origin.

## Limitations
The construction is intrinsically smooth and nonanalytic because the multiplier \(a\) is flat. No analogous statement is claimed for real-analytic vector fields, where a zero full Taylor series forces the germ to vanish. The result also does not classify which nonformal local or global data determine Morse–Lyapunov existence. It relies on the no-Morse conclusion of Jongeneel's Proposition 3.5, whose proof was independently reconstructed at the level of its Hessian argument but is not reproved from first principles here beyond the cited proposition.

## References
1. W. Jongeneel, *On global Lyapunov functions being Morse*, arXiv:2610.05626v1, first public 2026-10-04. Primary MSC 37B25.
2. A. Algaba, C. García, and J. Giné, *Geometric Criterium in the Center Problem*, Mediterranean Journal of Mathematics 13 (2016), 2593–2611, DOI:10.1007/s00009-015-0641-0.
