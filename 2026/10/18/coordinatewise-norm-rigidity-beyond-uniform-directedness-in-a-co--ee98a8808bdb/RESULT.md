# Coordinatewise norm rigidity beyond uniform directedness in a combinatorial Banach space

## Finding
There exists an explicit covering family \(\mathcal F\) of finite subsets of the positive integers whose associated real sequence space \(\mathrm{FIN}(\mathcal F)\) has all the following properties:

1. **Coordinatewise norm rigidity:** for every sequence \((x^{(m)})\) in \(\mathrm{FIN}(\mathcal F)\) and every \(x\in\mathrm{FIN}(\mathcal F)\), coordinatewise convergence \(x^{(m)}\to x\) and convergence \(\|x^{(m)}\|_{\mathcal F}\to\|x\|_{\mathcal F}\) together imply \(\|x^{(m)}-x\|_{\mathcal F}\to0\). Consequently \(\mathrm{FIN}(\mathcal F)=\mathrm{EXH}(\mathcal F)\), and every bounded equinormed subset of \(\mathrm{FIN}(\mathcal F)\) is relatively norm compact.
2. **Separation from uniform directedness:** in the directedness classes of Gulgowski--Sawicki, \(\mathcal F\) belongs to no \((\lambda,\gamma)\)-class for any \(0\le\lambda<1/2\) and \(\gamma>0\). Thus its compactness property lies strictly outside the hypotheses of the positive-uniform-directedness criteria in that work.
3. **Non-classical geometry:** the completion \(X_{\mathcal F}\) contains a \(1\)-complemented isometric copy of \(\ell_\infty^N\) for every positive integer \(N\). In particular it is not isomorphic to \(\ell_1\).

These assertions concern the particular explicit family below. No characterization of arbitrary generating families and no resolution of the remaining directedness problem for families admitting classes arbitrarily close to \((0,0)\) is asserted.

## Assumptions and scope
Partition \(\mathbb N=\bigsqcup_{j\ge1}I_j\) into successive, pairwise disjoint finite intervals with \(|I_j|=2^j\). A nonempty finite set \(F\subset\mathbb N\) belongs to \(\mathcal F\) if its occupied block indices are \(i_0<i_1<\cdots<i_s\), with
\[
i_{t+1}\ge2i_t\quad(0\le t<s),\qquad
|F\cap I_{i_t}|\le2^{i_t-i_0}\quad(1\le t\le s).
\]
There is no restriction on the nonempty principal block \(F\cap I_{i_0}\) beyond containment in \(I_{i_0}\). Every singleton belongs to \(\mathcal F\), so this is a covering family. The family need not itself be hereditary; this is permitted in the generating-family definition.

For a real sequence \(x=(x_n)\), set
\[
\|x\|_{\mathcal F}=\sup_{F\in\mathcal F}\sum_{n\in F}|x_n|,
\quad\mathrm{FIN}(\mathcal F)=\{x:\|x\|_{\mathcal F}<\infty\},
\quad\mathrm{EXH}(\mathcal F)=\{x\in\mathrm{FIN}(\mathcal F):\|x\mathbf1_{(N,\infty)}\|_{\mathcal F}\to0\}.
\]
A set \(A\subseteq\mathrm{FIN}(\mathcal F)\) is *equinormed* if, for each \(\varepsilon>0\), some finite subfamily \(\mathcal B\subset\mathcal F\) satisfies
\[
\|a\|_{\mathcal F}-\max_{F\in\mathcal B}\sum_{n\in F}|a_n|<\varepsilon\qquad\text{for every }a\in A.
\]
The directedness \((\lambda,\gamma)\)-classes are precisely those of Definition 7 in Gulgowski--Sawicki [1], using their finite-set weighted-covering families and simultaneous-extension quantifiers.

## Proof
**1. Local tail capture.** Suppose \(D\in\mathcal F\) has principal block index \(i\) and largest occupied block index \(h\). Choose the cutoff \(N\) beyond the end of \(I_{2h}\). For any \(F\in\mathcal F\) put \(B=F\cap(N,\infty)\). The occupied blocks of \(B\) are still separated successively by a factor at least two and all are past the last occupied block of \(D\) by more than a factor two. For every choice of nonnegative weights \((w_n)_{n\in B}\), select in each occupied block \(I_j\) of \(B\) the \(\min\{|B\cap I_j|,2^{j-i}\}\) largest-weight indices. Their union \(E\subseteq B\) has
\[
\sum_{n\in E}w_n\ge2^{-i}\sum_{n\in B}w_n,
\]
because \(|I_j|=2^j\), and the average of the largest \(k\) entries is no smaller than the full-block average. The union \(D\cup E\) is in \(\mathcal F\), with principal index \(i\). Therefore, for any \(y\in\mathrm{FIN}(\mathcal F)\),
\[
\boxed{\ \|y\mathbf1_{(N,\infty)}\|_{\mathcal F}
\le 2^i\left(\|y\|_{\mathcal F}-\sum_{n\in D}|y_n|\right).\ }
\tag{1}
\]
The cutoff may depend on \(D\), and its capture constant \(2^{-i}\) is deliberately nonuniform in the principal index.

**2. Existence of an anchor that norms each sequence.** For \(x\in\mathrm{FIN}(\mathcal F)\), put \(b_j(x)=\sum_{n\in I_j}|x_n|\), and let \(K_i(x)\) be the supremum of the defining sums over those \(F\in\mathcal F\) whose principal block index is exactly \(i\). Necessarily \(b_j(x)\to0\): otherwise some \(\delta>0\) and infinitely many blocks satisfy \(b_j(x)\ge\delta\). Choose a subsequence of these indices with successive indices at least double. A set with principal block index \(1\) can simultaneously take the largest half of each of its first \(m\) selected blocks, obtaining a norm contribution at least \(m\delta/2\), contradicting finiteness of \(\|x\|_{\mathcal F}\).

For \(i\ge2\), removing the principal block of any \(F\in\mathcal F\) with anchor \(i\) leaves a succession of secondary blocks that can be included, unchanged, in a member with principal index \(1\). Indeed their first index is at least \(2i\), and the quota \(2^{j-i}\) is no larger than \(2^{j-1}\). Hence
\[
\boxed{\ K_i(x)\le b_i(x)+K_1(x)\quad(i\ge2).\ }
\tag{2}
\]
Since \(b_i(x)\to0\), \(\limsup_{i\to\infty}K_i(x)\le K_1(x)\). As \(\|x\|_{\mathcal F}=\sup_{i\ge1}K_i(x)\), there is a **single finite index** \(i(x)\) for which \(K_{i(x)}(x)=\|x\|_{\mathcal F}\). This does not require attainment by one finite set: for every \(\delta>0\), some \(D\in\mathcal F\) anchored at the same \(i(x)\) has \(\sum_{n\in D}|x_n|>\|x\|_{\mathcal F}-\delta\).

**3. Coordinatewise norm rigidity.** Let \(x^{(m)}\to x\) coordinatewise with \(\|x^{(m)}\|_{\mathcal F}\to\|x\|_{\mathcal F}\). If \(x=0\), the assertion is immediate. Otherwise fix the index \(i=i(x)\) from Step 2. Given arbitrary \(\delta>0\), choose \(D\) with this anchor and deficit less than \(\delta\). For large \(m\), coordinatewise convergence on the finite set \(D\) and norm convergence give
\[
\|x^{(m)}\|_{\mathcal F}-\sum_{n\in D}|x^{(m)}_n|<2\delta.
\]
For the cutoff from Step 1, inequality (1) bounds the respective tails of \(x^{(m)}\) and \(x\) by \(2^{i+1}\delta\) and \(2^i\delta\). The finite-coordinate difference tends to zero, so
\[
\limsup_{m\to\infty}\|x^{(m)}-x\|_{\mathcal F}\le3\cdot2^i\delta.
\]
Since \(\delta\) was arbitrary, the claimed norm convergence follows.

**4. Consequences for compactness.** For any \(x\in\mathrm{FIN}(\mathcal F)\), coordinate truncations converge to \(x\) coordinatewise and their norms increase to \(\|x\|_{\mathcal F}\) (each admissible set is finite). Step 3 gives convergence in norm, proving \(\mathrm{FIN}(\mathcal F)=\mathrm{EXH}(\mathcal F)\). Now let \(A\) be bounded and equinormed. Every sequence in \(A\) has a coordinatewise convergent subsequence (diagonal extraction), with limit \(x\in\mathrm{FIN}(\mathcal F)\) by lower semicontinuity of the norm. For any \(\varepsilon>0\), finite equinorming seminorms on \(A\) and their coordinatewise limits imply \(\limsup\|x^{(m)}\|_{\mathcal F}\le\|x\|_{\mathcal F}+\varepsilon\); lower semicontinuity gives the reverse inequality. Thus the norms converge, and Step 3 makes the subsequence norm convergent. Sequential total boundedness in this Banach space proves relative compactness.

**5. Strict failure of uniform directedness.** Fix arbitrary \(0\le\lambda<1/2\) and \(\gamma>0\), and choose \(i\) with \(2^{-i}<\gamma\). Take \(D=I_i\). If the \((\lambda,\gamma)\)-condition held, its quantifiers would give a cutoff \(N\); take \(j\) so large that \(I_j\) lies past \(N\) and \(j\ge2i\), and let \(B=I_j\). Apply the two weighted-covering requirements to weights identically \(1\) on each block. One obtains subsets \(D'\subseteq D\) and \(B'\subseteq B\) that should admit a simultaneous extension \(C\in\mathcal F\), with
\[
|D'|\ge(1-\lambda)2^i>2^{i-1},\qquad |B'|\ge\gamma2^j>2^{j-i}.
\]
A member of \(\mathcal F\) containing more than half of \(I_i\) must have principal index exactly \(i\): any earlier anchor permits at most \(2^{i-h}\le2^{i-1}\) points of \(I_i\), and any later anchor permits none. But with principal index \(i\), that member contains at most \(2^{j-i}\) points of \(I_j\), contradicting the requirement for \(B'\). Consequently \(\mathcal F\) belongs to no such \((\lambda,\gamma)\)-class.

**6. Uniformly complemented finite-dimensional \(\ell_\infty\).** For each \(N\ge1\), let \(u_j=2^{-j}\mathbf1_{I_j}\), for \(N\le j<2N\). An admissible set meets at most one of those blocks, because occupied indices must double. Therefore
\[
\left\|\sum_{j=N}^{2N-1}a_j u_j\right\|_{\mathcal F}=\max_{N\le j<2N}|a_j|.
\]
The projection
\[
P_Nx=\sum_{j=N}^{2N-1}\left(\sum_{n\in I_j}x_n\right)u_j
\]
has norm exactly \(1\), because \(\left|\sum_{n\in I_j}x_n\right|\le\|x\|_{\mathcal F}\), and it fixes every \(u_j\). Thus \(X_{\mathcal F}\) contains \(1\)-complemented isometric \(\ell_\infty^N\) for arbitrarily large \(N\). The classical uniform cotype-two bound for \(\ell_1\), whereas the cotype-two constants of \(\ell_\infty^N\) grow at least as \(\sqrt N\), rules out an isomorphism \(X_{\mathcal F}\cong\ell_1\).

## Verification
A standalone finite checker, `verify_local_capture.py`, is included. Run `python verify_local_capture.py` without third-party packages. It checks explicit admissibility, the weight-capture inequality for independently sampled finite admissible block sets, the strict fractional-quota obstruction for representative parameters, the exact block-window geometry, and the anchoring inequality (2) for finite blocks by a dynamic program. Its expected successful output begins `LOCAL_CAPTURE_LACUNARY_BLOCK_FINITE_CHECKS_OK`. This is a finite sanity check only: all quantified and infinite-dimensional assertions are established by the proof above.

## Relationship to prior work
Gulgowski and Sawicki [1], Section 6, prove that uniform directedness \((0,c)\), or a sequence of positive \((\lambda,c')\)-conditions approaching a positive \(c\), suffices for equinormed compactness. Their Example 4 shows a non-\(\ell_1\)-equivalent norm under such a *uniform* positive fraction. Their Theorem 14 supplies a noncompactness obstruction, and their stated remaining question concerns classes approaching \((0,0)\). The present family has the same equinormed-compactness conclusion but fails **every** positive-fraction class with \(\lambda<1/2\); its stronger coordinatewise norm-rigidity and complemented block geometry separate the mechanisms. It does **not** settle the stated remaining question for families that actually belong to positive classes arbitrarily close to \((0,0)\). Borodulin-Nadzieja, Farkas, Jachimek and Pelczar-Barwacz [2] develop the general theory and related combinatorial examples; no identical weighted-lacunary rigidity statement was identified in the inspected material.

## Limitations
The family is an explicit nonhereditary generating presentation, not a classification of all covering families. The failure of uniform directedness is proved only for the range \(0\le\lambda<1/2\), which suffices to separate all families of positive classes approaching \((0,0)\). The argument establishes sequential coordinatewise norm rigidity, not a corresponding assertion for arbitrary nonmetrizable nets. The finite checker does not establish infinite assertions. Related work may contain unrecognized equivalent formulations of the example, so independent bibliographic and mathematical review remains worthwhile.

## References
[1] J. Gulgowski and P. Sawicki, *Compactness in Combinatorial Banach Spaces and Beyond*, arXiv:2610.09810v1 (first public posting 2026-10-07), especially Section 6, Theorems 12--14 and Examples 3--4. https://arxiv.org/html/2610.09810v1

[2] P. Borodulin-Nadzieja, B. Farkas, S. Jachimek and A. Pelczar-Barwacz, *The ZOO of combinatorial Banach spaces*, arXiv:2404.01733v1 (2024); Studia Mathematica 282 (2025), 101--132. https://arxiv.org/html/2404.01733v1
