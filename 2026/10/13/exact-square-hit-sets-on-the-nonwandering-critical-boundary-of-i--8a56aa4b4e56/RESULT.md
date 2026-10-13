# Exact square-hit sets on the nonwandering critical boundary of integral quadratics

## Finding
Let \(f(X)=aX^2+bX+c\in\mathbb Z[X]\) with \(a\ne0\), and let its critical point be \(\gamma=-b/(2a)\). Define
\[
\kappa=4ac-b^2+2b
\]
and
\[
S_f=\{k\ge1:f^{(k)}(\gamma)\in\mathbb Q^2\},\qquad \mathbb Q^2=\{y^2:y\in\mathbb Q\}.
\]
On the complete nonwandering boundary \(\kappa\in\{0,-4,-8\}\), the set \(S_f\) is determined exactly by the coefficients:

- If \(\kappa=0\), then \(f^{(k)}(\gamma)=-b/(2a)\) for every \(k\ge1\). Hence \(S_f\) is all positive integers iff \(-b/(2a)\in\mathbb Q^2\), and otherwise \(S_f=\varnothing\).
- If \(\kappa=-4\), then
\[
f^{(k)}(\gamma)=\begin{cases}
-(b+2)/(2a),&k\text{ odd},\\
-b/(2a),&k\text{ even}.
\end{cases}
\]
Thus \(S_f\) is the union of the odd positive integers iff \(-(b+2)/(2a)\in\mathbb Q^2\) and the even positive integers iff \(-b/(2a)\in\mathbb Q^2\).
- If \(\kappa=-8\), then
\[
f(\gamma)=-(b+4)/(2a),\qquad f^{(k)}(\gamma)=(4-b)/(2a)\quad(k\ge2).
\]
Thus \(1\in S_f\) iff \(-(b+4)/(2a)\in\mathbb Q^2\), while either every \(k\ge2\) belongs to \(S_f\) or none does, according as \((4-b)/(2a)\) is or is not a rational square.

In particular, \(S_f\) is infinite exactly in the following cases: \(\kappa=0\) and \(-b/(2a)\in\mathbb Q^2\); \(\kappa=-4\) and at least one of \(-b/(2a)\), \(-(b+2)/(2a)\) is in \(\mathbb Q^2\); or \(\kappa=-8\) and \((4-b)/(2a)\in\mathbb Q^2\).

If \(f\) is irreducible over \(\mathbb Q\), this specializes to an exact pattern list:
\[
\begin{array}{c|c}
\kappa&\text{possible }S_f\\ \hline
0&\varnothing\text{ or }\mathbb Z_{\ge1},\\
-4&\varnothing,\ \{k\ge1:k\text{ odd}\},\ \text{or }\{k\ge1:k\text{ even}\},\\
-8&\varnothing,\ \{1\},\ \text{or }\{k\ge2\}.
\end{array}
\]
In particular, only the \(\kappa=0\) class can have every critical iterate square while remaining irreducible.

## Assumptions and scope
The coefficients \(a,b,c\) are arbitrary integers with \(a\ne0\). Rational squares include \(0\). No irreducibility assumption is needed for the classification. The result concerns the critical orbit only, and only the three values of \(\kappa\) for which the critical point is nonwandering.

For irreducible quadratics, these are exactly the cases excluded from the wandering-critical-point hypothesis in the recent square-occurrence theorem of Ostafe and Tran. Their notation is \(c(f)=4ac-b^2+2b\); here \(\kappa=c(f)\).

## Proof
Set
\[
\phi(X)=aX+\frac b2.
\]
A direct calculation gives
\[
g=\phi\circ f\circ\phi^{-1},\qquad g(X)=X^2+\frac\kappa4,
\]
and \(\phi(\gamma)=0\). Therefore, if \(z_k=g^{(k)}(0)\), then
\[
f^{(k)}(\gamma)=\phi^{-1}(z_k)=\frac{2z_k-b}{2a}.
\]
It remains only to evaluate the three complete preperiodic critical orbits.

For \(\kappa=0\), one has \(g(X)=X^2\) and \(z_k=0\) for every \(k\ge1\), yielding \(f^{(k)}(\gamma)=-b/(2a)\).

For \(\kappa=-4\), one has \(g(X)=X^2-1\), so
\[
0\mapsto -1\mapsto0\mapsto-1\mapsto0\mapsto\cdots.
\]
Thus \(z_k=-1\) for odd \(k\) and \(z_k=0\) for even \(k\). Substitution in \((2z_k-b)/(2a)\) gives the two displayed values and hence the parity classification of \(S_f\).

For \(\kappa=-8\), one has \(g(X)=X^2-2\), so
\[
0\mapsto-2\mapsto2\mapsto2\mapsto\cdots.
\]
Thus \(z_1=-2\) and \(z_k=2\) for every \(k\ge2\). Substitution gives the stated first and tail values. The criterion for infinitely many square hits follows immediately in each case.

It remains to prune the patterns under irreducibility. The discriminant is
\[
\Delta=b^2-4ac=2b-\kappa.
\]
For \(\kappa=-4\), if both parity values are rational squares, then their product shows that \(b(b+2)\) is an integer square, say \(w^2\). Hence
\[
(b+1)^2-w^2=1,
\]
so integer factorization forces \(b\in\{0,-2\}\). Then \(\Delta=2b+4\in\{4,0\}\), a square, contradicting irreducibility. Thus an irreducible polynomial can have at most one square parity class.

For \(\kappa=-8\), if both the first value and the constant tail value are rational squares, their product shows that \(b^2-16=w^2\) for an integer \(w\). From \((b-w)(b+w)=16\), the same-parity divisor pairs give \(b\in\{-5,-4,4,5\}\). The boundary equation is \(4ac=b^2-2b-8\); for \(b=5\) or \(b=-5\) its right side is respectively \(7\) or \(27\), impossible for integral \(a,c\). For \(b=4\) or \(b=-4\), the discriminant \(\Delta=2b+8\) is respectively \(16\) or \(0\), again a square. Hence irreducibility forbids simultaneous first and tail square hits. The displayed pattern list follows.

## Verification
The proof is symbolic and covers every admissible coefficient triple. The accompanying `verify_boundary.py` independently replays the formulas using exact `fractions.Fraction` arithmetic. It enumerates integral coefficient triples satisfying each of \(\kappa=0,-4,-8\), computes the critical orbit directly through ten iterates, compares each value with the closed formula, and independently checks the rational-square membership rule.

The finite replay is not used as an infinite proof; it is a check on the algebra and implementation of the three symbolic cases.

## Relationship to prior work
Ostafe and Tran define \(c(f)=4ac-b^2+2b\), prove that the critical point is wandering iff \(c(f)\notin\{0,-4,-8\}\), and conjugate the three exceptions to \(X^2\), \(X^2-1\), and \(X^2-2\). Their Theorem 1.3 bounds square occurrences when the critical point is wandering. Their Remark 1.4 gives one irreducible example with a square at every critical iterate, while Remark 3.1 records selected constant auxiliary values showing that the wandering hypothesis is necessary. The present result instead determines the entire square-index set for every integral quadratic on all three excluded boundary classes, then proves that irreducibility eliminates the simultaneous-parity case for \(c(f)=-4\) and the simultaneous-first-and-tail case for \(c(f)=-8\).

Cahn, Jones, and Spear study rational maps whose orbits contain infinitely many distinct powers and obtain arithmetic-progression structure for certain power-index sets. That broader framework is compatible with the periodic index sets above, but it does not itself give these coefficient-wise critical-orbit formulas on the finite/preperiodic boundary.

## Limitations
This result does not improve the quantitative bound in the wandering case, classify square hits away from the critical point, or address higher-degree maps. The originality comparison is bounded by the literature searches and source inspections recorded in the accompanying review; an elementary equivalent formulation could exist elsewhere under different notation.

The lead source is classified primarily as number theory on its first public version. A more specific MSC2020 subdivision is not asserted here.

## References
1. A. Ostafe and D. T. Tran, *Powers in orbits and semigroups generated by polynomials*, arXiv:2610.00893v1, 1 October 2026. Relevant items: equation (1.3), Theorem 1.3, Remark 1.4, Lemma 2.11, and Remark 3.1.
2. J. Cahn, R. Jones, and J. Spear, *Powers in Orbits of Rational Functions: Cases of an Arithmetic Dynamical Mordell–Lang Conjecture*, Canadian Journal of Mathematics 71 (2019), 773–817, DOI 10.4153/CJM-2018-026-x.
