# Characteristic-five zero-rank strata and Cartier strings in a cyclic septic four-point family

## Finding
For every \(\lambda\in k\setminus\{0,1\}\), with \(k=\overline{\mathbb F}_5\), let \(C_\lambda\) be the smooth projective normalization of
\[
y^7=x(x-1)(x-\lambda)^6.
\]
Write \(q=\lambda^2-\lambda+1\). Then
\[
f_5(C_\lambda)=\begin{cases}6,&(\lambda+2)q\ne0,\\0,&(\lambda+2)q=0,\end{cases}\qquad
a(C_\lambda)=\begin{cases}0,&(\lambda+2)q\ne0,\\2,&(\lambda+2)q=0.\end{cases}
\]
At each of the three exceptional geometric parameters, the ranks of the first four Cartier iterates are \((6,4,2,0)\); the two nilpotent Cartier strings each have length three. The exceptional parameters are \(\lambda=3\in\mathbb F_5\) and the two roots of \(q\) in \(\mathbb F_{25}\setminus\mathbb F_5\). No smooth member has an intermediate \(5\)-rank.

The Hasse–Witt determinant is, up to a nonzero constant and the chosen trivialization,
\[
(\lambda+2)^2(\lambda^2-\lambda+1)^2.
\]
For unordered branch points respecting the two ramification labels, \(t=\lambda(1-\lambda)\) identifies the three exceptional ordered points into the two types \(t=4\) and \(t=1\). In this coordinate the displayed determinant polynomial becomes \((4-t)(1-t)^2\), up to a unit. This is a statement about this explicit determinant expression, not an assertion about a coarse-moduli Cartier divisor without choosing a trivialization.

## Assumptions and scope
Work over an algebraically closed field of characteristic \(5\). The cover has exponent pattern \((1,1,6,6)\) at \((0,1,\lambda,\infty)\) modulo \(7\), so all four points are fully tamely ramified. Riemann–Hurwitz gives \(2g-2=7(-2)+4(7-1)=10\), hence \(g=6\). All results concern the family \(\lambda\ne0,1\), and the geometric normalization is smooth. The three exceptional parameters are distinct and avoid the removed boundary: \(q(0)=q(1)=1\), \(q(3)=2\), and \(q\) has discriminant \(2\), not a square in \(\mathbb F_5\).

## Proof
For \(1\le j\le6\), set
\[
\omega_j=\frac{(x-\lambda)^{j-1}\,dx}{y^j}.
\]
At the branch points \(0,1\), the order of \(\omega_j\) is \(6-j\), and at \(\lambda,\infty\) it is \(j-1\). These valuations follow from ramification index seven, the orders \(1,1,6,-8\) of the radicand (the latter congruent to \(6\) modulo seven), and the corresponding order of \(dx\). Hence all six differentials are holomorphic. They have six different deck characters and, since the genus is six, form a basis.

Put \(f=x(x-1)(x-\lambda)^6\), \(s(j)=3j\bmod7\) with representative in \(\{1,\ldots,6\}\), and \(k(j)=(5s(j)-j)/7\), a nonnegative integer. Then \(5s(j)=j+7k(j)\), and
\[
\omega_j=\frac{(x-\lambda)^{j-1}f(x)^{k(j)}\,dx}{(y^{s(j)})^5}.
\]
For the polynomial
\[
G_j=x^{k(j)}(x-1)^{k(j)}(x-\lambda)^{6k(j)+j-1},
\]
coefficient extraction modulo five gives the exact identity
\[
[x^{5t+4}]G_j={s(j)-1\choose t}(-\lambda^5)^{s(j)-1-t}H_j(\lambda),\quad 0\le t<s(j),
\]
with no additional powers of the form \(5t+4\), and
\[
(H_1,H_2,H_3,H_4,H_5,H_6)
=(q,1,2(\lambda+2),2(\lambda+2),1,q).
\]
The ordinary Cartier coefficient-selection rule therefore gives \(\mathcal C(\omega_j)=H_j(\lambda)^{1/5}\omega_{s(j)}\). The permutation is the single cycle \(1\to3\to2\to6\to4\to5\to1\).

If the product of the six scalars is nonzero, Cartier is bijective, and its stable rank equals six. If \(q=0\), only arrows originating at indices \(1,6\) vanish; if \(\lambda+2=0\), only arrows from \(3,4\) vanish. In the six-cycle each pair of zero arrows is separated by three steps. Directly following the strings proves the iterate ranks \(6,4,2,0\) in either case. Thus the stable Cartier rank is zero, and the kernel dimension of the first Cartier operator is two. The stable rank equals Jacobian \(5\)-rank and the kernel dimension equals the \(a\)-number.

The product of the six fifth-power coefficients is a nonzero unit times \(q^2(\lambda+2)^2\), yielding the Hasse determinant. Swapping the two branch points with the same exponent acts by \(\lambda\mapsto1-\lambda\). For \(t=\lambda(1-\lambda)\), the characteristic-five identities \(q=1-t\) and \((\lambda+2)^2=4-t\) give the claimed two exceptional orbit parameters and the transformed determinant equation. The fixed parameter \(\lambda=3\) maps to \(t=4\); the conjugate roots of \(q\) map to \(t=1\).

## Verification
Run `python3 verify_cyclic_septic.py` using Python's standard library. The program constructs all six polynomials \(G_j\) in \(\mathbb F_5[x,\lambda]\), compares sparse-expansion coefficients with independent binomial-sum coefficients, checks every Cartier coefficient against the displayed formulas, verifies the cycle and iterate ranks, and checks the two invariant-coordinate identities. The exact program reports six `CARTIER_COEFFICIENT_OK` lines followed by `STRATA_OK` and `MODULI_OK`.

## Relationship to prior work
Bouw's work gives foundational characterwise Hasse–Witt methods for ramified abelian prime-to-characteristic covers; Elkin gives bounds and a Cartier framework for cyclic covers; Moonen studies special subvarieties arising from branch-varying cyclic covers. These methods and the general objects are prior work, not new constructions. The contribution asserted here is the explicit **complete** characteristic-five exceptional-locus classification for ramification pattern \((1,1,6,6)\) of degree seven, including the two length-three Cartier strings, both colored-branch orbits and their determinant expression. No equivalent complete calculation was located in the full texts and searches examined, but negative searches do not certify priority.

## Limitations
The claim does not determine the Newton polygon or full Ekedahl–Oort type, classify arbitrary genus-six covers, or identify all geometric curve-isomorphism classes under transformations beyond the marked branch-configuration symmetries stated. The determinant identity uses the displayed differential trivialization. Full historical priority and independent validation remain open.

## References
1. I. I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Math. 126 (2001), 295–322, DOI 10.1023/A:1017513122376.
2. A. Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431 (first submission 2007-08-02; later Journal of Algebra 327 (2011), 1–12).
3. B. Moonen, *Special subvarieties arising from families of cyclic covers of the projective line*, arXiv:1006.3400 (first submission 2010-06-17); Doc. Math. 15 (2010), 793–819.
