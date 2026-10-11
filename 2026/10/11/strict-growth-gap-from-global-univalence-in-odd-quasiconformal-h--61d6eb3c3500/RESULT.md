# Strict growth gap from global univalence in odd quasiconformal harmonic maps

## Finding

Let \(0\le k<1\), put \(K=(1+k)/(1-k)\), and let \(\mathcal F_k\) consist of the harmonic maps \(f=h+\overline g\) on \(\mathbb D\) satisfying all of the following:

1. \(f\) is odd, sense-preserving, globally injective, and normalized by \(h(0)=g(0)=g'(0)=0\) and \(h'(0)=1\).
2. Its analytic dilatation \(\omega=g'/h'\) satisfies \(|\omega(z)|\le k\) on \(\mathbb D\).
3. For at least one \(\varepsilon\) with \(|\varepsilon|=1\), the analytic function \(\phi_\varepsilon=h+\varepsilon g\) is univalent on \(\mathbb D\).

Define
\[
U(r)=\frac{1+r^2}{(1-r^2)^2},\qquad
T(k,r)=\int_0^r\frac{(1+ks^2)U(s)}{1-ks^2}\,ds,
\]
and
\[
M(k,r)=\max_{f\in\mathcal F_k}\max_{|z|=r}|f(z)|.
\]
The maximum exists for every fixed \(k,r\). For every \(0<r<1\),
\[
\boxed{M(0,r)=T(0,r)=\frac r{1-r^2}},
\qquad
\boxed{M(k,r)<T(k,r)\quad(0<k<1)}.
\]

The strict gap is not merely pointwise nonattainment in a noncompact family. For each fixed \(0<k<1\) and \(0<r<1\), compactness gives a genuinely improved, positive-deficit universal constant, even though no closed formula for \(M(k,r)\) is established here.

The mechanism can be classified exactly. If global univalence of \(f\) is omitted, while its local orientation and all other stated requirements are retained, then \(T(k,r)\) is an attained and sharp bound for every \(k\), and all normalized equality cases are the rotations of the canonical shear given below. For every \(k>0\), that shear has explicit double values and is therefore inadmissible in the original univalent class. At \(k=0\), it reduces to the univalent analytic odd Koebe square-root map.

## Assumptions and scope

All maps are defined on the open unit disk. The analytic/coanalytic decomposition is unique under the stated normalization. The condition on \(\phi_\varepsilon\) defines the odd quasiconformal harmonic subclass considered in Theorem 6 of the cited 2026 preprint. The inequality \(\lvert\omega(z)\rvert\le k\), together with oddness and \(g'(0)=0\), implies \(\lvert\omega(z)\rvert\le k\lvert z\rvert^2\) by Schwarz's lemma.

The distinction between local and global injectivity is essential: local orientation means that the Jacobian \(J_f=|h'|^2-|g'|^2\) is strictly positive, whereas membership in \(\mathcal F_k\) additionally requires injectivity on all of \(\mathbb D\).

The positive-deficit result is qualitative at each fixed radius; it does not determine the best constant \(M(k,r)\) explicitly or claim a uniform gap as \(r\) approaches an endpoint.

## Proof

**1. The universal envelope and its equality conditions.** Because \(f\) is odd, \(\omega\) is even and vanishes at the origin. For any admissible unit phase \(\varepsilon\), the analytic odd univalent map \(\phi=h+\varepsilon g\) obeys the classical odd distortion inequality
\[
|\phi'(z)|\le U(|z|).
\]
As \(\phi'=h'(1+\varepsilon\omega)\), we have on \(|z|=s\)
\[
|h'(z)|\le\frac{U(s)}{1-ks^2},\qquad
|g'(z)|\le\frac{ks^2U(s)}{1-ks^2}.
\]
Integrating radially yields \(|f(z)|\le T(k,|z|)\).

Suppose equality holds at some \(z_0\) with \(0<|z_0|=r<1\). The normalized rotation \(f_\theta(z)=e^{-i\theta}f(e^{i\theta}z)\), with \(z_0=re^{i\theta}\), belongs to the same class and attains equality at the real point \(r\). We therefore assume \(z_0=r\).

Every step in the radial estimate must then be an equality for all \(0<s<r\). In particular,
\[
|\phi'(s)|=U(s),\qquad |\omega(s)|=ks^2,
\qquad \varepsilon\omega(s)=-ks^2.
\]
The last identity extends analytically to \(\omega(z)=-\overline\varepsilon kz^2\). Moreover, write \(\phi(z)=z+a_3z^3+O(z^5)\). Comparing \(|\phi'(s)|=1+3s^2+O(s^4)\) as \(s\downarrow0\) gives \(\operatorname{Re}a_3=1\). The odd coefficient inequality \(|a_3|\le1\) forces \(a_3=1\). To see its equality classification directly, the normalized schlicht function \(\Phi(\zeta)=\phi(\sqrt\zeta)^2\) has second coefficient \(2a_3=2\). Equality in the classical second-coefficient inequality forces \(\Phi(\zeta)=\zeta/(1-\zeta)^2\), and therefore
\[
\phi(z)=\psi(z):=\frac z{1-z^2}.
\]
Set \(\eta=-\overline\varepsilon\). Then \(|\eta|=1\), and equality forces
\[
h'(z)=\frac{\psi'(z)}{1-kz^2},\qquad
g'(z)=\eta\,\frac{kz^2\psi'(z)}{1-kz^2}.
\]
Let \(H_k,G_k\) be the normalized primitives in the theorem, so that \(h=H_k\), \(g=\eta G_k\). For real \(0<r<1\), both \(H_k(r)\) and \(G_k(r)\) are strictly positive when \(k>0\), and \(H_k(r)+G_k(r)=T(k,r)\). Thus
\[
|f(r)|=|H_k(r)+\overline\eta G_k(r)|=T(k,r)
\]
forces \(\eta=1\), hence \(\varepsilon=-1\). Therefore the only possible normalized equality map at a positive real radius is
\[
F_k=H_k+\overline{G_k},\qquad H_k-G_k=\psi.
\]
All other equality maps are its normalized rotations.

**2. Exact global noninjectivity of the equality shear.** Fix \(0<k<1\). The function \(F_k\) is locally orientation-preserving, since
\[
\frac{G_k'(z)}{H_k'(z)}=kz^2,
\qquad J_{F_k}(z)=|H_k'(z)|^2(1-k^2|z|^4)>0.
\]
But \(F_k\) is not globally injective.

The conformal map \(\psi(z)=z/(1-z^2)\) sends \(\mathbb D\) onto the plane slit along the two rays
\[
\{iy:y\ge1/2\}\quad\text{and}\quad\{iy:y\le-1/2\}.
\]
Write \(w=\psi(z)=x+iy\). Because \(H_k-G_k=\psi\),
\[
F_k(z)=w+2\operatorname{Re}G_k(z),
\qquad \operatorname{Im}F_k(z)=y.
\]
For \(0<t<\pi/2\), both boundary points \(z_+=e^{it}\) and \(z_-=-e^{-it}\) map under \(\psi\) to \(iy\), where \(y=1/(2\sin t)>1/2\). The analytic function \(G_k\) extends across these boundary points. Its defining derivative gives
\[
\frac{d}{dt}\operatorname{Re}G_k(e^{it})
=\frac{\cos t}{2\sin^2t}\,
\operatorname{Im}\left(\frac{ke^{2it}}{1-ke^{2it}}\right)
=\frac{k\cos t\sin(2t)}{2\sin^2t\bigl(1-2k\cos(2t)+k^2\bigr)}>0.
\]
Since \(G_k(i)\) is purely imaginary, \(\operatorname{Re}G_k(e^{it})<0\). The real Taylor coefficients of \(G_k\) also yield \(G_k(-e^{-it})=-\overline{G_k(e^{it})}\), so the corresponding real part at \(z_-\) is positive.

Fix any \(y>1/2\). The horizontal line at height \(y\) has two components in \(\psi(\mathbb D)\), with \(x<0\) and \(x>0\). Along each component, with \(z=\psi^{-1}(x+iy)\), the real part of \(F_k\) is strictly increasing in \(x\):
\[
\frac{\partial}{\partial x}\operatorname{Re}F_k(\psi^{-1}(x+iy))
=1+2\operatorname{Re}\frac{kz^2}{1-kz^2}
=\frac{1-k^2|z|^4}{|1-kz^2|^2}>0.
\]
As \(x\to0^+\), the real part tends to \(2\operatorname{Re}G_k(e^{it})<0\), while as \(x\to0^-\) it tends to its positive opposite. As \(x\to\pm\infty\), the real part tends to \(\pm\infty\), because \(z\to\pm1\) and
\[
\frac{dG_k}{dw}=\frac{kz^2}{1-kz^2}\longrightarrow\frac{k}{1-k}.
\]
By continuity and strict monotonicity, one point on the right and one on the left both map under \(F_k\) to \(iy\). They are distinct points of \(\mathbb D\), proving noninjectivity for every \(k>0\). At \(k=0\), \(F_0=\psi\) is schlicht.

**3. Why the gap is genuinely strict.** We verify compactness rather than assuming it. The derivative estimates in step 1 are uniform on every smaller disk, so any sequence \(f_j=h_j+\overline{g_j}\) in \(\mathcal F_k\) has a subsequence for which \(h_j\to h\), \(g_j\to g\) locally uniformly. The witnessing phases have a convergent subsequence \(\varepsilon_j\to\varepsilon\); the normalized odd schlicht maps \(\phi_j=h_j+\varepsilon_jg_j\) converge to the normalized odd schlicht map \(\phi=h+\varepsilon g\), by the classical compactness theorem for normalized analytic univalent functions. The analytic dilatations also have a convergent subsequence \(\omega_j\to\omega\) with \(|\omega|\le k\); since \(\phi'=h'(1+\varepsilon\omega)\) and \(\phi'\ne0\), the limiting analytic derivative \(h'\) is nonzero and the limiting harmonic map has positive Jacobian.

This locally orientation-preserving limit is also globally injective. If two distinct interior points had the same image \(w\), choose disjoint small disks about them on which the limiting map is an orientation-preserving local diffeomorphism and whose boundaries avoid \(w\). The topological degree of the map about \(w\) is one on each disk. Local uniform convergence preserves both degrees, so for all large \(j\) the injective map \(f_j\) would have a preimage of \(w\) in each disk, a contradiction. Thus \(\mathcal F_k\) is sequentially compact, and \(M(k,r)\) is achieved.

If \(M(k,r)=T(k,r)\) for \(k>0\), an extremizer would, by step 1, be a normalized rotation of \(F_k\), contradicting its noninjectivity from step 2. Thus \(M(k,r)<T(k,r)\) at every positive radius. At \(k=0\), \(g\equiv0\), and \(\psi\in\mathcal F_0\) attains \(T(0,r)=r/(1-r^2)\).

Finally, the relaxed locally orientation-preserving family retains the same derivative bounds, and \(F_k\) itself belongs to it and attains \(T(k,r)\) along the positive real radius. Step 1 classifies its normalized equality maps. This completes the dichotomy.

## Verification

The proof is algebraic and geometric; the critical boundary identity can be replayed by differentiating
\[
\psi(e^{it})=\frac{i}{2\sin t},\qquad
G_k'(z)=\frac{kz^2\psi'(z)}{1-kz^2}.
\]
The exact positivity of the resulting derivative is independent of numerical experiments. Its strictness on \((0,\pi/2)\) is all that is needed to establish the overlap on every slit height \(y>1/2\).

As a consistency check only, at \(k=1/2\) and \(y=1\), numerical inversion of \(\psi\) and quadrature of \(G_k'\) give distinct preimages near \(\pm0.7552608658+0.3671083730i\), both mapped by \(F_k\) to approximately \(i\). The exact proof does not depend on these decimals.

The strictness for the original class uses compactness, not a numerical search for its maximum.

## Relationship to prior work

Parashar--Ponnusamy--Kaliraj's 2026 paper, Theorem 6, proves the same upper bound \(T(k,r)\) for the same odd, univalent quasiconformal harmonic class and describes it as sharp via a vertical shear of \(\psi\) with dilatation \(-kz^2\). Their construction is a valid univalent shear; however, the equality analysis above shows that saturation instead forces the opposite dilatation \(+kz^2\) with the analytic combination \(h-g=\psi\). That opposite shear is locally sense-preserving but globally noninjective. The article does not identify this obstruction or the resulting strict inequality for its stated class.

Jaglan--Sairam Kaliraj (2024) studies odd harmonic univalent maps, gives the vertical shear at the limiting dilatation, and proves coefficient and Hardy-space results. Its inspected initial main theorems do not classify finite-\(K\) growth equality or the collision phenomenon of the opposite shear. The classical Clunie--Sheil-Small shear theorem explains why matching a chosen convex direction can guarantee univalence, but does not show that a shear in the wrong direction is globally injective.

Searches for the exact source envelope, the two opposite shears, univalence/nonunivalence of the formal extremizer, and compactness-induced sharpness gaps did not locate an implication-equivalent earlier published statement.

## Limitations

No explicit formula or uniform lower bound is claimed for the positive gap \(T(k,r)-M(k,r)\). The gap may tend to zero when \(k\downarrow0\), and the proof does not control this rate.

The result concerns the normalized odd class with an analytic univalent combination. It does not rule out sharpness of other growth estimates for larger or geometrically different harmonic classes.

The locally orientation-preserving equality maps are not globally univalent when \(k>0\). Local nonvanishing of the Jacobian alone is not sufficient for global injectivity.

## References

1. J. Parashar, S. Ponnusamy, and A. Sairam Kaliraj, *Coefficients and integral mean estimates for K-quasiconformal harmonic mappings*, publicly available author manuscript, May 27, 2026, DOI: 10.13140/RG.2.2.36457.45921; arXiv:2608.28121v1 (August 28, 2026), especially Theorem 6 and its proof.
2. K. Jaglan and A. Sairam Kaliraj, *On odd univalent harmonic mappings*, Analysis and Mathematical Physics 14 (2024), Article 106, DOI: 10.1007/s13324-024-00964-5.
3. J. Clunie and T. Sheil-Small, *Harmonic univalent functions*, Annales Academiae Scientiarum Fennicae Series A I Mathematica 9 (1984), 3–25.
4. P. L. Duren, *Univalent Functions*, Springer, 1983, standard distortion and coefficient results for odd univalent analytic functions.
