# Sharp dual-symmetric-power character moments and the rank-three mixing transition

## Finding

Let \(N\ge3\), \(p\ge1\), \(G=SU(N)\) with normalized Haar probability measure, and let \(\chi_p\) be the character of the irreducible representation \(\operatorname{Sym}^p(\mathbb C^N)\). The characters \(1,\chi_p,\overline{\chi_p}\) are orthonormal. Define the sharp fourth-moment amplification
\[
K_{N,p}=\max_{|a|^2+|b|^2+|c|^2=1}\int_G|a\chi_p+b\overline{\chi_p}+c|^4\,dg.
\]
The exact constants and all equality cases are as follows.

**Ranks at least five.** For every \(N\ge5\),
\[
K_{N,p}=\frac{3(p+1)}2.
\]
Every normalized maximizing triple is \((a,b,c)=(\zeta/\sqrt2,\zeta\eta/\sqrt2,0)\), where \(|\zeta|=|\eta|=1\).

**Rank four.** For \(N=4\),
\[
K_{4,p}=\frac{3p+4}2.
\]
Every normalized maximizing triple is \((a,b,c)=(\zeta/\sqrt2,\pm\zeta/\sqrt2,0)\), with \(|\zeta|=1\).

**Rank three.** Write \(\delta_p=1\) if \(3\mid p\), otherwise \(\delta_p=0\), and set \(C_p=3(p+1)/2+5\delta_p/2\). The cubic
\[
4r^3+3\sqrt2\,r^2+(3p+5\delta_p-3)r-\sqrt2=0
\]
has a unique positive root \(r_p\), and
\[
K_{3,p}=\frac{C_p+2\sqrt2\,r_p+6r_p^2+r_p^4}{(1+r_p^2)^2}>C_p.
\]
Let \(\omega=e^{2\pi i/3}\). Every normalized maximizing triple has the form
\[
(a,b,c)=\frac{\zeta}{\sqrt{1+r_p^2}}
\left(\frac{\omega^j}{\sqrt2},\frac{\omega^{-j}}{\sqrt2},r_p\right),\qquad |\zeta|=1,
\]
where \(j=0,1,2\) if \(3\nmid p\), and only \(j=0\) if \(3\mid p\). In particular the trivial character occurs with a strictly nonzero coefficient exactly at rank three. As \(p\to\infty\),
\[
r_p=\frac{\sqrt2}{3p}+O(p^{-2}),\qquad
K_{3,p}-C_p=\frac{2}{3p}+O(p^{-2}).
\]
The parity-like arithmetic condition \(3\mid p\) changes the number of projective maximizing phase classes from three to one, but does not remove trivial-character mixing.

## Assumptions and scope

All groups are the compact special unitary groups, not the full unitary groups; integration is normalized to probability mass one. All coefficients are arbitrary complex numbers. The symmetric power has the highest weight \((p,0,\ldots,0)\) in Dynkin coordinates. No restriction on \(p\) except \(p\ge1\) is imposed. Equality classification is for nonzero triples under the displayed unit-energy normalization; unnormalized equality triples are their arbitrary nonzero complex scalar multiples. No claims are made for higher moments, additional character frequencies, or different groups.

## Proof

**1. Multiplicity-free tensor products and collisions.** Write \(X=\chi_p\) and \(Y=\overline{\chi_p}\). By the Pieri rule and the standard symmetric-tensor harmonic decomposition, the irreducible constituents, each of multiplicity one, of \(X^2\), \(Y^2\), and \(XY\), respectively, have the following Dynkin labels for \(0\le j\le p\):
\[
A_j=(2p-2j,j,0,\ldots,0),\quad
B_j=(0,\ldots,0,j,2p-2j),\quad
T_j=(j,0,\ldots,0,j).
\]
The written coordinate strings have length \(N-1\); in rank three \(A_j=(2p-2j,j)\), \(B_j=(j,2p-2j)\), and \(T_j=(j,j)\); in rank four \(T_j=(j,0,j)\). Each list has \(p+1\) distinct entries, and \(T_0\) is the trivial representation. For \(N\ge5\), these lists are pairwise disjoint; none contains \(X\) or \(Y\). For \(N=4\), the only collision across the lists is \(A_p=B_p=(0,p,0)\). For \(N=3\), \(B_p=X\), \(A_p=Y\), and the three lists intersect pairwise exactly in the one common constituent \((2p/3,2p/3)\) when \(3\mid p\); otherwise their intersections are empty. These assertions follow by comparing the nonzero Dynkin coordinates, including the end coordinates when the rank is small.

**2. The exact fourth-moment identity.** Let \(A=|a|^2\), \(B=|b|^2\), and \(D=|c|^2\). The square of the central function \(f=aX+bY+c\) is
\[
f^2=a^2X^2+b^2Y^2+2abXY+2acX+2bcY+c^2.
\]
Use irreducible-character orthogonality in the previous decomposition. For \(N\ge5\) it gives
\[
I_{N,p}(a,b,c)=(p+1)(A^2+B^2+4AB)+D^2+4D(A+B)+4\operatorname{Re}(c^2\overline{ab}).\tag{1}
\]
For \(N=4\) add to (1) the term \(2\operatorname{Re}(a^2\overline{b}^{\,2})\). For \(N=3\) add
\[
4\operatorname{Re}(a^2\overline{bc})+4\operatorname{Re}(b^2\overline{ac})
+\delta_p\bigl(|a+b|^4-(A^2+B^2+4AB)\bigr).\tag{2}
\]
For the last term note that at the common constituent the coefficient of \(f^2\) is \((a+b)^2\): the \(X^2,Y^2,2XY\) contributions coincide. The other cross terms in (2) come from the constituent \(Y\) in \(X^2\) and \(X\) in \(Y^2\). Thus (1)–(2) hold for all phases, including zero coefficients.

**3. Rank at least four.** For fixed magnitudes, all real parts are bounded by their products. At \(N\ge5\) this bound is attained whenever \(c^2\overline{ab}\) is nonnegative real. Write \(R=A+B\), \(D=1-R\), and note \(AB\le R^2/4\). Equation (1) becomes bounded by
\[
I_{N,p}\le 1+4R+\left(\frac{3p}{2}-\frac72\right)R^2,
\qquad 0\le R\le1.\tag{3}
\]
The right side is strictly increasing on \([0,1]\): its derivative is \(4+(3p-7)R\), whose minimum is at least zero and in the only borderline case \(p=1,R=1\) equals zero, while the function is still strictly increasing. In fact the endpoint derivative is \(3p-3\ge0\). Hence \(R=1\), \(A=B=1/2\), \(D=0\), yielding \(K_{N,p}=3(p+1)/2\). When \(D=0\) the phase is arbitrary. For \(N=4\), the added real term is at most \(2AB\), so similarly
\[
I_{4,p}\le1+4R+\left(\frac{3p}{2}-3\right)R^2.
\]
This is strictly increasing (derivative \(4+(3p-6)R\ge1\) for \(p\ge1\)); equality requires \(A=B=1/2,D=0\) and \(a^2\overline b^{\,2}\ge0\) real, equivalent to \(a/b=\pm1\).

**4. Rank three and its cubic.** All phase terms in (1)–(2) are simultaneously maximized by choosing \(a,b,c\ge0\) real: this includes the \(\delta_p\) term by the triangle inequality \(|a+b|\le|a|+|b|\). Let \(x=|a|\), \(y=|b|\), \(z=|c|\), \(R=x^2+y^2\), \(v=xy\), and \(x^2+y^2+z^2=1\). After substitution the upper-bound expression is
\[
(p+1)(R^2+2v^2)+z^4+4z^2R+4z^2v+4zvR
+\delta_p(2v^2+4Rv).
\]
It is strictly increasing in \(v\in[0,R/2]\) whenever \(R>0\) and \(z>0\); at \(z=0\) it is also strictly increasing for \(v>0\), and globally its maximum at any fixed \(R\) is attained at \(v=R/2\). Thus all global optimizers have \(x=y\). Put \(x=y=(2(1+r^2))^{-1/2}\), \(z=r(1+r^2)^{-1/2}\) for \(r\ge0\). The resulting objective is
\[
F_p(r)=\frac{C_p+2\sqrt2\,r+6r^2+r^4}{(1+r^2)^2}.
\]
Its derivative satisfies the exact factorization
\[
F_p'(r)=-\frac{2}{(1+r^2)^3}\left[4r^3+3\sqrt2\,r^2+(3p+5\delta_p-3)r-\sqrt2\right].
\]
For \(p\ge1\), the bracket is strictly increasing on \((0,\infty)\), starts negative, and tends to infinity. Consequently its single positive zero \(r_p\) is the unique global maximum, with \(r_p>0\) and \(F_p(r_p)>F_p(0)=C_p\). It also exceeds the \(z=1\) endpoint (whose fourth moment is one). The small-root expansion directly gives \(r_p=\sqrt2/(3p)+O(p^{-2})\), and substitution yields the stated strict-gain expansion.

**5. Equality phases.** Since the optimum has \(x,y,z>0\), each triangle inequality used in (1)–(2) must be sharp. If \(a=x e^{i\alpha}\), \(b=x e^{i\beta}\), \(c=z e^{i\gamma}\), this gives the three congruences
\[
2\gamma\equiv\alpha+\beta,\quad
2\alpha\equiv\beta+\gamma,\quad
2\beta\equiv\alpha+\gamma\pmod{2\pi}.
\]
After removal of the common phase they have exactly the three solutions \((\alpha,\beta,\gamma)\equiv(2\pi j/3,-2\pi j/3,0)\), \(j=0,1,2\). If \(3\mid p\), equality in \(|a+b|\le|a|+|b|\) further forces \(\alpha\equiv\beta\), and only \(j=0\) remains. Conversely every listed triple saturates every inequality. This proves the exact sharp constants and exhaustive equality classifications.

## Verification

The standalone Python program `checker.py` checks the Dynkin-label decompositions and all collisions over ranks three through eight and weights one through twelve, verifies the character-orthogonality moment identity against independently assembled representation-ring coefficients for five coefficient choices at each test, symbolically differentiates the cubic objective, checks twenty positive-root instances, and compares the formula with six independent, nonaliasing discrete Weyl torus quadratures. Run with `python checker.py`; the verified reference output is contained in `verification-output.txt`. These finite computational checks are corroboration, not the proof of the all-rank assertions; the proof is the preceding symbolic representation-theoretic argument.

## Relationship to prior work

Pieri decomposition and orthogonality are standard representation-theoretic tools. Zhang's compact-group Fourier-restriction results provide growth bounds for character norms but do not supply this exact sharp three-character optimization or its rank-three phase classification. Jonnadula–Keating–Mezzadri and Bailey–Keating use Schur functions and compact-unitary integrations to study characteristic-polynomial moments; their questions and conclusions differ from the sharp small-central-spectral-packet inequality above. The classical rank-two analogue is not equivalent: in \(SU(2)\) the fundamental symmetric powers are self-dual and the three displayed frequencies need not be distinct. Relevant published harmonic-analysis findings concerning rank-two character packets and abelian pair-product collisions have different irreducible-character multiplication laws; none of those inspected statements implies the rank-three mixing transition. No assertion of independently established historical priority is made.

## Limitations

The result is confined to \(SU(N)\), the dual pair of a single symmetric-power irreducible and the trivial character, and fourth moments. It does not identify sharp constants for arbitrary central packets or higher moments. Computational tests cover finite dimensions and weights only. The absence of an equivalent earlier formulation in material not inspected cannot be guaranteed, and no independent mathematical audit has been performed.

## References

1. Yunfeng Zhang, *On Fourier restriction type problems on compact Lie groups*, arXiv:2005.11451 (first posted 2020-05-23), Sections 1–2. https://arxiv.org/abs/2005.11451
2. C. H. Jonnadula, J. P. Keating, F. Mezzadri, *Symmetric Function Theory and Unitary Invariant Ensembles*, arXiv:2003.02620 (first posted 2020-03-05). https://arxiv.org/abs/2003.02620
3. E. C. Bailey and J. P. Keating, *On the moments of the moments of characteristic polynomials of random unitary matrices*, arXiv:1807.06605 (first posted 2018-07-17). https://arxiv.org/abs/1807.06605
4. The classical Pieri/Littlewood–Richardson rule and Weyl character orthogonality, used as established background identities.
