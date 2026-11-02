# Generator-refined Euler series and extremal strata of fat-node punctual Hilbert schemes

## Finding

For every \(u,v\ge1\), let \(R_{u,v}=\mathbb C[[x,y]]/(x^uy^v)\), and let \(\mathcal H_n(R_{u,v})\) be the punctual Hilbert scheme of colength-\(n\) ideals. Write \(\mathfrak m=(x,y)R_{u,v}\), \(\mu(I)=\dim_{\mathbb C}I/\mathfrak m I\) and \(\mathcal H_{n,r}=\{I\in\mathcal H_n:\mu(I)=r\}\). Let \(\chi_c\) denote compactly supported complex-topological Euler characteristic. Define \((a;q)_j=\prod_{i=0}^{j-1}(1-aq^i)\), \(P_j(q)=(q;q)_j\), and

\[
B_j(q,z)=\frac{((1-z)q;q)_j}{P_j(q)},\qquad T_{u,k}(q,z)=\frac{q^{(u+1)k}((1-z);q)_k}{P_k(q)}.
\]

Then, as a formal power series in \(q\) with coefficients in \(\mathbb Z[z]\),

\[
\boxed{\sum_{n\ge0}\sum_{r\ge1}\chi_c(\mathcal H_{n,r})q^nz^r
=zB_u(q,z)\sum_{k=0}^{v}T_{u,k}(q,z)
+(1-z)(B_u(q,z)-B_{u-1}(q,z))T_{u,v}(q,z).}
\]

Moreover \(\mu(I)\le u+v\) for **every** finite-colength ideal, not merely the torus-fixed ones, and

\[
\boxed{\sum_{n\ge0}\chi_c(\mathcal H_{n,u+v})q^n
=\frac{q^{\binom{u+v}{2}}}{P_u(q)P_v(q)}.}
\]

This top generator number is attained first at colength \(\binom{u+v}{2}\), by the power \(\mathfrak m^{u+v-1}\). For the illustrative bidegree \((u,v)=(3,6)\), the largest generator number is \(9\), and its first three Euler coefficients, at colengths \(36,37,38\), are \(1,2,5\). All formulas are symmetric under swapping \(u\) and \(v\), although the first displayed expression uses an asymmetric row decomposition.

## Assumptions and scope

The base field is \(\mathbb C\). The punctual Hilbert scheme means finite-length subschemes supported at the closed point of the fat-node curve germ; it is a complex finite-type scheme for every fixed \(n\). The constructible generator-number locus has a well-defined additive Euler characteristic, even if it is not smooth. For \(n=0\), the unique ideal is \(I=R_{u,v}\) and \(\mu(I)=1\). The exponent of \(q\) records colength and that of \(z\) records the **minimal number of ideal generators in the quotient ring**, not the ambient number of generators in \(\mathbb C[[x,y]]\), the contact length, or a motivic weight.

## Proof

**1. Torus localization to partitions.** The diagonal algebraic torus \((\mathbb C^*)^2\) acts on the punctual Hilbert scheme and preserves \(\mu\). For complex finite-type torus varieties, the additive compactly supported Euler characteristic of an invariant constructible locus equals that of its torus-fixed subset (stratify nonfixed loci into positive-dimensional torus orbits, each of Euler characteristic zero). The torus-fixed ideals of \(R_{u,v}\) are precisely monomial ambient ideals \(J\supseteq(x^uy^v)\). Associate a Young diagram \(\lambda=(\lambda_1\ge\lambda_2\ge\dots\ge0)\) of size \(n\), with \(\lambda_{v+1}\le u\); each \(\lambda_i\) is the length of the standard monomial row of \(y\)-degree \(i-1\). Conversely every such diagram defines a unique fixed ideal.

**2. Exact minimal-generator correction.** For an ambient monomial ideal \(J\), its minimal generator number is \(1+d(\lambda)\), where \(d(\lambda)\) is the number of distinct positive row lengths, including the empty partition convention \(d(\varnothing)=0\). Quotienting by \((x^uy^v)\) removes one minimal generator precisely when that monomial is itself a minimal generator of \(J\), equivalently

\[
\lambda_v>u,\qquad \lambda_{v+1}=u.
\]

Thus \(\mu(J/(x^uy^v))=1+d(\lambda)-\delta(\lambda)\) with this exact corner indicator \(\delta\in\{0,1\}\). No claim about all nonmonomial ideals is needed for this combinatorial identity.

**3. Count restricted diagrams.** Let \(k\) be the number of parts of \(\lambda\) strictly greater than \(u\). The containment restriction is exactly \(0\le k\le v\). The parts of size \(1,\ldots,u\) occur arbitrarily, with each *distinct* size contributing one factor \(z\). Their generating function is

\[
\prod_{j=1}^{u}\left(1+\frac{zq^j}{1-q^j}\right)=B_u(q,z).
\]

For exactly \(k\) parts greater than \(u\), with each distinct upper part size contributing one factor \(z\), the ordinary \(q\)-binomial identity yields

\[
[t^k]\prod_{j=u+1}^{\infty}\frac{1+(z-1)tq^j}{1-tq^j}
=T_{u,k}(q,z).
\]

The factor \(z\) for the baseline ambient generator gives \(zB_u\sum_{k=0}^vT_{u,k}\). The exceptional corner of step 2 requires \(k=v\) and presence of a part of size exactly \(u\); its lower-part series is \(B_u-B_{u-1}\), and changing its weight from \(z^{1+d}\) to \(z^d\) gives exactly the correction \((1-z)(B_u-B_{u-1})T_{u,v}\). This proves the full two-variable identity for every \(n,u,v\).

**4. Global generator ceiling.** Put \(N=u+v\) and \(\ell=x+y\), a nonzerodivisor of \(R_{u,v}\). The ring \(R_{u,v}/\ell R_{u,v}\cong\mathbb C[[x]]/(x^N)\) has length \(N\). For \(M=R_{u,v}/I\), the exact sequence induced by multiplying \(0\to I\to R_{u,v}\to M\to0\) by \(\ell\) gives

\[
0\to\ker(\ell:M\to M)\to I/\ell I\to R_{u,v}/\ell R_{u,v}\to M/\ell M\to0.
\]

Because \(M\) has finite length, the kernel and cokernel of its multiplication by \(\ell\) have equal length. Therefore \(\operatorname{length}(I/\ell I)=N\), so \(\mu(I)=\dim I/\mathfrak m I\le N\). For \(I=\mathfrak m^{N-1}\), the relation \(x^uy^v\) starts in degree \(N\), giving exactly \(N\) independent degree-\(N-1\) minimal generators, and \(\operatorname{length}(R_{u,v}/I)=\binom N2\).

**5. Top-generator coefficient.** A fixed diagram can attain \(\mu=N\) in exactly three mutually exclusive cases: (a) \(k=v-1\), all lower sizes \(1,\ldots,u\) appear, and its \(v-1\) upper parts are distinct; (b) \(k=v\), all lower sizes \(1,\ldots,u-1\) appear but \(u\) does not, and the \(v\) upper parts are distinct; (c) \(k=v\), all lower sizes \(1,\ldots,u\) appear, the \(v\) upper parts are distinct, and the corner correction removes one generator. The respective univariate series, with \(E=\binom{u+v}{2}\), are

\[
\frac{q^E}{P_u P_{v-1}},\qquad
\frac{q^{E+v}}{P_{u-1}P_v},\qquad
\frac{q^{E+u+v}}{P_u P_v}.
\]

Upon common denominator \(P_uP_v\), their numerators add to \((1-q^v)+q^v(1-q^u)+q^{u+v}=1\). This proves the sharp product formula, including the boundary cases \(u=1\) or \(v=1\).

## Verification

The accompanying standalone `verify.py`, using only the Python standard library, implements two independent finite combinatorial routes: (i) direct enumeration of every restricted Young diagram and its *quotient-ring* corner-corrected generator number; (ii) exact truncated formal-series arithmetic for the closed generating function. For all 30 pairs \(1\le u\le5\), \(1\le v\le6\) and all colengths \(0\le n\le38\), both routes agree on every coefficient (4,679 nonzero bivariate coefficients). The same computation checks the symmetric interchange of the branches and the extremal product coefficient-by-coefficient. The verified standard output begins with `VERIFY_OK`.

For reproducibility, run `python3 verify.py` from the extracted artifact directory. The finite verification is **not** substituted for the preceding infinite proof. In particular, the global bound for nonmonomial ideals uses a separate exact-sequence argument.

## Relationship to prior work

Luan, *Hilbert scheme of points on non-reduced nodal curves* (arXiv:2604.03111; first publicly submitted 2026-04-03), introduces the very same fat-node punctual Hilbert schemes, filtration methods and Poincaré-series formulas in several ranges of \((u,v)\). This is the qualifying recent source and supplies the geometric motivation; **its ordinary unrefined Euler or Poincaré data are not claimed here as new**. Huang, Jiang and Oblomkov, *Sheaves on nodal singularities I* (arXiv:2610.34676; first publicly posted 2026-10-26), provide an even stronger all-\((u,v)\) motivic Hilbert-zeta formula and an explicitly contact-length-refined series. That full prior formula **already covers the unrefined specialization \(z=1\)** of our answer. Their contact length is \(\dim R/(I+(x))\), however, not \(\dim I/\mathfrak m I\); their stated formulas do not directly supply the generator-number coefficient distribution, the sharp global generator ceiling, or the top-generator product series. Their stratifications might permit a further derivation, posing a priority risk for a differently expressed equivalent formula.

Hsiao and Szenes, *Refined Hilbert schemes, E-polynomials, and the number of generators of finite colength ideals in the plane* (arXiv:1806.03955), show why generator-number strata and elbows are a natural independent refinement, but work with ideals of the smooth **ambient plane**, not minimal generators in the quotient by the fat-node equation. The distinction accounts for the explicit one-generator corner correction. Oblomkov and Shende, *The Hilbert scheme of a plane curve singularity and the HOMFLY polynomial of its link* (arXiv:1003.1568), motivate the generator refinement in the reduced-curve setting; no HOMFLY equality is inferred here. Semantic mathematical-record searches for fat nodes, minimal generators, Young diagrams, equivalent Pochhammer products, and extremal strata did not retrieve an equivalent claim. Absence of a match is not proof of priority.

## Limitations

This is a **compactly supported Euler-characteristic** computation, not a motivic, Hodge, or cohomological refinement of generator-number strata. Although the strata are constructible and the Euler series has nonnegative coefficients, it does not establish cell decompositions for each such stratum. All scheme assertions are over \(\mathbb C\), and no claim is made for general planar singularities or full Hilbert schemes away from the singular point. Independent peer validation and exhaustive historical priority checking have not been performed. Most importantly, the all-\((u,v)\) **unrefined** motivic series is existing literature, so the contribution lies solely in the generator-number refinement, its exact closed form and the extremal-generator stratum.

## References

1. Yuze Luan, *Hilbert scheme of points on non-reduced nodal curves*, arXiv:2604.03111 (first posted 2026-04-03), https://arxiv.org/abs/2604.03111 .
2. Yifeng Huang, Ruofan Jiang, Alexei Oblomkov, *Sheaves on nodal singularities I*, arXiv:2610.34676 (first posted 2026-10-26), https://arxiv.org/abs/2610.34676 .
3. Yi-Ning Hsiao and Andras Szenes, *Refined Hilbert schemes, E-polynomials, and the number of generators of finite colength ideals in the plane*, arXiv:1806.03955, https://arxiv.org/abs/1806.03955 .
4. Alexei Oblomkov and Vivek Shende, *The Hilbert scheme of a plane curve singularity and the HOMFLY polynomial of its link*, arXiv:1003.1568, https://arxiv.org/abs/1003.1568 .
