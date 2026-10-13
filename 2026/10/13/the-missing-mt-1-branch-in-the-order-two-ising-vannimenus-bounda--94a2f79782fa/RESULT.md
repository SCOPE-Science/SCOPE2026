# The missing \(mt=1\) branch in the order-two Ising–Vannimenus boundary-law system

## Finding

Consider the order-two translation-invariant boundary-law system (4.2) of Mukhamedov–Akın–Khakimov. Set the source parameter \(b=1\) and write \(A=\widetilde a=\sqrt a>0\). Then all positive solutions are completely classified.

For every \(a>0\), there is the diagonal solution
\[
(x_1,x_2,x_3)=(A,A,A).
\]
If and only if \(a>3\), there are exactly two additional positive solutions
\[
(x_1,x_2,x_3)=\left(A,Am_\pm,\frac{A}{m_\pm}\right),
\qquad
m_\pm=\frac{a-1\pm\sqrt{(a-3)(a+1)}}{2},
\]
with \(m_+m_-=1\). Hence the complete positive-solution count is one for \(0<a\le3\) and three for \(a>3\).

In the notation of the source subsection, \(x_2=mx_1\) and \(x_3=tx_1\), both non-diagonal solutions satisfy \(t=m^{-1}\). Thus \(mt=1\) although \(m\ne1\) and \(t\ne1\). This directly contradicts the printed assertion that \(mt=1\) occurs if and only if \(m=t=1\), and shows that the ensuing restriction \(mt\ne1\) deletes an entire positive branch.

A concrete exact instance is \(a=7/2\). Then \(m=2\) and \(t=1/2\) give a non-diagonal solution, as does the reciprocal choice \(m=1/2\), \(t=2\).

## Assumptions and scope

The result concerns positive translation-invariant solutions of the source's system (4.2) with tree order \(k=2\) and \(b=1\). The source defines its exponential interaction parameters so that \(b=1\) is the zero prolonged-coupling boundary. All variables are strictly positive.

The result is an exact correction of the source-coordinate classification on this boundary. It does not claim that the low-temperature phase transition of the ordinary nearest-neighbor Ising model on an order-two Cayley tree is new; that physical transition is classical. It does not classify the full two-parameter Ising–Vannimenus system for \(b\ne1\), periodic boundary laws, or non-translation-invariant Gibbs measures.

## Proof

At \(b=1\), the first equation of (4.2) reduces identically to
\[
x_1=A.
\]
Multiplying the second and third equations then cancels every rational factor and gives
\[
x_2x_3=A^2.
\]
Therefore every positive solution can be written uniquely as
\[
x_2=Am,\qquad x_3=\frac{A}{m},\qquad m>0.
\]
Substitution into the second equation gives
\[
m=\frac{am^2+1}{a+m^2},
\]
where \(a=A^2\). Clearing the positive denominator yields the exact factorization
\[
(m-1)\bigl(m^2+(1-a)m+1\bigr)=0.
\]
Conversely, any positive \(m\) satisfying this factorization, together with \(x_1=A\) and \(x_3=A/m\), satisfies both remaining equations. Indeed, after the first equation is imposed the product of the right-hand sides of the second and third equations is exactly \(A^2\), matching \(x_2x_3\).

The factor \(m-1\) gives the diagonal solution. The quadratic factor has discriminant
\[
(a-1)^2-4=(a-3)(a+1).
\]
Because \(a>0\), it has two distinct positive roots exactly when \(a>3\), a repeated root \(m=1\) at \(a=3\), and no real non-diagonal root for \(0<a<3\). For \(a>3\), the two roots are
\[
m_\pm=\frac{a-1\pm\sqrt{(a-3)(a+1)}}{2},
\]
and their product is one. This proves both completeness and the solution count.

Finally, the source's variables in Section 4.2 satisfy \(m=x_2/x_1\) and \(t=x_3/x_1\). Hence the non-diagonal solutions above have \(t=1/m\), so \(mt=1\) with \(m,t\ne1\). The printed implication therefore fails.

## Verification

The bundled script `artifacts/verify.py` symbolically replays the factorization, the quadratic discriminant, the reciprocal-root identity, and the exact \(a=7/2\) counterexample. It also substitutes the parametric roots back into the source equations after \(b=1\).

The symbolic replay is a transcription check. Completeness for all positive parameters follows from the algebraic proof above, not from finite experimentation.

## Relationship to prior work

The 2017 primary paper explicitly says that Section 4.1 aims to study all solutions of its translation-invariant system, asks whether solutions exist outside the diagonal set, and in Section 4.2 asserts that \(mt=1\) is equivalent to \(m=t=1\) before imposing \(mt\ne1\). The present calculation identifies the missed case exactly.

The 2015 two-author predecessor with the same title was inspected because it predates the eligible source. Its phase-transition section works with a scalar restricted boundary field; it does not contain the 2017 three-coordinate system (4.2), the \(x_2=mx_1\), \(x_3=tx_1\) reduction, or the \(mt=1\) assertion. Thus it does not contain this correction.

Akın's earlier 2017 arbitrary-order memory-two paper uses a different four-variable recurrence and then analyzes a selected invariant set. It does not state the three-coordinate correction above, and it explicitly notes that exact description of its full recurrence systems is difficult. The classical nearest-neighbor Ising literature does cover the existence of one versus three translation-invariant phases at the corresponding threshold; that broader physical fact is treated here as prior knowledge rather than as the novelty claim.

Targeted searches using the source identifier, the literal \(mt=1\) assertion, the \(b=1\) specialization, reciprocal-branch language, and the equivalent \(m+m^{-1}+1=a\) relation located no published correction of the source-coordinate statement. A weakly indexed correction under different variables remains possible.

## Limitations

The finding is confined to the natural boundary \(b=1\). It does not repair the remainder of Section 4.2 for \(b\ne1\), reassess the paper's free-energy formulas, or classify all Gibbs measures of the model. The correspondence with the classical nearest-neighbor Ising transition provides a consistency check but is not presented as a new phase-transition theorem.

The originality claim is correspondingly narrow: the exact complete solution set of the 2017 source system on \(b=1\), and the identification of the false \(mt=1\) exclusion. Equivalent calculations could exist in weakly indexed literature under another boundary-law parametrization.

## References

1. F. Mukhamedov, H. Akın, O. Khakimov, “Gibbs measures and free energies of Ising-Vannimenus Model on the Cayley tree,” arXiv:1704.01933v1; DOI:10.1088/1742-5468/aa6c88.
2. F. Mukhamedov, H. Akın, “Gibbs measures and free energies of the Ising-Vannimenus Model on the Cayley tree,” arXiv:1504.00755v1.
3. H. Akın, “Gibbs Measures with memory of length 2 on an arbitrary order Cayley tree,” arXiv:1701.00715v1; DOI:10.1142/S012918311850016X.
4. U. A. Rozikov, *Gibbs Measures on Cayley Trees*, World Scientific, 2013.
