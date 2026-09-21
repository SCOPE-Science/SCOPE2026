# Exact L1 endpoint profile for weighted conditional expectation operators

## Result

Let \((X,\Sigma,\mu)\) be a complete sigma-finite measure space, let
\(\mathcal A\subseteq\Sigma\) be a sigma-finite sub-sigma-algebra, and let
\(E=E^{\mathcal A}\) be conditional expectation.  Suppose that
\[
T=M_wEM_u:L^1(\Sigma)\longrightarrow L^1(\Sigma)
\]
is bounded.  Put
\[
q=E(|w|).
\]
The standard \(L^1\) boundedness theorem gives \(qu\in L^\infty(\Sigma)\).

Write the canonical atomic/non-atomic decomposition of
\((X,\mathcal A,\mu|_{\mathcal A})\), modulo null sets, as
\[
X=B\sqcup\coprod_{n\in I} A_n ,
\]
where \(B\) is \(\mathcal A\)-non-atomic and the \(A_n\) are the at most
countably many \(\mathcal A\)-atoms.  Since \(\mathcal A\) is sigma-finite,
every \(A_n\) has finite measure.  The \(\mathcal A\)-measurable function
\(q\) is constant almost everywhere on each \(A_n\); denote that constant by
\(q_n\).  Define
\[
\gamma=\|qu\,\chi_B\|_\infty,\qquad
c_n=q_n\|u\chi_{A_n}\|_\infty ,
\]
with \(c_n=0\) if \(q_n=0\).  For \(k\ge1\), set
\[
c_k^*=\inf_{\substack{F\subset I\\ |F|<k}}\ \sup_{n\notin F}c_n ,
\]
where the supremum of an empty set is \(0\).

Then for every \(k\ge1\),
\[
\boxed{\quad a_k(T)=b_k(T)=\max\{\gamma,c_k^*\}.\quad}
\]
Here \(a_k\) and \(b_k\) are the approximation and Bernstein numbers.

If
\[
\rho=\max\left\{\gamma,\lim_{k\to\infty}c_k^*\right\},
\]
then
\[
\boxed{
\operatorname{dist}(T,\mathcal K)
=\operatorname{dist}(T,\mathcal{FSS})
=\operatorname{dist}(T,\mathcal{SS})
=\rho .
}
\]
Consequently
\[
T\text{ compact}\iff T\text{ finitely strictly singular}
\iff T\text{ strictly singular}
\iff \gamma=0\ \text{and}\ c_n\to0 .
\]
More quantitatively, whenever \(0<t<\rho\), \(T\) is bounded below by \(t\)
on a \(1\)-complemented subspace of \(L^1(\Sigma)\) isometric to \(\ell_1\).

Finally, \(T\) is nuclear if and only if
\[
\boxed{\quad \gamma=0,\qquad \sum_{n\in I}c_n<\infty.\quad}
\]
In that case the nuclear norm is exact:
\[
\boxed{\quad \|T\|_{\mathcal N}=\sum_{n\in I}c_n.\quad}
\]

Thus the correct \(L^1\) endpoint is controlled by an essential-supremum
quantity inside each \(\mathcal A\)-atom, not by the conditional average of
\(|u|\) on that atom.

## Block structure

For \(f\in L^1(\Sigma)\),
\[
\begin{aligned}
\|Tf\|_1
&=\int |w|\,|E(uf)|\,d\mu\\
&=\int q\,|E(uf)|\,d\mu
 =\int |E(quf)|\,d\mu .
\end{aligned}
\]
Hence \(T\), as far as its \(L^1\)-norm is concerned, is the conditional
averaging operator \(f\mapsto E(quf)\).

On an \(\mathcal A\)-atom \(A_n\),
\[
E(uf)|_{A_n}
=\frac1{\mu(A_n)}\int_{A_n}uf\,d\mu,
\]
and therefore
\[
T|_{L^1(A_n)}
=
\left(f\mapsto \int_{A_n}uf\,d\mu\right)
\otimes \frac{w\chi_{A_n}}{\mu(A_n)} .
\]
This is rank one and has norm
\[
\left\|T|_{L^1(A_n)}\right\|
=\|u\chi_{A_n}\|_\infty
 \frac{\|w\chi_{A_n}\|_1}{\mu(A_n)}
=q_n\|u\chi_{A_n}\|_\infty=c_n.
\]
On \(B\) the norm is exactly \(\gamma\).  The upper bound is immediate from
\(\|E(quf)\|_1\le\|qu\chi_B\|_\infty\|f\|_1\).  For the lower bound, choose
\(f\) supported where \(|qu|\) is arbitrarily close to \(\gamma\), with
phase chosen so that \(quf\ge0\); then
\(\|E(quf)\|_1=\int |qu||f|\,d\mu\).

The disjoint decomposition
\[
L^1(\Sigma)
=L^1(B)\oplus_1\bigoplus_{n\in I}^{\ell_1}L^1(A_n)
\]
therefore makes \(T\) an \(\ell_1\)-sum of one non-atomic block of norm
\(\gamma\) and rank-one atomic blocks of norms \(c_n\).

## Approximation and Bernstein numbers

For any finite \(F\subset I\), let \(T_F\) retain only the atomic blocks
indexed by \(F\).  Then \(\operatorname{rank}T_F\le |F|\) and
\[
\|T-T_F\|
=\max\left\{\gamma,\sup_{n\notin F}c_n\right\}.
\]
Taking \(|F|<k\) gives
\[
a_k(T)\le \max\{\gamma,c_k^*\}.
\]

For the reverse inequality, recall
\[
b_k(T)=\sup_{\dim E=k}\inf_{\substack{x\in E\\\|x\|=1}}\|Tx\|.
\]
If \(t<c_k^*\), there are \(k\) distinct atoms with \(c_n>t\).
Choose disjoint unit vectors \(f_1,\dots,f_k\), one in each corresponding
\(L^1(A_n)\), almost norming the rank-one functional
\(f\mapsto\int_{A_n}uf\).  Their images have disjoint supports, so
\[
\left\|T\sum_{j=1}^k\alpha_jf_j\right\|_1
\ge t\sum_{j=1}^k|\alpha_j|
=t\left\|\sum_{j=1}^k\alpha_jf_j\right\|_1 .
\]

If \(t<\gamma\), put
\[
D=\{x\in B:|qu(x)|>t\}.
\]
The finite or sigma-finite measure
\(\nu(C)=\mu(C\cap D)\), \(C\in\mathcal A|_B\), is non-atomic because it is
absolutely continuous with respect to the non-atomic measure
\(\mu|_{\mathcal A|_B}\).  After restricting to a finite positive-measure
piece if necessary, partition it into \(k\) disjoint
\(\mathcal A\)-measurable sets \(C_j\) with
\(\mu(D\cap C_j)>0\).  Choose disjoint normalized \(f_j\), supported in
\(D\cap C_j\), with phase making \(quf_j\ge t|f_j|\).  Then
\(E(quf_j)\) is supported in \(C_j\), and again
\[
\left\|T\sum_j\alpha_jf_j\right\|_1
\ge t\sum_j|\alpha_j|.
\]
Letting \(t\) increase to the relevant threshold yields
\[
b_k(T)\ge\max\{\gamma,c_k^*\}.
\]
Since \(b_k(T)\le a_k(T)\), equality follows.

## Compactness, strict singularity, and exact distances

Finite atomic truncations give
\[
\operatorname{dist}(T,\mathcal K)\le\rho.
\]
Conversely, for every \(t<\rho\), either the non-atomic construction above
can be continued countably many times, or infinitely many atomic blocks
satisfy \(c_n>t\).  In either case there is a disjoint normalized sequence
\((f_j)\) whose span \(E_0\) is isometric to \(\ell_1\) and
\[
\|Tx\|_1\ge t\|x\|_1\qquad(x\in E_0).
\]
This copy of \(\ell_1\) is \(1\)-complemented.  Indeed, choose
\(g_j\in L^\infty\), supported on \(\operatorname{supp}f_j\), with
\(\|g_j\|_\infty=1\) and \(\int f_jg_j\,d\mu=1\).  Then
\[
Ph=\sum_j\left(\int hg_j\,d\mu\right)f_j
\]
defines a contractive projection onto \(E_0\).

If \(S\) is strictly singular, \(S|_{E_0}\) is not bounded below.  Hence for
every \(\varepsilon>0\) there is a unit \(x\in E_0\) with
\(\|Sx\|<\varepsilon\), and therefore
\[
\|T-S\|\ge t-\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) and \(t\uparrow\rho\) gives
\(\operatorname{dist}(T,\mathcal{SS})\ge\rho\).  Since
\[
\mathcal K\subseteq\mathcal{FSS}\subseteq\mathcal{SS},
\]
all three distances equal \(\rho\), and the compact/FSS/SS equivalence
follows.

## Nuclearity and the exact nuclear norm

Assume first that \(\gamma=0\).  For every atom define
\[
\phi_n(f)=\int_{A_n}uf\,d\mu,\qquad
y_n=\frac{w\chi_{A_n}}{\mu(A_n)}.
\]
Then
\[
\|\phi_n\|=\|u\chi_{A_n}\|_\infty,\qquad
\|y_n\|_1=q_n,
\]
and, if \(\sum_n c_n<\infty\),
\[
T=\sum_n\phi_n\otimes y_n
\]
is a nuclear representation.  Thus
\[
\|T\|_{\mathcal N}\le\sum_n c_n.
\]

Conversely, suppose \(T\) is nuclear.  Then it is compact, so the preceding
result gives \(\gamma=0\).  Fix a finite \(F\subset I\) and
\(\varepsilon>0\).  For each \(n\in F\), choose a normalized
\(x_n\in L^1(A_n)\), with a phase adjustment, such that
\[
\phi_n(x_n)\ge(1-\varepsilon)\|\phi_n\|.
\]
Choose \(\psi_n\in L^\infty(A_n)\), \(\|\psi_n\|_\infty=1\), satisfying
\[
\int_{A_n}\psi_n y_n\,d\mu=\|y_n\|_1=q_n.
\]
The disjoint-support map
\[
J:\ell_1^F\to L^1(\Sigma),\qquad J(a)=\sum_{n\in F}a_nx_n,
\]
is an isometry, while
\[
Q:L^1(\Sigma)\to\ell_1^F,\qquad
Q(g)=\left(\int_{A_n}\psi_ng\,d\mu\right)_{n\in F}
\]
is a contraction.  The operator \(QTJ\) is diagonal on \(\ell_1^F\), with
diagonal entries at least \((1-\varepsilon)c_n\).  By the ideal property of
the nuclear norm and the trace lower bound for finite-dimensional nuclear
operators,
\[
\|T\|_{\mathcal N}
\ge\|QTJ\|_{\mathcal N}
\ge\operatorname{tr}(QTJ)
\ge(1-\varepsilon)\sum_{n\in F}c_n.
\]
Letting \(\varepsilon\downarrow0\) and then exhausting \(I\) by finite sets
gives
\[
\|T\|_{\mathcal N}\ge\sum_n c_n.
\]
This proves both necessity and the exact norm formula.

## Two counterexamples to previously stated L1 criteria

### The 2013/2014 compactness criterion

Estaremi--Jabbarzadeh (2013), Theorem 2.7, states for \(L^1\) that compactness
is equivalent to every threshold set
\[
\{x:|u(x)|E(|w|)(x)\ge\varepsilon\}
\]
being a union of finitely many \(\Sigma\)-atoms.  Estaremi (2014) gives the
same \(L^1\) criterion by a different proof.

As stated, this fails for the simplest conditional expectation onto a
trivial sigma-algebra.  Take \(X=[0,1]\) with Lebesgue measure,
\(\mathcal A=\{\varnothing,X\}\), and \(u=w=1\).  Then
\[
Tf=E(f)=\int_0^1f\,d\mu
\]
is rank one, hence compact and nuclear.  For every \(0<\varepsilon<1\),
however, the threshold set is all of \(X\), while the Lebesgue
\(\Sigma\)-space has no atoms.  In the formula above, \(\mathcal A\) has one
atom \(X\), \(c_1=1\), \(c_k^*=0\) for \(k\ge2\), and the profile correctly
detects finite rank.

### The 2026 L1 nuclearity criterion

Al Ghafri--Shamsigamchi--Estaremi (2026), Proposition 2.6 and Theorem 2.9,
state an \(L^1\) atomic nuclearity condition using
\[
\sum_n E(|w|)(A_n)E(|u|)(A_n).
\]
Their proof estimates the norm of
\[
\phi_n(f)=\int_{A_n}uf\,d\mu
\]
by \(E(|u|)(A_n)\).  On \(L^1\), however,
\[
\|\phi_n\|=\|u\chi_{A_n}\|_\infty,
\]
which can be much larger than the conditional average.

A concrete purely atomic counterexample is as follows.  Let
\[
X=\coprod_{n\ge1}A_n,\qquad |A_n|=2^n,
\]
with counting measure, let \(\Sigma=2^X\), and let \(\mathcal A\) be generated
by the blocks \(A_n\).  Choose one distinguished point \(a_n\in A_n\), and
set
\[
u(a_n)=2^n,\quad u=0\text{ on }A_n\setminus\{a_n\},\qquad
w=2^{-n}\text{ on }A_n.
\]
Then
\[
E(|u|)(A_n)=E(u)(A_n)=1,\qquad E(|w|)(A_n)=2^{-n},
\]
so the stated average-based nuclear series converges, and the compactness
threshold in Theorem 2.5 also tends to zero.  But for \(x\in A_n\),
\[
Tf(x)=2^{-n}f(a_n).
\]
Thus
\[
\|Te_{a_n}\|_1=1
\]
and the vectors \(Te_{a_n}\) have disjoint supports.  Hence \(T\) is an
isometry on the \(1\)-complemented copy
\(\overline{\operatorname{span}}\{e_{a_n}\}\cong\ell_1\); it is neither
strictly singular nor compact, and therefore is not nuclear.  The corrected
coefficients are \(c_n=2^{-n}\cdot2^n=1\).

## Relation to prior work and originality

The \(L^1\) boundedness identity
\[
\|M_wEM_u\|=\|uE(|w|)\|_\infty
\]
is prior work and is used here without a novelty claim.  Estaremi and
Jabbarzadeh (2013) studied boundedness and compactness of weighted Lambert
operators, and Estaremi (2014) revisited compactness and essential norms.
The 2026 preprint of Al Ghafri, Shamsigamchi and Estaremi studies nuclearity.

The contribution claimed here, to the best of our knowledge, is the corrected
\(L^1\) block invariant
\[
c_n=E(|w|)(A_n)\|u\chi_{A_n}\|_\infty,
\]
the exact all-\(k\) formula \(a_k=b_k=\max\{\gamma,c_k^*\}\), the exact
distances to compact/FSS/SS operators, the complemented-\(\ell_1\) witness
for every noncompact operator in this class, and the exact nuclear criterion
and nuclear norm.  The two elementary examples above show that the previously
stated \(L^1\) compactness and average-based nuclearity criteria cannot hold
as written.

A residual originality risk remains: older Banach-lattice work on
multiplication--conditional-expectation operators, including the general
representation literature, may imply parts of the block decomposition under
different terminology.  No source was located that gives this corrected
\(L^1\) all-\(k\) profile or the exact nuclear norm formula.

## References

1. Y. Estaremi and M. R. Jabbarzadeh, *Weighted Lambert type operators on
   \(L^p\) spaces*, Operators and Matrices **7** (2013), 101--116.
   https://doi.org/10.7153/oam-07-05
2. Y. Estaremi, *Essential norm of weighted conditional type operators on
   \(L^p\)-spaces*, Positivity **18** (2014), 41--52.
   https://doi.org/10.1007/s11117-013-0229-5
3. M. S. Al Ghafri, S. Shamsigamchi and Y. Estaremi,
   *Weighted conditional expectation operators and nuclearity*,
   arXiv:2602.19105v1 (2026).
   https://arxiv.org/abs/2602.19105
4. J. J. Grobler and B. de Pagter, *Operators representable as
   multiplication-conditional expectation operators*, Journal of Operator
   Theory **48** (2002), 15--40.
