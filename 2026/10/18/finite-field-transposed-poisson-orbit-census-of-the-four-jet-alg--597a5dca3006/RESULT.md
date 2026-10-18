# Finite-field transposed Poisson orbit census of the four-jet algebra

## Finding
Let \(q\) be an odd prime power and \(A=\mathbb F_q[t]/(t^4)\), with its fixed usual unital commutative associative product. A transposed Poisson bracket means an alternating Lie bracket \([\cdot,\cdot]\) satisfying
\[
2z[x,y]=[zx,y]+[x,zy]\qquad(x,y,z\in A).
\]
There are exactly \(q^3\) such brackets on the specified underlying associative algebra, in exactly **\(2q+2\) isomorphism classes** under multiplication-preserving linear isomorphisms. Every bracket is represented uniquely by
\[
[x,y]_f=xf(t)\frac{dy}{dt}-yf(t)\frac{dx}{dt},\qquad f(t)=at+bt^2+ct^3.
\]
Choose any nonsquare \(\nu\in\mathbb F_q^\times\). A complete, irredundant list of representatives, their orbit cardinalities in the set of \(q^3\) brackets, and their automorphism-group orders is:

| Representative \(f\) | Number of distinct orbits | Size of each orbit | Automorphism group order |
| --- | ---: | ---: | ---: |
| \(0\) | \(1\) | \(1\) | \((q-1)q^2\) |
| \(at\), for each \(a\in\mathbb F_q^\times\) | \(q-1\) | \(q^2\) | \(q-1\) |
| \(t^2+rt^3\), for each \(r\in\mathbb F_q\) | \(q\) | \(q-1\) | \(q^2\) |
| \(t^3\) and \(\nu t^3\) | \(2\) | \((q-1)/2\) | \(2q^2\) |

In particular, the cubic-leading locus splits into square and nonsquare classes, a distinction invisible over algebraically closed fields. The orbit mass identity is
\[
1+(q-1)q^2+q(q-1)+(q-1)=q^3.
\]

## Assumptions and scope
The field has odd characteristic, including characteristic three; neither algebraic closure nor a prime (as opposed to prime-power) field is assumed. The associative multiplication is held fixed, and two brackets are considered equivalent precisely if a \(\mathbb F_q\)-linear bijection preserves both that multiplication and the brackets. The formal derivative on \(A\) is used only in the combination \(f(t)d/dt\) with \(f\in tA\), which descends to the quotient because \(t^4=0\).

## Proof
**Derivation reduction.** For a bracket obeying the displayed compatibility identity, define \(D(y)=[1,y]\). Setting the first bracket argument to \(1\) yields
\[
[x,y]=2xD(y)-D(xy).
\]
Skew-symmetry then gives \(2D(xy)=2xD(y)+2yD(x)\). Since \(2\) is invertible, \(D\) is a derivation and \([x,y]=xD(y)-yD(x)\). Conversely, for every derivation \(D\) of a commutative associative algebra, direct expansion and cancellation with the Leibniz rule verify the Jacobi identity and the transposed Poisson identity. The associated identity \([xD,yD]=[x,y]_fD\) gives a complementary check. Taking \(x=1\) recovers \(D\), establishing uniqueness.

**All derivations.** A derivation is determined by \(f=D(t)\). The relation \(t^4=0\) requires \(0=D(t^4)=4t^3f\). Because the characteristic is odd, \(4\) is nonzero, so the constant coefficient of \(f\) vanishes. Conversely every \(f=at+bt^2+ct^3\) defines a derivation. There are exactly \(q^3\) such \(f\).

**Algebra automorphisms and their action.** Each automorphism is uniquely a substitution
\[
\phi(t)=ut+vt^2+wt^3,\quad u\in\mathbb F_q^\times,\quad v,w\in\mathbb F_q,
\]
so the automorphism group has order \((q-1)q^2\). Under \(D\mapsto\phi D\phi^{-1}\), the new coefficient is \(f(\phi(t))/\phi'(t)\), and direct truncation gives
\[
(a,b,c)\longmapsto\left(a,\;ub-\frac{av}{u},\;u^2c+2a\left(\frac{v^2}{u^2}-\frac wu\right)\right).
\]
For \(a\ne0\), choose \(v,w\) to remove \(b,c\), while \(a\) is invariant: one orbit for every nonzero \(a\), each containing all \(q^2\) pairs \((b,c)\). When \(a=0,b\ne0\), the action becomes \((b,c)\mapsto(ub,u^2c)\), and \(r=c/b^2\) is a complete invariant: one orbit of \(q-1\) brackets for each \(r\in\mathbb F_q\). When \(a=b=0,c\ne0\), the action is \(c\mapsto u^2c\), giving exactly the two square classes, each of size \((q-1)/2\). The zero derivation is fixed. Orbit-stabilizer gives the listed automorphism orders. The cases exhaust the entire derivation space and are mutually inequivalent, proving the classification.

## Verification
The supplied standalone `verify.py` independently computes substitution and inverse substitutions in the truncated ring, compares direct conjugation with the displayed action, checks the claimed orbit partitions exhaustively, and tests the Lie and transposed Poisson identities on a basis. For \(q=3,5,7\) it respectively obtains \(8,12,16\) classes of the predicted sizes. For \(q=3\) and \(q=5\) it checks the identities for every derivation; for \(q=7\) it checks specified sample derivations. Run `python3 verify.py` using Python 3.8 or newer. These finite checks corroborate rather than replace the proof for arbitrary odd prime powers.

## Relationship to prior work
Bai, Bai, Guo and Wu introduced transposed Poisson algebras and the standard derivation construction in 2020; the unital derivation correspondence is also established in the subsequent literature. **Those general principles are prior work, not the claimed contribution.** Beites, Fernández Ouaridi and Kaygorodov classify three-dimensional complex transposed Poisson algebras. Zhang, Hao, Sun and Chen give a comprehensive classification in dimension four **over the complex numbers**. Their field hypothesis does not determine the finite-field square-class split, orbit sizes or stabilizer counts in this fixed multiplication type. The present contribution is the explicit finite odd-field classification and enumeration on the length-four local algebra. General one-variable vector-field normal-form theory provides an additional conceptual overlap risk and is not represented as disproved.

## Limitations
This classification does not include characteristic two, higher truncation lengths, arbitrary associative multiplications, or all four-dimensional transposed Poisson algebras. It does not establish historical uniqueness against all possible older formal-vector-field orbit literature. The published general derivation theorem and any characteristic-zero versions of individual normal forms are explicitly excluded from the novelty claim.

## References
- C. Bai, R. Bai, L. Guo, and Y. Wu, *Transposed Poisson algebras, Novikov-Poisson algebras and 3-Lie algebras*, arXiv:2005.01110 (first publicly submitted 2020-05-03), https://arxiv.org/abs/2005.01110.
- P. D. Beites, A. Fernández Ouaridi, and I. Kaygorodov, *The algebraic and geometric classification of transposed Poisson algebras*, RACSAM (2023), DOI:10.1007/s13398-022-01385-4.
- P. D. Beites, B. C. Ferreira, and I. Kaygorodov, *Transposed Poisson algebras: a survey*, arXiv:2207.00281 (2022), https://arxiv.org/abs/2207.00281.
- Z. Zhang, Z. Hao, Y. Sun, and L. Chen, *The classification of 4-dimensional transposed Poisson algebras*, RACSAM 120 (2026), DOI:10.1007/s13398-026-01921-6.
