# Exactly \(135\) translation orbits of conic bundles on a rational elliptic surface

## Finding

Let \(X\) be a smooth rational elliptic surface over \(\mathbb C\) with a section \(O\) and **no reducible fibers** in its elliptic fibration \(\pi:X\to\mathbb P^1\). Identify conic bundles \(\varphi:X\to\mathbb P^1\) that differ only by an automorphism of their target. The Mordell–Weil group \(\operatorname{MW}(\pi)\), acting on \(X\) by fiberwise translations, has exactly
\[
\boxed{135}
\]
orbits on conic bundles. After fixing \(O\), the orbit set is canonically identified with the nonzero isotropic classes in \(E_8/2E_8\) for the quadratic form \(q(\bar v)=\langle v,v\rangle/2\pmod2\). Every orbit contains a pencil with reducible fiber \(O+S_v\), where \(S_v\) is a section whose Mordell–Weil vector has norm \(4\). Each of the \(135\) classes has exactly \(16\) norm-four representatives, and every conic bundle on \(X\) has exactly eight reducible fibers, each a transverse union of two sections.

## Assumptions and scope

The ground field is \(\mathbb C\). The elliptic surface is smooth and relatively minimal, is rational, possesses a zero section, and has no reducible elliptic fibers. For instance the blow-up at the nine distinct transverse basepoints of a general pencil of plane cubics meets these conditions. Fibers of type \(\mathrm I_1\) or \(\mathrm{II}\) are permitted. A conic bundle is a morphism to \(\mathbb P^1\) with general fiber a smooth rational curve; identifying target reparameterizations means the bundle is determined by its fiber divisor class. The group action is by Mordell–Weil translations **only**, not by all automorphisms of \(X\).

Write \(f=-K_X\) for the elliptic-fiber class and \(e=O+f\). Then \(e^2=e\cdot f=1\) and \(f^2=0\), while \(\operatorname{NS}(X)\cong(\mathbb Ze+\mathbb Zf)\oplus E_8(-1)\) is an orthogonal integral decomposition. Give the positive lattice \(E_8\) the pairing \(\langle\ ,\ \rangle\). Each \(v\in E_8\) corresponds to a unique section
\[
[S_v]=e+\left(\frac{\langle v,v\rangle}{2}-1\right)f+v,
\]
and the group law satisfies \(T_w(S_v)=S_{w+v}\).

## Proof

**1. Sections and reducible conic fibers.** The Néron–Severi splitting and section formula follow from the unimodular rational-elliptic-surface lattice and the Shioda height construction, because the elliptic fibration has no reducible fibers (Schütt–Shioda, §§11.1–11.14). Direct intersection gives
\[
S_v\cdot S_w=\frac{\langle v-w,v-w\rangle}{2}-1.
\]
Consequently two distinct sections meet in precisely one point, counted with intersection multiplicity, if and only if \(\langle v-w,v-w\rangle=4\). Their intersection is then transverse.

For any \(v\in E_8\) with \(\langle v,v\rangle=4\), put \(D_v=O+S_v\). We have \(D_v^2=-1-1+2(O\cdot S_v)=0\) and \(D_v\cdot f=2\). Furthermore \(D_v\) is nef: its intersection with either component is zero, and its intersection with any other irreducible curve is nonnegative because those curves are distinct effective curves on a smooth surface. Hence Costa's numerical characterization of conic bundles (Theorem 3.8 in arXiv:2206.03549) shows that \(|D_v|\) is a base-point-free conic pencil.

Conversely, every conic bundle has a singular fiber: \(X\) is the blow-up of \(\mathbb P^2\) at nine (possibly infinitely near) points, so its topological Euler characteristic is \(12\), whereas a smooth \(\mathbb P^1\)-bundle over \(\mathbb P^1\) has Euler characteristic \(4\). Costa's fiber classification (Theorem 4.2) states that, in the absence of reducible elliptic fibers, every singular conic fiber is of type \(A_2\), namely \(S_v+S_w\) for two distinct sections meeting transversely once. Therefore every conic bundle is the Mordell–Weil translate of a \(|D_u|\) with \(\langle u,u\rangle=4\), by translating \(S_v\) to \(O\).

**2. Translational equivalence.** For a norm-four vector \(u\), the formula above gives \([D_u]=2e+u\). The translation \(T_w\) fixes \(f\) and sends the section indexed by \(z\) to the section indexed by \(z+w\). Comparing the orthogonal \(E_8(-1)\)-coordinates of \(T_w(D_u)\) and \(D_{u'}\) shows that a necessary condition for their divisor classes to coincide is
\[
u'\equiv u\pmod{2E_8}.
\]
It is also sufficient. Indeed, if \(u'=u+2w\), the two classes have the same \(E_8(-1)\)-coordinate, the same intersection \(2\) with \(f\), and square zero; these conditions uniquely determine the remaining \(f\)-coefficient. Since \(\operatorname{Pic}^0(X)=0\), the divisor classes and hence the corresponding pencils coincide. Therefore translation orbits are precisely the residue classes modulo \(2E_8\) that contain a norm-four vector.

**3. Exact lattice count.** In its standard Euclidean realization,
\[
E_8=\{z\in\mathbb Z^8:\textstyle\sum z_i\equiv0\pmod2\}\ \cup\ 
\{z+(1/2,\ldots,1/2):z\in\mathbb Z^8,\ \textstyle\sum z_i\equiv0\pmod2\}.
\]
Its norm-four vectors are exhaustively of three forms: (i) one coordinate \(\pm2\), others zero, yielding \(16\); (ii) four coordinates \(\pm1\), others zero, yielding \(\binom84 2^4=1120\); (iii) exactly one coordinate \(\pm3/2\) and seven coordinates \(\pm1/2\), with the required even coordinate sum, yielding \(8\cdot2^7=1024\). The total is \(2160\). An exhaustive exact residue-class computation, implemented in the included standalone script `verify_e8_orbits.py`, groups these \(2160\) vectors into exactly \(135\) classes modulo \(2E_8\), each with exactly \(16\) representatives. The script checks the congruence relation using only exact integer arithmetic. Hence there are \(2160/16=135\) translation orbits. The independently enumerated quadratic form on \(E_8/2E_8\) has \(136\) isotropic classes; the zero class contains no norm-four vector because \(E_8\) has no norm-one vector, so the \(135\) represented classes are precisely the nonzero isotropic ones.

**4. Eight singular conic fibers.** Every singular conic fiber is a transverse union of two projective lines as abstract curves, so its Euler characteristic is \(3\) instead of \(2\) for a smooth rational fiber. By additivity of Euler characteristics,
\[
12=e(X)=2e(\mathbb P^1)+N=4+N,
\]
where \(N\) is the number of such fibers. Thus \(N=8\). This also explains the \(16\) norm-four representatives in each parity class: each of the eight reducible fibers has two possible orders for its sections.

## Verification

Run `python3 verify_e8_orbits.py` with Python 3 and no external dependencies. The script constructs every norm-four vector from the exhaustive three-family classification, groups vectors modulo \(2E_8\), verifies the \(135\) equal-size groups, and separately enumerates all \(256\) vectors of the mod-two root basis to recover \(136\) isotropic classes. The exact finite enumeration proves only the finite lattice-count step; the infinite-family geometric reduction is proved above from the section intersection formula, the correspondence with conic bundles, the translation law, and the classification of singular fibers.

## Relationship to prior work

Costa (arXiv:2206.03549, Theorems 3.8 and 4.2) characterizes conic bundles by nef isotropic divisor classes and classifies the possible singular conic fibers. Schütt–Shioda (arXiv:0907.0298, §11) supplies the Mordell–Weil lattice and its relation to the Néron–Severi group. Garbagnati–Salgado (arXiv:1703.02783) studies conic bundles as inputs to elliptic fibrations of K3 double covers. Costa's dissertation (arXiv:2302.05485, Chapters 2–3) develops the same conic-class and lattice framework. Meira (arXiv:2410.12066, §§3–5) relates singular conic fibers to sections and rank bounds. The cited classification of conic fibers does not state the quotient by Mordell–Weil translations or the exact \(135\)-orbit count in the inspected material; the new classification isolates these parity classes and counts them. Existing results are used as essential hypotheses, not presented as new.

## Limitations

The theorem assumes no reducible elliptic fibers and is formulated over \(\mathbb C\); it does not classify conic bundles on surfaces with reducible elliptic fibers or their orbits under the full automorphism group. The count concerns distinct linear pencils up to reparameterization, not individual morphisms with specified target coordinates. It does not determine the arithmetic fields of definition of pencils. Although the relevant primary texts and a mathematical-record search were compared, exact precedence under alternative descriptions of conic classes is a residual literature risk. Independent audit has not been performed.

## References

1. R. Dias Costa, *Classification of Conic Bundles on a Rational Elliptic Surface in any Characteristic*, arXiv:2206.03549 (first submitted 7 June 2022), especially Theorems 3.8, 4.2 and §7.1.
2. M. Schütt and T. Shioda, *Elliptic Surfaces*, arXiv:0907.0298, §§11.1–11.16, especially §11.14 and the formula for Mordell–Weil lattice sections.
3. A. Garbagnati and C. Salgado, *Linear systems on rational elliptic surfaces and elliptic fibrations on K3 surfaces*, arXiv:1703.02783, §§3 and 5.
4. R. Dias Costa, *Geometric and arithmetic aspects of rational elliptic surfaces*, arXiv:2302.05485, Chapters 2–3.
5. F. Z. Meira, *Conic bundles and Mordell–Weil ranks of elliptic surfaces*, arXiv:2410.12066, §§3–5.
