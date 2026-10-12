# Finite-precision Haar target volume is strictly ordered along the controlled-gate edge
## Finding
Watts, O’Connor, and Vala give an exact normalized Haar volume for a coordinate-cube target centered at any controlled two-qubit gate. Write the controlled-gate coordinate as \(c\), with the identity at \(c=0\) and the CNOT/CPHASE endpoint at \(c=\pi/2\), and let \(a\) be the side length of the target cube. For every nondegenerate admissible precision \(0<a<\pi/2\), their exact target volume \(V_a(c)\) is strictly increasing for
\[
a\le c\le \frac{\pi}{2}.
\]
Consequently, the CNOT/CPHASE endpoint uniquely has the largest effective Haar target volume within the full controlled-gate family at every admissible finite cube size. This is stronger than the common small-target scaling reported for nonlocal controlled gates: the ordering holds at finite \(a\), with no reversal anywhere on the admissible edge.

## Assumptions and scope
The statement uses exactly the Weyl-chamber convention and coordinate-cube target of Watts–O’Connor–Vala, Eq. (48). Define
\[
\begin{aligned}
A(a)&=8a+a\cos(3a)-9a\cos a,\\
B(a)&=3a\cos(3a)-3a\cos a-3\sin(3a)+9\sin a,\\
C(a)&=3a\cos(3a)-3a\cos a-6\sin(3a)+12\sin(2a)-6\sin a.
\end{aligned}
\]
Then their normalized target volume is
\[
V_a(c)=\frac{A(a)-B(a)\cos(2c)+C(a)\cos(4c)}{2\pi}.
\]
The source’s coordinate cube remains in the stated controlled-edge parameterization when \(0\le a\le c\le\pi/2\). The strict theorem concerns \(0<a<\pi/2\); at \(a=0\) the target volume degenerates, and at \(a=\pi/2\) the admissible interval contains only the endpoint.

## Proof
Differentiate the exact expression:
\[
\frac{\partial V_a}{\partial c}
=\frac{\sin(2c)}{\pi}\bigl(B(a)-4C(a)\cos(2c)\bigr).
\]
It therefore suffices to prove \(B(a)>4C(a)>0\) for \(0<a<\pi/2\).

Put
\[
t=\tan\frac a2,
\qquad 0<t<1,
\qquad a=2\arctan t.
\]
Elementary half-angle reduction gives
\[
B(a)=\frac{48t^2}{(1+t^2)^3}\Bigl(2t-a(1-t^2)\Bigr)
\]
and
\[
C(a)=\frac{48t^2(1-t^2)}{(1+t^2)^3}(2t-a).
\]
Since \(t>\arctan t\) for \(t>0\), one has \(2t-a=2(t-\arctan t)>0\), hence \(C(a)>0\).

For the stronger inequality, factor
\[
B(a)-4C(a)=\frac{48t^2}{(1+t^2)^3}F(t),
\]
where
\[
F(t)=6(1-t^2)\arctan t+8t^3-6t.
\]
Define
\[
G(t)=2t^3+t-(1+t^2)\arctan t.
\]
Direct differentiation gives
\[
F'(t)=\frac{12t}{1+t^2}G(t)
\]
and
\[
G'(t)=2t\bigl(3t-\arctan t\bigr)>0
\]
for every \(t>0\). Since \(F(0)=G(0)=0\), it follows that \(G(t)>0\) and then \(F(t)>0\) for \(t>0\). Thus \(B(a)>4C(a)>0\).

Finally, for \(a\le c<\pi/2\), one has \(\sin(2c)>0\) and \(\cos(2c)\le1\), so
\[
B(a)-4C(a)\cos(2c)\ge B(a)-4C(a)>0.
\]
Therefore \(\partial V_a/\partial c>0\) throughout the interior of the admissible interval. Continuity at \(c=\pi/2\) proves strict increase on the closed interval and the unique endpoint maximum.

## Verification
The proof is symbolic and exact. The source formula was checked directly in the full text around Eq. (48), together with its controlled-gate coordinate range and cube-size condition. Independent symbolic reconstruction verifies the derivative identity and the two nested derivative identities for \(F\) and \(G\). No numerical sampling, finite enumeration, or asymptotic truncation is used to infer the global sign.

The key boundary facts are explicit: \(a=0\) is excluded because the target volume is degenerate, and \(a=\pi/2\) leaves no nontrivial interval to order. The theorem makes no statement about target shapes other than the source’s coordinate cubes.

## Relationship to prior work
Watts–O’Connor–Vala derive the exact Haar-volume formula and emphasize that nonlocal controlled gates share a leading small-target scaling, but do not state or prove the finite-precision monotonic ordering in \(c\). Musz–Kuś–Życzkowski independently derive the Haar distribution of two-qubit interaction content and the perfect-entangler volume; those results determine the ambient measure but do not imply monotonicity of these moving coordinate-cube targets. Zhang–Vala–Sastry–Whaley supply the Weyl-chamber geometry underlying the controlled edge, without this Haar target-volume comparison.

Balakrishnan–Sankaranarayanan characterize controlled unitaries by operator-Schmidt structure and study entanglement measures along two-qubit edges. Those invariants are different from the Haar volume integrated over a finite coordinate target and do not imply the present ordering. Huang and collaborators later reuse effective target size as a gate-design metric and compare selected gates including CNOT, but their comparison does not establish a continuum theorem for all controlled gates.

## Limitations
The theorem is specific to the normalized Haar measure and coordinate-cube targets used in the source. It does not say that CNOT is easier to implement under every physical noise model, pulse-control constraint, norm ball, or compilation cost. It also does not compare controlled gates with gates off the controlled edge; the source itself identifies other globally favorable locations in the full Weyl chamber.

A literature search can never exclude every differently worded prior observation. The residual originality risk is that the same derivative inequality may have appeared under another target-volume terminology not located by searches over the source title, controlled-gate aliases, Haar-target terminology, Weyl-chamber terminology, and later effective-target-size literature.

## References
1. P. Watts, M. O’Connor, and J. Vala, “Metric Structure of the Space of Two-Qubit Gates, Perfect Entanglers and Quantum Control,” *Entropy* 15 (2013), 1963–1984. DOI: 10.3390/e15061963.
2. P. Musz, M. Kuś, and K. Życzkowski, “Unitary quantum gates, perfect entanglers, and unistochastic maps,” *Physical Review A* 87, 022111 (2013). DOI: 10.1103/PhysRevA.87.022111.
3. J. Zhang, J. Vala, S. Sastry, and K. B. Whaley, “Geometric theory of nonlocal two-qubit operations,” *Physical Review A* 67, 042313 (2003). DOI: 10.1103/PhysRevA.67.042313.
4. S. Balakrishnan and R. Sankaranarayanan, “Operator-Schmidt decomposition and the geometrical edges of two-qubit gates,” *Quantum Information Processing* 10 (2011). arXiv:1006.3412.
5. C. Huang et al., “Quantum Instruction Set Design for Performance,” *Physical Review Letters* 130, 070601 (2023). DOI: 10.1103/PhysRevLett.130.070601.
