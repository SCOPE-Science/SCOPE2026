# Characteristic-five ordinarity and superspecial degeneration of the symmetric plane sextic

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\). For every \(t\in k\), define the projective plane sextic
\[
 C_t:\quad F_t(X,Y,Z)=X^6+Y^6+Z^6+tX^2Y^2Z^2=0.
\]
The curve is geometrically smooth if and only if \(t^3\ne3\). Every smooth member is geometrically integral of genus \(10\). Its Jacobian has the following complete \(5\)-rank and \(a\)-number classification:
\[
 (f_5(J(C_t)),a(J(C_t)))=
 \begin{cases}
 (0,10),&t=0,\\
 (9,1),&t^3=1,\\
 (10,0),&t\ne0\text{ and }t^3\notin\{1,3\}.
 \end{cases}
\]
In particular, the Fermat member is superspecial, the three parameters with \(t^3=1\) give exactly the nonordinary, non-superspecial smooth curves, and every other smooth member is ordinary. Over the algebraic closure there are exactly four nonordinary smooth parameters in this marked family.

There is a geometric explanation for the middle rank: the coordinate-square morphism
\[
 \pi_t:C_t\longrightarrow E_t,\qquad[X:Y:Z]\longmapsto[X^2:Y^2:Z^2]
\]
is a connected degree-four tame Galois cover of the Hesse cubic
\[
 E_t:\quad U^3+V^3+W^3+tUVW=0,
\]
whose group is \((\mathbb Z/2\mathbb Z)^2\). The elliptic quotient is supersingular exactly for \(t(t^3-1)=0\). On every smooth member with \(t\ne0\), the complementary nine-dimensional isogeny factor of \(J(C_t)\) is ordinary. Thus, for those nonzero parameters, the only possible loss of ordinarity comes from the elliptic quotient.

## Assumptions and scope

The ground field is algebraically closed of characteristic exactly \(5\), and all parameter statements quantify over every \(t\in k\). Jacobian \(5\)-rank denotes the dimension of its maximal étale \(5\)-torsion subgroup; its \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J[5])\). These are geometric invariants of the smooth curve. The parameter equation \(t^3=3\) describes the excluded singular members, not an additional Jacobian stratum. The numerical distinction between one-step Hasse–Witt rank and stable Frobenius rank is essential.

## Proof

**1. Smoothness and geometric genus.** Since \(6\equiv1\pmod5\), differentiation gives
\[
 F_X=X^5+2tXY^2Z^2,\quad F_Y=Y^5+2tYX^2Z^2,\quad F_Z=Z^5+2tZX^2Y^2.
\]
A common zero of the derivatives cannot have a zero coordinate. Indeed, setting one coordinate to zero forces the other two to vanish. For nonzero coordinates put \(A=X^2\), \(B=Y^2\), \(C=Z^2\), and \(r=-2t\). The three derivative equations become
\[
 A^2=rBC,\quad B^2=rAC,\quad C^2=rAB.
\]
Multiplication gives \(r^3=1\), equivalent in characteristic \(5\) to \(t^3=3\). Conversely, if \(r^3=1\), choose \((A,B,C)=(1,r^{-1},1)\); all three equalities hold, and square roots exist in \(k\). By Euler's homogeneous identity \(X F_X+YF_Y+Z F_Z=6F=F\), this point lies on the curve. Hence the stated smoothness condition is both necessary and sufficient. A smooth plane curve is geometrically integral, and the plane genus formula gives \(g=(6-1)(6-2)/2=10\).

**2. Exact Frobenius matrix.** The hypersurface sequence induces the canonical identification
\[
 H^1(C_t,\mathcal O_{C_t})\cong H^2(\mathbb P^2_k,\mathcal O_{\mathbb P^2}(-6)).
\]
An ordered basis is \(e_{a,b,c}=[X^{-a-1}Y^{-b-1}Z^{-c-1}]\), for the ten triples \(a,b,c\ge0\) with \(a+b+c=3\), in the order
\[
 \begin{array}{lllll}
 v_0=(0,0,3),&v_1=(0,1,2),&v_2=(0,2,1),&v_3=(0,3,0),&v_4=(1,0,2),\\
 v_5=(1,1,1),&v_6=(1,2,0),&v_7=(2,0,1),&v_8=(2,1,0),&v_9=(3,0,0).
 \end{array}
\]
Frobenius on local Čech fractions raises the denominator to the fifth power and multiplies by \(F_t^4\). Consequently the entry in row \((a,b,c)\) and column \((d,e,f)\) is the coefficient of
\[
 X^{5(a+1)-(d+1)}Y^{5(b+1)-(e+1)}Z^{5(c+1)-(f+1)}
\]
in \(F_t^4\). Multinomial expansion modulo \(5\) shows that the entire ten-by-ten matrix \(H_t\) has precisely the following potentially nonzero entries:
\[
 \begin{aligned}
&H_{0,0}=H_{3,3}=H_{9,9}=t^2,\\
&H_{1,8}=H_{8,1}=H_{2,7}=H_{7,2}=H_{4,6}=H_{6,4}=2t,\\
&H_{5,5}=t^4-t=t(t^3-1).
\end{aligned}
\]
All other entries vanish identically. The basis therefore splits the semilinear Frobenius into three one-dimensional pieces, three two-dimensional swap pieces, and a single central one-dimensional piece. In particular,
\[
 \det(H_t)=t^{13}(t^3-1)\quad\text{in }k.
\]

**3. Stable \(5\)-rank and \(a\)-number.** At \(t=0\), the whole matrix is zero, so both its rank and its stable Frobenius rank are zero, and the \(a\)-number is \(10\). When \(t\ne0\), the nine-dimensional direct sum comprising the three \(t^2\)-lines and the three \(2t\)-swap blocks is invertible. Its Frobenius-semilinear iterations remain invertible because every coefficient and every Frobenius twist is nonzero. On the complementary line, Frobenius is multiplication by \(t(t^3-1)\) followed by fifth powering. Thus for \(t^3=1\) this line vanishes permanently and the stable rank is \(9\), whereas for \(t^3\ne1\) all ten dimensions survive. For a smooth curve, the Jacobian \(5\)-rank is the stable Frobenius rank on \(H^1(\mathcal O)\), and its \(a\)-number is the genus minus the one-step Hasse–Witt rank. The stated classification follows. The zero matrix at the Fermat member also gives its superspeciality, by the standard equivalence for abelian varieties of \(a\)-number equal to their dimension.

**4. The elliptic quotient and ordinary complement.** The coordinate-square map has degree four with group \((\mathbb Z/2\mathbb Z)^2\), and its image is the stated cubic. Under the smoothness condition this cubic is nonsingular: its three derivatives force \(t^3=3\) if they have a common projective zero. The cover is connected because its source is smooth and irreducible. Each coordinate line meets the cubic transversely in three geometric points and is the branch locus of one involution; this is a tame degree-four cover in characteristic \(5\). The invariant summand of \(H^1(\mathcal O_{C_t})\) is the central basis line \(v_5=(1,1,1)\): the projective coordinate-sign involutions act with invariant character only on that basis vector. Frobenius on that line is \(t^4-t\), which also equals the Hasse invariant of \(E_t\), calculated as the coefficient of \((UVW)^4\) in \((U^3+V^3+W^3+tUVW)^4\). Its zeros are \(t=0\) and \(t^3=1\), proving the elliptic supersingularity criterion. Since the covering group has order four prime to the characteristic, its invariant and complementary cohomology summands correspond, up to isogeny, to the elliptic quotient and a nine-dimensional abelian factor. For nonzero smooth \(t\), the complementary Frobenius matrix is invertible, proving that factor ordinary.

## Verification

The standalone standard-library script `verify_hesse_sextic.py` computes \(F_t^4\) by two independent polynomial-expansion algorithms, reconstructs every one of the one hundred Hasse–Witt entries, and verifies the ten displayed nonzero entries with their exact coefficient polynomials over \(\mathbb F_5[t]\). Over \(\mathbb F_{25}\), it exhausts all \(25\) parameters, checks singular points of every marked projective curve, and verifies Frobenius ranks and iterated semilinear ranks at all \(22\) smooth parameters. It reports the marker `CHAR5_HESSE_SEXTIC_FULL_HASSE_10X10_F25_SMOOTHNESS_AND_STABLE_RANK_PASS`. These finite-field examples are corroboration; the calculations in the proof establish the classification for all parameters in any algebraically closed characteristic-five field.

## Relationship to prior work

Badr and Bars introduce the exact one-parameter symmetric plane sextic among their automorphism-theoretic families (preprint first public August 26, 2022; final open-access article, Proposition 10.4). Their analysis is for characteristic zero or characteristic greater than \(21\) and does not determine the characteristic-five Jacobian invariants. The characteristic-five base change and its complete smooth/ordinary/nonordinary strata are the new assertions here. Borges and Gonçalves develop substantial \(p\)-rank formulas for Fermat-type curves \(y^m=x^n+1\) and selected other families; the Fermat point \(t=0\) is known in this context. Their results do not directly provide the variable mixed-monomial sextic's nine-dimensional ordinary complement or the three intermediate nonordinary smooth parameters. The Hesse cubic supersingularity condition is classical; the contribution is its precise interaction with the full genus-ten covering family.

## Limitations

No assertion is made for characteristics other than \(5\), for singular fibers \(t^3=3\), for a complete Newton polygon or Ekedahl–Oort stratification beyond the stated \(5\)-ranks and \(a\)-numbers, or for full automorphism groups in characteristic \(5\). The explicit matrix is on coherent cohomology; it does not by itself determine the whole \(p\)-divisible group. Mathematical priority remains subject to unindexed equivalent calculations. No independent external audit has been performed.

## References

- E. Badr and F. Bars, *The stratification by automorphism groups of smooth plane sextic curves*, arXiv:2208.12749, first public 2022-08-26; Annali di Matematica Pura ed Applicata (2025), DOI:10.1007/s10231-025-01558-z, §10.1 and Proposition 10.4. https://arxiv.org/abs/2208.12749 ; https://link.springer.com/article/10.1007/s10231-025-01558-z
- H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first public 2022-12-07, §§3–6. https://arxiv.org/html/2212.03987v3
- N. Yui, *On the Jacobian variety of the Fermat curve*, Journal of Algebra **65** (1980), 1–35 (classical Fermat-case background; cited in Borges–Gonçalves).
