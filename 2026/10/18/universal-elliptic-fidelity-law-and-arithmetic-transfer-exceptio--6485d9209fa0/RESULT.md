# Exact fidelity ceiling at odd–odd resonances of the static rhombic chain

## Finding

Consider the static staggered-flux rhombic chain of Li et al. [1]. Its two local angular frequencies are \(\omega_\pm=J\sqrt{4\pm2\cos(\phi/2)}\). Suppose \(\omega_-/\omega_+=p/q<1\) is reduced with both \(p,q\) odd. Let \(a,b>0\) be the unique solution of
\[
qa+pb=\pi,\qquad p\sin a=q\sin b.
\]
Then the optimal static transfer probability between the adjacent hubs of the \(\phi\)-plaquette is attained and is exactly
\[
P_{\max}=\left(\frac{\cos a+\cos b}{2}\right)^2<1.
\]
Uniformly over admissible odd–odd resonances as \(q\to\infty\), its infidelity is
\[
1-P_{\max}=\frac{\pi^2}{2(p^2+q^2)}+O(q^{-4}).
\]
At the degenerate endpoint \(p=q=1\) the transfer probability is identically zero. The result determines the largest threshold attainable at each obstructed resonance, rather than merely detecting the absence of exact transfer.

## Assumptions and scope

The infinite, one-particle Hermitian rhombic chain has sites \(A_n\), \(n\in\mathbb Z\), and two arm sites \(B_n,C_n\) between \(A_n,A_{n+1}\). Onsite terms vanish. Fix \(J>0\); use hoppings \(H_{A_n,B_n}=H_{A_n,C_n}=H_{A_{n+1},B_n}=J\) and \(H_{A_{n+1},C_n}=Je^{i\phi_n}\), with conjugate reverse hoppings. Here \(\phi_n=\phi\in[0,\pi]\) for even \(n\) and \(\phi_n=\pi\) for odd \(n\). The launch and target are \(A_0,A_1\); probability is \(|\langle A_1|e^{-itH}|A_0\rangle|^2\). Time is continuous and the flux is held fixed. The result does not cover noise, switched flux, many-particle dynamics, or finite observation-time statistics. For admissible nondegenerate odd–odd ratios, \(1/\sqrt 3\le p/q<1\) implies \(q>p\ge3\).

## Proof

**Reduction.** The \(A\)-sector of \(H^2\) has diagonal \(4J^2\) and hub-to-hub coupling \(J^2(1+e^{-i\phi_n})\), which vanishes on every odd bond. Its block on \((A_0,A_1)\) has eigenvalues \(\omega_-^2,\omega_+^2\). Bipartiteness annihilates the hub-to-hub block of odd powers; the matrix cosine on this block gives the known probability
\[
P(t)=\tfrac14[\cos(p\theta)-\cos(q\theta)]^2,
\qquad \theta=\omega_+t/q.
\]
At \(\phi=\pi\) the block is scalar and \(P(t)=0\).

**Sharp reduction to a line segment.** For any \(\theta\), choose nearest integer phase targets \(\pi u\) for \(p\theta\) and \(\pi v\) for \(q\theta\) with opposite parity: make the first target even if \(\cos(p\theta)\ge\cos(q\theta)\), and odd otherwise. The unsigned errors \(a_0=|p\theta-\pi u|\), \(b_0=|q\theta-\pi v|\) lie in \([0,\pi]\), and \(2\sqrt{P}=\cos a_0+\cos b_0\). The integer \(qu-pv\) is odd, so cancellation of the two exact phases gives \(qa_0+pb_0\ge\pi\). Shrinking both errors by the same factor to equality can only increase the cosine sum. Thus the maximum of the sum on the segment \(a,b\ge0,\ qa+pb=\pi\) gives an upper bound.

In fact every point on the segment is realized. Coprimality gives integers \(u,v\) with \(qu-pv=1\), necessarily of opposite parity. Adding \((p,q)\) if necessary makes \(u\) even and \(v\) odd. The equations \(p\theta=\pi u-a\) and \(q\theta=\pi v+b\) are consistent exactly because \(qa+pb=\pi\). Add an integer multiple of \(2\pi\) to \(\theta\) for nonnegative time. On this segment both cosines are positive, since \(a\le\pi/q\) and \(b\le\pi/p\le\pi/3\). Thus this phase attains the probability corresponding to the chosen errors.

**Optimization.** On that segment the cosine sum as a function of \(a\in[0,\pi/q]\), with \(b=(\pi-qa)/p\), has strictly negative second derivative \(-\cos a-(q/p)^2\cos b\). Its first derivative goes from \((q/p)\sin(\pi/p)>0\) to \(-\sin(\pi/q)<0\). Therefore its unique maximum is the stated interior solution and is strictly less than two. For the large-denominator estimate, all segment points have \(a,b=O(q^{-1})\) uniformly over the flux interval. There
\[
1-[(\cos a+\cos b)/2]^2=\tfrac12(a^2+b^2)+O(q^{-4}).
\]
The least squared length on the segment is \(\pi^2/(p^2+q^2)\), attained at the orthogonal projection \((a,b)=\pi(q,p)/(p^2+q^2)\). Bounding the minimum of the infidelity below on the whole segment and above at this projection proves the uniform expansion.

## Relationship to prior work

Li et al. [1, p. 3] give the two-frequency local amplitude and opposite-parity tuning for perfect transfer. The general phase-alignment mechanism for pretty-good transfer is also prior [2]. Neither perfect-transfer solvability nor the existence of a positive gap for each obstructed periodic orbit is claimed here as new. The result concerns the exact gap, including the attainability of the optimal error allocation for the odd–odd orbit. The generic irrational time law is not part of this finding: its distribution is the square of the classical square-lattice structure-function law [3, Eqs. (2), (4)] and has the standard product-beta density [4, §5.1] after torus equidistribution is applied to the known amplitude.

## Verification

The attached standard-library `verify.py` checks the attainment phases, stationary condition, and agreement with finite independent phase-grid lower bounds for admissible sample pairs. It also checks the large-denominator estimate on a sample sequence. The proof establishes the exact all-time optimum and the uniform remainder; the checks are supplementary.

## References

1. H. Li et al., *Engineering topological chiral transport in a flat-band lattice of ultracold atoms*, arXiv:2401.03611v1 (2024), https://arxiv.org/abs/2401.03611.
2. L. Vinet and A. Zhedanov, *Almost perfect state transfer in quantum spin chains*, arXiv:1205.4680v3, https://arxiv.org/abs/1205.4680.
3. A. J. Guttmann, *Lattice Green functions in all dimensions*, arXiv:1004.1435, https://arxiv.org/abs/1004.1435.
4. C. F. Dunkl, *Products of Beta distributed random variables*, arXiv:1304.6671v1 (2013), https://arxiv.org/abs/1304.6671.
