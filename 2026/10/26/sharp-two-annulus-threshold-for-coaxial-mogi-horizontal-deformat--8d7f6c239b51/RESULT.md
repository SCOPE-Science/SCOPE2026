# Sharp two-annulus threshold for coaxial Mogi horizontal deformation

## Finding

**Theorem (complete radial-mode classification).** In the ideal, linear-superposition Mogi point-source model, take two positive volume-change strengths \(A_1,A_2>0\) at strictly ordered depths \(0<d_1<d_2\), with the same horizontal source position. The radial horizontal surface displacement is
\[
U(r)=\frac{A_1 r}{(r^2+d_1^2)^{3/2}}+\frac{A_2 r}{(r^2+d_2^2)^{3/2}},\qquad r\ge0.
\]
Set \(z=(d_2/d_1)^2\), \(q=A_2/A_1\), and
\[
 z_*=11+2\sqrt{30},\quad D_*=\sqrt{z_*}=4.685557720282968\ldots.
\]
If \(1<z\le z_*\), \(U\) has exactly one strict local (hence global) maximum on \((0,\infty)\) for **every** \(q>0\). If \(z>z_*\), define
\[
 x_\pm=\frac{z+1\pm\sqrt{z^2-22z+1}}8,\qquad
 \Phi_z(x)=\frac{2x-1}{z-2x}\left(\frac{x+z}{x+1}\right)^{5/2}.
\]
Then \(1/2<x_-<x_+<z/2\) and \(\Phi_z(x_+)<\Phi_z(x_-)\). Precisely **two** strict local maxima, with one strict local minimum between them, occur if and only if
\[
 \boxed{\Phi_z(x_+)<q<\Phi_z(x_-).}
\]
For all other strengths there is exactly one strict local maximum. At equality with either bound, a second *nonextremal* horizontal stationary point (a shoulder) is present. There are no other positive-radius stationary extrema.

At the unique critical combination \(z=z_*\), \(q=\Phi_{z_*}(x_*)\), where \(x_*=(z_*+1)/8\), the unique strict maximum is quartically flat rather than quadratically flat. The admissible strength window opens according to
\[
 \Phi_z(x_-)-\Phi_z(x_+)
 =C(z-z_*)^{3/2}+o((z-z_*)^{3/2}),
\]
where
\[
 c_* =\frac{z_*-1}{2(2x_*-1)(z_*-2x_*)(x_*+1)(x_*+z_*)},\qquad
 C=\frac12\Phi_{z_*}(x_*)c_*30^{3/4}
 =0.277181208560743\ldots.
\]
This makes the threshold sharp, gives the full amplitude window for observing two concentric annular peaks, and quantifies the narrow opening near the threshold.

## Assumptions and scope

The formula is a mathematical model of **two positive, vertically coaxial Mogi point-dilatation sources**, under an isotropic, homogeneous elastic half-space with flat free surface and linear superposition. Both amplitudes use the same physical prefactor, so their ratio corresponds to the ratio of positive source-volume changes in the ideal point-source law. Depths, strengths and radius are continuous real quantities; the assertions hold for all \(0<d_1<d_2\), \(A_1,A_2>0\), \(r\ge0\). A peak means a strict local maximum in the one-sided radial profile for \(r>0\), not a local extremum of a signed Cartesian displacement component. Two positive-radius peaks correspond to two concentric high-displacement rings. No negative/deflating source or lateral source offset is allowed.

## Proof

**1. Normalize without changing extrema.** With \(\rho=r/d_1\), positive multiplication by \(d_1^2/A_1\) turns \(U\) into
\[
 F(\rho)=\frac{\rho}{(1+\rho^2)^{3/2}}
 +q\frac{\rho}{(z+\rho^2)^{3/2}},\qquad \rho\ge0.
\]
Putting \(x=\rho^2\), differentiation gives
\[
 F'(\rho)=\frac{1-2x}{(1+x)^{5/2}}
 +q\frac{z-2x}{(z+x)^{5/2}}.
\]
For \(0\le x\le1/2\) this is strictly positive, and for \(x\ge z/2\) it is strictly negative. All positive stationary points therefore lie strictly inside \((1/2,z/2)\), and \(F\) rises from zero and decays to zero.

**2. Reduce the sign to a derivative-ratio intersection.** Within that interval,
\[
 \operatorname{sgn} F'(\sqrt x)
 =\operatorname{sgn}(q-\Phi_z(x)),\quad
 \Phi_z(x)=\frac{2x-1}{z-2x}\left(\frac{x+z}{x+1}\right)^{5/2}.
\]
This positive continuous function tends to zero at the left endpoint and to positive infinity at the right endpoint. Its logarithmic derivative is exactly
\[
 \frac{\Phi_z'(x)}{\Phi_z(x)}=
 \frac{(z-1)P_z(x)}{2(2x-1)(z-2x)(x+1)(x+z)},\qquad
 P_z(x)=24x^2-6(z+1)x+9z.
\]
The denominator is positive in the interval. The discriminant of \(P_z\) as a polynomial in \(x\) is \(36(z^2-22z+1)\). For \(z>1\), this discriminant can be positive only when \(z>z_*\), where \(z_*=11+2\sqrt{30}\); at equality it vanishes. When \(z>z_*\), both zeros
\[
 x_-=\frac{z+1-\sqrt{z^2-22z+1}}8,\quad
 x_+=\frac{z+1+\sqrt{z^2-22z+1}}8
\]
lie strictly inside \((1/2,z/2)\). Indeed \(z>z_*>3\), \(\sqrt{z^2-22z+1}<z-3\), and \(\sqrt{z^2-22z+1}<3z-1\). Thus \(\Phi_z\) is increasing, then decreasing, then increasing, with a strict maximum at \(x_-\) and a strict minimum at \(x_+\).

**3. Exhaust all extrema and boundaries.** For \(z<z_*\), \(P_z>0\) and \(\Phi_z\) is strictly increasing. At \(z=z_*\) it remains strictly increasing despite one zero of \(\Phi_z'\). Hence every horizontal line \(q>0\) cuts it at one point, across which \(F'\) changes from positive to negative. For \(z>z_*\), it cuts three times exactly if \(\Phi_z(x_+)<q<\Phi_z(x_-)\), giving the alternating derivative signs \(+,-,+,-\) and two maxima. Outside the closed strength interval it cuts once. At a boundary it cuts once transversely and touches at one fold point: this produces one maximum and a nonextremal shoulder. At the critical cusp, \(P_z\) has a double zero, so \(\Phi_z(x)-q\) vanishes to third order at \(x_*\); consequently \(F'\) vanishes to third order and \(F\) has an isolated quartic strict maximum. These possibilities are exhaustive.

**4. Derive the strength-window opening.** Write \(\epsilon=z-z_*>0\), and let \(h=(x_+-x_-)/2=\sqrt{z^2-22z+1}/8\). The exact formula gives
\[
 h=\frac{30^{1/4}}4\sqrt{\epsilon}+O(\epsilon^{3/2}).
\]
Near \((x_*,z_*)\), the logarithmic derivative identity from step 2 has leading term
\[
 \frac{d}{dx}\log\Phi_z(x)
 =24c_*\big((x-x_*)^2-h^2\big)+O(\epsilon^{3/2})
\]
uniformly between the two critical points (a shift of their midpoint by \(\epsilon/8\) contributes only higher-order corrections after integration). Integrating from \(x_-\) to \(x_+\) gives
\[
 \log\Phi_z(x_-)-\log\Phi_z(x_+)
 =32c_*h^3+o(\epsilon^{3/2})
 =\tfrac12c_*30^{3/4}\epsilon^{3/2}+o(\epsilon^{3/2}).
\]
Since both endpoint strengths tend to \(\Phi_{z_*}(x_*)\), exponentiation yields the claimed coefficient \(C\). This is a local algebraic asymptotic, not a numerical extrapolation.

## Verification

The included standalone `verify_mogi.py` checks the exact derivative identity, the quadratic discriminant and critical double root symbolically with SymPy. It also reproduces deterministic derivative-ratio comparisons and sample three-stationary-point configurations, and checks the asymptotic coefficient numerically. Run `python verify_mogi.py` with the dependency in `requirements.txt`.

An explicit rational-parameter witness takes \(d_1=1\), \(d_2=6\), \(A_1=1\), \(A_2=45\). Here \(z=36\) and \(\Phi_{36}(x_+)\approx39.4969724<45<53.7374887\approx\Phi_{36}(x_-)\). The three stationary squared radii are approximately \(1.0482076511\), \(4.0709656119\), and \(10.8529207531\), producing a strict maximum, strict minimum and strict maximum in this order. Sample computations are not a substitute for the preceding proof.

## Relationship to prior work

Mogi's classical point-source law supplies the single-source deformation kernel; its discovery and the superposition principle are not new. Pascal, Neuberg and Rivalta (2013) explicitly analyze double pressure-source Mogi approximations against finite-element models and their interaction errors, including vertically superposed sources. Their investigated quantity is the accuracy of superposition and source-parameter inversion, not an all-depth, all-strength radial peak-count theorem. Their physical caveat about source interaction applies to this idealization.

Došlá (2009), especially Theorems 1 and 2, gives an abstract derivative-ratio criterion for bimodality of mixtures of two unimodal densities. After normalization, the positive radial Mogi profiles can be treated as two such densities. The general idea that three intersections of a derivative ratio produce two modes is therefore **prior work**. What is established here for the specific geophysical kernel is the exact, sharp depth contrast \(z_*\), the explicit radical locations of both strength thresholds, the exhaustive boundary degeneracies and the \(3/2\)-power window-opening coefficient; the cited paper's worked Cauchy/Student examples instead concern location-shift mixtures, not this co-located radial Mogi scale family. Aspri, Beretta and Mascia (2017) establish a rigorous single-cavity asymptotic foundation for Mogi-type formulas, not the two-scale profile threshold. Historical priority for an unlocated specialized theorem remains unverified.

## Limitations

The theorem concerns the *ideal algebraic superposition model*, not interacting finite-size magma chambers. Pressure-source interference, finite radii, nonhomogeneous elastic media, topography, lateral offsets, mixed inflation/deflation, measurement noise and spatial resolution are outside the proof. Two mathematical maxima do not guarantee distinguishability in field measurements or unique inversion of chamber depths and source strengths. The general mixture ratio-method is known prior work; the novel claim is restricted to the exact Mogi-specific phase boundary and its local behavior.

## References

1. K. Mogi, “Relations between the Eruptions of Various Volcanoes and the Deformations of the Ground Surfaces around them,” *Bulletin of the Earthquake Research Institute* **36** (1958), 99–134. DOI: 10.15083/0000033924.
2. K. Pascal, J. Neuberg and E. Rivalta, “On precisely modelling surface deformation due to interacting magma chambers and dykes,” *Geophysical Journal International* **196** (2014), 253–278; first online 2013-10-16. DOI: 10.1093/gji/ggt343.
3. Š. Došlá, “Conditions for bimodality and multimodality of a mixture of two unimodal densities,” *Kybernetika* **45** (2009), 279–292. DML-CZ 140075: https://www.dml.cz/handle/10338.dmlcz/140075.
4. A. Aspri, E. Beretta and C. Mascia, “Analysis of a Mogi-type model describing surface deformations induced by a magma chamber embedded in an elastic half-space,” *J. Éc. polytech. Math.* **4** (2017), 223–255. DOI: 10.5802/jep.42.
