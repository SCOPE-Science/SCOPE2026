# Exact endpoint Fourier norm of quartic residues in the nonreal period regime

## Finding
Let \(p\equiv5\pmod8\) be prime and \(H=(\mathbb F_p^\times)^4\subset\mathbb Z_p^\times\). Let \(P_H\) be the Fourier projection onto the characters indexed by \(H\), acting on complex functions on \(\mathbb Z_p\). There is a unique signed integer \(a\equiv1\pmod4\) and a positive integer \(b\) with \(p=a^2+4b^2\). Define
\[U_p=3p+1+2(a-1)\sqrt p,\qquad V_p=3p+1-2(a-1)\sqrt p.\]
Both are strictly positive. The exact sharp endpoint norm is
\[\boxed{\|P_H\|_{\ell^\infty\to\ell^\infty}=\|P_H\|_{\ell^1\to\ell^1}=\frac{p-1}{4p}\left(1+\frac{\sqrt{U_p}+\sqrt{V_p}}2\right).}\]
In particular this is a closed arithmetic formula (with no unevaluated exponential sums) for every prime in the nonreal quartic-period regime. Its scale is \(\sqrt p\) with an arithmetic leading factor determined by \(a/\sqrt p\):
\[\frac{\|P_H\|_{\infty\to\infty}}{\sqrt p}=\frac18\left(\sqrt{3+2a/\sqrt p}+\sqrt{3-2a/\sqrt p}\right)+O(p^{-1/2}),\]
with an absolute implied constant as \(p\to\infty\) through the specified primes.

Writing \(K(t)=\sum_{h\in H}e^{2\pi iht/p}\), the kernel is nonzero at every \(t\). Every nonzero equality case of \(\|P_Hf\|_\infty\le \|P_H\|_{\infty\to\infty}\|f\|_\infty\) is of the form
\[f(y)=\lambda\,\frac{\overline{K(x_0-y)}}{|K(x_0-y)|}\quad (y\in\mathbb Z_p),\]
where \(x_0\in\mathbb Z_p\) and \(\lambda\in\mathbb C\setminus\{0\}\). The corresponding \(\ell^1\) equality cases follow from translation and duality.

## Assumptions and scope
The modulus is a rational prime congruent to \(5\) modulo \(8\). The Fourier multiplier \(P_H\) is defined with Fourier transform \(\widehat f(r)=p^{-1}\sum_x f(x)e^{-2\pi irx/p}\) and inversion \(f(x)=\sum_r\widehat f(r)e^{2\pi irx/p}\). Thus \((P_Hf)(x)=p^{-1}\sum_yK(x-y)f(y)\). Input/output norms use ordinary counting \(\ell^1\) and maximum \(\ell^\infty\), although their projection operator norms are independent of this common normalization.

## Proof
**Step 1 (period reduction).** Fix a primitive root \(g\pmod p\); let \(h=(p-1)/4\) and define the four cosets \(C_j=g^jH\) and periods \(\eta_j=\sum_{t\in C_j}e^{2\pi it/p}\) for \(j=0,1,2,3\). Each nonzero \(t\) gives \(K(t)=\eta_j\) for one \(j\), and each period occurs exactly \(h\) times; also \(K(0)=h\). The triangle inequality is sharp for the full complex \(\ell^\infty\) unit ball, hence
\[\|P_H\|_{\infty\to\infty}=\frac hp\left(1+\sum_{j=0}^3|\eta_j|\right).\]
The same convolution-kernel mass gives the \(\ell^1\to\ell^1\) norm. Since \(p\equiv5\pmod8\), \(-1\in C_2\), so \(\eta_2=\overline{\eta_0}\) and \(\eta_3=\overline{\eta_1}\). The quadratic Gauss sum gives
\[\eta_0+\eta_2=\frac{-1+\sqrt p}{2},\qquad \eta_1+\eta_3=\frac{-1-\sqrt p}{2}.\]
Therefore \(\operatorname{Re}\eta_0=(\sqrt p-1)/4\) and \(\operatorname{Re}\eta_1=(-\sqrt p-1)/4\).

**Step 2 (Jacobi sum with its correct signed coordinate).** Let \(\chi\) be the quartic multiplicative character with \(\chi(g)=i\), and \(\phi=\chi^2\) its quadratic character, each extended by zero at the origin. Define \(J=\sum_{x\in\mathbb F_p}\chi(x)\chi(1-x)\in\mathbb Z[i]\). Gauss-sum orthogonality and the standard convolution identity yield \(|J|^2=p\) and \(\tau(\chi)^2=J\tau(\phi)=J\sqrt p\), where \(\tau(\psi)=\sum_x\psi(x)e^{2\pi ix/p}\). To fix the sign in the two-squares representation, pair each summand indexed by \(x\) with the one indexed by \(1-x\). The unique self-paired nonzero summand is at \(x=1/2\), and equals \(\chi(1/4)=\phi(2)=-1\), because \(p\equiv5\pmod8\). A paired summand contributes twice a fourth root of unity. The number of pairs outside \(x=1/2\) whose contributions are real is \((p-5)/4\): indeed \(\sum_x\phi(x(1-x))=-1\), there are \((p-3)/2\) nonzero values with \(\phi(x(1-x))=1\), and exactly one of those values is the fixed point. Since \((p-5)/4\) is even, \(\operatorname{Re}J\equiv-1\pmod4\). Consequently, with \(p=a^2+4b^2\) and \(a\equiv1\pmod4\), the signed real part is \(\operatorname{Re}J=-a\). Uniqueness of this \(a\) is the classical uniqueness of the sum-of-two-squares representation of a prime \(p\equiv1\pmod4\), with the real coordinate fixed modulo \(4\).

**Step 3 (two period moduli).** Put \(C=\eta_0-\eta_2\) and \(D=\eta_1-\eta_3\). Both are purely imaginary. Since \(\tau(\chi)=C+iD\), comparison of the real part of \(\tau(\chi)^2=-a\sqrt p+2ib\sqrt p\) with \(|\tau(\chi)|^2=p\) yields
\[|C|^2+|D|^2=p,\qquad |C|^2-|D|^2=a\sqrt p.\]
In particular \(|C|^2=(p+a\sqrt p)/2\) and \(|D|^2=(p-a\sqrt p)/2\). From the real parts in Step 1,
\[|\eta_0|^2=\frac{(\sqrt p-1)^2}{16}+\frac{p+a\sqrt p}{8}=\frac{U_p}{16},\]
\[|\eta_1|^2=\frac{(\sqrt p+1)^2}{16}+\frac{p-a\sqrt p}{8}=\frac{V_p}{16}.\]
The four moduli occur in conjugate pairs. Substitution in Step 1 gives the displayed formula. For positivity, the bound \(|a|<\sqrt p\) implies \(U_p,V_p\ge(\sqrt p-1)^2>0\). It also implies \(K(t)\ne0\) at every site, including \(K(0)=h>0\).

**Step 4 (sharp equality and scale).** For a fixed \(x_0\), choose \(f(y)=\lambda\overline{K(x_0-y)}/|K(x_0-y)|\); the convolution triangle inequality is equality at \(x_0\). Conversely, if a nonzero \(f\) achieves the operator norm, equality in the finite sum at a maximizing \(x_0\), together with absence of zero kernel coefficients, forces the same common phase and constant modulus for all \(y\), proving the stated classification. Finally substitute \(a/\sqrt p\in[-1,1]\) into the exact radical expression and expand uniformly for \(p\to\infty\) to obtain the asymptotic.

## Verification
The accompanying standalone Python program `verify_quartic_projection.py` checks every prime \(p\equiv5\pmod8\) below \(1001\), 43 primes in total. It constructs a primitive generator, four cosets and period sums, independently evaluates the quartic Jacobi sum, verifies its signed real part and norm, compares both squared period moduli with the formulas, and compares the explicit radical expression against the direct Fourier-kernel absolute sum. The replay prints `VERIFY_OK primes 43 range 5 997`. These finite floating-point checks are reproducibility tests only; the theorem for all primes follows from the character-sum proof above.

## Relationship to prior work
Green and Konyagin introduce the normalized Fourier-algebra norm in prime cyclic groups and prove lower bounds for sets of about half the residues, not an exact formula for the special index-four multiplicative subgroup. Barcanescu's accessible full text explicitly treats the quartic Gaussian-period polynomial (Section VI.3), including the \(p\bmod8\) split, but does not compute or classify the endpoint Fourier projection norm or its norm-attaining vectors. The standard quadratic and quartic Gauss--Jacobi identities supply the arithmetic ingredient used here, and no new evaluation of Gauss sums is asserted. A closely related published computation determines a cubic-residue projector norm by real cubic Gaussian periods, but its index-three sign analysis cannot be specialized to the present index-four nonreal regime. The novelty claim here is the exact endpoint operator norm and phase-matched equality classification for this natural full congruence class, not the old Gauss-sum theory itself.

## Limitations
The result concerns primes \(p\equiv5\pmod8\) only, not the real-period quartic case \(p\equiv1\pmod8\), nor composite conductors, nor intermediate \(\ell^q\) operator norms. The equality description is for complex-valued functions. The arithmetic leading coefficient is not claimed to be a universal limit; no equidistribution theorem for Gaussian prime arguments is proved. The principal originality risk is a previously unindexed formulation of the same absolute quartic-period sum as a Fourier-algebra or Lebesgue constant. Independent audit and publication-priority determination have not been carried out.

## References
1. B. Green and S. Konyagin, *On the Littlewood Problem Modulo a Prime*, arXiv:math/0601565, first public 2006-01-23, especially the Fourier-algebra norm and prime-cyclic setting.
2. S. Barcanescu, *The Coefficients of the Period Polynomials*, arXiv:1402.3833, first public 2014-02-16, especially Section VI.3 on biquadratic periods.
3. *Gauss Periods*, publicly dated 2014-01-16, https://www.ihes.fr/~dustin/files/CyclotimicFields/Cyclo12.pdf, especially the index-two Gauss-period identity.
4. *Exact cubic-residue Lebesgue constants from Gaussian period arithmetic*, public mathematical research record, 2026-10-11; related index-three projection calculation, not used as a premise.
