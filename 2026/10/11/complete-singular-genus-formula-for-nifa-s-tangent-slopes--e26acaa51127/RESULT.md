# Complete singular-genus formula for Nifa's tangent slopes
## Finding
Let \(N\ge2\), and let \(\Gamma_N\) be the exterior group in Nifa's construction of knotted tori with diffeomorphic exteriors. Write \(\lambda\) for the preferred trefoil longitude in \(\Gamma_N\). For every integer \(m\ne0\), write
\[
M=|m|=Na+r,\qquad a\ge0,\qquad 0\le r<N.
\]
Then
\[
\operatorname{cl}_{\Gamma_N}(\lambda^m)=
\begin{cases}
1+\left\lceil \dfrac{a(N-1)}2\right\rceil,&r=0,\\[6pt]
1+\left\lceil \dfrac{a(N-1)+r-1}2\right\rceil,&1\le r<N.
\end{cases}
\]
Equivalently,
\[
\operatorname{cl}_{\Gamma_N}(\lambda^m)
=1+\left\lfloor\frac{1+|m|(N-1)/N}2\right\rfloor
\qquad(m\ne0),
\]
and \(\operatorname{cl}_{\Gamma_N}(1)=0\).

For a core torus \(\widehat T_{N,j}\) in the same construction, the natural tangent generators satisfy
\[
\lambda_j\longmapsto\lambda,
\qquad
s_j\longmapsto\lambda^{-N}.
\]
Hence a primitive tangent slope
\[
\alpha=u[\lambda_j]+v[s_j]
\]
represents \(\lambda^m\), where \(m=u-Nv\). Nifa's singular-genus/commutator-length identification therefore gives
\[
g_{\mathrm{sing}}(\alpha)=0
\quad\text{if }m=0,
\]
and otherwise gives exactly the formula above with \(m=u-Nv\). Thus every primitive tangent slope in this family has an exact singular-genus value.

## Assumptions and scope
The statement concerns the exterior groups and tangent-coordinate systems appearing in Nifa's construction. For the corresponding filled core torus to lie in the standard \(S^4\), the filling index \(j\) is assumed to satisfy Nifa's stated arithmetic condition \(\gcd(N,6j-1)=1\). The group-theoretic commutator-length formula itself depends only on \(N\) and \(m\).

The result is about singular slope genus, not embedded slope genus. The zero case means the peripheral loop is trivial in the exterior group and hence has singular genus zero. No claim is made that the finite commutator length is determined by stable commutator length in an arbitrary group; the finite formula here uses the special covering construction and the explicit circle-action representation of \(\Gamma_N\).

## Proof
Nifa writes the trefoil group as
\[
G=\langle a,b\mid a^2=b^3\rangle,
\qquad
\mu=b^{-1}a,
\qquad
h=a^2=b^3,
\qquad
\lambda=h\mu^{-6},
\]
and obtains
\[
\Gamma_N\cong G/\langle\!\langle[\lambda^N,G]\rangle\!\rangle.
\]
In particular \(z=\lambda^N\) is central in \(\Gamma_N\).

For the lower bound, use Nifa's representation
\[
\rho_N:\Gamma_N\longrightarrow\widetilde{\mathrm{PSL}}_2(\mathbb R)
\]
into the group \(\mathcal H\) of lifts of orientation-preserving circle homeomorphisms. In the notation of the construction,
\[
\rho_N(\mu)=\widetilde Q\,\widetilde R_{\pi/(6N)}\,\widetilde Q^{-1},
\qquad
\rho_N(h)=\widetilde R_\pi.
\]
Because \(\lambda=h\mu^{-6}\), these two rotations have the same center and give
\[
\rho_N(\lambda)
=
\widetilde Q\,\widetilde R_{\pi(1-1/N)}\,\widetilde Q^{-1}.
\]
Thus \(\rho_N(\lambda^M)\) is conjugate in \(\mathcal H\) to the rigid translation
\[
x\longmapsto x+e,
\qquad
e=\frac{M(N-1)}N.
\]
The Eisenbud--Hirsch--Neumann criterion quoted and used by Nifa says that an element \(F\in\mathcal H\) is a product of \(g\ge1\) commutators exactly when
\[
\min_x|F(x)-x|<2g-1.
\]
Therefore the translation above needs at least the least integer \(g\ge1\) for which
\[
e<2g-1.
\]
Since commutator length cannot increase under a homomorphism,
\[
\operatorname{cl}_{\Gamma_N}(\lambda^M)
\ge
1+\left\lfloor\frac{1+e}2\right\rfloor.
\]
If \(r=0\), this is
\[
1+\left\lceil\frac{a(N-1)}2\right\rceil.
\]
If \(1\le r<N\), put
\[
A=a(N-1)+r-1.
\]
Then
\[
e=A+\frac{N-r}N,
\qquad
0<\frac{N-r}N<1,
\]
so the same lower bound is
\[
1+\left\lceil\frac A2\right\rceil.
\]

For the upper bound, the case \(r=0\) is exactly Nifa's Theorem 6.5. Suppose \(1\le r<N\). The case \(M=1\) is also already realized because Nifa explicitly writes \(\lambda\) as one commutator. Assume now \(M=D\ge2\).

Choose a permutation \(C\in S_D\) with cycle type
\[
N^a r^1,
\]
where a cycle of length one is allowed when \(r=1\). Thus \(C\) has \(a+1\) cycles and sign parity
\[
A=D-(a+1)=a(N-1)+r-1.
\]
Let \(\varepsilon\in\{0,1\}\) have the same parity as \(A\), and choose \(P_0\) to be the identity when \(\varepsilon=0\) and a transposition when \(\varepsilon=1\). Then \(CP_0\) is even. For \(D\ge5\), Bertram's cycle-factorization theorem writes \((CP_0)^{-1}\) as a product of two \(D\)-cycles; for \(D=2,3,4\), the same statement follows by the elementary low-degree check used in this covering argument.

Now apply the monodromy-cover construction of Nifa's Lemma 6.3 with boundary permutation \(C\). It gives a connected oriented degree-\(D\) branched cover \(S\to S_{1,1}\) whose boundary has \(a\) components of degree \(N\) and one component of degree \(r\), with exactly \(\varepsilon\) simple branch points. Hence
\[
\chi(S)=-D-\varepsilon.
\]
Writing the genus of \(S\) as \(g\), its \(a+1\) boundary components give
\[
2-2g-(a+1)=-D-\varepsilon,
\]
so
\[
g=1+\frac{A+\varepsilon}2
=1+\left\lceil\frac A2\right\rceil.
\]
Map the punctured-torus base to \(\Gamma_N\) so that its boundary represents \(\lambda\). The \(a\) degree-\(N\) boundary components of the cover map to conjugates of \(z=\lambda^N\), and the remaining component maps to a conjugate of \(\lambda^r\). Because \(z\) is central, their boundary product is conjugate to \(\lambda^{Na+r}=\lambda^M\), up to simultaneous inversion from orientation convention. The surface relation therefore expresses \(\lambda^M\) as a product of \(g\) commutators. This matches the lower bound.

Finally,
\[
\operatorname{cl}(x^{-1})=\operatorname{cl}(x),
\]
so the formula depends only on \(M=|m|\). The tangent-slope statement follows from Nifa's peripheral map and his lemma identifying singular slope genus with commutator length.

## Verification
The proof was checked against the source statements that carry the non-elementary input. Nifa's Proposition 2.3 gives the peripheral map and the quotient presentation of \(\Gamma_N\); the proof of Proposition 6.1 supplies the circle-action representation; Theorem 6.5 gives the exact central-power case and an explicit one-commutator expression for \(\lambda\); Lemma 6.6 identifies singular genus with commutator length; and Remark 6.8 records the remaining primitive tangent slopes for which the source asserts no formula.

The upper-bound construction is the same monodromy-cover mechanism as Nifa's Lemma 6.3, with the boundary permutation changed from equal \(N\)-cycles to cycle type \(N^a r^1\). Its only extra arithmetic is the number of boundary cycles and the parity correction. Bertram's even-permutation factorization supplies the two full cycles in degree at least five, with the low degrees checked directly.

The bundled verifier checks, over a large finite range, that the residue formula, the compact floor formula, the strict Eisenbud--Hirsch--Neumann threshold, the published central-power formula, and the Euler-characteristic genus formula all agree. This computation checks the arithmetic consequences only; it is not evidence for the universal covering or group-theoretic steps.

## Relationship to prior work
Liu--Ni--Sun--Wang identify singular slope genus with commutator length in the exterior group and the induced stable slope seminorm with stable commutator length. That framework is general and predates this exterior family.

Nifa proves the exact commutator length of every power of \(z=\lambda^N\), computes the corresponding singular genus in the divisibility case, and in Remark 6.8 explicitly states that no formula is asserted for the other primitive tangent slopes. The present formula fills exactly that finite, unstable remainder by combining the source's circle-action lower bound with a mixed-cycle version of its covering construction.

A previous stable calculation for this family determines
\[
\operatorname{scl}_{\Gamma_N}(\lambda^m)=\frac{N-1}{2N}|m|.
\]
That stable statement does not imply the finite commutator length above: the new formula contains a residue-sensitive integer correction and is what is needed for exact singular genus.

## Limitations
No embedded slope-genus statement is made. The proof uses special features of Nifa's group: centrality of \(\lambda^N\), the explicit representation into \(\mathcal H\), and the monodromy-cover construction. It is not a general formula for powers of a commutator in an arbitrary group.

The originality search can only compare accessible and indexed literature. No equivalent all-power formula was found in the inspected primary sources or targeted searches, but an unindexed observation could exist. The result should therefore be understood as a new derivation relative to the literature checked here, not as a claim that no one has ever noticed the formula.

## References
1. A. Nifa, *Knotted tori in the four-sphere with diffeomorphic exteriors*, 2026, DOI 10.5281/zenodo.22963510.
2. Y. Liu, Y. Ni, H. Sun, and S. Wang, *On slope genera of knotted tori in 4-space*, Pacific Journal of Mathematics 261 (2013), DOI 10.2140/pjm.2013.261.117.
3. E. A. Bertram, *Even permutations as a product of two conjugate cycles*, Journal of Combinatorial Theory, Series A (1972), DOI 10.1016/0097-3165(72)90102-1.
