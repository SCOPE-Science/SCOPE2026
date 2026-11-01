# Line-centered furtherness persistence of finite projective subspace posets

## Finding

Let \(q\ge2\) be any prime power and \(n\ge2\). The finite subspace poset of \(\mathbb F_q^n\), centered at one projective point, has an explicitly determined furtherness barcode in every degree. Put
\[
B_q(r)=\sum_{i=0}^{r}{r\brack i}_q,
\]
where \({r\brack i}_q\) counts the \(i\)-dimensional subspaces of \(\mathbb F_q^r\). There is one essential ordinary degree-zero interval \([0,\infty)\). For every integer \(1\le k\le n-1\), there are precisely
\[
\beta_k=q^{k(k+1)/2}{n-1\brack k}_q
\]
finite intervals in degree \(k-1\), all with endpoints
\[
[B_q(k)-1,\ B_q(k+1)-2).
\]
There are no other nonzero-length bars. At every level, integral homology is torsion-free, and the entire integer-coefficient persistence module splits into free interval modules of these multiplicities. Consecutive bursts occupy successive degrees, with a one-unit gap between the death of one burst and the birth of the next.

## Assumptions and scope

Let \(V=\mathbb F_q^n\), \(P=\{T\le V: \dim T\ge1\}\) ordered by inclusion, and choose a one-dimensional subspace \(L\). Give \(P\) its lower-Alexandrov topology, with principal open downsets \(U_T=\{W\in P:W\le T\}\). Following the furtherness convention for finite spaces, put \(\Psi(L,T)=|U_T\setminus U_L|\). For any real \(t\), let \(P_t=\{T\in P:\Psi(L,T)\le t\}\) and \(K_t=\Delta(P_t)\) its simplicial order complex. A barcode interval means a half-open interval of this increasing filtration; zero-length simplicial reduction pairs are excluded. An interval in degree \(d\) refers to ordinary homology \(H_d\) and a single interval \([0,\infty)\) appears in degree zero. Negative thresholds give the empty complex.

The principal downset contains exactly \(B_q(\dim T)-1\) nonzero subspaces. Thus
\[
\Psi(L,T)=B_q(\dim T)-B_q(\dim(L\cap T))
=\begin{cases}B_q(r)-2,&\dim T=r,\ L\le T,\\B_q(r)-1,&\dim T=r,\ L\not\le T.\end{cases}
\]
The conventions are \(B_q(0)=1\) and \({a\brack b}_q=0\) outside \(0\le b\le a\). The theorem covers all prime powers, not only prime fields, and assumes no choice of coordinates for \(L\).

## Proof

**1. Threshold partition and monotonicity.** Since \(B_q(r+1)>B_q(r)+1\) for \(r\ge1\), the increasing filtration introduces rank-\(r\) subspaces containing \(L\) at \(B_q(r)-2\), followed by rank-\(r\) subspaces avoiding \(L\) at \(B_q(r)-1\). The only rank-one subspace of the first kind is \(L\), which enters at zero. The function is order-preserving because \(U_T\setminus U_L\subseteq U_{T'}\setminus U_L\) whenever \(T\subseteq T'\). Consequently the order complexes form a simplicial filtration.

**2. Rank-truncated birth stages.** For \(1\le k\le n-1\), exactly at \(b_k=B_q(k)-1\), all nonzero subspaces of rank at most \(k\) have entered, and none of larger rank has entered. Denote their order complex by \(K^{(k)}\). The lattice of all linear subspaces of \(V\) is a geometric lattice of rank \(n\), with an EL-shelling. The standard rank-selection theorem for EL-shellable posets shows that the proper bottom rank selection \(\{1,\ldots,k\}\), for \(k<n\), is pure and shellable. Hence \(K^{(k)}\) is homotopy equivalent to a wedge of \((k-1)\)-spheres (for \(k=1\), a discrete set of points). In particular all reduced integer homology vanishes outside degree \(k-1\), and is free in that degree.

The Möbius number of the interval below a rank-\(i\) subspace is \((-1)^i q^{i(i-1)/2}\). The reduced Euler characteristic of the rank-selected order complex is therefore
\[
\widetilde\chi(K^{(k)})=-\sum_{i=0}^k (-1)^i q^{i(i-1)/2}{n\brack i}_q.
\]
The partial Gaussian-binomial identity
\[
\sum_{i=0}^k(-1)^i q^{i(i-1)/2}{n\brack i}_q
=(-1)^k q^{k(k+1)/2}{n-1\brack k}_q
\]
follows by induction on \(k\) from \({n\brack k}_q={n-1\brack k-1}_q+q^k{n-1\brack k}_q\); the initial case is \(k=0\). Since all reduced homology is in degree \(k-1\), its rank is exactly \(\beta_k=q^{k(k+1)/2}{n-1\brack k}_q\).

**3. Contractible death stages.** At \(d_k=B_q(k+1)-2\) the poset consists exactly of all nonzero subspaces of rank at most \(k\), together with all rank-\(k+1\) subspaces containing \(L\). The map
\[
c(T)=T+L
\]
is an order-preserving closure operator on this poset: it is extensive and idempotent, and every image contains \(L\) and has rank at most \(k+1\). Its image is the subposet of subspaces containing \(L\), which has the least element \(L\). The standard closure-operator deformation retraction of order complexes makes \(K_{d_k}\) contractible. No further vertices enter until \(b_{k+1}=B_q(k+1)-1=d_k+1\), apart from the terminal case \(k=n-1\), where the whole poset already has the greatest element \(V\).

**4. Persistence maps and integral coefficients.** Between \(b_k\) and \(d_k\) the complex is literally constant. It has free reduced homology \(\mathbb Z^{\beta_k}\) concentrated in degree \(k-1\). At \(d_k\) the complex is contractible, so every such class dies then, and the next nontrivial burst is one level later and in a different degree. There are no hidden maps or extension ambiguities. In degree zero, \(K_0\) consists of the single vertex \(L\); \(K^{(1)}\) is the discrete set of all one-dimensional subspaces, and the inclusion of the original component is a primitive direct summand. At \(d_1\), those components merge into a contractible complex. Choosing one basepoint component and the differences between it and the other components yields one free interval \([0,\infty)\) and \(\beta_1\) free intervals \([b_1,d_1)\). Thus the entire integral persistence module splits as stated, and base change to any field gives the same barcode.

## Verification

The standalone `verify.py` exhaustively generates all subspaces by span closure over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), builds every nonempty chain of the nonzero subspace poset, assigns its exact furtherness filtration weight, and performs full signed simplicial persistent boundary reduction independently modulo the primes \(2\), \(3\), and \(5\). It also checks Gaussian subspace counts, order monotonicity, essential intervals, and all positive-length barcode pairs. The following five complete cases and fifteen independent finite-field boundary reductions pass:

\[
(q,n)\in\{(2,2),(2,3),(2,4),(3,2),(3,3)\}.
\]
For instance, the \((q,n)=(2,4)\) case has \(66\) nonzero subspaces and \(1391\) nonempty chains, with finite bars \(14\) times \([1,3)\) in degree zero, \(56\) times \([4,14)\) in degree one, and \(64\) times \([15,65)\) in degree two. This computation confirms examples only; the all-prime-power theorem is proved by the shellability, Möbius-identity, and closure-operator arguments above.

Reproduce with `python verify.py` using a standard Python 3 installation; no additional modules or data files are required.

## Relationship to prior work

Badra and Singh introduced furtherness for finite spaces and subsequently considered the associated persistence diagrams, focusing their explicit classification on degree zero (arXiv:2603.18580 and arXiv:2610.16386). The furtherness function and poset-filtration construction here are taken from that work, not claimed as new. Classical geometric-lattice EL-shellability and Möbius numbers supply the rank-truncation input. Hersh and Sundaram (arXiv:2604.06479) construct general rank-selected homology bases for geometric lattices, which does not by itself specify these centered furtherness entry times or inter-rank death maps.

Related work on ordinary rank-filtered order complexes includes Kitajima (arXiv:2606.15241), which concerns rank-defined filtrations and shellability. Its accessible abstract does not state this furtherness barcode, but its full text was unavailable for a decisive comparison. A previously reported result for the Boolean subset lattice gives analogous formulas in a distributive lattice; the non-distributive projective subspace lattice requires the geometric-lattice shellability and the explicit closure map, and its Gaussian multiplicities and subspace-count thresholds are different. A literature search does not prove uniqueness; equivalent formulations may exist.

## Limitations

The center is a one-dimensional subspace, not a higher-dimensional center. The filtration is lower-Alexandrov furtherness with respect to one fixed center, not an arbitrary rank filtration or a metric Rips filtration. The theorem determines ordinary homology persistence and its integral splitting, not equivariant representations, higher operations, or general flag varieties. Finite verification covers only listed prime-field examples. Publication originality remains subject to external independent review; no independent validation is claimed.

## References

1. A. Badra and H. K. Singh, *Furtherness in finite topological spaces*, arXiv:2603.18580v1, 19 March 2026; especially Corollary 2.17.
2. A. Badra and H. K. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1, 12 October 2026; especially Sections 3–4.
3. P. Hersh and S. Sundaram, *Stability and ribbon bases for the rank-selected homology of geometric lattices*, arXiv:2604.06479v1, 7 April 2026; background on geometric-lattice EL-shellings and rank-selected homology.
4. Y. Kitajima, *Filtered order complexes and magnitude homology of finite graded posets*, arXiv:2606.15241v1, 13 June 2026; abstract-based comparison, full text not inspected.
5. A. Björner, *Shellable and Cohen–Macaulay partially ordered sets*, Transactions of the American Mathematical Society 260 (1980), 159–183; standard shellability background.
