# Exact metastable-energy census for asynchronous minority dynamics on circular prisms

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the circular prism with two labelled layers and \(n\) cyclically labelled rungs. Consider the one-vertex-at-a-time, uniformly sampled binary minority rule **with the selected vertex included in its own neighborhood**, retaining its previous state in the event of a tie. Write \(m(c)\) for the number of monochromatic (equal-spin) edges of a configuration \(c\). The polynomial enumerating absorbing configurations according to their edge energy is exactly
\[
A_n(z)=2\sum_{\substack{0\le k\le\lfloor n/2\rfloor\\k\equiv n\pmod2}}
\frac{n}{n-k}\binom{n-k}{k}z^{2k}
+2\mathbf 1_{2\mid n}z^n.
\]
Every recurrent communicating class is a singleton absorbing state. In particular, writing \(L_n=\varphi^n+\psi^n\) for the Lucas number with \(\varphi=(1+\sqrt5)/2\) and \(\psi=(1-\sqrt5)/2\), the complete attractor count is
\[
A_n(1)=L_n+2\cos(2\pi n/3)+2\mathbf1_{2\mid n}.
\]
The globally minimal monochromatic-edge energy is \(0\), with exactly two ground configurations, for even \(n\); for odd \(n\) it is \(2\), with exactly \(2n\) ground configurations. If \(T\) is the first hitting time of the absorbing set, then for every initial configuration, \(\mathbb E[T]\le6n^2\).

## Assumptions and scope
The vertex set is \(\{(i,r):i\in\mathbb Z/n\mathbb Z,\ r\in\{0,1\}\}\). Each \((i,r)\) has exactly three distinct neighbors \((i-1,r)\), \((i+1,r)\), and \((i,1-r)\). The restriction \(n\ge3\) ensures this is a simple cubic graph. State bits are in \(\{0,1\}\). At each step one of the \(2n\) vertices is selected independently and uniformly. Its update is the minority of the four bits consisting of its three neighbors and itself; in an exact tie its own bit is retained. \(m(c)\) counts undirected edges only once, so \(0\le m(c)\le3n\). \(A_n(z)=\sum_{c\text{ absorbing}}z^{m(c)}\), counting labelled configurations without quotienting by graph automorphisms.

## Proof
**Strict descent.** Let \(s\) be the number of neighbors agreeing with the fired vertex. By the specified closed-neighborhood minority rule, a flip occurs exactly when \(s\ge2\). Such a flip changes \(m(c)\) by \((3-s)-s=3-2s\le-1\). Therefore any actual change strictly decreases the nonnegative integer \(m(c)\). An absorbing configuration is exactly a coloring in which every vertex has at most one same-colored neighbor. Hence there are no nontrivial recurrent classes. From every nonabsorbing configuration, the probability of a state-changing update at each trial is at least \(1/(2n)\), so the conditional expected wait for a change is at most \(2n\). There can be at most \(3n\) changes; summing conditional waiting expectations gives \(\mathbb E[T]\le6n^2\).

**Rung dichotomy.** Write \(u_i\) and \(v_i\) for upper- and lower-layer bits. If for any rung \(i\) we have \(u_i=v_i\), its vertical edge is monochromatic. Stability forces both horizontal neighbors in **each** layer to carry the opposite spin. Thus \(u_{i\pm1}=v_{i\pm1}=1-u_i\). Induction around the ring forces all rungs monochromatic and their common spins alternating. This is possible only when \(n\) is even, and gives exactly two configurations, each with \(m(c)=n\) (all vertical edges monochromatic and no horizontal ones).

Every remaining absorbing configuration has all rungs bichromatic: \(v_i=1-u_i\) for all \(i\). Put \(x_i=u_i\) and let \(Z=\{i:x_i=x_{i+1}\}\) be the set of same-spin horizontal transitions. Since the vertical neighbor is opposite, stability at \((i,0)\) holds precisely when not both \(x_{i-1}=x_i\) and \(x_i=x_{i+1}\). The same condition holds in the lower layer. Therefore \(Z\) is an independent set of edge positions on the cycle. Write \(k=|Z|\). Among the \(n\) cyclic transitions, exactly \(n-k\) flip the bit, so cyclic consistency requires \(n-k\) to be even, equivalently \(k\equiv n\pmod2\). Conversely, every independent \(Z\) satisfying this parity constraint determines exactly two cyclic spin strings \(x\) (a starting bit and its global complement), hence exactly two absorbing configurations. Each equality transition makes one monochromatic horizontal edge in *both* layers, so \(m(c)=2k\).

The number of independent \(k\)-subsets of positions on a cycle of length \(n\) is \(\frac{n}{n-k}\binom{n-k}{k}\), including \(k=0\). One proof for \(k\ge1\) counts circular placements of \(k\) occupied sites separated by at least one vacant site: choose positive cyclic gaps summing to \(n-k\), give a marked occupied site, and divide by \(k\); the resulting number is \(\frac nk\binom{n-k-1}{k-1}\), equal to the displayed binomial expression. Adding the two coherent-rung states proves the energy polynomial.

**Lucas reduction and ground states.** Let \(I_n(t)=\sum_{Z\text{ independent in }C_n}t^{|Z|}\). The parity-constrained contribution at \(z=1\) equals \(I_n(1)+(-1)^n I_n(-1)\). The standard cycle transfer matrix gives \(I_n(t)=\lambda_+(t)^n+\lambda_-(t)^n\), where \(\lambda_\pm(t)\) solve \(\lambda^2=\lambda+t\). Consequently \(I_n(1)=L_n\) and \(I_n(-1)=2\cos(n\pi/3)\); since \((-1)^n\cos(n\pi/3)=\cos(2\pi n/3)\), the claimed formula follows. For even \(n\), parity allows \(k=0\), realized by the two proper bipartite colorings. For odd \(n\), parity forces \(k\ge1\); exactly \(n\) possible singleton sets and two global bit choices give \(2n\) ground states with \(m(c)=2\). No coherent-rung states exist for odd \(n\).

## Verification
The accompanying self-contained Python script `verify_prism.py` independently enumerates all \(2^{2n}\) labelled configurations for each \(3\le n\le9\). It applies the local update inequality vertex by vertex, directly counts equal-spin edges, and compares the resulting energy histogram with the stated coefficient formula. Its actual output is stored in `verified_output.txt`. The total counts for \(n=3,4,5,6,7,8,9\) are respectively \(6,8,10,22,28,48,78\). The proof above, rather than this finite check, establishes the theorem for all \(n\ge3\).

## Relationship to prior work
Regnault, Schabanel, and Thierry (2007) analyze asynchronous minority on two-dimensional tori with four neighbor sites and classify stable checkerboard bands under that different graph/neighborhood. Wacław and Burda (2008) study single-spin metastability of Ising **spin glasses with random Gaussian edge couplings**, including asymptotic estimates for infinite ladders; their random-coupling diagrammatics does not furnish this finite, uniform antiferromagnetic prism energy polynomial. Rouquier, Regnault, and Thierry (2010) establish the general minority update model and an energy principle: odd-degree vertices cannot keep flipping in recurrent behavior. The strict descent and absorption conclusion above are instances of that principle, not claimed as new on their own. The contribution examined here is the **full energy-resolved, exact, finite-volume absorbing-state census**, including its mod-six correction and ground-state multiplicities, for the simple cubic circular ladder.

## Limitations
The bound \(6n^2\) is a general sufficient estimate, not asserted optimal; no basin-size distribution, finite-time law, or exact expected absorption time is established. The census treats labelled vertices and the specified closed-neighborhood tie convention only. Literature comparisons cannot rule out an unindexed equivalent formula for one-spin-stable circular-ladder colorings.

## References
1. D. Regnault, N. Schabanel, É. Thierry, *Progresses in the Analysis of Stochastic 2D Cellular Automata: a Study of Asynchronous 2D Minority*, first posted 2007-06-17, arXiv:0706.2479, https://arxiv.org/abs/0706.2479.
2. B. Wacław, Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, first posted 2008-01-08, arXiv:0801.1224, https://arxiv.org/abs/0801.1224.
3. J.-B. Rouquier, D. Regnault, É. Thierry, *Stochastic Minority on Graphs*, first posted 2010-11-23, arXiv:1011.5119, https://arxiv.org/abs/1011.5119.
