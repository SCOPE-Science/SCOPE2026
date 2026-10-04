# Sharp nested all-cardinality profile for Bourgain \(\Lambda(p)\) selection
## Finding
For a finite bounded orthogonal system \(\Phi=(\phi_j)_{j=1}^N\), define
\[
K_p(S;\Phi)=\sup_{a
e0}
rac{\|\sum_{j\in S}a_j\phi_j\|_{L^p}}
{(\sum_{j\in S}|a_j|^2)^{1/2}}.
\]
For every \(p>2\) and \(A>0\), there is a constant \(C_{p,A}\) such that a uniformly random permutation \(\pi\) of \(\{1,\ldots,N\}\) has, with probability at least \(1-N^{-A}\), the simultaneous nested estimate
\[
K_p(S_m;\Phi)\le C_{p,A}\max\{1,\sqrt m\,N^{-1/p}\}
\qquad (1\le m\le N),
\]
where \(S_m=\{\pi(1),\ldots,\pi(m)\}\).

The order is sharp at every cardinality. For the trigonometric system \(\phi_j(x)=e^{2\pi i jx}\) on \(\mathbb T\), every \(m\)-element subset \(S\subset\{1,\ldots,N\}\) satisfies
\[
K_p(S;\Phi)\ge c_p\max\{1,\sqrt m\,N^{-1/p}\},
\qquad
c_p=(\sqrt3/2)6^{-1/p}.
\]
Thus the recent critical-cardinality theorem at \(msymp N^{2/p}\) is the transition point of a sharp all-cardinality profile, and one random ordering realizes the correct scale for all nested prefixes simultaneously.

## Assumptions and scope
The probability space has total measure one. The functions are pairwise orthogonal in \(L^2\) and satisfy \(\|\phi_j\|_\infty\le1\); no normalization from below is assumed. The constants depend only on the displayed parameters, not on \(N\), \(m\), or the system. The probabilistic conclusion concerns one uniformly random permutation and all of its prefixes simultaneously.

The proof uses as input the finite Bourgain selection theorem in the form proved by Burstein, Iosevich and Krause: for every exponent \(B>0\), an \(R\)-term bounded orthogonal system has a uniformly random subset of cardinality \(\lceil R^{2/p}ceil\) whose \(K_p\) is bounded by a constant depending only on \(p,B\), with failure probability at most \(R^{-B}\).

## Proof
Put \(eta=2/p\) and \(lpha=1-eta\).

First construct a uniform random permutation in blocks. From a residual set of \(R\) indices, choose uniformly a block of size
\[
b(R)=\lceil R^etaceil,
\]
order that block uniformly, and continue recursively on the complement. Induction on \(R\) shows that the resulting full ordering is a uniform random permutation: for any prescribed ordering, the first block has probability \(inom{R}{b(R)}^{-1}b(R)!^{-1}\), and the residual ordering has probability \((R-b(R))!^{-1}\), whose product is \(R!^{-1}\).

Call a block good when its \(K_p\) is at most the constant from the recent selection theorem with a failure exponent \(B\) to be chosen. Conditional on the preceding blocks, each new block is a uniformly random critical-size subset of the residual bounded orthogonal system. Hence its conditional failure probability is at most \(R^{-B}\). Every subset of a good block is also good with the same constant.

Consider first a prefix of size \(m\le N/2\). Before that prefix is completed, every residual size satisfies \(R\ge N-m\ge N/2\). If \(T_m\) blocks meet the prefix, then all but possibly the last contribute at least \((N/2)^eta\) indices, so
\[
T_m\le 1+2^eta mN^{-eta}.
\]
Writing the corresponding polynomial as a sum of its block pieces \(f_t\), Minkowski and Cauchy--Schwarz give, whenever all these blocks are good,
\[
\Big\|\sum_t f_t\Big\|_p
\le C_{p,B}\sum_t\|a^{(t)}\|_2
\le C_{p,B}\sqrt{T_m}\,\|a\|_2.
\]
Therefore
\[
K_p(S_m;\Phi)
\le C'_{p,B}\max\{1,\sqrt m\,N^{-1/p}\}
\qquad (m\le N/2).
\]

Only \(O_p(N^lpha)\) blocks can appear before the halfway point. Indeed, the preceding estimate with \(m=N/2\) already gives that count. Since every corresponding residual size is at least \(N/2\), a union bound makes the probability that any such block is bad at most
\[
O_p(N^lpha)(N/2)^{-B}.
\]
Choose \(B>A+lpha+2\). For all sufficiently large \(N\) this is at most \(N^{-A}\). The finitely many remaining \(N\) are absorbed by enlarging \(C_{p,A}\), using the deterministic interpolation bound below. Thus, with probability at least \(1-N^{-A}\), the desired estimate holds simultaneously for every prefix through \(N/2\).

For later prefixes use the deterministic estimate valid for every \(r\)-element set \(T\):
\[
K_p(T;\Phi)\le r^{lpha/2}.
\]
To see this, orthogonality and \(\|\phi_j\|_2\le1\) give \(\|\sum a_j\phi_j\|_2\le\|a\|_2\), while pointwise Cauchy--Schwarz gives \(\|\sum a_j\phi_j\|_\infty\le\sqrt r\,\|a\|_2\); interpolation yields the displayed bound. If \(m>N/2\), decompose the prefix into its first \(k=\lfloor N/2floor\) terms and the remaining tail. The first part has the already proved bound, and the tail has \(K_p\le N^{lpha/2}\). Since
\[
\sqrt m\,N^{-1/p}\ge 2^{-1/2}N^{lpha/2}
\]
for \(m>N/2\), another application of Cauchy--Schwarz to the two coefficient blocks yields the required estimate for every later prefix simultaneously.

For sharpness take \(\phi_j(x)=e^{2\pi i jx}\) and any \(m\)-element \(S\subset\{1,\ldots,N\}\). With all coefficients equal to one, on
\[
|x|\lerac1{12N}
\]
every phase has real part at least \(\cos(\pi/6)=\sqrt3/2\), so
\[
\left|\sum_{j\in S}e^{2\pi i jx}ight|
\gerac{\sqrt3}2m.
\]
The interval has normalized measure \(1/(6N)\). Hence
\[
K_p(S;\Phi)\ge
rac{\sqrt3}2\,6^{-1/p}\sqrt m\,N^{-1/p}.
\]
Taking a single nonzero coefficient also gives \(K_p(S;\Phi)\ge1\). Since the displayed \(c_p\) is less than one, the two bounds combine into the stated lower estimate.

## Verification
The argument is symbolic. The critical inputs were checked in the full text of arXiv:2609.12566v1: the fixed-cardinality theorem has cardinality \(\lceil R^{2/p}ceil\), an arbitrary polynomial failure exponent, and a constant independent of \(R\); its Fourier specialization explicitly records worst-case sharpness of the critical exponent.

The block construction was checked at the quantifier level: conditional uniformity is preserved after every previously exposed block, partial final blocks inherit a \(K_p\) bound, and the single good-block event through the halfway point controls all prefix cardinalities at once. The lower bound uses an interval on which every one of the \(N\) possible Fourier phases lies in the same \(\pi/3\)-wide sector; it therefore applies to every subset, not merely to consecutive frequencies.

No finite computation is used as evidence for the infinite statement.

## Relationship to prior work
Bourgain's 1989 theorem proves the existence of a bounded-\(K_p\) subsystem at the critical cardinality \(N^{2/p}\), and identifies that exponent as optimal. The 2026 proof of Burstein, Iosevich and Krause strengthens the critical-cardinality statement to a uniformly random subset with arbitrary polynomial failure probability. Its Corollary 4.1 again states one critical cardinality and notes the standard near-origin Fourier obstruction.

The present statement is not a rephrasing of the critical theorem: it gives a single nested family, generated by one uniform random permutation, with the sharp order of \(K_p\) simultaneously at every exact cardinality \(1\le m\le N\). The proof combines repeated critical selections with a block-count law and the deterministic large-prefix interpolation regime. Searches for an all-cardinality or nested-prefix formulation did not locate an equivalent statement in the inspected literature or in the compared research database.

## Limitations
The constants are not optimized. The result gives the correct order in \(N\) and \(m\), not a sharp numerical value of \(C_{p,A}\). The lower construction proves worst-case sharpness of the scale but does not determine the exact failure probability for random prefixes of the Fourier system. The argument depends on the bounded-orthogonal critical selection theorem; it does not by itself extend to weaker \(L^r\) normalization without replacing the block scale by the corresponding \(L^r\) exponent.

A residual literature risk remains that the nested all-cardinality corollary has appeared under different terminology, especially in work on proportional restrictions of bounded orthogonal systems. The inspected primary and modern sources state the critical-size theorem rather than this simultaneous prefix profile.

## References
1. W. Burstein, A. Iosevich, B. Krause, *Bourgain's \(\Lambda(p)\) selection theorem: a greedy proof with polynomial failure bounds*, arXiv:2609.12566v1, 2026.
2. J. Bourgain, *Bounded orthogonal systems and the \(\Lambda(p)\)-set problem*, Acta Mathematica 162 (1989), 227--245, DOI 10.1007/BF02392838.
3. H. Jung, B. Langowski, A. Ortiz, T. Vu, *Expository article: “Bounded orthogonal systems and the \(\Lambda(p)\)-set problem” by Jean Bourgain*, Expositiones Mathematicae 43 (2025), article 125691.
