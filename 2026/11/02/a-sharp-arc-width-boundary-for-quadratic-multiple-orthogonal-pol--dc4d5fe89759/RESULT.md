# A sharp arc-width boundary for quadratic multiple orthogonal polynomial zeros

## Finding

**Theorem (sharp universal support-width threshold for the original, non-Laurent MOPUC).** Let \(0<\alpha<\pi/2\), let \(\nu\) be an even Borel probability measure on \([ -\alpha,\alpha]\) other than the point mass at zero, and choose an angle
\[
 2\alpha<\theta<2\pi-2\alpha.
\]
Let \(\mu_1\) be the image of \(\nu\) under \(s\mapsto e^{is}\), and let \(\mu_2\) be its rotation through \(\theta\). The two measures have disjoint supporting closed arcs. Set
\[
 u=\int\cos s\,d\nu(s),\qquad
 v=\int\cos(2s)\,d\nu(s),\qquad
 h=\cos(\theta/2).
\]
The original type-II multiple orthogonal polynomial at multi-index \((1,1)\), namely the unique monic quadratic satisfying \(\int Q\,d\mu_1=\int Q\,d\mu_2=0\), is
\[
 Q(z)=z^2-\frac vu(1+e^{i\theta})z+ve^{i\theta}.
\]
Both zeros lie **strictly inside** the open unit disk if and only if
\[
 \boxed{(1+v)u>2|v|\,|h|.} \tag{1}
\]
At equality, exactly one zero lies on the unit circle; if the inequality reverses, a zero lies strictly outside it.

Define the universal angular half-width
\[
 \boxed{\alpha_*=\arccos(1/\sqrt3).} \tag{2}
\]
For every \(0<\alpha\le\alpha_*\), every even probability \(\nu\ne\delta_0\) supported in \([ -\alpha,\alpha]\), and every separated rotation \(\theta\) as above, both zeros lie strictly inside the disk. **This universal guarantee is sharp:** for each \(\alpha_*<\alpha<\pi/2\), some separated rotation and an even \(C^\infty\) density that is strictly positive on \((-\alpha,\alpha)\) and has support equal to the *entire* closed interval \([ -\alpha,\alpha]\) give a monic quadratic with a zero of modulus greater than one.

For the endpoint-pair measure \(\nu=\tfrac12(\delta_{-\alpha}+\delta_\alpha)\), the criterion has an exact phase boundary. When \(\alpha>\alpha_*\), put
\[
 \beta_\alpha=\frac{\cos^3\alpha}{1-2\cos^2\alpha},
 \qquad \theta_\alpha=2\arccos\beta_\alpha.
\]
Then \(2\alpha<\theta_\alpha<\pi\), and both zeros are strictly interior precisely for
\[
 \theta_\alpha<\theta<2\pi-\theta_\alpha.
\]
At the two endpoints of that interval there is one unimodular zero; outside it but within the separated-arc range, one zero is strictly exterior. For \(\alpha\le\alpha_*\), every separated rotation of this endpoint-pair measure is strictly stable.

By contrast, if \(\nu\) is normalized Lebesgue measure on \([ -\alpha,\alpha]\), the zeros are strictly interior for **every** \(0<\alpha<\pi/2\) and every separated rotation. Thus the sharp failure beyond \(\alpha_*\) concerns the shape of the density, not merely the existence of a wide arc.

## Assumptions and scope

The term *original* refers to the 2008 definition of Mínguez Ceniceros and Van Assche, with orthogonality against \(z^{-p}\) for \(p=0,\ldots,n_j-1\). For the index \((1,1)\) this is exactly orthogonality against the constant function for each of the two measures. This is not the later Laurent multiple-orthogonality construction, which has different moment conditions and a different zero-localization theorem.

Evenness means \(\nu(E)=\nu(-E)\) for Borel subsets of the real interval. Measures need not be absolutely continuous in the universal part of the theorem; the sharpness examples *are* absolutely continuous, smooth, and strictly positive on the interior of each support arc. Since \(|s|<\pi/2\), one has \(u\ge\cos\alpha>0\). Since \(\nu\ne\delta_0\), one has \(-1<v<1\). Angles and arc endpoints are real, and the strict inequalities exclude touching arcs. No assumptions about higher multi-indices are made.

## Proof

**1. Normality and exact polynomial.** Evenness gives \(\int e^{is}\,d\nu(s)=u\) and \(\int e^{2is}\,d\nu(s)=v\), both real. Let \(\omega=e^{i\theta}\) and \(Q(z)=z^2+Az+B\). The two orthogonality conditions are
\[
 v+Au+B=0,\qquad v\omega^2+Au\omega+B=0.
\]
Their coefficient determinant is \(u(1-\omega)\ne0\) because \(u>0\) and the arcs are separated. Subtraction gives \(A=-(v/u)(1+\omega)\) and then \(B=v\omega\). Thus the unique monic quadratic exists for *every* measure in the stated class.

**2. Disk criterion.** Under the rotation \(z=e^{i\theta/2}y\), division by \(e^{i\theta}\) reduces \(Q\) to the real quadratic
\[
 q(y)=y^2-2\frac vu\cos(\theta/2)y+v.
\]
For a real monic quadratic \(y^2+by+c\) with \(-1<c<1\), both roots are in \(|y|<1\) exactly when \(1+c>|b|\). To reconstruct this criterion, necessity follows from \(q(1)=(1-y_1)(1-y_2)>0\) and \(q(-1)=(1+y_1)(1+y_2)>0\), interpreted by conjugate pairing for nonreal roots. Conversely, a nonreal conjugate pair has squared modulus \(c\in(0,1)\). If roots are real, \(|c|<1\) rules out two roots both at least one or both at most negative one; a remaining root outside \([-1,1]\) forces one of \(q(1)\) or \(q(-1)\) to be nonpositive. Equality in one of the strict inequalities gives exactly one root \(1\) or \(-1\), since \(|c|<1\), and a strict reverse inequality gives an exterior root. Substitution gives (1), including its equality and failure cases.

**3. Uniform localization below the sharp half-width.** Put \(c=\cos\alpha\). For separated rotations, \(|h|<c\); also \(u\ge c\) and \(v\ge\cos(2\alpha)=2c^2-1\). If \(\alpha\le\alpha_*\), then \(2c^2-1\ge-1/3\). For \(-1/3\le v<1\) one has \(1+v\ge2|v|\). If \(v\ne0\), the strict \(u>|h|\) yields \((1+v)u>2|v||h|\); if \(v=0\), the same strict inequality is immediate. Thus (1) always holds. This also covers \(\alpha=\alpha_*\), because arc separation remains strict.

**4. Sharpness by smooth full-support measures.** Fix \(\alpha>\alpha_*\) and put \(c=\cos\alpha\in(0,1/\sqrt3)\). First take the symmetric atomic measure \(\nu_0=\tfrac12(\delta_{-\alpha}+\delta_\alpha)\), for which \(u=c\) and \(v=2c^2-1< -1/3\). In the limit \(\theta\downarrow2\alpha\), the left-minus-right side of (1) tends to
\[
 (1+v)c-2|v|c
 =2c(3c^2-1)<0.
\]
Continuity therefore gives a **strictly separated** angle \(\theta>2\alpha\) with an exterior root. Approximate \(\nu_0\) weakly by normalized even densities consisting of two nonnegative \(C^\infty\) bumps centered just inside \(\pm\alpha\), whose widths and distances to the endpoints tend to zero, plus a positive but vanishingly weighted \(C^\infty\) background that is positive at every \(s\in(-\alpha,\alpha)\) and flat at both endpoints. These densities are \(C^\infty\) on the circle and have support exactly \([ -\alpha,\alpha]\). Their first two cosine moments converge to \((c,2c^2-1)\); the strict reversed inequality persists. Their rotated supports remain disjoint, proving sharpness with smooth full-support weights, not merely discrete atoms.

**5. Exact endpoint-pair phase boundary.** In the atomic case, if \(\alpha>\alpha_*\), criterion (1) reduces to
\[
 |h|<\frac{(1+v)c}{2|v|}
 =\frac{c^3}{1-2c^2}=\beta_\alpha.
\]
The inequality \(\beta_\alpha<c\) is equivalent to \(3c^2<1\). On the admissible angle interval, \(|\cos(\theta/2)|<\beta_\alpha\) holds exactly when \(\theta_\alpha<\theta<2\pi-\theta_\alpha\). Endpoint and exterior cases follow from the quadratic criterion. The subcritical case follows from Step 3.

**6. Uniform angular density is always stable.** For normalized Lebesgue measure on the angular interval, \(u=\sin\alpha/\alpha\) and \(v=\sin(2\alpha)/(2\alpha)=u\cos\alpha>0\). Since \(|h|<\cos\alpha=c\), it suffices for (1) to show \(1+uc>2c^2\), equivalently \(\sin(2\alpha)/(2\alpha)>\cos(2\alpha)\). For \(\alpha\ge\pi/4\) this is immediate because the right side is nonpositive and the left side is positive. For \(0<\alpha<\pi/4\), it is the standard strict inequality \(\tan t>t\) for \(t=2\alpha\in(0,\pi/2)\). This completes the proof.

**A concrete exterior zero.** Take \(\alpha=\pi/3\), \(\theta=5\pi/6\), and \(\nu_0=\tfrac12(\delta_{-\pi/3}+\delta_{\pi/3})\). The arcs \([-\pi/3,\pi/3]\) and \([\pi/2,7\pi/6]\) are disjoint. Here the rotated quadratic is
\[
 q(y)=y^2+2\cos(5\pi/12)y-\tfrac12.
\]
Its value at \(y=-1\) equals \(\tfrac12-2\cos(5\pi/12)<0\), because \(4\cos(5\pi/12)=\sqrt6-\sqrt2>1\). Since \(q(y)\to+\infty\) as \(y\to-\infty\), one root lies strictly below \(-1\). The root is approximately \(-1.01180463468\). The preceding smoothing construction preserves strict escape for smooth densities on the full arcs.

## Verification

The accompanying standalone `checker.py` uses deterministic finite mixtures of symmetric angular measures to test the two moment conditions, rotated-root identities, and the Schur criterion. It tests many subcritical supports, supercritical endpoint-pair widths, the explicit exterior example, smooth endpoint-concentrated full-support approximations, and uniform angular measures. In the completed replay, it passed **14,215 supplementary assertions**. It uses Python's standard library only. Its finite computations do not certify the universal claim: Steps 1–6 above supply the proof.

For reproducibility, execute `python checker.py` in the same directory as this file. There are no external datasets, private inputs, or third-party code dependencies.

## Relationship to prior work

Mínguez Ceniceros and Van Assche introduced the original type-II MOPUC and studied examples on disjoint and overlapping arcs [1]. Their examples do not give the exact quadratic classification, the sharp universal support half-width, or smooth full-support exterior examples at index \((1,1)\). Kozhan and Vaktnäs [2] proved strict disk localization for the **different Laurent** multiple-orthogonal construction on Angelesco/AT systems, and explicitly distinguished that construction from the original MOPUC; their theorem does not cover the quadratic considered here. Gharakhloo, Kosmakov, and Miyahara [3] gave general mixed-moment reduction formulae for ordinary MOPUC and exhibited a high-degree resonance escape mechanism with a full-circle reference weight and arc-indicator companions. Their structural formula does not state, nor directly classify, the rotated symmetric quadratic measures or the sharp \(\arccos(1/\sqrt3)\) threshold. The present theorem is a specialization of the original orthogonality definition plus a new sharp family-wide localization/escape classification, not a claim to have invented moment linear algebra or zero escape itself.

## Limitations

The universal threshold applies to even angular measures and their rotated copies, the original type-II multi-index \((1,1)\), and separated arcs of equal angular half-width. It does not claim the same threshold for arbitrary nonsymmetric measures, differently shaped arc pairs, higher indices, or Laurent MOPUC. Counterexamples above the threshold are existential; not every density fails (uniform densities never do). The smooth construction uses limiting moments but supplies a strict-open perturbation argument, not a numerical existence assertion. Published coverage in older specialized moment or polynomial-root literature cannot be ruled out absolutely by a finite search. No independent audit or formal certificate has been performed.

## References

[1] J. Mínguez Ceniceros and W. Van Assche, *Multiple Orthogonal Polynomials on the Unit Circle*, 2008, Sections 2–3, https://wis.kuleuven.be/analyse/members/walter/mopu.pdf .

[2] R. Kozhan and M. Vaktnäs, *Zeros of Laurent multiple orthogonal polynomials on the unit circle*, arXiv:2603.21468v1, posted 2026-03-23, Sections 1.1–1.2 and 5, https://arxiv.org/html/2603.21468v1 .

[3] R. Gharakhloo, M. Kosmakov, and K. Miyahara, *Reduction of Multiple Orthogonal Polynomials to Standard Orthogonal Polynomials*, arXiv:2606.27594, posted 2026-06-25, Sections 3.2 and 6, https://arxiv.org/abs/2606.27594 .
