# Exact fibers of four-point quadratic derivative phase retrieval

## Finding

Let \(\mathcal M(P)\) consist of the eight intensities \(\bigl(|P(i^j)|^2,|P'(i^j)|^2\bigr)\), for \(j=0,1,2,3\), of a complex polynomial \(P(z)=a+bz+cz^2\). Polynomials are identified only under multiplication by a common complex scalar of modulus one. **Every fiber of \(\mathcal M\) consists of one, two, or three phase classes; three is attained and is the maximum.** The full classification is:

1. A polynomial \(P=bz\) with \(b\ne0\), or one of its ambiguous partners \(P=a+cz^2\) with \(ac\ne0\), \(|a|^2=3|c|^2\), and \(\operatorname{Re}(a\overline c)=0\), lies in a fiber of **exactly three** classes. In particular, \(z\), \((z^2+i\sqrt3)/2\), and \((z^2-i\sqrt3)/2\) have identical measurements.
2. If \(b=0\), \(ac\ne0\), and \(\operatorname{Im}(a\overline c)\ne0\), and the triple-fiber condition in item 1 does not hold, the fiber has **exactly two** classes, obtained by reflecting the relative phase of \(c\) against that of \(a\).
3. If \(abc\ne0\), \(|a|^2=3|c|^2\), \(\operatorname{Re}(a\overline c)=0\), and \(|b|\ne2|c|\), the fiber has **exactly two** classes. Its other representative is \(Q(z)=a/t+tbz+(c/t)z^2\), where \(t=2|c|/|b|\).
4. **All other fibers are singletons**, including the zero polynomial. The listed conditions are disjoint after giving the triple case precedence.

Thus the entire noninjectivity locus, not just an individual collision, is explicit, and the fiber size never exceeds three. In particular the four-point measurement is injective outside a proper real-algebraic exceptional set (though never universally injective).

## Assumptions and scope

The field is \(\mathbb C\); coefficients \(a,b,c\) are arbitrary, with leading coefficients permitted to vanish. The sampling grid is exactly the fourth roots of unity \(\{1,i,-1,-i\}\). Both channels measure squared moduli, with the ordinary complex derivative \(P'\). No data are rescaled or assumed noiseless beyond exact mathematical measurement equality. Equality modulo phase means \(Q=e^{i\theta}P\) for one real \(\theta\); amplitude rescaling is **not** allowed. The associated primary research context has MSC2020 code 30D05.

## Proof

Write \(f_j=|P(i^j)|^2\) and \(g_j=|P'(i^j)|^2\). From their normalized four-point discrete Fourier coefficients, define
\[
 S=\tfrac14\sum_j f_j,\quad U=\tfrac14\sum_j f_j i^{-j},\quad T=\tfrac14\sum_j(-1)^jf_j,\quad H=\tfrac14\sum_jg_j,\quad V=\tfrac14\sum_jg_j i^{-j}.
\]
Direct multiplication, remembering that Fourier indices \(2\) and \(-2\) alias on this grid, yields the five **exact** identities
\[
 S=|a|^2+|b|^2+|c|^2,\quad U=b\overline a+c\overline b,\quad T=2\operatorname{Re}(c\overline a),\quad H=|b|^2+4|c|^2,\quad V=2c\overline b.
\]
The remaining Fourier coefficients are determined by conjugate symmetry or vanish, so \((S,U,T,H,V)\) and the eight measurements determine each other. In particular this is an exact reduction, not merely a set of necessary conditions.

**First case: \(b\ne0\).** Put \(x=|b|^2>0\), \(A=U-V/2=b\overline a\), and \(C=V/2=c\overline b\). After a global phase rotation set \(b=\sqrt x>0\); then
\[
 a=\overline A/\sqrt x,\qquad c=C/\sqrt x.
\]
The entire inverse problem is now to find all positive \(x\) obeying
\[
 x^2-Sx+|A|^2+|C|^2=0,\quad x^2-Hx+4|C|^2=0,\quad Tx=2\operatorname{Re}(AC). \tag{1}
\]
Conversely every positive solution gives precisely one phase class and the correct complete measurements, by the identities above. If \(C\ne0\), two distinct solutions of (1) force the two monic quadratics to be identical, and force the last equation to have zero right and left sides. Thus
\[
 S=H,\quad |A|^2=3|C|^2,\quad \operatorname{Re}(AC)=T=0.
\]
In coefficient language these are exactly \(|a|^2=3|c|^2\) and \(\operatorname{Re}(a\overline c)=0\). The two roots multiply to \(4|C|^2\); starting with \(x=|b|^2\), the other is \(x'=4|c|^2\). They are distinct exactly when \(|b|\ne2|c|\), and rewriting the second reconstructed polynomial in the original phase gauge gives \(Q(z)=a/t+tbz+(c/t)z^2\) with \(t=2|c|/|b|\). If \(C=0\), then \(c=0\), and \(H=x\) uniquely fixes \(x\), hence the phase class. Therefore a nonmonomial \(P\) with \(b\ne0\) has at most two representatives, with exactly the described conditions for two.

**Second case: \(b=0\).** We then have \(U=V=0\), \(H=4|c|^2\), \(S=|a|^2+|c|^2\), and \(T=2\operatorname{Re}(c\overline a)\). Therefore \(|a|\), \(|c|\), and the cosine of their relative phase are fixed. When \(ac\ne0\), precisely two relative phases remain if \(\operatorname{Im}(a\overline c)\ne0\); otherwise there is one. With \(a\ne0\), an explicit alternative is \(a+(a/\overline a)\overline c\,z^2\), up to the original global phase. If either \(a\) or \(c\) vanishes, the binomial branch is unique.

**Cross-branch collisions.** If the data of a \(b=0\) polynomial agree with those of a polynomial with \(b'\ne0\), the equality \(V=2c'\overline{b'}=0\) forces \(c'=0\), and \(U=b'\overline{a'}=0\) forces \(a'=0\). Hence the other polynomial must be \(b'z\). Equality of \(H,S,T\) is then equivalent to \(|b'|=2|c|\), \(|a|^2=3|c|^2\), and \(\operatorname{Re}(a\overline c)=0\). Under these conditions there are exactly two inequivalent binomial phases (since \(ac\ne0\) and their relative phase is in quadrature), plus the single monomial class: a three-class fiber. The converse follows by substitution. If \(P=bz\), these are likewise its only possible partners. Finally, \(P=0\) gives all-zero intensities, forcing \(Q=0\). This exhausts all cases and proves the classification and sharp bound.

## Verification

Three standalone Python programs accompany the result. `symbolic_four_sample.py` checks all five Fourier coefficient identities as polynomial identities in six independent formal coefficient variables. `verify_four_sample.py` checks the full-support two-class pair, the cross-branch three-class family, a binomial two-class collision, and the collapsed-discriminant case; it also checks 5,000 deterministic integer-coefficient examples against direct Fourier sampling and reconstructs 500 generic examples by the rational inverse. `finite_grid_check.py` also independently enumerates 15,625 bounded Gaussian-integer coefficient triples with exact integer intensities. The latter two scripts use only the Python standard library; the symbolic script uses SymPy. Numerical checks corroborate the derivation; the all-coefficient assertion follows from the symbolic identities and the complete case analysis, **not** from finite testing.

## Relationship to prior work

Jaming and Rathmair, *Uniqueness of phase retrieval from three measurements* (first public preprint 2022-05-18), Section 3.1, prove universal reconstruction from five samples per channel in degree two (their Proposition 3.2) and give a four-sample counterexample (Lemma 3.3 and Proposition 3.4). That counterexample is one pair in the three-class fiber exhibited above. The present theorem instead classifies **every** four-sample fiber, proves the sharp cardinality bound of three, identifies both distinct exceptional mechanisms, and supplies an explicit inverse. It neither claims four-sample universal injectivity nor reclaims the previously established sample threshold. Király and Ehler treat generic algebraic phase retrieval and inversion for broadly varying measurement frames; their generic results do not supply this fixed-grid fiber census.

## Limitations

Only quadratic polynomials and the four equally spaced unit-circle nodes are treated. The theorem provides an exact noiseless inverse and ambiguity census; it does not establish quantitative stability under noise, nor characterize degrees three or higher, nor claim universal uniqueness with four nodes. The exceptional set includes genuine two-class fibers even with all coefficients nonzero; a generic injectivity statement alone would conceal these.

## References

1. Philippe Jaming and Martin Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753v1, 18 May 2022, Section 3.1, especially Lemma 3.3, Proposition 3.4 and Question 3.5; subsequent journal publication in *Advances in Computational Mathematics* 49 (2023), article 47. https://arxiv.org/abs/2205.08753
2. Franz J. Király and Martin Ehler, *The Algebraic Approach to Phase Retrieval, and Explicit Inversion at the Identifiability Threshold*, arXiv:1402.4053v1, 17 February 2014, Sections 1–2. https://arxiv.org/abs/1402.4053
