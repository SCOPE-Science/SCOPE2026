# Exact seven-level Fourier-frame spectrum on the finite-field paraboloid

## Finding

Let \(q\) be an odd prime power, \(F=\mathbb F_q\), and \(\psi:F\to\mathbb C\) any nontrivial additive character. Equip the paraboloid
\[
S=\{(x,y,x^2+y^2):x,y\in F\}\subset F^3
\]
with probability counting measure. Consider exactly \(3q-2\) restricted additive characters: the constant \(1\); the \(q-1\) characters \(X_a(x,y)=\psi(ax)\) for \(a\ne0\); the \(q-1\) characters \(Y_a(x,y)=\psi(ay)\); and the \(q-1\) characters \(Z_c(x,y)=\psi(c(x^2+y^2))\) for \(c\ne0\). Let \(G\) be their \((3q-2)\)-square Gram matrix, in this order, with the inner product conjugate linear in its first argument.

Put \(s=\chi(-1)/q\), where \(\chi\) is the quadratic multiplicative character of \(F\), and \(t=(q-1)/2\). Let \(u_1<u_2<u_3\) be the three (distinct real) roots of
\[
P_q(u)=u^3+(2-q)u^2-(3q+1)u+2q(q-1).
\]
Then the complete **eigenvalue multiset**, with exact multiplicity, is:

| Eigenvalue | Multiplicity |
|---|---:|
| \(1\) | \(3(q-1)/2\) |
| \(1-s\) | \((q-1)/2\) |
| \(1-s/2+\sqrt{1+16q}/(2q)\) | \((q-3)/2\) |
| \(1-s/2-\sqrt{1+16q}/(2q)\) | \((q-3)/2\) |
| \(1+s u_j\), each \(j=1,2,3\) | \(1\) each |

For \(q=3\) the two square-root rows have zero multiplicity; otherwise there are exactly seven distinct eigenvalues, and for \(q=3\) there are five. **The restricted character family is linearly independent precisely for \(q\ge7\)**; for \(q=3\) and \(q=5\) its nullity is exactly one. At every \(q\ge7\), the smallest and largest displayed eigenvalues are the sharp lower and upper Riesz constants, and their entire equality spaces are the corresponding eigenspaces of \(G\), explicitly constructible by the block decomposition below. In particular the squared condition number is their ratio. For growing prime powers in the indicated congruence classes,
\[
\lim_{q\to\infty,\ q\equiv1\ (\mathrm{mod}\ 4)}\kappa(G)^2=2,
\qquad
\lim_{q\to\infty,\ q\equiv3\ (\mathrm{mod}\ 4)}\frac{\kappa(G)^2}{q}=1.
\]
Thus the same canonical restriction family is uniformly well conditioned along one arithmetic class and becomes linearly ill conditioned along the other.

## Assumptions and scope

All statements are for finite fields of odd cardinality (including nonprime fields), with the normalized surface inner product \(q^{-2}\sum_{x,y\in F}\overline{f(x,y)}g(x,y)\). The chosen frequencies are exactly \((0,0,0)\), \((a,0,0)\), \((0,a,0)\), and \((0,0,c)\), with \(a,c\in F^\times\). No mixed-coordinate or general frequencies are included. Every character has unit norm. The assertion concerns the coefficient Gram matrix, not the full ambient Fourier-extension operator or its \(L^p\)-operator norm.

## Proof

**1. Gauss sums and Gram entries.** Let \(\chi\) be extended by \(\chi(0)=0\), and set \(\gamma=\sum_{z\in F}\chi(z)\psi(z)\). Standard finite-character orthogonality, or the elementary substitution \(z\mapsto-z\), gives \(|\gamma|^2=q\) and \(\gamma^2=\chi(-1)q\). For each \(c\ne0\),
\[
\sum_{x\in F}\psi(cx^2)=\chi(c)\gamma,
\qquad
q^{-2}\sum_{x,y\in F}\psi(cx^2+cy^2)=s.
\]
Thus \(1,X_a,Y_a\) are mutually orthonormal, and for nonzero indices
\[
\langle Z_c,Z_d\rangle=\begin{cases}1&c=d,\\s&c\ne d,\end{cases}\quad
\langle 1,Z_c\rangle=s,\quad
\langle X_a,Z_c\rangle=\langle Y_a,Z_c\rangle=s\psi\!\left(-\frac{a^2}{4c}\right).
\]
The last identity follows by completing the square in one variable and applying the preceding Gauss identity in the other. These are **all** Gram entries.

**2. Orthogonal reduction.** Let \(r=q-1=2t\). For each \(a\in F^\times\), the coefficient-space difference \((X_a-Y_a)/\sqrt2\) has Gram eigenvalue \(1\). Of the sums \(E_a=(X_a+Y_a)/\sqrt2\), the antisymmetric combinations \((E_a-E_{-a})/\sqrt2\) also have eigenvalue \(1\), contributing another \(t\). Hence \(1\) has multiplicity at least \(r+t=3r/2\).

Index the remaining symmetric sums \((E_a+E_{-a})/\sqrt2\) by the \(t\) nonzero quadratic residues \(b=a^2\), and set
\[
H_{b,c}=\psi\!\left(-\frac{b}{4c}\right),\qquad b\in(F^\times)^2,\ c\in F^\times.
\]
On constant / residue sums / vertical frequencies the Gram is
\[
B=\begin{pmatrix}
1&0&s\mathbf1_r^*\\
0&I_t&2sH\\
s\mathbf1_r&2sH^*&(1-s)I_r+s\mathbf1_r\mathbf1_r^*
\end{pmatrix}.
\]
Character orthogonality under inversion \(c\mapsto c^{-1}\) gives the **exact** identities
\[
H\mathbf1_r=-\mathbf1_t,\qquad HH^*=qI_t-J_t.
\]
Let \(L=(q+1)/2=q-t\). On the \((t-1)\)-dimensional sum-zero subspace of \(\mathbb C^t\), the singular value of \(H\) is \(\sqrt q\), and its image under \(H^*\) is orthogonal to \(\mathbf1_r\). Each associated two-dimensional invariant block is
\[
\begin{pmatrix}1&2s\sqrt q\\2s\sqrt q&1-s\end{pmatrix},
\]
whose eigenvalues are \(1-s/2\pm\sqrt{1+16q}/(2q)\), each with multiplicity \(t-1\). The subspace \(\ker H\cap\mathbf1_r^\perp\) has dimension \(t-1\) and eigenvalue \(1-s\).

**3. The four-dimensional residual block.** Let \(u=\mathbf1_t/\sqrt t\), \(v=H^*u/\sqrt L\), and put
\[
A=\langle v,\mathbf1_r\rangle=-\sqrt{t/L},\qquad
D=\sqrt{r-t/L}=\sqrt{q(q-1)/(q+1)},\qquad
k=(\mathbf1_r-Av)/D.
\]
The vectors \(v,k\) are orthonormal and \(Hk=0\). In the orthonormal coordinate order constant, \(u\), \(v\), \(k\), the remaining matrix is
\[
M=\begin{pmatrix}
1&0&sA&sD\\
0&1&2s\sqrt L&0\\
sA&2s\sqrt L&1-s+sA^2&sAD\\
sD&0&sAD&1-s+sD^2
\end{pmatrix}.
\]
A two-step Schur-complement determinant calculation, or direct expansion using \(L=(q+1)/2\), gives
\[
\det(\lambda I-M)=(\lambda-1+s)s^3
P_q\!\left(\frac{\lambda-1}{s}\right).
\]
Hence the residual eigenvalues are \(1-s\) and the three cubic values. This supplies the remaining copy of \(1-s\) and completes the multiplicity count. The equality spaces are fully constructive: combine the explicit antisymmetric and sum-zero blocks above with the nullspaces of the displayed \(2\)- and \(4\)-dimensional Hermitian matrices. These subspaces form an orthogonal direct sum of the entire coefficient space; no numerical eigenvector choices are required.

**4. Reality, separation, and rank.** The discriminant of \(P_q\), on putting \(h=q-3\), equals
\[
8h^5+73h^4+306h^3+933h^2+2172h+2420>0.
\]
Thus its roots are real and pairwise distinct for every odd \(q\ge3\). Values \(P_q(0)=2q(q-1)\) and \(P_q(-1)=2(q^2+1)\) exclude collisions with \(1\) and \(1-s\). The two square-root eigenvalues correspond, after setting \(u=(\lambda-1)/s\), to \(u^2+u-4q=0\), whose resultant with \(P_q\) is \(4q(q-3)(q-1)^2\). Accordingly the stated distinctness follows for \(q\ge5\).

The Gram matrix is positive semidefinite by construction. A zero among cubic values would require \(u=-1/s\). For \(s=-1/q\), this gives \(P_q(q)=q(q-3)\); for \(s=1/q\), it gives \(P_q(-q)=-q(2q^2-7q+1)\). Only \(q=3\) gives a zero from the cubic. The lower square-root value is zero exactly when \(s=1/q\) and \(q=5\); it has multiplicity one there. All other values are positive, proving the rank assertions.

**5. Asymptotic conditioning.** The largest cubic root satisfies \(u_3=q-1+O(q^{-1})\), as is seen by substitution into \(P_q\) and the derivative estimate \(P'_q(q-1)=q^2+O(q)\); the other two roots are \(O(\sqrt q)\), by the root sum and product or Vieta. The two square-root branches equal \(1+O(q^{-1/2})\), as does \(1-s\). For \(q\equiv1\pmod4\), the cubic top tends to \(2\), while all other spectral branches tend to \(1\), hence \(\kappa^2\to2\). For \(q\equiv3\pmod4\), the cubic top root produces the smallest eigenvalue \(1-u_3/q=q^{-1}+O(q^{-2})\), while the largest eigenvalue tends to \(1\), hence \(\kappa^2/q\to1\).

## Verification

Run `python paraboloid_frame_check.py` with NumPy installed. This independently forms the actual character columns, computes their Gram eigenvalues, and compares the ordered eigenvalue lists with the theorem for prime fields of orders \(3,5,7,11,13,17,19,23\) and the nonprime fields of orders \(9,25\). The quadratic extension implementation computes field multiplication and the trace additive character explicitly. The checker also verifies the one-dimensional nullspaces at \(3\) and \(5\). This is finite corroboration, **not** the proof for infinitely many fields; the preceding character identities and block reduction give the unrestricted result.

## Relationship to prior work

Mockenhaupt and Tao introduced finite-field Fourier restriction for the paraboloid, and Iosevich and Koh calculated its Fourier surface measure and developed extension estimates. Their estimates and Gauss identities motivate the present measurement family but do not determine this exact chosen coefficient Gram spectrum. Casazza and Fickus studied finite cyclic chirps and their frame correlations; their cyclic Fourier-transform formulas are not an exact spectral classification of the three-coordinate Fourier restriction on the finite-field paraboloid. The claim is the entire seven-level spectrum, equality eigenspaces, two exceptional dependencies, and congruence-dependent condition-number asymptotics; none is asserted to be a new Gauss-sum identity.

## Limitations

Only the stated first-coordinate frequency family is classified; general Fourier frequencies and arbitrary quadratic surfaces are not. The spectral formulas use cubic roots rather than elementary radicals. Exact novelty relative to all historical equivalent formulations in finite chirp-frame literature has not been independently certified. The same-model review is not an independent audit.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (initial public version 18 April 2002), Duke Math. J. 121 (2004), 35–74. https://arxiv.org/abs/math/0204234
2. P. G. Casazza and M. Fickus, *Fourier Transforms of Finite Chirps*, EURASIP J. Adv. Signal Process. 2006, Article 70204. https://doi.org/10.1155/ASP/2006/70204
3. A. Iosevich and D. Koh, *Extension Theorems for Paraboloids in the Finite Field Setting*, arXiv:0805.0814 (initial public version 6 May 2008). https://arxiv.org/abs/0805.0814
4. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (28 April 2008). https://arxiv.org/abs/0804.4505
