# Conditional exact Floquet spectrum for fourth-order blow-up profiles
## Finding
For every \(q>1\), set \(\eta=-4/(q-1)\) and define
\[
P_q(z)=\prod_{j=0}^{3}(z-\eta+j).
\]
If \(w\) is any nonconstant \(T\)-periodic solution of
\[
P_q(D)w+|w|^{q-1}w=0,
\]
then the Floquet multipliers of the variational equation along \(w\), counted with algebraic multiplicity, are exactly
\[
1,\qquad e^T,\qquad e^{-\sigma T},\qquad e^{-(\sigma+1)T},
\qquad \sigma=\frac{3q+5}{q-1}.
\]
Thus Floquet exponents can be chosen as
\[
0,\qquad 1,\qquad -\frac{3q+5}{q-1},\qquad -\frac{4(q+1)}{q-1}.
\]
In particular, every such periodic orbit is hyperbolic modulo the phase direction. For \(q=3\), the exponents are exactly \(0,1,-7,-8\).

This establishes the Floquet-exponent part of Conjecture 1 in D'Ambrosio--Lessard--Pugliese conditional only on the existence of the periodic orbit. Their conjectured existence statement for every \(q>1\) is not proved here.

## Assumptions and scope
The equation above is the auxiliary fourth-order equation \((W_q)\) used for the blow-up profile of \(u^{(4)}+|u|^{q-1}u=0\). The parameter range is \(q>1\), so \(x\mapsto |x|^{q-1}x\) is continuously differentiable and the variational equation is well defined. The periodic solution is assumed nonconstant and of least period \(T>0\). No existence assertion is made outside values of \(q\) for which such a periodic solution is already known or separately established.

The recent algebraic-dynamical correspondence of Matsue identifies the phase and scaling directions of periodic balance laws and, in the cubic suspension-bridge example, reports the stable exponents numerically as values extremely close to \(-7\) and \(-8\). The argument below adds an adjoint symmetry that forces the complete spectrum exactly and works for the full \(q>1\) auxiliary family whenever a periodic orbit exists.

## Proof
Write \(D=d/dt\), \(N(w)=|w|^{q-1}w\), and
\[
P_q(D)=(D-\eta)(D-\eta+1)(D-\eta+2)(D-\eta+3),
\qquad \eta=-\frac{4}{q-1}.
\]
The variational scalar operator along a periodic solution \(w\) is
\[
L_w=P_q(D)+q|w(t)|^{q-1}.
\]

First, two Floquet multipliers are explicit. Differentiating the nonlinear equation with respect to time gives \(L_w w'=0\), so the phase direction has multiplier \(1\). A second solution is
\[
v(t)=e^t\bigl(w'(t)-\eta w(t)\bigr).
\]
To check it directly, use
\[
P_q(D+1)(D-\eta)=P_q(D)(D-\eta+4).
\]
Then
\[
L_wv=e^t\left[P_q(D)(D-\eta+4)w+q|w|^{q-1}(D-\eta)w\right].
\]
The derivative of \(P_q(D)w+N(w)=0\) cancels the terms containing \(Dw\). What remains is
\[
-e^t\bigl(4+(q-1)\eta\bigr)N(w)=0,
\]
because \(\eta=-4/(q-1)\). Since \(w'-\eta w\) is periodic and cannot vanish identically for a nonconstant periodic \(w\), this solution has multiplier \(e^T\).

Now set
\[
\sigma=3-2\eta=\frac{3q+5}{q-1}>0.
\]
The four roots of \(P_q\) are symmetric under reflection across \(-\sigma/2\), hence
\[
P_q(z)=P_q(-\sigma-z).
\]
The formal adjoint therefore satisfies
\[
L_w^*=P_q(-D)+q|w|^{q-1}
      =P_q(D-\sigma)+q|w|^{q-1}
      =e^{\sigma t}L_we^{-\sigma t}.
\]
For a scalar periodic linear differential equation, the formal-adjoint monodromy has the reciprocal multiplier multiset: in first-order form the adjoint fundamental matrix is the inverse transpose of the original fundamental matrix. On the other hand, the displayed conjugacy sends a solution of \(L_wv=0\) with multiplier \(\mu\) to a solution of \(L_w^*u=0\) with multiplier \(e^{\sigma T}\mu\). Hence the multiplier multiset \(S\) of \(L_w\) obeys
\[
S=e^{-\sigma T}S^{-1}.
\]
Since \(1\) and \(e^T\) belong to \(S\), the reflected multipliers \(e^{-\sigma T}\) and \(e^{-(\sigma+1)T}\) also belong to \(S\). The equation is fourth order, so these are all four multipliers. They are pairwise distinct for \(q>1\), which also proves simplicity and hyperbolicity modulo the phase multiplier.

Finally,
\[
-(\sigma+1)=-\frac{4(q+1)}{q-1},
\qquad -\sigma=-\frac{3q+5}{q-1},
\]
which are precisely the two negative exponents proposed in the 2015 Conjecture 1. At \(q=3\), \(\sigma=7\), giving the exact spectrum \(0,1,-7,-8\).

## Verification
The proof is symbolic and does not depend on a finite numerical experiment. The key identities can be checked independently from the factorized polynomial \(P_q\): (i) shifting \(D\) by one yields the scaling-mode identity; (ii) reflecting \(D\) by \(-\sigma-D\) reverses the four factors; and (iii) the adjoint monodromy has reciprocal spectrum. All boundary conditions used are periodic Floquet boundary conditions over one least period \(T\).

For the cubic case \(q=3\), \(P_3(D)=(D+2)(D+3)(D+4)(D+5)\) reproduces the transformed suspension-bridge equation in Matsue's Section 5.3. The exact multipliers become \(1,e^T,e^{-7T},e^{-8T}\), matching the reported numerical values for the validated period near \(1.90809723205\).

## Relationship to prior work
Matsue, arXiv:2610.05354v1, Theorem 4.13 identifies two distinguished multipliers \(1\) and \(e^T\) for periodic balance laws. In Section 5.3 the paper revisits the cubic suspension-bridge profile and reports the remaining exponents numerically near \(-7\) and \(-8\), while emphasizing agreement with earlier computer-assisted work.

D'Ambrosio, Lessard, and Pugliese, DOI 10.1016/j.na.2014.12.026, rigorously validate a cubic periodic profile and its Floquet spectrum by computer-assisted estimates. Their Conjecture 1 proposes, for every \(q>1\), existence of a periodic solution together with the three nontrivial exponents
\[
-\frac{4(q+1)}{q-1},\qquad -\frac{3q+5}{q-1},\qquad 1.
\]
They state that the formulas outside the validated regime are supported numerically. The present argument separates the two issues: it does not settle existence, but it proves that whenever any nonconstant periodic solution exists, its entire Floquet spectrum is forced to have exactly the conjectured values.

Targeted literature searches using the exact source, the conjecture, adjoint/Floquet pairing, reciprocal multipliers, and the suspension-bridge exponent values did not locate a published statement deriving this conditional exact spectrum. The closest located records concern Floquet reductions for other dynamical systems and do not imply the fourth-order adjoint reflection used here.

## Limitations
The result is conditional on existence of a nonconstant periodic solution of \((W_q)\). It does not prove the existence or uniqueness portions of the 2015 conjectures, does not describe nonlinear basin boundaries, and does not claim that arbitrary lower-order perturbations preserve this exact spectrum. The adjoint reflection uses the special four consecutive factors in \(P_q\); a general fourth-order periodic equation need not have the same pairing.

## References
1. K. Matsue, “On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs,” arXiv:2610.05354v1, 2026. See Theorem 4.13 and Section 5.3.
2. L. D'Ambrosio, J.-P. Lessard, and A. Pugliese, “Blow-up profile for solutions of a fourth order nonlinear equation,” Nonlinear Analysis 121 (2015), 280–335. DOI: 10.1016/j.na.2014.12.026. See Theorem 4.17, Conjecture 1, and Remark 6.2.
