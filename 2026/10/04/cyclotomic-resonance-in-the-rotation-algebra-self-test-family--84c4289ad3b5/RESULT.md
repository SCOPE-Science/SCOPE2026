# Cyclotomic resonance in the rotation-algebra self-test family
## Finding
For real \(t\), define
\[
\mathcal A_t=C^*\!\left\langle z,u,v\text{ unitary}\ \middle|\ zu=uz,\ zv=vz,\ uv=zvu,\ (z+z^*-t\mathbf 1)(u+v-2\mathbf 1)=0\right\rangle .
\]
Let
\[
E=\{\zeta+\overline\zeta:\zeta\text{ is a root of unity}\}=\{2\cos(2\pi p/q):p\in\mathbb Z,\ q\ge1\}.
\]
Then the character \(\tau_0(z)=\tau_0(u)=\tau_0(v)=1\) is the unique finite-dimensional tracial state of \(\mathcal A_t\) exactly when \(t\notin E\).

There is a complete phase picture for the trace mechanism used by Chen and Zhao. If \(|t|>2\), then \(\mathcal A_t\cong\mathbb C\). If \(t\in(-2,2)\setminus E\), then \(\mathcal A_t\) has, in addition to \(\tau_0\), a distinct amenable tracial state coming from an irrational rotation-algebra quotient. Thus the general projection construction of arXiv:2609.25117v1 produces, for every \(t\in(-2,2)\setminus E\), an extreme synchronous correlation with two answers and 250 questions that self-tests a maximally entangled state of Schmidt rank 36 but is not a robust self-test.

The cyclotomic set \(E\cap(-2,2)\) is countable dense, while \((-2,2)\setminus E\) is also dense. Hence the operator-algebraic hypothesis behind this non-robust self-test family has a sharp dense arithmetic resonance boundary.

## Assumptions and scope
All algebras are unital complex \(C^*\)-algebras and all displayed generators are unitary. A finite-dimensional tracial state means a tracial state whose GNS representation is finite-dimensional. The statement about 250 questions and Schmidt rank 36 uses the specific projection construction of arXiv:2609.25117v1, not an assertion that those sizes are minimal.

The theorem classifies the two trace hypotheses of that construction within the one-parameter presentation above. It does not claim that every resonant parameter is incapable of producing a non-robust self-test by some different presentation or construction.

## Proof
The assignment \(z,u,v\mapsto1\) satisfies every relation, so \(\tau_0\) exists for all real \(t\).

First suppose \(t\notin E\), and let \(\pi:\mathcal A_t\to M_n(\mathbb C)\) be a unital finite-dimensional representation. Because \(z\) commutes with \(u\) and \(v\), each eigenspace of \(Z=\pi(z)\) is invariant under \(U=\pi(u)\) and \(V=\pi(v)\). On a nonzero eigenspace of dimension \(r\), write \(Z=\mu I_r\). The relation \(UV=\mu VU\) gives \(\mu^r=1\) after taking determinants. Therefore \(\mu\) is a root of unity and \(\mu+\mu^{-1}\in E\). Since \(t\notin E\), the scalar \(\mu+\mu^{-1}-t\) is nonzero, and the last defining relation forces \(U+V=2I_r\). Taking adjoints as well gives
\[
(U-I_r)^*(U-I_r)+(V-I_r)^*(V-I_r)=0.
\]
Both summands are positive, hence \(U=V=I_r\). The relation \(UV=\mu VU\) then forces \(\mu=1\). Thus every finite-dimensional representation sends all three generators to the identity. Applying this to the GNS representation of any finite-dimensional tracial state proves that \(\tau_0\) is unique.

Conversely, suppose \(t\in E\). Choose a root of unity \(\zeta\) with \(t=\zeta+\overline\zeta\). If \(\zeta\ne1\), let \(q\) be its order and take the standard clock and shift unitaries \(U,V\in M_q(\mathbb C)\) satisfying \(UV=\zeta VU\). Setting \(Z=\zeta I_q\) satisfies all four relations because \(Z+Z^*-tI_q=0\). The normalized matrix trace pulled back along this representation is a finite-dimensional tracial state distinct from \(\tau_0\), since it sends \(z\) to \(\zeta\ne1\). If \(\zeta=1\), then \(t=2\); setting \(z=1\), choosing any scalar unitary \(u\ne1\), and taking \(v=1\) gives a distinct one-dimensional character. Therefore finite-dimensional trace uniqueness holds if and only if \(t\notin E\).

If \(|t|>2\), the central element \(z+z^*-t\mathbf1\) is invertible because the spectrum of \(z+z^*\) lies in \([-2,2]\). Hence \(u+v=2\mathbf1\), which by the same positivity identity gives \(u=v=\mathbf1\); then \(uv=zvu\) gives \(z=\mathbf1\). Thus \(\mathcal A_t\cong\mathbb C\).

Now let \(t\in(-2,2)\setminus E\) and choose \(\zeta\in\mathbb T\) with \(\zeta+\overline\zeta=t\). Then \(\zeta\) is not a root of unity. The irrational rotation algebra
\[
\mathcal R_\zeta=C^*\!\left\langle U,V\text{ unitary}\ \middle|\ UV=\zeta VU\right\rangle
\]
is nonzero, nuclear, and carries a tracial state; arXiv:2609.25117v1 uses exactly these facts to obtain an amenable trace. The assignments \(z\mapsto\zeta\mathbf1\), \(u\mapsto U\), and \(v\mapsto V\) define a quotient map \(\mathcal A_t\to\mathcal R_\zeta\), because the last relation vanishes in the quotient. Pulling back a tracial state gives an amenable trace \(\tau_1\) with \(\tau_1(z)=\zeta\ne1=\tau_0(z)\).

Chen and Zhao prove that a finitely presented algebra with a character that is its unique finite-dimensional tracial state and with a distinct amenable trace feeds their projection construction to give an extreme synchronous self-test that is not robust. For every \(t\in(-2,2)\setminus E\), the expanded monomial support of the four defining relations is the same as in their fixed example: good parameters cannot equal \(0\), because \(0\in E\). Consequently their count remains \(|S|=13\), \(|W|=14\), matrix size \(N=36\), and \(|X|=250\).

Finally, roots of unity are countable and dense in the unit circle, so their real traces \(2\cos(2\pi p/q)\) are countable and dense in \([-2,2]\). Every nonempty subinterval is uncountable, so the complement of \(E\) is also dense in \((-2,2)\).

## Verification
The determinant step is exact and uses only finite dimensionality. The positivity identity proves \(U=V=I_r\) without any spectral approximation. The converse uses explicit clock-shift matrices at every cyclotomic resonance except \(t=2\), where an explicit distinct character suffices. The exterior collapse uses functional calculus for the central unitary \(z\).

The source paper's full text was inspected at Proposition 5.2 and Theorem 5.3. It proves the special case corresponding to \(t=1/2\), records the root-of-unity determinant obstruction, constructs the irrational-rotation quotient, and computes 250 questions and Schmidt rank 36 from the monomial support. A separate rational-rotation reference confirms the standard finite-dimensional clock-shift realization and the \(q\)-dimensional irreducible representation structure for rational rotation parameters.

A bundled checker verifies the presentation-support count and the exact modular clock-shift commutation identities for representative orders. These finite checks are only consistency tests; the theorem is proved analytically above.

## Relationship to prior work
Chen and Zhao, arXiv:2609.25117v1, give one explicit rotation-algebra presentation with relation \((2z+2z^*-\mathbf1)(u+v-2\mathbf1)=0\), corresponding after harmless rescaling to \(t=1/2\). Their Proposition 5.2 proves uniqueness of the finite-dimensional trace for that single value and supplies one irrational-rotation amenable trace; Theorem 5.3 then gives the 250-question, Schmidt-rank-36 non-robust self-test. The paper does not state a one-parameter classification.

Lawton's arXiv:2111.02932v1 develops rational rotation \(C^*\)-algebras and their \(q\)-dimensional irreducible representations. That theory supplies background for the resonant clock-shift witnesses but does not couple the cyclotomic parameter to the Chen-Zhao presentation or classify when their two trace hypotheses hold.

The present finding upgrades the isolated coefficient choice to an exact arithmetic phase diagram: cyclotomic traces are precisely the finite-dimensional uniqueness obstructions, nonresonant interior parameters support the amenable/finite-dimensional trace separation, and exterior parameters collapse to the scalar algebra.

## Limitations
The theorem concerns this particular one-parameter presentation and the specific projection construction of arXiv:2609.25117v1. It does not classify all possible non-robust self-tests, nor does it prove minimality of 250 questions or Schmidt rank 36. At resonant values it proves failure of the unique-finite-dimensional-trace hypothesis, not impossibility of every alternative self-testing mechanism. No quantitative robustness modulus is asserted.

## References
1. R. Chen and Y. Zhao, “A non-robust quantum correlation self-test,” arXiv:2609.25117v1, 20 September 2026. In particular Proposition 5.2 and Theorem 5.3.
2. W. M. Lawton, “Tutorial on Rational Rotation \(C^*\)-Algebras,” arXiv:2111.02932v1, 4 November 2021.
