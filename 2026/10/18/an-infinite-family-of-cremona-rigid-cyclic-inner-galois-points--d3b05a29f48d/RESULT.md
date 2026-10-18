# An infinite family of Cremona-rigid cyclic inner Galois points

## Finding
For each integer \(n\geq 9\) with \(n\equiv1\pmod4\), let \(C_n\subset\mathbb P^2_{\mathbb C}\) be the image of the morphism
\[
\nu_n:\mathbb P^1\longrightarrow\mathbb P^2,\qquad
[u:v]\longmapsto [u(v^{n+1}-u^{n+1}):u^n(u^2+v^2):v^n(u^2+v^2)].
\]
Then \(C_n\) is an irreducible rational curve of degree \(n+2\), normalized by \(\nu_n\), and its complete geometric singularity basket is
\[
\boxed{\frac{n^2+1}{2}\text{ ordinary nodes, and one }A_{n-1}\text{ cusp}.}
\]
The cusp lies at \([-1:1:0]\); the point \(P=[1:0:0]\) is one of the nodes. Projection from \(P\) induces the cyclic Galois extension \(\mathbb C(t)/\mathbb C(t^n)\), of degree \(n\).

The complete embedded projective automorphism group, and indeed the full plane Cremona stabilizer, are
\[
\boxed{\operatorname{Aut}_{\mathbb P^2}(C_n)=
\operatorname{Stab}_{\operatorname{Bir}(\mathbb P^2)}(C_n)
=\{1,\iota\}\cong C_2,\quad
\iota([X:Y:Z])=[-X:-Y:Z].}
\]
Consequently **no nonidentity element** of the cyclic inner Galois group \(G_P\cong C_n\) admits an extension to a Cremona transformation preserving \(C_n\). The first asserted new degree is \(n+2=11\), when the curve has \(41\) nodes and one \(A_8\) cusp; the earlier degree-seven case is known.

## Assumptions and scope
All statements are over \(\mathbb C\). The parameter \(n\) runs through all integers at least nine congruent to one modulo four; it need not be prime. A node means an ordinary double point with distinct tangent lines; \(A_{n-1}\) denotes the analytic germ \(y^2=x^n\), with \(n\) odd. The full Cremona stabilizer consists of birational self-maps of the ambient plane whose restriction preserves the irreducible curve birationally. An extension of a deck transformation means such a map whose induced normalization automorphism is the specified element of \(G_P\).

## Proof
**1. Morphism, degree, and Galois projection.** Write \(k=(n+1)/2\), an odd integer at least five. The displayed forms are homogeneous of degree \(n+2\). A simultaneous zero of their last two coordinates requires \(u^2+v^2=0\) (the cases \(u=0\) and \(v=0\) do not make both zero). At \(u/v=\pm i\), one has \((u/v)^{n+1}=-1\), so the first coordinate does not vanish. Hence the forms have no base point.

On the chart \(v=1\), away from \(1+t^2=0\), use target coordinates \(x=X/Z\) and \(y=Y/Z\). With \(t=u/v\),
\[
x(t)=\frac{t(1-t^{n+1})}{1+t^2},\qquad y(t)=t^n.
\]
If the image function field were a proper intermediate field between \(\mathbb C(t^n)\) and \(\mathbb C(t)\), Galois correspondence would give a nonidentity \(\zeta\in\mu_n\) fixing \(x(t)\). But
\[
\frac{x(t)-x(\zeta t)}{t}
=\frac{(\zeta-1)\bigl((\zeta+1)t^{n+1}+\zeta t^2-1\bigr)}{(1+t^2)(1+\zeta^2t^2)}
\]
is not the zero rational function for \(\zeta\neq1\). Therefore \(\mathbb C(x,y)=\mathbb C(t)\): the map is birational. Since the forms are base-point-free of degree \(n+2\), the image is integral of precisely that degree. The projection \([X:Y:Z]\dashrightarrow[Y:Z]\) becomes \(t\mapsto t^n\), so \(P\) is an inner cyclic Galois point of degree \(n\).

**2. Smooth branches and the distinguished node.** At any finite \(t\neq0,\pm i\), the derivative \(y'(t)=nt^{n-1}\) is nonzero; at \(t=0\), \(x'(0)=1\). Thus the parametrization is immersive away from the two points \(t=\pm i\) and infinity. The two points \(\pm i\) map to \(P\), where the local parameter \(Z/X\) has a simple zero. Their tangent slopes \(Y/Z=t^n\) are respectively \(+i\) and \(-i\). They form exactly one ordinary node at \(P\).

**3. All remaining collisions and their transverse nature.** Two distinct finite parameters \(s,t\) away from \(\pm i\) can have the same image only when \(s=\zeta t\) for some \(\zeta\in\mu_n\setminus\{1\}\); necessarily \(t\neq0\). Put \(w=t^2\). The displayed difference formula shows equality if and only if
\[
Q_\zeta(w):=(\zeta+1)w^k+\zeta w-1=0. \tag{1}
\]
Because \(n\) is odd, \(\zeta\neq-1\); hence \(Q_\zeta\) has degree \(k\), with neither \(w=0\) nor \(w=-1\) a root (the latter uses oddness of \(k\)).

Every root is simple. Indeed, a simultaneous zero of \(Q_\zeta\) and its derivative forces
\[
w=\frac{k}{(k-1)\zeta},\qquad
|1+\zeta|=\frac{(k-1)^{k-1}}{k^k}<\frac1k.
\]
But a nontrivial \(n\)-th root of unity, with odd \(n=2k-1\), satisfies
\[
|1+\zeta|\geq2\sin\frac{\pi}{2n}\geq\frac2n>\frac1k,
\]
a contradiction. Thus each nonidentity \(\zeta\) yields \(k\) distinct nonzero values of \(w\), hence \(2k\) ordered source parameters \(t\).

No image has three distinct finite preimages. Otherwise \(Q_\zeta(w)=Q_\eta(w)=0\) for distinct nonidentity \(\zeta,\eta\), and subtraction gives \(w^k+w=0\). Substitution into (1) yields \(w=-1\), contradicting oddness of \(k\). Nor can any of these points coincide with the image of infinity: the latter has \(Z=0\) and is distinct from \(P\), while the finite parameters here have \(Z\neq0\). The paired tangent lines are distinct, because \(y'(t)=\zeta y'(\zeta t)\) while the simple root of (1) gives \(\frac{d}{dt}(x(t)-x(\zeta t))\neq0\). Therefore each collision is an ordinary node. Dividing the \(2k(n-1)\) ordered collision pairs by two yields exactly \(k(n-1)=(n^2-1)/2\) further nodes.

**4. The unique cusp and completeness.** At \(t=\infty\) put \(a=v/u\), and use coordinates centered at \([-1:1:0]\):
\[
\xi=\frac{X+Y}{Y}=\frac{a^{n+1}+a^2}{1+a^2}
=a^2\frac{1+a^{n-1}}{1+a^2},
\qquad \eta=\frac ZY=a^n.
\]
Since \(n-1\) is divisible by four, the multiplicative unit in \(\xi/a^2\) is a convergent analytic unit in \(a^2\). Taking its analytic square root and then absorbing a unit in \(\eta\) gives the analytic normal form \(\eta'^2=\xi^n\). Thus the sole nonimmersive branch is an \(A_{n-1}\) cusp with multiplicity two and \(\delta=(n-1)/2\). The enumerated nodes contribute \((n^2+1)/2\) to the delta sum, so
\[
\sum\delta=\frac{n^2+1}{2}+\frac{n-1}{2}=\frac{n(n+1)}2=p_a(C_n).
\]
The normalization is \(\mathbb P^1\), so the genus formula proves the singularity census exhaustive. In particular every singular point has multiplicity exactly two.

**5. Full projective stabilizer.** A projective self-map of \(C_n\) lifts uniquely to an automorphism of its normalization. The unique unibranch singularity of type \(A_{n-1}\) fixes \(t=\infty\), so the lift is \(t\mapsto at+b\) with \(a\neq0\). The plane embedding is defined by the three-dimensional polynomial space
\[
W=\operatorname{span}\{t-t^{n+2},\ t^n+t^{n+2},\ 1+t^2\}\subset\mathbb C[t]_{\leq n+2}.
\]
A lift induced by a projective self-map must preserve this subspace. Its members have vanishing \(t^{n+1}\) coefficient, whereas \((at+b)-(at+b)^{n+2}\) has that coefficient equal to \(-(n+2)a^{n+1}b\). Hence \(b=0\). Moreover the sole elements of \(W\) of degree at most two are multiples of \(1+t^2\), so \(1+a^2t^2\in W\) forces \(a^2=1\). Both choices occur: \(t\mapsto-t\) acts on the target as \([X:Y:Z]\mapsto[-X:-Y:Z]\). Therefore the complete embedded projective automorphism group has order two.

**6. Cremona nonextendibility.** Abouelsaad's multiplicity rigidity lemma (Reference 1, Lemma 5.1) states that if each singularity of an irreducible plane curve has multiplicity strictly less than one third of the degree, every birational plane self-map preserving that curve is projective linear. Here \(2<(n+2)/3\) for all asserted \(n\), so the full Cremona stabilizer equals the just-computed projective group \(C_2\). Every nontrivial deck map is \(t\mapsto\zeta t\) with \(\zeta\in\mu_n\setminus\{1\}\); as \(n\) is odd, \(\zeta\neq-1\). No such lift lies in the projective stabilizer, proving nonextendibility.

## Verification
The included standalone \(\texttt{verify.py}\) checks the exact rational collision identity and verifies, for \(n=9,13,17\), that the discriminant of \(Q_\zeta\) is coprime to \((\zeta^n-1)/(\zeta-1)\). It also checks the genus/delta identities and the forced vanishing of the near-leading coefficient in the polynomial-space stabilizer argument. Those exact finite calculations test the uniform proof but do not establish the theorem by extrapolation; the root-modulus, no-triple, local-analytic, and polynomial-space arguments above establish it for all admissible \(n\).

## Relationship to prior work
Abouelsaad (Reference 1) supplies the degree-seven, cyclic degree-five example and the multiplicity-to-Cremona rigidity lemma, but does not classify the infinite degree-\(n+2\) family. The previously established degree-seven singularity basket of thirteen nodes plus an \(A_4\) cusp is acknowledged, and lies outside the asserted \(n\ge9\) domain. The new contribution is the parameter-uniform, exhaustive singularity classification, exact Cremona stabilizer, and arbitrarily large odd cyclic orders with no nontrivial ambient Cremona extensions. Miura (Reference 2) proves extension for cyclic order three, addressing a different range.

## Limitations
The theorem is restricted to characteristic zero and \(n\equiv1\pmod4\), \(n\ge9\); it does not classify all Galois points of \(C_n\), embeddings under arbitrary birational changes of plane coordinates, or other congruence classes. The roots defining the additional nodes are given implicitly by (1); their arithmetic fields are not classified. Bibliographic searches cannot rule out unpublished or unindexed equivalent generalizations.

## References
1. A. Abouelsaad, *Galois Points and Cremona Transformations*, arXiv:2302.00324v1 (1 February 2023), Glasgow Mathematical Journal 66 (2024), 471–478, DOI: 10.1017/S0017089524000090; especially Theorem C, Lemmas 5.1–5.2.
2. K. Miura, *Extendable birational transformations belonging to Galois points*, arXiv:2302.00870v1 (2023), especially Theorem 1 on cyclic order three.
