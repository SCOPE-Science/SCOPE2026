# Sharp phase-only sixth moments on characteristic-three finite parabolas

## Finding
Let \(F=\mathbb F_q\), where \(q=3^d\) and \(d\ge2\), and fix a nontrivial additive character \(\psi:F\to\mathbb S^1\). For every function \(h:F\to\mathbb S^1\) define
\[
P_h(x,y)=q^{-1/2}\sum_{t\in F}h(t)\psi(xt+yt^2),\qquad
\mathcal M(h)=q^{-2}\sum_{x,y\in F}|P_h(x,y)|^6.
\]
Then the **sharp phase-only sixth-moment inequality** is
\[
\boxed{\mathcal M(h)\le q+1-q^{-1}.}
\]
Equality holds if and only if there are \(\lambda\in\mathbb S^1\) and \(\alpha,\beta\in F\) such that
\[
h(t)=\lambda\psi(\alpha t+\beta t^2)\quad\text{for every }t\in F.
\]
There are exactly \(q^2\) equality classes after division by a common unimodular factor. The theorem is valid for every extension degree \(d\ge2\). It does **not** assert the unrestricted sharp \(L^2\to L^6\) inequality for nonconstant-modulus inputs.

## Assumptions and scope
All sums are over the finite field \(F\), including non-prime extensions; \(\psi\) has image the cubic roots of unity. The norm on the Fourier side is normalized counting measure on \(F^2\); the input restriction is pointwise \(|h(t)|=1\). An equality class identifies \(h\) and \(\zeta h\) for any \(\zeta\in\mathbb S^1\). The characteristic-three base-field case \(q=3\) is already covered by a known three-frequency classification and is excluded from the asserted new range. The primary MSC field is harmonic-analysis Fourier restriction, 42B05.

## Proof
**1. An exact convolution identity.** For \(s,u\in F\) put
\[
\mathcal F_{s,u}=\{(a,b,c)\in F^3:a+b+c=s,\ a^2+b^2+c^2=u\},
\quad T_h(s,u)=\sum_{(a,b,c)\in\mathcal F_{s,u}}h(a)h(b)h(c).
\]
Expand the cube of \(P_h\) and apply orthogonality of additive characters on \(F^2\):
\[
\mathcal M(h)=q^{-3}\sum_{s,u\in F}|T_h(s,u)|^2.
\]
To determine the fiber sizes, set \(w=a+b\), \(v=a-b\), and \(c=s-w\). Since \(2\) is invertible and \(3=0\) in \(F\), the second fiber equation becomes
\[
u=s^2+sw-v^2.
\]
If \(s\ne0\), each \(v\in F\) fixes one \(w\), hence exactly \(q\) ordered triples. If \(s=0\), the fiber has \(q\) elements when \(u=0\), \(2q\) when \(-u\) is a nonzero square, and zero otherwise. In particular, \(\mathcal F_{0,0}=\{(t,t,t):t\in F\}\). Therefore
\[
\sum_{s,u}|\mathcal F_{s,u}|^2
=q(q-1)q^2+q^2+\frac{q-1}{2}(2q)^2
=q^4+q^3-q^2.
\]
Because \(|h|=1\), the triangle inequality \(|T_h(s,u)|\le|\mathcal F_{s,u}|\) proves the sharp bound. It is attained by \(h\equiv1\); indeed, by any displayed quadratic phase, since the triple product equals \(\lambda^3\psi(\alpha s+\beta u)\) on every fiber.

**2. Equality forces ternary phases.** All summands \(|T_h(s,u)|^2\) are individually bounded, so equality in their sum forces every product \(h(a)h(b)h(c)\) to be constant within its nonempty fiber. In particular, \(\mathcal F_{0,0}\) gives \(h(t)^3=h(0)^3\) for every \(t\). Divide by \(h(0)\) and choose a primitive cube root \(\omega\), writing \(h(t)=\omega^{\varphi(t)}\) with \(\varphi:F\to\mathbb F_3\) and \(\varphi(0)=0\).

Translating an ordered triple \((x,y,-x-y)\) by any \(a\in F\) leaves both its sum and its squared-sum unchanged in characteristic three. Hence, for the difference function \(k_a(t)=\varphi(t+a)-\varphi(t)\), equality of fiber phases says
\[
k_a(x)+k_a(y)+k_a(-x-y)=0.
\]
Using the same equation at \((x,0,-x)\) and \((0,0,0)\), one obtains \(k_a(x+y)=k_a(x)+k_a(y)-k_a(0)\). Consequently
\[
B(a,t)=\varphi(a+t)-\varphi(a)-\varphi(t)
\]
is additive in \(t\) for every \(a\). Symmetry makes \(B:F\times F\to\mathbb F_3\) a symmetric \(\mathbb F_3\)-bilinear form. With \(Q(t)=\tfrac12B(t,t)\), the map \(\ell(t)=\varphi(t)-Q(t)\) is additive, and \(\varphi=Q+\ell\).

**3. The nonsingular fibers force the multiplication form.** For any triple \((x,y,z)\) with \(s=x+y+z\ne0\), let \(e=xy+xz+yz\) and \(v=-e/s\). The repeated-entry triple \((v,v,s+v)\) has the same sum \(s\) and the same squared-sum as \((x,y,z)\), because its second elementary symmetric polynomial is \(-sv=e\) and \(s^2=(x^2+y^2+z^2)+2e\). Thus fiber-phase equality gives
\[
\varphi(x)+\varphi(y)+\varphi(z)=2\varphi(v)+\varphi(s+v).
\]
Take \((x,y,z)=(t,1-t,0)\), so \(s=1\) and \(v=t^2-t\). The additive terms cancel. Expanding \(Q(a+b)=Q(a)+Q(b)+B(a,b)\) gives \(B(t,t)=B(1,t^2)\). Set \(L(w)=B(1,w)\), an additive functional. Polarizing the identity \(B(t,t)=L(t^2)\) yields
\[
2B(a,b)=L(2ab),\quad\text{hence}\quad B(a,b)=L(ab).
\]
The nondegenerate trace pairing on \(F/\mathbb F_3\) gives a unique \(\gamma\in F\) with \(L(w)=\operatorname{Tr}_{F/\mathbb F_3}(\gamma w)\). Likewise \(\ell(t)=\operatorname{Tr}(\delta t)\) for some \(\delta\in F\). Therefore
\[
\varphi(t)=\operatorname{Tr}(\delta t+\tfrac12\gamma t^2).
\]
Every nontrivial additive character of \(F\) is \(t\mapsto\omega^{\operatorname{Tr}(ct)}\) with \(c\ne0\); absorbing \(c\) into the two parameters proves the claimed form of \(h\).

**4. Counting classes.** Normalize \(h(0)=1\). Two functions \(\psi(\alpha t+\beta t^2)\) agree for all \(t\) only if their corresponding additive quadratic functions agree. Polarization gives zero bilinear form \(\operatorname{Tr}(2\beta st)\) and hence \(\beta=0\); the remaining trace linear form forces \(\alpha=0\). Thus the \(q^2\) parameter pairs are distinct modulo scalar.

## Verification
The standalone `verify.py` constructs \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\) as exact polynomial quotients. It exhaustively enumerates all triple fibers, verifies their complete size distribution and the fourth-degree energy identity, and computes the exact mod-three linear rank of all fiber-phase constraints. The nullities are respectively \(3,5,7\), matching \(1+2d\). It then checks quadratic phase alignment for all parameter pairs over \(\mathbb F_3,\mathbb F_9\) and five representatives over \(\mathbb F_{27}\). No floating-point arithmetic is used. This finite verification is corroborative; Steps 1–4 prove the general result.

## Relationship to prior work
González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (arXiv:2405.16647, first posted 26 May 2024), Theorem 1.3, prove a global sharp \(L^2\to L^6\) inequality for the finite parabola only when the characteristic exceeds three. Their Theorem 1.2 concerns the different paraboloid \(L^4\) problem. The present result concerns exclusively unimodular data, but covers **characteristic three in every extension degree at least two** and classifies its full phase-rigid maximizing family. Published related results establish the three-mode case (which covers \(q=3\)), local Hessian rigidity in characteristic three, and full extremizers for primes at least five; none of these statements imply this global phase-only classification for \(q=3^d\), \(d\ge2\).

## Limitations
The theorem does not optimize over arbitrary complex inputs with nonconstant modulus and does not establish a field-uniform quantitative stability inequality or a noise-robust reconstruction guarantee. The complete algebraic rigidity argument relies on characteristic three and does not extend verbatim to characteristic two or five. Earlier equivalent results might be indexed under finite-field Strichartz equality, Freiman characters, or additive quadratic phase functions; searches and the inspected sources do not constitute a proof of worldwide uniqueness. Independent external review has not been performed.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, publicly posted 2024-05-26, Theorems 1.2–1.3 and §6, https://arxiv.org/html/2405.16647v2.
2. *Exact local sixth-moment stability of the parabola in characteristic three*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-sixth-moment-stability-of-the-parabola-in-characteri--158763dab4f3 (local Hessian only).
3. *Sharp sixth Fourier moments for three parabolic modes in every odd characteristic*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-fourier-moments-for-three-parabolic-modes-in-every-o--52302cf3414e (three-mode comparison).
4. *Complete sixth-moment extremizers on the prime-field parabola*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-sixth-moment-extremizers-on-the-prime-field-parabola--a84363193055 (prime characteristic at least five).
