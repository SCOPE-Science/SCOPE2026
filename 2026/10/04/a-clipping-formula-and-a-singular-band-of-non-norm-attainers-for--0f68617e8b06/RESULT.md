# A clipping formula and a singular band of non-norm-attainers for measure-augmented C(K) norms
## Finding
Let \(K\) be a compact Hausdorff space and let \(\nu\) be a finite positive regular Borel measure with full support. Equip real \(C(K)\) with
\[
\|f\|_\nu=\|f\|_\infty+\int_K |f|\,d\nu.
\]
For a nonzero finite signed regular Borel measure \(\lambda\), write its Lebesgue decomposition with respect to \(\nu\) as
\[
\lambda=h\nu+\lambda_s,\qquad h\in L^1(\nu),\qquad \lambda_s\perp\nu.
\]
There is a unique \(\tau>0\) such that
\[
\|\lambda_s\|_{{TV}}+\int_K (|h|-\tau)_+\,d\nu=\tau.
\]
Then
\[
\|\lambda\|_{{\nu,*}}=\tau
=\inf_{{g\in L^\infty(\nu)}}\max\left\{{\|\lambda-g\nu\|_{{TV}},\|g\|_\infty}}\right\},
\]
and the infimum is attained by the clipped density
\[
g_\tau=\operatorname{{sgn}}(h)\min\{{|h|,\tau}}.
\]
Put \(r_\tau=\lambda-g_\tau\nu\). The functional \(\lambda\) attains its dual norm if and only if there exists \(u\in C(K)\) with \(\|u\|_\infty=1\) satisfying
\[
u=\frac{{d r_\tau}}{{d|r_\tau|}}\quad |r_\tau|\text{{-almost everywhere}},
\qquad
u g_\tau=\tau|u|\quad \nu\text{{-almost everywhere}}.
\]
In particular, if \(\lambda\perp\nu\) and \(\lambda\ne0\), then \(\|\lambda\|_{{\nu,*}}=\|\lambda\|_{{TV}}\) and \(\lambda\) does not attain its norm. Thus the entire \(\nu\)-singular band of the dual retains its total-variation geometry while losing norm attainment away from zero. If \(\nu\) is nonatomic, every evaluation \(\delta_t\) belongs to this singular band, so \(\|\delta_t\|_{{\nu,*}}=1\), no \(\delta_t\) attains, and
\[
\|\delta_s-\delta_t\|_{{\nu,*}}=2\qquad(s\ne t).
\]

## Assumptions and scope
The space is real \(C(K)\). The measure \(\nu\) is finite, positive, regular, and has full support. Full support makes \(f\mapsto\int_K|f|\,d\nu\) faithful on \(C(K)\) and makes the displayed norm an equivalent lattice norm. The signed measure \(\lambda\) is arbitrary except that the norm-attainment criterion is stated for \(\lambda\ne0\); the zero functional is trivial. No metrizability or separability of \(K\) is used. The nonatomic consequences require \(\nu(\{{t\}})=0\) for every \(t\in K\).

## Proof
Let \(p(f)=\|f\|_\infty\) and \(q(f)=\int_K|f|\,d\nu\). The diagonal map \(f\mapsto(f,f)\) embeds \(C(K)\), with norm \(p+q\), into the \(\ell_1\)-sum of the completions for \(p\) and \(q\). The first dual is the regular-measure space \(M(K)\) with total variation. Because continuous functions are dense in \(L^1(\nu)\), the second dual consists of functionals \(f\mapsto\int_K f g\,d\nu\) with \(g\in L^\infty(\nu)\), of norm \(\|g\|_\infty\). Taking the quotient dual of the diagonal subspace gives
\[
\|\lambda\|_{{\nu,*}}
=\inf_{{g\in L^\infty(\nu)}}
\max\left\{{\|\lambda-g\nu\|_{{TV}},\|g\|_\infty}}\right\}.
\]
Equivalently, \(\|\lambda\|_{{\nu,*}}\le t\) exactly when some \(g\) obeys \(\|g\|_\infty\le t\) and \(\|\lambda-g\nu\|_{{TV}}\le t\).

Using \(\lambda=h\nu+\lambda_s\) and mutual singularity,
\[
\|\lambda-g\nu\|_{{TV}}
=\|\lambda_s\|_{{TV}}+\int_K|h-g|\,d\nu.
\]
Under \(\|g\|_\infty\le t\), the pointwise best approximation is
\[
g_t=\operatorname{{sgn}}(h)\min\{{|h|,t}},
\]
for which
\[
\inf_{{\|g\|_\infty\le t}}\|\lambda-g\nu\|_{{TV}}
=\|\lambda_s\|_{{TV}}+\int_K(|h|-t)_+\,d\nu.
\]
Hence \(\|\lambda\|_{{\nu,*}}\) is the least \(t\ge0\) for which the right side is at most \(t\). The function
\[
\Phi(t)=\|\lambda_s\|_{{TV}}+\int_K(|h|-t)_+\,d\nu-t
\]
is continuous and strictly decreasing, with \(\Phi(0)=\|\lambda\|_{{TV}}>0\) for \(\lambda\ne0\) and \(\Phi(t)\to-\infty\). This proves existence and uniqueness of \(\tau\), the norm formula, and optimality of \(g_\tau\). It also gives \(\|r_\tau\|_{{TV}}=\tau\) and \(\|g_\tau\|_\infty\le\tau\).

For norm attainment, suppose first that \(f\ne0\) satisfies \(\lambda(f)=\tau\|f\|_\nu\), after changing sign if necessary. Since
\[
r_\tau(f)\le\tau\|f\|_\infty,
\qquad
\int_K f g_\tau\,d\nu\le\tau\int_K|f|\,d\nu,
\]
and the sum of the two left sides equals the sum of the two right sides, equality holds in both. Setting \(u=f/\|f\|_\infty\), equality in the total-variation estimate gives
\[
u=\frac{{d r_\tau}}{{d|r_\tau|}}
\quad |r_\tau|\text{{-almost everywhere}},
\]
while equality in the \(L^1\)-\(L^\infty\) estimate gives
\[
u g_\tau=\tau|u|\quad\nu\text{{-almost everywhere}}.
\]
Conversely, if such a continuous \(u\) exists, both estimates are equalities, so \(\lambda(u)=\tau\|u\|_\nu\); normalizing \(u\) in \(\|\cdot\|_\nu\) yields an attaining vector.

If \(\lambda\perp\nu\), then \(h=0\), the threshold equation gives \(\tau=\|\lambda\|_{{TV}}\), and \(g_\tau=0\). The norm-attainment condition would force a continuous \(u\) with \(\|u\|_\infty=1\) and \(u=0\) \(\nu\)-almost everywhere. Full support of \(\nu\) forces every such continuous \(u\) to vanish identically, a contradiction. Thus every nonzero singular measure is non-norm-attaining. For nonatomic \(\nu\), each \(\delta_t\) and each \(\delta_s-\delta_t\) with \(s\ne t\) is singular; their total variations are respectively \(1\) and \(2\), proving the final assertions.

## Verification
The proof was checked against the two equality cases used in the quotient-dual formula: total variation and \(L^1\)-\(L^\infty\) duality. Boundary cases were checked separately. For a purely singular measure, the formula reduces to \(\|\lambda\|_{{\nu,*}}=\|\lambda\|_{{TV}}\). For an evaluation at an atom of mass \(a=\nu(\{{t\}})>0\), the threshold equation yields \(\|\delta_t\|_{{\nu,*}}=1/(1+a)\); at a \(\nu\)-null point it yields \(1\). These specialize consistently with the lattice-homomorphism norm formula in Lemma 3.2 of the cited 2025 preprint. Full support is used exactly where a continuous function that vanishes \(\nu\)-almost everywhere is forced to vanish everywhere.

## Relationship to prior work
Bilokopytov, García-Sánchez, de Hevia, Martínez-Cervantes and Tradacete introduced the renorming \(\|x\|_\mu=\|x\|+\mu(|x|)\) and proved that, for a strictly positive \(\mu\), the only lattice homomorphisms attaining their norm are coordinate functionals of atoms. Their Lemma 3.2 computes the renormed norm of one lattice homomorphism, and their examples include \(C[0,1]\) with \(\|f\|_\infty+\int_0^1|f|\). The finding here treats every signed measure in \(C(K)^*\), gives an exact clipping formula for the full dual norm, characterizes norm attainment by equality in the two dual components, and identifies the whole \(\nu\)-singular band as an isometric family of non-norm-attainers. The earlier work of Dantas, Martínez-Cervantes, Rodríguez Abellán and Rueda Zoca establishes the unrenormed norm-attainment theory for lattice homomorphisms but does not provide this full signed-measure description.

## Limitations
The statement is specific to the additive lattice norm \(\|f\|_\infty+\int|f|\,d\nu\); different combinations of the two terms have corresponding rescalings but are not asserted here. The norm-attainment criterion is measure-theoretic and does not by itself classify when the required sign pattern admits a continuous representative for an arbitrary absolutely continuous density \(h\). The literature comparison found no statement with the same full dual formula plus norm-attainment classification, but the quotient-dual and clipping ingredients are standard functional-analysis tools; specialized interpolation literature could contain an equivalent reformulation. No independent audit has been performed.

## References
1. E. Bilokopytov, E. García-Sánchez, D. de Hevia, G. Martínez-Cervantes, P. Tradacete, “Norm-attaining lattice homomorphisms and renormings of Banach lattices,” arXiv:2502.10165v1, first public 14 February 2025; Journal of Functional Analysis 290 (2026), 111250, DOI 10.1016/j.jfa.2025.111250.
2. S. Dantas, G. Martínez-Cervantes, J. D. Rodríguez Abellán, A. Rueda Zoca, “Norm-attaining lattice homomorphisms,” Revista Matemática Iberoamericana 38 (2022), 981–1002, DOI 10.4171/RMI/1292.
