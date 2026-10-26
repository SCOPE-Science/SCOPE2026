# Seven-block Bernoulli statistics in a zero-entropy cubic toral skew system

## Finding

Consider the affine map \(T_\alpha:\mathbb T^4\to\mathbb T^4\), for arbitrary real \(\alpha\), given by
\[
T_\alpha(x_0,x_1,x_2,x_3)=(x_0+x_1,\ x_1+x_2,\ x_2+x_3,\ x_3+\alpha)\pmod1.
\]
Draw \(x\) from normalized Haar measure on \(\mathbb T^4\), put \(s(t)=+1\) for \(t\bmod1\in[0,1/2)\) and \(s(t)=-1\) otherwise, and observe the stationary signs \(Z_n=s((T_\alpha^nx)_0)\).

**Theorem.** For every real \(\alpha\), every integer \(k\), and every sign pattern \((\epsilon_0,\ldots,\epsilon_6)\in\{-1,+1\}^7\),
\[
\Pr(Z_k=\epsilon_0,\ldots,Z_{k+6}=\epsilon_6)=2^{-7}.
\]
The seven consecutive signs are thus exactly seven independent fair bits, although the complete stationary symbolic process has entropy rate zero. The conclusion covers all parameters, including rational and irrational \(\alpha\); it is not an asymptotic-independence or finite-grid assertion.

## Assumptions and scope

The phase coordinates \((x_0,x_1,x_2,x_3)\) are independent Haar-uniform circle variables at time zero; subsequent variables are generated deterministically by the displayed affine transformation. Addition is modulo one. The output is the indicated half-circle sign partition, with any choice of endpoint convention producing the same Haar law. Only seven **consecutive** times are asserted to be mutually independent. No corresponding assertion about arbitrary seven-time sets or eight consecutive times is made. The result is a measure-theoretic observation law, not a claim that the symbolic factor is Bernoulli as a process.

## Proof

**1. Polynomial orbit coordinates and invariance.** The linear part of \(T_\alpha\) is an integral unipotent triangular matrix of determinant one, so the affine map preserves Haar measure. Induction gives, for every integer \(n\ge0\),
\[
(T_\alpha^n x)_0=x_0+\binom n1x_1+\binom n2x_2+\binom n3x_3+\binom n4\alpha\pmod1.
\]
Haar invariance reduces the assertion for any starting index \(k\) to the block at indices \(0,\ldots,6\).

**2. Fourier obstruction to a nonzero sign moment.** The bounded half-circle sign \(s\) has mean zero, and its Fourier coefficients vanish at even integers; at odd nonzero integers \(m\) they are \(2/(\pi i m)\). Replace \(s\) by its Fejér approximations. These are uniformly bounded by one and retain exclusively odd nonzero Fourier frequencies. For a nonempty set \(S\subseteq\{0,\ldots,6\}\), every term in the finite Fourier expansion of \(\mathbb E\prod_{j\in S}s((T_\alpha^j x)_0)\) vanishes under Haar integration in \(x_0,x_1,x_2,x_3\), except possibly terms with integer coefficients \(c_j\) that are odd for \(j\in S\), zero otherwise, and satisfy
\[
\sum_{j=0}^6 c_j\binom jr=0\qquad(r=0,1,2,3).
\]
Equivalently, the integral polynomial \(C(z)=\sum_{j=0}^6c_jz^j\) is divisible by \((z-1)^4\).

**3. Exact obstruction lemma.** Suppose a polynomial of degree at most six has all coefficients either zero or odd and is divisible by \((z-1)^4\). Then it is zero. Indeed, write
\[
C(z)=(z-1)^4(a+bz+cz^2),\qquad a,b,c\in\mathbb Z.
\]
Its coefficients at powers three, one, and five, respectively, are
\[
-4a+6b-4c,\qquad b-4a,\qquad b-4c.
\]
The first is even, hence must be zero; therefore \(3b=2(a+c)\) and \(b\) is even. The other two coefficients are now even and must likewise vanish. Thus \(b=4a=4c\), so \(a=c\); substitution into the first equality gives \(16a=0\). Hence \(a=b=c=0\), as claimed. This rules out every potentially surviving Fourier term in step 2. Fejér approximation converges in \(L^1\) under each Haar-uniform phase coordinate, and boundedness permits passing from the finite approximants to the original product. Every nonempty Walsh moment of the seven signs is therefore zero.

**4. Recover the complete seven-bit law.** Walsh inversion on \(\{-1,+1\}^7\) now gives, for each sign pattern,
\[
\Pr((Z_0,\ldots,Z_6)=\epsilon)=2^{-7}\sum_{S\subseteq\{0,\ldots,6\}}\Big(\prod_{j\in S}\epsilon_j\Big)\mathbb E\Big[\prod_{j\in S}Z_j\Big]=2^{-7},
\]
because the empty-set term is one and the other \(127\) moments vanish.

**5. Zero entropy of the full process.** The linear part of \(T_\alpha^n\) has entries bounded by a cubic polynomial in \(n\). For fixed accuracy \(\varepsilon>0\), a mesh with spacing of order \(\varepsilon n^{-3}\) in each of four torus coordinates spans every orbit segment of length \(n\) in the Bowen metric. Its cardinality is at most polynomial of degree twelve in \(n\). Thus \(h_{\mathrm{top}}(T_\alpha)=0\). The Haar measure-theoretic entropy, and hence the entropy rate of its binary observation process, are zero. The seven-block independence therefore coexists with global deterministic dependence.

## Verification

The standalone standard-library program `verify.py` recomputes the complete integer coefficient identities for \((z-1)^4(a+bz+cz^2)\), checks the zero-or-odd obstruction for a finite range as a consistency check, and verifies an exact finite-grid seven-bit histogram. On the \(32^4\) points of the dyadic phase grid at \(\alpha=0\), all \(128\) output words occur exactly \(8192\) times. This last finite-grid identity is **not** used to infer the unrestricted Haar theorem; steps 2–4 supply its proof.

A degree-seven polynomial \((z-1)^4(1+z+z^2+z^3)\) has coefficients \((1,-3,3,-1,-1,3,-3,1)\), all odd. This demonstrates why the coefficient-parity obstruction at degree six does not simply extend one further degree. It does **not** establish that the eighth sign moment is nonzero; the theorem intentionally makes no eight-block optimality claim.

## Relationship to prior work

Anzai's classical 1951 toral-skew-product analysis develops the spectral structure and ergodic examples of skew rotations. Cecchi and Tiedra de Aldecoa (arXiv:1501.06245v1, 2015) study higher-dimensional Furstenberg-type toral skew transformations and their spectral and ergodic properties. Those sources motivate the dynamical setting but do not state the particular half-circle seven-block distribution calculated here. General Fourier orthogonality and the existence of skew transformations are prior techniques; the finite zero-or-odd polynomial lemma and its explicit seven-bit consequence are the assessed result. A related degree-two toral-skew sign observation admits only a three-block universal independence statement and parameter-sensitive four-block behavior, so it does not imply this degree-three result. The priority comparison is limited to inspected literature and accessible indexed records; an unindexed equivalent binary coding may exist.

## Limitations

The proof is exact and does not require Diophantine hypotheses on \(\alpha\). However, the observed partition must be the balanced half circle, and the output times must be consecutive. There is no claim that blocks of length eight are dependent for every parameter, that distinct nonconsecutive septuples are independent, or that the process has positive entropy. Independent scientific validation has not been performed.

## References

1. H. Anzai, *Ergodic skew product transformations on the torus*, Osaka Mathematical Journal **3** (1951), 83–99. DOI: 10.18910/11966. Open full text: https://ir.library.osaka-u.ac.jp/repo/ouka/all/11966/omj03_01_08.pdf.
2. P. A. Cecchi and R. Tiedra de Aldecoa, *Furstenberg transformations on Cartesian products of infinite-dimensional tori*, first public arXiv version 2015-01-26, arXiv:1501.06245v1. https://arxiv.org/pdf/1501.06245v1.
