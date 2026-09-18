# Same-model review

## Result reviewed

**Finite-field enumeration and automorphism orders for Dedekind Poisson algebras**

The reviewed claims are:

1. over \(\mathbb F_q\), the active dimension in the Plakosh--Pypka Type II classification is at most one for even \(q\) and at most two for odd \(q\);
2. in odd characteristic, the mixed two-dimensional active pairs are classified by the exact nonsquare invariant \(\kappa=-\det(\omega)/\det(\beta)\);
3. the resulting all-dimension class counts are \(2,3,4,4,\ldots\) for even \(q\) and \(2,3,(q+9)/2,q+5,q+5,\ldots\) for odd \(q\);
4. the automorphism-group orders stated in RESULT.md follow from the characteristic filtration \(Fc=P^2\subset Z\oplus Fc=\operatorname{Ann}(P(+ ,\cdot))\) and the active similitude groups.

## Correctness review

### Active-dimension bounds

In characteristic two, the diagonal quadratic map of a symmetric bilinear form has the shape
\[
\beta(v,v)=\sum_i b_{ii}v_i^2.
\]
Because a finite field of characteristic two is perfect, this is the square of a linear functional. In dimension at least two the functional has a nonzero kernel, contradicting the required anisotropy. Hence \(d=1\).

For odd \(q\), if \(d\ge3\), Chevalley--Warning applies to the single homogeneous quadratic polynomial \(\beta(v,v)\): its degree is smaller than the number of variables, so its number of zeros is divisible by the characteristic. Since zero is one solution, there must be a nonzero solution. Hence an anisotropic quadratic form over \(\mathbb F_q\) has dimension at most two.

### Two-dimensional mixed invariant

With \(T\) defined by \(\omega(u,v)=\beta(u,Tv)\), alternation makes \(T\) \(\beta\)-skew-adjoint. In dimension two, \(\operatorname{tr}T=0\), and if \(\omega\ne0\), then \(T\) is invertible. Cayley--Hamilton gives
\[
T^2=\kappa I,\qquad \kappa=-\det T=-\det(\omega)/\det(\beta).
\]
The determinant of a nonzero alternating binary form is a square. A binary symmetric form is anisotropic exactly when \(-\det\beta\) is nonsquare. Therefore \(\kappa\) is nonsquare.

Under simultaneous similarity by \(\phi\) with common multiplier \(\lambda\), the operator \(T\) is conjugated, so \(\kappa\) is invariant. Conversely, for any nonsquare \(\kappa\), the displayed normal form has \(T^2=\kappa I\); the skew-adjoint relation determines \(\beta\) up to the common scalar. Hence distinct nonsquares give distinct classes and all mixed classes occur. The count is \((q-1)/2\).

### Enumeration

The source isomorphism criterion separates the presence of the idempotent summand, the dimension of the zero summand, and the active-pair class. The dimension equation is
\[
n=\epsilon+z+d+1.
\]
Counting the allowed \((\epsilon,z,d)\) and the active-pair classes gives the formulas in RESULT.md. Boundary cases \(n=1,2,3\) were checked separately; in particular the two-dimensional Type II class first appears at \(n=2\), and the two-dimensional active sector first appears at \(n=3\).

### Automorphism groups

For Type II, \(P^2=Fc\) and \(\operatorname{Ann}(P(+ ,\cdot))=Z\oplus Fc\), so both subspaces are characteristic. The unique nonzero idempotent, when present, is fixed. This forces the triangular automorphism form written in RESULT.md. The free shear parameters contribute
\[
q^{dz+d+z},
\]
and \(\operatorname{GL}(Z)\) contributes \(G_z(q)\).

For \(d=1\), the active similitude group has order \(q-1\). For a pure anisotropic plane it is \(GO^-(2,q)\), of order \(2(q^2-1)\). In the mixed case, simultaneous similitude of \(\beta\) and \(\omega\) forces commutation with \(T\). Since \(X^2-\kappa\) is irreducible, \(\mathbb F_q[T]\cong\mathbb F_{q^2}\), and the nonzero centralizer elements are exactly the simultaneous similitudes. This gives order \(q^2-1\). Substitution yields the three displayed automorphism formulas.

Finite checks for odd prime fields \(q=3,5,7\) agree with the orbit and stabilizer formulas: the pure binary sector has one orbit with stabilizer orders \(16,48,96\), while the mixed sector has \(1,2,3\) orbits with stabilizer orders \(8,24,48\), respectively. These checks support but are not used in the proof.

### Adversarial checks

- The mixed invariant is the exact scalar \(\kappa\), not merely its square class; the common scaling in the source isomorphism relation cancels from \(-\det\omega/\det\beta\).
- The two-dimensional zero-bracket sector is a single similarity class because all anisotropic binary symmetric forms over a finite odd field have the same determinant square class.
- No mixed class exists in even characteristic over a finite field because the active dimension is at most one.
- The idempotent summand does not change the automorphism order: the nonzero idempotent is unique and hence fixed.
- The central annihilator shears are included; omitting them would undercount automorphisms by \(q^{dz+d+z}\).
- The general classification of pairs of bilinear forms is not being claimed as new.

**Correctness: PASS.**

## Originality review

The primary source arXiv:2609.13767v1 was inspected for its structural classification, isomorphism relation, finite-field consequences, and examples. It supplies the arbitrary-field Type I/Type II theorem and simultaneous-similarity criterion, but does not give a finite-field all-dimension enumeration or the automorphism-group table recorded here.

The contemporaneous arXiv:2609.13784v1 classifies Poisson algebras in dimensions at most three and overlaps with the low-dimensional normal-form phenomena. Accordingly, no novelty is claimed for three-dimensional Poisson normal forms by themselves.

General pair-of-bilinear-forms classification is classical and is known to be wild in broader settings. The present originality claim is restricted to the finite-field Dedekind specialization: the explicit orbit collapse, the stable class counts, the exact mixed-class count in all dimensions, and the automorphism-order formulas.

Targeted searches for Dedekind Poisson automorphism groups, finite-field isomorphism counts, enumeration formulas, and equivalent formulations did not reveal these formulas. The primary and low-dimensional source papers are very recent, so later revisions or concurrent independent derivations remain a material originality risk.

**Originality: PASS, to the best of our knowledge.**

## Value review

The result converts a structural arbitrary-field classification into a fully explicit finite-field moduli count. The stabilization
\[
N_q(n)=q+5\quad(q\text{ odd},\ n\ge4)
\]
and \(N_q(n)=4\) for even \(q\) and \(n\ge3\) are concise global consequences not visible from the raw simultaneous-form statement. The automorphism formulas further quantify each class and distinguish the pure and mixed binary sectors by a factor of two in their active similitude groups.

**Value: PASS.**

## Scientific limitations

- The result concerns finite coefficient fields and finite-dimensional algebras.
- The arbitrary-field structural theorem and its isomorphism criterion are prior work and are essential inputs.
- Low-dimensional Poisson normal forms overlap with contemporaneous prior work and are excluded from the novelty claim.
- The source papers are recent preprints and may be revised.
- Originality is to the best of our knowledge; no independent validation is asserted.

Same-model review: passed. Cross-model review: not yet performed.
