# Perrin attractor census and quadratic absorption bound for stochastic minority on wheels

## Finding
For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) have \(n\) labelled rim vertices and one hub. Under *uniform asynchronous closed-neighborhood minority* (one vertex selected uniformly at each discrete step, changing its bit to the minority of its closed neighborhood, with ties retaining the bit), define the Perrin sequence by \(P_0=3\), \(P_1=0\), \(P_2=2\), \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\). The finite Markov chain has exactly \(2P_n\) recurrent states. If \(n\) is odd, all \(2P_n\) are absorbing singleton classes. If \(n\) is even, there are precisely \(2P_n-4\) absorbing singleton classes and exactly two recurrent classes of size two, with each nontrivial class obtained by flipping only the hub while the rim alternates.

More precisely, for each choice of hub bit and each integer \(z\), the number of recurrent configurations with exactly \(z\) rim vertices agreeing with the hub is
\[
B(n,z)=\begin{cases}\displaystyle\frac{n}{z}\binom{z}{n-2z},&\lceil n/3\rceil\le z\le\lfloor n/2\rfloor,\\0,&\text{otherwise.}\end{cases}
\]
Among these, precisely the \(z=n/2\) configurations (possible only for even \(n\)) are nonabsorbing.

Let \(E(c)=2\#\{uv\in E(W_n):c_u=c_v\}\), and let \(T\) be the first time the chain enters its recurrent set. For *every* initial configuration \(c\),
\[
\mathbb E_c[T]\le\frac32(n+1)E(c)\le6n(n+1).
\]
The asymptotic recurrent-state count is \(2P_n\sim2\rho^n\), where \(\rho\approx1.324717957\) is the real root of \(\rho^3-\rho-1=0\). Thus the fraction of all states that are recurrent equals \(P_n/2^n\) and tends to zero exponentially.

## Assumptions and scope
The graph is simple and undirected, the rim is a labelled simple \(n\)-cycle with \(n\ge3\), and every rim vertex has degree three. Update selections are independent and uniform over all \(n+1\) vertices. Every closed neighborhood includes the selected vertex itself. If the two bit counts in that neighborhood are equal, the selected vertex retains its state. A recurrent class means a closed communicating class of the associated finite Markov chain; self-loops from unchanged updates are included. The statements do not concern simultaneous updates, open-neighborhood minority, biased selection, or arbitrary wheel-like graphs.

## Proof
**Energy and the one-neutral-vertex principle.** Write \(s_v(c)\) for the number of *other* neighbors of vertex \(v\) with the same bit. A vertex of degree \(d_v\) flips precisely when \(2s_v(c)>d_v-1\). Flipping it changes the monochromatic-edge energy by
\[
E(c^{(v)})-E(c)=2(d_v-2s_v(c)).
\]
For odd \(d_v\), every legal flip strictly decreases \(E\) by at least two. For even \(d_v\), a legal flip is energy-neutral exactly when \(s_v(c)=d_v/2\); every other legal flip also decreases \(E\) by at least two. The \(n\) rim degrees are odd. Therefore the only possible energy-neutral flip, when there is one, is at the even-degree hub (so \(n\) must be even). Every energy-neutral hub flip is reversible, and two consecutive such flips return to the original state. No rim vertex can flip within a communicating recurrent class, since a strict energy drop cannot be undone.

**Local structure of recurrent configurations.** Fix hub bit \(h\). Encode a rim bit by \(0\) if it equals \(h\) and by \(1\) otherwise. A rim vertex is inactive if and only if it has at most one same-colored neighbor among its three ordinary neighbors. Hence every \(0\) must have two neighboring \(1\)'s, and every \(1\) must not have two neighboring \(1\)'s. Equivalently, the cyclic rim word contains neither \(00\) nor \(111\), where these forbidden patterns are understood cyclically. Such words consist of \(z\ge1\) zeros, each followed by one or two ones. In particular \(2z\le n\le3z\).

The hub has exactly \(z\) agreeing neighbors. If \(n\) is odd then \(z\le\lfloor n/2\rfloor\), making the hub inactive. If \(n\) is even, it is inactive unless \(z=n/2\), which forces every interzero gap to have length one, i.e. the rim must alternate. In that alternating case the hub flips neutrally when selected and both hub bits leave the rim inactive. These two hub states form a closed communicating pair. There are exactly two labelled alternating rim words, giving precisely two such pairs. Conversely, if an energy-neutral hub pair is recurrent, every rim vertex must be inactive for **both** hub values. Each rim vertex matches one of those hub values, so its two rim neighbors must both disagree with it. Thus its rim must alternate. No other recurrent classes are possible. All nonalternating valid words give absorbing singletons.

**Weighted enumeration.** For \(z\) labelled cyclic zeros, let \(j=n-2z\) be the number of interzero gaps of length two; the other \(z-j\) gaps have length one. Counting pairs consisting of a labelled rim word and a distinguished zero gives both \(zB(n,z)\) and \(n\binom zj\): choose the distinguished zero's position in \(n\) ways and choose the \(j\) long gaps among the \(z\) successive gaps. This proves the displayed formula for \(B(n,z)\).

The total \(\sum_z B(n,z)\) is the number of cyclic binary words avoiding \(00\) and \(111\). Their unique cyclic state presentation uses states \(A=0\), \(B=01\), \(C=011\), with allowed transitions \(A\to B\), \(B\to A\), \(B\to C\), \(C\to A\). Its adjacency matrix is
\[
M=\begin{pmatrix}0&1&0\\1&0&1\\1&0&0\end{pmatrix}.
\]
Thus the number is \(\operatorname{tr}(M^n)\). The characteristic polynomial is \(\lambda^3-\lambda-1\), so Cayley–Hamilton gives \(\operatorname{tr}(M^n)=\operatorname{tr}(M^{n-2})+\operatorname{tr}(M^{n-3})\). Initial traces are \(3,0,2\). Therefore this count equals \(P_n\). There are two choices of hub bit. The two alternating rim words produce four nonabsorbing recurrent states when \(n\) is even; otherwise every recurrent state is absorbing. This proves the complete census and the weighted formula. The eigenvalue equation also gives \(P_n=\rho^n+O(\rho^{-n/2})\), since the other two eigenvalues are complex conjugates of modulus \(\rho^{-1/2}\).

**Uniform expected hitting time.** Let \(N=n+1\). At any energy level, every actual state change is either a strict energy decrease or an energy-neutral hub flip. Without an energy-neutral hub flip, a nonrecurrent configuration has an available strict decrease, whose selection occurs within expected time at most \(N\). When the hub flip is neutral, there are at most two states on the current energy plateau, differing only at the hub. Write \(a,b\) for the numbers of active rim vertices in these states. If \(a=b=0\), the pair is already a closed recurrent class. Otherwise \(a+b\ge1\). Let \(e_0,e_1\) be the expected times to the first strict energy decrease starting from either plateau state; accounting for self-loops and the single neutral hub flip gives
\[
(a+1)e_0=N+e_1,\qquad (b+1)e_1=N+e_0.
\]
Consequently
\[
e_0=\frac{N(b+2)}{ab+a+b},\qquad e_1=\frac{N(a+2)}{ab+a+b},
\]
so \(\max(e_0,e_1)\le3N\) for all nonnegative integers \(a,b\) with \(a+b\ge1\). Every strict energy decrease lowers the nonnegative, even-valued \(E\) by at least two. Applying the strong Markov property after each strict decrease therefore bounds the expected time before entering a recurrent plateau by \(3N E(c)/2\). Finally, the wheel has \(2n\) edges, hence \(E(c)\le4n\). This proves the uniform quadratic bound and almost-sure absorption.

## Verification
The accompanying standard-library-only `CHECK.py` constructs every possible single-site update on each labelled wheel with \(3\le n\le11\), enumerates sink strongly connected components, and checks their sizes, hub-pair structure and refined \(z\)-profile against the formulas. The recorded output is `CHECK.out`. This is an independent finite consistency test only: the proof above, not the enumeration, establishes all \(n\) and the expected-time inequality. The weighted formula, transfer-matrix identity and plateau exit-time equations can also be checked symbolically from the displayed expressions.

## Relationship to prior work
Rouquier, Regnault and Thierry (2010) define exactly the asynchronous closed-neighborhood minority rule used here; their general energy monotonicity and odd-degree observations are premises. They classify the limit sets for cliques and cycles/paths and give an \(O(N^3)\) expected hitting bound for cycles/paths, as well as exponentially slow tree constructions. The wheel-specific complete recurrent-class census, weighted profile and uniform \(O(n^2)\) absorption inequality are not stated in the inspected portions of that work. The Perrin sequence and its interpretation as the number of maximal independent sets of \(C_n\) are already known (OEIS A001608); the sequence itself is not claimed as new. The additional dynamics concern which states are transient, which recurrent states are absorbing versus hub-flipping, and their stochastic hitting times. Related work on synchronous wheel-majority dynamics uses the opposite update direction and synchronous updates, so it does not imply this classification.

## Limitations
The bound \(6n(n+1)\) is an upper bound, not claimed to be sharp; no distribution of hitting times or probabilities of selecting particular recurrent classes is determined. The Perrin enumeration is known combinatorially; originality is limited to its dynamical interpretation together with the complete stochastic attractor and time-to-attractor statements. Literature search is necessarily bounded, and an unindexed equivalent result remains possible. Finite checks through eleven rim vertices cannot establish an infinite theorem by themselves.

## References
1. J.-B. Rouquier, D. Regnault, and E. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119 (first submitted 2010-11-23), https://arxiv.org/abs/1011.5119. Relevant material: model Definitions 1–6, Lemma 1, Corollary 1, Theorems 4.1–4.2, and the discussion of slow tree examples.
2. OEIS Foundation, *A001608: Perrin sequence*, https://oeis.org/A001608. Known cyclic maximal-independent-set interpretation and plastic-constant asymptotics.
3. AMS, *Mathematics Subject Classification 2020*, category 37B15 (dynamical aspects of cellular automata), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=37B52.
