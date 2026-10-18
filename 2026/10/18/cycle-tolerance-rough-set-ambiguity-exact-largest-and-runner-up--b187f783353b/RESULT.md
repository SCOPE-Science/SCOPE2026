# Cycle-tolerance rough-set ambiguity: exact largest and runner-up fibers

## Finding
Let \(n\ge3\), let \(C_n\) be the simple cycle on the labeled vertices \(\mathbb Z/n\mathbb Z\) (the triangle when \(n=3\)), and use its reflexive closed-neighborhood tolerance \(R\). For any vertex subset \(X\), define \(L(X)=\{v:N[v]\subseteq X\}\), \(U(X)=\{v:N[v]\cap X\ne\varnothing\}\), and \(\rho(X)=(L(X),U(X))\). A *fiber* is the set of all \(X\) realizing the same pair. All comparisons below concern distinct **realized** approximation pairs.

Put \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), \(\Lambda_n=F_{n-1}+F_{n+1}\), and define the periodic correction \(\delta(t)=1,0,-1\) according as \(t\equiv0,1,2\pmod3\).

**Theorem (sharp two-tier ambiguity spectrum).** For every \(n\ge3\), the completely uncertain rough observation \(Q_*=(\varnothing,\mathbb Z/n\mathbb Z)\) is the **unique** observation with largest fiber. Its exact multiplicity is
\[
 M_n=|\rho^{-1}(Q_*)|=\Lambda_n+\begin{cases}2,&3\mid n,\\-1,&3\nmid n.\end{cases}
\]
For every \(n\ge7\), the **second-largest distinct fiber multiplicity** is
\[
 S_n=\frac{F_{n-2}+\delta(n-1)}2.
\]
It is attained by **exactly \(2n\)** realized observations: choose one cyclic position and require its neighborhood to be entirely absent (output symbol \(0\)) or entirely present (symbol \(1\)), while every other position is uncertain (symbol \(?\)). No observation with two or more definite positions attains \(S_n\). For \(3\le n\le6\), every noncentral realized fiber is a singleton, so the runner-up multiplicity is \(1\).

In particular, under the uniform distribution on all \(2^n\) vertex subsets, the maximum observation probability is \(M_n/2^n\), the largest noncentral probability is \(S_n/2^n\) for \(n\ge7\), and the ratio \(M_n/S_n\) tends to \(2\sqrt5\,\varphi^2\), with \(\varphi=(1+\sqrt5)/2\).

**Every fiber**, not just the extremal fibers, is computable exactly as a trace of a product of four fixed nonnegative integer matrices, specified below.

## Assumptions and scope
The vertex set is labeled, the cycle is undirected, adjacency is made reflexive, and both approximations use the *same* closed-neighborhood relation. Thus every \(N[v]\) consists of the cyclic three-vertex window centered at \(v\). Distinct rotations of an output count as distinct labeled outputs. The word \(?\) means an uncertain position: it belongs to \(U(X)\setminus L(X)\). No result for arbitrary unicyclic graphs or other radii is asserted.

Index ordered binary states as \(00,01,10,11\). Write \(E_{ij}\) for the matrix with its only \(1\) in row \(i\), column \(j\), in this state order. Define
\[
 A_0=E_{00,00},\qquad A_1=E_{11,11},\qquad
 A_?=\begin{pmatrix}
0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0
\end{pmatrix}.
\]
For any observed cyclic word \(y=(y_1,\ldots,y_n)\in\{0,1,?\}^n\), including unrealizable words, its number of preimages is
\[
 \boxed{\ |\rho^{-1}(y)|=\operatorname{tr}(A_{y_1}A_{y_2}\cdots A_{y_n})\ }.
\]
Here \(\rho^{-1}(y)\) abbreviates the preimage of the lower/upper pair encoded by \(y\).

## Proof
**1. Local channel and cyclic transfer.** If the input subset has indicator bits \(x_i\in\{0,1\}\), its local observation is \(0\) when \((x_{i-1},x_i,x_{i+1})=(0,0,0)\), is \(1\) for \((1,1,1)\), and is \(?\) otherwise. A transition from state \((a,b)\) to \((b,c)\) records precisely one triple, and it contributes to the matrix of its observed symbol. Any cyclic length-\(n\) bitword corresponds bijectively to a length-\(n\) closed walk in the two-bit state graph, including when \(n=3\). Thus the trace formula counts every input once.

**2. Central fiber.** The all-uncertain observation has multiplicity \(M_n=\operatorname{tr}(A_?^n)\). Direct determinant expansion gives
\[
 \det(tI-A_?)=(t^2-t-1)(t^2+t+1).
\]
The first factor's roots are \(\varphi\) and \((1-\sqrt5)/2\), whose \(n\)-th-power sum is the Lucas number \(\Lambda_n\). The other two roots are primitive cube roots of unity, whose \(n\)-th-power sum is \(2\) for multiples of three and \(-1\) otherwise. This proves the exact formula for \(M_n\); the transfer trace also confirms that the central observation is realized for all \(n\ge3\).

**3. An endpoint-path inequality.** Let
\[
 a_t=(A_?^t)_{00,00},\quad b_t=(A_?^t)_{00,11},\quad f_t=\max\{a_t,b_t\},\qquad t\ge0.
\]
For \(t\ge1\), matrix inversion (or substitution in the four-state recurrence) gives the two formal generating series
\[
 \sum_{t\ge0}(a_t+b_t)z^t=\frac{1-z}{1-z-z^2},\qquad
 \sum_{t\ge0}(a_t-b_t)z^t=\frac{1+z}{1+z+z^2}.
\]
Therefore \(a_t+b_t=F_{t-1}\) for \(t\ge1\), \(a_t-b_t=\delta(t)\) for all \(t\ge0\), and
\[
 a_t=\frac{F_{t-1}+\delta(t)}2,\qquad
 f_t=\frac{F_{t-1}+|\delta(t)|}2\quad(t\ge1),\qquad f_0=1.
\]
The matrix \(A_?\) is invariant under swapping zero and one. Choose one of the two endpoint states \(00,11\) giving \(f_p\) paths from \(00\) in \(p\) steps. Starting from that state, bit-complement symmetry gives \(f_q\) paths in \(q\) steps to some endpoint state. Concatenating yields at least \(f_pf_q\) paths from \(00\) to an endpoint in \(p+q\) steps. Hence
\[
 \boxed{f_{p+q}\ge f_pf_q}\qquad(p,q\ge0).
\]
The displayed Fibonacci formula gives \(f_0=1,f_1=0,f_2=f_3=f_4=1\), and \(f_t\) is nondecreasing for \(t\ge2\). For \(n\ge7\),
\[
 a_{n-1}-f_{n-2}
 =\frac{F_{n-4}+\delta(n-1)-|\delta(n-2)|}{2}>0.
\]
The inequality is checked directly at \(n=7,8,9\); for \(n\ge10\), \(F_{n-4}\ge8\) dominates both periodic corrections.

**4. Every noncentral fiber and its strict gap.** If an observation contains \(r\ge1\) definite symbols \(0\) or \(1\), let \(g_1,\ldots,g_r\ge0\) be the counts of consecutive \(?\) symbols in the gaps between them, so \(\sum_i g_i=n-r\). Each definite symbol's matrix is the rank-one projector onto state \(00\) or \(11\). Cyclically rotating the trace yields the **exact** product formula
\[
 |\rho^{-1}(y)|=\prod_{i=1}^r(A_?^{g_i})_{s_i,s_{i+1}},
 \qquad s_i\in\{00,11\},\quad s_{r+1}=s_1.
\]
Each factor is either \(a_{g_i}\) or \(b_{g_i}\) by complement symmetry. Thus repeated application of the endpoint-path inequality gives
\[
 |\rho^{-1}(y)|\le\prod_i f_{g_i}\le f_{n-r}.
\]
If \(r\ge2\) and \(n\ge7\), then \(n-r\le n-2\); the monotonicity of \(f_t\) for \(t\ge2\), together with \(f_0\le f_{n-2}\) and \(f_1\le f_{n-2}\), gives
\[
 |\rho^{-1}(y)|\le f_{n-2}<a_{n-1}.
\]
For \(r=1\), there is one forced state and one uncertain gap of length \(n-1\), so \(|\rho^{-1}(y)|=a_{n-1}\), independently of whether the unique definite symbol is \(0\) or \(1\). This is strictly positive for \(n\ge7\), proving that precisely these \(2n\) outputs attain the runner-up formula.

Finally \(M_n\), the all-uncertain count, is strictly larger than \(a_{n-1}\) for \(n\ge7\): the Lucas formula gives \(M_n\ge\Lambda_n-1\), whereas \(a_{n-1}\le(F_{n-2}+1)/2\), and \(\Lambda_n-1>(F_{n-2}+1)/2\). Consequently the central fiber is uniquely maximal. For the four remaining cycle lengths \(n=3,4,5,6\), direct exhaustive enumeration of respectively \(8,16,32,64\) input subsets gives central sizes \(6,6,10,20\) and shows every other realized observation has one preimage; the complete finite enumeration is replayable in the attached verifier.

**5. Asymptotic separation.** Using \(F_j\sim\varphi^j/\sqrt5\), \(\Lambda_n\sim\varphi^n\), and bounded periodic corrections proves \(M_n/S_n\longrightarrow2\sqrt5\,\varphi^2\).

## Verification
The standalone, dependency-free `verify.py` independently constructs the local observation of every input subset on cycle lengths \(3\) through \(16\) and counts the fibers. It checks that the central output is uniquely maximal for all those cases and that exactly \(2n\) runner-up outputs have the claimed form for \(7\le n\le16\). For \(n\le11\), it also independently computes **every** realized fiber size using the four-state trace formula. Finally it checks the endpoint-path formulas through exponent \(79\) and supermultiplicativity for exponents less than \(35\). Run `python3 verify.py` in the directory containing the embedded file. Finite checks supplement but do not replace the proof for all \(n\).

## Relationship to prior work
The reflexive-relation rough approximations and their order-theoretic study are established in Järvinen--Radeleczki (2023). Qiao and collaborators (2022) study graph-based rough approximation operators rather than sharp inverse-fiber multiplicities. The earlier Järvinen--Radeleczki tolerance representation theorem (2016 preprint) concerns regular Kleene-algebra representations, not cyclic inverse-fiber maxima. The elementary Lucas/Fibonacci trace identity uses the familiar no-monochromatic-three cyclic-word transfer matrix and is not claimed to create new Fibonacci numbers. What is isolated here is the **ranked fiber multiplicity theorem** for this observation map: its unique maximum, exact runner-up, exact classification of runner-up outputs, and nonvanishing asymptotic gap. Previously studied analogous path and tree observation maps do not imply the cyclic result, since the additional cycle edge imposes a global parity constraint on crossing-edge patterns.

## Limitations
This is a theorem only for binary vertex subsets of reflexive simple cycles. It neither classifies all attainable nonextremal fiber sizes nor proves an optimal universal bound for arbitrary graphs. The theorem has undergone self-review but **not independent external audit**. Although mathematical-record and literature comparisons were performed, an earlier equivalent cyclic three-symbol-channel result might exist under other terminology; publication priority is not certified.

## References
1. J. Järvinen and S. Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, arXiv:2304.05641 (first publicly posted 2023-04-12), full preprint, https://arxiv.org/pdf/2304.05641 .
2. S. Qiao et al., *Rough Set Analysis of Graphs*, Filomat **36** (2022), 3331--3354, https://www.pmf.ni.ac.rs/filomat-content/2022/36-10/36-10-12-13614.pdf .
3. J. Järvinen and S. Radeleczki, *Representing regular pseudocomplemented Kleene algebras by tolerance-based rough sets*, arXiv:1610.09847 (2016-10-31), https://arxiv.org/pdf/1610.09847 .
