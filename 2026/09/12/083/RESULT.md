# Simple-module top spaces for the parafermion VOA \(K(G_2,2)\)

## Finding

The parafermion vertex operator algebra \(K(G_2,2)\) has 48 inequivalent simple modules. Their lowest conformal weights \(h\) and top dimensions \(t\) are given below, and
\[
\dim A(K(G_2,2))=\sum t^2=149.
\]
The vacuum character, with its leading power of \(q\) removed, begins
\[
1+6q^2+13q^3+38q^4+80q^5+182q^6+O(q^7).
\]
Let \(C_0=\{(0,0)\}\), \(C_6=\{(0,1),(0,5),(1,1),(1,2),(1,4),(1,5)\}\), \(C_2=\{(0,2),(0,4)\}\), and \(C_3=\{(0,3),(1,0),(1,3)\}\). Each entry applies separately to every class in its column, giving \(4(1+6+2+3)=48\) entries.

| Affine highest weight | \(C_0:(h,t)\) | \(C_6:(h,t)\) | \(C_2:(h,t)\) | \(C_3:(h,t)\) |
|---|---|---|---|---|
| \(0\) | \((0,1)\) | \((5/6,1)\) | \((4/3,3)\) | \((1/2,1)\) |
| \(\omega_1\) | \((2/3,2)\) | \((1/2,1)\) | \((1,3)\) | \((1/6,1)\) |
| \(\omega_2\) | \((1/3,1)\) | \((1/6,1)\) | \((2/3,3)\) | \((5/6,3)\) |
| \(2\omega_2\) | \((7/9,3)\) | \((11/18,2)\) | \((1/9,1)\) | \((5/18,1)\) |

## Assumptions and scope

Work over \(\mathbb C\), with long roots of squared length 2. The simple root \(\alpha_1\) is long and \(\alpha_2\) is short. In root coordinates \(w=a\alpha_1+b\alpha_2\),
\[
(w,w)=2a^2-2ab+\tfrac23b^2,\quad
\omega_1=(2,3),\quad\omega_2=(1,2),\quad\rho=(3,5).
\]
The long-root lattice is \(Q_L=\mathbb Z\alpha_1+3\mathbb Z\alpha_2\); the class of \(w\) is \((a\bmod2,b\bmod6)\). The level-2 affine highest weights are \(0,\omega_1,\omega_2,2\omega_2\), with affine conformal weights \(0,2/3,1/3,7/9\). Classes denote the actual affine weight \(w\), not \(w-\Lambda\). The finding does not resolve generators and relations or the classically-free question.

## Proof

### 1. Lattice translation gives a finite cutoff

For affine grade \(n\), define
\[
E(w)=9(w,w)=18a^2-18ab+6b^2,\qquad F(n,w)=36n-E(w).
\]
Dong–Ren's equations (4.1)–(4.3) and Proposition 4.4 express each fixed class as a lattice module tensored with one parafermion module. Thus
\[
\Delta_\Lambda+n=(w,w)/4+s+h,
\]
where \(s\ge0\) is the rank-two Heisenberg oscillator grade and \(h\) the parafermion weight. Replacing momentum \(w\) by any representative \(w_0\) in the same class preserves the oscillator and parafermion factors, changing the affine grade to \(n_0\) with
\[
36n_0-E(w_0)=36n-E(w).
\]
Every hypothetical parafermion weight below a candidate top therefore has a nonzero affine vector at \(w_0\), with oscillator grade zero.

Choose \(w_0\) minimizing \(E\) in its class. In lexicographic class order \((0,0),(0,1),\ldots,(1,5)\), the minima are
\[
0,6,24,18,24,6,18,6,6,18,6,6.
\]
These are global minima: the completed squares
\[
E=18(a-b/2)^2+\tfrac32b^2
 =6(b-3a/2)^2+\tfrac92a^2
\]
give \(E>24\) whenever \(|a|\ge3\) or \(|b|\ge5\). Enumeration of \(|a|\le2,|b|\le4\) contains a minimizer for each class.

Exact affine grades 0–2 give:

| \(\Lambda\) | \(C_0:(F,t)\) | \(C_6:(F,t)\) | \(C_2:(F,t)\) | \(C_3:(F,t)\) |
|---|---|---|---|---|
| \(0\) | \((0,1)\) | \((30,1)\) | \((48,3)\) | \((18,1)\) |
| \(\omega_1\) | \((0,2)\) | \((-6,1)\) | \((12,3)\) | \((-18,1)\) |
| \(\omega_2\) | \((0,1)\) | \((-6,1)\) | \((12,3)\) | \((18,3)\) |
| \(2\omega_2\) | \((0,3)\) | \((-6,2)\) | \((-24,1)\) | \((-18,1)\) |

For every class the integer \((F+E(w_0))/36\) is between 0 and 2. The verifier checks the displayed multiplicity at that grade and zero multiplicity at every earlier grade at \(w_0\). A smaller parafermion weight would occur at an earlier affine grade there, contrary to the exact finite calculation. This proves all-grade minimality. At the top the oscillator grade is zero, so the affine multiplicity equals \(t\). Theta-translated weights represent the same top and must not be summed. Finally \(h=\Delta_\Lambda+F/36\).

### 2. Completeness of the finite affine calculation

The positive finite roots are \((1,0),(1,3),(2,3),(0,1),(1,1),(1,2)\). Grade-zero weights lie in the convex hull of the finite Weyl orbit of \(\Lambda\), hence in \(|a|\le2,|b|\le4\) for these modules. A Poincaré–Birkhoff–Witt spanning set at grade at most \(n\) uses at most \(n\) negative nonzero modes; each changes finite coordinates by a root or zero. Thus all genuine weights through grade 2 lie in \(|a|\le6,|b|\le10\), inside the recursion box 14. Omitted weights outside that box are zero.

The verifier implements Freudenthal–Kac in exact rational arithmetic, ordered by grade then descending finite-root height. Its denominator is
\[
3\big((\Lambda+\rho,\Lambda+\rho)-(w+\rho,w+\rho)\big)+36n.
\]
For a genuine nonhighest weight \(\mu\), it is positive. Integrable affine weights lie in the convex hull of the affine Weyl orbit of \(\widehat\Lambda\). On the fixed-level affine hyperplane the invariant squared norm is a convex function (its quadratic part is the positive finite-root norm), so \((\mu,\mu)\le(\widehat\Lambda,\widehat\Lambda)\). Also \(\widehat\Lambda-\mu\) is a nonzero nonnegative integral sum of simple affine roots, each pairing positively with \(\widehat\rho\). Therefore
\[
(\widehat\Lambda+\widehat\rho)^2-(\mu+\widehat\rho)^2
=\widehat\Lambda^2-\mu^2+2(\widehat\rho,\widehat\Lambda-\mu)>0.
\]
Thus denominator-zero points other than the initial highest weight are not genuine weights. The recurrence includes all positive real affine roots and imaginary roots of multiplicity 2. Its ordering puts every nonzero right-hand weight earlier; the proved support boxes make every omitted weight zero. Induction on that ordering gives the genuine multiplicities, not just a consistent numerical array.

### 3. Classification, Zhu algebra, and vacuum coefficients

Ai–Dong–Jiao–Ren Theorem 5.1 gives exactly
\[
|P^2_+|\,|Q/2Q_L|/|P/Q|=4\cdot12/1=48
\]
inequivalent modules. Dong–Ren Theorem 5.1 proves rationality; its proof gives \(C_2\)-cofiniteness. Zhu's algebra is finite-dimensional semisimple, with simple-module dimensions \(t\); Artin–Wedderburn gives 149.

For the vacuum, grade-zero support is just zero. The same spanning-set bound places all weights through grade 6 in \(|a|\le12,|b|\le18\), inside box 20. The weight-zero affine string coefficients are
\[
1,2,11,35,114,317,847.
\]
Multiplying by \(\prod_{m\ge1}(1-q^m)^2\) removes Heisenberg oscillators, giving \(1,0,6,13,38,80,182\) through grade 6.

## Verification

Run python artifacts/verify_finite.py. This stdlib-only verifier checks all shortest representatives, all 48 \((F,t)\) pairs, their representative grades and earlier-grade zeros, the sum 149, and the displayed vacuum coefficients. Its final line is VERIFY_OK: all 48 sectors and finite lattice-translation cutoff.

The finite recurrence certifies numerical data in proved support boxes. The lattice-decomposition argument supplies the all-grade theorem. Older exploratory artifacts are retained for comparison, not as an extrapolation to infinite grades.

## Relationship to prior work

Rationality, classification, lattice translation and affine multiplicity recursion are prior results. The contribution is the explicit exceptional low-level top-space table and Zhu dimension with a finite, support-complete certificate of their all-grade meaning, not a new general classification or character formula. Kuniba–Nakanishi–Suzuki Section 2, equations (9)–(16), already proposes vacuum-sector characters for arbitrary untwisted types and includes a \(G_2\), level-2 consistency check; its stated scope there is exclusively the affine vacuum label. The vacuum row and initial character are therefore not claimed as independent originality. That formula does not supply the three nonvacuum-label rows here; those require the explicit certified affine multiplicities. Arakawa–Lam–Yamada's exact Zhu-dimension formula in Sections 7–8 is for \(\mathfrak{sl}_2\), while its general Section 10 proves \(C_2\)-cofiniteness. Neither is an exact \(G_2\), level-2 top table. No absolute historical-first claim is made.

## Limitations

Only vacuum coefficients through grade 6 are certified here. Later entries in older exploratory string artifacts are not independently certified by this cutoff. Unindexed branching tables may overlap. No proof-assistant or external expert certification is claimed.

## References

- Chongying Dong and Li Ren, *Representations of the parafermion vertex operator algebras*, [arXiv:1411.6085](https://arxiv.org/abs/1411.6085), equations (4.1)–(4.3), Proposition 4.4, Theorem 5.1.
- Chunrui Ai, Chongying Dong, Xiangxu Jiao, and Li Ren, *The irreducible modules and fusion rules for the parafermion vertex operator algebras*, [arXiv:1412.8154](https://arxiv.org/abs/1412.8154), Theorem 5.1.
- Tomoyuki Arakawa, Ching Hung Lam, and Hiromichi Yamada, *Zhu's algebra, \(C_2\)-algebra and \(C_2\)-cofiniteness of parafermion vertex operator algebras*, [arXiv:1207.3909](https://arxiv.org/abs/1207.3909).
- Atsuo Kuniba, Tomoki Nakanishi, and Junji Suzuki, *Characters in Conformal Field Theories from Thermodynamic Bethe Ansatz*, [arXiv:hep-th/9301018](https://arxiv.org/pdf/hep-th/9301018), Section 2, equations (9)–(16).
