# An arithmetic phase transition in the invariant quartic-curve Fourier norm

## Finding
For a finite field \(F=\mathbb F_q\) of characteristic \(p>3\), fix a nontrivial additive character \(\psi\) and the graph \(\Gamma_4=\{(t,t^4):t\in F\}\). Define the unnormalized extension operator
\[
Tf(u,v)=\sum_{t\in F} f(t)\psi(ut+vt^4),\qquad (u,v)\in F^2.
\]
The input uses counting-measure \(\ell^2(F)\); the output uses probability-measure \(L^4(F^2)\). Let \(V\) be the multiplicatively invariant subspace consisting of functions constant on \(F^\times\), with a possibly different coefficient at zero. Write \(m=q-1\), \(h=\chi(-7)\), and \(k=\chi(-3)\), where \(\chi\) is the quadratic character with \(\chi(0)=0\).

The exact fourth power of the restriction of \(T\) to \(V\), relative to its counting \(\ell^2\) norm, equals
\[
\mathcal M(q)=\begin{cases}
\dfrac{3q-4-2k}{q-1},&h=-1,\\[2mm]
\dfrac{r^4+4mr^2+4m(1+h)r+m(3q-8-4h-2k)}{(m+r^2)^2},&h\in\{0,1\},
\end{cases}
\]
where, in the second case, \(r\) is the **unique positive root** of
\[
r^3+3(1+h)r^2+(q-6-4h-2k)r-m(1+h)=0.
\]
All nonzero maximizers in \(V\) are exactly the scalar multiples of the function having value \(0\) at zero and \(1\) elsewhere when \(h=-1\), or of the function having value \(r\) at zero and \(1\) elsewhere when \(h\in\{0,1\}\). In particular, the behavior switches between vanishing and enhanced origin mass according to \(\chi(-7)\). The characteristic-seven regime is included in the second case.

A further consequence for the **unrestricted** extension problem is that the constant input \(f\equiv1\) is never a stationary point of the fourth-power quotient for any \(q\) of characteristic greater than \(3\): the origin perturbation has a nonzero derivative whose sign is governed by \(1+q\chi(-7)+2\chi(-3)\). No unrestricted sharp norm is asserted.

## Assumptions and scope
All finite fields \(\mathbb F_q\) of odd characteristic greater than \(3\) are included, not just prime fields. A function belongs to \(V\) precisely when \(f(0)=z c\) and \(f(t)=c\) for every nonzero \(t\), for complex scalars \(z,c\); the case \(c=0\) is separately allowed. The normalization uses \(q^{-2}\sum_{u,v\in F}\lvert Tf(u,v)\rvert^4\), not an unnormalized sum and not the customary probability normalization for the *input*.

Multiplicative reparametrization \(t\mapsto\lambda t\), \(\lambda\in F^\times\), is a symmetry of the extension quotient, compensated by \((u,v)\mapsto(\lambda^{-1}u,\lambda^{-4}v)\). Therefore \(V\) is its canonical fixed space, rather than a choice of coordinate slice without invariant meaning.

## Proof
**1. The local collision profile.** Character orthogonality yields
\[
\lVert Tf\rVert_4^4=\sum_{a,b,c,d\in F\,:\,a+b=c+d\,,\ a^4+b^4=c^4+d^4}
 f(a)f(b)\overline{f(c)f(d)}.
\]
Let \(w(t)\) count these ordered quadruples whose first entry is a prescribed \(t\). Fixing the second entry \(a\), put \(s=t+a\) and \(P=ta\). When a second ordered pair has product \(Q\) and sum \(s\), the fourth-power identity \(t^4+a^4=s^4-4Ps^2+2P^2\) implies \((P-Q)(P+Q-2s^2)=0\). The first branch contains \(2-\mathbf1_{a=t}\) ordered pairs. The second branch, with product \(Q=2s^2-P\), contains \(1+\chi(4ta-7(t+a)^2)\) ordered pairs.

For \(t=0\), their common pair arises only at \(a=0\), once. The quadratic-character sum equals \(m\chi(-7)\), so
\[
w(0)=3q-2+m\chi(-7).
\]
For \(t\ne0\), their intersections occur at \(ta=(t+a)^2\), namely at the \(1+\chi(-3)\) roots of a quadratic, each carrying two ordered pairs. The remaining character sum, after setting \(a=tx\), is
\[
\sum_{x\in F}\chi(-7x^2-10x-7)=-\chi(-7).
\]
Indeed its discriminant is \(-96\ne0\), so the standard nondegenerate quadratic character sum applies when \(p\ne7\); in characteristic \(7\), the polynomial becomes nonconstant linear and its character sum vanishes, agreeing with \(\chi(-7)=0\). Therefore
\[
w(t)=3q-3-\chi(-7)-2\chi(-3),\qquad t\ne0.
\]
This is a genuinely local representation count, not merely the summed additive energy.

**2. An exact invariant fourth-moment polynomial.** Normalize the nonzero input value to \(1\) and write \(f_z(0)=z\). There is exactly one quadruple with four zeros, none with exactly three zeros, and exactly \(4m\) quadruples with two zeros. The identity for \(w(0)\) gives exactly \(4m(1+h)\) quadruples with exactly one zero. The total number of quadruples is \(3q^2-3q+1-2mk\), obtained by summing the local profile; subtracting the other strata gives \(m(3q-8-4h-2k)\) quadruples with no zeros. Complex conjugation symmetry splits the single-zero stratum equally between the two sides. Thus
\[
\boxed{\lVert Tf_z\rVert_4^4=\lvert z\rvert^4+4m\lvert z\rvert^2+4m(1+h)\operatorname{Re}z+m(3q-8-4h-2k)}
\]
Also \(\lVert f_z\rVert_2^2=m+\lvert z\rvert^2\). These equations establish the exact quotient for every complex \(z\), rather than merely for real perturbations.

**3. Global maximization on the fixed space.** If \(h\in\{0,1\}\), then \(1+h>0\) and, at any fixed \(\lvert z\rvert\), the quotient is maximized uniquely by \(z=\lvert z\rvert\ge0\). For \(r\ge0\), differentiation gives
\[
\frac{d}{dr}\frac{r^4+4mr^2+4m(1+h)r+m(3q-8-4h-2k)}{(m+r^2)^2}
=-\frac{4m}{(m+r^2)^3}\left[r^3+3(1+h)r^2+(q-6-4h-2k)r-m(1+h)\right].
\]
The cubic is negative at zero and positive at infinity. Its coefficient-sign sequence has exactly one sign change for every permitted field, whether the linear coefficient is positive, zero, or negative; Descartes' rule therefore gives one and only one positive root. The derivative changes from positive to negative there, establishing the unique global positive radial maximizer and the stated value.

If \(h=-1\), the quotient depends only on \(x=\lvert z\rvert^2\). It is strictly decreasing for \(x\ge0\), since
\[
\frac{d}{dx}\frac{x^2+4mx+m(3q-4-2k)}{(m+x)^2}
=-\frac{2m(x+q-2-2k)}{(m+x)^3}<0.
\]
The maximum is therefore uniquely at \(z=0\). In either case a function supported only at zero has quotient \(1\), strictly smaller than the displayed values, so it creates no additional maximizer. Scalar multiplication accounts for every nonzero maximizer in \(V\).

**4. Failure of constant criticality.** Differentiating at \(r=1\) gives
\[
\left.\frac{d}{dr}\frac{\lVert Tf_r\rVert_4^4}{\lVert f_r\rVert_2^4}\right\rvert_{r=1}=
\frac{4(q-1)}{q^3}\left(1+q\chi(-7)+2\chi(-3)\right).
\]
If \(\chi(-7)=-1\), the bracket is negative for \(q\ge5\); if \(\chi(-7)=+1\), it is positive. The remaining case \(\chi(-7)=0\) occurs in characteristic \(7\), where \(\chi(-3)=1\) and the bracket equals \(3\). Hence the derivative is always nonzero, and the constant function cannot be critical even in the full coefficient space.

## Verification
The standalone file `artifacts/verify.py` implements arithmetic for prime fields and quadratic extensions, builds every ordered pair-sum fiber, checks the two exact local collision profiles, and tests the complete complex weighted fourth-moment polynomial by Gaussian-integer convolution. Run `python artifacts/verify.py` from the extracted package root. Successful execution prints `VERIFY_OK fields=14 Gaussian_integer_fourth_moments=84 local_representation_profiles=14 quadratic_characters=PASS`. These finite tests corroborate the formulas; their validity for every specified finite field follows from the character-sum and optimization proof above, not from enumeration.

## Relationship to prior work
Mockenhaupt–Tao introduced the relevant finite-field extension framework and the even-exponent collision mechanism. Iosevich–Koh treated nondegenerate quadratic surfaces, whereas the present graph has quartic second coordinate. González-Riquelme–Oliveira e Silva proved sharp finite-field inequalities for parabolae, paraboloids, and cones, including noncritical constants on certain origin-completed cones; these are different support varieties, and their inequalities do not specialize to \(\Gamma_4\). Biswas and collaborators studied the full moment curve with all consecutive coordinates, rather than the sparse quartic graph.

A published note, *Exact additive energy of the finite-field quartic graph*, already establishes the total collision count and the constant-input fourth moment on precisely this graph. **Those results are not claimed as new.** The distinction here is the local collision profile, a further arithmetic discriminant \(-7\), and the exact global optimization and equality classification in the natural multiplicatively invariant coefficient subspace. Summed energy cannot by itself determine these weighted quantities. A complete unrestricted \(\ell^2\)-to-\(L^4\) operator norm remains open here.

## Limitations
The result concerns the symmetry-fixed two-orbit subspace, not the full coefficient space; the unrestricted sharp operator norm and its extremizers are not determined. The argument requires characteristic greater than \(3\), but includes characteristic \(7\) as a distinct regime. Historical weighted-additive-energy or group-invariant restriction literature could contain an equivalent result, so this note does not claim exhaustive priority. The supplementary computer checks cover finitely many fields and are not an infinite proof.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first public 18 April 2002, Section 5.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, 2008.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, 2024.
4. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, 2025.
5. *Exact additive energy of the finite-field quartic graph*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.
