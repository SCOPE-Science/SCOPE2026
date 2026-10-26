# A genus-preserving leaf-to-internal injection for multiplicity-four numerical semigroups

## Finding

For every integer \(g\ge 3\), the leaves among numerical semigroups of multiplicity \(4\) and genus \(g\) admit an explicit **genus-preserving injection** into the internal semigroups of the same multiplicity and genus. In particular, if \(L_4(g)\) and \(I_4(g)\) are the respective numbers, then

\[
L_4(g)\le I_4(g)\qquad(g\ge3).
\]

More precisely, with the four counting functions below (taken to be zero outside the indicated parity and lower-bound ranges),

\[
\begin{aligned}
A_{2s+1}&=s-\left\lceil\frac{s-1}{3}\right\rceil &&(s\ge2),\\
B_{2s}&=s-\left\lceil\frac{s}{3}\right\rceil &&(s\ge2),\\
C_g&=\max\left\{0,\left\lfloor\frac g4\right\rfloor-\left\lceil\frac{g+2}{5}\right\rceil+1\right\},\\
D_g&=\max\left\{0,\left\lfloor\frac{g-2}{4}\right\rfloor-\left\lceil\frac{g-1}{5}\right\rceil+1\right\},
\end{aligned}
\]

one has \(L_4(g)=A_g+B_g+C_g+D_g\). Consequently,

\[
L_4(g)=\frac{13}{30}g+O(1),\qquad
\frac{L_4(g)}{L_4(g)+I_4(g)}=\frac{26}{5g}+O(g^{-2}).
\]

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\); its multiplicity is its smallest positive element, its genus is the number of nonnegative integers it omits, and its Frobenius number \(F\) is its largest omitted integer. A semigroup is **internal** in the usual numerical-semigroup tree if it has a child obtained by removing some minimal generator exceeding \(F\); otherwise it is a **leaf**. We use the full numerical-semigroup tree, not the separate fixed-multiplicity subtree. All results concern **every** multiplicity-four semigroup with genus \(g\ge3\); no Frobenius-number or embedding-dimension restriction is imposed.

Its Apéry set modulo \(4\) is uniquely

\[
\operatorname{Ap}(S,4)=\{0,4a+1,4b+2,4c+3\},
\]

where \(a,b,c\) are positive integers satisfying the complete Kunz inequalities

\[
b\le2a,\quad c\le a+b,\quad a\le b+c+1,\quad b\le2c+1.
\]

Conversely every such triple defines one semigroup. Its genus is \(g=a+b+c\), and its Frobenius number equals \(\max\{4a+1,4b+2,4c+3\}-4\).

## Proof

**1. Effective generators and the leaf partition.** Write \(w_1=4a+1\), \(w_2=4b+2\), \(w_3=4c+3\). Each minimal generator other than \(4\) must be an Apéry element. The only possible decompositions between positive Apéry elements are

\[
\begin{array}{c|c}
\text{nonminimal element}&\text{necessary and sufficient equality}\\ \hline
w_1&w_1=w_2+w_3\iff a=b+c+1\\
w_2&w_2=2w_1\iff b=2a\quad\text{or}\quad w_2=2w_3\iff b=2c+1\\
w_3&w_3=w_1+w_2\iff c=a+b.
\end{array}
\]

Indeed, any decomposition of an Apéry element into two positive semigroup elements can be reduced modulo \(4\) to a sum of nonzero Apéry elements; a positive multiple of \(4\) cannot occur because of minimality in the residue class. The displayed equalities exhaust the residue-compatible two-term decompositions, and any longer decomposition contains a two-term decomposition.

If \(g=3\), the only triple is \((1,1,1)\), and generator \(4\) exceeds the Frobenius number \(3\): it is internal. Assume henceforth \(g\ge4\); then \(F\ge4\) and generator \(4\) is not effective. If \(w_1\) is nonminimal, then \(w_1=w_2+w_3\), so both other Apéry elements are at least four less than \(w_1\). The same applies to \(w_3=w_1+w_2\). When \(w_2=2w_1\), both other elements lie at most \(F\) exactly when \(c\le 2a-2\); when \(w_2=2w_3\), this is equivalent to \(a\le 2c\). Thus a semigroup is a leaf precisely when its Kunz triple belongs to one of the following **pairwise disjoint** sets:

\[
\begin{array}{ll}
\mathcal A:&a=b+c+1,\\
\mathcal B:&c=a+b,\\
\mathcal C:&b=2a,\ \ a\le c\le 2a-2,\\
\mathcal D:&b=2c+1,\ \ c+1\le a\le 2c.
\end{array}
\]

Here the inequalities in \(\mathcal C\) and \(\mathcal D\) are the Kunz conditions combined with the requirement that the nonminimal Apéry element be the only Apéry element above \(F\). The four sets are mutually exclusive: \(\mathcal A\) and \(\mathcal B\) cannot coincide with each other or with the equality defining \(\mathcal C\) or \(\mathcal D\); the \(\mathcal C\) and \(\mathcal D\) ranges are also incompatible.

**2. Constructing the injection.** On the four leaf sets respectively, define

\[
\Phi(a,b,c)=\begin{cases}
(a-1,b,c+1),& (a,b,c)\in\mathcal A,\\
(a+1,b,c-1),& (a,b,c)\in\mathcal B,\\
(a+1,b-1,c),& (a,b,c)\in\mathcal C\cup\mathcal D.
\end{cases}
\]

Every target coordinate is positive and every target satisfies the four Kunz inequalities. For example, for \(\mathcal C\) the input restrictions \(b=2a\) and \(a\le c\le2a-2\) give output \((a+1,2a-1,c)\); the four Kunz inequalities follow directly. For \(\mathcal D\), \(c+1\le a\le2c\) gives \((a+1,2c,c)\). The equalities \(a=b+c+1\) or \(c=a+b\) establish admissibility in the remaining two cases. All branches preserve \(a+b+c\).

To check **both non-leaf status and injectivity**, let \((x,y,z)=\Phi(a,b,c)\). The four image sets obey respectively

\[
\begin{array}{ll}
\Phi(\mathcal A):&x=y+z-1,\quad y\le2z-1,\\
\Phi(\mathcal B):&z=x+y-2,\\
\Phi(\mathcal C):&y=2x-3,\quad x\ge3,\quad x-1\le z\le2x-4,\\
\Phi(\mathcal D):&y=2z,\quad z+2\le x\le2z+1.
\end{array}
\]

No target satisfies any of the four leaf conditions: the respective equations exclude the \(\mathcal A\) and \(\mathcal B\) equalities, and the respective inequalities exclude \(\mathcal C\) and \(\mathcal D\). For clarity, on the first image \(x=y+z-1\) misses the leaf equality \(x=y+z+1\), \(z=x+y\) would force \(2y=1\), \(y=2x\) is impossible for positive \(y,z\), and \(y=2z+1\) contradicts \(y\le2z-1\). The other three images are checked by direct substitution into the displayed conditions.

Each branch of \(\Phi\) is a translation and hence injective. The four image sets are mutually disjoint: intersection of the first two would force \(2y=3\); first and third would force \(z=4-x<x-1\) for \(x\ge3\); first and fourth contradict \(y\le2z-1\) and \(y=2z\); second and third would give \(z=3x-5>2x-4\) for \(x\ge3\); second and fourth would give \(x=2-z<z+2\); and third and fourth have \(y\) respectively odd and even. Thus \(\Phi\) injects leaves of genus \(g\) into internal semigroups of the same genus, proving \(L_4(g)\le I_4(g)\).

**3. Counting and asymptotics.** In \(\mathcal A\), \(g=2(b+c)+1\); putting \(b+c=s\) gives the range \(\lceil(s-1)/3\rceil\le c\le s-1\). In \(\mathcal B\), \(g=2(a+b)\); putting \(a+b=s\) gives \(\lceil s/3\rceil\le a\le s-1\). In \(\mathcal C\), \(g=3a+c\) and \(a\le c\le2a-2\), so \(\lceil(g+2)/5\rceil\le a\le\lfloor g/4\rfloor\). In \(\mathcal D\), \(g=a+3c+1\) and \(c+1\le a\le2c\), so \(\lceil(g-1)/5\rceil\le c\le\lfloor(g-2)/4\rfloor\). These are exactly the four formulas in the statement.

The parity-specific leading term from \(\mathcal A\) or \(\mathcal B\) is \(g/3\), and each of \(\mathcal C\) and \(\mathcal D\) contributes \(g/20\), up to bounded errors. This gives \(L_4(g)=13g/30+O(1)\). The previously known partition enumeration of all multiplicity-four semigroups gives \(L_4(g)+I_4(g)=g^2/12+O(g)\), yielding the asserted leaf proportion.

## Verification

Run `python3 VERIFY.py` using only Python's standard library. It independently tests semigroup membership and genuine minimal generators, checks the four leaf classes against the actual Frobenius-number definition, constructs all injection images and detects collisions, and compares the exact four-family formulas for every genus from \(3\) through \(80\). Expected output begins with `VERIFY_OK`. These finite checks do **not** establish the infinite-genus claim; the proof above does.

## Relationship to prior work

Casas, Madrid and Rosales (2026), *Internal numerical semigroups*, conjecture that internal semigroups dominate leaves at fixed multiplicity and genus. Their published abstract and separately indexed Section 6 description identify the conjecture, while a complete copy of that source's paper was not accessible for comparison. The present theorem proves the full claim for multiplicity \(4\), gives an explicit genus-preserving injection, and derives a closed leaf-count formula.

García-Sánchez, Marín-Aragón and Robles-Pérez (2018), *The tree of numerical semigroups with low multiplicity*, give the Kunz-coordinate framework and count **all** multiplicity-four semigroups of fixed genus (their Section 3 and Corollary 18). They explicitly discuss the difficulty of a child-count approach for multiplicity four; their result does not give the leaf-to-internal injection or the four leaf-count formulas. Bras-Amorós and Torra (2026) study multiparameter enumeration and differently defined leaf-discriminating enumeration trees, not the above full-tree leaf split.

## Limitations

The proof concerns multiplicity exactly \(4\). It does not establish the dominance conjecture for other multiplicities, fixed Frobenius number, or unrestricted semigroups. The asymptotic estimate is for genus tending to infinity with multiplicity fixed. A full primary-text comparison with the 2026 motivating paper could not be completed; the originality assessment therefore retains a specific bibliographic risk, and independent mathematical review has not been performed.

## References

1. M. Casas, J. A. Madrid and J. C. Rosales, *Internal numerical semigroups*, arXiv:2608.19984v1 (first public: 2026-08-20), https://arxiv.org/abs/2608.19984.
2. P. A. García-Sánchez, D. Marín-Aragón and A. M. Robles-Pérez, *The tree of numerical semigroups with low multiplicity*, arXiv:1803.06879v1 (2018), https://arxiv.org/abs/1803.06879.
3. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups: recurrences and leaf-discriminating trees*, arXiv:2607.23111 (first public: 2026-07-25), https://arxiv.org/abs/2607.23111.
