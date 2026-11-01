# Exact Markov law, spectral decay, and entropy loss for skew-tent ordinal dynamics

## Finding

For **every** \(0<c<1\), the three-point ordinal-pattern process of the full-branch skew tent map, observed with one-step delay and initialized with invariant Lebesgue measure, is an **exactly first-order stationary Markov chain on five patterns**. Its transition matrix, its stationary distribution, all eigenvalues, and the entropy loss relative to the original chaotic dynamics have closed forms. In particular, putting \(s=1+c(1-c)\), its entropy rate is
\[
h_{\mathrm{ord}}(c)=\frac{H_{\mathrm b}(c)}s,
\qquad H_{\mathrm b}(c)=-c\log c-(1-c)\log(1-c).
\]
The dynamical entropy of the source is \(H_{\mathrm b}(c)\). Thus the exact fractional loss is \(c(1-c)/[1+c(1-c)]\), which is positive for every parameter and attains \(1/5\) at \(c=1/2\). In other words, the ordinal walk can be genuinely Markov while discarding a precisely quantifiable fraction of its source's entropy.

The symbolic topological support is independent of \(c\) and has entropy \(\log\rho\), where \(\rho\) is the unique root exceeding one of \(\rho^3-2\rho^2+\rho-1=0\). Its Markov transition operator has exact nontrivial spectral radius \(\max\{1-c,\sqrt{c(1-c)}\}\).

## Assumptions and scope

For \(0<c<1\) define \(T_c:[0,1]\to[0,1]\) by
\[
T_c(x)=\begin{cases}x/c&0\le x\le c,\\(1-x)/(1-c)&c<x\le1.\end{cases}
\]
The distribution of \(X_0\) is Lebesgue measure on \([0,1]\). It is invariant, because the two full inverse branches contract lengths by \(c\) and \(1-c\), whose sum is one. For each integer \(t\ge0\), let \(\omega_t\) be the permutation of \((0,1,2)\) listing the time indices in **increasing** order of the three real numbers \(T_c^t(X_0),T_c^{t+1}(X_0),T_c^{t+2}(X_0)\). Ties form a null set and are discarded. All logarithms are natural.

Write
\[
s=1+c(1-c),\qquad a=\frac c{2-c},\qquad b=\frac c{s},\qquad u=\frac1{2-c},\qquad v=\frac1s.
\]
Then \(0<a<b<c<u<v<1\). The only positive-measure ordinal patterns, in left-to-right order as the initial coordinate increases, are
\[
012:(0,a),\quad 021:(a,b),\quad 201:(b,u),\quad
102:(u,v),\quad 120:(v,1).
\]
Denote these five states by \(A,B,C,D,E\), respectively, and order all matrices this way. The exact transition matrix is
\[
P_c=\begin{pmatrix}
c&\frac{c(1-c)^2}{s}&\frac{1-c}{s}&0&0\\
0&0&0&1&0\\
0&0&0&(1-c)^2&c(2-c)\\
0&0&1&0&0\\
\frac{s}{2-c}&\frac{(1-c)^2}{2-c}&0&0&0
\end{pmatrix}.
\]
Its invariant row vector, given by the lengths of the five intervals, is
\[
\pi_c=\left(\frac c{2-c},\frac{c(1-c)^2}{(2-c)s},
\frac{1-c}{(2-c)s},\frac{(1-c)^2}{(2-c)s},\frac{c(1-c)}s\right).
\]
The matrix is primitive and the entire symbolic process (not merely its two-point marginal) has the law of this stationary Markov chain.

## Proof

**1. Ordinal atoms and full branches.** One has \(T_c(x)>x\) precisely for \(x\in(0,u)\). Also \(T_c^2(x)>T_c(x)\) exactly when \(T_c(x)<u\), apart from ties. The changes of sign of \(T_c^2(x)-x\) occur at the fixed/period-two points \(0,b,u,v\), with \(T_c(b)=v\) and \(T_c(v)=b\). Combining these comparisons yields exactly the five ordered intervals above. The critical point \(c\) lies inside the atom \(C\), but is not an ordinal boundary.

The complete graph of one-step atom transitions is
\[
A\to A,B,C;\qquad B\to D;\qquad C\to D,E;\qquad
D\to C;\qquad E\to A,B.
\]
For **every** permitted arrow \(i\to j\), the intersection of atom \(i\) with the inverse image of atom \(j\) consists of one affine inverse branch mapping onto the whole of atom \(j\), **except** the arrow \(C\to E\), which has two such full affine branches. This follows directly from \(T_c(A)=(0,u)\), \(T_c(B)=(u,v)\), \(T_c(D)=(b,u)\), and \(T_c(E)=(0,b)\), and from splitting \(C=(b,u)\) at its internal critical point \(c\): its left image is \((v,1)\), and its right image is \((u,1)\). Thus the right subbranch covers both \(D\) and \(E\), while the left subbranch covers \(E\).

**2. Exact Markov property.** An atom-word cylinder \((i_0,\ldots,i_n)\) splits into finitely many intervals, one for each composition of the above full affine inverse branches. Every such composition maps its interval bijectively onto the **entire** terminal atom \(i_n\) by an affine map. Lebesgue measure pushed forward from each cylinder component is therefore a constant multiple of Lebesgue measure on \(i_n\). Their sum is constant there. Consequently, conditional on **any** finite history of ordinal states ending at \(i_n\), the position \(X_n\) is uniform on atom \(i_n\). Its next-symbol distribution depends only on \(i_n\). This proves the full first-order Markov law for every history length. Computing relative inverse-branch lengths gives the displayed \(P_c\); the interval lengths give \(\pi_cP_c=\pi_c\).

**3. Entropy identity and its mechanism.** Consider refining each permitted arrow by its individual monotone inverse branch. If a source atom \(I_i\) has length \(\ell_i\), and a chosen inverse branch to destination atom \(I_j\) has constant expansion \(d\), the conditional probability of that individual branch is \(q=\ell_j/(d\ell_i)\). Averaging the branch-level Shannon uncertainty gives
\[
-\sum_i\pi_i\sum_{j,\mathrm{branch}}q\log q
=\sum_i\pi_i\log\ell_i-\sum_j\pi_j\log\ell_j
 +\int_0^1\log|T_c'(x)|\,dx
=H_{\mathrm b}(c).
\]
The first two sums cancel by stationarity. All arrows have one branch, except \(C\to E\), whose two branches have relative probabilities \(c\) and \(1-c\). The stationary probability of this arrow is
\[
\pi_C(P_c)_{CE}=\frac{1-c}{(2-c)s}\,c(2-c)=\frac{c(1-c)}s.
\]
Combining those two branches into one observable arrow removes exactly \([c(1-c)/s]H_{\mathrm b}(c)\) from the entropy. Therefore the Markov chain's entropy rate is exactly \(H_{\mathrm b}(c)/s\). The full-branch map's standard two-branch generating itinerary has metric entropy \(H_{\mathrm b}(c)\), yielding the asserted exact deficit. Its relative magnitude is maximized when \(c(1-c)\) is maximal, namely at \(c=1/2\).

**4. Exact mixing spectrum.** Direct expansion of the displayed matrix gives
\[
\det(zI-P_c)=z(z-1)(z+1-c)\bigl(z^2+c(1-c)\bigr).
\]
Thus the eigenvalues are \(1,0,-(1-c),\pm i\sqrt{c(1-c)}\). The transition graph is strongly connected and has the loop \(A\to A\); hence it is primitive. Its nonstationary spectral radius (and the exact exponential rate of operator convergence, in the spectral-radius sense) is
\[
 r(c)=\max\{1-c,\sqrt{c(1-c)}\}=
 \begin{cases}1-c&0<c\le 1/2,\\\sqrt{c(1-c)}&1/2\le c<1.\end{cases}
\]
No claim of uniform exponential convergence across the open parameter interval is made.

**5. Symbolic topological entropy.** The adjacency matrix is
\[
G=\begin{pmatrix}
1&1&1&0&0\\0&0&0&1&0\\0&0&0&1&1\\0&0&1&0&0\\1&1&0&0&0
\end{pmatrix}.
\]
Since every allowed arrow has at least one full inverse branch onto its destination, every finite directed path corresponds to a cylinder with positive Lebesgue measure. Conversely, every forbidden arrow has zero cylinder measure. Thus the closed symbolic support is exactly the one-sided shift of finite type presented by \(G\). A direct determinant expansion yields
\[
\det(zI-G)=z(z+1)(z^3-2z^2+z-1).
\]
Perron–Frobenius theory gives the claimed topological entropy \(\log\rho\), independent of \(c\), and graph primitivity gives mixing of the support shift.

## Verification

The standalone `verify_ordinal_skew.py` uses only the Python 3 standard library. Run `python3 verify_ordinal_skew.py` from a directory containing this package. For the seven **exact rational** parameters \(c=1/10,1/4,1/3,1/2,2/3,3/4,9/10\), it derives all two- and three-state cylinder measures directly by inverse-image interval arithmetic and checks them against \(\pi_iP_{ij}\) and \(\pi_iP_{ij}P_{jk}\), checks all length-at-most-four words against the adjacency graph, verifies stationarity and stochasticity, and evaluates characteristic polynomials through exact determinant calculations. It also evaluates the entropy formula numerically. All tests passed before final packaging. Finite tests do not establish the universal claims, which follow from the affine full-branch proof above.

For the symmetric parameter \(c=1/2\), the chain's entropy is \((4/5)\log2\) versus source entropy \(\log2\), and its nontrivial spectral radius is \(1/2\); the topological symbolic support has entropy \(\log\rho\approx0.5623\).

## Relationship to prior work

Bandt, Keller, and Pompe previously identified **five** three-point ordinal atoms for the symmetric full tent map and proved asymptotic entropy recovery as pattern length increases. The five-atom special case is therefore **not** claimed as new. Unakafov investigated ordinal conditional entropy for skew tent maps and the general possibility of non-Markov ordinal factors at some embedding orders. These works do not supply the displayed all-parameter exact three-point Markov matrix, mixing spectrum, and entropy-deficit identity. Potratzki, de Jong, Small, and Bröhl (2026) develop ordinal-transition-network Markov surrogates and spectral diagnostics; the present statement supplies a precise family in which the transition network is genuinely the entire symbolic law but its entropy still differs from the source entropy. The motivating article's complete main text was not accessible during final comparison, so full-document priority against it remains an explicit limitation, not a claim of verified noncoverage.

## Limitations

The theorem assumes Lebesgue-stationary full-branch skew tent maps, consecutive length-three ordinal windows, and no observation noise. The corresponding symbolic process at other window lengths or sampling delays need not be first-order Markov. Symbolic topological support includes limiting paths that may correspond only to tie points; the Markov distribution statements are almost-sure claims. The exact spectral rate is pointwise in \(c\), not uniform as \(c\to0\) or \(c\to1\). Historical priority remains provisional, especially for specialized ordinal-coding calculations not indexed or available in full text.

## References

1. M. Potratzki, T. G. de Jong, M. Small, and T. Bröhl, *Ordinal-pattern transition networks as a symbolic substrate for reservoir computing*, arXiv:2610.21973v1 (first submitted 2026-10-15), https://arxiv.org/abs/2610.21973.
2. C. Bandt, G. Keller, and B. Pompe, *Entropy of interval maps via permutations*, Nonlinearity **15** (2002), 1595–1602, https://doi.org/10.1088/0951-7715/15/5/312; accessible full-text transcription https://studylib.net/doc/7963413/entropy-of-interval-maps-via-permutations.
3. A. M. Unakafov, *Ordinal-patterns-based segmentation and discrimination of time series with applications to EEG data*, doctoral thesis (2015), especially Sections 2.3 and 3.3, https://www.zhb.uni-luebeck.de/epubs/ediss1524.pdf.
4. L. Alsedà, M. Misiurewicz, and R. A. Pérez, *Flexibility of entropies for piecewise expanding unimodal maps* (2020 preprint), arXiv:2004.01813, https://arxiv.org/abs/2004.01813.
