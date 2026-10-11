# Exact adversarial-erasure spectra for two-character cyclic harmonic frames

## Finding
For every integer \(N\ge3\), every pair of distinct residues \(a,b\in\mathbb Z_N\), and every erasure size \(0\le r\le N\), consider the unit-norm cyclic harmonic frame
\[
\varphi_k=2^{-1/2}\bigl(\exp(2\pi iak/N),\exp(2\pi ibk/N)\bigr),\quad k\in\mathbb Z_N.
\]
Set \(g=\gcd(N,b-a)\), \(m=N/g\), \(r=qg+s\) with \(0\le s<g\), and \(\zeta_m=\exp(2\pi i/m)\). Define
\[
M_{N,g}(r)=\left|g\sum_{j=0}^{q-1}\zeta_m^j+s\zeta_m^q\right|.
\]
For every set \(E\subset\mathbb Z_N\) of \(r\) erased coefficient indices, the retained frame operator satisfies the **simultaneously sharp** universal bounds
\[
\boxed{\frac{N-r-M_{N,g}(r)}2 I\ \preceq\ \sum_{k\notin E}\varphi_k\varphi_k^*\ \preceq\ \frac{N-r+M_{N,g}(r)}2 I.}
\]
Both endpoint eigenvalues occur for the *same* erasure masks. Precisely, these masks fill all \(g\) indices in each of \(q\) consecutive phase classes around the quotient circle of order \(m\), and, when \(s>0\), select exactly \(s\) indices from one adjacent phase class. These and only these masks attain the two extreme universal spectral bounds.

The number \(C_{N,g}(r)\) of worst erasure subsets is \(1\) for \(r=0,N\). For \(0<r<N\) it is
\[
\boxed{C_{N,g}(r)=
\begin{cases}
m,&s=0,\\
m\binom gs,&s>0\ \text{and }q\in\{0,m-1\},\\
2m\binom gs,&s>0\ \text{and }1\le q\le m-2.
\end{cases}}
\]
The frame-survival threshold \(r\le N-g-1\) is also a consequence of the existing projective-orbit zero-proportion theorem; it is recorded here only as an interpretation of the new quantitative formula, not as a separate new theorem. In the projectively faithful case \(g=1\), the formula reduces to
\[
M_{N,1}(r)=\frac{\sin(\pi r/N)}{\sin(\pi/N)}
\]
and there are exactly \(N\) worst masks at each nontrivial size.

## Assumptions and scope
The two row frequencies are distinct modulo \(N\). The vectors are normalized to unit Euclidean norm. An erasure removes a *labelled coefficient index*; thus identical projective rays remain distinct available measurements, and combinatorial multiplicities matter. The phase map is \(k\mapsto ((b-a)/g)k\pmod m\), which has exactly \(g\) preimages over each phase class. “Consecutive” means cyclically consecutive values of this phase map, not necessarily consecutive original indices.

The symbol \(\preceq\) denotes Loewner order. The bounds concern the retained analysis operator and its eigenvalues, not an optimization over arbitrary dual-frame reconstruction operators. No claim is made for three or more Fourier rows or for nonuniform sampling weights.

## Proof
**1. Spectral reduction.** Orthogonality of the distinct Fourier characters gives
\[\sum_{k\in\mathbb Z_N}\varphi_k\varphi_k^*=\tfrac N2I.\]
For any erasure set \(E\) of size \(r\), put \(z_E=\sum_{k\in E}\exp(2\pi i(b-a)k/N)\). The retained operator has both diagonal entries \((N-r)/2\) and conjugate off-diagonal entries \(-z_E/2\) and \(-\overline z_E/2\). Its two eigenvalues are therefore
\[\lambda_\pm(E)=\tfrac12(N-r\pm|z_E|).\]
Consequently, the entire problem is to maximize \(|z_E|\) over all \(r\)-element sets \(E\), including multiplicity counts and equality cases.

**2. Capacity-constrained circular rearrangement.** The homomorphism \(k\mapsto ((b-a)/g)k\pmod m\) sends the \(N\) labels onto the \(m\) phase classes, each with capacity \(g\). Hence \(z_E=\sum_{j=0}^{m-1}c_j\zeta_m^j\) for integers \(0\le c_j\le g\) and \(\sum_j c_j=r\). Conversely every such vector of counts is realizable.

For \(0<r<N\), a maximizing vector has nonzero sum (selecting consecutive available phases provides a nonzero sum). Rotate the complex plane so that its sum is positive real. If a selected copy has smaller real projection than an unselected copy, exchanging them strictly increases the projected sum, and hence its modulus, contradicting maximality. Therefore, for this direction, one must first fill capacity at the phases with largest cosines. On a regular \(m\)-gon, these phases form a consecutive cyclic arc: \(q\) full classes and at most one class with \(s\) selected indices.

There can be a tie between the two boundary phases. If a positive number of labels is assigned to each while both can be adjusted, moving an integer amount from one boundary class to the other makes the complex sum affine in that amount with nonzero slope. Its squared modulus is a strictly convex quadratic. An interior split therefore cannot be globally maximal. At an endpoint the configuration again has \(q\) full consecutive classes and, if needed, a single partially occupied adjacent class. All such arcs are related by a rotation and possibly reflection; they have the same modulus. Thus every maximizer, and only a maximizer, has exactly the claimed arc form, and the maximum is \(M_{N,g}(r)\). The cases \(r=0,N\) have zero phase sum directly.

**3. Equality-mask census.** For \(0<r<N\), when \(s=0\) there are \(m\) full consecutive arcs. When \(s>0\), a partial class may lie on either side of a nonempty proper full arc. If \(1\le q\le m-2\) these give \(2m\) distinct phase-count patterns. When \(q=0\) or \(q=m-1\) the two descriptions coincide and there are \(m\) patterns. In each partially selected phase class one may choose any \(s\) of its \(g\) labelled indices. This proves the formula for \(C_{N,g}(r)\).

**4. Exact stability threshold.** The retained frame has rank one exactly when all its nonzero vectors lie on one projective ray. No such ray occurs more than \(g\) times. Thus every remaining set spans \(\mathbb C^2\) precisely when \(N-r\ge g+1\), equivalently \(r\le N-g-1\). At and beyond the threshold there are retained sets of at most \(g\) copies of one ray. This also proves the strict or zero lower bound at every boundary.

**5. Closed evaluation.** Put \(D_q=\sin(\pi q/m)/\sin(\pi/m)\). The geometric-sum identity gives
\[
M_{N,g}(r)^2=g^2D_q^2+s^2+2gsD_q\cos\!\left(\frac{(q+1)\pi}{m}\right).
\]
For \(g=1\), \(s=0\) and \(q=r\), yielding the displayed sine formula. These identities cover every integer parameter in the stated domain.

## Verification
Running `python3 verify.py` with Python 3 and the standard library exhaustively enumerates every labelled erasure mask for every \(3\le N\le12\), every distinct row-frequency difference, and every erasure count. The replay checks \(635\) parameter triples and \(81{,}920\) labelled masks, including all equality-mask counts. It independently enumerates \(246\) capacity-vector parameter triples and compares their maxima and optimizer counts. The maximum numerical discrepancy was below \(2.2\times10^{-14}\); the checker reports `VERIFY_OK`. This finite replay corroborates the exact all-dimensional proof above; it is not used to extrapolate from finite cases.

As a nontrivial composite example, \(N=12\), \(b-a=4\), and \(r=6\) give \(g=4\), \(m=3\), \(q=1\), \(s=2\), \(M_{12,4}(6)=2\sqrt3\). The sharp retained lower bound is \(3-\sqrt3\), and precisely \(36\) of the \(924\) labelled erasure masks realize it.

## Relationship to prior work
Marshall and Waldron (2016 preprint) define cyclic harmonic frames via Fourier-character rows and investigate their counting and equivalence classes. Their Fourier description supplies the natural model here, but their enumerative results do not determine retained spectral bounds for every erasure count. Bodmann and Paulsen study general erasure error bounds for two-uniform frames, whereas nontrivial two-row cyclic frames need not be two-uniform; their framework gives neither the cyclic arithmetic \(\gcd\) profile nor the exact worst-mask census. Cheng, Lv, and Sun characterize uniform-subframe-bound frames, in which every given-size subframe has the same spectral behavior; this differs from finding sharp minima and their attaining masks over nonuniform subframes. Haikin, Zamir, and Gavish derive *expected moments* under Bernoulli erasures, a different quantifier from worst-case fixed-cardinality deletion.

The prior exact projective-orbit zero-proportion theorem already implies the qualitative frame-survival threshold \(N-r>g\), since the cyclic orbit contains exactly \(m\) projective rays of multiplicity \(g\). It does not determine any positive retained eigenvalue. In the rank-deficient regime the zero-bound masks and their counts can also be deduced from that ray-multiplicity result. The new portion is the exact *positive-regime* spectral constants and the attaining arc-mask census, unified with their endpoint cases in one formula; the threshold and its singular cases are credited as earlier consequences.

The published two-frequency \(L^1\) concentration formula on finite cyclic groups concerns maxima of pointwise character sums divided by a global \(\ell^1\) norm. The published subgroup-plus-one-point Riesz ratio concerns optimizing exponential basis partners on another finite-group set. Neither statement implies extremal spectra, multiplicity-capped arc masks, or their counts for labelled erasures of a two-row Fourier frame. The elementary polygonal projection ordering used in this proof is not claimed as new; the claimed contribution is its exact, all-count, all-frequency-difference application to the frame erasure spectrum and the complete equality census.

## Limitations
The theorem is specifically for two *unweighted* Fourier rows and ordinary retained-frame spectral bounds. The proof does not provide an optimal reconstruction dual, minimum-error decoder for nonlinear sensing, or an analogous formula for three-row Fourier frames. The exact circle-arrangement lemma is elementary, and a folklore frame-theoretic reformulation or an unindexed equivalent result could exist. The accompanying computations use floating point and do not themselves certify infinitely many dimensions; the mathematical proof is exact.

## References
1. S. Marshall and S. Waldron, *On the number of harmonic frames*, first public arXiv version 2016-11-22, arXiv:1611.07121v1; *Applied and Computational Harmonic Analysis* 48 (2020), 46–63, DOI:10.1016/j.acha.2018.02.004.
2. B. G. Bodmann and V. I. Paulsen, *Frames, graphs and erasures*, arXiv:math/0406134; *Linear Algebra and Its Applications* 404 (2005), 118–146, DOI:10.1016/j.laa.2005.02.016.
3. Q. Cheng, F. Lv, and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, *Linear Algebra and Its Applications* 555 (2018), 186–200, DOI:10.1016/j.laa.2018.05.025.
4. M. Haikin, R. Zamir, and M. Gavish, *Frame Moments and Welch Bound with Erasures*, arXiv:1801.04548v1 (2018).
5. *Exact zero proportion for every two-dimensional finite-group orbit*, published mathematical finding, `2026/10/4/SCOPE-exact-zero-proportion-for-every-two-dimensional-finite-group-orb--26cb02dc2302`.
6. *Exact two-frequency \(L^1\) concentration on every cyclic group*, published mathematical finding, `2026/10/4/SCOPE-exact-two-frequency-l-1-concentration-on-every-cyclic-group--aabfaa5078e3`.
7. *Exact Riesz ratio of the subgroup-plus-one-point family*, published mathematical finding, `2026/10/4/SCOPE-exact-riesz-ratio-of-the-subgroup-plus-one-point-family--1aeaccf87af3`.
