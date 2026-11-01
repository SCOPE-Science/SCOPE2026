# A sharp eccentricity transition in a degenerating family of harmonic-convolution counterexamples

## Finding

Let \(B_r(z)=(z-r)/(1-rz)\) for real \(-1<r<1\). Fix \(0<k<1/4\) and, for sufficiently small \(\varepsilon>0\), put \(a=-1+\varepsilon\), \(b=k\varepsilon\), and
\[
\Gamma_{\varepsilon,k}(z)=z\frac{B_a(z)}{B_b(z)},\qquad |z|=1.
\]
Write \(U_{\varepsilon,k}\) for its harmonic Poisson extension and \(c_j\) for its real Fourier coefficients. Let \(\Delta=c_1^2-c_{-1}^2\), and define
\[
 f_{\varepsilon,k}(z)=\frac{c_1\{U_{\varepsilon,k}(z)-c_0\}-c_{-1}\overline{\{U_{\varepsilon,k}(z)-c_0\}}}{\Delta}.
\]
Then \(f_{\varepsilon,k}=h_{\varepsilon,k}+\overline{g_{\varepsilon,k}}\) is a normalized, sense-preserving harmonic diffeomorphism of the disk onto a bounded convex ellipse: \(h(0)=g(0)=0\), \(h'(0)=1\), and \(g'(0)=0\). Its major/minor semiaxis ratio tends to \(E(k)=1/(1-k)\).

The harmonic Hadamard self-convolution \(F_{\varepsilon,k}=h_{\varepsilon,k}*h_{\varepsilon,k}+\overline{g_{\varepsilon,k}*g_{\varepsilon,k}}\) converges locally uniformly on the unit disk to the explicit rational harmonic map
\[
 F_d(z)=z+(1+d)^2\frac{z^2}{1-z}+\overline{d^2\frac{z^2}{1-z}},\qquad d=\frac{k}{2(1-k)}.
\]
Its Jacobian is strictly positive at every interior point if and only if
\[
 k\le k_c:=1-\sqrt{\frac35}\quad\Longleftrightarrow\quad E(k)\le\sqrt{\frac53}.
\]
For every \(k_c<k<1/4\), the limiting Jacobian is negative somewhere on the negative real radius; at that fixed interior point the Jacobian of \(F_{\varepsilon,k}\) is also negative for all sufficiently small \(\varepsilon>0\). Since the latter is positive at the origin, each corresponding bounded-ellipse self-convolution fails local injectivity. Consequently, for every \(\eta>0\) there is such a counterexample with ellipse axis ratio strictly between \(\sqrt{5/3}\) and \(\sqrt{5/3}+\eta\). The critical ratio is sharp **for the stated singular limiting family**, not a universal lower bound for all harmonic counterexamples.

One entirely rational finite witness is \(k=23/100\), \(\varepsilon=1/100\), with ellipse ratio
\[
 E_{\varepsilon,k}=\frac{6030299371723}{4647100628277}<\frac{13}{10}.
\]
At \(z=-99/100\), its self-convolution analytic and coanalytic derivatives satisfy \(15/1000<p'(z)<16/1000\) and \(-17/1000<q'(z)<-16/1000\). Thus its Jacobian is negative, whereas its Jacobian at zero equals one.

## Assumptions and scope

The input circle map is the explicit real two-Blaschke quotient above; \(k\) is fixed in \((0,1/4)\), while \(\varepsilon\downarrow0\). Each finite positive \(\varepsilon\) defines a bounded ellipse, but the limiting rational map does **not** itself have a bounded target. Convolution is coefficientwise in the analytic and coanalytic Taylor components. The classification concerns the Jacobian of the displayed limit, and yields bounded-ellipse failure by strict negativity and compact convergence; it does not classify all convex harmonic mappings or all ellipses.

## Proof

**1. Circle orientation and bounded convex images.** For \(x=\cos t\), differentiate the argument of \(\Gamma\):
\[
 \frac{d}{dt}\arg\Gamma(e^{it})=1+\frac{1-a^2}{1-2ax+a^2}-\frac{1-b^2}{1-2bx+b^2}.
\]
Multiplication by the positive product of denominators gives the quadratic
\[
 N(x)=4abx^2-4b(ab+1)x+a^2b^2-a^2+3b^2+1.
\]
Since \(ab<0\), this quadratic is strictly concave, so its minimum on \([-1,1]\) occurs at an endpoint. Exact factorizations are
\[
 N(-1)=(a+1)(b+1)(ab-a+3b+1),
 \qquad N(1)=(a-1)(b-1)(ab+a-3b+1).
\]
After substituting \(a=-1+\varepsilon\), \(b=k\varepsilon\), the last factors become, respectively, \(2+(2k-1)\varepsilon+k\varepsilon^2\) and \((1-4k)\varepsilon+k\varepsilon^2\), both positive when \(\varepsilon>0\) is small and \(0<k<1/4\). Therefore the angle derivative is positive throughout the circle. As the winding degree is \(1+1-1=1\), \(\Gamma\) is an orientation-preserving circle diffeomorphism. The Radó–Kneser–Choquet theorem makes its Poisson extension a sense-preserving harmonic diffeomorphism onto the disk.

**2. Fourier coefficients, ellipse and normalization.** Partial fractions on \(b<|z|<1/|a|\) give the real Fourier coefficients
\[
 c_1=\frac{a^2-ab+b^2-1}{ab-1},\quad
 c_{-1}=\frac{-b(a-b)(b^2-1)}{ab-1},\quad
 c_2=\frac{(a^2-1)(a-b)}{ab-1},
\]
with \(c_n=c_2a^{n-2}\) and \(c_{-n}=c_{-1}b^{n-1}\) for integers \(n\ge2\). As \(\varepsilon\downarrow0\),
\[
 c_1=(2-k)\varepsilon+O(\varepsilon^2),\quad
 c_{-1}=k\varepsilon+O(\varepsilon^2),\quad
 c_2=-2\varepsilon+O(\varepsilon^2),\quad
 \Delta=4(1-k)\varepsilon^2+O(\varepsilon^3).
\]
Hence \(c_1>c_{-1}>0\) and \(\Delta>0\) for sufficiently small \(\varepsilon\). The real-affine expression defining \(f\) is an orientation-preserving automorphism postcomposed with the Poisson disk diffeomorphism. Its real and imaginary scale factors are \(1/(c_1+c_{-1})\) and \(1/(c_1-c_{-1})\), respectively. This proves the ellipse claim, the normalization at zero, and
\[
 \frac{R_y}{R_x}=\frac{c_1+c_{-1}}{c_1-c_{-1}}\longrightarrow\frac1{1-k}.
\]

**3. Limiting convolution.** For every \(n\ge2\), the Taylor coefficients of the normalized analytic and coanalytic parts are
\[
 M_n=A_\varepsilon a^{n-2}+B_\varepsilon b^{n-2},\qquad
 N_n=D_\varepsilon a^{n-2}+C_\varepsilon b^{n-2},
\]
where
\[
 A_\varepsilon=\frac{c_1c_2}{\Delta},\quad B_\varepsilon=-\frac{c_{-1}^2b}{\Delta},\quad
 C_\varepsilon=\frac{c_1c_{-1}b}{\Delta},\quad D_\varepsilon=-\frac{c_{-1}c_2}{\Delta}.
\]
Writing \(d=k/[2(1-k)]\), these tend to \(-(1+d),0,0,d\), respectively. Summing the geometric series, \(h=z+A_\varepsilon z^2/(1-az)+B_\varepsilon z^2/(1-bz)\) and \(g=D_\varepsilon z^2/(1-az)+C_\varepsilon z^2/(1-bz)\). Coefficientwise squaring and summing gives the locally uniform limit \(F_d\) displayed above. In detail, with \(S_r(z)=z(2-rz)/(1-rz)^2\),
\[
 p_\varepsilon'=1+A_\varepsilon^2S_{a^2}+2A_\varepsilon B_\varepsilon S_{ab}+B_\varepsilon^2S_{b^2},\qquad
 q_\varepsilon'=D_\varepsilon^2S_{a^2}+2D_\varepsilon C_\varepsilon S_{ab}+C_\varepsilon^2S_{b^2},
\]
which converge on compact subsets to \(p_d'=1+(1+d)^2 S_1\), \(q_d'=d^2S_1\). These formulas also establish convergence of Jacobians on compact subsets.

**4. Exact phase transition of the limiting Jacobian.** Put \(A_2=(1+d)^2\), \(C=A_2+d^2\), and \(S=S_1(z)=1/(1-z)^2-1\). The Jacobian is \(J_d=|1+A_2S|^2-d^4|S|^2\). The critical condition \(C=4/3\) has the unique positive solution \(d_c=(\sqrt{15}-3)/6\); using \(1+2d=1/(1-k)\), it is equivalent to \(k=k_c=1-\sqrt{3/5}\).

If \(0\le d\le d_c\), then \(A_2\le A_2(d_c)<4/3\). Thus \(p_d'\) has no zeros in the closed unit disk: indeed \(p_d'=0\) would require \(w^2=1-1/A_2<1/4\) for \(w=1/(1-z)\), whereas \(\operatorname{Re}w\ge1/2\) on the closed disk away from \(z=1\). The quotient \(q_d'/p_d'\) is holomorphic in the disk and extends continuously across \(z=1\) with limit \(d^2/A_2\).

For \(z\) on the unit circle other than \(1\), write \(w=1/2+iy\), so \(S=-3/4-y^2+iy\). Direct expansion gives
\[
 J_d(z)=(A_2^2-d^4)y^4+
 \left(\tfrac52(A_2^2-d^4)-2A_2\right)y^2+
 \frac{(6d-1)(6d^2+6d-1)}{16}.
\]
The coefficient of \(y^2\) simplifies to \(\frac12+6d+13d^2+10d^3>0\). For \(0\le d<d_c\), the constant is positive; at \(d=d_c\), it is zero only at \(y=0\), corresponding to \(z=-1\). The maximum-modulus principle for \(q_d'/p_d'\) now gives \(|q_d'/p_d'|<1\) everywhere inside the disk, including at criticality (the quotient is nonconstant). Consequently \(J_d>0\) throughout the open disk for \(d\le d_c\).

Conversely, when \(d>d_c\), choose a real \(x\in(-1,0)\) so that \(t=-S_1(x)\) lies between \(1/C\) and \(\min\{3/4,1/(1+2d)\}\). Such a choice exists because \(C>4/3\) and \(C>1+2d\). Then
\[
 J_d(x)=[1-Ct][1-(1+2d)t]<0.
\]
This proves the exact if-and-only-if classification and, by convergence of the finite-parameter derivatives, the bounded-ellipse counterexamples for every \(k_c<k<1/4\). To obtain ellipses arbitrarily near the critical axis ratio from above, first choose such \(k\) with \(1/(1-k)\) arbitrarily near \(\sqrt{5/3}\), then take \(\varepsilon\) sufficiently small.

**5. Exact finite witness.** For \(k=23/100\), \(\varepsilon=1/100\), \(x=-99/100\), the endpoint factorizations in Step 1 have positive values. Substitution in the exact rational coefficients and the \(S_r\)-derivatives above yields
\[
 \frac{15}{1000}<p_\varepsilon'(x)<\frac{16}{1000},\quad
 -\frac{17}{1000}<q_\varepsilon'(x)<-\frac{16}{1000},\quad
 \frac{R_y}{R_x}=\frac{6030299371723}{4647100628277}<\frac{13}{10}.
\]
All comparisons are exact rational inequalities and reproduced by the standalone checker. Since \(J(0)=1\) but \(J(x)<0\), an intermediate point has zero Jacobian. Lewy's theorem rules out local one-to-one harmonic behavior there.

## Verification

Run \(\texttt{python3 verify.py}\) with the Python standard library. The checker uses exact rational arithmetic to recompute the Fourier coefficients, endpoint orientation signs, normalized two-tail coefficients, ellipse axis ratio, and the negative Jacobian witness. It also checks the rational strict inequalities used above. Its numerical printout is illustrative only. The all-parameter phase diagram and local-uniform convergence are proved analytically in Steps 1–4; no finite grid or numerical experiment is used to certify the continuum statement.

## Relationship to prior work

Wang and Zhong (arXiv:2609.11556, first public 2026-09-10) construct a single normalized convex harmonic ellipse map for which the Hadamard self-square has a negative Jacobian at an interior point. Their 12-page primary paper contains the Blaschke quotient, exact Fourier tails, affine normalization, and fixed-parameter derivative formulas. The present result instead varies both Blaschke parameters in a singular ray and determines a full limiting phase transition, with a smaller explicit ellipse ratio and a geometric accumulation threshold. The earlier paper's formulas provide context, not the eccentricity bifurcation statement.

A separate public fixed-first-parameter calculation locates a Jacobian sign threshold along \(a=-10/11\) while holding the test point fixed; this does not control the simultaneous \(a\to-1\), \(b/(1+a)\to k\) regime. Another two-parameter result concerns a **different**, complex-linear disk normalization whose coanalytic derivative at zero generally does not vanish; it does not imply the real-affine ellipse-normalized self-convolution law proved here. Earlier harmonic convolution literature establishes important preservation results under additional assumptions, but none of the inspected statements supplies this limiting threshold.

## Limitations

The threshold \(\sqrt{5/3}\) is sharp for the displayed singular family and limiting rational maps; it is **not** a theorem that every harmonic self-convolution counterexample must have ellipse ratio at least this number. For \(k\le k_c\), positivity is established for the **limiting map** \(F_d\); no disk-wide preservation theorem for the finite \(F_{\varepsilon,k}\) at those values is claimed. The finite exact example and counterexample regime do not imply a globally optimal ellipse shape. Historical priority for hidden equivalent specializations has not been independently settled. No independent mathematical audit has been performed.

## References

1. Zhi-Gang Wang and Deguang Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1 (submitted 2026-09-10), especially §§3–8 and the concluding remarks. Full open-access PDF: https://pdfs.assets.alphaxiv.org/2609.11556v1.pdf.
2. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables Theory Appl. **45** (2001), 263–271. Historical source of the bounded-convex question, as referenced by Wang–Zhong.
3. J. Clunie and T. Sheil-Small, *Harmonic univalent functions*, Ann. Acad. Sci. Fenn. Ser. A I Math. **9** (1984), 3–25.
4. Public published-finding corpus mathematical record, *Exact parameter threshold for the Dorff counterexample’s rational witness* (2026), record `e20d7884e72b` (metadata-level comparison; complete text not independently inspected).
5. Public mathematical record, *Global univalence of disk-normalized Blaschke-quotient harmonic convolution squares* (2026), finding identifier `dd1deefa-c28f-420b-9cd2-a1a904ea01e2` (different normalization).
