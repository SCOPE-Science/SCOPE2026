# Most square-zero transformations avoid largest commutative nilpotent semigroups

## Finding

For every integer \(n\ge5\), let \(T_n\) be the full transformation monoid of an \(n\)-point labeled set, and let \(Q_n\) be the set of maps \(f\in T_n\) for which \(f^2\) is constant. Write \(\mathcal M_n\) for the maximum-cardinality commutative nilpotent subsemigroups of \(T_n\). The following is an exact extension count and an asymptotic separation result.

Define \(\mathcal I_n=\operatorname*{arg\,max}_{1\le t\le n}t^{n-t}\), with \(t_- =\min\mathcal I_n\) and \(t_+=\max\mathcal I_n\). Put \(S(m,a)\) for a Stirling number of the second kind, with \(S(0,0)=1\). Then the number \(E_n\) of elements of \(Q_n\) belonging to at least one semigroup in \(\mathcal M_n\) is exactly

\[
E_n=n\sum_{b=t_-}^{n}{n-1\choose b-1}
\sum_{a=0}^{\min(t_+-1,b-1,n-b)}
{b-1\choose a}\,a!\,S(n-b,a).
\]

The total number of square-zero transformations (including the constant maps) is

\[
|Q_n|=n\sum_{b=1}^{n}{n-1\choose b-1}(b-1)^{n-b},
\]

where \(0^0=1\). If \(f\) is uniform on \(Q_n\), then

\[
\Pr\bigl(f\in\bigcup\mathcal M_n\bigr)
=\frac{E_n}{|Q_n|}
=O\!\left(\frac{\log n}{\sqrt n\,\log\log n}\right)
\longrightarrow0.
\]

Thus, although every element of \(Q_n\) lies in some (not necessarily maximum-cardinality) null transformation semigroup, asymptotically almost none lie in any *largest* commutative nilpotent one.

## Assumptions and scope

Composition is ordinary transformation composition. A semigroup is nilpotent when a sufficiently long product of arbitrary elements equals its zero; *null* means every product of two elements equals its zero. The phrase "square-zero transformation" means specifically that \(f^2\) is a constant transformation, not that \(f\) itself is constant. The theorem concerns labeled transformations and sampling uniformly from \(Q_n\), not uniformly from all of \(T_n\), nor uniformly from subsemigroups. The classification of maximum-cardinality commutative nilpotent subsemigroups used below is due to Cain, Malheiro and Paulista, building on Cameron and collaborators, and is not claimed here.

For a fixed point \(c\) and a set \(Y\) containing \(c\), define

\[
N(c,Y)=\{g:X\to X:g(X)\subseteq Y,\quad g(y)=c\text{ for all }y\in Y\}.
\]

Every such \(N(c,Y)\) is null and has size \(|Y|^{n-|Y|}\). The cited extremal classification implies that, for \(n\ge5\), the members of \(\mathcal M_n\) are exactly these \(N(c,Y)\) with \(|Y|\in\mathcal I_n\). The set \(\mathcal I_n\) has one or two adjacent integers because \((n-t)\log t\) is strictly concave as a function of positive real \(t\).

## Proof

**1. Individual containment criterion.** If \(f^2\) is constant with value \(c\), then \(f(c)=c\), since \(f\circ f^2=f^2\circ f\). Set \(B=f^{-1}(c)\), \(b=|B|\), and \(k=|\operatorname{im}f|\). The identity \(f^2=c\) says precisely that \(\operatorname{im}f\subseteq B\), hence \(1\le k\le b\). By the definition of \(N(c,Y)\),

\[
f\in N(c,Y)\quad\Longleftrightarrow\quad
\operatorname{im}f\subseteq Y\subseteq B.
\]

Therefore \(f\) belongs to some largest commutative nilpotent subsemigroup precisely when \(k\le t\le b\) for some \(t\in\mathcal I_n\), equivalently \(b\ge t_-\) and \(k\le t_+\). The last equivalence uses \(k\le b\) and the fact that \(\mathcal I_n\) consists of consecutive integers.

**2. Exact counts.** There are \(n\) choices of \(c\), followed by \({n-1\choose b-1}\) choices of \(B\) containing \(c\). Every point of \(B\) must map to \(c\), while each of the other \(n-b\) points may independently map to any of the \(b-1\) points of \(B\setminus\{c\}\). This proves the total-count formula. To count maps with \(k=a+1\), choose the \(a\) distinct noncentral image points and distribute the \(n-b\) outside points surjectively onto them. This gives \({b-1\choose a}a!S(n-b,a)\). The criterion in step 1 now proves the displayed formula for \(E_n\), including the boundary case \(b=n\).

**3. Location of the zero-fiber size.** Conditional on choosing a uniform member of \(Q_n\), the random variable \(B_n=|f^{-1}(c)|\) has mass proportional to

\[
F_n(b)={n-1\choose b-1}(b-1)^{n-b},\qquad 1\le b\le n.
\]

For \(2\le b<n\) its consecutive-weight ratio is

\[
R_n(b)=\frac{F_n(b+1)}{F_n(b)}
=\frac{n-b}{b^2}\left(\frac{b}{b-1}\right)^{n-b}.
\]

This ratio decreases strictly with \(b\). Let \(L=\log n\), \(\ell=\log\log n\). The maximizer of the real function \((n-t)\log t\) is \(n/W(en)\), where \(W\) is the positive Lambert function. Thus

\[
t_+=\frac{n}{L-\ell+1+o(1)}+O(1).
\]

Uniformly for \(b\asymp n/L\), direct expansion of the displayed exact ratio gives

\[
\log R_n(b)=\frac nb-L+2\log\!\left(\frac nb\right)-1+o(1).
\]

Set \(b_1=\left\lceil n/(L-3\ell/2)\right\rceil\) and \(b_2=\left\lfloor n/(L-7\ell/4)\right\rfloor\). For all sufficiently large \(n\), these are well-defined, \(t_+<b_1<b_2\), and

\[
b_1-t_+\ge\frac{n\ell}{4L^2},\qquad
b_2-b_1\ge\frac{n\ell}{5L^2},\qquad
\log R_n(b)\ge\frac\ell8\quad(2\le b\le b_2).
\]

Monotonicity of the ratio and comparison of \(F_n(b_1)\) with \(F_n(b_2)\) give

\[
\Pr(B_n\le b_1)
\le n\exp\!\left(-\frac{n\ell^2}{40L^2}\right).
\]

Likewise, for \(b\ge\lceil3n/(2L)\rceil\), the expansion and monotonicity give \(\log R_n(b)\le-L/6\) eventually. Comparing the weights at \(\lceil3n/(2L)\rceil\) and \(\lceil2n/L\rceil\), and then summing the tail, yields

\[
\Pr\!\left(B_n>\left\lceil\frac{2n}{L}\right\rceil\right)
\le n\exp(-n/13)
\]

for sufficiently large \(n\) (the fixed constants are deliberately nonoptimal).

**4. Almost all possible image points are used.** Conditional on \(B_n=b\), the \(n-b\) outside images are independent and uniform on \(B\setminus\{c\}\). Let \(H_n\) be the number of points in this set that receive no preimage from outside \(B\). Then

\[
|\operatorname{im}f|=b-H_n,
\qquad
\mathbb E(H_n\mid B_n=b)
=(b-1)\left(1-\frac1{b-1}\right)^{n-b}
\]

for \(b>1\). Uniformly for \(b_1\le b\le\lceil2n/L\rceil\), the expectation is \(O(\sqrt n/L)\). Thus Markov's inequality gives

\[
\Pr\!\left(H_n\ge\frac{n\ell}{4L^2},\quad
b_1\le B_n\le\left\lceil\frac{2n}{L}\right\rceil\right)
=O\!\left(\frac{L}{\sqrt n\,\ell}\right).
\]

Outside the two negligible tails of step 3, this shows \(|\operatorname{im}f|=B_n-H_n>t_+\) with probability tending to one. By the exact containment criterion of step 1, such maps cannot lie in any maximum-cardinality commutative nilpotent subsemigroup. Summing the three error bounds proves the stated rate.

## Verification

A standalone standard-library checker `check.py` directly enumerates all labeled maps for sizes \(2\) through \(7\), tests whether their squares are constant, measures the distinguished preimage size and image rank, and compares direct counts with the Stirling formula. The entire direct search comprises \(873611\) transformations. The tested pairs \((|Q_n|,E_n)\) for \(n=5,6,7\) are, respectively, \((205,185)\), \((1176,1146)\), and \((7399,6517)\). The small sizes \(2,3,4\) check the arithmetic identity but are not used to invoke the extremal classification in the statement. The asymptotic step is analytic and is not inferred from these finite tests.

Reproduce with `python check.py`; the expected final line is recorded in `check_output.txt`.

## Relationship to prior work

Cameron, East, FitzGerald, Mitchell, Pebody and Quinn-Gregson describe null transformation semigroups by fibers and give their maximum size and extremal shape; Cain, Malheiro and Paulista prove that these are also precisely the maximum-size commutative nilpotent transformation semigroups. Their classification supplies the *known* structural input in step 1. It does not itself state the count of **individual** square-zero transformations contained in their union or the result that a uniform square-zero transformation asymptotically avoids that union. The independent novelty assessed here lies in the exact extension counting and its occupancy/saddle-point asymptotic, not in the known extremal classification or in the elementary definition of \(N(c,Y)\).

## Limitations

The theorem is asymptotic in the labeled set size and does not give the optimal asymptotic constant or a matching lower bound for the rare extension probability. The big-O estimate is deliberately coarse. It concerns maximum **cardinality** among commutative nilpotent subsemigroups, not inclusion-maximal semigroups, and counts transformations rather than isomorphism classes. Published or otherwise unindexed probabilistic analyses of rooted height-two mappings may imply a stronger result; originality is assessed only within the sources actually compared. Computational checks are finite corroboration, not an infinite proof. No independent validation is claimed.

## References

1. A. J. Cain, A. Malheiro, and T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481 (first publicly posted 2023-10-12), especially Theorem 3.12 and Section 2. https://arxiv.org/abs/2310.08481
2. P. J. Cameron, J. East, D. FitzGerald, J. D. Mitchell, L. Pebody, and T. Quinn-Gregson, *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups*, arXiv:2110.09701 (first publicly posted 2021-10-19), especially Section 4.1 and Theorem 4.4. https://arxiv.org/html/2110.09701v2
3. T. Paulista, *Characterizing the largest commutative (full and partial) transformation semigroups of certain types*, arXiv:2511.09495 (2025), related later extremal-classification work; full text not inspected. https://arxiv.org/abs/2511.09495
