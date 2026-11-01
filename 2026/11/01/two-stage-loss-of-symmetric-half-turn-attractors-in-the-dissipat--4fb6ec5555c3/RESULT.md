# Two-stage loss of symmetric half-turn attractors in the dissipative Labyrinthic map

## Finding
For the two-harmonic dissipative Labyrinthic map, the symmetry-exchanging period-two family has **two successive, distinct losses of local attraction** after its initial fold. Exact closed-form thresholds describe a sequence with zero, two, one, and zero exponentially attracting half-turn orbits as the forcing amplitude grows. In particular, two sinks emerge at the same fold but are never lost at the same forcing amplitude.

Let \(q=1-\gamma\), \(\rho=\sqrt{1-1/(2a)}\), and
\[
H=\frac{\gamma}{\pi(2a-1)(2-\gamma)},\qquad
s_\pm=\frac{6+H^2\pm H\sqrt{H^2+8}}{2(9+H^2)}.
\]
Set
\[
b_0=\frac{3\sqrt3}{8}(2-\gamma)\rho,\qquad
b_\pm=\frac{(2-\gamma)\rho}{4\sqrt{s_\pm}(1-s_\pm)}.
\]
Then \(0<s_-<1/3<s_+<1\) and strictly \(0<b_0<b_-<b_+\). The complete count of these *symmetry-exchanging half-turn* orbits, with the count of their exponentially attracting members in parentheses, is

| Forcing amplitude | Number of distinct two-cycles (attracting) |
| --- | --- |
| \(0<b<b_0\) | 0 (0) |
| \(b=b_0\) | 2 (0); both nonhyperbolic |
| \(b_0<b<b_-\) | 4 (2) |
| \(b=b_-\) | 4 (1); one other nonhyperbolic |
| \(b_-<b<b_+\) | 4 (1) |
| \(b=b_+\) | 4 (0); one nonhyperbolic |
| \(b>b_+\) | 4 (0); all are saddles |

At each nonhyperbolic boundary the return multipliers are exactly \(1\) and \((1-\gamma)^2\). The two-cycles at the first boundary meet in two nondegenerate folds within the specified symmetry class. The two later thresholds are losses of exponential attraction; no global or off-symmetry bifurcation statement is asserted.

## Assumptions and scope
On \(\mathbb R\times(\mathbb R/\mathbb Z)\) define
\[
\begin{aligned}
I'&=(1-\gamma)I-b\,g(\theta),\\
\theta'&=\theta+a(1-(I')^2)\pmod 1,\\
g(\theta)&=\sin(2\pi\theta)+\sin(6\pi\theta).
\end{aligned}
\]
Throughout, \(1/2<a<1\), \(0<\gamma<1\), and \(b>0\). The odd-harmonic involution is \(S(I,\theta)=(-I,\theta+1/2)\), with \(S^2\) the identity. A *primary-strip half-turn two-cycle* is a distinct least-period-two orbit having a representative \((I,\theta)\) with \(0<|I|<1\) and satisfying \(F(I,\theta)=S(I,\theta)\). This is the precise counting class; other periodic cycles may exist.

## Proof
**1. Symmetry and a forced amplitude.** Since \(g(\theta+1/2)=-g(\theta)\) and the angular increment is even in \(I'\), one has \(F\circ S=S\circ F\). Thus a solution to \(F(z)=S(z)\) is a prime-two orbit (the involution has no fixed points on the cylinder), and its second point is \(S(z)\). In the strip \(0<|I|<1\), \(0<a(1-I^2)<1\); hence the angular half-turn constraint can only be \(a(1-I^2)=1/2\). Consequently \(I=\pm\rho\), where \(0<\rho<1\). Represent each two-cycle uniquely at \(I=+\rho\). The action update now becomes \(b g(\theta)=(2-\gamma)\rho\). Since the right side is positive, its solutions lie in \(\theta\in(0,1/2)\) and, putting \(u=2\pi\theta\in(0,\pi)\), \(t=\sin u\in(0,1)\), reduce to
\[
4t(1-t^2)=\frac{(2-\gamma)\rho}{b}.\tag{1}
\]
The left side has a strict nondegenerate maximum \(8/(3\sqrt3)\) at \(t=1/\sqrt3\). Each \(t\in(0,1)\) gives two angles \(u\) and \(\pi-u\), including at the maximum where the two distinct angular maxima remain. At either angular maximum, \(g\prime\prime(\theta)=-64\pi^2/\sqrt3\ne0\), while the forcing-level derivative with respect to \(b\) is nonzero. This proves the zero/two/four counts and \(b_0\), and establishes two nondegenerate symmetry-class folds there.

**2. Exact return spectrum.** At \(I=\rho\), set \(h=b g'(\theta)\) and \(c=2a\rho\); at the second point \(S(I,\theta)\), the derivative of \(g\) reverses sign. The one-step derivatives are
\[
A=\begin{pmatrix}q&-h\\cq&1-ch\end{pmatrix},\qquad
B=\begin{pmatrix}q&h\\-cq&1-ch\end{pmatrix}.
\]
Writing \(k=ch=2ab\rho g'(\theta)\), direct multiplication gives
\[
\det(BA)=q^2,\qquad
\operatorname{tr}(BA)=1+q^2+k^2-2\gamma k.\tag{2}
\]
For \(0<q<1\), the strict Schur inequalities \(1-\det(BA)>0\), \(1-\operatorname{tr}(BA)+\det(BA)>0\), and \(1+\operatorname{tr}(BA)+\det(BA)>0\) reduce exactly to \(0<k<2\gamma\). Indeed the middle inequality equals \(k(2\gamma-k)>0\); the last is at least \((2-\gamma)^2>0\). When \(k<0\) or \(k>2\gamma\), the trace exceeds \(1+q^2\), so a real multiplier is greater than one and the other is smaller than one: these are saddles. At \(k=0\) or \(2\gamma\) the multipliers are \(1,q^2\).

**3. Exactly two initially attracting branches.** Differentiation gives \(g'(\theta)=8\pi\cos u(1-3t^2)\). For each solution \(t\) of (1), the two angles have opposite derivative signs. Thus, for \(b>b_0\), two branches have \(k<0\) and are saddles, while two have \(k>0\) and are sinks until \(k=2\gamma\). At the fold all four limiting branches have \(k=0\).

**4. Both stability crossings are unique.** With \(s=t^2\), using (1) to eliminate \(b\) from positive \(k\) gives
\[
k=2\pi(2a-1)(2-\gamma)f(s),\quad
f(s)=\frac{|1-3s|}{\sqrt{s(1-s)}}.
\]
The derivative
\[
\frac{d}{ds}f(s)^2=\frac{(s+1)(3s-1)}{s^2(s-1)^2}
\]
shows that \(f\) decreases on \((0,1/3)\), vanishes at \(1/3\), and increases on \((1/3,1)\), diverging at each outer endpoint. Each of the two \(t\)-branches moves monotonically away from \(1/\sqrt3\) as \(b\) increases; each \(k\) therefore grows strictly from zero to infinity. The equation \(k=2\gamma\) is \(f(s)=H\), equivalently to
\[
(9+H^2)s^2-(6+H^2)s+1=0.
\]
Its two roots are exactly \(s_-<1/3<s_+\), and substitution into (1) yields \(b_-\) and \(b_+\). Both exceed \(b_0\).

**5. Strict ordering, not merely distinct numerical roots.** At a fixed \(b>b_0\), let \(x<1/\sqrt3<y\) be the two \(t\)-solutions of (1). Equality \(x-x^3=y-y^3\) implies \(x^2+xy+y^2=1\). Write \(r=y/x>1\). Direct elimination gives the positive-branch growth-rate ratio
\[
\frac{f(x^2)}{f(y^2)}=\frac{r+2}{2r+1}\sqrt r>1,
\]
where the last strict inequality follows upon squaring from \(r(r+2)^2-(2r+1)^2=r^3-1>0\). Thus the low-amplitude-\(t\) branch reaches \(k=2\gamma\) strictly before the high-\(t\) branch, so \(b_-<b_+\). The listed stability census follows.

## Verification
Run \(\texttt{python verify.py}\) with Python 3, SymPy, and NumPy. The standalone script checks the determinant and trace identities, the forcing identity and derivative, the monotonicity and ordering identities, and recomputes actual two-step trajectories and multipliers at four parameter pairs in three post-fold forcing regions, together with the pre-fold absence. It evaluated 48 explicit cycles, finding sink counts 2, 1, and 0 in the predicted regions. These finitely many checks corroborate, but do not replace, the symbolic proof or establish any global dynamics.

For a concrete parameter slice, \(a=11/20\), \(\gamma=4/5\), the thresholds are approximately \(b_0=0.235004835540\), \(b_-=0.305323158518\), \(b_+=0.332417122942\). Thus \(b=0.27\) has two exponentially attracting cycles of the stated class; \(b=0.32\) has one; \(b=0.35\) has none.

## Relationship to prior work
Souza et al. [1] introduce and numerically explore this dissipative two-harmonic map, its odd-harmonic symmetry, coexistence of attractors, and periodic windows; no exact closed-form stability census of the symmetry-exchanging half-turn two-cycles is given in its inspected full text. Martins et al. [2] treat the conservative Labyrinthic map and its resonance structure, without the dissipative return criterion (2). Earlier work [3] on dissipative Labyrinthic dynamics discusses shearless attractors and symmetry but no identified two-stage half-turn threshold. Mugnaine et al. [4] study dissipative non-twist coexistence principally in the single-harmonic specialization; their reported numerical two-cycles do not determine the present two-harmonic roots. Kato and de Carvalho [5] study transport barriers and coexisting shearless attractors; only their abstract was accessible for this comparison. These distinctions are differences in mathematical statements and assumptions, not a proof of global historical novelty.

## Limitations
The result counts only cycles fixed under the relation \(F(z)=S(z)\) with \(0<|I|<1\), not every period-two orbit, any other resonance strip, or all attractors. The first fold statement is within this restricted symmetry class; the later unit-multiplier crossings establish loss of exponential stability, but not the type of any off-symmetry bifurcation. No basin-volume or global-attraction statement is made. A relevant 2019 paper [5] was available only in abstract, so priority must remain provisional pending full-source comparison. Independent audit has not been performed.

## References
[1] L. F. B. Souza, R. Egydio de Carvalho, R. L. Viana, and I. L. Caldas, “Shearless and periodic attractors in the dissipative Labyrinthic map,” *Chaos* **34**, 123132 (published online 2024-12-05), doi:10.1063/5.0225577; complete author preprint arXiv:2610.26534 (2026-10-19).

[2] C. C. Martins et al., “Labyrinthic standard non-twist map,” *J. Phys. A* **44**, 045102 (2011), doi:10.1088/1751-8113/44/4/045102.

[3] R. Egydio de Carvalho and C. Abud, “Robust attractor of non-twist systems,” *Physica A* **440**, 42–48 (2015), doi:10.1016/j.physa.2015.08.008.

[4] M. Mugnaine et al., “Curry–Yorke route to shearless attractors and coexistence of attractors in dissipative nontwist systems,” *Chaos* **31**, 023125 (2021), doi:10.1063/5.0035303.

[5] L. K. Kato and R. Egydio de Carvalho, “Transport barriers with shearless attractors,” *Phys. Rev. E* **99**, 032218 (2019), doi:10.1103/PhysRevE.99.032218 (abstract only inspected).
