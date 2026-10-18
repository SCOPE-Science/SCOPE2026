# A one-blowup resolution of the positive-characteristic Anick cyclic quotient

## Finding
For an algebraically closed field \(k\) of characteristic \(p>0\), the cyclic quotient of the Anick four-variable polynomial automorphism is a factorial, normal, Gorenstein singular fourfold. Blowing up its reduced singular plane gives a smooth resolution with discrepancy \(2-p\). Its exceptional divisor is smooth but every geometric fibre over the plane is a nonreduced \(p\)-fold line. The quotient morphism has generic degree \(p\) and special fibre length \(p^2\), hence is not flat.

## Assumptions and scope
Let \(p\) be any prime and \(k\) an algebraically closed field of characteristic \(p\). Put \(A=k[x,y,z,t]\) and \(\delta=xz-yt\). Let \(\sigma\) act by
\[
\sigma(x,y,z,t)=(x+\delta t,\ y+\delta z,\ z,\ t).
\]
It has exact order \(p\): \(\delta,z,t\) are fixed, so its \(j\)-th iterate adds \(j\delta(t,z)\), and it is not the identity for \(1\le j<p\). Denote \(X_p=\operatorname{Spec}(A^{\langle\sigma\rangle})\).

Define the invariant polynomials
\[
U=x^p-(\delta t)^{p-1}x,\qquad
V=y^p-(\delta z)^{p-1}y.
\]
The quotient has the hypersurface coordinates \((z,t,d,U,V)\), with \(d\) representing \(\delta\), and equation
\[
F=z^pU-t^pV-d^p\bigl(1-(zt)^{p-1}\bigr)=0.
\]
The presentation itself follows from Kuroda's general Nagata-type invariant-ring theory; the geometric blowup, exceptional fibres, discrepancy and factoriality are the assertions proved here.

## Proof
**Invariant presentation and finiteness.** The five displayed functions are invariant by the characteristic-\(p\) binomial identity. They satisfy \(F=0\), since \(zx-ty=\delta\). Set \(B=k[z,t,d,U,V]/(F)\). The polynomial \(F\) is irreducible: its coefficients as a polynomial linear in \(U\) and \(V\) have gcd one (in particular \(z^p\) is coprime to \(t^pV+d^p(1-(zt)^{p-1})\)). Its Jacobian satisfies \(\partial_UF=z^p\) and \(\partial_VF=-t^p\); hence singular points lie on \(z=t=0\), where \(d^p=0\). The reduced singular locus is exactly \(S=V(z,t,d)\simeq\mathbb A^2_{U,V}\), of codimension two in \(X_p\). Thus \(B\) is normal by \(R_1+S_2\). The ring \(A\) is integral over \(B\), because \(x,y\) satisfy monic degree-\(p\) equations, and \(B_z=k[z,z^{-1},t,d,V]\): there \(x=(d+yt)/z\), while \(\sigma(y)=y+dz\), so \(V\) generates the invariant rational field of this Artin–Schreier translation. Consequently \(\operatorname{Frac}(B)=\operatorname{Frac}(A)^{\langle\sigma\rangle}\). Every invariant in \(A\) is integral over \(B\) and lies in its fraction field; normality yields \(A^{\langle\sigma\rangle}=B\).

**Factoriality and singularities.** Because \(B_z=k[z,z^{-1},t,d,V]\) is factorial and
\[
B/(z)=k[t,d,U,V]/(t^pV+d^p)
\]
is a domain (the defining polynomial is primitive and linear in \(V\)), the principal element \(z\) is prime. Nagata's localization criterion implies \(B\) is a UFD, hence \(\operatorname{Cl}(X_p)=0\). The Jacobian argument identifies the entire geometric singular set: exactly \(S\), smooth of dimension two. Since \(B\) is a hypersurface it is Gorenstein.

**One-blowup resolution.** Blow up the reduced ideal \(I=(z,t,d)\) of \(S\). Its three standard affine charts are the following strict transforms; they equal the respective blowup charts because the displayed quotients are domains and the respective exceptional coordinate is a nonzerodivisor:
\[
\begin{array}{ll}
 z\text{-chart}: & t=zb,\ d=zc,\quad U-b^pV-c^p(1-(z^2b)^{p-1})=0;\\
 t\text{-chart}: & z=ta,\ d=tc,\quad a^pU-V-c^p(1-(t^2a)^{p-1})=0;\\
 d\text{-chart}: & z=da,\ t=db,\quad a^pU-b^pV-1+(d^2ab)^{p-1}=0.
\end{array}
\]
The first two charts are smooth because their equations have unit partial derivatives with respect to \(U\) and \(V\), respectively. In the third, \(a=b=0\) gives the impossible equality \(-1=0\) when \(d=0\); when \(d\ne0\), the blowup is already isomorphic to the smooth complement of \(S\). More directly, \(a\) and \(b\) cannot both vanish on the third chart since then its equation reduces to \(-1=0\), at every \(d\); therefore at least one of \(\partial_UF_{d}=a^p\) and \(\partial_VF_{d}=-b^p\) is nonzero. All charts are smooth, so the blowup \(\pi:\widetilde X_p\to X_p\) is a resolution.

**Exceptional divisor and discrepancy.** In \(S\times\mathbb P^2_{[Z:T:D]}\), the exceptional divisor is
\[
E=\big\{Z^pU-T^pV-D^p=0\big\}.
\]
Its total space is smooth: where \(Z\ne0\) or \(T\ne0\), differentiation in \(U\) or \(V\) is nonzero; the locus \(Z=T=0\) is excluded by its equation. It is integral, since the displayed equation is primitive and linear in \(U,V\). At every geometric point \((U,V)=(u,v)\in S(k)\), it becomes
\[
(u^{1/p}Z-v^{1/p}T-D)^p=0,
\]
so the scheme fibre is one projective line thickened with multiplicity exactly \(p\). In the ambient blowup of \(\mathbb A^5\) along its codimension-three plane, the relative canonical divisor is \(2E_{\mathrm{amb}}\), while the defining hypersurface has multiplicity exactly \(p\) along that plane. Adjunction on the smooth strict transform yields
\[
K_{\widetilde X_p}-\pi^*K_{X_p}=(2-p)E.
\]
Thus \(a(E;X_p)=2-p\), with the conventional discrepancy normalization where smooth blowup of a codimension-three centre has discrepancy two.

**Failure of flatness.** On \(z\ne0\), the quotient is degree \(p\) by the nontrivial Artin–Schreier translation. Over any geometric point of \(S\) with base coordinates \((u,v)\), the quotient fibre algebra is
\[
k[x,y]/(x^p-u,\ y^p-v),
\]
which has length \(p^2\). As \(p^2\ne p\), the finite quotient morphism cannot be flat.

## Verification
The accompanying `anick_quotient_verifier.py` checks invariance, the hypersurface relation and all three strict-transform identities over the finite fields with \(p=2,3,5,7\). It exhaustively evaluates \(16+81+625+2401=3123\) affine four-tuples. The infinite claims of normality, factoriality, smoothness, discrepancy and fibre multiplicities follow from the proofs above, not from the finite calculations.

## Relationship to prior work
Miasnikov–Shestakov (2026) give the Anick automorphism and its tame factorization in characteristic different from two, but do not study this positive-characteristic cyclic quotient or its blowup. Crucially, Kuroda (2022), Theorems 6.8 and 6.10, already gives a broad invariant-ring presentation for Nagata-type order-\(p\) automorphisms; taking base \(k[z,t]\), linear parameter \(-ty\) and invariant \(zx-ty\) encompasses the displayed invariant hypersurface. Accordingly, this presentation is an **input**, not a novelty claim. The additional geometric theorem here computes the explicit one-step resolution, factoriality, exceptional fibres, discrepancy and finite-map failure of flatness. Lorenzini–Schröer (2019) study other positive-characteristic wild quotient singularities; their abstract does not resolve these specific claims, though uninspected details remain a literature risk.

## Limitations
The statement concerns this named cyclic action over algebraically closed fields of characteristic \(p\); it does not classify all polynomial automorphism quotient singularities. It does not assert minimality or uniqueness of resolutions. The exceptional geometric fibres are nonreduced as schemes, not multiple irreducible exceptional components. The novelty comparison cannot exclude inaccessible or unindexed equivalent local blowup calculations.

## References
Miasnikov, A. and Shestakov, I., *An explicit tame factorization of the four-variable Anick automorphism*, arXiv:2610.11013v1 (first posted 2026-10-07), Sections 1–5.

Kuroda, S., *Polynomial automorphisms of characteristic order and their invariant rings*, arXiv:2202.00262v1 (2022), Section 6, especially Theorems 6.8 and 6.10.

Lorenzini, D. and Schröer, S., *Moderately ramified actions in positive characteristic*, arXiv:1904.08371 (2019), background comparison only.
