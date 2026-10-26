# Complete two-local symmetry census of the three-dimensional Heisenberg Lie algebra over finite fields

## Finding

Let \(F=\mathbb F_q\) be any finite field, with \(q\ge2\), and let \(H=V\oplus Fz\), \(V=F^2\), with bracket \([v+cz,w+dz]=\det(v,w)z\). A two-local derivation, respectively two-local automorphism, is an arbitrary map \(H\to H\) whose values at each *pair* of elements coincide with those of some genuine linear derivation, respectively Lie-algebra automorphism; the witness may depend on the pair. No linearity or additivity is assumed of the two-local map.

**Theorem (complete classification and enumeration).** Every two-local derivation is uniquely of the form
\[
\Delta(v+cz)=f(v)+g(v,c)z,
\]
where \(f:V\to V\) and \(g:H\to F\) are arbitrary degree-one homogeneous functions: \(f(av)=af(v)\) and \(g(av,ac)=a g(v,c)\) for every \(a\in F\). Conversely, every such pair defines a two-local derivation. In particular,
\[
\bigl|\operatorname{2LocDer}(H)\bigr|=q^{q^2+3q+3}.
\]

Every two-local automorphism is uniquely of the same displayed form, but with the following conditions: (i) \(f\) is homogeneous, nonzero away from zero, and its induced map of \(\mathbb P(V)\) is a permutation; (ii) \(g\) is homogeneous with \(g(0,c)=\tau c\) for some \(\tau\in F^\times\); and (iii) for each \(v\ne0\), the vertical section \(c\mapsto g(v,c)\) permutes \(F\). Conversely, these conditions suffice. The complete number is
\[
\bigl|\operatorname{2LocAut}(H)\bigr|=(q+1)!(q-1)^{q+2}(q!)^{q+1}.
\]
Every two-local automorphism so classified is bijective. The classification includes the prime field of characteristic two and all finite extension fields.

## Assumptions and scope

The Lie bracket is bilinear and alternating, also in characteristic two; the displayed determinant defines the standard three-dimensional Heisenberg Lie algebra in every characteristic. In all two-local definitions, the same genuine witness must interpolate both chosen elements. Homogeneous means homogeneous over the entire field \(F\), not merely over its prime subfield. Automorphisms are \(F\)-linear bracket-preserving bijections. Maps under classification need not be \(F\)-linear, additive, or continuous.

## Proof

**Ordinary witnesses.** Write the projection to \(V\) as \(\pi\). Every derivation and automorphism preserves the derived ideal \(Fz\). Every derivation has the unique form
\[
 D(v+cz)=Av+\bigl(\ell(v)+c\operatorname{tr}A\bigr)z,
 \quad A\in M_2(F),\quad \ell\in V^*;
\]
every automorphism has the unique form
\[
 T(v+cz)=Av+\bigl(\ell(v)+c\det A\bigr)z,
 \quad A\in\operatorname{GL}_2(F),\quad\ell\in V^*.
\]
Indeed, apply the defining identity to \([e_1,e_2]=z\); the induced coefficient of \(z\) is respectively \(\operatorname{tr}A\) or \(\det A\). Conversely the formulas satisfy the derivation or bracket-preservation identities; invertibility in the second case is equivalent to \(A\) being invertible.

**Necessity.** For a two-local map \(\Psi\), each value on \(Fz\) is central, and homogeneity follows by interpolating the pair \(x,ax\). For fixed \(v\), interpolating \(v+cz,v+dz\) with a linear witness shows that the quotient \(\pi\Psi(v+cz)\) is independent of \(c\), hence equals a homogeneous map \(f(v)\). Its remaining coefficient \(g(v,c)\) is homogeneous as a function on \(H\). These are exactly the conditions stated for derivations.

For a two-local automorphism, invertibility of every witness forces \(f(v)\ne0\) for \(v\ne0\). Interpolating two elements with linearly independent quotient vectors forces their \(f\)-images to be independent. Hence the induced projective map is injective and therefore a permutation of the finite projective line, which has \(q+1\) points. Any automorphism acts on \(z\) by a nonzero scalar, so homogeneity gives \(g(0,c)=\tau c\), \(\tau\ne0\). Interpolating \(v+cz,v+dz\) for \(c\ne d\), their difference is a nonzero central vector and remains nonzero under the common automorphism witness, so \(g(v,c)\ne g(v,d)\). Thus each vertical section permutes \(F\).

**Sufficiency for both kinds.** Fix arbitrary \(x=v+cz\) and \(y=w+dz\). If the quotient vectors \(v,w\) are independent, select the unique linear operator \(A\) with \(Av=f(v)\), \(Aw=f(w)\). In the automorphism case, the projective condition ensures \(\det A\ne0\). Set \(\kappa=\operatorname{tr}A\) for derivations, or \(\kappa=\det A\) for automorphisms. There is a unique \(\ell\in V^*\) with
\[
\ell(v)=g(v,c)-\kappa c,\qquad \ell(w)=g(w,d)-\kappa d.
\]
The resulting witness interpolates both \(x,y\).

If \(v,w\) are dependent but \(x,y\) are independent, exchange the pair if necessary and write \(w=t v\) with \(v\ne0\) and \(d-tc\ne0\). Put
\[
\kappa=\frac{g(t v,d)-t g(v,c)}{d-tc},\qquad L=g(v,c)-\kappa c.
\]
A linear \(A\) with \(Av=f(v)\) and prescribed trace \(\kappa\) always exists, and \(\ell\) may be chosen with \(\ell(v)=L\). For automorphisms, \(f(v)\ne0\) and the same construction has \(\kappa\ne0\): when \(t=0\), homogeneity and the central condition give \(\kappa=\tau\ne0\); when \(t\ne0\), homogeneity gives \(g(tv,d)=t g(v,d/t)\), so vertical injectivity and \(d/t\ne c\) give a nonzero numerator. For every nonzero \(\kappa\), an invertible \(A\) satisfying \(Av=f(v)\) and \(\det A=\kappa\) exists. Again the witness interpolates both vectors. Finally, if \(x,y\) are dependent, the required witness exists already at one of the nonzero vectors by the same prescribed-trace/determinant construction, and homogeneity handles the other. This proves both classifications.

**Enumeration.** A homogeneous map \(F^d\to F^a\) is freely determined by its values on one representative of each of the \((q^d-1)/(q-1)\) projective points. Thus the two independent homogeneous maps in a two-local derivation admit respectively \(q^{2(q+1)}\) and \(q^{q^2+q+1}\) choices, yielding the first formula. In the automorphism case, \(f\) is specified by a permutation of \(q+1\) projective points and one nonzero scalar on each: \((q+1)!(q-1)^{q+1}\) choices. For \(g\), a nonzero central multiplier has \(q-1\) choices, and each of \(q+1\) projective quotient fibres has an arbitrary permutation of \(q\) values: \((q!)^{q+1}\) choices. These choices are independent, giving the second formula. Because the quotient projective map and each vertical section are bijective, the complete two-local automorphism is a bijection on \(H\).

## Verification

The standalone `verify.py` constructs every ordinary derivation and automorphism witness over \(\mathbb F_2\) and compares both target outputs at every pair of algebra elements. It checks **all** \(8192\) maps in the classified two-local derivation family and all \(48\) in the classified two-local automorphism family. It finds respectively \(128\) and \(24\) additive maps, with \(64\) ordinary derivations and \(24\) ordinary automorphisms. Over \(\mathbb F_3\), it checks all pairs for \(150\) reproducibly sampled maps in each classified family against all ordinary witnesses. The final execution prints `VERIFY_OK`. These finite computations support, but do not replace, the field-uniform proof.

## Relationship to prior work

Ayupov–Kudaybergenov–Rakhimov established the existence of nonderivation two-local derivations in nilpotent Lie algebras (2015). Ayupov–Kudaybergenov (arXiv:1602.05187v1, Section 3) constructed nonordinary two-local automorphisms on nilpotent Lie algebras using homogeneous central functions. Ayupov–Kudaybergenov–Omirov (arXiv:1703.10506v1, Sections 3.2 and 6.2) developed related constructions for nilpotent Leibniz algebras; those general existence constructions are not being claimed as new. Sheng–Liu–Miao, DOI 10.1007/s11464-023-0061-6, treat local and **linear** two-local automorphisms of Heisenberg Lie (super)algebras. The scope here is the complete, arbitrary-map finite-field classification and exact size of both nonadditive two-local symmetry sets, including projective permutations and vertical fibre permutations. The \(F\)-linear subcases are not asserted as new.

## Limitations

No assertion of publication-priority uniqueness is made. The accessible 2015 derivation paper was assessed through its published descriptions, not a complete verified full-text comparison, and the complete 2025 Heisenberg linear-automorphism paper was not accessible for inspection beyond its public abstract. No claim is made that a finite-field count implies a classification for infinite fields. Computation checks only the prime fields of orders \(2\) and \(3\); the general theorem is mathematical rather than computational.

## References

1. Sh. A. Ayupov, K. K. Kudaybergenov, I. S. Rakhimov, “2-Local derivations on finite-dimensional Lie algebras,” *Linear Algebra and its Applications* 474 (2015), 1–11. DOI 10.1016/j.laa.2015.01.016.
2. Sh. A. Ayupov, K. K. Kudaybergenov, “2-local automorphisms on finite-dimensional Lie algebras,” arXiv:1602.05187v1 (2016), Section 3. https://arxiv.org/abs/1602.05187
3. Sh. A. Ayupov, K. K. Kudaybergenov, B. A. Omirov, “Local and 2-local derivations and automorphisms on simple Leibniz algebras,” arXiv:1703.10506v1, first public 2017-03-30; Sections 3.2 and 6.2. https://arxiv.org/abs/1703.10506
4. Y. Sheng, W. Liu, X. Miao, “Local and Linear 2-local Automorphisms of Heisenberg Lie (Super)algebras,” *Frontiers of Mathematics*, online 2025-03-28. DOI 10.1007/s11464-023-0061-6.
