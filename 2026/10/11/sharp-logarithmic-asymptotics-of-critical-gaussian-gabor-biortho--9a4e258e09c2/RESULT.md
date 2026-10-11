# Sharp logarithmic asymptotics of critical Gaussian Gabor biorthogonals

## Finding

Let
\[
g(t)=e^{-\pi t^2},
\qquad
g_{m,n}(t)=e^{2\pi int}g(t-m),
\qquad (m,n)\in\mathbb Z^2.
\]
For a fixed deleted lattice atom \((a,b)\), the system
\[
\{g_{m,n}:(m,n)\in\mathbb Z^2\setminus\{(a,b)\}\}
\]
is complete and minimal in \(L^2(\mathbb R)\), and has a unique biorthogonal family \(\{\gamma_{m,n,a,b}\}\).

**Theorem.** There is a universal finite constant \(B\) such that, for every \((a,b)\in\mathbb Z^2\) and every \((m,n)\ne(a,b)\), writing
\[
R=\sqrt{(m-a)^2+(n-b)^2}\ge1,
\]
one has
\[
\left|
\|\gamma_{m,n,a,b}\|_{L^2(\mathbb R)}^2
-C_{\mathrm G}\log R
\right|\le B,
\qquad
C_{\mathrm G}=\frac{4}{\pi|\theta_1'(0,e^{-\pi})|^2}.
\]
Here the Jacobi theta function is normalized by
\[
\theta_1(z,q)=-i\sum_{k\in\mathbb Z}(-1)^k q^{(k+1/2)^2}e^{(2k+1)iz}
\]
and
\[
\theta_1'(0,e^{-\pi})
=2\sum_{k=0}^{\infty}(-1)^k(2k+1)e^{-\pi(k+1/2)^2}>0.
\]
Numerically,
\[
C_{\mathrm G}\approx1.54852449005.
\]
Consequently
\[
\lim_{R\to\infty}
\frac{\|\gamma_{m,n,a,b}\|_2^2}{\log R}
=C_{\mathrm G}
\]
uniformly in the deleted atom and lattice direction. In particular,
\[
\|\gamma_{m,n,a,b}\|_2^2\asymp\log(e+R).
\]
This proves the logarithmic biorthogonal-norm conjecture formulated in the cited 2026 article and identifies the sharp leading constant.

## Assumptions and scope

The time-frequency shifts have unit lattice spacing and the **unnormalized** Gaussian \(g(t)=e^{-\pi t^2}\), exactly as in the 2026 source. The earlier 2025 paper uses the unit-norm Gaussian \(2^{1/4}g\); its Zak derivative is divided by \(2^{1/4}\) when used here.

The norms and the asymptotic are those of the unique \(L^2\) biorthogonal family after **one** lattice atom is removed. The result is uniform in every deleted lattice point. It does not assert the deleted system is a Riesz basis or a Schauder basis, nor does it determine optimal weights for every conceivable lower semi-frame.

The Zak transform is
\[
Zh(x,\xi)=\sum_{k\in\mathbb Z}h(x-k)e^{2\pi i k\xi},
\qquad (x,\xi)\in Q=[0,1)^2.
\]
It is unitary from \(L^2(\mathbb R)\) onto \(L^2(Q)\). The lattice Gabor transform identity is
\[
Zg_{m,n}(x,\xi)
=e^{2\pi i(nx-m\xi)}Zg(x,\xi).
\]

## Proof

**Step 1: The exact dual under the Zak transform.** Set
\[
E_{m,n}(x,\xi)=e^{2\pi i(nx-m\xi)},
\qquad p=(1/2,1/2).
\]
For \((m,n)\ne(0,0)\) define
\[
U_{m,n}(x,\xi)
=\frac{E_{m,n}(x,\xi)-E_{m,n}(p)}{\overline{Zg(x,\xi)}}
=\frac{E_{m,n}(x,\xi)-(-1)^{m+n}}{\overline{Zg(x,\xi)}}.
\]
The Gaussian Zak transform has exactly one zero on the fundamental square, at \(p\), and that zero is simple; this is verified explicitly in Step 2. The numerator vanishes at \(p\), so \(U_{m,n}\in L^2(Q)\). Moreover, for every \((r,s)\ne(0,0)\), orthogonality of distinct characters on \(Q\) gives
\[
\big\langle E_{r,s}Zg,U_{m,n}\big\rangle_{L^2(Q)}
=\int_Q E_{r,s}(\overline{E_{m,n}}-\overline{E_{m,n}(p)})\,dx\,d\xi
=\delta_{(r,s),(m,n)}.
\]
Here the Hilbert inner product is linear in its first entry. Since the system after deletion is complete and minimal, its biorthogonal family is unique. Thus
\[
Z\gamma_{m,n,0,0}=U_{m,n}.
\]
Unitarity therefore gives the exact identity
\[
\|\gamma_{m,n,0,0}\|_2^2
=\int_Q
\frac{|E_{m,n}(x,\xi)-(-1)^{m+n}|^2}
{|Zg(x,\xi)|^2}\,dx\,d\xi.
\tag{1}
\]

**Step 2: The only singularity is isotropic and simple.** For
\[
q=e^{-\pi},\qquad u=x-1/2,\qquad v=\xi-1/2,
\]
the classical theta representation of the Gaussian Zak transform gives the first-order Taylor expansion
\[
Zg(p+(u,v))
=-\pi\theta_1'(0,q)(u+iv)+O(u^2+v^2).
\tag{2}
\]
The series defining \(\theta_1'(0,q)\) is a strictly alternating series with strictly decreasing positive terms; hence it is positive. Alternatively, the standard theta product gives the same nonvanishing. The theta expression shows that \(p\) is the only zero in \(Q\). Set
\[
\kappa=\pi\theta_1'(0,e^{-\pi})>0,
\qquad r=\sqrt{u^2+v^2}.
\]
Equation (2) implies
\[
|Zg(p+(u,v))|^2=\kappa^2 r^2+O(r^3).
\]
For sufficiently small fixed \(\rho\in(0,1/2)\), uniformly on \(0<r<\rho\),
\[
\left|\frac1{|Zg|^2}-\frac1{\kappa^2 r^2}\right|\le\frac{A}{r}
\tag{3}
\]
with an absolute finite constant \(A\). On the compact complement of the \(\rho\)-disk in \(Q\), \(|Zg|\) is bounded away from zero.

**Step 3: Uniform oscillatory integral asymptotics.** Since
\[
|E_{m,n}-(-1)^{m+n}|^2\le4,
\]
equation (3) and the bounded contribution from the complement imply that (1) differs by at most a **universal** additive constant from
\[
\frac1{\kappa^2}
\int_{u^2+v^2<\rho^2}
\frac{|e^{2\pi i(nu-mv)}-1|^2}{u^2+v^2}\,du\,dv.
\]
Set
\[
R=\sqrt{m^2+n^2}\ge1.
\]
Rotating polar coordinates to align their angular axis with \((n,-m)\), and defining the Bessel average
\[
J_0(t)=\frac1{2\pi}\int_0^{2\pi}\cos(t\cos\vartheta)\,d\vartheta,
\]
the last integral is exactly
\[
\frac{4\pi}{\kappa^2}
\int_0^\rho\frac{1-J_0(2\pi Rr)}{r}\,dr
=\frac{4\pi}{\kappa^2}
\int_0^{2\pi R\rho}\frac{1-J_0(t)}t\,dt.
\tag{4}
\]
The Taylor expansion of the cosine average gives
\[
1-J_0(t)=O(t^2)
\quad (0<t\le1).
\]
The oscillatory integral representation, splitting at neighborhoods of the two stationary points and integrating by parts elsewhere, gives
\[
|J_0(t)|\le C t^{-1/2}
\quad(t\ge1).
\]
It follows that
\[
\int_0^L\frac{1-J_0(t)}t\,dt=\log L+O(1)
\quad (L\to\infty).
\]
Putting this into (4) and then into (1) proves
\[
\|\gamma_{m,n,0,0}\|_2^2
=\frac{4\pi}{\kappa^2}\log R+O(1)
=\frac4{\pi|\theta_1'(0,e^{-\pi})|^2}\log R+O(1),
\]
with an error bound independent of the lattice direction. The finitely many remaining small radii can be absorbed in the same universal additive constant.

**Step 4: Any deleted lattice atom.** Integer time-frequency shifts commute up to the phase
\[
e^{2\pi i\ell}=1\quad(\ell\in\mathbb Z).
\]
The unitary operator \(M_bT_a\) therefore sends the system with \(g_{0,0}\) deleted bijectively onto the system with \(g_{a,b}\) deleted and carries its unique biorthogonal family onto the new one, up to harmless unit phases. Consequently
\[
\|\gamma_{m,n,a,b}\|_2
=\|\gamma_{m-a,n-b,0,0}\|_2.
\]
The estimate from Step 3 is therefore uniform also in the deleted atom. This proves the theorem.

## Verification

The proof uses exact Zak unitarity, the explicit biorthogonal formula, a nonzero first-order theta coefficient, and a classical oscillatory Bessel integral. Each step is stated above with its normalization. In particular, the **unscaled** Gaussian derivative is \(\pi\theta_1'(0,e^{-\pi})\), not the derivative for the unit-norm Gaussian.

An independent vectorized numerical consistency check approximated the integral (1) on a uniform midpoint grid. For deletion of the origin, the values at \((m,n)=(20,0),(40,0),(80,0)\) were approximately \(7.394044,8.467403,9.540806\), respectively. Subtracting \(C_{\mathrm G}\log R\) gave approximately \(2.755079,2.755083,2.755131\), consistent with a direction-uniform bounded remainder. The exact theorem does **not** rely on these samples. The optional checker file documents the numerical procedure; the proof works for all lattice indices without enumeration.

## Relationship to prior work

Zikkos (2026) proves that the critical-density Gaussian Gabor system is a weighted lower semi-frame. His Theorem 1.1 gives a sufficient condition in terms of the squared norms of the unique dual vectors after deletion of one atom. **Conjecture 4.1** predicts precisely the two-sided logarithmic order for deletion at the origin, and explicitly says the estimates have not been verified. The theorem above proves the conjecture, computes its sharp leading coefficient and makes the bound uniform over all deleted atoms.

Hart, Heil, Katz and Northington (2025) prove that deleting one atom produces an exact, non-Schauder system. Their Section 4 contains the Zak character quotient and the theta expansion at its simple zero. Those formulas are **foundational inputs** and are not presented here as discoveries. Their article does not state a quantitative asymptotic for the individual biorthogonal norms. The additional argument here turns the exact quotient into a uniform logarithmic asymptotic through a singular oscillatory integral and angular Bessel averaging.

In combination with Zikkos's sufficient criterion, the norm asymptotic makes its summability hypothesis equivalent to
\[
\sum_{(m,n)\ne(a,b)}
\frac{\log(e+\sqrt{(m-a)^2+(n-b)^2})}{c_{m,n}^2}<\infty.
\]
For instance, the explicit weights
\[
c_{m,n}=\sqrt{1+R^2}\,\bigl[\log(e+R)\bigr]^{1+\varepsilon},
\qquad\varepsilon>0,
\]
satisfy this condition. This equivalence concerns the **specific sufficient criterion**, not a claim that every lower semi-frame weight must obey it.

## Limitations

The result concerns the square integer lattice at critical density, the Gaussian window and deletion of exactly one atom. It does not prove optimality of any choice of weights among all lower semi-frame constructions.

The asymptotic has an additive bounded error. No explicit limiting additive constant is asserted. The uniformity refers to the lattice indices and deleted atom; it is not a statement over all Gaussian shapes or lattice covolumes.

The displayed numerical values are consistency checks only and are not used to establish the infinite-lattice theorem.

## References

1. E. Zikkos, *The Gaussian Gabor system at the critical density is a weighted lower semi frame*, arXiv:2606.00764v1, first publicly posted 30 May 2026, especially Theorem 1.1 and Conjecture 4.1.
2. L. Hart, C. Heil, I. Katz, and M. Northington V, *Overcomplete Reproducing Pairs*, Journal of Fourier Analysis and Applications **31** (2025), article 58, DOI: 10.1007/s00041-025-10190-7, especially Section 4 and Corollary 4.3.
3. P. Balazs, R. Corso, and D. Stoeva, *Weighted frames, weighted lower semi frames and unconditionally convergent multipliers*, Journal of Fourier Analysis and Applications **32** (2026), article 24.
