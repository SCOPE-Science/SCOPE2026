# Phase-rigid sharp Fourier extension for binary-field quadratic conics

## Finding

**Theorem.** Let \(q=2^r\), \(r\ge1\), and let \(F=\mathbb F_q\). Let \(Q:F^2\to F\) be a homogeneous quadratic form whose polar form is nondegenerate, and fix \(j\in F^\times\). Set
\[
S=\{v\in F^2:Q(v)=j\},\qquad M=|S|.
\]
A split form has \(M=q-1\) and a nonsplit form has \(M=q+1\). For any nontrivial additive character \(\chi:F\to\mathbb C\), define
\[
(Ef)(\xi)=\frac1M\sum_{v\in S}f(v)\chi(\xi\cdot v),\qquad \xi\in F^2.
\]
On the input use normalized surface measure \(M^{-1}\sum_{v\in S}\); on the output use *unnormalized* counting measure \(\sum_{\xi\in F^2}\). Then the sharp extension norm satisfies
\[
\boxed{\|E\|_{L^2(S)\to\ell^4(F^2)}^4=\frac{q^2}{M^2}\left(3-\frac2M\right).}
\]
All nonzero equality cases, and only those, have the form
\[
\boxed{f(v)=c\varepsilon_v\quad(v\in S),\qquad c\in\mathbb C^\times,\quad\varepsilon_v\in\{1,-1\}.}
\]
Consequently there are exactly \(2^{M-1}\) complex-projective equality cases (including the single case at \(M=1\)). The large family of independent sign choices is a characteristic-two phenomenon.

The stronger *exact stability identity* holds for every nonzero \(f:S\to\mathbb C\). Write
\[
T=\sum_{v\in S}|f(v)|^2,\qquad a_v=\frac{|f(v)|^2}{T},\qquad z_v=\frac{f(v)^2}{T}.
\]
Then
\[
\boxed{
\left(3-\frac2M\right)-\frac{M^2}{q^2}\frac{\|Ef\|_4^4}{\|f\|_2^4}
=2\sum_{v\in S}\left(a_v-\frac1M\right)^2
 +1-\left|\sum_{v\in S}z_v\right|^2.
}
\]
Both terms on the right are nonnegative; together they measure amplitude imbalance and desynchronization of squared phases. In particular, this formula includes the exact equality classification without requiring a compactness argument.

A structural companion identity is the restricted pair-sum law: for \(s\in F^2\setminus\{0\}\), the number of ordered pairs \((v,w)\in S^2\) with \(v+w=s\) is either \(0\) or \(2\); for \(s=0\), it is exactly \(M\). Hence
\[
|S+S|=1+\binom M2.
\]

## Assumptions and scope

The homogeneity condition is \(Q(tv)=t^2Q(v)\). Its polar form is \(B(u,v)=Q(u+v)-Q(u)-Q(v)\), a nondegenerate alternating bilinear form over \(F\). A form is *split* when it has a nonzero isotropic vector (equivalently two isotropic projective directions), and *nonsplit* otherwise (zero isotropic projective directions). The level \(j\) must be nonzero. A nontrivial additive character is arbitrary; the norm and equality cases are independent of its choice. The displayed \(L^2\) and \(\ell^4\) normalizations are part of the claim.

For \(q=2\), the split level set has \(M=1\), and the nonsplit level set has \(M=3\). No argument silently assumes \(M\ge2\).

## Proof

**1. Cardinality.** The projective line \(\mathbb P^1(F)\) has \(q+1\) directions. A nondegenerate binary quadratic form has exactly two isotropic directions when split and none when nonsplit: after a change of variables a split form is a nonzero multiple of \(xy\), while a nonsplit form is equivalent to a norm form of the separable quadratic field extension. Equivalently, in a symplectic basis it is \(ax^2+xy+cy^2\), whose isotropy equation is a separable quadratic with either zero or two roots. For each nonisotropic projective direction \(Fv\), the equation \(Q(tv)=j\) has a unique solution \(t\in F^\times\), because the Frobenius square map is bijective. Thus \(M=q+1-2=q-1\) or \(M=q+1\), respectively.

**2. Exact pair-sum fibers.** Fix \(s\ne0\) and ask whether \(v\in S\) and \(v+s\in S\). Using characteristic two and the polarization identity gives
\[
Q(v+s)=Q(v)+Q(s)+B(v,s),\qquad B(v,s)=Q(s).
\]
If \(Q(s)=0\), this becomes \(B(v,s)=0\). Since the symplectic orthogonal complement of nonzero \(s\) in the two-dimensional space is precisely \(Fs\), every such \(v\) would have \(Q(v)=0\), contradicting \(j\ne0\). Thus this sum has no representations.

If \(Q(s)\ne0\), the affine equation \(B(v,s)=Q(s)\) defines an affine line \(v_0+Fs\). Along this line,
\[
Q(v_0+ts)=Q(v_0)+Q(s)(t^2+t),\qquad t\in F.
\]
Since \(t^2+t=c\) has either zero or exactly two solutions, differing by \(1\), the fiber has either zero or exactly the two ordered solutions \((v,v+s)\) and \((v+s,v)\). They are distinct because \(s\ne0\). For \(s=0\), characteristic two forces \(w=v\), yielding exactly \(M\) diagonal pairs. Distinct unordered off-diagonal pairs therefore have distinct sums, so the sumset cardinality is \(1+\binom M2\).

**3. Fourth-moment evaluation.** Put \(T=\sum_{v\in S}|f(v)|^2\) and \(U=\sum_{v\in S}f(v)^2\). Character orthogonality in \(F^2\) and the expansion of the fourth power yield
\[
\|Ef\|_4^4=\frac{q^2}{M^4}
\sum_{s\in F^2}\left|\sum_{v+w=s}f(v)f(w)\right|^2.
\]
The zero-sum contribution is \(|U|^2\). Each off-diagonal unordered pair \(\{v,w\}\) contributes \(|2f(v)f(w)|^2=4|f(v)|^2|f(w)|^2\), and none collides with another. Consequently,
\[
\boxed{\|Ef\|_4^4=\frac{q^2}{M^4}
\left(2T^2-2\sum_{v\in S}|f(v)|^4+|U|^2\right).}
\]
The input satisfies \(\|f\|_2^2=T/M\).

**4. Optimal constant and exact extremizers.** Two inequalities are sharp:
\[
\sum_{v\in S}|f(v)|^4\ge\frac{T^2}{M},
\qquad
\left|\sum_{v\in S}f(v)^2\right|^2\le T^2.
\]
The first becomes equality precisely for constant \(|f(v)|\); the second, by triangle equality, becomes equality precisely when all nonzero squared values \(f(v)^2\) have a common argument. Since constant modulus excludes zeros for nonzero \(f\), the simultaneous equality cases are exactly \(f(v)=c\varepsilon_v\) with \(\varepsilon_v=\pm1\). Therefore the displayed sharp norm holds for every \(q,Q,j\). Two sign patterns are complex-scalar equivalent exactly when they differ by a global sign, so there are \(2^{M-1}\) projective patterns.

**5. Deficit identity.** Divide the fourth-moment identity by \(T^2\), use \(\sum_v a_v=1\) and \(\sum_v a_v^2=1/M+\sum_v(a_v-1/M)^2\), and rearrange. The result is exactly the boxed stability formula. The second term is nonnegative because \(|\sum z_v|\le\sum|z_v|=1\). All steps are identities except the explicit two inequalities above.

## Verification

The standalone `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` from the directory containing this report and the checker. It implements five concrete binary fields using listed irreducible polynomials, split and nonsplit forms, every nonzero level in each field, complete ordered-pair-sum enumeration, and direct character sums at smaller sizes. The tested field orders are \(2,4,8,16,32\). The reproducibility output is:

`VERIFY_OK level_sets=114 pair_fibers=114 convolution_patterns=228 direct_fourier=8`

These are finite consistency checks of arithmetic, normalizations, equality profiles, and the exact convolution formula. The proof above is uniform in the extension degree and is not inferred from finite enumeration.

## Relationship to prior work

Iosevich and Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (2008), investigate the same general extension problem and its pair-sum method. Their opening assumptions explicitly impose characteristic greater than two, and Section 4 proves uniform \(L^2\to L^4\) boundedness via a pair-sum bound; their displayed result does not evaluate this characteristic-two sharp constant or its equality and deficit identities.

Koh and Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240 (first posted 22 March 2010), classify admissible extension **exponents** for planar curves. Their Theorem 1.1 assumes odd characteristic and characteristic greater than curve degree, rather than yielding the present characteristic-two exact norm.

González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024), address sharpness and equality for paraboloids, hyperbolic paraboloids, and related surfaces in their stated characteristic ranges, not this binary quadratic conic family. The present problem is distinguished by the collapse of all diagonal sums to zero, a restricted pair-sum rigidity specific to characteristic two, and unconstrained sign choices at equality.

## Limitations

The theorem requires an even-order finite field, a homogeneous quadratic form with nondegenerate polar form, and a nonzero level. It does not cover affine/parabolic curves with degenerate polar forms, zero-level cones, or higher-dimensional quadratic hypersurfaces. It determines the exact \(L^2\to\ell^4\) endpoint under the stated normalization, not every extension exponent. The short pair-sum argument may admit an equivalent formulation in older Sidon-set or finite-geometry language; no exhaustive novelty assertion is made. Numeric examples do not substitute for the proof.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, 2008, arXiv:0804.4505. https://arxiv.org/html/0804.4505v1
2. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, 2010, arXiv:1003.4240. https://arxiv.org/html/1003.4240v3
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, 2024, arXiv:2405.16647. https://arxiv.org/abs/2405.16647
