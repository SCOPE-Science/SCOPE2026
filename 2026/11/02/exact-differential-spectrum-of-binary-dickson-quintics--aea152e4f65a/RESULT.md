# Exact differential spectrum of binary Dickson quintics

## Finding

Let \(m\ge2\) be an integer, \(q=2^m\), and \(a\in\mathbb F_q^\times\). Define
\[
f_a(x)=x^5+ax^3,\qquad C_a=\{(x,f_a(x)):x\in\mathbb F_q\}.
\]
For every \((s,v)\in\mathbb F_q^2\) define the **ordered** two-sum representation count
\[
R_a(s,v)=\#\{x\in\mathbb F_q:f_a(x)+f_a(x+s)=v\}.
\]
Equivalently, this is the standard difference-distribution table of \(f_a\) in characteristic two, including the zero-input-difference row. Set
\[
n_4=\frac q2-1-\mathbf1_{2\mid m},\qquad n_2=q-1-n_4.
\]
Exactly \(n_4\) nonzero values of \(s\) produce \(q/4\) output values with \(R_a(s,v)=4\), and exactly \(n_2\) nonzero values of \(s\) produce \(q/2\) output values with \(R_a(s,v)=2\). All other outputs in each such row have count zero. The sole nonzero representation count for \(s=0\) is \(R_a(0,0)=q\).

In particular, writing \(H_j=\#\{(s,v):R_a(s,v)=j\}\), the complete global spectrum is
\[
H_q=1,\quad H_4=\frac{qn_4}{4},\quad
H_2=\frac{qn_2}{2},\quad
H_0=q^2-1-H_4-H_2.
\]
At \(q=4\), the formula gives \(H_4=0\); there is no ambiguity between the zero first-coordinate row of count four and the four-preimage rows, which are absent. Every other multiplicity has count zero.

Therefore
\[
|C_a+C_a|=\begin{cases}
(3q^2-2q+8)/8,&m\text{ odd},\\
1+3q^2/8,&m\text{ even},
\end{cases}
\]
and the ordered additive energy is
\[
E(C_a)=\sum_{s,v}R_a(s,v)^2=
\begin{cases}4q^2-4q,&m\text{ odd},\\4q^2-6q,&m\text{ even}.
\end{cases}
\]
For nonzero directions the differential uniformity is two when \(m=2\), and four for all \(m\ge3\). All formulas are independent of the particular \(a\ne0\).

The first-kind Dickson quintic in characteristic two is
\[
D_5(x,a)=x^5+ax^3+a^2x.
\]
Adding the linear term maps each graph point \((x,f_a(x))\) to \((x,f_a(x)+a^2x)\), an invertible additive shear. Thus the same twofold-sum spectrum, energy, and differential uniformity hold for \(D_5\).

## Assumptions and scope

Only fields of characteristic two with \(m\ge2\) and nonzero coefficient \(a\) are covered. All pairs are ordered; neither collisions nor diagonal pairs are quotiented by symmetry. Absolute trace means \(\operatorname{Tr}=\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}\). The twofold sumset consists of all ordered graph-point sums. No assertion is made for prime-power rings of characteristic greater than two.

## Proof

**1. Normalize the derivative.** Fix \(s\in\mathbb F_q^\times\), write \(x=st\), and put \(c=a/s^2\). The characteristic-two binomial identities give the exact affine decomposition
\[
\begin{aligned}
f_a(st)+f_a(s(t+1))
 &=s^5\left[t^4+t+1+c(t^2+t+1)\right]\\
 &=s^5\left[1+c+L_c(t)\right],
\end{aligned}
\]
where the \(\mathbb F_2\)-linearized polynomial satisfies
\[
L_c(t)=t^4+ct^2+(1+c)t=t(t+1)(t^2+t+1+c).
\]
The map from \(t\) to the derivative output is therefore affine over \(\mathbb F_2\), with every nonempty fiber of cardinality \(K_c=|\ker L_c|\).

**2. Classify the kernel exactly.** Both zero and one lie in \(\ker L_c\). When \(c=1\), the quadratic factor is \(t^2+t\); its only roots are zero and one, so \(K_1=2\). When \(c\ne1\), this quadratic has two distinct roots outside \(\{0,1\}\) if and only if \(\operatorname{Tr}(1+c)=0\), by the Artin–Schreier trace criterion. In that case the kernel has exactly four points, since the factors have no repeated common roots; otherwise its kernel is exactly \(\{0,1\}\). Hence
\[
K_c=4\iff c\ne1\text{ and }\operatorname{Tr}(1+c)=0;
\qquad K_c=2\text{ otherwise}.
\]
The trace criterion follows directly from \(\operatorname{im}(t\mapsto t^2+t)=\ker\operatorname{Tr}\): the map has kernel \(\{0,1\}\), and all its images have trace zero, so both sets have \(q/2\) elements.

**3. Count directions and image sizes.** The map \(s\mapsto a/s^2\) is a bijection of \(\mathbb F_q^\times\); indeed squaring is an automorphism. Because \(\operatorname{Tr}(1)=m\bmod2\), precisely \(q/2\) elements of \(\mathbb F_q\) have \(\operatorname{Tr}(1+c)=0\). Among them discard \(c=1\) and, if \(m\) is even, \(c=0\), which is excluded by \(s\ne0\). This leaves
\[
n_4=q/2-1-\mathbf1_{2\mid m}
\]
directions with kernel four, and the remaining \(n_2=q-1-n_4\) directions have kernel two. An affine map on a set of size \(q\) with kernel of size \(K\) has exactly \(q/K\) distinct outputs, each of multiplicity \(K\). The nonzero rows of the representation table are therefore as claimed.

**4. The zero row and derived invariants.** If \(s=0\), each graph pair has \(y=x\), hence \(v=f_a(x)+f_a(x)=0\); therefore \(R_a(0,0)=q\) and \(R_a(0,v)=0\) for \(v\ne0\). Adding the nonzero-row histograms gives the four displayed values of \(H_j\). The number of occupied targets is \(1+H_2+H_4\), yielding the sumset formula. The energy, counting quadruples of graph points with equal sums, is
\[
E(C_a)=q^2+4H_2+16H_4
=q^2+2qn_2+4qn_4,
\]
which simplifies to the two parity formulas. When \(m=2\), \(n_4=0\); for every \(m\ge3\), \(n_4>0\). This proves the exact APN/four-uniform dichotomy.

**5. Coefficient and Dickson equivalence.** For each \(a\ne0\), its unique square root \(b\) satisfies \(a=b^2\). Then
\[
f_a(bx)=b^5(x^5+x^3),
\]
so invertible scalings on the source and output coordinates identify all coefficients. Finally \(D_5(x,a)=f_a(x)+a^2x\); its graph differs by the additive shear \((s,v)\mapsto(s,v+a^2s)\), which permutes targets, preserving every multiplicity. \(\square\)

## Verification

The accompanying independent standard-library program `verify_binary_sums.py` enumerates finite fields using binary polynomial arithmetic, forms every ordered pair of graph points, and computes complete multiplicity histograms without using the proof's trace criterion. It checks every coefficient for degrees \(2\le m\le6\) and selected coefficients for degrees seven and eight, comparing both the entire spectrum and exact energy. The verifier additionally checks the zero-coefficient Gold family only as a comparison; that family is not part of the claim. Run with `python verify_binary_sums.py` in the file's directory. All enumerated checks passed. These computations do not establish the general result; the proof covers all integer degrees \(m\ge2\).

## Relationship to prior work

The degree-five Dickson polynomial is classical, and Qin and Hong explicitly use it in a finite-field permutation construction (Example 2.2 in the original version and Example 2.1 in the revision; arXiv:1303.2229, originally submitted 2013-03-09). Wang and Yucas study general Dickson definitions and factorization/permutation behavior. These are polynomial identities and permutation results rather than the full difference-distribution spectrum across all binary extensions. Göloğlu's APN-trinomial study concerns other families and emphasizes trace decompositions, not this Dickson quintic's exact all-direction spectrum. Rønjom and Sandrib's Theorem 6 concerns Dickson polynomials over non-field Galois rings (ring exponent at least two), establishing a ring-level differential-uniformity result; that result is **not** a formula for the finite-field full DDT when the ring exponent is one. The apparently different uniformity scales must not be conflated. The Gold monomial \(x^5\) arises at \(a=0\), which is excluded and has a different spectrum. The general binary-graph Fourier and APN results in related literature do not by themselves evaluate these DDT multiplicities.

## Limitations

The result does not classify the full Walsh spectrum, arbitrary quintic deformations, general characteristic or higher prime-power Galois-ring derivatives. It does not resolve publication priority absolutely: specialized differential-cryptanalysis literature may contain a logically equivalent result under different terminology. Complete equivalence checks of every older source are not possible. No independent mathematical audit or external certification has been performed.

## References

1. X. Qin and S. Hong, *Constructing permutation polynomials over finite fields*, arXiv:1303.2229v1, submitted 9 March 2013; full text available at https://arxiv.org/html/1303.2229v2. Relevant material: Example 2.2 (v1) / Example 2.1 (v2) and polynomial construction.
2. Q. Wang and J. L. Yucas, *Dickson polynomials over finite fields*, *Finite Fields and Their Applications* 18 (2012), 814–831, https://doi.org/10.1016/j.ffa.2012.02.001; author-hosted full text: https://people.math.carleton.ca/~wang/papers/genDickson.pdf.
3. F. Göloğlu, *APN trinomials and hexanomials*, arXiv:1411.2981, 2014, https://arxiv.org/abs/1411.2981.
4. S. Rønjom and A. Sandrib, *On the differential uniformity of polynomials over Galois rings*, *Cryptography and Communications* 18 (2026), 2057–2077, https://doi.org/10.1007/s12095-026-00895-x, especially §4.2 and Theorem 6 (different ring-level problem).
