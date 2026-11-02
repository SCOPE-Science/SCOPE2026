# Arithmetic phase-retrieval rigidity on a single hyperbola, with the sharp exceptional degree

## Finding

Consider one right branch of the real hyperbola
\[
\Gamma_{a,b}=\{x+iy:x^2/a^2-y^2/b^2=1,\ x>0\},\qquad a,b>0.
\]
Let \(\theta=\arctan(b/a)\in(0,\pi/2)\). Two complex polynomials \(P,Q\) have the same labelled magnitudes at every point of \(\Gamma_{a,b}\) exactly when their reduced rational quotient has the classification below (with the zero-polynomial case treated separately).

**Irrational-slope theorem.** If \(\theta/\pi\notin\mathbb Q\), then equality of magnitudes implies \(P=\lambda Q\) for a constant \(\lambda\) with \(|\lambda|=1\). This holds without a bound on their degrees.

**Exact rational-angle fiber theorem.** If \(\theta/\pi=p/q\) in lowest terms, set
\[
m=\frac{q}{\gcd(q,2)},\quad c=\frac{a+ib}{2},\quad s=\frac{a^2+b^2}{4},\quad r=\frac{\overline c}{c},\quad \varepsilon=r^m\in\{-1,1\}.
\]
Define Dickson polynomials by \(D_0(z,s)=2\), \(D_1(z,s)=z\), and
\[
D_{j+1}(z,s)=zD_j(z,s)-sD_{j-1}(z,s)\quad(j\ge1),
\]
and define \(T_m(z)=D_m(z,s)\) when \(\varepsilon=1\), or \(T_m(z)=-iD_m(z,s)\) when \(\varepsilon=-1\). Then \(T_m\) is a degree-\(m\) polynomial real-valued on \(\Gamma_{a,b}\). For nonzero \(P,Q\), equality of magnitudes on \(\Gamma_{a,b}\) is equivalent to
\[
\frac{P(z)}{Q(z)}=R(T_m(z))
\]
as a rational-function identity, for a rational function \(R\) satisfying
\[
R(t)\overline{R(\overline t)}=1
\]
as an identity wherever both sides are defined. A nonconstant such quotient in reduced form has degree \(m\deg R\), so no ambiguity is possible below degree \(m\); the pair \(P=T_m+i\), \(Q=T_m-i\) realizes ambiguity at degree exactly \(m\).

**Arbitrary finite samples.** If \(n\ge0\) and either \(\theta/\pi\notin\mathbb Q\) or \(\theta/\pi=p/q\) with \(n<m\), then magnitudes at any \(4n+1\) distinct points of one branch identify every polynomial of degree at most \(n\) up to global phase. If \(n\ge m\), no selection of points confined to that hyperbola can have universal uniqueness. Translations, rotations, and positive rescalings preserve the conclusions and the degree cutoff.

## Assumptions and scope

All measurements are exact and labelled by locations on one branch. Polynomials may have arbitrary complex coefficients. The quotient of nonzero polynomials is reduced by cancelling common factors before its degree is discussed; equality of magnitudes forbids any pole of the reduced quotient on the measurement branch. The zero polynomial is distinguished from every nonzero polynomial because a nonzero polynomial cannot vanish on the entire branch. A constant unimodular multiple is the only declared equivalence. The hyperbola is nondegenerate and has positive, finite semiaxes, so the two asymptote directions are distinct.

For a reduced nonconstant rational function \(H=P/Q\), \(\deg H\) means the maximum of the degrees of its coprime numerator and denominator. For rational \(R\), \(R^{\#}(t)=\overline{R(\overline t)}\); the real-line-inner condition is the rational identity \(RR^{\#}=1\), not a claim of holomorphy in a half-plane.

## Proof

**1. Two involutions from one hyperbola.** Parameterize its right branch by \(w>0\):
\[
z(w)=cw+\frac{\overline c}{w},\quad c=\frac{a+ib}{2},\qquad w=e^u,
\]
so that \(\operatorname{Re}z=a\cosh u\) and \(\operatorname{Im}z=b\sinh u\). Put \(r=\overline c/c=e^{-2i\theta}\), and \(h(w)=H(z(w))\). The rational parametrization has deck involution \(\tau(w)=r/w\), hence \(h(\tau(w))=h(w)\).

For a rational function \(f(w)\), let \(f^{\#}(w)=\overline{f(\overline w)}\). The equality \(|H(z(w))|=1\) for all \(w>0\), away from finitely many zeros, extends by the rational identity theorem to \(h(w)h^{\#}(w)=1\). But
\[
z^{\#}(w)=\overline c\,w+\frac c w=z(1/w).
\]
Consequently \(h^{\#}\) is invariant under the conjugate deck map \(\tau^{\#}(w)=\overline r/w\). Since \(h=1/h^{\#}\), \(h\) is invariant under both \(\tau\) and \(\tau^{\#}\), and therefore under their composition \(w\mapsto r^2w\). No assumptions about isolated zeros or poles were suppressed: the arguments are identities of rational functions and extend across removable points.

**2. Irrational angle.** If \(\theta/\pi\) is irrational, then \(r^2=e^{-4i\theta}\) has infinite order. A nonconstant rational function has finite fibers over a generic value and therefore cannot be invariant under infinitely many distinct rotations of a generic nonzero argument. Hence \(h\), and thus \(H\), is constant. The unit-modulus condition makes that constant unimodular.

**3. Exact finite invariant field.** Suppose \(r^2\) has order \(m\), equivalently \(\theta/\pi=p/q\) and \(m=q/\gcd(q,2)\). The transformations \(w\mapsto r^2w\) and \(w\mapsto r/w\) generate a dihedral group of order \(2m\) acting faithfully on the rational function field \(\mathbb C(w)\). Set \(u=w^m\), \(\varepsilon=r^m=\pm1\). Invariance under \(w\mapsto r^2w\) says precisely \(h\in\mathbb C(u)\); the remaining reflection sends \(u\mapsto\varepsilon/u\). Its fixed field is \(\mathbb C(u+\varepsilon/u)\): indeed \(u\) solves a quadratic over that field, and the displayed involution swaps its generic roots. Thus
\[
h(w)=R_0\!\left(w^m+\frac{\varepsilon}{w^m}\right)
\]
for some rational \(R_0\).

The recurrence defining \(D_j\) gives, by induction,
\[
D_m(z(w),s)=c^mw^m+\overline c^{\,m}w^{-m}=c^m\left(w^m+\frac{\varepsilon}{w^m}\right).
\]
Therefore \(H(z)=R(T_m(z))\) for some rational \(R\); equality after substituting the nonconstant rational function \(z(w)\) implies equality in \(\mathbb C(z)\). Since \(\overline c^{\,m}=\varepsilon c^m\), the number \(c^m\) is real for \(\varepsilon=1\), and purely imaginary for \(\varepsilon=-1\). Hence the displayed choice of \(T_m\) is real on the entire branch. Its image contains a real interval, so \(|R(T_m(z))|=1\) there implies the rational identity \(RR^{\#}=1\). The converse follows immediately because \(T_m\) takes real values on the branch and a rational real-line-inner function has modulus one at every real point where it is finite. Such an \(R\) cannot have an uncancelled real pole, since \(RR^{\#}=1\).

**4. Sharp degree barrier and witness.** The map \(T_m\) is a polynomial of degree \(m\); degrees of nonconstant rational maps multiply under composition. Thus \(\deg H=m\deg R\) when \(R\) is nonconstant, forcing \(\max(\deg P,\deg Q)\ge m\). Conversely \(P(z)=T_m(z)+i\) and \(Q(z)=T_m(z)-i\) are distinct, not globally phase-related, and have the same modulus at every point of \(\Gamma_{a,b}\). They both have degree \(m\). When \(\theta=\pi/4\) and \(a=b=1\), for example, \(m=2\), \(T_m(z)=-i(z^2-1)\), and the same conclusion is visible from \(\operatorname{Re}(z^2)=1\) on the hyperbola.

**5. Finite-sample bound.** For polynomials of degree at most \(n\), the difference of squared moduli along \(z(w)\), evaluated for real \(w>0\), is a Laurent polynomial with exponents between \(-2n\) and \(2n\). Multiplication by \(w^{2n}\) yields an ordinary polynomial of degree at most \(4n\). Any \(4n+1\) distinct branch points correspond to distinct positive \(w\), so equality of moduli at these points forces this polynomial to vanish identically. The continuous classification then gives the phase conclusion for \(n<m\) or irrational angle. The constructed degree-\(m\) pair proves failure for every \(n\ge m\). Composing with a Euclidean similarity preserves polynomial degree and magnitudes, proving the coordinate-invariant statement.

## Verification

The companion `verify_hyperbola.py` uses exact symbolic arithmetic and SymPy. It verifies the Dickson recurrence and Laurent identity, the order of \(r^2\), real-valuedness of \(T_m\) on the parameter line, and explicit colliding pairs at rational angles \(\pi/4\), \(\pi/6\), \(\pi/8\), and \(\pi/3\). It also checks the \(4n\)-degree Laurent reduction for representative pairs through degree five and a nonresonant rational-parameter example. The test is supplemental: it cannot verify the infinite-order argument or all dimensions of the rational-function classification. Those are proven in the preceding algebraic steps.

## Relationship to prior work

Chalendar and Partington [1] prove phase rigidity on two intersecting lines or smooth arcs at irrational crossing angles, along with two-circle and parallel-line configurations. Their intersection condition is local at a finite crossing; the present data lie on a single nonintersecting branch of an unbounded conic, and the sharp finite-degree arithmetic threshold and complete quotient field are not supplied by their theorems. Liehr [2] proves uniqueness criteria on unions of parallel straight lines and translates, a different geometry with different reflection groups. Orevkov and Pakovich [3] study rational-function lemniscates and intersections, with a broad algebraic factorization perspective; their stated results do not directly classify polynomial quotient functions unimodular on an arbitrary prescribed hyperbola, nor the first exceptional polynomial degree.

The complexified hyperbola's deck transformation has a unit-modulus multiplier and can generate a finite rotation group, unlike the strict contracting dilation in a noncircular ellipse. This change is precisely what creates arithmetic resonance; the general reflection-group method is background rather than a novelty claim.

## Limitations

A general theorem on rational functions with prescribed real algebraic lemniscate components might imply the classification after nontrivial specialization. Only polynomial signals, exact magnitude equality and real nondegenerate hyperbolas are covered. The finite \(4n+1\) sample bound is sufficient rather than optimal. The theorem makes no quantitative stability claim under perturbations or noise, no classification of all polynomial pairs without first taking their rational quotient, and no extension to arbitrary entire functions.

## References

[1] I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, first posted 2024-03-24; Canadian Mathematical Bulletin 67 (2024), 927–935. https://arxiv.org/abs/2403.16255

[2] L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, Bulletin of the London Mathematical Society 56 (2024), 3316–3330, first published 2024-08-13. https://doi.org/10.1112/blms.13134

[3] S. Orevkov and F. Pakovich, *On intersection of lemniscates of rational functions*, arXiv:2309.04983, first posted 2023-09-10. https://arxiv.org/abs/2309.04983
