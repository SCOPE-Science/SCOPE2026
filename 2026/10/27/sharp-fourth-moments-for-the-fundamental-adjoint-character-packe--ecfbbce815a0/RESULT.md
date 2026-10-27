# Sharp fourth moments for the fundamental–adjoint character packet on \(SU(3)\)

## Finding

Let \(G=SU(3)\), equipped with Haar probability measure \(dg\). For Dynkin labels \((p,q)\), let \(\chi_{(p,q)}\) be the ordinary trace character of the irreducible representation of highest weight \((p,q)\). In particular the characters for \((1,0)\), \((0,1)\) and \((1,1)\) have dimensions \(3,3,8\) and are orthonormal in \(L^2(G)\).

For \(F=a\chi_{(1,0)}+b\chi_{(0,1)}+c\chi_{(1,1)}\), with arbitrary complex coefficients not all zero, the exact sharp quotient is

\[
\frac{\int_G |F|^4\,dg}{(\int_G |F|^2\,dg)^2}
\le K_*:=\frac{8r_*^4+36r_*^2+16r_*+12}{(r_*^2+2)^2}=8.792646640053\ldots,
\]

where \(r_*\) is the unique positive solution of

\[r_*^3+6r_*^2-12r_*-4=0,\qquad r_*=1.816810237633\ldots.\]

All nonzero equality triples, and no others, are

\[
(a,b,c)=\lambda(\omega^k,\omega^{-k},r_*),\quad
\lambda\in\mathbb C\setminus\{0\},\quad k\in\{0,1,2\},\quad
\omega=e^{2\pi i/3}.
\]

Under the normalization \(|a|^2+|b|^2+|c|^2=1\), the coefficient vector is \(e^{i\theta}(\omega^k,\omega^{-k},r_*)/\sqrt{2+r_*^2}\). Thus all three isotypic contributions are necessary, and there are exactly three projective phase classes related by the center of \(SU(3)\).

## Assumptions and scope

Ordinary, dimension-*unnormalized* characters and Haar probability are used. Characters are complex-valued central functions. The statement concerns the exact three-dimensional subspace spanned by the two dual fundamental characters and the adjoint character; it is not an optimization over arbitrary matrix coefficients or over all irreducible representations. The adjoint character satisfies \(\chi_{(1,1)}(g)=|\operatorname{tr}(g)|^2-1\), while the two fundamental characters are \(\operatorname{tr}(g)\) and its conjugate.

## Proof

**1. Tensor products.** Write \(A=\chi_{(1,0)}\), \(B=\chi_{(0,1)}\), and \(C=\chi_{(1,1)}\). Standard \(SU(3)\) tensor products, whose multiplicities can also be computed by semistandard Schur tableaux, are

\[
\begin{aligned}
A^2&=\chi_{(2,0)}+B, & B^2&=\chi_{(0,2)}+A,\\
AB&=1+C, & AC&=A+\chi_{(0,2)}+\chi_{(2,1)},\\
BC&=B+\chi_{(2,0)}+\chi_{(1,2)},
& C^2&=1+2C+\chi_{(3,0)}+\chi_{(0,3)}+\chi_{(2,2)}.
\end{aligned}
\]

The dimensions on the right agree with the product dimensions in each row; the exact identities are independently checked by tableau enumeration in `check.py`. Expanding \(F^2\) gives the following irreducible-character coefficients: \(c^2+2ab\) at \((0,0)\); \(2c^2+2ab\) at \((1,1)\); \(a^2+2bc\) at each of \((2,0)\) and \((0,1)\); \(b^2+2ac\) at each of \((0,2)\) and \((1,0)\); \(c^2\) at each of \((3,0)\), \((0,3)\), \((2,2)\); \(2ac\) at \((2,1)\); and \(2bc\) at \((1,2)\).

**2. Exact fourth moment.** Irreducible-character orthonormality and \(|F|^4=|F^2|^2\) yield, with no sign or reality restrictions,

\[
\begin{aligned}
\int_G|F|^4\,dg={}&|c^2+2ab|^2+|2c^2+2ab|^2\\
&+2|a^2+2bc|^2+2|b^2+2ac|^2\\
&+3|c|^4+4|ac|^2+4|bc|^2.
\end{aligned}
\]

Also \(\int_G|F|^2\,dg=|a|^2+|b|^2+|c|^2\). The identity above is independently established by an exact Laurent-polynomial Weyl-integration constant-term calculation in `check.py` (all six coefficient variables, not sample-only testing).

**3. Phases.** Every summand has nonnegative tensor multiplicities, so the triangle inequality bounds the preceding expression by its value at \((|a|,|b|,|c|)\). Put \(x=|a|\), \(y=|b|\), \(z=|c|\), and \(s=x^2+y^2\), \(q=xy\). The phase-aligned fourth moment is exactly

\[
2s^2+4q^2+8zq\sqrt{s+2q}+12z^2q+12z^2s+8z^4.
\]

For fixed \(s,z\) with \(s>0\), the expression is strictly increasing as \(q\) increases from \(0\) to \(s/2\): the \(4q^2\) term is strictly increasing and every other \(q\)-dependent term is nondecreasing. Hence every nontrivial maximizer with \(s>0\) has \(x=y>0\). The case \(s=0\) has quotient \(8\), whereas the choice \(x=y=1,z=2\) has quotient \(316/36>8\), so no maximizer has \(s=0\).

**4. One-variable sharp optimization.** Set \(x=y=t>0\) and \(z=rt\) with \(r\ge0\). The sharp ratio at these magnitudes is

\[
R(r)=\frac{8r^4+36r^2+16r+12}{(r^2+2)^2},\qquad
R'(r)=-\frac{8(r^3+6r^2-12r-4)}{(r^2+2)^3}.
\]

The cubic in the numerator of \(-R'(r)\) has exactly one positive zero by Descartes' rule (its coefficient signs are \(+,+,-,-\)); it is negative at zero and positive for sufficiently large \(r\). Thus \(R\) is strictly increasing up to \(r_*\) and strictly decreasing afterward. At \(r=0\) the quotient is \(3\), while \(R(r)\to8\) at infinity, and \(R(2)=316/36>8\). Therefore the unique interior maximum is global and equals \(K_*\), proving the sharp bound and uniqueness of the magnitude profile.

**5. All complex equality cases.** The maximizer has \(abc\ne0\). Equality in each of the three nontrivial triangle inequalities in step 3 requires

\[
2\arg c\equiv\arg a+\arg b,\quad
2\arg a\equiv\arg b+\arg c,\quad
2\arg b\equiv\arg a+\arg c\pmod{2\pi}.
\]

Solving these simultaneous congruences gives exactly \(\arg a=\theta+2\pi k/3\), \(\arg b=\theta-2\pi k/3\), and \(\arg c=\theta\), with \(k\in\{0,1,2\}\). Conversely these phases align every collision term above, so all listed triples are genuine extremizers. They are distinct modulo multiplication of \((a,b,c)\) by a common nonzero complex scalar.

## Verification

`check.py` uses only the Python standard library. It constructs the eleven low \(SU(3)\) characters required in the proof by semistandard-tableau enumeration, verifies all six displayed tensor decompositions as Laurent identities, implements Weyl's normalized constant-term integration formula, and compares all coefficients of the entire six-formal-variable fourth-moment polynomial with the tensor-product formula. It also checks the exact derivative identity and provides auxiliary bisection for the unique positive cubic root. Run `python3 check.py`; `check_output.txt` contains the corresponding output. The analytic phase/magnitude arguments above establish the global theorem; neither finite numerical sampling nor bisection is used as an infinite proof.

## Relationship to prior work

Clebsch–Gordan decomposition for \(SU(3)\) is classical; Martins–Suffak–de Guise describe symbolic tensor-coupling methods and multiplicity-free products. Jonnadula–Keating–Mezzadri study symmetric functions and moments of unitary ensembles, including the general character-moment background. Zhang proves sharp *asymptotic exponent* bounds for individual compact-Lie-group characters and related spectral functions. These works motivate the class-function Fourier setting and supply the standard methods, but the inspected results do not state the exact sharp coefficient-optimized fourth moment for this specified fundamental/antifundamental/adjoint packet or classify its three projective maximizing phases. This is a best-knowledge comparison, not an assertion that every possible earlier or unindexed formulation has been exhaustively ruled out.

## Limitations

The classification is for this three-character subspace of \(SU(3)\), not all low-degree characters or arbitrary \(SU(N)\). There is no asserted independent audit or definitive bibliographic priority adjudication. The numerical digits are approximations to the displayed algebraic definitions; the proof is exact. Stronger norms and other exponents are not addressed.

## References

1. A. C. N. Martins, M. W. Suffak, and H. de Guise, “SU(3) Clebsch-Gordan coefficients and some of their symmetries,” arXiv:1909.09055, first public 2019-09-19. https://arxiv.org/abs/1909.09055
2. B. Jonnadula, J. P. Keating, and F. Mezzadri, “Symmetric Function Theory and Unitary Invariant Ensembles,” arXiv:2003.02620, first public 2020-03-05. https://arxiv.org/abs/2003.02620
3. Y. Zhang, “On Fourier restriction type problems on compact Lie groups,” arXiv:2005.11451, first public 2020-05-23. https://arxiv.org/abs/2005.11451
